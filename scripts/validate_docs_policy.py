#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

FORBIDDEN_SLUG = re.compile(r"(followup|self|skill-update|datasets-optimize|kev|known-exploited-vulnerabilities|cisa-known-exploited)", re.I)
FORBIDDEN_TITLE = re.compile(r"\b(KEV|Known Exploited Vulnerabilities)\b", re.I)
ALLOWED_TITLE = re.compile(r"^#\s*(Datasets:|.+osint-story)", re.I)


def staged_files() -> list[str]:
    out = subprocess.check_output([
        "git",
        "diff",
        "--cached",
        "--name-only",
        "--diff-filter=ACMR",
    ], text=True)
    return [x.strip() for x in out.splitlines() if x.strip()]


def main() -> int:
    bad: list[str] = []
    for rel in staged_files():
        p = Path(rel)
        if p.suffix != ".md" or p.parent != Path("docs"):
            continue
        if p.name.lower() in {"latest.md", "readme.md", "datasets-catalog.md", "dataset-playbook.md"}:
            continue
        if FORBIDDEN_SLUG.search(p.stem):
            bad.append(f"forbidden slug pattern: {rel}")
            continue
        full = ROOT / rel
        if not full.exists():
            continue
        try:
            first = full.read_text(encoding="utf-8", errors="ignore").splitlines()[0]
        except Exception:
            first = ""
        if FORBIDDEN_TITLE.search(first):
            bad.append(f"forbidden KEV-family title: {rel} :: {first}")
            continue
        if not ALLOWED_TITLE.search(first):
            bad.append(f"title must be STORY or 'Datasets:' -> {rel} :: {first}")

    if bad:
        print("\n[docs-policy] Blocked commit: publication policy violation(s):", file=sys.stderr)
        for b in bad:
            print(f" - {b}", file=sys.stderr)
        print("\nAllowed docs publications: STORY posts or 'Datasets:' posts only.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
