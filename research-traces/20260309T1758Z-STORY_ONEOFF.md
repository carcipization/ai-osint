# Private research trace — STORY (one-off)

## Testable question
Has the U.S. 10-year minus 3-month Treasury spread stayed sustainably positive in early 2026, and does that change how decision-makers should use recession-risk signals?

## Evidence ledger

1. URL: https://fred.stlouisfed.org/graph/fredgraph.csv?id=T10Y3M  
   Publisher: Federal Reserve Bank of St. Louis (FRED)  
   Retrieved: 2026-03-09 17:55 UTC  
   Classification: Observation  
   What it proves: Daily 10Y-3M spread values; latest shown 0.46 on 2026-03-06; last negative print 2025-10-16; 95 consecutive positive trading days through latest point.  
   Limitation: Market series can revise; spread is a signal, not a standalone recession clock.

2. URL: https://fred.stlouisfed.org/graph/fredgraph.csv?id=FEDFUNDS  
   Publisher: Federal Reserve Bank of St. Louis (FRED)  
   Retrieved: 2026-03-09 17:56 UTC  
   Classification: Observation  
   What it proves: Effective federal funds rate down to 3.64 (2026-02) from 4.33 (2025-02), consistent with lower short-end rates helping re-steepen the curve.  
   Limitation: Monthly series; does not isolate all drivers of curve shape.

3. URL: https://fred.stlouisfed.org/graph/fredgraph.csv?id=RECPROUSM156N  
   Publisher: Federal Reserve Bank of St. Louis (FRED, New York Fed recession-probability model series)  
   Retrieved: 2026-03-09 17:56 UTC  
   Classification: Observation  
   What it proves: Latest published monthly recession probability in series remains nonzero (0.80 for 2025-12), indicating model-based risk gauges can lag market regime shifts.  
   Limitation: Monthly lagged model output; not a real-time forecast feed.

## Mechanical checks
- Recomputed positive streak from latest date backward: 95 trading days.
- Recomputed matched-window average T10Y3M:
  - 2026-01-01 to 2026-03-06 average: 0.4825 (44 observations)
  - 2025-01-01 to 2025-03-06 average: 0.1782 (44 observations)

## Could this be wrong because...
- Disconfirming hypothesis: The positive spread is temporary noise and does not reflect sustained regime change.
- What would invalidate current conclusion: Multiple new negative T10Y3M prints over coming weeks or a sharp short-end repricing that re-inverts the curve.
- Found/missing: No new negative prints in available series through 2026-03-06; future data could still reverse the signal quickly.
