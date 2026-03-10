#!/usr/bin/env python3
from __future__ import annotations

"""Build GitHub Pages site.

Source of truth:
  - docs/*.md

Outputs:
  - site/*.md (copied)
  - site/*.html (rendered)
  - site/index.html (generated)
  - site/latest.md + site/latest.html (copies of most recent doc by filename)

Design goals:
  - One place to publish (site/)
  - Deterministic builds
  - Human-readable index
"""

from dataclasses import dataclass
import json
from pathlib import Path
from datetime import datetime
import html
import re
import shutil

import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
# GitHub Pages source is /docs for this repo.
OUT = DOCS

POLICY = json.loads((ROOT / "policy" / "publication_policy.json").read_text(encoding="utf-8"))

CSS = """
:root { --fg:#111; --muted:#666; --bg:#fff; --card:#f7f8fa; --link:#0b57d0; }
body { font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif; color:var(--fg); background:var(--bg); max-width: 900px; margin: 32px auto; padding: 0 16px; line-height: 1.6; }
a { color: var(--link); }
code { background:#f1f3f4; padding:2px 6px; border-radius:6px; }
pre code { display:block; padding:12px; overflow:auto; }
.meta { color: var(--muted); }
hr { border:0; border-top:1px solid #e5e7eb; margin: 24px 0; }
.card { background: var(--card); padding: 14px 16px; border-radius: 12px; margin: 12px 0; }
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


def extract_dateline(md_text: str) -> str | None:
    # Matches lines like: **Dateline:** 2026-02-25
    m = re.search(r"^\*\*Dateline:\*\*\s*([^\n]+)\s*$", md_text, re.M)
    if not m:
        return None
    return m.group(1).strip()


URL_RE = re.compile(r"(?<!\]\()(?<!\()(?<!\[)(?P<url>https?://[^\s<>)\]]+)")


def linkify_plain_urls(md_text: str) -> str:
    """Convert bare http(s) URLs to proper Markdown links.

    Leaves existing markdown links untouched.
    """

    def repl(match: re.Match[str]) -> str:
        url = match.group("url")
        return f"[{url}]({url})"

    return URL_RE.sub(repl, md_text)


def upsert_crosslinks(md_text: str, slug: str) -> str:
    # Keep method docs terse: skip auto crosslink header for playbook pages.
    if slug == "dataset-playbook":
        return linkify_plain_urls(md_text)

    html_url = f"https://carcipization.github.io/ai-osint/{slug}.html"
    md_url = f"https://carcipization.github.io/ai-osint/{slug}.md"

    if "**Human-readable HTML:**" in md_text and "**LLM-friendly Markdown:**" in md_text:
        return linkify_plain_urls(md_text)

    lines = md_text.splitlines()
    insert_at = 1 if lines and lines[0].startswith("# ") else 0
    block = [
        "",
        f"**Human-readable HTML:** [HTML]({html_url})",
        f"**LLM-friendly Markdown:** [Markdown]({md_url})",
        "",
    ]
    new_lines = lines[:insert_at] + block + lines[insert_at:]
    return linkify_plain_urls("\n".join(new_lines).rstrip() + "\n")


def render_md_to_html(md_text: str, title: str) -> str:
    body = markdown.markdown(
        md_text,
        extensions=["extra", "fenced_code", "tables", "sane_lists", "toc"],
    )
    return html_shell(title, body)


@dataclass(frozen=True)
class Item:
    slug: str
    title: str
    dateline: str | None


def list_source_items() -> list[Path]:
    # docs/latest.md is treated as an output pointer (kept for backwards-compat)
    # and should not be considered a standalone post.
    exclude = {"readme.md", "latest.md"}
    files = sorted(p for p in DOCS.glob("*.md") if p.name.lower() not in exclude)
    return files


def build_item(md_path: Path) -> Item:
    slug = md_path.stem
    raw = md_path.read_text(encoding="utf-8")
    text = upsert_crosslinks(raw, slug)
    title = md_title(text, slug)
    dateline = extract_dateline(text)

    # Write normalized markdown back into docs (so crosslinks are committed)
    if text != raw:
        md_path.write_text(text, encoding="utf-8")

    OUT.mkdir(parents=True, exist_ok=True)
    out_html = OUT / f"{slug}.html"
    out_html.write_text(render_md_to_html(text, title), encoding="utf-8")

    return Item(slug=slug, title=title, dateline=dateline)


def write_latest(latest: Item) -> None:
    # Copy (not symlink) for compatibility with GitHub Pages.
    shutil.copyfile(DOCS / f"{latest.slug}.md", OUT / "latest.md")
    shutil.copyfile(OUT / f"{latest.slug}.html", OUT / "latest.html")


def dateline_sort_key(it: Item) -> tuple[datetime, str]:
    if not it.dateline:
        return (datetime.min, it.slug)
    for fmt in ("%Y-%m-%d %H:%M UTC", "%Y-%m-%d"):
        try:
            return (datetime.strptime(it.dateline, fmt), it.slug)
        except ValueError:
            continue
    return (datetime.min, it.slug)


SPECIAL_DATASET_DOCS = set(POLICY["feed"]["datasetReferences"])
FEED_INCLUDE = re.compile(POLICY["feed"]["includeSlugRegex"], re.I)
FEED_EXCLUDE = re.compile(POLICY["feed"]["excludeSlugRegex"], re.I)


def is_story_or_datasets_item(it: Item) -> bool:
    s = it.slug.lower()
    if s in SPECIAL_DATASET_DOCS:
        return False
    if FEED_EXCLUDE.search(s):
        return False
    return FEED_INCLUDE.search(s) is not None


def write_index(items: list[Item], latest: Item) -> None:
    # newest-first by dateline (fallback to slug)
    items_sorted = sorted(items, key=dateline_sort_key, reverse=True)

    rows = []
    for it in items_sorted:
        meta = f"<div class=\"meta\">Dateline: {html.escape(it.dateline)}</div>" if it.dateline else ""
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

    page_size = int(POLICY["feed"].get("pageSize", 20))
    pagination_js = """
