#!/usr/bin/env python3
"""Generate a structured EVOLVE research-trace scaffold.

Purpose: make EVOLVE runs faster to execute and easier to audit by enforcing
hypothesis -> change -> before/after -> impact documentation.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def build(slot_label: str, run_label: str) -> str:
    lines: list[str] = []
    lines.append("# EVOLVE trace scaffold")
    lines.append("")
    lines.append(f"**Run UTC:** {now_utc()}")
    lines.append(f"**Slot:** {slot_label}")
    lines.append(f"**Run label:** {run_label}")
    lines.append("")
    lines.append("## Problem statement")
    lines.append("- What failure mode are we fixing?")
    lines.append("- Why this is high leverage for quality/rate over 7-14 days?")
    lines.append("")
    lines.append("## Hypothesis")
    lines.append("- If we change X, then Y should improve because Z.")
    lines.append("")
    lines.append("## Changes made")
    lines.append("- File/path:")
    lines.append("- Concrete change:")
    lines.append("- Scope/risk notes:")
    lines.append("")
    lines.append("## Before checks")
    lines.append("- Baseline behavior (brief):")
    lines.append("- Known pain points:")
    lines.append("")
    lines.append("## After checks")
    lines.append("- What now happens differently:")
    lines.append("- Quick validation run or dry check:")
    lines.append("")
    lines.append("## Expected impact (7-14 days)")
    lines.append("- Publication quality impact:")
    lines.append("- Throughput/hit-rate impact:")
    lines.append("- Compliance/auditability impact:")
    lines.append("")
    lines.append("## Rollback criteria")
    lines.append("- What signal would indicate this change should be reverted/adjusted?")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate an EVOLVE trace scaffold markdown")
    ap.add_argument("--out", required=True, help="Output markdown path")
    ap.add_argument("--slot", default="EVOLVE")
    ap.add_argument("--run-label", default="cadence")
    args = ap.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(args.slot, args.run_label), encoding="utf-8")
    print(str(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
