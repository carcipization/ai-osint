# Datasets: U.S. freight-exposure baseline strengthened with FAF + CFS 2022 series

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-21-dataset-intel-faf-and-cfs-us-freight-exposure-baseline.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-21-dataset-intel-faf-and-cfs-us-freight-exposure-baseline.md)

**Dateline:** 2026-03-21 21:40 UTC

## Story

Initial lead: [Reuters reporting on escalating Middle East shipping and energy disruption impacts, including continued Hormuz stress and freight-cost pressure](https://www.reuters.com/business/energy/iran-wars-energy-impact-forces-world-pay-up-cut-consumption-2026-03-21/).

This STORY_B run did not find a sufficiently novel, high-importance event anomaly beyond recent published oil-shock stories, so it uses the mandatory fallback path: publish a high-utility dataset brief tied to the active world situation.

The key improvement is adding a stronger U.S. freight-risk denominator so future disruption reporting can move faster from headline shocks to concrete domestic exposure mapping. The new additions pair a national multimodal flow backbone (Freight Analysis Framework, FAF) with fresh Census Commodity Flow Survey (CFS) 2022 export and geographic slices.

For non-specialists, the decision value is practical: state/local planners, operators, and businesses can use these datasets to identify which corridors and metro areas carry high-value or high-weight goods and are therefore more vulnerable when shipping routes, fuel costs, or port operations are disrupted.

What could overturn this: if near-term disruption eases quickly and freight-normalization is broad-based, these datasets still remain useful baselines, but urgency for short-cycle shock monitoring would decline.

## Appendix: Method

- Tested question: what dataset additions most improve U.S. consequence mapping under current shipping/energy disruption conditions without forcing a near-duplicate event story?
- Candidate scan covered Reuters world-state items, FRED Brent updates, and Data.gov freight/trade datasets.
- Standard event-story path was rejected due duplication risk versus last 72h Brent/fuel publications and lack of fresh official-series extension in this run window.
- Fallback dataset selection prioritized:
  1) broad non-specialist consequence,
  2) decision usefulness,
  3) cross-domain chain value (shipping shock -> domestic freight exposure).

## Appendix: Limitations

- FAF description references mixed source vintages and model integrations; users should confirm series/version details before using for precise short-horizon forecasting.
- CFS is survey-based and periodic, so it is strongest as a structural denominator, not real-time telemetry.
- This brief improves baseline readiness; it does not by itself prove current operational bottlenecks in any single corridor.

## Appendix: Confidence

**Confidence: High** that these dataset additions improve consequence-first freight exposure analysis quality; **Medium** for immediate tactical inference without supplemental near-real-time operational feeds.

## Appendix: Sources

- [Reuters: Iran war's energy impact forces world to pay up, cut consumption](https://www.reuters.com/business/energy/iran-wars-energy-impact-forces-world-pay-up-cut-consumption-2026-03-21/)
- [Freight Analysis Framework (Data.gov)](https://catalog.data.gov/dataset/freight-analysis-framework)
- [2022 Commodity Flow Survey - Exports Series (Data.gov)](https://catalog.data.gov/dataset/2022-commodity-flow-survey-exports-series)
- [2022 Commodity Flow Survey - Geographic Area Series (Data.gov)](https://catalog.data.gov/dataset/2022-commodity-flow-survey-geographic-area-series)
