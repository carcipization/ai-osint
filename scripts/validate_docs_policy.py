#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

POLICY = json.loads((ROOT / "policy" / "publication_policy.json").read_text(encoding="utf-8"))
FORBIDDEN_SLUG = re.compile(POLICY["forbiddenDocsSlugRegex"], re.I)
FORBIDDEN_TITLE = re.compile(POLICY["forbiddenTitleRegex"], re.I)
ALLOWED_TITLE = re.compile(POLICY["allowedTitleRegex"], re.I)
REUTERS_LINK = re.compile(r"https?://(?:www\.)?reuters\.com/", re.I)
REUTERS_TEXT = re.compile(r"\breuters\b", re.I)

# Hard editorial cap (enforced at commit time):
# Do not allow more than 2 Andes-subject STORY posts in any trailing 4-day window.
ANDES_RE = re.compile(r"\bandes\b", re.I)
STORY_FILE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-.*-osint-story\.md$", re.I)
DATE_PREFIX_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-")

def staged_files() -> list[str]:
    out = subprocess.check_output([
        "git",
        "diff",
        "--cached",
        "--name-only",
        "--diff-filter=ACMR",
    ], text=True)
    return [x.strip() for x in out.splitlines() if x.strip()]


def _story_date_from_name(name: str) -> datetime | None:
    m = DATE_PREFIX_RE.match(name)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y-%m-%d")
    except ValueError:
        return None


def _is_andes_story(path: Path) -> bool:
    if not path.exists() or path.suffix.lower() != ".md":
        return False
    if not STORY_FILE_RE.match(path.name):
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    first = text.splitlines()[0] if text.splitlines() else ""
    return bool(ANDES_RE.search(path.stem) or ANDES_RE.search(first))


def main() -> int:
    bad: list[str] = []
    staged = staged_files()
    for rel in staged:
        p = Path(rel)
        if p.parent != Path("docs") or p.suffix not in {".md", ".html"}:
            continue

        full = ROOT / rel
        if not full.exists():
            continue
        try:
            text = full.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            text = ""

        if REUTERS_LINK.search(text) or REUTERS_TEXT.search(text):
            bad.append(f"reuters references disallowed in docs publication: {rel}")

        # Title/slug checks are markdown-specific
        if p.suffix != ".md":
            continue
        if p.name.lower() in {"latest.md", "readme.md", "datasets-catalog.md", "dataset-playbook.md"}:
            continue
        if FORBIDDEN_SLUG.search(p.stem):
            bad.append(f"forbidden slug pattern: {rel}")
            continue

        first = text.splitlines()[0] if text.splitlines() else ""
        if FORBIDDEN_TITLE.search(first):
            bad.append(f"forbidden KEV-family title: {rel} :: {first}")
            continue
        if not ALLOWED_TITLE.search(first):
            bad.append(f"title must be STORY or 'Datasets:' -> {rel} :: {first}")

    # Enforce Andes hard cap on newly added/modified story markdown files.
    changed_story_md = [
        Path(rel) for rel in staged
        if Path(rel).parent == Path("docs") and Path(rel).suffix.lower() == ".md" and STORY_FILE_RE.match(Path(rel).name)
    ]
    for rel_path in changed_story_md:
        full = ROOT / rel_path
        if not _is_andes_story(full):
            continue
        story_dt = _story_date_from_name(rel_path.name)
        if story_dt is None:
            continue
        window_start = story_dt - timedelta(days=3)
        andes_count = 0
        andes_names: list[str] = []
        for candidate in DOCS.glob("*.md"):
            cdt = _story_date_from_name(candidate.name)
            if cdt is None:
                continue
            if cdt < window_start or cdt > story_dt:
                continue
            if _is_andes_story(candidate):
                andes_count += 1
                andes_names.append(candidate.name)
        if andes_count > 2:
            bad.append(
                f"Andes subject cap exceeded ({andes_count} in trailing 4-day window for {rel_path.name}): {', '.join(sorted(andes_names))}"
            )

    if bad:
        print("\n[docs-policy] Blocked commit: publication policy violation(s):", file=sys.stderr)
        for b in bad:
            print(f" - {b}", file=sys.stderr)
        print("\nAllowed docs publications: STORY posts or 'Datasets:' posts only.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
