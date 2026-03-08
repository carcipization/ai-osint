# Research trace — KEV ransomware tag share

Date: 2026-03-08 UTC

## Testable question
Has the KEV catalog’s ransomware-tagged share in 2026 remained below prior years even as total KEV entries increased?

## Evidence ledger
1. https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
   - Type: Tier 1 (primary machine-readable source)
   - Observation: total entries=1536; 2026-added=52; 2026 ransomware Known=3
   - Limitation: attribute revisions can occur after initial add
2. https://www.cisa.gov/binding-operational-directive-22-01
   - Type: Tier 1 policy source
   - Observation: BOD remediation framework applies to KEVs regardless of ransomware label

## Mechanical checks
- 3 / 52 = 0.05769 => 5.8%
- Prior years from feed: 2021=76/311 (24.4%), 2022=123/555 (22.2%), 2023=43/187 (23.0%), 2024=42/186 (22.6%), 2025=25/245 (10.2%)

## Could this be wrong because...
- Disconfirming hypothesis: 2026 ransomware-tag values are lagged and later backfilled, making current share artificially low.
- Invalidating evidence needed: a subsequent KEV feed revision with substantial 2026 `Known` backfills.
- Status: not found at time of pull; treated as explicit limitation.
