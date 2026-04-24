#!/usr/bin/env python3
"""Validate STORY private trace completeness for cadence quality gates.

Usage:
  python3 scripts/story_trace_guard.py <trace.md>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "query basket plan",
    "executed queries",
    "top disconfirming findings",
    "rejected_due_to_confirmation_risk",
    "cross-domain candidates surfaced",
]


def count_queries(text: str, label: str) -> int:
    # Accepts forms like "Bluesky (8/8 executed)" or "Polymarket (7 scans executed)"
    patterns = [
        rf"{label}\s*\((\d+)\s*/\s*(\d+)",
        rf"{label}\s*\((\d+)\s+scans\s+executed\)",
        rf"{label}\s*\((\d+)\s+executed\)",
    ]
    for p in patterns:
        m = re.search(p, text, flags=re.IGNORECASE)
        if m:
            return int(m.group(1))
    return 0


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/story_trace_guard.py <trace.md>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: trace file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8", errors="replace")
    errors: list[str] = []

    lowered = text.lower()
    for section in REQUIRED_SECTIONS:
        if section not in lowered:
            errors.append(f"Missing required section: '{section}'")

    bluesky_n = count_queries(text, "Bluesky")
    polymarket_n = count_queries(text, "Polymarket")

    if bluesky_n < 8:
        errors.append(f"Bluesky executed queries too low: {bluesky_n} (required >= 8)")
    if polymarket_n < 6:
        errors.append(f"Polymarket executed queries too low: {polymarket_n} (required >= 6)")

    if errors:
        print("STORY TRACE GUARD: FAIL")
        for e in errors:
            print(f"- {e}")
        return 1

    print("STORY TRACE GUARD: PASS")
    print(f"- Bluesky executed: {bluesky_n}")
    print(f"- Polymarket executed: {polymarket_n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
