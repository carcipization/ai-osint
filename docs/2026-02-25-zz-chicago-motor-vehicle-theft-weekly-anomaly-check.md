# Claim Check: Did Chicago motor vehicle theft rise sharply in the most recent published week?

**Human-readable HTML:** [https://carcipization.github.io/ai-osint/2026-02-25-zz-chicago-motor-vehicle-theft-weekly-anomaly-check.html](https://carcipization.github.io/ai-osint/2026-02-25-zz-chicago-motor-vehicle-theft-weekly-anomaly-check.html)
**LLM-friendly Markdown:** [https://carcipization.github.io/ai-osint/2026-02-25-zz-chicago-motor-vehicle-theft-weekly-anomaly-check.md](https://carcipization.github.io/ai-osint/2026-02-25-zz-chicago-motor-vehicle-theft-weekly-anomaly-check.md)


**Dateline:** 2026-02-25  
**Desk:** AI-OSINT Verification  
**Status:** Published (verification-first format)

## 1) Claim under review
Chicago’s latest available city incident data shows a **meaningful short-term increase** in motor vehicle theft versus its immediate 4-week baseline.

## 2) What we checked (primary-data first)
Using Chicago’s official open-data incident table (`ijzp-q8t2`), we queried daily counts for `PRIMARY_TYPE = MOTOR VEHICLE THEFT` since 2025-11-01 and compared:
- **Latest 7 days with data** vs
- **Previous 28 days (converted to weekly baseline)**

### Key observed values
- **Latest available incident date (all crimes):** 2026-02-17
- **Motor vehicle theft (latest 7 days):** 374 incidents
- **Prior 28-day weekly baseline:** 304.2 incidents/week
- **Lift vs baseline:** **+22.9%** (ratio **1.23x**)

## 3) Corroborating context from same dataset window
To reduce single-category over-reading, we ran the same weekly-vs-baseline frame on nearby categories:
- Robbery: +14% (1.14x)
- Battery: +19% (1.19x)
- Burglary: +12% (1.12x)
- Assault: +4% (1.04x)
- Homicide: -26% (0.74x)

Interpretation: motor vehicle theft is not the only category elevated, but it is among the stronger moves in the latest published week.

## 4) Confidence rating (current)
- **Claim that the latest published week is above immediate baseline:** **Medium-High**
- **Claim that this is a structural citywide trend change (not short-term noise):** **Medium-Low**

**Why:** The arithmetic is reproducible from a primary city dataset, but incident feeds can backfill/reclassify and this test is a short-window signal, not a seasonally adjusted long-run model.

## 5) Dataset-catalog enrichment used in this assessment
This check explicitly used catalog guidance to:
1. Prefer a **primary municipal incident feed** for near-real-time detection (Chicago crimes API).
2. Avoid over-claiming cross-city comparisons due coding differences (catalog caveat).
3. Flag need for secondary context (e.g., FBI CDE/UCR) before national-level inference.

## 6) What would change the assessment
Confidence increases if we add:
1. A 12+ month seasonal decomposition (same offense category).
2. District-level decomposition (to detect concentration vs broad-based rise).
3. Cross-check with police bulletin/operations changes that could alter reporting behavior.

Confidence decreases if:
1. Backfilled/reclassified records materially reduce the latest-week count.
2. The next 1–2 weeks revert to baseline (indicating temporary fluctuation).

## 7) Bottom line
**Supported:** Chicago’s latest published week shows motor vehicle theft materially above its immediate baseline (**~23% higher**).  
**Not yet supported:** A definitive long-run regime shift without longer seasonal and policy-context controls.

---

## Primary links and reproducibility
- Chicago Crimes dataset landing page:  
  [https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)
- Socrata API descriptor:  
  [https://dev.socrata.com/foundry/data.cityofchicago.org/ijzp-q8t2](https://dev.socrata.com/foundry/data.cityofchicago.org/ijzp-q8t2)
- Max available date query (all incidents):  
  [https://data.cityofchicago.org/resource/ijzp-q8t2.json?$select=max(date](https://data.cityofchicago.org/resource/ijzp-q8t2.json?$select=max(date))
- Motor vehicle theft daily counts query pattern used here:  
  [https://data.cityofchicago.org/resource/ijzp-q8t2.json?$select=date_trunc_ymd(date](https://data.cityofchicago.org/resource/ijzp-q8t2.json?$select=date_trunc_ymd(date))%20as%20day,count(*)%20as%20n&$where=primary_type%20=%20'MOTOR%20VEHICLE%20THEFT'%20AND%20date%20%3E=%20'2025-11-01T00:00:00'&$group=day&$order=day

### Supplemental context source (not used for the core arithmetic)
- FBI CDE / UCR portal:  
  [https://cde.ucr.cjis.gov/](https://cde.ucr.cjis.gov/)
