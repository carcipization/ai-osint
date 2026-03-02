#!/usr/bin/env python3
from __future__ import annotations

"""Lightweight guardrail checks for claim-check markdown posts.

Why: cadence slots require strict claim provenance + dateline formatting.
This script makes those requirements easy to verify before publish/push.
"""

from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

DATELINE_RE = re.compile(r"^\*\*Dateline:\*\* \d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC$", re.M)
HAS_PROVENANCE_HEADER_RE = re.compile(r"^## Claim provenance\s*$", re.M)
URL_RE = re.compile(r"https?://[^\s)]+")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Specific claim-check markdown paths to validate")
    args = parser.parse_args()

    bad: list[str] = []
    files = [Path(p) for p in args.paths] if args.paths else sorted(DOCS.glob("*claim-check.md"))

    if not files:
        print("No claim-check markdown files found.")
        return 0

    for path in files:
        if not path.exists():
            bad.append(f"{path}: file not found")
            continue
        text = path.read_text(encoding="utf-8")

        if not DATELINE_RE.search(text):
            bad.append(f"{path.name}: missing/invalid dateline format (**Dateline:** YYYY-MM-DD HH:MM UTC)")

        if not HAS_PROVENANCE_HEADER_RE.search(text):
            bad.append(f"{path.name}: missing '## Claim provenance' section")
            continue

        # Require at least one direct URL in provenance block slice.
        # Keep parser simple: between '## Claim provenance' and next H2 or EOF.
        start = text.find("## Claim provenance")
        end = text.find("\n## ", start + 1)
        block = text[start:end] if end != -1 else text[start:]
        urls = URL_RE.findall(block)
        if not urls:
            bad.append(f"{path.name}: claim provenance has no URLs")

    if bad:
        print("Claim-check validation failed:")
        for item in bad:
            print(f"- {item}")
        return 1

    print(f"Claim-check validation passed for {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
