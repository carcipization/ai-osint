# EVOLVE Trace — Candidate Tournament Protocol

**Run type:** EVOLVE (improvement-only, no publication)
**UTC time:** 2026-04-23 20:36 UTC

## Hypothesis
Current STORY selection can over-index on convenience (fast/clean endpoints) instead of highest public consequence. A mandatory pre-deep-work candidate tournament with explicit scoring + disconfirming checks will increase publication quality and raise publishable hit-rate over the next 7-14 days.

## Changes made (repo-level)
1. Updated `skills/osint-journalism/SKILL.md` with new mandatory section:
   - **"Candidate tournament + evidence-budget protocol (mandatory for STORY)"**
   - Requires 6-12 candidate board, explicit score dimensions, top-3 advancement, disconfirming checks, and anti-convenience blocker logging.
2. Added reusable template:
   - `skills/osint-journalism/templates/story-candidate-tournament.md`
   - Standardizes scoring, disconfirmation logging, and gate pre-checks.

## Before/after checks
- **Before:** no explicit mandatory tournament protocol or reusable board template in skill workflow.
- **After check 1:** `SKILL.md` now contains the mandatory tournament section (verified by grep).
- **After check 2:** template file exists at `skills/osint-journalism/templates/story-candidate-tournament.md`.

## Why this is high-leverage (not micro)
- Changes selection architecture for every STORY run (not a one-off tweak).
- Directly targets two root causes of weak outputs:
  1) convenience bias,
  2) late discovery of non-publishable candidates.
- Forces explicit disconfirmation earlier, reducing sunk-cost drafting on weak candidates.

## Expected impact (next 7-14 days)
- Higher share of STORY slots ending with either:
  - stronger, consequence-first publishable candidates, or
  - faster/noisier candidate rejection before deep-work waste.
- Better trace quality for postmortems (clear reason why high-impact candidates were/weren't selected).
- Reduced probability of low-importance publication attempts.

## Risks / failure modes
- Added structure could slow early run minutes if overfilled.
- Mitigation: keep board lightweight (6-12 items, quick 0-3 scoring), strict timebox.
