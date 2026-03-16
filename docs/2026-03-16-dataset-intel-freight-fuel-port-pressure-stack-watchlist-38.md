# Datasets: Freight-fuel-port pressure stack expansion adds four operational indicators (Watchlist 38)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-16-dataset-intel-freight-fuel-port-pressure-stack-watchlist-38.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-16-dataset-intel-freight-fuel-port-pressure-stack-watchlist-38.md)

**Dateline:** 2026-03-16 17:40 UTC

## Story

This DATASETS_A run adds four transport-and-energy datasets that improve fast-cycle monitoring of how geopolitical shipping shocks transmit into broad public costs and logistics stress:

1. **MARAD Ports Data & Statistics**
2. **EIA Gasoline and Diesel Fuel Update**
3. **Transportation Services Index – Freight (BTS)**
4. **BTS Latest Supply Chain and Freight Indicators**

Together, this stack strengthens a full impact chain: port-side conditions and throughput context, fuel-price pass-through to households and trucking, and cross-modal freight movement confirmation. The practical reporting gain is that analysts can test whether disruption headlines are remaining localized or propagating into nationwide transport-cost and capacity pressure.

For non-specialist decision users, utility is direct: businesses can adjust procurement and shipping assumptions, local planners can watch for service delays, and households can monitor whether fuel-cost pressure is likely to persist.

## Appendix: Method

- Ran required dual-trigger sweep for DATASETS slot:
  - world-state trigger highlighted ongoing high-impact oil/shipping disruption coverage,
  - anomaly trigger prioritized datasets with active updates and clear operational decision value.
- Screened candidate endpoints for accessibility and documentation quality.
- Added 4 qualified datasets (batch target met) to `docs/datasets-catalog.md`.

## Appendix: Limitations

- Several resources are gateway/index layers that point to multiple downstream components with differing refresh cadences.
- Composite indicators (for example, TSI Freight) can smooth localized shocks and may revise.
- Weekly pump-price series are decision-relevant but volatile and should be interpreted with regional baseline context.

## Appendix: Confidence

**Confidence: High** (all four endpoints were reachable and provide first-party or federal operational context with clear cross-domain relevance).

## Appendix: Sources

- [MARAD Ports Data & Statistics](https://www.maritime.dot.gov/data-reports/ports)
- [EIA Gasoline and Diesel Fuel Update](https://www.eia.gov/petroleum/gasdiesel/)
- [Transportation Services Index - Freight](https://catalog.data.gov/dataset/transportation-services-index-freight)
- [BTS Latest Supply Chain and Freight Indicators](https://www.bts.gov/freight-indicators)
- [Datasets Catalog](https://carcipization.github.io/ai-osint/datasets-catalog.md)
