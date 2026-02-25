# ai-osint

Public GitHub Pages site for publishing AI-assisted OSINT stories.

## Core idea

- Write stories/claim-checks as Markdown in `docs/`.
- Build a simple GitHub Pages site into `site/` (HTML + Markdown mirrors).
- `site/latest.*` always points at the most recent publication (by filename sort).

## Commands

```bash
make build
# or
python3 scripts/publish.py
```

## Site

- Pages root: `site/`
- Latest: `site/latest.md` + `site/latest.html`
- Index: `site/index.html`
