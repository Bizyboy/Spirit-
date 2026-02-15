#!/usr/bin/env python3
"""
Example: Continuous Refinement Loop

This script demonstrates Sourcer's continuous refinement capability.
After completing each task, it identifies and suggests the next advancement.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from sourcer.core import Sourcer


def demonstrate_refinement_loop():
    """Demonstrate the continuous refinement loop."""
    
    print("="*70)
    print("  SOURCER CONTINUOUS REFINEMENT DEMONSTRATION")
    print("="*70)
    print()
    
    # Initialize Sourcer
    sourcer = Sourcer()
    
    # Define a series of tasks
    tasks = [
        {
            "name": "Vulnerability Research",
            "query": {
                "target": "CVE-2024-1234",
                "purpose": "Security vulnerability research",
                "sources": ["vulnerability_db"]
            }
        },
        {
            "name": "Business Intelligence",
            "query": {
                "target": "Example Corp",
                "purpose": "Public business research",
                "sources": ["business_registry"]
            }
        },
        {
            "name": "Domain Research",
            "query": {
                "target": "example.com",
                "purpose": "Network infrastructure research",
                "sources": ["whois"]
            }
        },
        {
            "name": "Multi-Source OSINT",
            "query": {
                "target": "example.com",
                "purpose": "Comprehensive OSINT gathering",
                "sources": ["whois", "dns", "osint"]
            }
        }
    ]
    
    # Execute tasks and show refinement suggestions
    for i, task in enumerate(tasks, 1):
        print(f"\n{'='*70}")
        print(f"  TASK {i}: {task['name']}")
        print(f"{'='*70}\n")
        
        # Execute the task
        print(f"Executing: {task['query']['purpose']}")
        print(f"Target: {task['query']['target']}")
        print(f"Sources: {', '.join(task['query']['sources'])}")
        print()
        
        results = sourcer.gather_intelligence(task['query'])
        
        if results['success']:
            print("✓ Task completed successfully")
            print(f"  Sources queried: {results['metadata']['sources_queried']}")
            print(f"  Findings: {len(results['findings'])} items")
        else:
            print(f"✗ Task failed: {results.get('error', 'Unknown error')}")
        
        print()
        
        # Get refinement suggestion
        refinement = sourcer.continuous_refinement()
        print("REFINEMENT STATUS:")
        print(f"  Completed tasks: {refinement['completed_tasks']}")
        print(f"  Next advancement: {refinement['next_advancement']}")
        print()
        
        # Show audit trail summary
        if i == len(tasks):
            print(f"\n{'='*70}")
            print("  FINAL AUDIT TRAIL")
            print(f"{'='*70}\n")
            
            audit = sourcer.get_audit_trail()
            print(f"Total operations: {len(audit)}")
            print(f"All operations passed ethical validation: {all(entry['ethical_check'] for entry in audit)}")
            print()
            
            print("Operations summary:")
            for j, entry in enumerate(audit, 1):
                query = entry['query']
                print(f"  {j}. {query.get('purpose', 'Unknown')} - {query.get('target', 'Unknown')}")
    
    print(f"\n{'='*70}")
    print("  CONTINUOUS REFINEMENT AREAS")
    print(f"{'='*70}\n")
    
    refinement = sourcer.continuous_refinement()
    print("Next steps to improve the system:")
    for area in refinement['refinement_areas']:
        print(f"  • {area}")
    
    print()
    print("The continuous refinement loop ensures that after each task,")
    print("the system identifies practical advancements to improve its capabilities.")
    print()


if __name__ == "__main__":
    demonstrate_refinement_loop()
