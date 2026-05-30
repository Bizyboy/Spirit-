# Sourcer Configuration

This directory contains configuration files for the Sourcer AI system.

## Configuration Template

The `config.template.json` file provides a template for configuring Sourcer.

### How to Use

1. Copy `config.template.json` to `config.json`
2. Customize the settings for your needs
3. Place `config.json` in this directory

**Note:** `config.json` is gitignored to protect your settings.

### Configuration Options

#### Sourcer Settings
- `version`: Version identifier
- `ethical_mode`: Set to "strict" for maximum ethical enforcement
- `audit_logging`: Enable/disable audit trail logging

#### Data Sources
Configure which data sources are enabled and their rate limits:
- `vulnerability_databases`: CVE, NVD, security advisories
- `business_intelligence`: SEC EDGAR, business registries
- `osint`: WHOIS, DNS, public repositories

Each source supports:
- `enabled`: true/false to enable/disable
- `sources`: List of specific sources to use
- `rate_limit_per_minute`: API rate limiting

#### Ethical Constraints
- `require_purpose_statement`: Require purpose for each query
- `maintain_audit_trail`: Keep logs of all operations
- `respect_privacy`: Enforce privacy boundaries
- `public_sources_only`: Only use public data sources
- `follow_shrine_virtues`: Apply Shrine Virtue principles

#### Output Settings
- `format`: Output format (json, text, etc.)
- `include_sources`: Include source information
- `include_timestamps`: Add timestamps to results
- `include_ethical_validation`: Show ethical validation results

#### Continuous Refinement
- `enabled`: Enable continuous refinement suggestions
- `auto_suggest_improvements`: Automatically suggest improvements
- `track_task_completion`: Track completed tasks

## Example Configuration

See `config.template.json` for a complete example configuration.
