#!/usr/bin/env python3
"""Generate a structured STORY research-trace scaffold.

High-level goal: reduce missed quality gates and speed up publishable-story
selection by producing a consistent private-trace template aligned with SKILL.md.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def build_markdown(run_label: str, slot: str, candidates: int) -> str:
    lines: list[str] = []
    lines.append(f"# {slot} research trace scaffold")
    lines.append("")
    lines.append(f"**Run UTC:** {utc_now()}")
    lines.append(f"**Run label:** {run_label}")
    lines.append("")
    lines.append("## First-principles frame")
    lines.append("- Core decision-relevant question:")
    lines.append("- Required evidence families:")
    lines.append("- Top falsification path:")
    lines.append("")
    lines.append("## Discovery-pack execution (data-first)")
    lines.append("| check | datasets/sources used | baseline window | observed delta | status |")
    lines.append("|---|---|---|---|---|")
    lines.append("| Latest-vs-baseline deltas |  |  |  | done/pending |")
    lines.append("| Threshold crossings |  |  |  | done/pending |")
    lines.append("| Cross-source divergence |  |  |  | done/pending |")
    lines.append("| Structural breaks (30/90d) |  |  |  | done/pending |")
    lines.append("| Geographic concentration |  |  |  | done/pending |")
    lines.append("| Revision-risk scan |  |  |  | done/pending |")
    lines.append("")

    lines.append("## Dual-trigger candidate board")
    lines.append("- World-state candidates scanned:")
    lines.append("- Anomaly candidates scanned:")
    lines.append("- Candidate rotation log (ordered by priority and why each was accepted/rejected):")
    lines.append("")

    lines.append("## Source availability / blocker log")
    lines.append("| source | url | first_status | retry_status | timestamp_utc | notes |")
    lines.append("|---|---|---|---|---|---|")
    lines.append("|  |  |  |  |  |  |")
    lines.append("")

    lines.append("## Canonical URL / auth retry ledger")
    lines.append("| source_family | failing_url | failure_code | retry_path (hub/index/auth) | replacement_url_or_auth | final_status | timestamp_utc |")
    lines.append("|---|---|---|---|---|---|---|")
    lines.append("|  |  |  |  |  |  |  |")
    lines.append("")

    for i in range(1, candidates + 1):
        lines.append(f"### Candidate {i}")
        lines.append("1) Testable question:")
        lines.append("2) Three required evidence checks:")
        lines.append("3) One falsifier:")
        lines.append("4) Target datasets/sources:")
        lines.append("")
        lines.append("Gate outcomes:")
        lines.append("- Anomaly: pass/fail + note")
        lines.append("- Mechanism: pass/fail + note")
        lines.append("- Decision: pass/fail + note")
        lines.append("- Importance: pass/fail + note")
        lines.append("")

    lines.append("## Claim-evidence matrix (pre-prose)")
    lines.append("| claim_id | claim_text | evidence_family | source_url | timestamp_utc | status (supported/unproven/contradicted) | limitation |")
    lines.append("|---|---|---|---|---|---|---|")
    lines.append("| C1 |  |  |  |  |  |  |")
    lines.append("")

    lines.append("## Corroboration independence ledger")
    lines.append("| claim_id | source | upstream_origin | evidence_family | independent_of | proves | limitation |")
    lines.append("|---|---|---|---|---|---|---|")
    lines.append("| C1 |  |  |  |  |  |  |")
    lines.append("")

    lines.append("## Origin-diversity preflight (mandatory)")
    lines.append("| claim_id | claim_criticality (high/med/low) | artifact_urls | origin_families_count | corroboration_minutes_spent | pass/fail | action |")
    lines.append("|---|---|---|---|---|---|---|")
    lines.append("| C1 |  |  |  |  |  | escalate/provisional/rotate |")
    lines.append("")
    lines.append("Threshold checks:")
    lines.append("- High-impact claims have >=2 independent origin families or are explicitly downgraded provisional: yes/no")
    lines.append("- If key claims collapse to one origin family after ~12 min targeted corroboration: rotate candidate")
    lines.append("- Contradiction unresolved in-slot: hold/rotate")
    lines.append("")

    lines.append("## Could this be wrong because...")
    lines.append("- Top disconfirming hypothesis:")
    lines.append("- Evidence that would invalidate current conclusion:")
    lines.append("- Found or missing:")
    lines.append("")

    lines.append("## 72h overlap check")
    lines.append("- Potential duplicate post(s):")
    lines.append("- Material delta justifying publish OR no-publish rationale:")
    lines.append("")

    lines.append("## Candidate exhaustion check")
    lines.append("- Remaining viable candidates after gates:")
    lines.append("- If none, why this run is exhausted (availability/importance/mechanism/decision blockers):")
    lines.append("")

    lines.append("## Decision-actor map (non-specialist utility)")
    lines.append("| actor | decision they could change now | trigger threshold/evidence needed |")
    lines.append("|---|---|---|")
    lines.append("|  |  |  |")
    lines.append("")

    lines.append("## Consequence-first lead check (pre-publish)")
    lines.append("- Paragraph 1 states concrete broad consequence (cost/access/safety/mobility/services): yes/no")
    lines.append("- Paragraph 1 names a non-specialist actor decision: yes/no")
    lines.append("- If either no, demote/hold and continue candidate rotation: yes/no")
    lines.append("")

    lines.append("## Publish/no-publish decision")
    lines.append("- Decision:")
    lines.append("- Short rationale:")
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate a STORY trace scaffold markdown")
    ap.add_argument("--out", required=True, help="Output markdown path")
    ap.add_argument("--run-label", default="cadence", help="Run label")
    ap.add_argument("--slot", default="STORY", help="Slot label")
    ap.add_argument("--candidates", type=int, default=4, help="Number of candidate packets (default 4)")
    args = ap.parse_args()

    if args.candidates < 1 or args.candidates > 12:
        raise SystemExit("--candidates must be between 1 and 12")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(build_markdown(args.run_label, args.slot, args.candidates), encoding="utf-8")
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
