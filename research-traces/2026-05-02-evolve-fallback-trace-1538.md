# EVOLVE fallback trace — 2026-05-02 14:40 UTC

## Hypothesis
Story hit-rate is reduced by manual inconsistency in candidate challenge testing. Automating a structured challenge worksheet will speed falsification and rotate weak candidates faster.

## Change made (repo-level)
Added `scripts/story_challenge_sheet.py` to generate a standard challenge worksheet template with required fields (question, evidence checks, falsifier, baseline, independence, consequence, disposition).

## Before/after checks
- Before: ad-hoc notes, variable field coverage.
- After: deterministic template generated in seconds; enforces first-principles packet + challenge fields.

## Expected impact (7-14 days)
Higher throughput of candidate rotation, cleaner trace-to-copy mapping, and improved publication rate by reducing time spent on weak leads.
