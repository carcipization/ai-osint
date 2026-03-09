# U.S. yield curve stayed positive in early 2026, but recession-risk signals remain mixed

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-09-us-yield-curve-stayed-positive-in-early-2026-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-09-us-yield-curve-stayed-positive-in-early-2026-osint-story.md)

**Dateline:** 2026-03-09 17:58 UTC

The U.S. Treasury yield curve measure that many recession watchers track most closely — the 10-year minus 3-month spread — remained positive through early March, according to Federal Reserve Bank of St. Louis data.

The spread printed 0.46 percentage points on March 6 and has not closed below zero since Oct. 16, 2025, a 95-trading-day positive run in the published series. In practical terms, that means the market has stayed in a normal, upward-sloping configuration for more than four months after a long inversion period.

The mechanism appears concentrated at the short end. The effective federal funds rate fell to 3.64% in February 2026 from 4.33% a year earlier, while the 10-year Treasury yield remained around 4.13% in early March, leaving a positive term spread.

For decision-makers, the signal is not that recession risk has disappeared. It is that single-indicator playbooks can misfire during transitions. The New York Fed recession-probability series carried on FRED remained nonzero in its latest monthly print, underscoring that model-based risk gauges can lag market-structure shifts. Portfolio, credit and hiring decisions that still assume an actively inverted curve should be re-checked against current rate-term data rather than legacy thresholds.

## Appendix: Method

- Pulled first-party CSV series from FRED for T10Y3M (10Y minus 3M spread), FEDFUNDS (effective federal funds rate), DGS10 (10-year Treasury), TB3MS (3-month Treasury), and RECPROUSM156N (recession probability series).
- Removed missing markers (`.`), then recomputed the latest-value check, last negative date, and current positive-streak length from the daily T10Y3M series.
- Calculated matched-window average spread for 2026-01-01 to 2026-03-06 versus the same month/day window in 2025.
- Used FEDFUNDS, DGS10 and TB3MS levels to test whether short-end easing plausibly explains sustained positive spread prints.

## Appendix: Limitations

- FRED-hosted series can be revised; near-term values may update after publication.
- Yield-curve slope is a market signal, not a direct recession measurement.
- The recession-probability model series is monthly and can lag daily market moves.
- This analysis identifies relationships in published rates; it does not estimate causal impact of any single policy decision.

## Appendix: Confidence

**Medium-high.** The core conclusion (sustained positive T10Y3M prints through the latest available date) is directly observed in first-party time series and mechanically reproducible. Confidence is lower on forward-looking interpretation because recession risk depends on broader macro variables beyond term structure alone.

## Appendix: Sources

1. [FRED CSV: 10-Year Treasury Constant Maturity Minus 3-Month Treasury Constant Maturity (T10Y3M)](https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y3M) — retrieved 2026-03-09 17:55 UTC
2. [FRED CSV: Effective Federal Funds Rate (FEDFUNDS)](https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS) — retrieved 2026-03-09 17:56 UTC
3. [FRED CSV: 10-Year Treasury Constant Maturity Rate (DGS10)](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10) — retrieved 2026-03-09 17:56 UTC
4. [FRED CSV: 3-Month Treasury Bill Secondary Market Rate (TB3MS)](https://fred.stlouisfed.org/graph/fredgraph.csv?id=TB3MS) — retrieved 2026-03-09 17:56 UTC
5. [FRED CSV: Smoothed U.S. Recession Probabilities (RECPROUSM156N)](https://fred.stlouisfed.org/graph/fredgraph.csv?id=RECPROUSM156N) — retrieved 2026-03-09 17:56 UTC
