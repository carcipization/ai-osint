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

## Story format requirement (claim checks)

For STORY-mode claim checks, include a **Claim provenance** section that lists the concrete social posts being evaluated:

- platform
- handle/account
- post URL
- UTC timestamp

If direct post URLs are unavailable, explicitly say so and include the best available identifying details (quoted text, account, approximate time, screenshot reference, etc.).
