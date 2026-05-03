#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_followup_trace.py <trace.md>")
        return 2

    p = Path(sys.argv[1])
    if not p.exists():
        print(f"FAIL: trace file not found: {p}")
        return 1

    text = p.read_text(encoding="utf-8", errors="ignore")

    # Minimal gate only:
    # Require an explicit verdict + primary-data evidence note.
    verdict_ok = re.search(r"materially new primary-data signal\?\s*(yes|no)", text, flags=re.I)
    evidence_ok = re.search(r"primary-data evidence\s*:\s*.+", text, flags=re.I)

    if not verdict_ok:
        print("FAIL: missing verdict line: 'Materially new primary-data signal? yes|no'")
        return 1
    if not evidence_ok:
        print("FAIL: missing evidence line: 'Primary-data evidence: ...'")
        return 1

    print("PASS: minimal follow-up gate satisfied (verdict + evidence)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
