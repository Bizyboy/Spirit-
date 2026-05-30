# The Book of Light

This repository contains foundational material from the Book of Light.

## Contents

- `knowledge/shrines.py` - Implementation of core concepts and the 12 Shrine Virtues
- `sourcer/` - Sourcer AI: Ethical intelligence gathering system

## Components

### Shrine Virtues (`knowledge/shrines.py`)

The 12 Shrine Virtues provide ethical guardrails based on the Book of Light Pillars:
- Discipline, Truth, Openness, Humility
- Evolution, Protection, Silence, Boundaries  
- Paradox, Betrayal, Enough, Crossroads

These virtues guide all operations and decision-making within the project.

### Sourcer AI (`sourcer/`)

An AI-powered intelligence gathering system for ethical research:
- **Software Vulnerability Research** - CVE/NVD databases, security advisories
- **Business Intelligence** - Public filings, registries, business relationships
- **Open Source Intelligence (OSINT)** - WHOIS, DNS, public repositories

Built with strong ethical constraints:
- ✓ Only public, legal sources
- ✓ Maintains audit trail
- ✓ Respects privacy boundaries
- ✗ No unauthorized access
- ✗ No stalking or harassment

See [`sourcer/README.md`](sourcer/README.md) for detailed documentation.

## Quick Start

### Using Shrine Virtues

```python
from knowledge.shrines import ShrineVirtues

# Get ethical guidance for a query
guidance = ShrineVirtues.get_context_for_query("I need to make a decision")
print(guidance)
```

### Using Sourcer

```bash
# Show capabilities
python sourcer/sourcer_cli.py capabilities

# Query vulnerability database
python sourcer/sourcer_cli.py query vuln CVE-2024-1234

# Show ethical guidelines
python sourcer/sourcer_cli.py ethics
```

Or via Python:

```python
from sourcer.core import Sourcer

sourcer = Sourcer()
results = sourcer.gather_intelligence({
    "target": "CVE-2024-1234",
    "purpose": "Security research",
    "sources": ["vulnerability_db"]
})
```

## Project Structure

```
Spirit-/
├── knowledge/
│   └── shrines.py           # 12 Shrine Virtues
├── sourcer/                  # Sourcer AI system
│   ├── core.py              # Main engine
│   ├── ethics.py            # Ethical guardrails
│   ├── sourcer_cli.py       # CLI interface
│   ├── modules/             # Research modules
│   └── config/              # Configuration
├── README.md
└── .gitignore
```

## Ethical Framework

All components follow the Shrine Virtues:
- **Truth** - Accuracy and transparency
- **Protection** - Never enable harm
- **Boundaries** - Respect privacy and limits
- **Humility** - Acknowledge uncertainties

## License

See repository for licensing information.

---

*"Truth is our foundation. Together, we rise."*