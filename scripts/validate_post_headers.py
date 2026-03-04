#!/usr/bin/env python3
from __future__ import annotations

"""Validate baseline markdown publication headers for cadence safety.

Checks:
- Required top links are present (short clickable format):
  - **Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/<slug>.html)
  - **LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/<slug>.md)
- Dateline format is strict: **Dateline:** YYYY-MM-DD HH:MM UTC
- If AP preflight section exists, it uses proper Markdown ordered-list syntax (`1.`..`5.`)

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


def has_required_link(text: str, label: str, link_text: str, url: str) -> bool:
    expected = f"**{label}:** [{link_text}]({url})"
    return expected in text


def has_valid_ap_preflight_ordered_list(text: str) -> bool:
    if "## AP editor preflight" not in text:
        return True
    nums = [1, 2, 3, 4, 5]
    return all(re.search(rf"^\s*{n}\.\s+", text, re.M) for n in nums)


def validate_file(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    slug = path.stem
    base = f"https://carcipization.github.io/ai-osint/{slug}"
    html_url = f"{base}.html"
    md_url = f"{base}.md"

    if not has_required_link(text, "Human-readable HTML", "HTML", html_url):
        issues.append(f"{path.name}: missing/incorrect Human-readable HTML link ([HTML](...))")
    if not has_required_link(text, "LLM-friendly Markdown", "Markdown", md_url):
        issues.append(f"{path.name}: missing/incorrect LLM-friendly Markdown link ([Markdown](...))")
    if not DATELINE_RE.search(text):
        issues.append(f"{path.name}: missing/invalid dateline format (**Dateline:** YYYY-MM-DD HH:MM UTC)")
    if not has_valid_ap_preflight_ordered_list(text):
        issues.append(f"{path.name}: AP preflight present but ordered list is not valid Markdown 1.-5.")

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
