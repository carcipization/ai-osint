# SKILL trace — fail-closed STORY importance adjudication upgrade

**Date:** 2026-03-13
**Slot:** SKILL
**Scope:** tighten STORY importance enforcement to reduce convenience-led publication drift.

## Problem diagnosed
Recent cadence pressure can still reward "easy-to-measure" signals even when broad public consequence is marginal or unclear. Existing guidance had importance checks, but lacked a compact adjudication rubric that is mandatory and auditable per candidate.

## Change made
Updated `skills/osint-journalism/SKILL.md` by adding a new section:
- `Importance gate adjudication rubric (SKILL quality upgrade)`

New hard requirements:
1. One-line public-interest stake with explicit actor/action.
2. Broad-impact floor (non-specialist consequence required).
3. Convenience override check across top candidates.
4. Fail-closed rule (`importance_fail`) when ambiguous.
5. Mandatory `importance_adjudication` trace block for published STORY candidates.

## Why this improves output quality
- Converts a general importance principle into a repeatable, auditable decision step.
- Raises resistance to convenience bias (clean data / fast queries) when consequence magnitude is weak.
- Improves consistency with PRECEPTS editorial north star: story quality and real-world impact over process convenience.
