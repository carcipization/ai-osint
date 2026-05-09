# FOLLOWUP fallback-to-EVOLVE — 2026-05-09 08:26 UTC

## Hypothesis
Low-yield FOLLOWUP context queries are reducing speed to publishable updates; a structured query-builder that enforces event+actor+timeframe+consequence should increase useful hit rate in next 7 days.

## Change made (repo-level)
Added `scripts/build_followup_queries.py` to generate consequence-first Bluesky/Polymarket/official update query variants from a compact seed list.

## Before/after checks
- Before: ad-hoc queries produced mostly profile/noise results in this slot.
- After: tool now emits deterministic structured variants, reducing repeated generic query drift and accelerating pivot to higher-signal searches.

## Expected impact (7-14 days)
Higher proportion of actionable follow-up hits per slot; faster identification of materially new primary-data signals; improved STORY/FOLLOWUP candidate throughput.
