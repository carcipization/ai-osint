# Datasets: health, mobility, and household pressure stack (watchlist 98)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-10-dataset-intel-health-mobility-and-household-pressure-stack-watchlist-98.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-10-dataset-intel-health-mobility-and-household-pressure-stack-watchlist-98.md)

**Dateline:** 2026-04-10 18:03 UTC

This DATASETS_B cycle adds five machine-readable datasets that improve consequence-first monitoring across hospital baseline capacity, airfare affordability and route pressure, homelessness system load, and overdose emergency burden.

## Added in this run

- **[Licensed and Certified Healthcare Facility Bed Types and Counts](https://catalog.data.gov/dataset/licensed-and-certified-healthcare-facility-bed-types-and-counts-ad4df)** — facility-level bed-type capacity counts for California providers, useful for baseline care-capacity and surge-bottleneck checks.
- **[Consumer Airfare Report: Table 1a - All U.S. Airport Pair Markets](https://catalog.data.gov/dataset/consumer-airfare-report-table-1a-all-u-s-airport-pair-markets)** — airport-pair fare and passenger-volume data for national route-level travel-cost and access monitoring.
- **[Consumer Airfare Report: Table 6 - Contiguous State City-Pair Markets That Average At Least 10 Passengers Per Day](https://catalog.data.gov/dataset/consumer-airfare-report-table-6-contiguous-state-city-pair-markets-that-average-at-least-1)** — medium/high-traffic city-pair fare panel for concentration and fare-premium shift tracking.
- **[DHS Daily Report](https://catalog.data.gov/dataset/dhs-daily-report)** — daily New York City shelter census/service-load data for homelessness pressure and capacity trend checks.
- **[Opioid EMS Calls](https://catalog.data.gov/dataset/opioid-ems-calls-ac2fc)** — incident-level overdose-related EMS response calls in Tempe, Arizona for high-frequency local emergency burden monitoring.

## Why this stack matters

- **Health capacity + acute burden linkage:** bed-type capacity and overdose call pressure provide a stronger operational picture than either alone.
- **Mobility affordability consequence:** route-level airfare changes can quickly alter household travel access and small-business operating costs.
- **Housing-system stress visibility:** daily shelter census data gives near-operational insight into homelessness system load rather than annual snapshots.

## Practical use pattern

1. Track bed-capacity and shelter-load baselines for stress thresholds.
2. Monitor city-pair airfare shifts for sudden accessibility/cost pressure.
3. Pair overdose EMS call spikes with local hospital-load context before causal claims.
4. Use multi-dataset triangulation to distinguish temporary noise from persistent pressure.

## Caveats

- Several additions are subnational (California, NYC, Tempe) and should not be over-generalized nationally.
- Administrative and operational datasets can revise after backfills.
- Route composition and seasonal travel patterns can affect airfare comparability.

## Appendix: Sources

- Data.gov catalog (all datasets linked above)
