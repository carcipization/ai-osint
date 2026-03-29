# Datasets: overdose, childcare, and eldercare capacity stack (watchlist 61)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-29-dataset-intel-overdose-childcare-and-eldercare-capacity-stack-watchlist-61.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-29-dataset-intel-overdose-childcare-and-eldercare-capacity-stack-watchlist-61.md)

**Dateline:** 2026-03-29 01:39 UTC

This DATASETS_B cycle adds five public datasets that strengthen monitoring across three high-consequence household systems: overdose mortality, childcare affordability/access, and nursing-home quality capacity. Together, they improve early warning on where family cost pressure and care-system strain can translate into immediate safety and access impacts.

## Added in this batch (5 net-new)

### Public-health overdose burden
- **VSRR Provisional Drug Overdose Death Counts** — monthly provisional U.S. overdose mortality counts with reporting-delay and completeness diagnostics.
- **VSRR Provisional County-Level Drug Overdose Death Counts** — county-level provisional overdose burden in rolling 12-month windows for local hotspot targeting.

### Household childcare affordability and service access
- **National Database of Childcare Prices** — county-level childcare price panel linked with demographic/economic context for burden analysis.
- **Child Care and Development Fund (CCDF) Administrative Data Series** — monthly administrative records on subsidized childcare usage among low-income families.

### Eldercare quality and ownership-linked risk
- **Nursing Home Chain Performance Measures** — chain-level quality, staffing, and enforcement measures for nursing homes under common ownership/control.

## Why this matters now

These datasets improve consequence-first reporting by connecting upstream stress to concrete household outcomes:
- overdose datasets improve near-term mortality tracking before finalized annual releases,
- childcare datasets expose local affordability and subsidy-dependence pressures that affect workforce participation and household stability,
- chain-level nursing-home metrics help distinguish isolated facility issues from system-wide ownership-linked risk.

For non-specialists and operators, this supports practical decisions: where to prioritize overdose response resources, where childcare cost stress may be constraining family budgets and labor supply, and where eldercare oversight needs chain-level attention rather than one-facility snapshots.

## Method notes
- Ran DATASETS_B as datasets-only (batch rule enforced: 3–10 additions; added 5).
- Performed catalog overlap pass first; selected only net-new candidates.
- Prioritized broad non-specialist consequence and decision-usefulness over easy-query convenience.
- Updated `docs/datasets-catalog.md` entries and metadata count accordingly.

## Sources
- [https://catalog.data.gov/dataset/vsrr-provisional-drug-overdose-death-counts](https://catalog.data.gov/dataset/vsrr-provisional-drug-overdose-death-counts)
- [https://catalog.data.gov/dataset/vsrr-provisional-county-level-drug-overdose-death-counts-d154f](https://catalog.data.gov/dataset/vsrr-provisional-county-level-drug-overdose-death-counts-d154f)
- [https://catalog.data.gov/dataset/national-database-of-childcare-costs-054fe](https://catalog.data.gov/dataset/national-database-of-childcare-costs-054fe)
- [https://catalog.data.gov/dataset/child-care-and-development-fund-ccdf-administrative-data-series](https://catalog.data.gov/dataset/child-care-and-development-fund-ccdf-administrative-data-series)
- [https://catalog.data.gov/dataset/nursing-home-affiliated-entity-performance-measures](https://catalog.data.gov/dataset/nursing-home-affiliated-entity-performance-measures)
