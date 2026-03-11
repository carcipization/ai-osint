# TGA rebuilt after four-session drawdown, but funding gauges show no immediate stress (osint-story)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-11-tga-rebuilt-after-four-session-drawdown-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-11-tga-rebuilt-after-four-session-drawdown-osint-story.md)

**Dateline:** 2026-03-11 15:47 UTC

## Story
The U.S. Treasury General Account (TGA) posted a sharp one-session rebuild on the latest Daily Treasury Statement, ending March 9 at $858.548 billion after $833.086 billion on March 6. Treasury data show deposits of $44.750 billion and withdrawals of $19.289 billion for a net +$25.461 billion swing.

That breaks a short run of four straight withdrawal-dominant sessions and matters because TGA changes can shift liquidity conditions for banks and money markets. In plain terms, when Treasury cash rises at the Federal Reserve, private-sector reserves can be drained unless other flows offset it.

The strongest challenge to a stress narrative is in funding prices: the Secured Overnight Financing Rate (SOFR) did not rise alongside the cash rebuild, edging down from 4.34 to 4.33 on the latest print. That pattern indicates the move is, for now, more consistent with routine cash-management timing than with an immediate funding squeeze.

What could overturn this conclusion: if the next several Treasury statements continue rebuilding TGA while SOFR and related short-term funding rates begin to rise materially, the signal would shift from timing noise toward a tightening liquidity regime.

For treasury and funding desks, the actionable point is to monitor this as a sequence, not a single print: pair each Daily Treasury Statement update with next-day funding-rate behavior before changing cash or hedge posture.

## Appendix: Method
- Pulled Daily Treasury Statement operating-cash-balance records from Treasury FiscalData API.
- Extracted three line items for the latest session: TGA closing balance, total TGA deposits, and total TGA withdrawals.
- Recomputed net daily flow (deposits minus withdrawals) and checked arithmetic against closing-balance change.
- Cross-checked immediate market impact using SOFR daily series from FRED (New York Fed source series).

## Appendix: Limitations
- Daily Treasury Statement figures can be revised.
- One-day cash moves can reflect settlement and calendar effects, not structural regime change.
- SOFR alone does not capture every corner of short-term funding stress.

## Appendix: Confidence
**Confidence:** Medium

Rationale: High confidence in the observed Treasury cash arithmetic and latest SOFR print; medium confidence in interpretation because persistence needs multiple subsequent sessions.

## Appendix: Sources
- U.S. Treasury FiscalData API, Operating Cash Balance: [https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance?sort=-record_date&page%5Bsize%5D=500](https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance?sort=-record_date&page%5Bsize%5D=500)
- FiscalData dataset documentation, Daily Treasury Statement Operating Cash Balance: [https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/operating-cash-balance](https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/operating-cash-balance)
- FRED SOFR CSV: [https://fred.stlouisfed.org/graph/fredgraph.csv?id=SOFR](https://fred.stlouisfed.org/graph/fredgraph.csv?id=SOFR)