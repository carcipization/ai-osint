# Research Trace — 2026-03-11 Fed overnight reverse repo usage near zero

## Testable question
Has Federal Reserve overnight reverse repo (ON RRP) usage dropped to a materially new low that changes near-term liquidity-monitoring priorities for cash managers?

## Evidence ledger

1) https://fred.stlouisfed.org/graph/fredgraph.csv?id=RRPONTSYD
- Publisher: Federal Reserve Bank of St. Louis (FRED), series sourced from New York Fed temporary open market operations
- Retrieved: 2026-03-11 04:04 UTC
- Classification: **Observation**
- What it shows: Daily aggregated ON RRP accepted amount (billions of dollars).
- Mechanical recompute from downloaded CSV:
  - Latest value (2026-03-10): **$0.278 billion**
  - Previous 20-operation average: **$1.993 billion**
  - Latest vs previous 20-operation average: **-86.05%**
  - Same date one year earlier (2025-03-10): **$129.054 billion**
  - Year-over-year change: **-99.78%**
  - 2026 readings below $1 billion: **12 of 46** operations in the year-to-date sample.
- Limitation: FRED republishes upstream data; final values can be revised if source corrections occur.

2) https://markets.newyorkfed.org/api/rp/all/all/results/lastTwoWeeks.json
- Publisher: Federal Reserve Bank of New York (Markets API)
- Retrieved: 2026-03-11 04:04 UTC
- Classification: **Observation**
- What it shows: Operation-level results for recent repo/reverse repo activity.
- Key matching observations:
  - 2026-03-10 ON RRP total accepted amount: **$278,000,000** with 4 counterparties.
  - 2026-03-09 ON RRP total accepted amount: **$332,000,000**.
- Limitation: Endpoint is rolling-window recent history, not a full historical archive in a single pull.

3) https://www.newyorkfed.org/markets/rrp_faq
- Publisher: Federal Reserve Bank of New York
- Retrieved: 2026-03-11 04:04 UTC
- Classification: **Observation** for policy mechanics, **Inference** for implications
- What it shows: ON RRP operations are run daily to support policy implementation; facility shifts liabilities between reserves and reverse repos while SOMA size remains unchanged.
- Limitation: FAQ explains mechanism but does not itself provide trend statistics.

## Contradiction pass
- Disconfirming hypothesis: The near-zero print is an isolated calendar effect and not a meaningful regime-level shift.
- Checks run:
  - Confirmed two consecutive sub-$0.4 billion prints in New York Fed operation results (Mar. 9 and Mar. 10).
  - Compared latest print against both short-run baseline (20-operation average) and one-year-ago value.
- Result: Direction and magnitude remain consistent with a sustained low-usage regime rather than a single-day anomaly.

## Could this be wrong because...
- Quarter-end or tax-date cash movements could temporarily pull usage away from ON RRP and then reverse.
- Data may revise after publication windows.
- Facility usage can stay low even when broader money-market stress emerges elsewhere.

Evidence that would invalidate or weaken current conclusion:
- A multi-session rebound back into double-digit billions.
- Policy-rate or technical-adjustment changes that alter relative attractiveness of ON RRP versus bill holdings.

Status: No invalidating evidence found in this pass; confidence assessed as medium-high on the directional claim, moderate on persistence horizon.
