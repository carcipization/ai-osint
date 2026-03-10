# Research Trace — 2026-03-10 Early-March US airport screenings baseline shift

## Testable question
Did U.S. checkpoint traffic in early March 2026 rise meaningfully above the immediately preceding late-February baseline, in a way that could matter for near-term operational planning?

## Evidence ledger

1) https://www.tsa.gov/travel/passenger-volumes  
- Publisher: Transportation Security Administration (TSA)  
- Retrieved: 2026-03-10 01:00 UTC  
- Classification: **Observation**  
- What it shows: Daily U.S. checkpoint traveler totals.  
- Mechanical recomputations used in story:  
  - 2026-03-01 to 2026-03-08 average = 2,449,583/day  
  - 2026-02-21 to 2026-02-28 average = 2,304,562/day  
  - Adjacent-window change = +6.29%  
  - Trailing 7-day average ending 2026-03-08 = 2,415,608  
  - Prior 7-day average = 2,337,661  
  - 7-day change = +3.33%  
  - 2026-03-08 (2,781,523) is second-highest posted day in 2026 series (behind 2026-01-04: 2,817,509).  
- Limitation: TSA table is rolling and subject to late revisions; no full in-table multi-year model in this pass.

2) https://www.airlines.org/news-update/u-s-airlines-prepare-for-record-number-of-passengers-this-spring-amid-government-shutdown/  
- Publisher: Airlines for America (A4A)  
- Timestamp: 2026-02-24 (from page)  
- Classification: **Observation** for stated projection; **Inference** for demand framing  
- What it shows: Projection of ~2.8 million passengers/day during Mar-Apr period.  
- Limitation: Trade-group source, not neutral administrative reporting.

## Contradiction pass
- Disconfirming hypothesis: apparent pickup is mostly calendar noise (weekend/holiday mix), not a baseline shift.
- Falsification checks run:
  - Compared two adjacent equal-length windows (8 days vs 8 days), not just a single-day peak.
  - Compared trailing 7-day average to prior 7-day average.
- Result: Both windowed measures rose (+6.29%, +3.33%), which weakens the pure-noise explanation, though it does not eliminate seasonality effects.

## Could this be wrong because...
- TSA updates could revise one or more daily counts.
- School-break timing could temporarily inflate early-March volumes without durable continuation.
- A4A projection may overstate realized demand.

Evidence that would invalidate or weaken current conclusion:
- Next several daily prints pull the trailing 7-day average back to or below late-February levels.
- Additional administrative sources show March throughput flattening despite TSA peak days.

Status: No direct invalidating evidence found in this pass; confidence held at medium.
