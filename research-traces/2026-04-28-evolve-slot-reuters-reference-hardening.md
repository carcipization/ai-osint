# EVOLVE trace — Reuters reference hardening in publication preflight (2026-04-28)

**Run UTC:** 2026-04-28 02:24 UTC  
**Slot:** EVOLVE

## Hypothesis
Publication-policy enforcement currently catches Reuters URLs in staged markdown docs, but can miss non-link Reuters mentions and staged HTML outputs. This leaves a leak path where disallowed Reuters references can still ship in generated/public artifacts.

## Change made (repo-level)
Updated `scripts/validate_docs_policy.py` to harden Reuters checks:
1. Expanded staged docs scanning from markdown-only to both `docs/*.md` and `docs/*.html`.
2. Added plain-text Reuters detection (`\breuters\b`) in addition to URL-host detection.
3. Preserved markdown-only title/slug policy checks while applying Reuters checks to all staged docs artifacts.

## Before/after checks
- Before:
  - Reuters detection scope: markdown files only.
  - Detection type: URL pattern only (`reuters.com`).
  - Gap: plain-text references and staged HTML could bypass this guard.
- After:
  - Reuters detection scope: staged markdown + HTML in docs.
  - Detection type: URL + plain-text references.
  - Result: tighter pre-commit guard against policy-incompatible sourcing leakage.

## Expected 7-14 day impact
- Fewer policy-reject surprises late in publish flow.
- Lower risk of accidental Reuters references in public artifacts.
- Faster, cleaner cadence runs by failing early at commit-preflight stage with clearer constraint enforcement.
