# Sourcer AI - Ethical Intelligence Gathering System

**Part of the Spirit- Project**

Sourcer is an AI-powered intelligence gathering system built on strong ethical principles from the Book of Light's Shrine Virtues. It automates the collection and analysis of publicly available information for legitimate research purposes.

## 🎯 Purpose

Sourcer helps researchers, security professionals, and businesses gather intelligence from public sources while maintaining strict ethical boundaries:

- **Software Vulnerability Research** - Track CVEs, security advisories, and vulnerability patterns
- **Business Intelligence** - Analyze public company filings, registries, and relationships  
- **Open Source Intelligence (OSINT)** - Gather information from legal public sources
- **Network Research** - Query WHOIS, DNS, and public infrastructure data

## 🛡️ Ethical Framework

Sourcer is built on the **Shrine Virtues** from the Book of Light:

- **Truth** - Only gather and present accurate information
- **Protection** - Never harm individuals or enable harmful actions
- **Boundaries** - Respect privacy and legal limits
- **Humility** - Acknowledge limitations and uncertainties

### ✓ What Sourcer CAN Do

- Query public vulnerability databases (CVE, NVD)
- Access public business registries and SEC filings
- Perform WHOIS/DNS lookups for legitimate purposes
- Search public code repositories
- Analyze patterns in publicly available data

### ✗ What Sourcer CANNOT Do

- Access private or unauthorized data
- Enable stalking, harassment, or harm
- Bypass authentication or security measures
- Collect personal data without consent
- Violate terms of service or legal boundaries

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
cd Spirit-/sourcer

# No additional dependencies required for basic framework
# (Real implementations would require: requests, etc.)
```

### Basic Usage

```python
from sourcer.core import Sourcer

# Initialize Sourcer
sourcer = Sourcer()

# Show capabilities
capabilities = sourcer.get_capabilities()
print(capabilities)

# Run a query
query = {
    "target": "CVE-2024-1234",
    "purpose": "Security vulnerability research",
    "sources": ["vulnerability_db"],
    "scope": "technical_details"
}

results = sourcer.gather_intelligence(query)
print(results)
```

### Command-Line Interface

```bash
# Show capabilities
python sourcer/sourcer_cli.py capabilities

# Show ethical guidelines
python sourcer/sourcer_cli.py ethics

# Query vulnerability database
python sourcer/sourcer_cli.py query vuln CVE-2024-1234

# Query business information
python sourcer/sourcer_cli.py query business "Example Corp"

# Query domain information
python sourcer/sourcer_cli.py query domain example.com

# Show next refinement task
python sourcer/sourcer_cli.py refine
```

## 📁 Project Structure

```
sourcer/
├── __init__.py              # Package initialization
├── core.py                  # Main Sourcer engine
├── ethics.py                # Ethical guard and validation
├── sourcer_cli.py          # Command-line interface
├── config/
│   └── config.template.json # Configuration template
├── modules/
│   ├── __init__.py
│   ├── vulnerability.py     # Vulnerability research
│   ├── business.py          # Business intelligence
│   └── osint.py            # OSINT gathering
└── data/                    # Data storage (gitignored)
```

## 🔄 Continuous Refinement

Sourcer implements a continuous refinement loop as specified in the original requirements:

```python
# After completing a task, get next advancement
refinement = sourcer.continuous_refinement()
print(f"Next task: {refinement['next_advancement']}")
```

The system tracks completed tasks and automatically suggests the next practical advancement to continue refinement.

## 🔍 Modules

### Vulnerability Research (`vulnerability.py`)

Research software vulnerabilities from public databases:
- CVE (Common Vulnerabilities and Exposures)
- NVD (National Vulnerability Database)
- Security advisories and disclosures

### Business Intelligence (`business.py`)

Gather public business information:
- SEC EDGAR filings (for public companies)
- State business registries
- Public court records
- Business relationships from public filings

### OSINT Gatherer (`osint.py`)

Open-source intelligence from legal sources:
- WHOIS databases
- DNS records
- Public repositories
- Web archives (respecting ToS)

## ⚖️ Legal & Compliance

**IMPORTANT**: This is a framework designed for ethical, legal intelligence gathering.

- All operations must have a legitimate purpose
- Only public information from legal sources
- Respects rate limits and terms of service
- Maintains audit trail of all actions
- Requires proper authorization for any restricted data

**Users are responsible for ensuring their use complies with all applicable laws and regulations.**

## 🔐 Audit Trail

All operations are logged for transparency and accountability:

```python
# Get audit trail for session
audit_log = sourcer.get_audit_trail()
```

Each entry includes:
- Timestamp
- Query details
- Ethical validation result
- Sources accessed
- Results summary

## 🛠️ Configuration

Copy `config/config.template.json` to `config/config.json` and customize:

```json
{
  "sourcer": {
    "ethical_mode": "strict",
    "audit_logging": true
  },
  "data_sources": {
    "vulnerability_databases": {
      "enabled": true,
      "rate_limit_per_minute": 30
    }
  }
}
```

## 🤝 Integration with Spirit- Project

Sourcer integrates with the existing Shrine Virtues system:

```python
from knowledge.shrines import ShrineVirtues

# Get ethical guidance for a query
guidance = ShrineVirtues.get_context_for_query("research vulnerabilities")
```

## 📝 Current Status

**Version**: 0.1.0 (Framework)

This is a foundational framework. The core architecture and ethical guardrails are in place. Module implementations are placeholder code that would need to be completed with actual API integrations.

### Ready Components
- ✅ Ethical validation system
- ✅ Core Sourcer engine
- ✅ Audit logging
- ✅ Module structure
- ✅ CLI interface
- ✅ Continuous refinement loop

### Needs Implementation
- ⏳ Actual API integrations for data sources
- ⏳ Rate limiting
- ⏳ Data persistence
- ⏳ Advanced analysis capabilities
- ⏳ Report generation

## 🔮 Future Refinements

Based on the continuous refinement principle:

1. **Expand Data Source Coverage**
   - Integrate real APIs for NVD, CVE databases
   - Add more business intelligence sources
   - Expand OSINT capabilities

2. **Improve Analysis Depth**
   - Pattern recognition across vulnerabilities
   - Relationship mapping for businesses
   - Temporal analysis of trends

3. **Enhance Correlation**
   - Cross-reference data from multiple sources
   - Identify connections and patterns
   - Generate insights from aggregated data

4. **Automated Reporting**
   - Generate comprehensive reports
   - Visualize relationships and patterns
   - Export in multiple formats

## 📄 License

Part of the Spirit- project. See main repository for licensing information.

## ⚠️ Disclaimer

This tool is designed for legitimate research purposes only. Users must:
- Obtain proper authorization for their research
- Comply with all applicable laws and regulations
- Respect privacy and ethical boundaries
- Use responsibly and ethically

The developers are not responsible for misuse of this tool.

---

*"Truth is our foundation. Together, we rise."*  
— The Book of Light
