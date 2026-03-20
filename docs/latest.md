# Datasets: Food-input pass-through and flood-claims pressure baselines expand (Watchlist 44)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-20-dataset-intel-food-input-and-flood-claims-pressure-baselines-watchlist-44.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-20-dataset-intel-food-input-and-flood-claims-pressure-baselines-watchlist-44.md)

**Dateline:** 2026-03-20 17:39 UTC

This datasets-only run adds three high-consequence baselines to improve coverage of (a) upstream food-cost pressure transmission and (b) recurring household flood-loss exposure. Together they strengthen cross-domain tracking from input shocks to consumer prices and from hazard events to repeated insurance claims burden.

## Added datasets (3)

1. **Fertilizer Use and Price**  
   URL: [https://catalog.data.gov/dataset/fertilizer-use-and-price](https://catalog.data.gov/dataset/fertilizer-use-and-price)  
   Why it matters: Adds long-run nutrient and fertilizer price context for farm-input stress, a key upstream driver of food production costs that can later pass through to household grocery inflation.

2. **Price Spreads from Farm to Consumer**  
   URL: [https://catalog.data.gov/dataset/price-spreads-from-farm-to-consumer](https://catalog.data.gov/dataset/price-spreads-from-farm-to-consumer)  
   Why it matters: Adds direct farm-to-retail spread evidence to test whether consumer food-price movement is farm-cost driven, processing/marketing-system driven, or mixed.

3. **FIMA NFIP Redacted Claims (OpenFEMA)**  
   URL: [https://catalog.data.gov/dataset/fima-nfip-redacted-claims-openfema](https://catalog.data.gov/dataset/fima-nfip-redacted-claims-openfema)  
   Why it matters: Adds transaction-level flood-claims context for repeated household loss pressure and insurance burden persistence across disaster cycles.

## Decision-use framing

- **Households:** better context for whether food inflation pressure is likely to persist from farm-input channels versus retail-chain dynamics.
- **Local/state planners:** better longitudinal signal on recurring flood claims pressure when evaluating mitigation prioritization and recovery strategy.
- **OSINT workflow:** tighter linkage between hazard → claims burden and input costs → shelf-price outcomes.

## Method notes

- Slot policy: DATASETS_A (datasets-only), with required batch size met (3 additions).
- Selection prioritized broad non-specialist consequence and cross-domain chain value over convenience.
- Catalog entries were added with caveats on cadence, revisions, and comparability.

## Sources

- [https://catalog.data.gov/dataset/fertilizer-use-and-price](https://catalog.data.gov/dataset/fertilizer-use-and-price)
- [https://catalog.data.gov/dataset/price-spreads-from-farm-to-consumer](https://catalog.data.gov/dataset/price-spreads-from-farm-to-consumer)
- [https://catalog.data.gov/dataset/fima-nfip-redacted-claims-openfema](https://catalog.data.gov/dataset/fima-nfip-redacted-claims-openfema)
