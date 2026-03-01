#!/usr/bin/env python3
"""Lightweight docs validator for AI-OSINT publishing hygiene.

Checks (docs/*.md):
1) Story-like files include UTC dateline in format: **Dateline:** YYYY-MM-DD HH:MM UTC
2) Dataset intel files include at least one source link (http/https markdown link)
"""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1] / "docs"

DATELINE_RE = re.compile(r"\*\*Dateline:\*\*\s\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}\sUTC")
LINK_RE = re.compile(r"\[[^\]]+\]\(https?://[^)]+\)")

EXCLUDE = {
    "latest.md",
    "dataset-playbook.md",
    "dataset-strategy.md",
}

# Legacy files before this date are reported as warnings, not hard failures.
STRICT_FROM = date(2026, 2, 26)


def is_story_file(path: Path) -> bool:
    name = path.name
    return name.endswith(".md") and name not in EXCLUDE


def is_dataset_post(path: Path) -> bool:
    n = path.name.lower()
    return "dataset" in n and n != "datasets-catalog.md"


def file_date(path: Path) -> date | None:
    # Expected prefix: YYYY-MM-DD-...
    try:
        y, m, d = path.name[:10].split("-")
        return date(int(y), int(m), int(d))
    except Exception:
        return None


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    files = sorted(p for p in DOCS.glob("*.md") if is_story_file(p))

    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        fdate = file_date(path)
        strict = bool(fdate and fdate >= STRICT_FROM)

        if not DATELINE_RE.search(text):
            msg = f"Missing/invalid UTC dateline: {path.name}"
            (errors if strict else warnings).append(msg)

        if is_dataset_post(path) and not LINK_RE.search(text):
            msg = f"Dataset post missing source link(s): {path.name}"
            (errors if strict else warnings).append(msg)

    if warnings:
        print("VALIDATION WARNINGS")
        for w in warnings:
            print(f"- {w}")

    if errors:
        print("VALIDATION FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"VALIDATION OK: checked {len(files)} markdown docs files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
