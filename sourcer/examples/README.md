# Sourcer Examples

This directory contains example scripts demonstrating various features of the Sourcer AI system.

## Available Examples

### 1. Basic Usage (`basic_usage.py`)

Demonstrates fundamental Sourcer operations:
- Initializing the Sourcer
- Viewing ethical guidelines
- Running vulnerability research
- Gathering business intelligence
- Performing domain research
- Reviewing the audit trail

**Run it:**
```bash
python3 sourcer/examples/basic_usage.py
```

### 2. Continuous Refinement Demo (`continuous_refinement_demo.py`)

Demonstrates the continuous refinement loop:
- Executing a series of tasks
- Automatic suggestion of next advancements
- Tracking completed tasks
- Identifying improvement areas

**Run it:**
```bash
python3 sourcer/examples/continuous_refinement_demo.py
```

## What These Examples Show

### Ethical Framework in Action
Both examples demonstrate how Sourcer:
- Validates all operations ethically before execution
- Maintains a complete audit trail
- Respects privacy and legal boundaries
- Integrates with the Shrine Virtues

### Continuous Refinement
The refinement demo specifically shows how Sourcer:
- Tracks completed tasks
- Identifies gaps in coverage
- Suggests practical next steps
- Implements the "replace with next advancement" principle

### Real-World Application
These examples provide templates for:
- Security research workflows
- Business intelligence gathering
- Domain and network analysis
- Multi-source intelligence aggregation

## Customizing Examples

You can modify these examples to:
- Test different data sources
- Experiment with multi-source queries
- Implement custom analysis workflows
- Integrate with your own systems

## Next Steps

After running these examples, you can:
1. Use the CLI interface: `python3 sourcer/sourcer_cli.py --help`
2. Import Sourcer in your own Python scripts
3. Extend the modules in `sourcer/modules/`
4. Implement real API integrations

## Notes

These examples use the framework version of Sourcer. Real API integrations would require:
- API keys for various services
- Network connectivity
- Proper authentication
- Rate limiting configuration

See the main Sourcer README for more information.
