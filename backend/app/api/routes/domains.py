import logging
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc, and_
from typing import List

from app.core.db import get_db
from app.api.deps import get_current_user
from app.models.domain import Domain
from app.models.user import User
from app.schemas.domain import DomainCreate, DomainOut, DomainUpdate
from app.services.dns_service import DNSService
from app.services.verification_service import generate_verification_token, verification_txt_value
from app.services.audit_service import audit_log
from app.core.cache import CacheService

router = APIRouter(prefix="/api", tags=["domains"])
logger = logging.getLogger(__name__)
dns_service = DNSService()

@router.get("/domains", response_model=List[DomainOut])
def list_domains(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    status_filter: str = Query(None)
):
    """List user's domains with pagination"""
    cache_key = f"domains:{current_user.id}:{skip}:{limit}"
    cached = CacheService.get(cache_key)
    if cached:
        return cached
    
    query = db.query(Domain).filter(Domain.user_id == current_user.id)
    
    if status_filter:
        query = query.filter(Domain.status == status_filter)
    
    domains = query.order_by(desc(Domain.created_at)).offset(skip).limit(limit).all()
    
    CacheService.set(cache_key, domains, ttl=300)
    return domains

@router.post("/domains", response_model=DomainOut, status_code=status.HTTP_201_CREATED)
async def create_domain(
    payload: DomainCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new domain"""
    # Validate domain name
    if not payload.is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid domain name format"
        )
    
    domain_name = payload.name.strip().lower()
    
    # Check if domain already exists
    existing = db.query(Domain).filter(Domain.name == domain_name).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Domain already registered in system"
        )
    
    # Generate verification token
    verification_token = generate_verification_token()
    
    # Create domain
    domain = Domain(
        user_id=current_user.id,
        name=domain_name,
        status="pending",
        verification_method="txt",
        verification_token=verification_token,
        verification_value=verification_txt_value(verification_token),
        dns_status="unknown"
    )
    db.add(domain)
    db.commit()
    db.refresh(domain)
    
    # Create zone in PowerDNS
    try:
        await dns_service.create_zone(domain_name)
        domain.dns_status = "ready"
        db.commit()
    except Exception as e:
        logger.error(f"Failed to create DNS zone for {domain_name}: {str(e)}")
        domain.dns_status = "error"
        db.commit()
    
    audit_log(db, current_user.id, "domain_created", {"domain": domain_name})
    CacheService.delete(f"domains:{current_user.id}:*")
    
    return domain

@router.get("/domains/{domain_id}", response_model=DomainOut)
def get_domain(
    domain_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get domain details"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    return domain

@router.put("/domains/{domain_id}", response_model=DomainOut)
def update_domain(
    domain_id: int,
    payload: DomainUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update domain settings"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    if payload.auto_renew is not None:
        domain.auto_renew = payload.auto_renew
    if payload.auto_ptr is not None:
        domain.auto_ptr = payload.auto_ptr
    if payload.notes is not None:
        domain.notes = payload.notes
    
    domain.updated_at = datetime.utcnow()
    db.commit()
    
    audit_log(db, current_user.id, "domain_updated", {"domain_id": domain_id})
    CacheService.delete(f"domains:{current_user.id}:*")
    
    return domain

@router.delete("/domains/{domain_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_domain(
    domain_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete domain"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    # Delete zone from PowerDNS
    try:
        await dns_service.delete_zone(domain.name)
    except Exception as e:
        logger.error(f"Failed to delete DNS zone {domain.name}: {str(e)}")
    
    db.delete(domain)
    db.commit()
    
    audit_log(db, current_user.id, "domain_deleted", {"domain": domain.name})
    CacheService.delete(f"domains:{current_user.id}:*")
    
    return None

@router.post("/domains/{domain_id}/verify")
async def verify_domain(
    domain_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Verify domain ownership"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    # Verify TXT record
    is_verified = await dns_service.verify_txt_record(
        domain.name,
        domain.verification_value
    )
    
    if is_verified:
        domain.status = "verified"
        domain.verified_at = datetime.utcnow()
        db.commit()
        audit_log(db, current_user.id, "domain_verified", {"domain": domain.name})
        CacheService.delete(f"domains:{current_user.id}:*")
        return {"status": "verified", "message": "Domain ownership verified"}
    else:
        return {"status": "pending", "message": "TXT record not found or incorrect"}

@router.get("/domains/{domain_id}/verification")
def get_verification_info(
    domain_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get domain verification information"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    return {
        "domain": domain.name,
        "status": domain.status,
        "method": domain.verification_method,
        "record_name": f"_personaldns.{domain.name}",
        "record_value": domain.verification_value,
        "record_type": "TXT"
    }
