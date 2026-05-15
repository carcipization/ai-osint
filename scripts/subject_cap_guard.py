#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

STORY_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-.*-osint-story\.md$", re.I)
ANDES_RE = re.compile(r"\bandes\b", re.I)


def story_date(name: str) -> datetime | None:
    m = STORY_FILE_RE.match(name)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y-%m-%d")
    except ValueError:
        return None


def is_andes_story(path: Path) -> bool:
    if not path.exists() or not path.name.lower().endswith("-osint-story.md"):
        return False
    txt = path.read_text(encoding="utf-8", errors="ignore")
    title = txt.splitlines()[0] if txt.splitlines() else ""
    return bool(ANDES_RE.search(path.stem) or ANDES_RE.search(title))


def count_andes_in_window(dt: datetime) -> tuple[int, list[str]]:
    start = dt - timedelta(days=3)
    names: list[str] = []
    for p in DOCS.glob("*.md"):
        sdt = story_date(p.name)
        if sdt is None:
            continue
        if sdt < start or sdt > dt:
            continue
        if is_andes_story(p):
            names.append(p.name)
    return len(names), sorted(names)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: subject_cap_guard.py <candidate-md-path>", file=sys.stderr)
        return 2
    candidate = Path(sys.argv[1]).resolve()
    if not candidate.exists():
        print(f"missing candidate: {candidate}", file=sys.stderr)
        return 2
    dt = story_date(candidate.name)
    if dt is None:
        print("PASS (non-story filename)")
        return 0
    if not is_andes_story(candidate):
        print("PASS (subject cap not applicable)")
        return 0

    n, names = count_andes_in_window(dt)
    if n > 2:
        print(f"BLOCK Andes cap exceeded: {n} in trailing 4-day window")
        for x in names:
            print(f" - {x}")
        return 1

    print(f"PASS Andes cap: {n} in trailing 4-day window")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
