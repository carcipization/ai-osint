# Datasets: maternal, hospital-capacity, and utility-service pressure stack (watchlist 96)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-10-dataset-intel-maternal-hospital-and-utility-service-pressure-stack-watchlist-96.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-10-dataset-intel-maternal-hospital-and-utility-service-pressure-stack-watchlist-96.md)

**Dateline:** 2026-04-10 09:52 UTC

This DATASETS_A cycle adds four machine-readable datasets that strengthen consequence-first monitoring across maternal health, hospital load, household utility service quality, and local food-safety enforcement.

## Added in this run

- **[VSRR Provisional Maternal Death Counts and Rates](https://catalog.data.gov/dataset/vsrr-provisional-maternal-death-counts)** — U.S. provisional maternal mortality signal with direct CSV/JSON access for early trend checks before finalized annual vital-statistics releases.
- **[COVID-19 Reported Patient Impact and Hospital Capacity by Facility -- RAW](https://catalog.data.gov/dataset/covid-19-reported-patient-impact-and-hospital-capacity-by-facility-raw)** — Facility-level U.S. hospital utilization and capacity data (including inpatient/ICU burden fields) for localized surge and health-system stress monitoring.
- **[Utility Company Customer Service Response Index (CSRI): Beginning 2005](https://catalog.data.gov/dataset/utility-company-customer-service-response-index-csri-beginning-2005)** — New York utility customer-service response index time series for measuring complaint-response performance and persistent service friction.
- **[HHS - Food Inspection Data from July 2024 and onward](https://catalog.data.gov/dataset/hhs-food-inspection-data-from-july-2024-and-onward)** — Montgomery County (MD) food-establishment inspection records with violation/outcome fields for local public-health and compliance-risk checks.

## Why these matter together

- **Maternal + facility capacity linkage:** Maternal mortality risk interpretation is stronger when read alongside real-time facility-capacity constraints and surge periods.
- **Household consequence layer:** Utility complaint-response performance provides an operational measure of whether households are getting timely resolution during billing/outage stress.
- **Public-health ground signal:** Local inspection outcomes add near-operational food-safety context that can surface neighborhood-level service and enforcement pressure.

## Practical use pattern

1. Track maternal provisional mortality direction and reporting-vintage shifts.
2. Cross-check hospital burden by geography and week for capacity context.
3. Monitor utility response-index deterioration for service-friction escalation.
4. Add food-inspection violation density as a local environmental-health pressure indicator.

## Constraints and caveats

- Provisional mortality and facility feeds can revise; trend confidence should be recalibrated after backfills.
- Utility CSRI and food-inspection datasets are subnational and should not be over-generalized nationally.
- Cross-dataset conclusions should separate measured association from causal attribution.
