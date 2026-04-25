#!/usr/bin/env python3
"""Run a compact FOLLOWUP context probe (Bluesky + Polymarket).

Purpose: standardize mandatory FOLLOWUP context checks so each cycle records
query strings and top findings with less ad hoc command glue.
"""

from __future__ import annotations

import argparse
import json
import subprocess
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


def main() -> int:
    ap = argparse.ArgumentParser(description="FOLLOWUP cycle probe helper")
    ap.add_argument("--repo-root", default=".", help="Path to ai-osint repo")
    ap.add_argument("--bluesky-query", action="append", default=[], help="Bluesky query string (repeatable)")
    ap.add_argument("--poly-term", action="append", default=[], help="Polymarket search term (repeatable)")
    ap.add_argument("--poly-limit", type=int, default=5)
    args = ap.parse_args()

    repo = Path(args.repo_root).resolve()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    out = {
        "run_utc": now,
        "bluesky_queries": [web_search_bluesky(q, 5) for q in args.bluesky_query],
        "polymarket": [polymarket_search(repo, t, args.poly_limit) for t in args.poly_term],
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
