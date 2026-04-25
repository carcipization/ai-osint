#!/usr/bin/env python3
"""Quick Socrata latest-vs-baseline anomaly scanner.

Purpose: speed up STORY candidate triage by producing a consistent delta summary
for time-series style Socrata datasets with minimal manual query work.
"""

from __future__ import annotations

import argparse
import json
import statistics
import urllib.parse
import urllib.request


def fetch_rows(domain: str, dataset: str, date_col: str, metric_col: str, where: str, limit: int) -> list[dict]:
    base = f"https://{domain}/resource/{dataset}.json"
    params = {
        "$select": f"{date_col},sum({metric_col}) as metric",
        "$group": date_col,
        "$order": f"{date_col} DESC",
        "$limit": str(limit),
    }
    if where:
        params["$where"] = where
    url = base + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "ai-osint-socrata-scan/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def summarize(rows: list[dict], date_col: str) -> dict:
    clean = []
    for r in rows:
        d = r.get(date_col)
        m = r.get("metric")
        if not d or m in (None, ""):
            continue
        try:
            clean.append((str(d)[:10], float(m)))
        except ValueError:
            continue
    if len(clean) < 13:
        raise ValueError(f"Need at least 13 usable rows for latest vs 4/12-week baseline; got {len(clean)}")

    latest_date, latest_val = clean[0]
    prev4 = [v for _, v in clean[1:5]]
    prev12 = [v for _, v in clean[1:13]]
    avg4 = sum(prev4) / len(prev4)
    avg12 = sum(prev12) / len(prev12)
    std12 = statistics.pstdev(prev12) if len(prev12) > 1 else 0.0
    z12 = (latest_val - avg12) / std12 if std12 > 0 else None

    def pct_delta(a: float, b: float) -> float | None:
        if b == 0:
            return None
        return (a - b) / b * 100.0

    return {
        "latest": {"date": latest_date, "value": latest_val},
        "baseline": {
            "avg_prev_4": avg4,
            "avg_prev_12": avg12,
            "std_prev_12": std12,
        },
        "delta": {
            "pct_vs_prev_4": pct_delta(latest_val, avg4),
            "pct_vs_prev_12": pct_delta(latest_val, avg12),
            "z_vs_prev_12": z12,
        },
        "sample_rows_used": len(clean),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Scan Socrata series for latest-vs-baseline anomaly summary")
    ap.add_argument("--domain", required=True, help="Socrata domain, e.g. data.cdc.gov")
    ap.add_argument("--dataset", required=True, help="Dataset ID, e.g. r8kw-7aab")
    ap.add_argument("--date-col", required=True, help="Date column name")
    ap.add_argument("--metric-col", required=True, help="Metric column name to sum")
    ap.add_argument("--where", default="", help="Optional SoQL where clause")
    ap.add_argument("--limit", type=int, default=52, help="Number of grouped rows to fetch (default 52)")
    args = ap.parse_args()

    rows = fetch_rows(args.domain, args.dataset, args.date_col, args.metric_col, args.where, args.limit)
    out = {
        "input": {
            "domain": args.domain,
            "dataset": args.dataset,
            "date_col": args.date_col,
            "metric_col": args.metric_col,
            "where": args.where,
            "limit": args.limit,
        },
        "summary": summarize(rows, args.date_col),
    }
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
