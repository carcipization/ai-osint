# Research Trace — 2026-03-10 US airport screenings spring ramp

## Testable question
Did U.S. checkpoint volume move meaningfully above its recent baseline at the start of March 2026, and is that consistent with a broader spring-travel ramp rather than routine noise?

## Evidence ledger

1) https://www.tsa.gov/travel/passenger-volumes  
- Publisher: Transportation Security Administration (TSA)  
- Retrieved: 2026-03-10 00:52 UTC  
- Classification: **Observation**  
- What it shows: Daily checkpoint traveler counts; latest posted day is 2026-03-08 at 2,781,523.  
- Derived checks (mechanical recompute):
  - Trailing 7-day average ending 2026-03-08 = 2,415,608
  - Prior 7-day average = 2,337,661
  - Week-over-week change = +3.33%
  - Latest day vs prior four Sundays (2026-02-08/15/22 and 2026-03-01 average 2,493,449) = +11.55%
  - 2026-03-08 is second-highest day in posted 2026 series; only 2026-01-04 (2,817,509) is higher.
- Limitation: Public page currently displays a short rolling window (no full-year historical panel in same table), so long-horizon seasonality checks are limited.

2) https://www.airlines.org/news-update/u-s-airlines-prepare-for-record-number-of-passengers-this-spring-amid-government-shutdown/  
- Publisher: Airlines for America (A4A)  
- Timestamp: 2026-02-24 (from page)  
- Classification: **Observation** for quoted forecast, **Inference** for demand narrative  
- What it shows: U.S. airlines forecast 171 million passengers for Mar-Apr (about 2.8 million/day), up 4% y/y.  
- Limitation: Trade-group forecast with advocacy incentives; not a neutral administrative count.

## Contradiction pass
- Disconfirming hypothesis: The March 8 jump is only weekend noise and does not indicate broader spring ramp.
- Check run: Compared latest day to prior same-weekday baseline (last four Sundays) and compared trailing 7-day window to previous 7-day window.
- Result: Latest Sunday was +11.55% above prior four-Sunday average, and 7-day average rose +3.33% week-over-week; this weakens (but does not eliminate) the pure-noise explanation.

## Could this be wrong because...
- The TSA page is revised later, changing one or more daily values.
- A holiday/calendar mix effect (school-break timing) could explain most of the increase without implying a sustained trend.
- A4A projection may overstate realized demand.

Evidence that would invalidate or weaken current conclusion:
- A multi-day drop that pulls the next trailing 7-day average back to or below the prior week.
- Official carrier or DOT data showing March capacity reductions inconsistent with a ramp.

Status: Invalidating evidence not found in this pass; medium confidence retained with explicit caveats.
