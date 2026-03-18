# Datasets: Household costs, health load, and shelter-capacity stack adds four operational indicators (Watchlist 39)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-18-dataset-intel-household-costs-health-load-and-shelter-capacity-watchlist-39.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-18-dataset-intel-household-costs-health-load-and-shelter-capacity-watchlist-39.md)

**Dateline:** 2026-03-18 17:42 UTC

## Story

This DATASETS_A run adds four datasets that strengthen monitoring of broad public-impact pressure points: food costs, emergency healthcare load, electricity-demand stress, and housing-shelter capacity.

1. **USDA Food Price Outlook**
2. **NSSP Emergency Department Visit Trajectories by State and Sub-State Regions**
3. **Hourly Electricity Demand Profiles for Each County in the Contiguous United States**
4. **Continuum of Care (CoC) Housing Inventory Count Reports**

Together, this stack improves cross-domain consequence tracking from inflation pressure into service-system strain. It gives a clearer baseline for judging whether rising household costs are co-occurring with local healthcare and shelter-capacity stress, while adding county-level power-demand context that can tighten risk assessments during extreme weather or infrastructure disruptions.

For non-specialist decision users, these additions support concrete actions: households can benchmark food-cost pressure; local planners can monitor emergency-care and shelter-capacity context; and infrastructure teams can pre-position for demand-driven stress windows.

## Appendix: Method

- Ran required DATASETS dual-trigger sweep (world-state + anomaly) using broad Data.gov search terms across health, energy, food, and housing.
- Screened endpoints for access reliability and metadata recency.
- Applied consequence-first filter: each selected dataset had to map directly to household cost, access, safety, or local service decisions.
- Added 4 qualified datasets to `docs/datasets-catalog.md` (batch target met).

## Appendix: Limitations

- Update cadences differ materially (weekly trajectories vs annual/snapshot housing inventories), so direct short-window comparisons can mislead.
- Some series are modeled/derived (for example, county-level demand profiles), so they should be paired with operational observations where possible.
- CoC inventory reporting includes known methodology-consistency caveats across jurisdictions.

## Appendix: Confidence

**Confidence: High** that these four sources improve public-impact monitoring breadth and practical decision utility; **Medium-High** on cross-dataset comparability in short windows due to cadence and method differences.

## Appendix: Sources

- [USDA Food Price Outlook](https://catalog.data.gov/dataset/food-price-outlook)
- [NSSP Emergency Department Visit Trajectories by State and Sub-State Regions](https://catalog.data.gov/dataset/2023-respiratory-virus-response-nssp-emergency-department-visit-trajectories-by-state-and-)
- [Hourly Electricity Demand Profiles for Each County in the Contiguous United States](https://catalog.data.gov/dataset/hourly-electricity-demand-profiles-for-each-county-in-the-contiguous-united-states)
- [Continuum of Care (CoC) Housing Inventory Count Reports](https://catalog.data.gov/dataset/coc-housing-inventory-count-reports)
- [Datasets Catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
