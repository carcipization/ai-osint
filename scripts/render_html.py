#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import html
import re
import shutil
from datetime import datetime
from dataclasses import dataclass

import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CSS = """
:root { --fg:#111; --muted:#666; --bg:#fff; --card:#f7f8fa; --link:#0b57d0; }
body { font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif; color:var(--fg); background:var(--bg); max-width: 900px; margin: 32px auto; padding: 0 16px; line-height: 1.6; }
a { color: var(--link); }
code { background:#f1f3f4; padding:2px 6px; border-radius:6px; }
pre code { display:block; padding:12px; overflow:auto; }
.meta { color: var(--muted); }
hr { border:0; border-top:1px solid #e5e7eb; margin: 24px 0; }
"""


def html_shell(title: str, body: str) -> str:
    return f"""<!doctype html>
<html>
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{html.escape(title)}</title>
  <style>{CSS}</style>
</head>
<body>
  <p><a href=\"./index.html\">← AI OSINT Home</a></p>
  {body}
</body>
</html>
"""


def md_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def upsert_crosslinks(md_path: Path) -> None:
    slug = md_path.stem
    html_url = f"https://carcipization.github.io/ai-osint/{slug}.html"
    md_url = f"https://carcipization.github.io/ai-osint/{slug}.md"
    text = md_path.read_text(encoding="utf-8")

    if "**Human-readable HTML:**" in text and "**LLM-friendly Markdown:**" in text:
        return

    lines = text.splitlines()
    insert_at = 1 if lines and lines[0].startswith("# ") else 0
    block = [
        "",
        f"**Human-readable HTML:** [HTML]({html_url})",
        f"**LLM-friendly Markdown:** [Markdown]({md_url})",
        "",
    ]
    new_lines = lines[:insert_at] + block + lines[insert_at:]
    md_path.write_text("\n".join(new_lines).rstrip() + "\n", encoding="utf-8")


def render_one(md_path: Path) -> Path:
    upsert_crosslinks(md_path)
    text = md_path.read_text(encoding="utf-8")
    title = md_title(text, md_path.stem)

    body = markdown.markdown(
        text,
        extensions=["extra", "fenced_code", "tables", "sane_lists", "toc"],
    )
    html_text = html_shell(title, body)

    out_path = md_path.with_suffix(".html")
    out_path.write_text(html_text, encoding="utf-8")
    return out_path


@dataclass(frozen=True)
class Item:
    slug: str
    title: str
    dateline: str | None


def extract_dateline(md_text: str) -> str | None:
    m = re.search(r"^\*\*Dateline:\*\*\s*([^\n]+)\s*$", md_text, re.M)
    return m.group(1).strip() if m else None


def dateline_sort_key(dateline: str | None, slug: str) -> tuple[datetime, str]:
    if not dateline:
        return (datetime.min, slug)
    for fmt in ("%Y-%m-%d %H:%M UTC", "%Y-%m-%d"):
        try:
            return (datetime.strptime(dateline, fmt), slug)
        except ValueError:
            continue
    return (datetime.min, slug)


SPECIAL_DOCS = {"datasets-catalog", "dataset-playbook", "dataset-strategy"}


def write_latest_and_index(md_files: list[Path]) -> None:
    posts = [
        p
        for p in md_files
        if p.name.lower() not in {"readme.md", "latest.md"} and p.stem not in SPECIAL_DOCS
    ]
    items: list[Item] = []
    for p in posts:
        t = p.read_text(encoding="utf-8")
        items.append(Item(slug=p.stem, title=md_title(t, p.stem), dateline=extract_dateline(t)))

    if not items:
        return

    latest = max(items, key=lambda it: dateline_sort_key(it.dateline, it.slug))
    shutil.copyfile(DOCS / f"{latest.slug}.md", DOCS / "latest.md")
    shutil.copyfile(DOCS / f"{latest.slug}.html", DOCS / "latest.html")

    rows = []
    for it in sorted(items, key=lambda it: dateline_sort_key(it.dateline, it.slug), reverse=True):
        meta = f'<div class="meta">Dateline: {html.escape(it.dateline)}</div>' if it.dateline else ""
        rows.append(
            "\n".join(
                [
                    '<div class="card">',
                    f"<div><strong>{html.escape(it.title)}</strong></div>",
                    meta,
                    f"<div><a href=\"{it.slug}.html\">HTML</a> · <a href=\"{it.slug}.md\">Markdown</a></div>",
                    "</div>",
                ]
            )
        )

    rows_html = "\n".join(rows)
    index = f"""<!doctype html>
<html>
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>AI OSINT</title>
  <style>{CSS}\n.card {{ background: var(--card); padding: 14px 16px; border-radius: 12px; margin: 12px 0; }}</style>
</head>
<body>
<h1>AI OSINT</h1>
<p class=\"meta\">Verification-first public story feed</p>
<h2>Core references</h2>
<ul>
  <li><a href=\"datasets-catalog.html\">Datasets Catalog</a> · <a href=\"datasets-catalog.md\">Markdown</a></li>
  <li><a href=\"dataset-playbook.html\">Dataset Playbook</a> · <a href=\"dataset-playbook.md\">Markdown</a></li>
  <li><a href=\"dataset-strategy.html\">Dataset Strategy (legacy)</a> · <a href=\"dataset-strategy.md\">Markdown</a></li>
</ul>
<hr/>
<h2>Latest story</h2>
<p><a href=\"{latest.slug}.html\"><strong>{html.escape(latest.title)}</strong></a></p>
<p><a href=\"latest.md\">latest.md</a> and <a href=\"latest.html\">latest.html</a> always point to the most recent story publication.</p>
<hr/>
<h2>Story feed</h2>
{rows_html}
<hr/>
<p>Repo: <a href=\"https://github.com/carcipization/ai-osint\">github.com/carcipization/ai-osint</a></p>
</body>
</html>
"""
    (DOCS / "index.html").write_text(index, encoding="utf-8")


def main() -> None:
    md_files = sorted(p for p in DOCS.glob("*.md") if p.name.lower() != "readme.md")
    for md_file in md_files:
        out = render_one(md_file)
        print(f"Rendered {out.relative_to(ROOT)}")
    write_latest_and_index(md_files)
    print("Updated docs/latest.(md|html) and docs/index.html")


if __name__ == "__main__":
    main()
