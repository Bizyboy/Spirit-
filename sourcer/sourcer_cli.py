#!/usr/bin/env python3
"""
Sourcer CLI - Command-line interface for the Sourcer AI system

Usage:
    python sourcer_cli.py capabilities              # Show capabilities
    python sourcer_cli.py ethics                    # Show ethical guidelines
    python sourcer_cli.py query <type> <target>     # Run a query
    python sourcer_cli.py refine                    # Show next refinement task
"""

import sys
import json
import argparse
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sourcer.core import Sourcer
from sourcer.ethics import EthicalGuard


def show_capabilities():
    """Display Sourcer capabilities."""
    sourcer = Sourcer()
    caps = sourcer.get_capabilities()
    
    print("\n" + "="*70)
    print(f"  {caps['name']} v{caps['version']}")
    print("="*70)
    print(f"\nPurpose: {caps['purpose']}")
    print(f"Ethical Framework: {caps['ethical_framework']}")
    
    print("\n✓ CAPABILITIES:")
    for cap in caps['capabilities']:
        print(f"  • {cap}")
    
    print("\n✓ COMPLIANCE:")
    for comp in caps['compliance']:
        print(f"  • {comp}")
    
    print("\n✗ PROHIBITED ACTIONS:")
    for prohibited in caps['prohibited']:
        print(f"  • {prohibited}")
    
    print("\n✓ ALLOWED SOURCES:")
    for source in caps['allowed_sources']:
        print(f"  • {source}")
    print()


def show_ethics():
    """Display ethical guidelines."""
    print(EthicalGuard.get_ethical_summary())


def run_query(query_type: str, target: str, purpose: str = None):
    """Run an intelligence gathering query."""
    sourcer = Sourcer()
    
    # Map query type to sources
    source_map = {
        "vuln": ["vulnerability_db"],
        "vulnerability": ["vulnerability_db"],
        "business": ["business_registry"],
        "company": ["business_registry"],
        "domain": ["whois"],
        "whois": ["whois"],
        "osint": ["whois", "dns"]
    }
    
    sources = source_map.get(query_type.lower(), ["vulnerability_db"])
    
    query = {
        "target": target,
        "purpose": purpose or f"{query_type} research for legitimate purposes",
        "sources": sources,
        "scope": "standard"
    }
    
    print("\n" + "="*70)
    print("  EXECUTING QUERY")
    print("="*70)
    print(f"Target: {target}")
    print(f"Type: {query_type}")
    print(f"Purpose: {query['purpose']}")
    print(f"Sources: {', '.join(sources)}")
    print()
    
    results = sourcer.gather_intelligence(query)
    
    print("RESULTS:")
    print(json.dumps(results, indent=2))
    print()


def show_refinement():
    """Show next refinement task."""
    sourcer = Sourcer()
    refinement = sourcer.continuous_refinement()
    
    print("\n" + "="*70)
    print("  CONTINUOUS REFINEMENT STATUS")
    print("="*70)
    print(f"\nCompleted Tasks: {refinement['completed_tasks']}")
    print(f"Next Advancement: {refinement['next_advancement']}")
    
    print("\nRefinement Areas:")
    for area in refinement['refinement_areas']:
        print(f"  • {area}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Sourcer AI - Ethical Intelligence Gathering System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s capabilities
  %(prog)s ethics
  %(prog)s query vuln CVE-2024-1234
  %(prog)s query business "Example Corp"
  %(prog)s query domain example.com
  %(prog)s refine
        """
    )
    
    parser.add_argument('command', 
                       choices=['capabilities', 'ethics', 'query', 'refine'],
                       help='Command to execute')
    parser.add_argument('query_type', nargs='?',
                       help='Type of query (vuln, business, domain, osint)')
    parser.add_argument('target', nargs='?',
                       help='Target to research')
    parser.add_argument('--purpose', 
                       help='Purpose statement for the query')
    
    args = parser.parse_args()
    
    if args.command == 'capabilities':
        show_capabilities()
    elif args.command == 'ethics':
        show_ethics()
    elif args.command == 'query':
        if not args.query_type or not args.target:
            parser.error("query command requires query_type and target")
        run_query(args.query_type, args.target, args.purpose)
    elif args.command == 'refine':
        show_refinement()


if __name__ == "__main__":
    main()
