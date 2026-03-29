# Datasets: coverage friction and benefit-access signals (watchlist 63)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-29-dataset-intel-coverage-friction-and-benefit-access-signals-watchlist-63.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-29-dataset-intel-coverage-friction-and-benefit-access-signals-watchlist-63.md)

**Dateline:** 2026-03-29 21:41 UTC

This DATASETS_B cycle adds five public datasets focused on household service continuity under stress: children’s health coverage retention, unemployment-benefit access friction, and chronic school absenteeism as a downstream social strain signal.

## Added in this batch (5 net-new)

1. **Program Information for Medicaid and CHIP Beneficiaries by Month**  
   Monthly Medicaid/CHIP beneficiary counts by program type for tracking care-coverage continuity.

2. **Separate CHIP Enrollment by Month and State – Historic CAA/Unwinding Period**  
   State-month CHIP enrollment series for children’s coverage shifts during post-pandemic redetermination windows.

3. **Unemployment Insurance Nonmonetary Determination Activity Data (ETA-207)**  
   UI adjudication and denial activity data for detecting administrative bottlenecks affecting income support.

4. **Unemployment Insurance Benefit Rights and Experience Data (ETA-218)**  
   State-level claimant eligibility and benefit-rights outcomes for policy strictness and access comparisons.

5. **Student Absenteeism**  
   State chronic-absenteeism counts (15+ days absent) as a high-salience signal of family stress and service disruption.

## Why this matters now

These additions improve consequence-first monitoring of whether shocks are translating into lived access problems:
- **health coverage continuity risk** (Medicaid/CHIP churn),
- **income-protection access risk** (UI adjudication and eligibility frictions),
- **household strain manifestation** in schools (chronic absenteeism).

Together they strengthen cross-domain chains from macro/labor disruption to immediate household outcomes that non-specialists and local operators can act on.

## Method notes
- DATASETS_B run executed as datasets-only batch (5 additions, within required 3–10 range).
- Conducted overlap pass against current catalog and selected **net-new** entries while skipping already-listed adjacent CMS/nursing-home and weekly UI claims datasets.
- Prioritized broad public consequence and decision usefulness over easy endpoint availability.
- Updated `docs/datasets-catalog.md` count and descriptors.

## Sources
- [https://catalog.data.gov/dataset/program-information-for-medicaid-and-chip-beneficiaries-by-month-72256](https://catalog.data.gov/dataset/program-information-for-medicaid-and-chip-beneficiaries-by-month-72256)
- [https://catalog.data.gov/dataset/separate-chip-enrollment-by-month-and-state](https://catalog.data.gov/dataset/separate-chip-enrollment-by-month-and-state)
- [https://catalog.data.gov/dataset/unemployment-insurance-nonmonetary-determination-activity-data-eta-207](https://catalog.data.gov/dataset/unemployment-insurance-nonmonetary-determination-activity-data-eta-207)
- [https://catalog.data.gov/dataset/unemployment-insurance-benefit-rights-and-experience-data-eta-218](https://catalog.data.gov/dataset/unemployment-insurance-benefit-rights-and-experience-data-eta-218)
- [https://catalog.data.gov/dataset/student-absenteeism-b0fcc](https://catalog.data.gov/dataset/student-absenteeism-b0fcc)
