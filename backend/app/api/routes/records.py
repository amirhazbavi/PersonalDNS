import logging
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc, and_
from typing import List

from app.core.db import get_db
from app.api.deps import get_current_user
from app.models.domain import Domain
from app.models.record import DNSRecord
from app.models.user import User
from app.schemas.record import RecordCreate, RecordOut, RecordUpdate, RECORD_TYPES
from app.services.dns_service import DNSService
from app.services.audit_service import audit_log
from app.core.cache import CacheService

router = APIRouter(prefix="/api", tags=["records"])
logger = logging.getLogger(__name__)
dns_service = DNSService()

@router.get("/domains/{domain_id}/records", response_model=List[RecordOut])
def list_records(
    domain_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    record_type: str = Query(None)
):
    """List DNS records for a domain"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    cache_key = f"records:{domain_id}:{skip}:{limit}:{record_type}"
    cached = CacheService.get(cache_key)
    if cached:
        return cached
    
    query = db.query(DNSRecord).filter(DNSRecord.domain_id == domain_id)
    
    if record_type and record_type in RECORD_TYPES:
        query = query.filter(DNSRecord.record_type == record_type.upper())
    
    records = query.order_by(desc(DNSRecord.created_at)).offset(skip).limit(limit).all()
    
    CacheService.set(cache_key, records, ttl=300)
    return records

@router.post("/domains/{domain_id}/records", response_model=RecordOut, status_code=status.HTTP_201_CREATED)
async def create_record(
    domain_id: int,
    payload: RecordCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new DNS record"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    if domain.status != "verified":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Domain must be verified before adding records"
        )
    
    # Validate record
    try:
        payload.validate()
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
    # Create record
    record = DNSRecord(
        domain_id=domain.id,
        name=payload.name.lower(),
        record_type=payload.record_type.upper(),
        content=payload.content,
        ttl=payload.ttl,
        priority=payload.priority,
        weight=payload.weight,
        port=payload.port,
        enabled=payload.enabled
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    
    # Update in PowerDNS
    try:
        fqdn = f"{payload.name}.{domain.name}" if payload.name != "@" else domain.name
        await dns_service.upsert_record(
            zone_name=domain.name,
            record_name=fqdn,
            record_type=payload.record_type.upper(),
            content=payload.content,
            ttl=payload.ttl,
            priority=payload.priority
        )
        record.synced_at = datetime.utcnow()
        db.commit()
    except Exception as e:
        logger.error(f"Failed to sync record to DNS: {str(e)}")
        record.enabled = False
        db.commit()
    
    audit_log(
        db, current_user.id, "record_created",
        {"domain": domain.name, "name": payload.name, "type": payload.record_type}
    )
    CacheService.delete(f"records:{domain_id}:*")
    
    return record

@router.get("/domains/{domain_id}/records/{record_id}", response_model=RecordOut)
def get_record(
    domain_id: int,
    record_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific DNS record"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    record = db.query(DNSRecord).filter(
        and_(DNSRecord.id == record_id, DNSRecord.domain_id == domain_id)
    ).first()
    
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )
    
    return record

@router.put("/domains/{domain_id}/records/{record_id}", response_model=RecordOut)
async def update_record(
    domain_id: int,
    record_id: int,
    payload: RecordUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a DNS record"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    record = db.query(DNSRecord).filter(
        and_(DNSRecord.id == record_id, DNSRecord.domain_id == domain_id)
    ).first()
    
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )
    
    # Update fields
    record.content = payload.content
    record.ttl = payload.ttl
    record.priority = payload.priority
    record.weight = payload.weight
    record.port = payload.port
    record.enabled = payload.enabled
    record.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(record)
    
    # Sync to PowerDNS
    try:
        fqdn = f"{record.name}.{domain.name}" if record.name != "@" else domain.name
        await dns_service.upsert_record(
            zone_name=domain.name,
            record_name=fqdn,
            record_type=record.record_type,
            content=payload.content,
            ttl=payload.ttl,
            priority=payload.priority
        )
        record.synced_at = datetime.utcnow()
        db.commit()
    except Exception as e:
        logger.error(f"Failed to sync record to DNS: {str(e)}")
    
    audit_log(
        db, current_user.id, "record_updated",
        {"domain": domain.name, "record_id": record_id}
    )
    CacheService.delete(f"records:{domain_id}:*")
    
    return record

@router.delete("/domains/{domain_id}/records/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_record(
    domain_id: int,
    record_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a DNS record"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    record = db.query(DNSRecord).filter(
        and_(DNSRecord.id == record_id, DNSRecord.domain_id == domain_id)
    ).first()
    
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )
    
    # Delete from PowerDNS
    try:
        fqdn = f"{record.name}.{domain.name}" if record.name != "@" else domain.name
        await dns_service.delete_record(
            zone_name=domain.name,
            record_name=fqdn,
            record_type=record.record_type
        )
    except Exception as e:
        logger.error(f"Failed to delete record from DNS: {str(e)}")
    
    db.delete(record)
    db.commit()
    
    audit_log(
        db, current_user.id, "record_deleted",
        {"domain": domain.name, "record_id": record_id}
    )
    CacheService.delete(f"records:{domain_id}:*")
    
    return None

@router.post("/domains/{domain_id}/records/{record_id}/toggle")
def toggle_record(
    domain_id: int,
    record_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Toggle record enabled/disabled status"""
    domain = db.query(Domain).filter(
        and_(Domain.id == domain_id, Domain.user_id == current_user.id)
    ).first()
    
    if not domain:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Domain not found"
        )
    
    record = db.query(DNSRecord).filter(
        and_(DNSRecord.id == record_id, DNSRecord.domain_id == domain_id)
    ).first()
    
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )
    
    record.enabled = not record.enabled
    db.commit()
    
    audit_log(
        db, current_user.id, "record_toggled",
        {"domain": domain.name, "record_id": record_id, "enabled": record.enabled}
    )
    CacheService.delete(f"records:{domain_id}:*")
    
    return {"enabled": record.enabled}
