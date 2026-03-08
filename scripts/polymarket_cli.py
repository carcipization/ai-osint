#!/usr/bin/env python3
"""Minimal Polymarket CLI for OSINT workflows.

Commands:
  - search: find markets by keyword
  - market: show one market by id/slug
  - snapshot: dump key fields for many markets (JSON/CSV)

Uses Polymarket Gamma API (public HTTP endpoints).
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

BASE_URL = "https://gamma-api.polymarket.com"


def _get_json(path: str, params: dict[str, Any] | None = None) -> Any:
    qs = ""
    if params:
        encoded = {k: v for k, v in params.items() if v is not None}
        qs = "?" + urllib.parse.urlencode(encoded, doseq=True)
    url = f"{BASE_URL}{path}{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": "ai-osint-polymarket-cli/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _normalize_row(m: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": m.get("id"),
        "slug": m.get("slug"),
        "question": m.get("question"),
        "category": m.get("category"),
        "active": m.get("active"),
        "closed": m.get("closed"),
        "volume": m.get("volume"),
        "liquidity": m.get("liquidity"),
        "startDate": m.get("startDate"),
        "endDate": m.get("endDate"),
        "outcomes": m.get("outcomes"),
        "outcomePrices": m.get("outcomePrices"),
        "url": f"https://polymarket.com/event/{m.get('slug')}" if m.get("slug") else None,
    }


def cmd_search(args: argparse.Namespace) -> int:
    data = _get_json(
        "/markets",
        {
            "limit": args.limit,
            "offset": args.offset,
            "closed": "false" if args.open_only else None,
        },
    )

    q = args.query.lower().strip()
    rows = []
    for m in data:
        text = " ".join(
            str(x)
            for x in [m.get("question"), m.get("description"), m.get("category"), m.get("slug")]
            if x
        ).lower()
        if q in text:
            rows.append(_normalize_row(m))

    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0

    for i, row in enumerate(rows, 1):
        print(f"{i}. {row['question']}")
        print(f"   id={row['id']} slug={row['slug']} category={row['category']} open={not row['closed']}")
        print(f"   volume={row['volume']} liquidity={row['liquidity']} url={row['url']}")
        if row.get("outcomes") and row.get("outcomePrices"):
            print(f"   outcomes={row['outcomes']} prices={row['outcomePrices']}")
    if not rows:
        print("No matches.")
    return 0


def cmd_market(args: argparse.Namespace) -> int:
    if args.slug:
        path = "/markets"
        data = _get_json(path, {"slug": args.slug})
        if isinstance(data, list):
            m = data[0] if data else None
        else:
            m = data
    else:
        m = _get_json(f"/markets/{args.id}")

    if not m:
        print("Market not found.", file=sys.stderr)
        return 1

    print(json.dumps(_normalize_row(m), indent=2, ensure_ascii=False))
    return 0


def cmd_snapshot(args: argparse.Namespace) -> int:
    data = _get_json(
        "/markets",
        {
            "limit": args.limit,
            "offset": args.offset,
            "closed": "false" if args.open_only else None,
        },
    )
    rows = [_normalize_row(m) for m in data]

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.format == "json":
        out.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        fields = [
            "id",
            "slug",
            "question",
            "category",
            "active",
            "closed",
            "volume",
            "liquidity",
            "startDate",
            "endDate",
            "outcomes",
            "outcomePrices",
            "url",
        ]
        with out.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            for r in rows:
                rr = dict(r)
                rr["outcomes"] = json.dumps(rr["outcomes"], ensure_ascii=False)
                rr["outcomePrices"] = json.dumps(rr["outcomePrices"], ensure_ascii=False)
                w.writerow(rr)

    print(str(out))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Polymarket CLI (Gamma API)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="Search markets by keyword")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=200)
    s.add_argument("--offset", type=int, default=0)
    s.add_argument("--open-only", action="store_true")
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=cmd_search)

    m = sub.add_parser("market", help="Fetch one market")
    g = m.add_mutually_exclusive_group(required=True)
    g.add_argument("--id")
    g.add_argument("--slug")
    m.set_defaults(func=cmd_market)

    snap = sub.add_parser("snapshot", help="Dump market snapshot to file")
    snap.add_argument("--limit", type=int, default=500)
    snap.add_argument("--offset", type=int, default=0)
    snap.add_argument("--open-only", action="store_true")
    snap.add_argument("--format", choices=["json", "csv"], default="json")
    snap.add_argument("--out", required=True)
    snap.set_defaults(func=cmd_snapshot)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
