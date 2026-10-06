import logging
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List

from app.core.db import get_db
from app.api.deps import require_admin
from app.models.user import User
from app.models.domain import Domain
from app.models.audit_log import AuditLog
from app.services.audit_service import audit_log

router = APIRouter(prefix="/api/admin", tags=["admin"])
logger = logging.getLogger(__name__)

@router.get("/users")
def list_users(
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """List all users (admin only)"""
    users = db.query(User).filter(
        User.is_deleted == False
    ).order_by(desc(User.created_at)).offset(skip).limit(limit).all()
    
    return [
        {
            "id": u.id,
            "email": u.email,
            "is_active": u.is_active,
            "is_verified": u.is_verified,
            "is_admin": u.is_admin,
            "created_at": u.created_at,
            "last_login": u.last_login
        }
        for u in users
    ]

@router.patch("/users/{user_id}/toggle-active")
def toggle_user_active(
    user_id: int,
    active: bool,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """Toggle user active/inactive status"""
    if user_id == admin.id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot modify your own account"
        )
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    user.is_active = active
    db.commit()
    
    audit_log(
        db, admin.id, "admin_user_toggled",
        {"target_user_id": user_id, "is_active": active}
    )
    
    return {"is_active": user.is_active}

@router.patch("/users/{user_id}/promote-admin")
def promote_to_admin(
    user_id: int,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db)
):
    """Promote user to admin"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    user.is_admin = True
    db.commit()
    
    audit_log(
        db, admin.id, "admin_promoted",
        {"target_user_id": user_id}
    )
    
    return {"is_admin": user.is_admin}

@router.get("/domains")
def list_all_domains(
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """List all domains (admin only)"""
    domains = db.query(Domain).order_by(
        desc(Domain.created_at)
    ).offset(skip).limit(limit).all()
    
    return domains

@router.get("/audit-logs")
def get_audit_logs(
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    action: str = Query(None),
    user_id: int = Query(None)
):
    """Get audit logs (admin only)"""
    query = db.query(AuditLog)
    
    if action:
        query = query.filter(AuditLog.action == action)
    
    if user_id:
        query = query.filter(AuditLog.user_id == user_id)
    
    logs = query.order_by(desc(AuditLog.created_at)).offset(skip).limit(limit).all()
    
    return logs

@router.get("/stats")
def get_stats(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    """Get system statistics (admin only)"""
    total_users = db.query(User).filter(User.is_deleted == False).count()
    active_users = db.query(User).filter(
        User.is_deleted == False,
        User.is_active == True
    ).count()
    total_domains = db.query(Domain).count()
    verified_domains = db.query(Domain).filter(Domain.status == "verified").count()
    
    return {
        "total_users": total_users,
        "active_users": active_users,
        "total_domains": total_domains,
        "verified_domains": verified_domains
    }
