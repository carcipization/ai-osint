#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


def count_numbered_items(section: str) -> int:
    return len(re.findall(r"^\s*\d+\.\s+`", section, flags=re.M))


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_followup_trace.py <trace.md>")
        return 2

    p = Path(sys.argv[1])
    if not p.exists():
        print(f"FAIL: trace file not found: {p}")
        return 1

    text = p.read_text(encoding="utf-8", errors="ignore")

    bsky_m = re.search(r"### Bluesky queries \(5\)(.*?)(?:\n### |\Z)", text, flags=re.S)
    poly_m = re.search(r"### Polymarket queries \(3\)(.*?)(?:\n### |\Z)", text, flags=re.S)

    if not bsky_m:
        print("FAIL: missing '### Bluesky queries (5)' section")
        return 1
    if not poly_m:
        print("FAIL: missing '### Polymarket queries (3)' section")
        return 1

    bsky_count = count_numbered_items(bsky_m.group(1))
    poly_count = count_numbered_items(poly_m.group(1))

    errs: list[str] = []
    if bsky_count < 5:
        errs.append(f"Bluesky query count too low: {bsky_count} < 5")
    if poly_count < 3:
        errs.append(f"Polymarket query count too low: {poly_count} < 3")

    if errs:
        for e in errs:
            print(f"FAIL: {e}")
        return 1

    print(f"PASS: Bluesky={bsky_count}, Polymarket={poly_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
