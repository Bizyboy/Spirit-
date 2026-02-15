"""
Ethical Guard - Enforces ethical boundaries for Sourcer operations

This module integrates with the Shrine Virtues to ensure all operations
comply with ethical and legal standards.
"""

import sys
import os
from typing import Dict, List, Optional, Tuple

# Add parent directory to path to import shrines
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from knowledge.shrines import ShrineVirtues
except ImportError:
    ShrineVirtues = None


class EthicalGuard:
    """
    Enforces ethical guidelines for all Sourcer operations.
    
    Principles:
    1. Truth - Only gather and present accurate information
    2. Protection - Never harm individuals or enable harm
    3. Boundaries - Respect privacy and legal limits
    4. Humility - Acknowledge limitations and uncertainty
    """
    
    PROHIBITED_ACTIONS = [
        "unauthorized_access",
        "private_data_collection",
        "stalking",
        "harassment",
        "identity_theft",
        "illegal_surveillance",
        "hacking",
        "data_breach"
    ]
    
    ALLOWED_SOURCES = [
        "public_apis",
        "government_databases",
        "public_registries",
        "cve_databases",
        "vulnerability_disclosures",
        "vulnerability_db",
        "business_registry",
        "whois",
        "dns",
        "osint",
        "sec_filings",
        "public_court_records",
        "whois_lookups",
        "dns_records"
    ]
    
    @classmethod
    def validate_action(cls, action: str, context: Dict) -> Tuple[bool, str]:
        """
        Validate if an action is ethical and legal.
        
        Args:
            action: The action to validate
            context: Context about the action
            
        Returns:
            (is_valid, message)
        """
        # Check for prohibited actions
        for prohibited in cls.PROHIBITED_ACTIONS:
            if prohibited in action.lower():
                return False, f"Action '{action}' is prohibited: involves {prohibited}"
        
        # Check data source
        source = context.get("source", "").lower()
        if source and not any(allowed in source for allowed in cls.ALLOWED_SOURCES):
            return False, f"Data source '{source}' is not in allowed list"
        
        # Check for privacy violations
        if context.get("requires_authentication") and not context.get("has_authorization"):
            return False, "Cannot access private data without proper authorization"
        
        # Check for personal data collection
        if context.get("collecting_personal_data"):
            if not context.get("has_consent") and not context.get("is_public_record"):
                return False, "Cannot collect personal data without consent or public record status"
        
        return True, "Action validated"
    
    @classmethod
    def get_shrine_guidance(cls, query: str) -> str:
        """Get relevant shrine virtue guidance for a query."""
        if ShrineVirtues:
            return ShrineVirtues.get_context_for_query(query)
        return "Shrine guidance not available. Follow core ethical principles."
    
    @classmethod
    def log_action(cls, action: str, result: str, ethical_check: bool):
        """Log all actions for audit trail."""
        # In a production system, this would write to a secure audit log
        print(f"[AUDIT] Action: {action} | Ethical: {ethical_check} | Result: {result}")
    
    @classmethod
    def get_ethical_summary(cls) -> str:
        """Get summary of ethical guidelines."""
        return """
SOURCER ETHICAL GUIDELINES
==========================

CORE PRINCIPLES (from Shrine Virtues):
• Truth - Only gather and present accurate information
• Protection - Never harm individuals or enable harm  
• Boundaries - Respect privacy and legal limits
• Humility - Acknowledge limitations and uncertainty

ALLOWED ACTIVITIES:
✓ Software vulnerability research (CVE, security advisories)
✓ Public business intelligence (SEC filings, business registries)
✓ Open-source intelligence from legal public sources
✓ DNS/WHOIS lookups for legitimate purposes
✓ Public court records (where legally accessible)

PROHIBITED ACTIVITIES:
✗ Unauthorized access to systems or data
✗ Collection of private information without consent
✗ Stalking, harassment, or enabling harm
✗ Identity theft or impersonation
✗ Illegal surveillance or data breaches
✗ Hacking or exploiting vulnerabilities

USAGE REQUIREMENTS:
→ All queries must have legitimate purpose
→ Must respect rate limits and terms of service
→ Must maintain audit trail of all actions
→ Must obtain proper authorization for non-public data
"""
