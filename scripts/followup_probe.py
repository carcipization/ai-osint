#!/usr/bin/env python3
"""Follow-up source probe with canonical URL fallback.

Purpose: quickly test a batch of follow-up source URLs, auto-apply known
canonical replacements for common churny publishers, and emit JSON summaries
for research traces.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

CANONICAL_FALLBACKS = {
    # CDC retired dashboard path -> current respiratory index page
    "https://www.cdc.gov/respiratory-viruses/data-research/dashboard/activity-levels.html":
        "https://www.cdc.gov/respiratory-viruses/data/index.html",
    # ENTSO-E short slug seen in older traces -> full current slug
    "https://www.entsoe.eu/news/2026/03/20/entso-e-publishes-final-report-on-iberian-blackout/":
        "https://www.entsoe.eu/news/2026/03/20/entso-e-publishes-expert-panel-final-report-on-28-april-2025-blackout-in-spain-and-portugal/",
}


def fetch_once(url: str, timeout: int = 20) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-osint-followup-probe/1.0"})
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            final_url = resp.geturl()
            return {
                "ok": True,
                "status": resp.status,
                "url": url,
                "final_url": final_url,
                "fetched_at_utc": ts,
            }
    except urllib.error.HTTPError as e:
        return {
            "ok": False,
            "status": e.code,
            "error": f"HTTP {e.code}",
            "url": url,
            "fetched_at_utc": ts,
        }
    except Exception as e:
        return {
            "ok": False,
            "status": None,
            "error": str(e),
            "url": url,
            "fetched_at_utc": ts,
        }


def probe(url: str) -> dict:
    first = fetch_once(url)
    out = {"initial": first, "retry": None, "canonical_used": None}
    if first["ok"]:
        return out

    canonical = CANONICAL_FALLBACKS.get(url)
    if canonical:
        out["canonical_used"] = canonical
        out["retry"] = fetch_once(canonical)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Probe follow-up source URLs with canonical fallback")
    ap.add_argument("urls", nargs="+", help="URLs to probe")
    ap.add_argument("--json", action="store_true", help="emit JSON output")
    args = ap.parse_args()

    results = [{"input_url": u, **probe(u)} for u in args.urls]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            i = r["initial"]
            print(f"URL: {r['input_url']}")
            print(f"  initial: ok={i['ok']} status={i.get('status')} error={i.get('error', 'none')}")
            if r["canonical_used"]:
                rt = r["retry"]
                print(f"  canonical: {r['canonical_used']}")
                print(f"  retry: ok={rt['ok']} status={rt.get('status')} error={rt.get('error', 'none')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
