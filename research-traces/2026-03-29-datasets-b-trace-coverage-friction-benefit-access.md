# DATASETS_B trace — 2026-03-29 — coverage friction and benefit-access stack

**Run window (UTC):** 2026-03-29 21:39–21:42  
**Slot:** DATASETS_B

## Situational-awareness + anomaly sweep (datasets mode)

Discovery queries run:
- `site:catalog.data.gov utility shutoff data water arrears households`
- `site:catalog.data.gov school absenteeism chronic absenteeism dataset`
- `site:catalog.data.gov emergency rental assistance program data`
- `site:catalog.data.gov food pantry usage dataset`
- `site:catalog.data.gov medicaid enrollment monthly by state dataset`
- `site:catalog.data.gov unemployment insurance appeals processing time dataset`
- `site:catalog.data.gov nursing home staffing data payroll based journal`
- `site:catalog.data.gov hospital price transparency machine readable dataset national`

## Overlap pass against catalog

Already present/adjacent examples found and excluded from net-new adds:
- State Medicaid and CHIP Applications, Eligibility Determinations, and Enrollment Data
- Payroll Based Journal Daily Nurse Staffing
- Medicare Monthly Enrollment
- Nursing Home Compare
- Unemployment Insurance Weekly Claims & Extended Benefits Trigger Data (ETA-539)

## Selected net-new datasets (5)
1. Program Information for Medicaid and CHIP Beneficiaries by Month
2. Separate CHIP Enrollment by Month and State – Historic CAA/Unwinding Period
3. Unemployment Insurance Nonmonetary Determination Activity Data (ETA-207)
4. Unemployment Insurance Benefit Rights and Experience Data (ETA-218)
5. Student Absenteeism

## Selection rationale
- Maintains breadth-first objective while building a coherent household-consequence chain:
  - health coverage continuity,
  - unemployment-support access friction,
  - education attendance stress.
- Improves decision usefulness for non-specialists and local operators monitoring whether macro stress is becoming service-access loss.

## Rejected/held candidates
- Hospital Price Transparency Enforcement Activities and Outcomes: useful but narrower enforcement lens vs broader household-consequence chain selected this run.
- FEMA/HUD rental-assistance related candidates surfaced in query results were either already represented by adjacent disaster housing-support entries or lower fit for this batch’s coverage-friction theme.
- Water-related candidates found in this pass were either non-public, highly local, or weaker direct consequence fit for this cycle’s selected stack.

## Sources used
- https://catalog.data.gov/dataset/program-information-for-medicaid-and-chip-beneficiaries-by-month-72256
- https://catalog.data.gov/dataset/separate-chip-enrollment-by-month-and-state
- https://catalog.data.gov/dataset/unemployment-insurance-nonmonetary-determination-activity-data-eta-207
- https://catalog.data.gov/dataset/unemployment-insurance-benefit-rights-and-experience-data-eta-218
- https://catalog.data.gov/dataset/student-absenteeism-b0fcc
