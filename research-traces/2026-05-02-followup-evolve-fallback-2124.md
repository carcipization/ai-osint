# EVOLVE fallback — FOLLOWUP slot — 2026-05-02 21:24 Europe/London

## Why FOLLOWUP did not publish
No materially conclusion-changing primary evidence emerged after required follow-up checks.

## Hypothesis
Embedding explicit FOLLOWUP query-log fields in the standard trace scaffold will improve compliance reliability and make no-publish decisions faster to audit.

## Change made
- Updated `scripts/story_trace_scaffold.py` to include a dedicated `FOLLOWUP social/context query log` section with required fields:
  - Bluesky query list (>=5)
  - Polymarket query list (>=3)
  - top findings
  - explicit conclusion-impact note

## Before/after
- Before: requirement existed in policy but not codified in scaffold output.
- After: scaffold now prompts mandatory capture, reducing omission risk.

## Expected impact (7–14 days)
- Higher FOLLOWUP run consistency.
- Faster auditability of publish/no-publish rationale.
- Lower compliance drift when runs are time-constrained.
