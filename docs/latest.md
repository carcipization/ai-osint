# Datasets: FAO FPMA adds market-level food-price stress tracking as global prices turn up

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-14-dataset-intel-fao-fpma-food-price-stress-tracking.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-14-dataset-intel-fao-fpma-food-price-stress-tracking.md)

**Dateline:** 2026-03-14 00:47 UTC

## Story

Initial lead: [FAO Food Price Index page (March 2026 update cycle)](https://www.fao.org/worldfoodsituation/foodpricesindex/en/).

Global food prices rising again is a broad public-risk signal because it can quickly affect household costs, humanitarian demand, and government subsidy decisions. In this run, no event-style candidate cleared the full STORY gate with a fresh mechanism break, so we executed mandatory fallback and added the **FAO Food Price Monitoring and Analysis (FPMA) Tool** to the datasets catalog.

The FPMA tool matters because it complements top-line global indexes with market-level commodity price series and country context. That gives decision-makers a faster way to distinguish between broad global movement and localized stress, which is often where affordability shocks become visible first.

For non-specialist users, the practical decision consequence is direct: FPMA can help answer whether a price jump is isolated or spreading across markets, which can change procurement timing, aid allocation, and household budgeting choices.

## Appendix: Method

- Ran one-off STORY sweep with world-state and anomaly triggers.
- Tested standard STORY candidates; none passed all anomaly/mechanism/decision + importance gates in this window.
- Ran mandatory fallback comparison across three source families before selection.
- Added **FAO FPMA Tool** to `docs/datasets-catalog.md` under **Humanitarian and hazard context**.
- Published dataset-focused explainer with source links and caveats.

## Appendix: Limitations

- FPMA coverage and update cadence vary by country, market, and commodity; not all markets update at the same speed.
- Price series are monitoring indicators and should be triangulated with local official statistics and field reporting before strong causal claims.
- This publication is a monitoring-infrastructure addition, not an assertion of a specific country-level food emergency.

## Appendix: Confidence

**Confidence: Moderate** (primary-source FAO documentation confirms scope and relevance; operational consistency depends on market-level update behavior).

## Appendix: Sources

- [FAO Food Price Monitoring and Analysis (FPMA) Tool](https://fpma.fao.org/giews/fpmat4/global/)
- [FAO Food Price Index](https://www.fao.org/worldfoodsituation/foodpricesindex/en/)
- [FAO Markets and Trade: FPMA Tool reference page](https://www.fao.org/markets-and-trade/do-not-touch/publications-original(2)/food-price-monitoring---analysis-(fpma)-tool---updated-version/en)
- [Datasets Catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
