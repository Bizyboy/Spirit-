"""
Linear Ethics Algorithm — Spirit- / Book of Light

A sequential pipeline that evaluates any action or decision against the
12 Shrine Virtues defined in knowledge/shrines.py.

Pipeline stages (executed in order):
  1. InputStage     — normalise and parse the raw action text
  2. MappingStage   — identify which shrine virtues are relevant
  3. ScoringStage   — compute a per-virtue ethical score (0.0 – 1.0)
  4. ValidationStage— flag violations of shrine protocols
  5. DecisionStage  — derive a final ethical verdict
  6. OutputStage    — assemble a human-readable ethical report

Each stage is a pure function that receives a shared context dict and
returns it enriched with its own output.  The pipeline runner calls them
one after another, keeping the design strictly linear.
"""

from __future__ import annotations

import re
import textwrap
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Tuple

from knowledge.shrines import ShrineVirtues


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class EthicsContext:
    """Shared state that travels through every pipeline stage."""

    raw_input: str
    normalized: str = ""
    words: List[str] = field(default_factory=list)

    # stage outputs
    matched_shrines: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    scores: Dict[str, float] = field(default_factory=dict)
    violations: List[str] = field(default_factory=list)
    overall_score: float = 0.0
    verdict: str = ""
    guidance: str = ""
    report: str = ""


@dataclass
class EthicsResult:
    """Final result returned to the caller."""

    verdict: str           # "APPROVED" | "CAUTION" | "REJECTED"
    overall_score: float   # 0.0 (unethical) – 1.0 (fully ethical)
    violations: List[str]
    guidance: str
    report: str


# ---------------------------------------------------------------------------
# Stage 1 — Input
# ---------------------------------------------------------------------------

def input_stage(ctx: EthicsContext) -> EthicsContext:
    """Normalise raw text: lowercase, strip punctuation excess, tokenise."""
    text = ctx.raw_input.strip().lower()
    # collapse whitespace
    text = re.sub(r"\s+", " ", text)
    ctx.normalized = text
    ctx.words = re.findall(r"\b\w+\b", text)
    return ctx


# ---------------------------------------------------------------------------
# Stage 2 — Virtue Mapping
# ---------------------------------------------------------------------------

def mapping_stage(ctx: EthicsContext) -> EthicsContext:
    """
    Map the normalised action to every shrine whose keywords appear in the
    token set.  At least the default shrine (truth) is always included.
    """
    word_set = set(ctx.words)
    matched: Dict[str, Dict[str, Any]] = {}

    for shrine_key, shrine in ShrineVirtues.get_all_shrines().items():
        keywords: List[str] = shrine.get("keywords", [])
        hits = [kw for kw in keywords if kw in word_set]
        if hits:
            matched[shrine_key] = {"shrine": shrine, "hits": hits}

    # always include the truth shrine as the ethical baseline
    if "truth" not in matched:
        matched["truth"] = {
            "shrine": ShrineVirtues.get_shrine("truth"),
            "hits": [],
        }

    ctx.matched_shrines = matched
    return ctx


# ---------------------------------------------------------------------------
# Stage 3 — Ethical Scoring
# ---------------------------------------------------------------------------

# Words that suggest unethical intent; each occurrence decreases the score.
_NEGATIVE_SIGNALS: List[str] = [
    "harm", "hurt", "deceive", "lie", "cheat", "steal", "manipulate",
    "coerce", "exploit", "abuse", "oppress", "betray", "destroy", "kill",
    "corrupt", "violate", "threaten", "blackmail",
]

# Words that reinforce ethical intent; each occurrence increases the score.
_POSITIVE_SIGNALS: List[str] = [
    "help", "protect", "honest", "truth", "care", "support", "heal",
    "guide", "teach", "learn", "respect", "safe", "trust", "grow",
    "serve", "defend", "love", "peace", "share", "collaborate",
]


def scoring_stage(ctx: EthicsContext) -> EthicsContext:
    """
    Assign a score between 0.0 and 1.0 to each matched shrine based on:
      • positive keyword presence  (+0.1 per hit, capped at +0.5)
      • negative keyword presence  (−0.2 per hit, floored at 0.0)

    The overall score is the mean across all matched shrines.
    """
    word_set = set(ctx.words)
    scores: Dict[str, float] = {}

    neg_count = sum(1 for w in _NEGATIVE_SIGNALS if w in word_set)
    pos_count = sum(1 for w in _POSITIVE_SIGNALS if w in word_set)

    for shrine_key, data in ctx.matched_shrines.items():
        base = 0.5  # neutral start
        bonus = min(pos_count * 0.1, 0.5)
        penalty = min(neg_count * 0.2, 0.5)
        score = max(0.0, min(1.0, base + bonus - penalty))
        scores[shrine_key] = round(score, 3)

    ctx.scores = scores
    ctx.overall_score = (
        round(sum(scores.values()) / len(scores), 3) if scores else 0.5
    )
    return ctx


# ---------------------------------------------------------------------------
# Stage 4 — Validation
# ---------------------------------------------------------------------------

