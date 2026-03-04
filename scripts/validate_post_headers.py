#!/usr/bin/env python3
from __future__ import annotations

"""Validate baseline markdown publication headers for cadence safety.

Checks:
- Required top links are present:
  - **Human-readable HTML:** https://carcipization.github.io/ai-osint/<slug>.html
  - **LLM-friendly Markdown:** https://carcipization.github.io/ai-osint/<slug>.md
- Dateline format is strict: **Dateline:** YYYY-MM-DD HH:MM UTC

Usage:
  python3 scripts/validate_post_headers.py
  python3 scripts/validate_post_headers.py docs/<file>.md
"""

from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

DATELINE_RE = re.compile(r"^\*\*Dateline:\*\* \d{4}-\d{2}-\d{2} \d{2}:\d{2} UTC$", re.M)


def has_required_link(text: str, label: str, url: str) -> bool:
    plain = f"**{label}:** {url}"
    markdown = f"**{label}:** [{url}]({url})"
    if plain in text or markdown in text:
        return True
    # Fallback regex: labeled line containing exact URL anywhere after label.
    rx = re.compile(rf"^\*\*{re.escape(label)}:\*\*.*{re.escape(url)}.*$", re.M)
    return bool(rx.search(text))


def validate_file(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    slug = path.stem
    base = f"https://carcipization.github.io/ai-osint/{slug}"
    html_url = f"{base}.html"
    md_url = f"{base}.md"

    if not has_required_link(text, "Human-readable HTML", html_url):
        issues.append(f"{path.name}: missing/incorrect Human-readable HTML link")
    if not has_required_link(text, "LLM-friendly Markdown", md_url):
        issues.append(f"{path.name}: missing/incorrect LLM-friendly Markdown link")
    if not DATELINE_RE.search(text):
        issues.append(f"{path.name}: missing/invalid dateline format (**Dateline:** YYYY-MM-DD HH:MM UTC)")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", help="Specific markdown paths to validate")
    args = parser.parse_args()

    files = [Path(p) for p in args.paths] if args.paths else sorted(DOCS.glob("*.md"))
    # Skip generated pointer file.
    files = [p for p in files if p.name != "latest.md"]

    if not files:
        print("No markdown files found.")
        return 0

    all_issues: list[str] = []
    for path in files:
        if not path.exists():
            all_issues.append(f"{path}: file not found")
            continue
        all_issues.extend(validate_file(path))

    if all_issues:
        print("Post header validation failed:")
        for issue in all_issues:
            print(f"- {issue}")
        return 1

    print(f"Post header validation passed for {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
