# Datasets: openFDA recall and adverse-event stack (watchlist 110)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-17-dataset-intel-openfda-recall-and-adverse-event-stack-watchlist-110.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-17-dataset-intel-openfda-recall-and-adverse-event-stack-watchlist-110.md)

**Dateline:** 2026-04-17 14:31 UTC

This DATASETS cycle adds five machine-readable FDA datasets to strengthen rapid safety monitoring where product recalls and adverse-event signals can change household and healthcare decisions.

## Added in this run

- **[openFDA Drug Enforcement Reports API](https://open.fda.gov/apis/drug/enforcement/)** — drug recall enforcement records with recall class, reason, and distribution scope.
- **[openFDA Food Enforcement Reports API](https://open.fda.gov/apis/food/enforcement/)** — food recall and market-withdrawal records for contamination-risk triage.
- **[openFDA Device Enforcement Reports API](https://open.fda.gov/apis/device/enforcement/)** — medical-device recall actions for patient-safety and care-disruption monitoring.
- **[openFDA Drug Adverse Event API (FAERS)](https://open.fda.gov/apis/drug/event/)** — adverse-event reports for medicine safety-signal scans.
- **[openFDA Device Adverse Event API (MAUDE)](https://open.fda.gov/apis/device/event/)** — medical-device adverse-event reports for implant and equipment risk monitoring.

## Why this stack matters

- **Broad non-specialist consequence:** recalls and adverse events can rapidly affect household consumption choices, medicine availability, and clinical equipment trust.
- **Decision usefulness:** supports practical decisions for consumers (avoidance/substitution), providers (risk communications), and local operators (stock and response planning).
- **Cross-domain chain value:** links upstream regulatory safety actions to downstream care access and service continuity effects.

## Practical use pattern

1. Monitor weekly recall volume and Class I/II mix changes across food, drug, and device streams.
2. Cross-reference affected products with pharmacy/clinical access context to identify potential substitution pressure.
3. Track adverse-event signal clustering by product classes to prioritize deeper verification and follow-up reporting.
4. Escalate only when movement is persistent and mapped to concrete public-facing consequences.

## Caveats

- openFDA endpoints are curated from FDA reporting systems and can include reporting lag, deduplication challenges, and ongoing case updates.
- Adverse-event reports are not direct causality findings; they are signal inputs that require corroboration.
- Recall distribution geography can be incomplete or updated as investigations evolve.

## Appendix: Sources

- openFDA API dataset pages linked above.