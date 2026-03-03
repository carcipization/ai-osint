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

# cadence safety check for claim-check posts (all, or specific files)
python3 scripts/validate_claim_checks.py
python3 scripts/validate_claim_checks.py docs/2026-03-02-zzzzzzzzzzzzzzzzzzz-california-robotaxi-permit-readiness-claim-check.md

# cadence-safe git sync when tracked runtime checkpoint files are dirty
bash scripts/safe_rebase_sync.sh
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
