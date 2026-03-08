#!/usr/bin/env python3
"""Minimal Metaculus CLI for OSINT workflows.

Commands:
  - search: find questions by keyword
  - question: fetch one question
  - snapshot: dump questions to JSON/CSV
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any
from urllib.error import HTTPError

BASE_URL = os.environ.get("METACULUS_API_BASE", "https://www.metaculus.com/api2")


def _load_local_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env.local"
    if not env_path.exists():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        if k and k not in os.environ:
            os.environ[k] = v.strip()


def _get_json(path: str, params: dict[str, Any] | None = None, *, token: str | None = None, cookie: str | None = None) -> Any:
    qs = ""
    if params:
        qs = "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    url = f"{BASE_URL}{path}{qs}"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
        "Accept": "application/json,text/plain,*/*",
        "Referer": "https://www.metaculus.com/",
    }
    if token:
        headers["Authorization"] = f"Token {token}"
    if cookie:
        headers["Cookie"] = cookie
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8", errors="ignore")
        except Exception:
            pass
        raise RuntimeError(f"HTTP {e.code} for {url} :: {body[:220]}") from e


def _row(q: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": q.get("id"),
        "title": q.get("title"),
        "status": q.get("status"),
        "resolution": q.get("resolution"),
        "author": (q.get("author") or {}).get("username"),
        "publish_time": q.get("publish_time"),
        "resolve_time": q.get("resolve_time"),
        "community_prediction": (q.get("community_prediction") or {}).get("full"),
        "url": f"https://www.metaculus.com/questions/{q.get('id')}/" if q.get("id") else None,
    }


def _auth(args: argparse.Namespace) -> dict[str, Any]:
    return {"token": args.token, "cookie": args.cookie}


def cmd_search(args: argparse.Namespace) -> int:
    data = _get_json("/questions/", {"search": args.query, "limit": args.limit, "offset": args.offset}, **_auth(args))
    items = data.get("results", [])
    rows = [_row(i) for i in items]
    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0
    if not rows:
        print("No matches.")
        return 0
    for i, r in enumerate(rows, 1):
        print(f"{i}. {r['title']}")
        print(f"   id={r['id']} status={r['status']} resolve_time={r['resolve_time']} url={r['url']}")
        if r.get("community_prediction") is not None:
            print(f"   community_prediction={r['community_prediction']}")
    return 0


def cmd_question(args: argparse.Namespace) -> int:
    q = _get_json(f"/questions/{args.id}/", **_auth(args))
    print(json.dumps(_row(q), indent=2, ensure_ascii=False))
    return 0


def cmd_snapshot(args: argparse.Namespace) -> int:
    data = _get_json("/questions/", {"limit": args.limit, "offset": args.offset, "search": args.search}, **_auth(args))
    rows = [_row(i) for i in data.get("results", [])]
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    if args.format == "json":
        out.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        fields = list(rows[0].keys()) if rows else ["id", "title", "status", "resolution", "author", "publish_time", "resolve_time", "community_prediction", "url"]
        with out.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
    print(str(out))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Metaculus CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=50)
    s.add_argument("--offset", type=int, default=0)
    s.add_argument("--json", action="store_true")
    s.add_argument("--token", default=os.environ.get("METACULUS_TOKEN"))
    s.add_argument("--cookie", default=os.environ.get("METACULUS_COOKIE"))
    s.set_defaults(func=cmd_search)

    q = sub.add_parser("question")
    q.add_argument("id", type=int)
    q.add_argument("--token", default=os.environ.get("METACULUS_TOKEN"))
    q.add_argument("--cookie", default=os.environ.get("METACULUS_COOKIE"))
    q.set_defaults(func=cmd_question)

    snap = sub.add_parser("snapshot")
    snap.add_argument("--search", default=None)
    snap.add_argument("--limit", type=int, default=200)
    snap.add_argument("--offset", type=int, default=0)
    snap.add_argument("--format", choices=["json", "csv"], default="json")
    snap.add_argument("--out", required=True)
    snap.add_argument("--token", default=os.environ.get("METACULUS_TOKEN"))
    snap.add_argument("--cookie", default=os.environ.get("METACULUS_COOKIE"))
    snap.set_defaults(func=cmd_snapshot)

    return p


def main() -> int:
    _load_local_env()
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
