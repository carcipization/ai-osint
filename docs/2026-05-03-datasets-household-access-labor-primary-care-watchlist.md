# Datasets: Household Access, Labor Stress, and Primary Care Coverage Watchlist

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-05-03-datasets-household-access-labor-primary-care-watchlist.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-05-03-datasets-household-access-labor-primary-care-watchlist.md)

**Dateline:** 2026-05-03 09:50 UTC

This one-off datasets run adds three net-new, primary-source datasets focused on everyday consequence surfaces: food-access infrastructure for low-income households, local labor-market deterioration risk, and frontline healthcare appointment access.

## What was added

1. **SNAP Retailer Locator Historical Data (USDA FNS)**  
   URL: [https://www.fns.usda.gov/snap/retailer-locator/data](https://www.fns.usda.gov/snap/retailer-locator/data)  
   Why it matters: gives tract/ZIP-adjacent retailer presence and churn context to test whether affordability shocks are also turning into practical access frictions.

2. **BLS Local Area Unemployment Statistics (LAUS)**  
   URL: [https://www.bls.gov/lau/](https://www.bls.gov/lau/)  
   Why it matters: high-frequency county/metro unemployment signals help connect macro labor moves to likely near-term pressure on rent, food, and utility payment resilience.

3. **NHS England GP Appointments Data Hub**  
   URL: [https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/gp-appointments-data](https://digital.nhs.uk/data-and-information/data-tools-and-services/data-services/gp-appointments-data)  
   Why it matters: appointment volume and timeliness indicators provide direct service-access evidence for primary care strain affecting household decision-making.

## Selection notes

- Prioritized broad non-specialist consequence over technical convenience.
- Kept to direct raw-data access endpoints (download/API/dashboard export), not catalog wrappers.
- Kept intake independent of wire-media leads and anchored to primary-source dataset ecosystems.

## Next-use impact chain

These additions strengthen near-term cross-domain chain coverage:
- **Labor stress -> affordability pressure** (LAUS)
- **Affordability pressure -> food-access infrastructure exposure** (SNAP retailer footprint)
- **Household strain -> primary-care access friction** (NHS GP appointments)
