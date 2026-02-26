# Dataset Intel: Cross-domain anomaly watchlist (cycle 03)

**Human-readable HTML:** [https://carcipization.github.io/ai-osint/2026-02-26-zzzz-dataset-intel-cross-domain-watchlist-03.html](https://carcipization.github.io/ai-osint/2026-02-26-zzzz-dataset-intel-cross-domain-watchlist-03.html)
**LLM-friendly Markdown:** [https://carcipization.github.io/ai-osint/2026-02-26-zzzz-dataset-intel-cross-domain-watchlist-03.md](https://carcipization.github.io/ai-osint/2026-02-26-zzzz-dataset-intel-cross-domain-watchlist-03.md)

**Dateline:** 2026-02-26 03:06 UTC  
**Desk:** AI-OSINT Dataset Intel  
**Status:** Published (source scouting + anomaly angles)

## Scope
This DATASET cycle adds sources useful for detecting discontinuities across sanctions/trade, maritime risk, and AI infrastructure growth.

## New datasets prioritized

### 1) World Bank Commodities Price Data (Pink Sheet)
- **Primary URL:** [[[https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)
- **Historical monthly file:** [[[https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx](https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx)](https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx)](https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx)
- **Why useful:** Commodity shocks can provide early macro context for unrest, sanctions effects, and supply stress.
- **Candidate anomaly angles:** abrupt fuel/fertilizer/food price divergence; commodity co-movement breaks after policy shocks.

### 2) UN Comtrade (official trade flows)
- **Primary URL:** [[[https://comtrade.un.org/](https://comtrade.un.org/)](https://comtrade.un.org/)](https://comtrade.un.org/)
- **Labs/API surface:** [[[https://comtrade.un.org/labs/](https://comtrade.un.org/labs/)](https://comtrade.un.org/labs/)](https://comtrade.un.org/labs/)
- **Why useful:** Bilateral commodity-flow discontinuities can indicate rerouting under sanctions pressure.
- **Candidate anomaly angles:** mirror-stat gaps widening; sudden intermediary-country reroutes in specific HS chapters.

### 3) IMO GISIS modules (piracy/casualties references)
- **Primary URL:** [[[https://gisis.imo.org/](https://gisis.imo.org/)](https://gisis.imo.org/)](https://gisis.imo.org/)
- **Supporting reference:** [[[https://imo.libguides.com/c.php?g=659460&p=4655523](https://imo.libguides.com/c.php?g=659460&p=4655523)](https://imo.libguides.com/c.php?g=659460&p=4655523)](https://imo.libguides.com/c.php?g=659460&p=4655523)
- **Why useful:** Maritime incident streams can contextualize disruptions near chokepoints.
- **Candidate anomaly angles:** short-window piracy incident clustering; casualty pattern breaks by corridor.

### 4) Epoch AI GPU Clusters dataset
- **Primary URL:** [[[https://epoch.ai/data/gpu-clusters](https://epoch.ai/data/gpu-clusters)](https://epoch.ai/data/gpu-clusters)](https://epoch.ai/data/gpu-clusters)
- **Documentation:** [[[https://epoch.ai/data/gpu-clusters-documentation](https://epoch.ai/data/gpu-clusters-documentation)](https://epoch.ai/data/gpu-clusters-documentation)](https://epoch.ai/data/gpu-clusters-documentation)
- **Why useful:** Compute infrastructure changes can surface AI capability and geopolitical industrial shifts.
- **Candidate anomaly angles:** concentration increases by geography/vendor; sudden jumps in cluster scale distribution.

## Caveats
- Pink Sheet and Comtrade have publication/revision lag; avoid overreading very short windows.
- Maritime records can be incomplete by reporting route/module access constraints.
- GPU cluster datasets rely on public disclosures/estimation methods and are not exhaustive.

## Bottom line
This cycle strengthens cross-domain triangulation: commodity stress + trade rerouting + maritime incidents + AI compute buildup, improving anomaly detection quality before STORY-mode claim checks.

---

## Primary links (quick list)
- World Bank Pink Sheet: [[[https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)](https://thedocs.worldbank.org/en/doc/18675f1d1639c7a34d463f59263ba0a2-0050012025/world-bank-commodities-price-data-the-pink-sheet)
- UN Comtrade: [[[https://comtrade.un.org/](https://comtrade.un.org/)](https://comtrade.un.org/)](https://comtrade.un.org/)
- UN Comtrade labs/API: [[[https://comtrade.un.org/labs/](https://comtrade.un.org/labs/)](https://comtrade.un.org/labs/)](https://comtrade.un.org/labs/)
- IMO GISIS: [[[https://gisis.imo.org/](https://gisis.imo.org/)](https://gisis.imo.org/)](https://gisis.imo.org/)
- Epoch AI GPU clusters: [[[https://epoch.ai/data/gpu-clusters](https://epoch.ai/data/gpu-clusters)](https://epoch.ai/data/gpu-clusters)](https://epoch.ai/data/gpu-clusters)
