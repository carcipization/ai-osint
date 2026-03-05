#!/usr/bin/env python3
"""Bulk dataset intake lane for fast discovery.

Scans CKAN catalogs in batches, scores candidates, and writes:
- JSON (full normalized candidates)
- CSV (tabular shortlist)
- Markdown summary (top-ranked)

Usage:
  python scripts/bulk_dataset_intake.py --pages 5 --rows 200 --top 150
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import pathlib
import urllib.parse
import urllib.request
from typing import Any, Dict, List

PORTALS = [
    {"name": "data.gov", "base": "https://catalog.data.gov/api/3/action/package_search"},
    {"name": "HDX", "base": "https://data.humdata.org/api/3/action/package_search"},
    {"name": "European Data Portal", "base": "https://data.europa.eu/api/hub/search/datasets"},
]

API_LIKE_FORMATS = {"json", "geojson", "api", "xml", "csv", "parquet"}


def _http_json(url: str, timeout: int = 25) -> Dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": "ai-osint-bulk-intake/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", errors="replace"))


def _parse_iso_date(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    value = value.strip().replace("Z", "+00:00")
    try:
        d = dt.datetime.fromisoformat(value)
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d
    except Exception:
        return None


def _score_candidate(c: Dict[str, Any], now: dt.datetime) -> int:
    score = 0
    modified = _parse_iso_date(c.get("modified"))
    if modified:
        days = (now - modified).days
        if days <= 30:
            score += 3
        elif days <= 180:
            score += 2
        elif days <= 365:
            score += 1
    if c.get("license") and c.get("license") not in {"n/a", "none", "", "other"}:
        score += 1
    if c.get("formats"):
        fset = {f.lower() for f in c["formats"]}
        if fset & API_LIKE_FORMATS:
            score += 1
    if c.get("org"):
        score += 1
    if c.get("tags"):
        score += 1
    return score


def _dataset_permalink(portal: str, name: str | None) -> str:
    if not name:
        return ""
    if portal == "data.gov":
        return f"https://catalog.data.gov/dataset/{name}"
    if portal == "HDX":
        return f"https://data.humdata.org/dataset/{name}"
    return ""


def _norm_ckan(pkg: Dict[str, Any], portal: str) -> Dict[str, Any]:
    resources = pkg.get("resources") or []
    formats = sorted({(r.get("format") or "").strip() for r in resources if (r.get("format") or "").strip()})
    name = pkg.get("name")
    return {
        "portal": portal,
        "id": pkg.get("id"),
        "name": name,
        "title": pkg.get("title") or name,
        "url": pkg.get("url") or pkg.get("notes_url") or _dataset_permalink(portal, name) or "",
        "license": pkg.get("license_id") or pkg.get("license_title") or "",
        "modified": pkg.get("metadata_modified") or pkg.get("revision_timestamp") or "",
        "org": (pkg.get("organization") or {}).get("title") if isinstance(pkg.get("organization"), dict) else "",
        "tags": [t.get("name") for t in (pkg.get("tags") or []) if isinstance(t, dict) and t.get("name")],
        "formats": formats,
        "resource_count": len(resources),
    }


def fetch_ckan(portal_name: str, base: str, rows: int, pages: int) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for page in range(pages):
        params = urllib.parse.urlencode({"rows": rows, "start": page * rows})
        url = f"{base}?{params}"
        data = _http_json(url)
        if not data.get("success"):
            break
        results = (data.get("result") or {}).get("results") or []
        if not results:
            break
        out.extend(_norm_ckan(pkg, portal_name) for pkg in results)
    return out


def dedupe(cands: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen = set()
    out = []
    for c in cands:
        key = (c.get("portal"), c.get("id") or c.get("name") or c.get("title"))
        if key in seen:
            continue
        seen.add(key)
        out.append(c)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", type=int, default=200, help="Rows per API page per portal")
    ap.add_argument("--pages", type=int, default=5, help="Pages per portal")
    ap.add_argument("--top", type=int, default=150, help="Top candidates in markdown summary")
    ap.add_argument("--outdir", default="research-traces", help="Output directory")
    args = ap.parse_args()

    now = dt.datetime.now(dt.timezone.utc)
    all_candidates: List[Dict[str, Any]] = []
    errors: List[str] = []

    # CKAN portals only (eu portal endpoint in list is non-ckan; skip gracefully)
    for p in PORTALS:
        try:
            if "package_search" not in p["base"]:
                continue
            all_candidates.extend(fetch_ckan(p["name"], p["base"], args.rows, args.pages))
        except Exception as e:
            errors.append(f"{p['name']}: {e}")

    all_candidates = dedupe(all_candidates)

    for c in all_candidates:
        c["score"] = _score_candidate(c, now)

    all_candidates.sort(key=lambda x: (x.get("score", 0), x.get("resource_count", 0), x.get("modified") or ""), reverse=True)

    ts = now.strftime("%Y%m%dT%H%M%SZ")
    outdir = pathlib.Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    json_path = outdir / f"{ts}-bulk-dataset-intake.json"
    csv_path = outdir / f"{ts}-bulk-dataset-intake.csv"
    md_path = outdir / f"{ts}-bulk-dataset-intake-summary.md"

    json_path.write_text(json.dumps({"generated_at": now.isoformat(), "count": len(all_candidates), "errors": errors, "candidates": all_candidates}, indent=2), encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["score", "portal", "title", "name", "id", "modified", "license", "org", "resource_count", "formats", "url"],
        )
        w.writeheader()
        for c in all_candidates:
            w.writerow(
                {
                    "score": c.get("score"),
                    "portal": c.get("portal"),
                    "title": c.get("title"),
                    "name": c.get("name"),
                    "id": c.get("id"),
                    "modified": c.get("modified"),
                    "license": c.get("license"),
                    "org": c.get("org"),
                    "resource_count": c.get("resource_count"),
                    "formats": ",".join(c.get("formats") or []),
                    "url": c.get("url"),
                }
            )

    top = all_candidates[: args.top]
    lines = [
        "# Bulk Dataset Intake Summary",
        "",
        f"- Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}",
        f"- Total candidates: {len(all_candidates)}",
        f"- Top listed: {len(top)}",
    ]
    if errors:
        lines.append("- Errors:")
        lines.extend([f"  - {e}" for e in errors])
    lines.extend(["", "## Top Candidates", ""])
    for i, c in enumerate(top, 1):
        lines.append(
            f"{i}. [{c.get('title')}]({c.get('url') or '#'}) | score={c.get('score')} | {c.get('portal')} | modified={c.get('modified') or 'unknown'} | formats={','.join(c.get('formats') or [])}"
        )

    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(str(json_path))
    print(str(csv_path))
    print(str(md_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
