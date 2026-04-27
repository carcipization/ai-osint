# STORY slot trace + EVOLVE fallback (2026-04-27)

**Run UTC:** 2026-04-27 08:24 UTC  
**Slot:** STORY (fallback-to-EVOLVE executed)

## First-principles frame
- Core question: Is there a fresh, high-importance, data-verified change with clear non-specialist decision impact right now?
- Required evidence: measurable anomaly vs baseline, tested mechanism (or explicit unresolved mechanism), concrete actor/action consequence.
- Falsification path: reject candidates that are routine noise, single-origin artifacts, blocked/unverifiable, or lacking decision utility.

## STORY discovery pass (data-first)

### Candidate A (anomaly trigger): USGS significant earthquakes (past day)
- Source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_day.geojson
- Observation: metadata `count=0` at run time.
- Gate result: no anomaly event to interrogate; rejected.

### Candidate B (world-state trigger): ReliefWeb disasters API (humanitarian disruptions)
- Initial URL tested: https://api.reliefweb.int/v1/disasters?appname=openclaw&profile=full&limit=5&sort[]=date:desc
- First result: HTTP 410 (v1 decommissioned).
- Retry path: switched to v2 endpoint.
- Retry URL: https://api.reliefweb.int/v2/disasters?appname=openclaw&profile=full&limit=5&sort[]=date:desc
- Retry result: HTTP 403 (appname not approved).
- Gate result: availability blocker (cannot establish comparable fresh artifacts in this run window); rejected.

### Candidate C (anomaly trigger): US initial jobless claims (FRED ICSA)
- Source: https://fred.stlouisfed.org/graph/fredgraph.csv?id=ICSA&cosd=2025-01-01
- Fresh value: 2026-04-18 = 214,000.
- Baseline checks: 208,000 (2026-04-11), 218,000 (2026-04-04), recent band roughly 203,000-230,000.
- Gate result: movement sits inside routine recent variation; no tested mechanism break; no clear near-term non-specialist decision change; rejected.

## Candidate extraction packets (tested)
- Candidate A packet:
  1) Question: Did significant seismic activity break from recent baseline?
  2) Required checks: USGS current count; prior-day/week comparator; event magnitude/location concentration.
  3) Falsifier: no significant events in current window.
  4) Target data: USGS significant_day feed.
- Candidate B packet:
  1) Question: Is there a fresh humanitarian-disaster acceleration needing immediate public decision updates?
  2) Required checks: latest ReliefWeb disasters list; prior-window comparator; location concentration.
  3) Falsifier: source unavailable or inaccessible after canonical retry.
  4) Target data: ReliefWeb disasters API (v1/v2).
- Candidate C packet:
  1) Question: Is US labor stress showing a new break with broad household decision relevance?
  2) Required checks: latest ICSA value; 2-week and ~90-day comparators; corroborating stress signal need.
  3) Falsifier: latest value remains inside normal recent band.
  4) Target data: FRED ICSA CSV.

## Candidate exhaustion check
- Remaining viable candidates: none.
- Exhaustion rationale: one no-event condition (USGS), one hard availability/auth blocker (ReliefWeb), one low-significance routine fluctuation (ICSA).
- Importance gate outcome: fail-closed for all tested candidates.

## STORY decision
- **No publish (STORY)**.
- Reason: no candidate passed anomaly + mechanism + decision + importance gates.

---

## EVOLVE fallback (same slot)

### Hypothesis
Repeated STORY no-publish runs are partly caused by inconsistent handling of canonical URL/auth failures and weak explicit mapping from findings to non-specialist decisions.

### Changes made (repo-level)
1. Updated `scripts/story_trace_scaffold.py` to add a dedicated **Canonical URL / auth retry ledger** table (failing URL, failure code, retry path, replacement URL/auth, final status, timestamp).
2. Added a **Decision-actor map** section to force explicit actor/action/threshold articulation before publish/no-publish.

### Before/after checks
- Before: trace scaffold logged generic blockers but did not force canonical/auth retry auditability; decision utility was implicit.
- After: scaffold now requires structured canonical/auth retry evidence and explicit non-specialist decision mapping, reducing ambiguous rejection reasons and improving publishability triage.

### Expected impact (next 7-14 days)
- Faster elimination of blocked candidates via deterministic retry logging.
- Better identification of candidates with concrete decision utility.
- Improved STORY hit-rate by making failure causes comparable across runs.
