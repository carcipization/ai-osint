#!/usr/bin/env python3
"""Shared helpers for cadence trace guard scripts."""

from __future__ import annotations

import re
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def missing_sections(text: str, required_sections: list[str]) -> list[str]:
    low = text.lower()
    return [s for s in required_sections if s.lower() not in low]


def extract_section(text: str, heading: str) -> str:
    m = re.search(rf"##\s+{re.escape(heading)}[\s\S]*?(?=\n##\s+|\Z)", text, flags=re.IGNORECASE)
    return m.group(0) if m else ""


def count_numbered_lines(section_text: str) -> int:
    return len(re.findall(r"^\s*\d+\.\s+`?.+`?\s*$", section_text, flags=re.MULTILINE))


def first_group_count(text: str, patterns: list[str]) -> int:
    for p in patterns:
        m = re.search(p, text, flags=re.IGNORECASE)
        if m:
            return int(m.group(1))
    return 0
