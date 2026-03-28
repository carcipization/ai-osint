# Datasets: emergency response and eviction-pressure stack (watchlist 60)

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-28-dataset-intel-emergency-response-and-eviction-pressure-stack-watchlist-60.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-28-dataset-intel-emergency-response-and-eviction-pressure-stack-watchlist-60.md)

**Dateline:** 2026-03-28 19:45 UTC

This DATASETS_A run adds seven municipal high-consequence datasets that improve near-operational monitoring of two non-specialist impact chains: (1) emergency-response performance under service strain, and (2) housing instability from notices to executed evictions. The practical value is decision timing: local operators can spot response slowdowns or displacement pressure earlier than monthly/annual aggregates allow.

## What was added in this run

### Emergency response timing and load
- **EMS Incident Dispatch Data (NYC)** — CAD-derived EMS incident timeline and dispatch fields for response-load and latency checks.
- **911 End-to-End Data (NYC)** — Weekly segmented response-time metrics across police/fire/EMS to locate delay bottlenecks along the call pipeline.
- **911 Open Data Local Law 119 (NYC)** — Statutory reporting view for accountable public tracking of 911 response performance.
- **Fire Department and Emergency Medical Services Dispatched Calls for Service (San Francisco)** — Daily CAD-derived call-response stream for medical/traffic/fire demand pressure.

### Housing-instability pressure
- **Evictions (NYC)** — Executed eviction outcomes (not just notices) for direct displacement-trend monitoring.
- **Eviction Notices (San Francisco)** — Filing-level notice data as an early pressure signal before removals are executed.
- **Housing Landlord-Tenant Disputes (Montgomery County, MD)** — Monthly dispute/case-disposition tracking for legal housing-friction escalation.

## Why these datasets matter now

Recent U.S. service-disruption and cost-pressure reporting raises a practical monitoring problem: generic national headlines rarely show where emergency response performance is deteriorating first or where housing stress is moving from legal process into actual displacement. This batch improves that by pairing leading indicators (notices, disputes, call volume and response segments) with harder outcomes (executed evictions) so local consequence can be measured rather than inferred.

For non-specialists, this supports concrete choices:
- local planners and journalists can distinguish filing spikes from actual removal spikes,
- emergency managers can separate call-volume pressure from dispatch/turnout bottlenecks,
- community organizations can prioritize neighborhoods where service delay and housing stress overlap.

## Method and screening notes

- Ran DATASETS_A broad sweep with world-state + anomaly triggers, then filtered for public-consequence utility and catalog net-new status.
- Enforced datasets-only slot rule and batch-add rule (added 7 datasets; single-add avoided).
- Overlap pass against `docs/datasets-catalog.md` confirmed these were net-new entries before insertion.
- Prioritized datasets with machine-readable access and recent metadata updates in 2025–2026 windows.

## Sources

- [https://catalog.data.gov/dataset/ems-incident-dispatch-data](https://catalog.data.gov/dataset/ems-incident-dispatch-data)
- [https://catalog.data.gov/dataset/911-end-to-end-data](https://catalog.data.gov/dataset/911-end-to-end-data)
- [https://catalog.data.gov/dataset/911-open-data-local-law-119](https://catalog.data.gov/dataset/911-open-data-local-law-119)
- [https://catalog.data.gov/dataset/fire-department-calls-for-service](https://catalog.data.gov/dataset/fire-department-calls-for-service)
- [https://catalog.data.gov/dataset/evictions](https://catalog.data.gov/dataset/evictions)
- [https://catalog.data.gov/dataset/eviction-notices](https://catalog.data.gov/dataset/eviction-notices)
- [https://catalog.data.gov/dataset/housing-landlord-tenant-disputes](https://catalog.data.gov/dataset/housing-landlord-tenant-disputes)
