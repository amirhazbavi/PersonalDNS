import logging
import asyncio
import dns.resolver
import dns.rdatatype
from typing import Dict, List, Any
from app.services.pdns_client import PowerDNSClient

logger = logging.getLogger(__name__)

class DNSService:
    """High-level DNS operations service"""
    
    def __init__(self):
        self.pdns = PowerDNSClient()
        self.resolver = dns.resolver.Resolver()
        self.resolver.timeout = 5
        self.resolver.lifetime = 10
    
    async def create_zone(self, zone_name: str) -> bool:
        """Create a new DNS zone in PowerDNS"""
        return await self.pdns.create_zone(zone_name)
    
    async def delete_zone(self, zone_name: str) -> bool:
        """Delete a DNS zone from PowerDNS"""
        return await self.pdns.delete_zone(zone_name)
    
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
        return await self.pdns.upsert_record(
            zone_name, record_name, record_type, content, ttl, priority
        )
    
    async def delete_record(
        self,
        zone_name: str,
        record_name: str,
        record_type: str
    ) -> bool:
        """Delete a DNS record"""
        return await self.pdns.delete_record(zone_name, record_name, record_type)
    
    async def lookup(self, domain: str, record_type: str = "A") -> Dict[str, Any]:
        """Perform DNS lookup"""
        try:
            answers = self.resolver.resolve(domain, record_type)
            return {
                "query": domain,
                "record_type": record_type,
                "resolved": True,
                "records": [str(rdata) for rdata in answers],
                "ttl": answers.rrset.ttl
            }
        except Exception as e:
            logger.warning(f"DNS lookup failed for {domain}: {str(e)}")
            return {
                "query": domain,
                "record_type": record_type,
                "resolved": False,
                "error": str(e)
            }
    
    async def reverse_lookup(self, ip: str) -> Dict[str, Any]:
        """Perform reverse DNS lookup"""
        try:
            answers = self.resolver.resolve_address(ip)
            return {
                "ip": ip,
                "resolved": True,
                "hostnames": [str(rdata) for rdata in answers]
            }
        except Exception as e:
            logger.warning(f"Reverse DNS lookup failed for {ip}: {str(e)}")
            return {
                "ip": ip,
                "resolved": False,
                "error": str(e)
            }
    
    async def verify_txt_record(self, domain: str, expected_value: str) -> bool:
        """Verify a TXT record exists for domain verification"""
        try:
            verification_domain = f"_personaldns.{domain}"
            answers = self.resolver.resolve(verification_domain, "TXT")
            
            for rdata in answers:
                for txt_string in rdata.strings:
                    if expected_value in txt_string.decode():
                        logger.info(f"TXT verification successful for {domain}")
                        return True
            
            return False
        except Exception as e:
            logger.warning(f"TXT verification failed for {domain}: {str(e)}")
            return False
    
    async def check_propagation(self, domain: str, nameservers: List[str] = None) -> Dict[str, Any]:
        """Check DNS propagation across multiple nameservers"""
        if not nameservers:
            nameservers = [
                "8.8.8.8",
                "1.1.1.1",
                "208.67.222.222"
            ]
        
        results = {}
        
        for ns in nameservers:
            try:
                resolver = dns.resolver.Resolver()
                resolver.nameservers = [ns]
                resolver.timeout = 5
                
                answer = resolver.resolve(domain, "A")
                results[ns] = {
                    "propagated": True,
                    "records": [str(rdata) for rdata in answer]
                }
            except Exception as e:
                results[ns] = {
                    "propagated": False,
                    "error": str(e)
                }
        
        propagated_count = sum(1 for r in results.values() if r["propagated"])
        
        return {
            "domain": domain,
            "propagated": propagated_count == len(nameservers),
            "propagation_percentage": (propagated_count / len(nameservers)) * 100,
            "nameservers": results
        }
