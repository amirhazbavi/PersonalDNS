import logging
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.services.dns_service import DNSService

router = APIRouter(prefix="/api/dns", tags=["dns"])
logger = logging.getLogger(__name__)
dns_service = DNSService()

@router.get("/lookup")
async def dns_lookup(
    q: str = Query(..., min_length=1, max_length=255),
    record_type: str = Query("A", regex="^(A|AAAA|MX|TXT|NS|CNAME|SOA|SRV|CAA)$"),
    current_user: User = Depends(get_current_user)
):
    """Perform DNS lookup"""
    try:
        result = await dns_service.lookup(q, record_type)
        return result
    except Exception as e:
        logger.error(f"DNS lookup failed for {q}: {str(e)}")
        return {
            "query": q,
            "record_type": record_type,
            "resolved": False,
            "error": str(e)
        }

@router.get("/reverse")
async def reverse_lookup(
    ip: str = Query(..., min_length=7, max_length=45),
    current_user: User = Depends(get_current_user)
):
    """Perform reverse DNS lookup"""
    try:
        result = await dns_service.reverse_lookup(ip)
        return result
    except Exception as e:
        logger.error(f"Reverse DNS lookup failed for {ip}: {str(e)}")
        return {
            "ip": ip,
            "resolved": False,
            "error": str(e)
        }

@router.get("/check")
async def check_dns(
    domain: str = Query(..., min_length=3, max_length=255),
    current_user: User = Depends(get_current_user)
):
    """Check DNS propagation status"""
    try:
        result = await dns_service.check_propagation(domain)
        return result
    except Exception as e:
        logger.error(f"DNS check failed for {domain}: {str(e)}")
        return {
            "domain": domain,
            "propagated": False,
            "error": str(e)
        }

@router.get("/stats")
def dns_stats(current_user: User = Depends(get_current_user)):
    """Get DNS query statistics"""
    # Placeholder - implement with Prometheus metrics
    return {
        "queries_24h": 0,
        "queries_7d": 0,
        "avg_response_time_ms": 0,
        "error_rate_percent": 0
    }
