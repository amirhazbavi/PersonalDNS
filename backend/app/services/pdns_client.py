import logging
from typing import Optional, Dict, Any
import httpx
from app.core.config import get_settings

settings = get_settings()
logger = logging.getLogger(__name__)

class PowerDNSClient:
    """PowerDNS API client for zone and record management"""
    
    def __init__(self):
        self.base_url = settings.powerdns_api_url
        self.api_key = settings.powerdns_api_key
        self.timeout = 15
    
    def _headers(self) -> Dict[str, str]:
        """Get API headers with authentication"""
        return {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json"
        }
    
    async def create_zone(self, zone_name: str, kind: str = "Native") -> bool:
        """Create a new DNS zone"""
        zone_name = zone_name if zone_name.endswith(".") else zone_name + "."
        
        payload = {
            "name": zone_name,
            "kind": kind,
            "rrsets": [],
            "nameservers": [
                settings.powerdns_ns1 + ".",
                settings.powerdns_ns2 + "."
            ]
        }
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/api/v1/servers/localhost/zones",
                    headers=self._headers(),
                    json=payload,
                    timeout=self.timeout
                )
                
                if response.status_code in (200, 201, 202):
                    logger.info(f"Zone created: {zone_name}")
                    return True
                else:
                    logger.error(f"Failed to create zone {zone_name}: {response.text}")
                    raise RuntimeError(response.text)
        except Exception as e:
            logger.error(f"PowerDNS zone creation error: {str(e)}")
            raise
    
    async def delete_zone(self, zone_name: str) -> bool:
        """Delete a DNS zone"""
        zone_name = zone_name if zone_name.endswith(".") else zone_name + "."
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(
                    f"{self.base_url}/api/v1/servers/localhost/zones/{zone_name}",
                    headers=self._headers(),
                    timeout=self.timeout
                )
                
                if response.status_code in (200, 201, 202, 204):
                    logger.info(f"Zone deleted: {zone_name}")
                    return True
                else:
                    logger.error(f"Failed to delete zone {zone_name}: {response.text}")
                    raise RuntimeError(response.text)
        except Exception as e:
            logger.error(f"PowerDNS zone deletion error: {str(e)}")
            raise
    
    async def upsert_record(
        self,
        zone_name: str,
        record_name: str,
        record_type: str,
        content: str,
        ttl: int = 300,
        priority: int = None
    ) -> bool:
        """Create or update a DNS record"""
        zone_name = zone_name if zone_name.endswith(".") else zone_name + "."
        record_name = record_name if record_name.endswith(".") else record_name + "."
        
        # Build record content
        if record_type in ["MX", "SRV"] and priority:
            record_content = f"{priority} {content}"
        else:
            record_content = content
        
        rrsets = [
            {
                "name": record_name,
                "type": record_type,
                "ttl": ttl,
                "changetype": "REPLACE",
                "records": [
                    {
                        "content": record_content,
                        "disabled": False
                    }
                ]
            }
        ]
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.patch(
                    f"{self.base_url}/api/v1/servers/localhost/zones/{zone_name}",
                    headers=self._headers(),
                    json={"rrsets": rrsets},
                    timeout=self.timeout
                )
                
                if response.status_code in (200, 201, 202, 204):
                    logger.debug(f"Record updated: {record_name} ({record_type})")
                    return True
                else:
                    logger.error(f"Failed to update record: {response.text}")
                    raise RuntimeError(response.text)
        except Exception as e:
            logger.error(f"PowerDNS record update error: {str(e)}")
            raise
    
    async def delete_record(
        self,
        zone_name: str,
        record_name: str,
        record_type: str
    ) -> bool:
        """Delete a DNS record"""
        zone_name = zone_name if zone_name.endswith(".") else zone_name + "."
        record_name = record_name if record_name.endswith(".") else record_name + "."
        
        rrsets = [
            {
                "name": record_name,
                "type": record_type,
                "changetype": "DELETE"
            }
        ]
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.patch(
                    f"{self.base_url}/api/v1/servers/localhost/zones/{zone_name}",
                    headers=self._headers(),
                    json={"rrsets": rrsets},
                    timeout=self.timeout
                )
                
                if response.status_code in (200, 201, 202, 204):
                    logger.debug(f"Record deleted: {record_name} ({record_type})")
                    return True
                else:
                    logger.error(f"Failed to delete record: {response.text}")
                    raise RuntimeError(response.text)
        except Exception as e:
            logger.error(f"PowerDNS record deletion error: {str(e)}")
            raise
