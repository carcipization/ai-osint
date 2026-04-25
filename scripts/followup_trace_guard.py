#!/usr/bin/env python3
"""Validate FOLLOWUP private trace completeness.

Usage:
  python3 scripts/followup_trace_guard.py <trace.md>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from trace_guard_common import (
    count_numbered_lines,
    extract_section,
    first_group_count,
    missing_sections,
    read_text,
)

REQUIRED_SECTIONS = [
    "sampled prior stories",
    "bluesky query basket",
    "polymarket market/signal queries",
    "followup publish decision",
]


def extract_count(text: str, label: str) -> int:
    block = extract_section(text, label)
    if not block:
        return 0

    n = first_group_count(
        block,
        [
            rf"{label}[^\n]*\(required[^\n]*\)\s*\nexecuted queries\s*\((\d+)\)",
            r"executed queries\s*\((\d+)\):",
        ],
    )
    if n > 0:
        return n

    # fallback: count numbered items in the section
    return count_numbered_lines(block)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/followup_trace_guard.py <trace.md>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ERROR: trace file not found: {path}")
        return 2

    text = read_text(path)
    errors: list[str] = []

    for section in missing_sections(text, REQUIRED_SECTIONS):
        errors.append(f"Missing required section: '{section}'")

    bluesky_n = extract_count(text, "Bluesky query basket")
    polymarket_n = extract_count(text, "Polymarket market/signal queries")

    if bluesky_n < 5:
        errors.append(f"Bluesky executed queries too low: {bluesky_n} (required >= 5)")
    if polymarket_n < 3:
        errors.append(f"Polymarket executed queries too low: {polymarket_n} (required >= 3)")

    if errors:
        print("FOLLOWUP TRACE GUARD: FAIL")
        for e in errors:
            print(f"- {e}")
        return 1

    print("FOLLOWUP TRACE GUARD: PASS")
    print(f"- Bluesky executed: {bluesky_n}")
    print(f"- Polymarket executed: {polymarket_n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
