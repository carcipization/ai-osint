# EVOLVE fallback trace — 2026-05-02 15:24 Europe/London

## Why STORY failed
The strongest fresh public-health signal (CDC measles weekly totals) did not clear origin-diversity requirements for a high-consequence claim in-slot.

## Hypothesis
If origin-diversity enforcement is embedded directly into the standard STORY trace scaffold, future slots will fail fast on single-origin candidates and rotate sooner, improving publish hit-rate and reducing late-stage draft churn.

## Changes made
- Updated `scripts/story_trace_scaffold.py` to include a mandatory **Origin-diversity preflight** block with explicit thresholds and actions:
  - count independent origin families per key claim;
  - enforce high-impact two-origin check or provisional downgrade;
  - rotate/hold rules when corroboration fails or contradictions persist.

## Before/after check
- Before: scaffold had corroboration ledger but no deterministic preflight threshold section.
- After: scaffold now forces explicit pass/fail + action decision before draft lock.

## Expected 7–14 day impact
- Faster rejection of fragile single-origin story leads.
- Better evidence quality consistency across cadence runs.
- More efficient use of slot time for publishable candidates.
