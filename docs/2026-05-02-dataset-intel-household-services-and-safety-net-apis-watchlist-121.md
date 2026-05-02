# Dataset Intel: Household services and safety-net APIs (Watchlist #121)
**Date (UTC):** 2026-05-02

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-05-02-dataset-intel-household-services-and-safety-net-apis-watchlist-121.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-05-02-dataset-intel-household-services-and-safety-net-apis-watchlist-121.md)

---

## Why this batch matters
This batch expands high-consequence, non-specialist monitoring around household stability: utility burden, food access, and local social-service demand. These are practical early-warning surfaces for cost stress and service-access deterioration before slower annual reports.

## Added datasets (3)

### 1) 211 Counts (AIRS / 211 network)
- **URL:** [https://search.211counts.org/](https://search.211counts.org/)
- **What it is:** Standardized local 211 call/request trends by need category (housing, utilities, food, mental health, etc.) across participating communities.
- **Why it’s useful:** Near-operational demand-side signal for household hardship and unmet basic-needs pressure.
- **Caveats:** Participation and taxonomy consistency vary by region; call volume reflects help-seeking behavior and access, not full underlying prevalence.

### 2) USDA Food Access Research Atlas
- **URL:** [https://www.ers.usda.gov/data-products/food-access-research-atlas/](https://www.ers.usda.gov/data-products/food-access-research-atlas/)
- **What it is:** U.S. tract-level indicators of low-income/low-access food environments and related access measures.
- **Why it’s useful:** Structural denominator for interpreting where food-price or transport shocks are most likely to hit household access.
- **Caveats:** Not high-cadence; best used as vulnerability baseline rather than incident-time nowcast.

### 3) U.S. Census SAIPE (Small Area Income and Poverty Estimates)
- **URL:** [https://www.census.gov/programs-surveys/saipe/data.html](https://www.census.gov/programs-surveys/saipe/data.html)
- **What it is:** County/school-district poverty and income estimates used widely for program allocation and local hardship benchmarking.
- **Why it’s useful:** Stable county-level poverty baseline for contextualizing changes in assistance demand and service-friction signals.
- **Caveats:** Annual model-based estimates; not designed for weekly shock detection.

## Selection notes
- Chosen for broad non-specialist consequence coverage (food, utilities, household hardship) and cross-domain chain value with existing safety-net and housing datasets.
- Prioritized net-new practical decision surfaces over narrowly technical telemetry.
