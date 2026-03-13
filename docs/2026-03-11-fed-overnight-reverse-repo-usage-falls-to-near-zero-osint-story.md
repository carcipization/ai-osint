# Fed overnight reverse repo usage falls to near zero, shifting cash-market watchpoints

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-11-fed-overnight-reverse-repo-usage-falls-to-near-zero-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-11-fed-overnight-reverse-repo-usage-falls-to-near-zero-osint-story.md)

**Dateline:** 2026-03-11 04:06 UTC

## Story
Federal Reserve overnight reverse repo usage has dropped to a fresh post-tightening low, with New York Fed operations showing just $278 million accepted on March 10 after $332 million the day before. That leaves a facility that once absorbed trillions of dollars operating near zero in daily take-up.

Recomputed daily data from the St. Louis Fed’s FRED series (which mirrors New York Fed operation totals) show the March 10 print is down 86.05% from the previous 20-operation average of about $1.99 billion, and down 99.78% from $129.05 billion on the same date a year earlier.

The signal is not that cash has vanished from money markets. The New York Fed’s operational FAQ says overnight reverse repo (ON RRP) activity mainly shifts Federal Reserve liabilities between bank reserves and reverse repos while the central bank’s securities holdings stay unchanged. In plain terms, cash that previously sat in ON RRP is increasingly being parked elsewhere, especially in short-dated Treasury bills.

Why it matters: for treasury desks, money market funds and bank liquidity teams, ON RRP is becoming less useful as a standalone stress gauge. With balances now near floor levels, monitoring should shift toward bill-auction demand, reserve distribution and secured funding rates for earlier warning of any funding pressure.

## Appendix: Method
- Pulled and recomputed the FRED daily ON RRP series (`RRPONTSYD`) from CSV.
- Calculated latest value, prior 20-operation average, and year-over-year comparison (same calendar date).
- Cross-checked latest values against the New York Fed Markets API operation results endpoint (`lastTwoWeeks.json`) for operation-level confirmation.
- Used New York Fed FAQ for mechanism context only (not for numerical trend claims).

## Appendix: Limitations
- FRED series is a republished feed and can reflect upstream revisions.
- Recent-operation API window is rolling and does not by itself provide full-history context.
- A low ON RRP level does not rule out localized funding stress in other instruments.

## Appendix: Confidence
**Confidence:** Medium-High

Rationale: High confidence in the observed near-zero readings and arithmetic cross-check; moderate confidence in persistence because quarter-end balance-sheet dynamics can temporarily change facility demand.

## Appendix: Sources
- FRED ON RRP daily series (`RRPONTSYD`): [https://fred.stlouisfed.org/graph/fredgraph.csv?id=RRPONTSYD](https://fred.stlouisfed.org/graph/fredgraph.csv?id=RRPONTSYD)
- New York Fed Markets API, recent operation results: [https://markets.newyorkfed.org/api/rp/all/all/results/lastTwoWeeks.json](https://markets.newyorkfed.org/api/rp/all/all/results/lastTwoWeeks.json)
- New York Fed ON RRP FAQ: [https://www.newyorkfed.org/markets/rrp_faq](https://www.newyorkfed.org/markets/rrp_faq)
