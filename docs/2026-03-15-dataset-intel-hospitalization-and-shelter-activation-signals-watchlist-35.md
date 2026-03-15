# Datasets: added hospitalization and shelter-activation signals for crisis service-pressure tracking (Watchlist 35)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-15-dataset-intel-hospitalization-and-shelter-activation-signals-watchlist-35.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-15-dataset-intel-hospitalization-and-shelter-activation-signals-watchlist-35.md)

**Dateline:** 2026-03-15 03:01 UTC

## Story

This DATASETS_B cycle adds three public-service stress datasets to improve rapid crisis-context verification:

- **Respiratory Virus Response (RVR) U.S. Hospitalization Metrics by Jurisdiction (Timeseries)**
- **National Shelter System Facilities**
- **Emergency Shelter Activation Status**

Together these sources strengthen a key response chain: healthcare demand pressure plus shelter-readiness posture. That helps distinguish whether disruption narratives are matched by measurable system stress and local protective actions.

For non-specialist decision users, this means faster answers to practical questions: are hospital occupancy signals rising across jurisdictions, where shelter capacity exists, and whether local authorities have activated emergency shelter operations.

## Appendix: Method

- Ran datasets-only discovery pass on Data.gov catalog for operational response indicators.
- Selected sources with direct service-impact relevance and machine-readable/public catalog availability.
- Added 3 datasets to `docs/datasets-catalog.md` (within required 3–10 range).

## Appendix: Limitations

- RVR metrics depend on reporting timeliness and may revise.
- National shelter facility inventories may lag real-time facility status.
- Shelter activation feed is jurisdiction-specific and not a national indicator.

## Appendix: Confidence

**Confidence: Moderate-High** (all three are authoritative public-catalog sources with clear operational value; caveats are mainly cadence and coverage scope).

## Appendix: Sources

- [Respiratory Virus Response (RVR) U.S. Hospitalization Metrics by Jurisdiction (Timeseries)](https://catalog.data.gov/dataset/respiratory-virus-response-rvr-united-states-hospitalization-metrics-by-jurisdiction-times)
- [National Shelter System Facilities](https://catalog.data.gov/dataset/national-shelter-system-facilities)
- [Emergency Shelter Activation Status](https://catalog.data.gov/dataset/emergency-shelter-activation-status)
- [Datasets Catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
