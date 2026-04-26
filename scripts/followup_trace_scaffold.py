#!/usr/bin/env python3
"""Generate a structured FOLLOWUP research-trace scaffold.

Goal: standardize FOLLOWUP runs so mandatory query accounting and publishability
reasoning are captured consistently before rotating cadence state.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def build_markdown(run_label: str, sampled: int) -> str:
    lines: list[str] = []
    lines.append("# FOLLOWUP research trace scaffold")
    lines.append("")
    lines.append(f"**Run UTC:** {utc_now()}")
    lines.append(f"**Run label:** {run_label}")
    lines.append("")

    lines.append("## First-principles frame")
    lines.append("- Core re-check question:")
    lines.append("- What would count as a materially conclusion-changing update:")
    lines.append("- Falsification path for prior conclusion:")
    lines.append("")

    lines.append("## Sampled stories (3-10 target)")
    lines.append("| story_slug | prior core conclusion | fresh source checked | update found? (yes/no) | material? (yes/no) | notes |")
    lines.append("|---|---|---|---|---|---|")
    for _ in range(sampled):
        lines.append("|  |  |  |  |  |  |")
    lines.append("")

    lines.append("## Mandatory Bluesky query log (>=5)")
    for i in range(1, 6):
        lines.append(f"{i}. Query:")
        lines.append("   - Top findings:")
        lines.append("   - Why it does/does not change conclusion:")
    lines.append("")

    lines.append("## Mandatory Polymarket query log (>=3)")
    for i in range(1, 4):
        lines.append(f"{i}. Query:")
        lines.append("   - Top findings:")
        lines.append("   - Context-only relevance note:")
    lines.append("")

    lines.append("## Source availability / blocker log")
    lines.append("| source | url | first_status | retry_status | timestamp_utc | notes |")
    lines.append("|---|---|---|---|---|---|")
    lines.append("|  |  |  |  |  |  |")
    lines.append("")

    lines.append("## Follow-up decision")
    lines.append("- Publishable materially conclusion-changing update found? (yes/no):")
    lines.append("- If yes: what changed and why it alters decision consequences:")
    lines.append("- If no: concise no-publish rationale:")
    lines.append("")

    lines.append("## If no publish: fallback-to-EVOLVE mini-cycle")
    lines.append("- Hypothesis about FOLLOWUP bottleneck:")
    lines.append("- Concrete repo-level change made:")
    lines.append("- Before/after check:")
    lines.append("- Expected 7-14 day impact:")
    lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate FOLLOWUP trace scaffold markdown")
    ap.add_argument("--out", required=True, help="Output markdown path")
    ap.add_argument("--run-label", default="cadence-followup", help="Run label")
    ap.add_argument("--sampled", type=int, default=3, help="Rows for sampled-story table (default 3)")
    args = ap.parse_args()

    if args.sampled < 1 or args.sampled > 12:
        raise SystemExit("--sampled must be between 1 and 12")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build_markdown(args.run_label, args.sampled), encoding="utf-8")
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
