import logging
import secrets
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List

from app.core.db import get_db
from app.core.security import hash_password, generate_api_key
from app.api.deps import get_current_user
from app.models.api_key import APIKey
from app.models.user import User
from app.schemas.api_key import APIKeyCreate, APIKeyOut
from app.services.audit_service import audit_log
from app.core.cache import CacheService

router = APIRouter(prefix="/api", tags=["api_keys"])
logger = logging.getLogger(__name__)

@router.get("/api-keys", response_model=List[APIKeyOut])
def list_api_keys(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """List user's API keys"""
    keys = db.query(APIKey).filter(
        APIKey.user_id == current_user.id
    ).order_by(desc(APIKey.created_at)).offset(skip).limit(limit).all()
    
    return keys

@router.post("/api-keys", response_model=APIKeyOut, status_code=status.HTTP_201_CREATED)
def create_api_key(
    payload: APIKeyCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create new API key"""
    # Generate key
    api_key_value = generate_api_key()
    api_key_hash = hash_password(api_key_value)
    
    # Create key object
    api_key = APIKey(
        user_id=current_user.id,
        name=payload.name,
        key_hash=api_key_hash,
        scopes=payload.scopes,
        is_active=True,
        revoked=False
    )
    db.add(api_key)
    db.commit()
    db.refresh(api_key)
    
    # Return with actual key (only shown once)
    result = APIKeyOut.model_validate(api_key)
    result.key = api_key_value
    
    audit_log(db, current_user.id, "api_key_created", {"name": payload.name})
    CacheService.delete(f"api_keys:{current_user.id}:*")
    
    return result

@router.post("/api-keys/{key_id}/rotate")
def rotate_api_key(
    key_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Rotate/refresh an API key"""
    api_key = db.query(APIKey).filter(
        APIKey.id == key_id,
        APIKey.user_id == current_user.id
    ).first()
    
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="API key not found"
        )
    
    # Generate new key
    new_key_value = generate_api_key()
    api_key.key_hash = hash_password(new_key_value)
    api_key.last_used = None
    db.commit()
    db.refresh(api_key)
    
    result = APIKeyOut.model_validate(api_key)
    result.key = new_key_value
    
    audit_log(db, current_user.id, "api_key_rotated", {"key_id": key_id})
    CacheService.delete(f"api_keys:{current_user.id}:*")
    
    return result

@router.patch("/api-keys/{key_id}/toggle")
def toggle_api_key(
    key_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Toggle API key active/inactive"""
    api_key = db.query(APIKey).filter(
        APIKey.id == key_id,
        APIKey.user_id == current_user.id
    ).first()
    
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="API key not found"
        )
    
    api_key.is_active = not api_key.is_active
    db.commit()
    
    audit_log(
        db, current_user.id, "api_key_toggled",
        {"key_id": key_id, "is_active": api_key.is_active}
    )
    CacheService.delete(f"api_keys:{current_user.id}:*")
    
    return {"is_active": api_key.is_active}

@router.delete("/api-keys/{key_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_api_key(
    key_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete API key"""
    api_key = db.query(APIKey).filter(
        APIKey.id == key_id,
        APIKey.user_id == current_user.id
    ).first()
    
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="API key not found"
        )
    
    db.delete(api_key)
    db.commit()
    
    audit_log(db, current_user.id, "api_key_deleted", {"key_id": key_id})
    CacheService.delete(f"api_keys:{current_user.id}:*")
    
    return None
