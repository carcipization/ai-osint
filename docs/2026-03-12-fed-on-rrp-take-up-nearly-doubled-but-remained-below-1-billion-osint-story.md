# Fed ON RRP take-up nearly doubled but remained below $1 billion, reinforcing low-demand regime (osint-story)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-12-fed-on-rrp-take-up-nearly-doubled-but-remained-below-1-billion-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-12-fed-on-rrp-take-up-nearly-doubled-but-remained-below-1-billion-osint-story.md)

**Dateline:** 2026-03-12 03:22 UTC

## Story
Federal Reserve overnight reverse repo (ON RRP) usage rose to $552 million on March 11, up from $278 million a day earlier, according to New York Fed operation results. The increase is sharp in percentage terms, but the facility is still running at levels far below its recent operating range.

Recomputed from the New York Fed’s latest two-week operations feed, March 11 take-up was 98.6% above March 10 but still 80.9% below the prior 10-operation average of about $2.89 billion. In plain terms, money market funds used the facility more than the day before, but not in size that signals a return to heavy dependence.

The strongest challenge to a benign interpretation is that a one-day jump can sometimes be an early warning of cash-market friction. Fresh cross-checks do not yet support that. Treasury Daily Treasury Statement data show the Treasury General Account (TGA) rose by a modest $4.293 billion on the latest print, and the Secured Overnight Financing Rate (SOFR) eased by 1 basis point to 3.64 rather than rising.

Why it matters: for funding desks, this keeps the same near-term decision posture as prior sessions—treat ON RRP as a low-level, noisy indicator and prioritize confirmation from funding rates and upcoming bill-settlement flows before changing liquidity positioning.

What could overturn this conclusion: a multi-session rise in ON RRP accompanied by firmer SOFR or other secured funding rates would point to a broader tightening signal rather than day-to-day operational noise.

## Appendix: Method
- Pulled New York Fed repo operation results (`lastTwoWeeks.json`) and filtered overnight `Reverse Repo` rows.
- Recomputed day-over-day ON RRP change and comparison versus prior-operation average.
- Pulled U.S. Treasury FiscalData Daily Treasury Statement operating cash balance to recompute latest TGA close change.
- Pulled New York Fed SOFR recent prints (`last/10.json`) for immediate funding-price cross-check.

## Appendix: Limitations
- New York Fed operation endpoint used here is a rolling two-week window, not full-cycle history.
- ON RRP is one liquidity valve; stress can emerge first in instruments not captured by this measure.
- Daily Treasury Statement and rate series can revise.

## Appendix: Confidence
**Confidence:** Medium

Rationale: High confidence in the reported March 11 operation amount and arithmetic; medium confidence in regime interpretation because quarter-end dynamics can change facility demand quickly.

## Appendix: Sources
- New York Fed repo operation results (`lastTwoWeeks.json`): [https://markets.newyorkfed.org/api/rp/all/all/results/lastTwoWeeks.json](https://markets.newyorkfed.org/api/rp/all/all/results/lastTwoWeeks.json)
- U.S. Treasury FiscalData, Daily Treasury Statement operating cash balance: [https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance?sort=-record_date&page%5Bsize%5D=500](https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance?sort=-record_date&page%5Bsize%5D=500)
- New York Fed SOFR recent prints (`last/10.json`): [https://markets.newyorkfed.org/api/rates/secured/sofr/last/10.json](https://markets.newyorkfed.org/api/rates/secured/sofr/last/10.json)
