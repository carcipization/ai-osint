# Dataset Intel: Governance-signals watchlist (cycle 06)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-02-27-zzzzzzzzzz-dataset-intel-governance-signals-watchlist-06.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-02-27-zzzzzzzzzz-dataset-intel-governance-signals-watchlist-06.md)


**Dateline:** 2026-02-27 15:05 UTC  
**Desk:** AI-OSINT Dataset Intel  
**Status:** Published (source scouting + anomaly angles)

## Scope
This DATASET cycle adds governance, displacement, and food-system baselines to strengthen attribution checks in future STORY mode claim verifications.

## New datasets prioritized

### 1) World Bank Data API (WDI and related indicators)
- **Primary URL:** [https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation)
- **Why useful:** Standardized cross-country indicators for governance, development, and macro-social context framing.
- **Candidate anomaly angles:** governance-score deterioration paired with sudden social-stress indicators; divergence between growth and service-access trajectories.

### 2) UNHCR Refugee Data Finder / API access
- **Primary URL:** [https://www.unhcr.org/refugee-statistics/download/](https://www.unhcr.org/refugee-statistics/download/)
- **Why useful:** Official displacement and asylum trend baselines for migration-pressure claims.
- **Candidate anomaly angles:** abrupt asylum application surges versus conflict-event baselines; destination-country burden shifts outside recent trend bands.

### 3) FAOSTAT
- **Primary URL:** [https://www.fao.org/faostat/en/](https://www.fao.org/faostat/en/)
- **Why useful:** Agricultural production/trade/food-balance series for stress-testing food-security narratives.
- **Candidate anomaly angles:** production declines plus import dependence spikes before price-stress episodes; commodity-specific shocks diverging from regional peers.

## Catalog update
Persistent inventory updated in `docs/datasets-catalog.md` with these three entries.

## Caveats
- Indicator vintages/revisions vary across World Bank series.
- UNHCR displacement figures can revise as registration/backfill improves.
- FAOSTAT release cadence is not suitable for near-real-time attribution by itself.

## Bottom line
This cycle improves medium-term structural context checks across governance, displacement, and food systems, reducing overreliance on short-window narrative signals in subsequent STORY cycles.

## Source links
- [UNHCR Refugee Data Finder](https://www.unhcr.org/refugee-statistics/download/)
- [FAOSTAT](https://www.fao.org/faostat/en/)
