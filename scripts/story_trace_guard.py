#!/usr/bin/env python3
"""Validate STORY private trace completeness for cadence quality gates.

Usage:
  python3 scripts/story_trace_guard.py <trace.md>
"""

from __future__ import annotations

import sys
from pathlib import Path

from trace_guard_common import first_group_count, missing_sections, read_text

REQUIRED_SECTIONS = [
    "query basket plan",
    "executed queries",
    "top disconfirming findings",
    "rejected_due_to_confirmation_risk",
    "cross-domain candidates surfaced",
]


def count_queries(text: str, label: str) -> int:
    # Accepts forms like "Bluesky (8/8 executed)" or "Polymarket (7 scans executed)"
    return first_group_count(
        text,
        [
            rf"{label}\s*\((\d+)\s*/\s*(\d+)",
            rf"{label}\s*\((\d+)\s+scans\s+executed\)",
            rf"{label}\s*\((\d+)\s+executed\)",
        ],
    )


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/story_trace_guard.py <trace.md>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: trace file not found: {path}")
        return 2

    text = read_text(path)
    errors: list[str] = []

    for section in missing_sections(text, REQUIRED_SECTIONS):
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
