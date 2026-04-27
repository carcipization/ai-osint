# EVOLVE trace — Reuters-ban prepublish guard (2026-04-27)

**Run UTC:** 2026-04-27 02:27 UTC
**Slot:** EVOLVE

## Hypothesis
A recurring quality/compliance failure mode is Reuters links entering draft/published docs posts despite current sourcing policy. The highest-leverage fix is to enforce this at commit-time in the existing publication-policy gate, not via ad hoc reviewer memory.

## Changes made (repo-level)
- Updated `scripts/validate_docs_policy.py` to detect and block Reuters links in staged docs markdown files.
- Added regex guard:
  - `https?://(?:www\.)?reuters\.com/`
- Validator now emits a blocking error:
  - `reuters links disallowed in docs publication: <file>`

## Before/after check
- Before: policy validator enforced slug/title class constraints only; Reuters links could still pass if title/slug were valid.
- After: staged docs posts containing Reuters URLs fail policy validation before commit/publish.

## Expected impact (7-14 days)
- Lower policy-violation risk in STORY outputs.
- Faster editorial cycle by failing invalid drafts immediately.
- Better alignment with current sourcing constraints without adding manual process overhead.
