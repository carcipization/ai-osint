# EVOLVE fallback trace (from STORY no-publish)

**Run UTC:** 2026-04-23 20:24 UTC
**Trigger:** STORY slot failed publish gates; required fallback-to-EVOLVE executed.

## Hypothesis

Repeated 404s from rotating primary-source URLs (observed in recent follow-up traces for CDC and ENTSO-E paths) are introducing avoidable friction and can reduce effective evidence time in cadence slots.

If we codify a deterministic canonical-URL retry discipline in the journalism skill, source retrieval reliability should improve and reduce false "blocked source" outcomes.

## Changes made

1. Updated `skills/osint-journalism/SKILL.md` with new section:
   - `## Canonical-URL retry discipline for volatile publishers (quality upgrade)`
2. Added required procedure steps:
   - log first 404/410/redirect-loop with UTC;
   - retry from canonical hub/index page;
   - resolve canonical deep URL from hub;
   - proceed only after reachable canonical URL is confirmed;
   - log failed + replacement URL and final status in trace.

## Before/after checks

Before:
- Recent traces recorded ad-hoc URL corrections (example pattern: initial deep link 404 then manual switch to canonical URL).
- No explicit cross-slot standard in SKILL for this failure mode.

After:
- SKILL now has a named, deterministic procedure for URL churn handling.
- Future STORY/FOLLOWUP traces can be evaluated against explicit compliance steps.

## Expected impact on future publishability

- Lower time loss from URL churn during verification.
- Better consistency in blocked/error logging quality.
- Higher reliability of primary-source retrieval, improving odds that evidence packs complete within slot timeboxes.
