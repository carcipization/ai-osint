# TGA posted its largest one-day drawdown in two weeks, but SOFR stayed flat (osint-story)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-13-tga-posted-largest-one-day-drawdown-in-two-weeks-but-sofr-stayed-flat-osint-story.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-13-tga-posted-largest-one-day-drawdown-in-two-weeks-but-sofr-stayed-flat-osint-story.md)

**Dateline:** 2026-03-13 03:01 UTC

## Story
The U.S. Treasury General Account (TGA) fell by $57.035 billion in the latest Daily Treasury Statement, dropping from $862.841 billion on March 10 to $805.806 billion on March 11.

That was a 6.61% day-over-day decline and the largest one-day drawdown in the recent two-week window, based on the same official Treasury series. The move reverses a short rebuild sequence seen earlier this week and reintroduces a near-term liquidity-watch question.

The strongest challenge to a stress interpretation is in funding prices: the New York Fed’s Secured Overnight Financing Rate (SOFR) was unchanged at 3.64 on the latest print. In other words, a large Treasury cash swing appeared without an immediate rise in the main secured overnight rate.

Why it matters: for treasury and funding desks, this is a watch signal rather than a one-print regime break. A repeat pattern of large TGA drawdowns or rebuilds paired with firmer funding rates would be a stronger trigger for liquidity posture changes than this single move on its own.

What could overturn this conclusion: if upcoming sessions show continued large cash swings and SOFR (or related secured funding measures) starts to rise materially, the current "monitor, don’t overreact" stance would likely need to shift.

## Appendix: Method
- Pulled U.S. Treasury FiscalData Daily Treasury Statement operating cash balance series.
- Extracted TGA closing balances for March 10 and March 11 and recomputed absolute and percentage change.
- Checked recent-session context by comparing one-day changes across the latest two-week period.
- Cross-checked immediate funding conditions using New York Fed SOFR recent prints.

## Appendix: Limitations
- Daily Treasury Statement values can revise.
- This check uses a short lookback window; longer seasonal settlement patterns are not modeled here.
- SOFR is a key but not exhaustive measure of short-term funding stress.

## Appendix: Confidence
**Confidence:** Medium

Rationale: High confidence in Treasury balance arithmetic and SOFR level on the latest print; medium confidence in broader liquidity interpretation until follow-on sessions confirm persistence or reversal.

## Appendix: Sources
- U.S. Treasury FiscalData, Daily Treasury Statement operating cash balance: [https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance?sort=-record_date&page%5Bsize%5D=500](https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance?sort=-record_date&page%5Bsize%5D=500)
- FiscalData dataset documentation, Daily Treasury Statement operating cash balance: [https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/operating-cash-balance](https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/operating-cash-balance)
- New York Fed SOFR recent prints (`last/10.json`): [https://markets.newyorkfed.org/api/rates/secured/sofr/last/10.json](https://markets.newyorkfed.org/api/rates/secured/sofr/last/10.json)
