#!/usr/bin/env python3
"""Build compact STORY candidate packets from newline-delimited leads.

Each lead becomes a 4-item packet required by SKILL.md:
1) testable question
2) three required evidence checks
3) one falsifier
4) target datasets for interrogation
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone


def packet_for_lead(lead: str) -> dict:
    lead = lead.strip()
    return {
        "lead": lead,
        "testable_question": f"What measurable change occurred in '{lead}' versus its recent baseline, and does it alter a concrete public decision?",
        "required_evidence_checks": [
            "Latest primary artifact with timestamp and metric definition",
            "Baseline comparator (prior window and 30/90d context where available)",
            "Independent confirmation family from a different upstream origin",
        ],
        "falsifier": "A same-window independent dataset shows no anomaly or opposite direction after denominator normalization.",
        "target_datasets": [
            "Primary operational series for the phenomenon",
            "Independent confirmation telemetry/registry",
            "Spillover indicator linked to cost/access/safety/mobility/services",
        ],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lead", action="append", default=[], help="Lead text (repeatable)")
    ap.add_argument("--infile", help="File with one lead per line")
    ap.add_argument("--out", help="Output path for JSON")
    args = ap.parse_args()

    leads = list(args.lead)
    if args.infile:
        with open(args.infile, "r", encoding="utf-8") as f:
            leads.extend([ln.strip() for ln in f if ln.strip() and not ln.startswith("#")])

    leads = [x for x in leads if x.strip()]
    if not leads:
        raise SystemExit("No leads provided. Use --lead and/or --infile")

    out = {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "count": len(leads),
        "packets": [packet_for_lead(x) for x in leads],
    }

    payload = json.dumps(out, indent=2, ensure_ascii=False)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(payload + "\n")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
