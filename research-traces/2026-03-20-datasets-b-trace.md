# DATASETS_B trace — 2026-03-20 01:39 UTC

## Situational-awareness and anomaly sweep

Initial candidate queries emphasized high-consequence disaster, housing, and social-service pressure pathways:
- `site:catalog.data.gov openfema housing assistance owners renters`
- `site:catalog.data.gov openfema individuals and households program valid registrations`
- `site:catalog.data.gov emergency rental assistance program data`

Selection rationale:
- Prior DATASETS_A run established disaster declaration/recovery-finance stack.
- This DATASETS_B run extends the same consequence chain with missing **household demand and intake** layers.
- Domain repetition accepted with explicit reason: chain completion for broad non-specialist decision use.

## Selected additions (4)

1. Housing Assistance Program Data – Renters
2. Registration Intake and Individuals Household Program (RI-IHP)
3. Individual Assistance Housing Registrants – Large Disasters
4. FEMA Individual Assistance Open Disaster Statistics

## Endpoint verification snapshots

- Housing Assistance Program Data – Renters: HTTP 200; metadata updated Jun 7, 2025.
- RI-IHP: HTTP 200; metadata updated Jun 7, 2025.
- Individual Assistance Housing Registrants – Large Disasters: HTTP 200; metadata updated Jun 7, 2025.
- FEMA Individual Assistance Open Disaster Statistics: HTTP 200; metadata updated Oct 19, 2022 (older metadata; retained due strong consequence relevance and open-disaster operational value).

## Rejections/misses

- Additional housing/eviction city-only feeds were deprioritized for this slot due weaker national comparability.
- Kept batch size at 4 to maintain quality and avoid low-value padding.

## Output actions

- Added 4 datasets to `docs/datasets-catalog.md`.
- Published watchlist explainer: `2026-03-20-dataset-intel-household-disaster-assistance-demand-stack-watchlist-43.md`.
