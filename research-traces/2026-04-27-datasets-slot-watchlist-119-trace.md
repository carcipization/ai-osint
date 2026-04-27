# DATASETS slot trace (watchlist 119) — 2026-04-27

**Run UTC:** 2026-04-27 14:24 UTC  
**Slot:** DATASETS

## First-principles framing
- Core question: which net-new datasets add broad non-specialist consequence coverage and improve decision-useful STORY discovery in coming cycles?
- Required qualities: direct raw-data access, repeatable retrieval, cross-domain chain value, and clear household/service consequence relevance.
- Falsification path: reject candidates that are metadata wrappers, duplicate existing catalog entries, or narrow specialist telemetry without practical downstream consequence.

## Candidate scan and overlap checks

Tested candidate families:
1. HDX HAPI humanitarian indicator shards (operational presence, needs/response, food prices)
2. WHO machine-readable global health indicators
3. UN machine-readable SDG baseline indicators

Rejected examples during overlap pass:
- World Bank Indicators API (already cataloged)
- ECB Data Portal API (already cataloged)

## Added datasets (5)
1. https://data.humdata.org/dataset/hdx-hapi-operational-presence
2. https://data.humdata.org/dataset/hdx-hapi-humanitarian-needs
3. https://data.humdata.org/dataset/hdx-hapi-food-price
4. https://ghoapi.azureedge.net/api/
5. https://unstats.un.org/SDGAPI/v1/sdg/Goal/List

## Non-specialist consequence screen
- Operational presence + HNRP indicators: improves verification of whether response capacity tracks crisis burden affecting shelter, food, and core services.
- Food-price indicators: direct household affordability and nutritional-access relevance.
- WHO GHO + UN SDG baselines: strengthens denominator context for public-health and infrastructure-consequence reporting across countries.

## Blockers / reliability notes
- No hard endpoint failures in final selected set during access checks.
- FAOSTAT API candidate timed out from this environment during test and was not added in this cycle.

## Publication decision
- Publish DATASETS_INTEL update: **yes**.
- Added 5 datasets (meets batch rule 3-10; single-add avoided).
