"""
Sourcer - Ethical Intelligence Gathering System
Part of the Spirit- project

This module provides tools for gathering publicly available information
for legitimate purposes such as:
- Software vulnerability research
- Public business intelligence
- Open-source intelligence (OSINT) from legal sources

ETHICAL GUIDELINES:
- Only collect publicly available information
- Respect privacy and legal boundaries
- Follow the Shrine Virtues from the Book of Light
- Never engage in unauthorized access or illegal surveillance
"""

from .core import Sourcer
from .ethics import EthicalGuard

__version__ = "0.1.0"
__all__ = ["Sourcer", "EthicalGuard"]
