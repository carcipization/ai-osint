# ai-osint

Public GitHub Pages site for publishing AI-assisted OSINT stories.

## Core idea

- Write stories/claim-checks as Markdown in `docs/`.
- GitHub Pages is served from `docs/` (repo Pages source is `/docs`).
- `docs/latest.*` always points at the most recent publication.

## Commands

```bash
make build
# or
python3 scripts/publish.py
```

## Published site (GitHub Pages)

- Pages root: `docs/`
- Latest: `docs/latest.md` + `docs/latest.html`
- Index: `docs/index.html`
