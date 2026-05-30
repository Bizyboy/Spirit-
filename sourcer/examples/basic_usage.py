#!/usr/bin/env python3
"""
Example: Basic Sourcer Usage

This script demonstrates basic usage of the Sourcer AI system.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from sourcer.core import Sourcer
from sourcer.ethics import EthicalGuard


def main():
    print("="*70)
    print("  SOURCER AI - BASIC USAGE EXAMPLE")
    print("="*70)
    print()
    
    # Show ethical guidelines
    print("1. ETHICAL GUIDELINES")
    print("-" * 70)
    print(EthicalGuard.get_ethical_summary())
    
    # Initialize Sourcer
    print("\n2. INITIALIZE SOURCER")
    print("-" * 70)
    sourcer = Sourcer()
    capabilities = sourcer.get_capabilities()
    print(f"Name: {capabilities['name']}")
    print(f"Version: {capabilities['version']}")
    print(f"Purpose: {capabilities['purpose']}")
    print()
    
    # Example 1: Vulnerability Research
    print("\n3. EXAMPLE: VULNERABILITY RESEARCH")
    print("-" * 70)
    query1 = {
        "target": "CVE-2024-1234",
        "purpose": "Security vulnerability research",
        "sources": ["vulnerability_db"],
        "scope": "technical_details"
    }
    
    print(f"Researching: {query1['target']}")
    results1 = sourcer.gather_intelligence(query1)
    print(f"Success: {results1['success']}")
    print(f"Ethical validation: {results1['metadata']['ethical_validation']}")
    print()
    
    # Example 2: Business Intelligence
    print("\n4. EXAMPLE: BUSINESS INTELLIGENCE")
    print("-" * 70)
    query2 = {
        "target": "Example Corporation",
        "purpose": "Public business research",
        "sources": ["business_registry"],
        "scope": "public_filings"
    }
    
    print(f"Researching: {query2['target']}")
    results2 = sourcer.gather_intelligence(query2)
    print(f"Success: {results2['success']}")
    print(f"Sources queried: {results2['metadata']['sources_queried']}")
    print()
    
    # Example 3: Domain Research
    print("\n5. EXAMPLE: DOMAIN RESEARCH")
    print("-" * 70)
    query3 = {
        "target": "example.com",
        "purpose": "Network infrastructure research",
        "sources": ["whois", "dns"],
        "scope": "registration_info"
    }
    
    print(f"Researching: {query3['target']}")
    results3 = sourcer.gather_intelligence(query3)
    print(f"Success: {results3['success']}")
    print(f"Findings: {list(results3['findings'].keys())}")
    print()
    
    # Show audit trail
    print("\n6. AUDIT TRAIL")
    print("-" * 70)
    audit = sourcer.get_audit_trail()
    print(f"Total operations: {len(audit)}")
    print(f"All ethical checks passed: {all(entry['ethical_check'] for entry in audit)}")
    print()
    
    for i, entry in enumerate(audit, 1):
        query = entry['query']
        print(f"{i}. {query['purpose']}")
        print(f"   Target: {query['target']}")
        print(f"   Sources: {', '.join(query['sources'])}")
        print(f"   Ethical: {'✓' if entry['ethical_check'] else '✗'}")
        print()
    
    # Continuous refinement
    print("\n7. CONTINUOUS REFINEMENT")
    print("-" * 70)
    refinement = sourcer.continuous_refinement()
    print(f"Next advancement: {refinement['next_advancement']}")
    print()


if __name__ == "__main__":
    main()
