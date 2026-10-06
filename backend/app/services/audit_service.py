import logging
from datetime import datetime
from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog

logger = logging.getLogger(__name__)

def audit_log(
    db: Session,
    user_id: int | None,
    action: str,
    details: dict,
    resource: str = None,
    resource_id: int = None,
    ip_address: str = None,
    user_agent: str = None,
    status: str = "success",
    error_message: str = None
):
    """Log an audit event"""
    try:
        log = AuditLog(
            user_id=user_id,
            action=action,
            details=details,
            resource=resource,
            resource_id=resource_id,
            ip_address=ip_address,
            user_agent=user_agent,
            status=status,
            error_message=error_message,
            created_at=datetime.utcnow()
        )
        db.add(log)
        db.commit()
        logger.debug(f"Audit log: {action} by user {user_id}")
    except Exception as e:
        logger.error(f"Failed to create audit log: {str(e)}")
