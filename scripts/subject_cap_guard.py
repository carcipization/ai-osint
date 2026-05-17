#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

STORY_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-.*-osint-story\.md$", re.I)
SUBJECT_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("space-weather", re.compile(r"\b(space weather|swpc|noaa space weather|geomagnetic|solar flare|coronal mass ejection|\bcme\b)\b", re.I)),
    ("andes", re.compile(r"\bandes\b", re.I)),
    ("earthquakes", re.compile(r"\b(usgs|earthquake|seismic|aftershock|m\d(?:\.\d)?)\b", re.I)),
    ("measles", re.compile(r"\bmeasles\b", re.I)),
]


def story_date(name: str) -> datetime | None:
    m = STORY_FILE_RE.match(name)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y-%m-%d")
    except ValueError:
        return None


def story_subject(path: Path) -> str | None:
    if not path.exists() or not path.name.lower().endswith("-osint-story.md"):
        return None
    txt = path.read_text(encoding="utf-8", errors="ignore")
    title = txt.splitlines()[0] if txt.splitlines() else ""
    hay = f"{path.stem} {title}"
    for key, pat in SUBJECT_PATTERNS:
        if pat.search(hay):
            return key
    return None


def count_subject_in_window(dt: datetime, subject: str) -> tuple[int, list[str]]:
    start = dt - timedelta(days=3)
    names: list[str] = []
    for p in DOCS.glob("*.md"):
        sdt = story_date(p.name)
        if sdt is None:
            continue
        if sdt < start or sdt > dt:
            continue
        if story_subject(p) == subject:
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
    subject = story_subject(candidate)
    if not subject:
        print("PASS (subject unknown; cap not applied)")
        return 0

    n, names = count_subject_in_window(dt, subject)
    if n > 2:
        print(f"BLOCK subject cap exceeded for '{subject}': {n} in trailing 4-day window")
        for x in names:
            print(f" - {x}")
        return 1

    print(f"PASS subject cap for '{subject}': {n} in trailing 4-day window")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
