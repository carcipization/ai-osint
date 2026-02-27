# Dataset Playbook

**Human-readable HTML:** [https://carcipization.github.io/ai-osint/dataset-playbook.html](https://carcipization.github.io/ai-osint/dataset-playbook.html)
**LLM-friendly Markdown:** [https://carcipization.github.io/ai-osint/dataset-playbook.md](https://carcipization.github.io/ai-osint/dataset-playbook.md)



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

## Strategy mode

For exploratory "find me a story in the data" work, use [dataset-strategy.md](./dataset-strategy.md).

Use this playbook for claim verification and publication discipline.

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
## Related
- Strategy guide: [`dataset-strategy.md`](./dataset-strategy.md)

