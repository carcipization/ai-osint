# EVOLVE trace — 2026-05-02 — Source-diversity guardrail

## Hypothesis
A recurring failure mode is spending too long on candidates that later collapse to a single-origin evidence chain. If we force an early "origin map" check with a hard rotation trigger, we should increase publish hit-rate and reduce wasted slot time over the next 1–2 weeks.

## Changes made
1. Updated `skills/osint-journalism/SKILL.md` with a new **Origin-diversity preflight (mandatory for STORY/FOLLOWUP)** section.
2. Added a concrete source-family mapping workflow and hard fail/rotate thresholds:
   - classify each key claim's backing artifacts by upstream origin family;
   - block escalation if high-impact claims rely on one origin;
   - require explicit contradiction handling path before draft lock.

## Before check
- Existing guidance already encouraged independence checks, but did not enforce a concise preflight map with explicit stop/rotate thresholds at a fixed early point.
- Result: easier to drift into writing before detecting single-origin fragility.

## After check
- New preflight introduces a deterministic decision point before deep drafting.
- Candidate quality gate now explicitly ties claim criticality to required independent origin count.
- Rotation triggers are now concrete and fast to execute.

## Expected impact (7–14 days)
- Higher publication reliability: fewer stories that fail late due to origin collapse.
- Better slot throughput: faster discard of weak candidates and quicker rotation.
- Improved confidence calibration in publish/no-publish decisions.
