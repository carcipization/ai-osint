# Datasets: added revision-sensitive retrieval lens and flag-handling rule

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-06-datasets-optimize-revision-sensitive-retrieval-lens.html)  
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-06-datasets-optimize-revision-sensitive-retrieval-lens.md)

**Dateline:** 2026-03-06 18:07 UTC

## What changed

Catalog quality/structure was improved without adding or removing datasets.

Changes in `docs/datasets-catalog.md`:
- Added a **Revision-sensitive series** retrieval lens under “Retrieval lenses”.
- Added a maintenance rule requiring explicit surfacing of revision/provisional flags in downstream story method/limitations when sources expose them.
- Refreshed catalog dateline.

## Why this matters

Some high-value official feeds expose estimated/provisional/break-in-series markers. Without a retrieval-level reminder, cadence stories can overstate trend certainty from unstable points.

This optimization improves triage and confidence calibration:
- analysts can quickly identify which series need confidence-capped interpretation,
- publication notes can consistently explain revision risk,
- no dataset churn was introduced.

## Files updated

- `docs/datasets-catalog.md`

## Source links

- [Updated datasets catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
- [Eurostat API detailed guidelines](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics)
- [World Bank indicator API reference](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
