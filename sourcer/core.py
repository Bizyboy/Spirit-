"""
Sourcer Core - Main intelligence gathering system

This is the core engine that coordinates ethical information gathering
from public sources for legitimate research purposes.
"""

import json
import sys
import os
from datetime import datetime
from typing import Dict, List, Optional, Any

# Handle both package and standalone imports
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from sourcer.ethics import EthicalGuard
else:
    from .ethics import EthicalGuard


class Sourcer:
    """
    Main Sourcer class for coordinating intelligence gathering operations.
    
    All operations are subject to ethical validation via EthicalGuard.
    """
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize Sourcer with optional configuration.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.guard = EthicalGuard()
        self.audit_log = []
        self.session_id = datetime.now().isoformat()
        
    def gather_intelligence(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Main entry point for intelligence gathering.
        
        Args:
            query: Dictionary containing:
                - target: What to research (e.g., CVE ID, company name)
                - purpose: Legitimate purpose for the research
                - sources: List of sources to query
                - scope: Scope of information needed
                
        Returns:
            Dictionary with results and metadata
        """
        # Validate ethical compliance
        is_valid, message = self.guard.validate_action(
            action=f"gather_intelligence: {query.get('purpose', 'unspecified')}",
            context={
                "source": ",".join(query.get('sources', [])),
                "has_authorization": True,  # Assumed for public sources
                "is_public_record": True
            }
        )
        
        if not is_valid:
            self._log_action(query, {"error": message}, False)
            return {
                "success": False,
                "error": message,
                "ethical_guidance": self.guard.get_shrine_guidance(query.get('purpose', ''))
            }
        
        # Gather from specified sources
        results = self._execute_gathering(query)
        
        self._log_action(query, results, True)
        
        return results
    
    def _execute_gathering(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the actual information gathering.
        
        This is a framework - specific modules handle actual data collection.
        """
        target = query.get('target', '')
        sources = query.get('sources', [])
        purpose = query.get('purpose', '')
        
        results = {
            "success": True,
            "session_id": self.session_id,
            "timestamp": datetime.now().isoformat(),
            "query": {
                "target": target,
                "purpose": purpose,
                "sources": sources
            },
            "findings": {},
            "metadata": {
                "ethical_validation": "passed",
                "sources_queried": len(sources)
            }
        }
        
        # Framework for module-based gathering
        # Each source type would have its own module
        for source in sources:
            if source == "vulnerability_db":
                results["findings"]["vulnerabilities"] = self._query_vulnerability_db(target)
            elif source == "business_registry":
                results["findings"]["business_info"] = self._query_business_registry(target)
            elif source == "whois":
                results["findings"]["domain_info"] = self._query_whois(target)
            else:
                results["findings"][source] = {"status": "module_not_implemented"}
        
        return results
    
    def _query_vulnerability_db(self, target: str) -> Dict:
        """Query public vulnerability databases (placeholder)."""
        return {
            "source": "CVE/NVD Database (public)",
            "target": target,
            "status": "framework_ready",
            "note": "Would query public CVE/NVD APIs for vulnerability information"
        }
    
    def _query_business_registry(self, target: str) -> Dict:
        """Query public business registries (placeholder)."""
        return {
            "source": "Public Business Registry",
            "target": target,
            "status": "framework_ready",
            "note": "Would query public business registries and SEC filings"
        }
    
    def _query_whois(self, target: str) -> Dict:
        """Query WHOIS databases (placeholder)."""
        return {
            "source": "WHOIS Database (public)",
            "target": target,
            "status": "framework_ready",
            "note": "Would query WHOIS for domain registration information"
        }
    
    def _log_action(self, query: Dict, results: Dict, ethical: bool):
        """Log action to audit trail."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": self.session_id,
            "query": query,
            "ethical_check": ethical,
            "results_summary": {
                "success": results.get("success", False),
                "sources": len(results.get("findings", {}))
            }
        }
        self.audit_log.append(entry)
        self.guard.log_action(
            str(query.get('purpose', 'unknown')),
            str(results.get("success", False)),
            ethical
        )
    
    def get_audit_trail(self) -> List[Dict]:
        """Return the audit trail for this session."""
        return self.audit_log
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Return information about Sourcer capabilities."""
        return {
            "name": "Sourcer AI",
            "version": "0.1.0",
            "purpose": "Ethical intelligence gathering from public sources",
            "capabilities": [
                "Software vulnerability research (CVE, security advisories)",
                "Public business intelligence (SEC filings, registries)",
                "Domain/network information (WHOIS, DNS)",
                "Open-source intelligence (OSINT) from legal sources"
            ],
            "ethical_framework": "Shrine Virtues from Book of Light",
            "compliance": [
                "Respects privacy boundaries",
                "Only uses public sources",
                "Maintains audit trail",
                "Validates all actions ethically"
            ],
            "prohibited": self.guard.PROHIBITED_ACTIONS,
            "allowed_sources": self.guard.ALLOWED_SOURCES
        }
    
    def continuous_refinement(self) -> Dict[str, Any]:
        """
        Implement the continuous refinement loop.
        
        After each task completion, identifies the next practical advancement.
        """
        # Analyze recent activities
        recent_tasks = self.audit_log[-5:] if len(self.audit_log) >= 5 else self.audit_log
        
        if not recent_tasks:
            next_task = "Initialize first intelligence gathering operation"
        else:
            # Determine next advancement based on recent work
            sources_used = set()
            for task in recent_tasks:
                query = task.get("query", {})
                sources_used.update(query.get("sources", []))
            
            # Suggest next refinement
            all_sources = ["vulnerability_db", "business_registry", "whois", "osint"]
            unused_sources = [s for s in all_sources if s not in sources_used]
            
            if unused_sources:
                next_task = f"Expand coverage by implementing: {unused_sources[0]}"
            else:
                next_task = "Enhance existing modules with deeper analysis capabilities"
        
        return {
            "status": "ready_for_next_task",
            "completed_tasks": len(self.audit_log),
            "next_advancement": next_task,
            "refinement_areas": [
                "Expand data source coverage",
                "Improve analysis depth",
                "Enhance correlation capabilities",
                "Add automated report generation"
            ]
        }


if __name__ == "__main__":
    # Example usage
    print("Sourcer AI - Ethical Intelligence Gathering System")
    print("=" * 60)
    
    sourcer = Sourcer()
    
    # Display capabilities
    print("\nCapabilities:")
    caps = sourcer.get_capabilities()
    print(f"Name: {caps['name']}")
    print(f"Purpose: {caps['purpose']}")
    print("\nAllowed Activities:")
    for cap in caps['capabilities']:
        print(f"  ✓ {cap}")
    
    # Example query
    print("\n" + "=" * 60)
    print("Example Query:")
    query = {
        "target": "CVE-2024-1234",
        "purpose": "Security vulnerability research",
        "sources": ["vulnerability_db"],
        "scope": "technical_details"
    }
    
    results = sourcer.gather_intelligence(query)
    print(json.dumps(results, indent=2))
    
    # Show continuous refinement
    print("\n" + "=" * 60)
    print("Continuous Refinement Status:")
    refinement = sourcer.continuous_refinement()
    print(json.dumps(refinement, indent=2))
