# Dataset Playbook

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/dataset-playbook.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/dataset-playbook.md)

**Dateline:** 2026-03-04 21:31 UTC
**Status:** Living guide

## Purpose
Operational guide for turning dataset signals into publishable OSINT stories.

Use this for both:
- **Verification mode** (test a concrete claim), and
- **Discovery mode** (find a story candidate in data).

## Core operating loop
1. Define one falsifiable claim/question.
2. Run significance gate: why it matters if true/false, and who is affected.
3. Set scope (window, geography, domain, minimum evidence).
4. Collect primary evidence first.
5. Triangulate with at least 2 independent source classes.
6. Compare against baseline (not raw counts alone).
7. Test at least one null/alternative explanation.
8. Publish with confidence + limitations + decision relevance.
9. Log follow-up triggers and revisit cadence.

## Claim formats
- “Did X change in window Y?”
- “Did behavior shift after event Z?”
- “Is X an anomaly vs baseline?”

Reject broad narrative prompts until a measurable question exists.

## Triangulation minimum
For each consequential claim:
- **Primary:** closest available ground-truth source.
- **Corroborator:** different collection method/source class.
- **Control/context:** confounder check (seasonality, policy, weather, outages, calendar effect, revisions).

## Discovery mode (when no claim exists yet)
Scan for:
1. **Baseline breaks:** level/slope shifts vs rolling history.
2. **Concentration shifts:** flows/spend/ownership moving into fewer entities.
3. **Decouplings:** metrics that usually track each other diverge.
4. **Cross-border reroutes:** corridor substitutions after policy/sanctions pressure.
5. **Cross-domain synchrony:** independent systems moving together in time.

Promote a candidate to full story only if all are true:
- one falsifiable claim can be written,
- >=2 independent sources exist,
- one plausible null can be tested quickly.

## Fast candidate scoring
Score 1–5 each:
- Signal strength
- Corroboration availability
- Public stakes
- Actionability (publishable now)
- False-positive risk (inverse)

Prioritize high signal + high corroboration + low/medium FP risk.

## Evidence reliability tiers
- **Tier 1 (strongest):** official registries, agency/statistical releases, primary filings.
- **Tier 2:** machine-coded/model-derived feeds and telemetry products.
- **Tier 3:** third-party aggregators/social-derived indicators.

Publishing rule of thumb:
- Hard claims should include Tier 1, or convergent multi-source Tier 2 evidence with explicit caveats.

## Dataset quality keys (for catalog maintenance + story triage)
- **Access:** Open / registration / restricted
- **Format:** API / CSV / dashboard / mixed
- **Revision risk:** Low / Medium / High
- **Operational role:** Baseline / anomaly detection / corroboration / lead generation

## Starter bundles (quick triage patterns)
- **Conflict escalation:** ACLED + GDELT + ReliefWeb
- **Internet shutdown:** OONI + RIPE/IODA + official telecom notices
- **Energy stress (EU):** AGSI+ + ENTSO-E + Pink Sheet context
- **Trade reroute/sanctions:** UN Comtrade + OpenSanctions + AIS/maritime source
- **AI capability vs risk:** HELM + Epoch compute + AI Incident Database
- **Cyber exploitation tempo:** CISA KEV + EPSS + NVD

## Confidence labels
- **High:** independent sources converge; confounders tested.
- **Medium:** core finding supported; key dependency unresolved.
- **Low:** preliminary signal with substantial uncertainty.
- **False/Misleading:** stronger evidence contradicts claim.

Always include a one-line rationale for the label.

## Failure modes checklist
- Cadence mismatch (daily claim, monthly source)
- Schema/taxonomy drift
- Coverage illusion/probe dropout
- Backfill/revision shock
- Base-rate neglect
- Narrative lock-in
- Source monoculture
- False precision on tiny denominators

## Story output minimum
- Headline
- **Dateline:** YYYY-MM-DD HH:MM UTC
- Why this update now
- Evidence (numbered, linked)
- Method (reproducible)
- Hypotheses and adjudication (for STORY slots)
- Limitations
- Confidence + rationale
- One-line decision relevance

## Follow-up triggers
Run follow-up immediately when:
- primary source correction/reclassification lands,
- independent source materially changes confidence,
- magnitude/trajectory moves beyond prior uncertainty bounds,
- downstream real-world impact appears.

Default revisit cadence:
- High velocity: 6–24h
- Medium: 1–3d
- Low: 3–14d

## Catalog optimization rules
- Optimize for signal density first, compactness second.
- Default to shrinking/holding size; growth needs explicit operational value.
- Remove speculative sections not tied to active workflows.
- Prefer replace/merge over append-only edits.
- If a pass grows size, document rationale and schedule cleanup.

## Related
- Dataset list: [`datasets-catalog.md`](./datasets-catalog.md)
