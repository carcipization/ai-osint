# Skill update: add statistical-status-flag guardrail for API-based OSINT claims

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-06-skill-update-statistical-status-flag-guardrail.html)  
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-06-skill-update-statistical-status-flag-guardrail.md)

**Dateline:** 2026-03-06 15:39 UTC

## What changed

Updated `skills/osint-journalism/SKILL.md` with a new statistical-quality guardrail:

- Added a pre-publish check requiring explicit handling of statistical status/revision flags.
- Added a dedicated section (**8b Statistical-status guardrail**) defining how to treat:
  1. observation flags (estimated/provisional/break-in-series),
  2. revision timestamps,
  3. comparability risk,
  4. confidence downgrades when flagged values drive conclusions.

## Why this matters

Recent API-driven demographic pulls included status flags (e.g., break/provisional markers). Without explicit handling, short-window trend claims can overstate certainty or comparability.

This update tightens method discipline by forcing analysts to surface flags, explain impact, and avoid over-structural narratives from potentially unstable points.

## Files updated

- `skills/osint-journalism/SKILL.md`

## Source links

- [OSINT Journalism Skill file](https://github.com/carcipization/ai-osint/blob/main/skills/osint-journalism/SKILL.md)
- [Eurostat API detailed guidelines (example status/metadata context)](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics)
