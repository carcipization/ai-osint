# Datasets: housing and fiscal stress signal stack (watchlist 111)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-18-dataset-intel-housing-and-fiscal-stress-signal-stack-watchlist-111.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-18-dataset-intel-housing-and-fiscal-stress-signal-stack-watchlist-111.md)

**Dateline:** 2026-04-18 14:34 UTC

This DATASETS cycle adds four machine-readable federal datasets focused on household housing pressure and U.S. fiscal-flow risk context.

## Added in this run

- **[FHFA House Price Indexes (HPIs)](https://catalog.data.gov/dataset/fhfa-house-price-indexes-hpis-948c6)** — repeat-sales home-price index suite across national, state, metro, county, ZIP, and tract levels for tracking housing-cost divergence.
- **[Daily Treasury Statement (DTS)](https://catalog.data.gov/dataset/daily-treasury-statement-dts)** — daily Treasury cash and debt operations tables for short-cycle fiscal-liquidity monitoring.
- **[Monthly Treasury Statement (MTS)](https://catalog.data.gov/dataset/monthly-treasury-statement-mts)** — monthly receipts/outlays/deficit and financing flows for structural fiscal-balance tracking.
- **[Monthly Statement of the Public Debt (MSPD)](https://catalog.data.gov/dataset/monthly-statement-of-the-public-debt)** — debt stock composition by instrument and holder class for maturity and rollover-risk baselines.

## Why this stack matters

- **Broad non-specialist consequence:** shelter costs and federal fiscal pressure can cascade into mortgage affordability, public-service budgets, and borrowing conditions.
- **Decision usefulness:** supports household timing decisions (rent/buy/refinance), operator planning (housing and social services), and policy-risk monitoring.
- **Cross-domain chain value:** links household cost pressure (housing) with macro fiscal conditions that can amplify or dampen downstream economic stress.

## Practical use pattern

1. Track FHFA HPI acceleration/deceleration by geography to separate national narrative from local affordability shocks.
2. Use DTS for high-frequency detection of unusual cash/debt operation shifts, then verify persistence in MTS windows.
3. Use MSPD to test whether short-cycle fiscal changes are occurring alongside debt-composition or maturity-profile shifts.
4. Escalate to STORY only when movement is anomalous, mechanism-tested, and tied to clear non-specialist decision impact.

## Caveats

- Fiscal tables can include line-item definition updates and debt-limit-period nulls that require careful method notes.
- Monthly Treasury series are more stable than daily snapshots but still subject to revision and classification updates.
- FHFA geographies are powerful for comparison, but cross-geography interpretation requires consistent vintage and series-definition handling.

## Appendix: Sources

- Dataset pages linked above (Data.gov entries exposing machine-readable federal source feeds/tables).