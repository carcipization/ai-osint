#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import html
import re

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
        f"**Human-readable HTML:** {html_url}",
        f"**LLM-friendly Markdown:** {md_url}",
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


def main() -> None:
    md_files = sorted(p for p in DOCS.glob("*.md") if p.name != "README.md")
    for md_file in md_files:
        out = render_one(md_file)
        print(f"Rendered {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