<script>
(() => {{
  const PAGE_SIZE = __PAGE_SIZE__;
  const cards = Array.from(document.querySelectorAll('#feed .card'));
  const totalPages = Math.max(1, Math.ceil(cards.length / PAGE_SIZE));
  let page = 1;
  const pageInfo = document.getElementById('page-info');
  const prevBtn = document.getElementById('page-prev');
  const nextBtn = document.getElementById('page-next');

  function render() {{
    const start = (page - 1) * PAGE_SIZE;
    const end = start + PAGE_SIZE;
    cards.forEach((card, i) => {{ card.style.display = (i >= start && i < end) ? '' : 'none'; }});
    pageInfo.textContent = `Page ${page} of ${totalPages}`;
    prevBtn.disabled = page <= 1;
    nextBtn.disabled = page >= totalPages;
  }}

  prevBtn.addEventListener('click', () => {{ if (page > 1) {{ page--; render(); }}}});
  nextBtn.addEventListener('click', () => {{ if (page < totalPages) {{ page++; render(); }}}});
  render();
}})();
</script>
""".replace("__PAGE_SIZE__", str(page_size))

    body = "\n".join(
        [
            "<h1>AI OSINT</h1>",
            "<p class=\"meta\">Verification-first public story feed</p>",
            "<h2>Latest</h2>",
            f"<p><a href=\"{latest.slug}.html\"><strong>{html.escape(latest.title)}</strong></a></p>",
            "<p><a href=\"latest.md\">latest.md</a> and <a href=\"latest.html\">latest.html</a> always point to the most recent publication.</p>",
            "<hr/>",
            "<h2>Story feed</h2>",
            "<div id=\"feed\">",
            "\n".join(rows) if rows else "<p>(No posts found.)</p>",
            "</div>",
            '<div style="display:flex; gap:10px; align-items:center; margin:12px 0 4px 0;">',
            '<button id="page-prev" type="button">Previous</button>',
            '<span id="page-info" class="meta"></span>',
            '<button id="page-next" type="button">Next</button>',
            "</div>",
            pagination_js,
            "<hr/>",
            "<h2>Dataset references</h2>",
            "<ul>",
            '<li><a href="datasets-catalog.html">Datasets Catalog</a> · <a href="datasets-catalog.md">Markdown</a></li>',
            '<li><a href="dataset-playbook.html">Dataset Playbook</a> · <a href="dataset-playbook.md">Markdown</a></li>',
            "</ul>",
            "<hr/>",
            '<p>Repo: <a href="https://github.com/carcipization/ai-osint">github.com/carcipization/ai-osint</a></p>',
        ]
    )

    index = f"""<!doctype html>
<html>
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>AI OSINT</title>
  <style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""

    (OUT / "index.html").write_text(index, encoding="utf-8")


def main() -> None:
    sources = list_source_items()
    if not sources:
        raise SystemExit("No docs/*.md files found")

    items = [build_item(p) for p in sources]
    feed_items = [it for it in items if is_story_or_datasets_item(it)]
    if not feed_items:
        raise SystemExit("No STORY/DATASETS items found for feed")

    # Use dateline-first selection for feed "latest" (fallback to slug).
    latest = max(feed_items, key=dateline_sort_key)

    write_latest(latest)
    write_index(feed_items, latest)

    print(f"Built {len(items)} posts into docs/ (feed items={len(feed_items)}, latest={latest.slug})")


if __name__ == "__main__":
    main()
