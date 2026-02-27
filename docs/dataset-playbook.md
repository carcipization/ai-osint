# Dataset Playbook (General-purpose OSINT)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/dataset-playbook.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/dataset-playbook.md)

**Dateline:** 2026-02-27  
**Desk:** AI-OSINT Methods  
**Status:** Living guide

## Why this exists
This playbook is a practical operating guide for turning datasets into high-confidence, verification-first stories.

It is designed to be:
- **General-purpose** (works across geopolitics, security, infrastructure, climate, domestic risk, AI governance)
- **Repeatable** (same checks every cycle)
- **Auditable** (easy to trace claims back to source evidence)

---

## Core operating model

### 1) Start with a falsifiable question
Use a concrete claim shape:
- "Did X increase/decrease in Y timeframe?"
- "Did behavior shift after event Z?"
- "Is this pattern unusual versus baseline?"

Avoid vague prompts like "what looks interesting?" until after baseline checks are done.

### 2) Build a minimum triangulation set
For each story angle, use at least:
- **1 primary dataset** (closest to ground truth)
- **1 independent corroborator** (different collection method)
- **1 context/control source** (to test confounders)

### 3) Separate signal from mechanics
Before interpreting meaning, test whether the pattern can be explained by:
- release cadence changes,
- schema changes,
- backfills/revisions,
- temporary outages/coverage shifts,
- platform policy changes.

### 4) State confidence explicitly
Use labels consistently:
- **Confirmed** (multiple independent sources align)
- **Likely** (strong but incomplete evidence)
- **Inconclusive** (insufficient or conflicting evidence)
- **False/Misleading** (claim contradicted by stronger evidence)

### 5) Preserve auditability
Every published claim should include:
- source URLs,
- time window,
- metric definition,
- caveats,
- what would change the conclusion.

---

## Dataset selection framework

When deciding whether to use a dataset in production cycles, score it on:

1. **Coverage fit** — Does it actually cover the geography/time/topic needed?
2. **Cadence fit** — Is update frequency appropriate for the claim horizon?
3. **Method transparency** — Is collection/processing method documented?
4. **Revision behavior** — Are backfills/re-writes common?
5. **Reproducibility** — Can someone else independently rerun your logic?
6. **Operational friction** — API reliability, licensing, auth burden, cost.

High story value with low methodological transparency is allowed for scouting, but should be tagged as provisional.

---

## Workflow by cycle (practical)

### A) Scout
- Pull candidate anomalies from high-cadence feeds.
- Discard anything that cannot be expressed in a measurable way.

### B) Verify
- Re-query at least one independent source.
- Compare against a recent baseline and seasonal window if relevant.

### C) Stress-test
- Check known failure modes (coverage gaps, reporting lag, dedupe issues, taxonomy drift).
- Attempt one plausible null explanation.

### D) Publish
- Keep claim narrow.
- Include confidence and caveats.
- Log unresolved verification gaps as explicit follow-ups.

### E) Catalog maintenance
- Add high-value sources to `datasets-catalog.md`.
- Keep entries short, practical, and comparable.

---

## Common failure modes (and fixes)

- **Cadence mismatch** → comparing daily claims against monthly datasets.
  - *Fix:* align claim horizon to release frequency.

- **Taxonomy drift** → category definitions changed mid-series.
  - *Fix:* re-normalize or split pre/post periods.

- **Coverage illusions** → apparent drop is sensor/reporting dropout.
  - *Fix:* add coverage/probe-density control metric.

- **Narrative overfitting** → selecting evidence to fit a prior.
  - *Fix:* write the disconfirming test first.

- **Cross-domain overreach** → jumping from correlation to causation.
  - *Fix:* phrase as hypothesis unless causal chain is evidenced.

---

## Weird/obscure sources: trade-offs and usage

These sources can be extremely high-yield, but require stronger caveats discipline.

### A) Behavioral-derivative datasets
Examples: Global Fishing Watch anchorage behavior, AIS/ADS-B derived activity states.

- **Strength:** detects pattern changes before formal reporting catches up.
- **Risk:** inferred states can be wrong in edge cases.
- **Best use:** early warning + triangulation trigger, not standalone proof.

### B) Technical-side-effect datasets
Examples: OONI network interference measurements.

- **Strength:** can reveal censorship/disruption mechanics directly.
- **Risk:** probe distribution and local network quirks can bias interpretation.
- **Best use:** corroborate platform-blocking narratives with explicit uncertainty.

### C) Governance/incident curation datasets
Examples: AI Incident Database (AIAAIC).

- **Strength:** structured chronology of complex sociotechnical harms.
- **Risk:** not exhaustive; media/reporting bias matters.
- **Best use:** trend context and divergence checks, paired with primary incident docs.

### D) Research corpora snapshots
Examples: TGDataset (public Telegram channels), benchmark archives.

- **Strength:** rich historical graph analysis and longitudinal modeling.
- **Risk:** snapshot staleness and collection-scope constraints.
- **Best use:** structural baseline building; avoid treating as live ground truth.

### E) Aggregator mega-feeds
Examples: OpenSanctions, GDELT, OpenCorporates (aggregated registry paths).

- **Strength:** broad, fast discovery across jurisdictions/domains.
- **Risk:** inherited upstream errors and uneven source latency.
- **Best use:** discovery and prioritization; escalate to primary records for final claims.

---

## Pairing patterns that work well

- **Mobility + sanctions/trade:** ADS-B/AIS + OpenSanctions + UN Comtrade
- **Unrest + censorship:** ACLED/UCDP + OONI + local official statements
- **Procurement + ownership:** TED/USAspending/Contracts Finder + OpenOwnership/PSC/OpenCorporates
- **Climate hazard + infrastructure risk:** IBTrACS/FIRMS + maritime/port activity + official advisories
- **Narrative networks:** TGStat/Telemetr/TGDataset + event timeline + independent reporting

---

## Confidence rubric (recommended wording)

- **High confidence:** independent sources converge; known confounders tested.
- **Moderate confidence:** signal is strong but one key uncertainty remains.
- **Low confidence:** preliminary indicator only; multiple unresolved uncertainties.

Always include one-line rationale for confidence level.

---

## Publication checklist (short form)

Before publish, confirm:
- [ ] Claim is specific and measurable
- [ ] Time window is explicit
- [ ] At least two independent sources used
- [ ] One plausible null explanation tested
- [ ] Caveats listed
- [ ] Confidence level stated
- [ ] Follow-up data gaps logged

---

## Maintenance policy

- Review this playbook when adding a new dataset class.
- If a failure mode is discovered in production, add it here immediately.
- Keep this file concise and operational; move long case studies to separate docs.

This file is intentionally a living methods guide, not a static manifesto.