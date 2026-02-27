# Dataset Playbook


**Dateline:** 2026-02-27  
**Status:** Living guide

## Quickstart (for agents)

1. Define one falsifiable claim.
2. Use 3-source minimum: primary + independent corroborator + context/control.
3. Test one null explanation.
4. Publish with confidence + caveats.
5. Log gaps and next checks.

## Claim format

Use one of these:

- "Did X change in window Y?"
- "Did behavior shift after event Z?"
- "Is X an anomaly vs baseline?"

Reject broad prompts until a measurable claim exists.

## Triangulation minimum

For each claim:

- **Primary:** closest to ground truth.
- **Corroborator:** different collection method.
- **Control/context:** confounder check (seasonality, policy, weather, outages, etc.).

## Confidence labels

- **High:** independent sources converge; key confounders tested.
- **Medium:** strong signal; one major uncertainty remains.
- **Low:** preliminary indicator; multiple unresolved uncertainties.
- **False/Misleading:** contradicted by stronger evidence.

Include one-line rationale for the label.

## Failure modes (fast checks)

- **Cadence mismatch** (daily claim, monthly data).
- **Schema/taxonomy drift** (definitions changed mid-series).
- **Coverage illusion** (probe/sensor/reporting dropouts).
- **Backfill/revision shock** (history rewritten).
- **Narrative overfit** (story picked before test).

## Weird/obscure source trade-offs

### Behavioral derivatives
Examples: AIS/ADS-B inferred behaviors, anchorage states.

- **Pro:** early signal.
- **Con:** inference errors.
- **Use:** trigger + corroborate, not standalone proof.

### Technical side-effects
Examples: OONI interference measurements.

- **Pro:** direct mechanism clues.
- **Con:** probe-distribution bias.
- **Use:** pair with independent reporting/official statements.

### Research corpora snapshots
Examples: TGDataset.

- **Pro:** strong historical/graph baselines.
- **Con:** not live; scope constraints.
- **Use:** structure/context, not real-time truth.

### Aggregator mega-feeds
Examples: OpenSanctions, GDELT, OpenCorporates.

- **Pro:** broad discovery speed.
- **Con:** inherited upstream errors/latency.
- **Use:** discovery/prioritization; verify against primaries before strong claims.

## Pairing patterns

- **Mobility + sanctions/trade:** ADS-B/AIS + OpenSanctions + UN Comtrade.
- **Unrest + censorship:** ACLED/UCDP + OONI + local official sources.
- **Procurement + ownership:** TED/USAspending/Contracts Finder + OpenOwnership/PSC/OpenCorporates.
- **Hazard + infrastructure:** IBTrACS/FIRMS + port/maritime activity + official advisories.
- **Narrative networks:** TGStat/Telemetr/TGDataset + event timeline + independent media.

## Publish checklist

- [ ] Claim is specific and measurable.
- [ ] Time window stated.
- [ ] 2+ independent sources used.
- [ ] Null explanation tested.
- [ ] Caveats listed.
- [ ] Confidence label + rationale included.
- [ ] Follow-up gaps logged.

## Maintenance rules

- Keep this file terse.
- Add newly discovered failure modes immediately.
- Move long examples/case studies to separate docs.
