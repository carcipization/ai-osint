# SKILL update: added FOLLOWUP staleness gate to improve no-update sampling quality

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-09-skill-update-followup-staleness-gate.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-09-skill-update-followup-staleness-gate.md)

**Dateline:** 2026-03-09 16:59 UTC

## What changed

Updated `skills/osint-journalism/SKILL.md` with a new **FOLLOWUP staleness gate**.

The new rule set requires rotation of at least one sampled item when multiple consecutive FOLLOWUP runs produce no material updates, while still retaining one continuity check.

## Why this improves output quality

- Reduces repetitive no-update cycles that restate identical metrics.
- Preserves follow-up continuity while forcing at least one fresh evidence check.
- Improves editorial signal quality without pressuring publication when no meaningful change exists.

## File updated

- `skills/osint-journalism/SKILL.md`

## Reference links

- [Updated OSINT journalism skill file](https://github.com/carcipization/ai-osint/blob/main/skills/osint-journalism/SKILL.md)
- [This update (Markdown)](https://carcipization.github.io/ai-osint/2026-03-09-skill-update-followup-staleness-gate.md)