# Protocols whose violation is an automatic ethical flag.
_PROTOCOL_VIOLATIONS: List[Tuple[str, List[str]]] = [
    ("truth",      ["deceive", "lie", "false", "mislead"]),
    ("protection", ["harm", "hurt", "abuse", "oppress"]),
    ("discipline", ["break", "abandon", "quit", "neglect"]),
    ("humility",   ["arrogant", "ego", "superior", "dominate"]),
    ("boundaries", ["violate", "intrude", "ignore", "override"]),
]


def validation_stage(ctx: EthicsContext) -> EthicsContext:
    """Flag any shrine-protocol violations found in the action text."""
    word_set = set(ctx.words)
    violations: List[str] = []

    for shrine_key, bad_words in _PROTOCOL_VIOLATIONS:
        shrine = ShrineVirtues.get_shrine(shrine_key)
        if shrine is None:
            continue
        triggered = [bw for bw in bad_words if bw in word_set]
        if triggered:
            violations.append(
                f"{shrine['name']}: protocol breach — "
                f"detected '{', '.join(triggered)}' "
                f"(Protocol: {shrine['protocol']})"
            )

    ctx.violations = violations
    return ctx


# ---------------------------------------------------------------------------
# Stage 5 — Decision
# ---------------------------------------------------------------------------

_THRESHOLD_APPROVED = 0.65
_THRESHOLD_CAUTION  = 0.40


def decision_stage(ctx: EthicsContext) -> EthicsContext:
    """
    Derive a final verdict from the overall score and violations:

      APPROVED  — score ≥ 0.65 and no violations
      CAUTION   — score ≥ 0.40 or minor violations present
      REJECTED  — score < 0.40 or critical violations present
    """
    has_violations = len(ctx.violations) > 0

    if ctx.overall_score >= _THRESHOLD_APPROVED and not has_violations:
        ctx.verdict = "APPROVED"
    elif ctx.overall_score >= _THRESHOLD_CAUTION:
        ctx.verdict = "CAUTION"
    else:
        ctx.verdict = "REJECTED"

    # Build guidance from matched shrines
    guidance_lines: List[str] = []
    for shrine_key, data in ctx.matched_shrines.items():
        shrine = data["shrine"]
        guidance_lines.append(
            f"• [{shrine['name']}] {shrine['protocol']}"
        )

    ctx.guidance = "\n".join(guidance_lines) if guidance_lines else ""
    return ctx


# ---------------------------------------------------------------------------
# Stage 6 — Output
# ---------------------------------------------------------------------------

def output_stage(ctx: EthicsContext) -> EthicsContext:
    """Render a complete, human-readable ethical report."""
    bar_length = 20
    filled = int(ctx.overall_score * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)

    score_pct = int(ctx.overall_score * 100)

    violation_block = (
        "\n".join(f"  ⚠ {v}" for v in ctx.violations)
        if ctx.violations
        else "  ✓ None"
    )

    shrine_block = "\n".join(
        f"  {sk:15s}  {ctx.scores.get(sk, 0.0):.3f}"
        for sk in ctx.matched_shrines
    )

    verdict_symbol = {"APPROVED": "✅", "CAUTION": "⚠️", "REJECTED": "❌"}.get(
        ctx.verdict, "?"
    )

    report = textwrap.dedent(f"""
    ╔══════════════════════════════════════════════════════╗
    ║          LINEAR ETHICS ALGORITHM — REPORT           ║
    ╚══════════════════════════════════════════════════════╝

    INPUT:
      "{ctx.raw_input}"

    OVERALL ETHICAL SCORE:
      [{bar}] {score_pct}%

    VERDICT:  {verdict_symbol}  {ctx.verdict}

    SHRINE SCORES:
    {shrine_block}

    PROTOCOL VIOLATIONS:
    {violation_block}

    GUIDANCE:
    {ctx.guidance}
    """).strip()

    ctx.report = report
    return ctx


# ---------------------------------------------------------------------------
# Pipeline runner
# ---------------------------------------------------------------------------

# The stages are defined as a linear sequence — order matters.
_PIPELINE: List[Callable[[EthicsContext], EthicsContext]] = [
    input_stage,
    mapping_stage,
    scoring_stage,
    validation_stage,
    decision_stage,
    output_stage,
]


def evaluate(action: str) -> EthicsResult:
    """
    Run *action* through the linear ethics pipeline and return an
    :class:`EthicsResult`.

    Parameters
    ----------
    action:
        A plain-text description of the action or decision to evaluate.

    Returns
    -------
    EthicsResult
        Contains the verdict, score, violations, guidance, and full report.
    """
    if not isinstance(action, str):
        raise TypeError(f"action must be a str, got {type(action).__name__}")
    if not action.strip():
        raise ValueError("action must not be empty")

    ctx = EthicsContext(raw_input=action)

    for stage in _PIPELINE:
        ctx = stage(ctx)

    return EthicsResult(
        verdict=ctx.verdict,
        overall_score=ctx.overall_score,
        violations=ctx.violations,
        guidance=ctx.guidance,
        report=ctx.report,
    )


# ---------------------------------------------------------------------------
# CLI demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    demo_actions = [
        "I will help protect the vulnerable and guide them with truth.",
        "I will deceive and manipulate others to gain power.",
        "I want to learn, grow, and serve those around me with honesty.",
        "I will remain silent and listen before I speak.",
    ]

    for action in demo_actions:
        result = evaluate(action)
        print(result.report)
        print()
