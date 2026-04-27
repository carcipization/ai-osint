#!/usr/bin/env python3
"""Run a compact FOLLOWUP context probe (Bluesky + Polymarket).

Purpose: standardize mandatory FOLLOWUP context checks so each cycle records
query strings and top findings with less ad hoc command glue.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run(cmd: list[str]) -> tuple[int, str, str]:
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def web_search_bluesky(query: str, count: int) -> dict:
    # Uses existing repo workflow via OpenClaw shell wrapper expectations.
    # Here we call a tiny python snippet with requests to Brave endpoint only if
    # available in environment is out-of-scope; this script accepts injected
    # results if used outside OpenClaw.
    return {"query": query, "note": "execute via OpenClaw web_search tool", "count": count}


def polymarket_search(repo_root: Path, term: str, limit: int) -> dict:
    cmd = ["python3", str(repo_root / "scripts" / "polymarket_cli.py"), "search", term, "--limit", str(limit), "--json"]
    code, out, err = run(cmd)
    data = None
    if out:
        try:
            data = json.loads(out)
        except json.JSONDecodeError:
            data = {"raw": out}
    return {
        "command": " ".join(cmd),
        "exit_code": code,
        "results": data,
        "stderr": err or None,
    }


def _poly_top_findings(poly_runs: list[dict]) -> list[dict]:
    findings: list[dict] = []
    for run in poly_runs:
        term = run.get("command", "")
        results = run.get("results")
        if not isinstance(results, list):
            findings.append({"query": term, "matches": 0, "top": []})
            continue
        top = []
        for m in results[:3]:
            top.append(
                {
                    "question": m.get("question"),
                    "slug": m.get("slug"),
                    "prices": m.get("outcomePrices"),
                    "volume": m.get("volume"),
                }
            )
        findings.append({"query": term, "matches": len(results), "top": top})
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description="FOLLOWUP cycle probe helper")
    ap.add_argument("--repo-root", default=".", help="Path to ai-osint repo")
    ap.add_argument("--bluesky-query", action="append", default=[], help="Bluesky query string (repeatable)")
    ap.add_argument("--poly-term", action="append", default=[], help="Polymarket search term (repeatable)")
    ap.add_argument("--poly-limit", type=int, default=5)
    ap.add_argument("--enforce-followup-minimums", action="store_true", help="Fail if fewer than 5 Bluesky queries or 3 Polymarket terms are provided")
    args = ap.parse_args()

    if args.enforce_followup_minimums:
        if len(args.bluesky_query) < 5:
            print("error: FOLLOWUP requires at least 5 Bluesky queries", file=sys.stderr)
            return 2
        if len(args.poly_term) < 3:
            print("error: FOLLOWUP requires at least 3 Polymarket queries", file=sys.stderr)
            return 2

    repo = Path(args.repo_root).resolve()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    poly_runs = [polymarket_search(repo, t, args.poly_limit) for t in args.poly_term]
    out = {
        "run_utc": now,
        "bluesky_queries": [web_search_bluesky(q, 5) for q in args.bluesky_query],
        "polymarket": poly_runs,
        "polymarket_top_findings": _poly_top_findings(poly_runs),
        "minimums": {
            "bluesky_queries": len(args.bluesky_query),
            "polymarket_queries": len(args.poly_term),
            "enforced": bool(args.enforce_followup_minimums),
        },
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
