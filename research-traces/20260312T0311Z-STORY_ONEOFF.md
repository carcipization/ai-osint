# STORY one-off trace — 2026-03-12 03:11 UTC

## Testable question
Did New York Fed overnight reverse repo (ON RRP) usage move in a way that changes near-term funding-stress interpretation?

## Lane scan (freshness + availability)
1. **NY Fed ON RRP operations API** — available; fresh 2026-03-11 operation result posted.
2. **Treasury Daily Treasury Statement (DTS) operating cash balance** — available; fresh 2026-03-10 update posted.
3. **NY Fed SOFR reference rates API** — available; fresh 2026-03-10 fix posted.

Selected lane: ON RRP + cash/funding cross-check.

## Evidence ledger

- URL: https://markets.newyorkfed.org/api/rp/all/all/results/lastTwoWeeks.json  
  Publisher: Federal Reserve Bank of New York  
  Timestamp used: pull at 2026-03-12 ~03:15 UTC; latest operationDate 2026-03-11  
  What it proves: Overnight Reverse Repo accepted amount was $552 million on 2026-03-11 vs $278 million on 2026-03-10 (reverse repo, overnight rows).  
  Class: **Observation**  
  Limitation: Two-week window; limited long-history baseline in this endpoint.

- URL: https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance?sort=-record_date&page%5Bsize%5D=500  
  Publisher: U.S. Treasury FiscalData  
  Timestamp used: pull at 2026-03-12 ~03:16 UTC; latest record_date 2026-03-10  
  What it proves: TGA closing balance moved from $858.548 billion (Mar 9 close) to $862.841 billion (Mar 10 close), a +$4.293 billion increase.  
  Class: **Observation**  
  Limitation: Daily Treasury Statement values can revise; one-day changes are timing-sensitive.

- URL: https://markets.newyorkfed.org/api/rates/secured/sofr/last/10.json  
  Publisher: Federal Reserve Bank of New York  
  Timestamp used: pull at 2026-03-12 ~03:16 UTC; latest effectiveDate 2026-03-10  
  What it proves: SOFR printed 3.64 on 2026-03-10 vs 3.65 on 2026-03-09.  
  Class: **Observation**  
  Limitation: Single-rate check; does not capture all funding corners.

## Mechanical checks
- ON RRP day-over-day change: (552m - 278m) / 278m = **+98.56%**.
- ON RRP latest versus prior-10-operation average (excluding latest): 552m vs 2.8895bn = **-80.90%**.
- TGA close change: 862,841m - 858,548m = **+4,293m**.

## Contradiction pass
Potential disconfirming thesis: a near-doubling in ON RRP could signal emerging funding stress.

Counter-evidence found: latest SOFR eased by 1 bp (3.65 to 3.64) while TGA rise was modest (+$4.293bn), which is inconsistent with an immediate broad funding squeeze.

## Could this be wrong because...
- Quarter-end positioning can abruptly change ON RRP demand, making this low-level regime unstable.
- Two-week operation window underweights longer seasonal patterns.
- Stress could appear first in market segments not captured by SOFR.

## Duplicate/novelty check (last 72h)
- 2026-03-11 ON RRP story concluded usage near zero.  
- Material delta now: ON RRP nearly doubled day-over-day but remained below $1bn; interpretation updated to “bounce without regime break,” with explicit cross-check against fresh SOFR and DTS prints.
