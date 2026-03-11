# Research trace — TGA rebuilt after four-session drawdown

## Testable question
Did the U.S. Treasury General Account (TGA) show a meaningful short-term regime shift on the latest Daily Treasury Statement print, and does cross-market pricing indicate immediate funding stress?

## Last-72h overlap check
- Recent STORY posts reviewed in docs/: ON RRP near-zero story (2026-03-11), TSA throughput stories (2026-03-10), yield-curve story (2026-03-09).
- Duplicate decision: **not duplicate** (different source lane: Treasury cash-balance flow vs ON RRP level).

## Evidence ledger
1) URL: https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/dts/operating_cash_balance?sort=-record_date&page%5Bsize%5D=500  
   Publisher: U.S. Treasury FiscalData (Daily Treasury Statement)  
   Timestamp used: latest available record date 2026-03-09  
   What it proves: TGA closing balance moved from 833,086 to 858,548 (USD millions) between 2026-03-06 and 2026-03-09; deposits 44,750 vs withdrawals 19,289 (net +25,461).  
   Class: Observation  
   Limitation: one-day move; DTS can be revised.

2) URL: https://fred.stlouisfed.org/graph/fredgraph.csv?id=SOFR  
   Publisher: Federal Reserve Bank of New York series distributed by FRED  
   Timestamp used: latest print 2026-03-10  
   What it proves: SOFR eased slightly from 4.34 to 4.33 despite TGA rebuild.  
   Class: Observation  
   Limitation: SOFR is one funding benchmark and may miss localized balance-sheet strain.

3) URL: https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/operating-cash-balance  
   Publisher: U.S. Treasury (dataset documentation)  
   Timestamp used: accessed 2026-03-11 UTC  
   What it proves: unit/field interpretation for operating cash balance table entries.  
   Class: Observation  
   Limitation: metadata page, not the transaction series itself.

## Mechanical checks
- Net flow recomputation: 44,750 - 19,289 = 25,461 (USD millions).
- Closing balance recomputation: 833,086 + 25,461 ~= 858,547 (reported 858,548; 1 million rounding difference at table granularity).
- Previous 20-session mean net flow: -4,073.8 (USD millions); latest session is a positive swing versus that recent average.

## Contradiction pass
- Potential contradiction: If the cash rebuild were already tightening front-end funding, SOFR should jump materially.
- Observed: SOFR was flat-to-lower (4.34 to 4.33), weakening a near-term stress interpretation.

## Could this be wrong because...
- Top disconfirming hypothesis: The move is routine timing noise (coupon/tax timing) with no persistent liquidity effect.
- What would invalidate current conclusion: next 2-3 DTS sessions reverse most of the rebuild while funding benchmarks remain unchanged.
- Found vs missing: partial evidence found (SOFR stability supports “no immediate stress”); missing multi-day persistence confirmation.
