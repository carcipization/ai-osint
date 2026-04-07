# DATASETS_B trace — 2026-04-07

- Slot: DATASETS_B
- UTC window: 2026-04-07 09:39–10:00
- Discovery method: `scripts/bulk_dataset_intake.py --pages 2 --rows 200 --top 80`
- Discovery outputs:
  - `research-traces/20260407T093946Z-bulk-dataset-intake.json`
  - `research-traces/20260407T093946Z-bulk-dataset-intake.csv`
  - `research-traces/20260407T093946Z-bulk-dataset-intake-summary.md`

## Overlap pass against `docs/datasets-catalog.md`

Selected (net-new):
1. FOIA Logs — **net-new**
2. Skilled Nursing Facility All Owners — **net-new**
3. Provisional COVID-19 Death Counts by Week Ending Date and State — **net-new**
4. Monthly Rates of Laboratory-Confirmed COVID-19 Hospitalizations from COVID-NET — **net-new**
5. Current Employment Statistics (CES) — **net-new**

Examples intentionally skipped:
- Recalls Data — duplicate (already cataloged under Domestic public safety)
- Border Crossing Entry Data — duplicate (already cataloged under Economy/governance)
- Quarterly Census of Employment and Wages (QCEW) — duplicate (already cataloged)
- MTA Subway Hourly Ridership — duplicate (already cataloged)

## Consequence screen (non-specialist)

- FOIA Logs: accountability/transparency delays affect public oversight decisions.
- SNF All Owners: ownership concentration has direct patient/family care-access and risk implications.
- COVID provisional deaths + COVID-NET hospitalizations: severe-burden tracking for household and hospital decisions.
- CES: employment/income shock detection for household planning and policy response.

## Publication action

- Added 5 datasets to `docs/datasets-catalog.md` across Humanitarian/hazard, Economy/governance, and Ownership/sanctions sections.
- Published dataset brief:
  - `docs/2026-04-07-dataset-intel-governance-health-and-labor-risk-signals-watchlist-86.md`
