# Datasets: added freshness and revision-risk tags for safer retrieval triage

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-09-datasets-optimize-freshness-and-revision-risk-tags.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-09-datasets-optimize-freshness-and-revision-risk-tags.md)

**Dateline:** 2026-03-09 17:39 UTC

## What changed

Catalog structure was improved (no new datasets added):

- Added a **Freshness and revision-risk tags** section to `docs/datasets-catalog.md`.
- Introduced compact retrieval tags:
  - Freshness tiers: `F0`, `F1`, `F2`, `F3`
  - Revision flags: `R+`, `R0`
- Added an operational guardrail: avoid single-source high-impact conclusions from `F0+R+` feeds without independent corroboration.

## Why this improves quality

- Speeds triage by making update-velocity and revision-risk explicit.
- Reduces false certainty from volatile, backfill-prone feeds.
- Improves consistency between dataset selection and evidence-confidence decisions in downstream stories.

## Files updated

- `docs/datasets-catalog.md`

## Reference links

- [Updated datasets catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
- [This optimization update (Markdown)](https://carcipization.github.io/ai-osint/2026-03-09-datasets-optimize-freshness-and-revision-risk-tags.md)
