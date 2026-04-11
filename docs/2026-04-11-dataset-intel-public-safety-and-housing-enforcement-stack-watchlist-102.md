# Datasets: public safety and housing-enforcement stack (watchlist 102)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-04-11-dataset-intel-public-safety-and-housing-enforcement-stack-watchlist-102.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-04-11-dataset-intel-public-safety-and-housing-enforcement-stack-watchlist-102.md)

**Dateline:** 2026-04-11 17:41 UTC

This DATASETS_B cycle adds four machine-readable datasets that strengthen consequence-first monitoring across emergency demand, traffic safety risk, and housing condition/compliance pressure.

## Added in this run

- **[Police Dispatched Incidents](https://catalog.data.gov/dataset/police-dispatched-incidents)** — Montgomery County incident-level police dispatch stream updated up to four times daily.
- **[Automated Red Light Violations](https://catalog.data.gov/dataset/automated-red-light-violations)** — camera-captured red-light violations for intersection-level traffic-safety hotspot checks.
- **[Housing Code Violations](https://catalog.data.gov/dataset/housing-code-violations)** — housing code-enforcement records (2013–present) with weekly updates.
- **[Housing Licensing and Registration](https://catalog.data.gov/dataset/housing-licensing-and-registration)** — rental license/registration inventory for condominiums, single-family, multifamily, and accessory units.

## Why this stack matters

- **Immediate local decision utility:** dispatch and red-light violation streams provide fast operational signals for safety pressure and enforcement load.
- **Household safety linkage:** housing code violations surface potential habitability and health-risk conditions affecting residents directly.
- **Denominator context for housing stress:** licensing/registration records improve interpretation of complaint and dispute datasets by adding stock/compliance baseline.

## Practical use pattern

1. Track 7/30-day shifts in dispatched incidents by type and geography.
2. Compare red-light violation concentration with crash and complaint data before causal claims.
3. Monitor weekly housing-code violation trends for persistent hotspot clusters.
4. Use licensing inventory to normalize violation/dispute rates and avoid raw-count bias.

## Caveats

- These are subnational datasets and should not be generalized to national conditions.
- Dispatch and enforcement records reflect administrative workflows and coding policies.
- Camera-placement, reporting behavior, and inspection intensity can influence observed counts.

## Appendix: Sources

- Data.gov catalog (all datasets linked above)
