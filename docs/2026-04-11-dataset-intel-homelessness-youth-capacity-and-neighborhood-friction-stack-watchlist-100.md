# Datasets: homelessness, youth capacity, and neighborhood-friction stack (watchlist 100)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-11-dataset-intel-homelessness-youth-capacity-and-neighborhood-friction-stack-watchlist-100.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-11-dataset-intel-homelessness-youth-capacity-and-neighborhood-friction-stack-watchlist-100.md)

**Dateline:** 2026-04-11 09:41 UTC

This DATASETS_A cycle adds four machine-readable datasets that improve consequence-first monitoring of shelter pressure, youth housing capacity, and neighborhood service-friction signals.

## Added in this run

- **[DHS Daily Report (Historical)](https://catalog.data.gov/dataset/dhs-daily-report-historical)** — pre-2021 New York City daily shelter census and application-flow history for longer baseline and regime-shift checks.
- **[DHS Data Dashboard](https://catalog.data.gov/dataset/dhs-data-dashboard)** — demographic composition of households in NYC shelter services, useful for targeting support where burden concentration shifts.
- **[Runaway and Homeless Youth (RHY) Daily Census](https://catalog.data.gov/dataset/runaway-and-homeless-youth-rhy-daily-census)** — daily bed availability and vacancy metrics across youth crisis and transitional housing programs.
- **[Noise Complaints](https://catalog.data.gov/dataset/noise-complaints)** — Montgomery County complaint-level noise records from 311/web channels with near-daily refresh.

## Why this stack matters

- **Household protection decisions:** shelter census and historical baseline layers improve early warning for overflow and sustained housing stress.
- **Youth-specific service risk:** RHY bed vacancy data helps distinguish total-system pressure from youth-program bottlenecks.
- **Neighborhood quality-of-life pressure:** noise complaint surges can reveal localized service friction that often precedes broader municipal strain narratives.

## Practical use pattern

1. Build current-vs-historical shelter pressure baselines using current and historical DHS series.
2. Segment by demographic composition to detect burden concentration shifts.
3. Track RHY vacancy rates as an operational slack indicator for youth placement risk.
4. Cross-check local complaint spikes with weather, events, and service disruptions before causal claims.

## Caveats

- Three of four additions are NYC-scoped and should not be generalized nationally.
- Complaint datasets reflect reporting behavior and enforcement pathways, not all underlying incidents.
- Administrative social-service datasets can revise with backfills or category-policy updates.

## Appendix: Sources

- Data.gov catalog (all datasets linked above)
