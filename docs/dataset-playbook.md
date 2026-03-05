# Dataset Playbook

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/dataset-playbook.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/dataset-playbook.md)

**Dateline:** 2026-03-05 21:40 UTC
**Status:** Living guide

## Purpose
Operational guide for **dataset intake and catalog quality**.

This is **not** the story-writing guide.
Use this to discover, score, and promote datasets in batches.

## Hard separation from STORY workflow
- Do **not** run AP/story preflight for dataset selection.
- Do **not** require narrative publishability checks to add datasets.
- Story framing belongs in story/claim-check workflows only.

## Core dataset loop (batch-first)
1. Run wide ingest (`make bulk-intake`) and gather candidate sources at scale.
2. Deduplicate/canonicalize by source and endpoint.
3. Score candidates (relevance, reproducibility, update cadence, access).
4. Promote top qualified candidates to catalog/watchlists in **batches**.
5. Record caveats + intended operational use for each promoted dataset.
6. Log rejects briefly (why excluded) to avoid re-triage churn.

## Batch defaults
- Discovery target: tens/hundreds of candidates per run when tooling allows.
- Promotion default: **3–10 qualified datasets per cycle**.
- Single-dataset promotion is an exception and must include a reason in trace notes.

## Scoring rubric (1–5)
- Domain relevance to active reporting lanes
- Source authority/provenance
- Reproducibility/access reliability
- Update cadence freshness
- Complementarity (adds new coverage vs duplicate signal)
- Noise/false-positive risk (inverse)

Prioritize: high relevance + high authority + high reproducibility + medium/low noise.

## Evidence tiers for dataset quality
- **Tier 1:** official registries, agencies, primary institutional releases
- **Tier 2:** structured telemetry/model-derived systems
- **Tier 3:** aggregators/social-derived feeds

Catalog can include Tier 2/3, but mark caveats clearly.
High-stakes verification should anchor on Tier 1 when available.

## Promotion criteria (dataset-level)
Promote when all are true:
- Source is real, reachable, and stably identifiable
- Operational use-case is concrete
- Caveats are known/documented
- It adds coverage breadth or materially improves existing lane quality

## Output format for DATASET posts (lean)
- What changed this cycle (count + list)
- Added datasets (name, URL, domain, access, update cadence)
- Why each matters operationally (1–2 lines)
- Key caveats/limitations (brief)
- Catalog files touched
- Trace/reference links

Avoid story-style sections like “Why this update now”, AP preflight, or editorial verdict.

## Catalog maintenance rules
- Optimize for retrieval speed and signal density.
- Prefer replace/merge over append-only sprawl.
- Remove stale/low-utility entries when better substitutes exist.
- Keep taxonomy consistent and compact.

## Related
- Dataset list: [`datasets-catalog.md`](./datasets-catalog.md)
- Story and claim-check style rules: [`../skills/osint-journalism/SKILL.md`](../skills/osint-journalism/SKILL.md)
