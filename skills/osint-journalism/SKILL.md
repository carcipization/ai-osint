# OSINT Journalism Skill

Purpose: produce high-quality automated OSINT journalism: fast, clear, evidence-based reporting that reads like publishable wire copy.

## Editorial north star

- Optimize for: **story quality**, **reporting reliability**, **publication speed**.
- Rules are tools, not outcomes.
- If a checklist step does not materially improve journalism, skip or shorten it.

## Quick operating mode

1. **Classify the task first**
   - Claim-check (specific claim + provenance URL)
   - OSINT story (new analysis, not a claim-check)
   - Follow-up (re-check prior posts; publish only material changes)
   - Dataset task (catalog addition/optimization)

2. **Pick evidence tiers**
   - Tier 1: official registry/agency/primary release
   - Tier 2: structured monitoring systems (Cloudflare Radar, IODA, OONI, PortWatch, etc.)
   - Tier 3: media/social/aggregators (lead generation)

3. **Set publication confidence**
   - Supported / Not supported / Partly supported / Inconclusive
   - Add explicit caveats for model-derived metrics and method-sensitive estimates

## STORY broad-sweep selection (data-first, mandatory)

Reverse the old flow. Do not start with a narrative idea.

## Seed-to-dataset interrogation protocol (mandatory for wire-led STORY candidates)

When a lead starts from Reuters/AP/major wire (or any single media seed), do this exact sequence before drafting:

1. **Write seed claim + competing questions (private trace)**
   - One seed claim sentence (what the wire says happened).
   - At least 2 competing questions that do **not** assume the seed framing is correct.

2. **Run targeted catalog retrieval before narrative drafting**
   - Pull candidate datasets from `docs/datasets-catalog.md` by topic keywords tied to the seed domain.
   - Build a short list of relevant datasets (target 5-15) and classify each: `usable now` / `not usable now` with reason.

3. **Interrogate data first, question second**
   - For each `usable now` dataset, extract the freshest available artifact and one baseline comparator (prior period/window).
   - Record only observed changes first (no causal language yet): what moved, where, magnitude, and timeframe.

4. **Build a claim-evidence matrix before prose**
   - For each major claim, log: claim text, evidence family, source URL, timestamp, status (`supported` / `unproven` / `contradicted`).
   - If the lead claim remains single-origin after this pass, keep it explicitly provisional.

5. **Select story question from data findings (not from seed framing)**
   - Choose the final reporting question only after step 3-4 outputs are complete.
   - If data findings point elsewhere, re-angle or demote.

6. **Publication class discipline**
   - If targeted dataset interrogation does not produce meaningful new evidence, do not publish as a full event STORY.
   - Use dataset brief / analysis framing instead of story framing.

Hard failure rule:
- Publishing a wire-led STORY without completing the targeted dataset interrogation + claim-evidence matrix is non-compliant.

**No predefined tracks and no fixed upfront shortlist.** Build candidates continuously from what data is actually updating now.

1. **Freshness + availability scan first (hard first pass)**
   - Discover candidate signals dynamically from currently updating, reachable sources.
   - Use broad discovery inputs: official release calendars, API latest endpoints, wire/headline event surfaces, and high-signal social leads.
   - Define a candidate only after finding a concrete fresh artifact.
   - Score each discovered candidate on:
     - freshness (new/updated artifact in current window),
     - availability (query works now; no blocking errors),
     - baseline comparability (enough history/context to judge anomaly),
     - decision surface (who would act if true).
   - Continue expanding candidate discovery through the scan window; do not freeze the option set early.

2. **Only then generate story concepts**
   - Generate concepts from the strongest observed candidates after the broad scan window, not from an early capped list.
   - Prefer concept framing as: “what changed vs baseline, and what decision could change?”

3. **Timebox for STORY runs**
   - Data freshness/availability scan: 10–15 min
   - Concept + evidence testing: 15–20 min
   - Publish/no-publish decision: 5 min

4. **No-publish guardrail**
   - Do not no-publish before completing the data-first scan unless discovered candidates are unavailable with documented errors.

## Situational awareness + anomaly sweep (mandatory for STORY/FOLLOWUP/DATASETS)

Run a short dual-trigger sweep at the start of each run (timebox: 5–10 minutes).

Required:
- Use web/news search to identify active developments across event classes (not a single headline track).
- **Bluesky check is STORY-only.** Do not run Bluesky sweeps in DATASETS, FOLLOWUP, or DATASETS_OPTIMIZE slots.
- **Bluesky discovery pass minimum:** run at least **5 distinct Bluesky queries** per STORY run.
- **Trending scan required:** include a quick pass over current Bluesky trending/discussion topics and convert the top relevant trends into additional query terms.
- Use Bluesky results to surface candidate datasets/sensors to inspect next (lead generation for dataset targeting), not just headline leads.
- **Polymarket signal pass is STORY-only and mandatory:** run at least **3 distinct Polymarket queries/market scans** per STORY run (for expectation-shift lead generation, not as standalone proof).
- Log any non-result/low-liquidity limitation when Polymarket signal quality is weak.
- Do **not** use convenience/default query shortcuts (e.g., generic TSA/NOAA filler checks) unless directly justified by findings.
- Do not predispose the pass to any predefined track, domain, or dataset family.

Dual-trigger rule (hard):
1. **World-state trigger**: build a neutral brief from what is newly active now, then rank by expected real-world impact.
2. **Anomaly trigger**: run a blind dataset anomaly scan for fresh, non-routine changes even when no matching headline/news story exists.

Selection rule:
- Derive candidate signals from both triggers before deep data pulls.
- Include at least one world-state-derived candidate and one anomaly-derived candidate per run when available.
- If either side yields no qualified candidate, document why in the trace.
- If the top-impact item is not selected first, document explicit blocker(s) in trace.

Trace rule:
- Capture search terms, links, timestamps, anomaly checks attempted, and reasons for candidate acceptance/rejection.
- For STORY runs, explicitly log: (a) all Bluesky queries run (minimum 5), (b) trending topics reviewed, (c) which trend-derived queries were added, (d) dataset leads produced from Bluesky (or explicit none), (e) Polymarket queries/scans run (minimum 3), and (f) any Polymarket limitation notes (e.g., no match/low liquidity/noisy contract framing).
- For every blocked/error fetch, log a structured line with: source name, URL, HTTP/status or error type, UTC timestamp, and one retry outcome (success/fail + status).

## Dataset intake policy (batch-first, consequence-first)

- Default to **bulk discovery** and **multi-add promotion**, not one-by-one additions.
- Discovery pass target: scan at least tens/hundreds of candidates per run when tooling allows.
- Promotion default: add **3–10 qualified datasets per cycle** (unless quality is genuinely thin).
- Adding only one dataset is unacceptable.
- Prioritize coverage breadth across domains before polishing niche depth.
- Before final selection, run a **catalog overlap pass** against `docs/datasets-catalog.md` and classify each candidate as **net-new / adjacent / duplicate**.
- Prefer **net-new** candidates; choose **adjacent** only when they clearly improve broad non-specialist consequence coverage and decision usefulness.
- Do **not** run AP/story preflight for dataset selection, but do run a **non-specialist consequence screen** before promotion.

Hard selection priorities (in order):
1. **Broad non-specialist consequence potential** (cost/access/safety/mobility/services) over specialist-only telemetry.
2. **Decision usefulness** for general audiences and operators, not just technical observability.
3. **Cross-domain chain value** (can the dataset connect upstream events to downstream real-world effects).
4. **Freshness and reliability** (important, but never sufficient on their own).

Anti-bias guardrails:
- **No recency anchoring:** a domain is not preferred just because it produced a recent story.
- **No convenience anchoring:** easy-to-query machine-readable feeds do not outrank relevance.
- **Domain repetition cap:** if the same domain dominated recent dataset runs, require explicit rationale to continue; otherwise rotate to a higher-impact domain.
- **NOAA-specific constraint:** do not add NOAA-centric datasets unless clear broad public consequence is demonstrated for the current run window.

### Dataset hunting protocol (event-class, cross-domain)

1. Start from situational-awareness event classes (conflict/disruption/sanctions/infrastructure/humanitarian, etc.).
2. Map each class to an impact chain (physical flows -> prices/risk -> policy/social effects).
3. Hunt datasets in **families** for each chain:
   - primary operational indicator,
   - independent confirmation indicator,
   - spillover/second-order indicator.
4. Score candidate datasets before promotion (ordered):
   - non-specialist consequence relevance,
   - decision relevance,
   - cross-domain chain contribution,
   - freshness cadence,
   - endpoint reliability,
   - baseline depth/comparability,
   - coverage breadth,
   - revision risk.
5. Prefer datasets that complete or strengthen a cross-domain chain with clear public-facing consequence; deprioritize isolated specialist telemetry without downstream decision value.
6. Recency is a tie-breaker only after consequence and decision relevance are satisfied.
7. Log misses in trace (missing source class, endpoint failure, sparse history, or failed consequence screen) to improve future hunts.

### DATASETS_OPTIMIZE cache maintenance (mandatory)

Every DATASETS_OPTIMIZE run must maintain the local dataset-change cache:
1. Run `python3 /home/pi/.openclaw/workspace/autonomous-osint-reporter/scripts/ai_osint_ctl.py discovery cache-sync`.
2. Pull a maintenance batch with `discovery cache-next` and review/scan selected entries.
3. Record scan outcomes with `discovery cache-mark` (use `--changed` when meaningful movement is detected).
4. Include cache stats in the private trace: active entries, scanned this run, changed flagged, blocked/errors.
5. Enumerate each blocked/error item in the trace with source name + URL + status/error + UTC timestamp + retry result.
6. If cache maintenance fails, treat DATASETS_OPTIMIZE as incomplete and report exact blocker(s).
7. During DATASETS_OPTIMIZE, when a dataset endpoint returns repeatable hard failures (e.g., 404 after one retry), log it as a catalog-quality issue and queue a replacement-source search in the next dataset slot.
8. Run a lightweight catalog-structure hygiene pass on scanned entries: flag title bloat/near-duplicates (for example repetitive "Application Programming Interface (API)" suffix variants) and queue canonical naming/merge cleanup for the next DATASETS_A/B slot.

## Claim-check minimum standard

A claim-check must include all of the following before publication:

- `## Claim provenance`
- Direct post URL(s) being checked
- Dateline in exact format: `**Dateline:** YYYY-MM-DD HH:MM UTC`
- Source links in evidence section
- Limitation notes (measurement and update-lag risks)

If no concrete claim-source URL exists, **do not publish in claim-check format**.

## Anti-pattern filter (important)

Avoid weak “mainstream-wire-only + regulator page” checks unless a novel OSINT angle exists.

A piece is novel when it adds at least one of:
- Primary data pull or time-series reconstruction
- Cross-source synthesis that changes the conclusion
- Geospatial or registry linkage not present in headline coverage
- Non-obvious inference that materially extends public reporting

## Lead attribution rule (mandatory)

When the initial idea comes from an existing external story/report/post, always credit it and link it.

Required behavior:
- Add an explicit `Initial lead:` line near the top of STORY posts (immediately after dateline or first paragraph).
- Include outlet/author/account name + direct URL to the lead item.
- Keep attribution specific (do not use vague phrases like “reports said”).
- Separate attribution from contribution: state what new OSINT value this piece adds beyond the lead (new data pull, falsification, cross-source test, etc.).
- If multiple leads informed the idea, list the primary lead first and move others to Sources.

## Domain prioritization (operator preference)

- Deprioritize Fed/banking-liquidity signals by default in STORY runs.
- Treat Fed/banking candidates as secondary/fallback signals; only elevate when there is a clear regime break or cross-domain consequence (e.g., broad spillover into labor, logistics, energy, conflict, or public-safety decisions).
- In the first-pass freshness scan, prefer non-Fed/non-banking domains unless data quality is materially worse.

## Cybersecurity focus gate (hard)

Permanent exclusion: do not use CISA KEV as a dataset or story source. KEV-family topics are excluded from publication and dataset intake.

Default stance: cybersecurity is secondary unless the signal is operationally meaningful.

Do not publish cyber stories based only on small statistical drift (minor ratio/percentage movement) without concrete downstream implications.

A cybersecurity story is publishable only if at least one is true:
- active exploitation trajectory materially changed,
- high-severity exposure affects critical infrastructure or broad public attack surface,
- authoritative remediation/patch guidance diverges from observed exploitation reality,
- cross-source evidence indicates a genuine anomaly likely to change defender prioritization.

If none of the above are met, drop or defer the cyber candidate and prioritize other domains.

## Story significance gate (hard, all domains)

Do not publish descriptive drift without decision consequence.

A STORY candidate is publishable only if it passes all three gates:
1. **Anomaly gate:** signal is meaningfully outside expected variation (not routine noise/batch wobble).
2. **Mechanism gate:** plausible explanation tested against at least one artifact/null alternative.
3. **Decision gate:** identifies a concrete actor/action that should change because of this finding.

## Importance gate (hard, fail-closed)

A STORY must also pass an always-on importance check before drafting and again before publish.

Pass criteria (all required):
1. **Broad relevance:** consequences are meaningful beyond specialist audiences.
2. **Concrete consequence:** at least one real-world outcome is explicit (cost/access/safety/mobility/policy/operations), not just technical-state movement.
3. **Decision utility:** a non-specialist actor can make or update a concrete decision from the reporting.

Fail-close policy:
- If importance is ambiguous or weak, do **not** publish STORY (use brief/hold/no-publish as appropriate).
- Do not treat clean/easy data access as a substitute for importance.
- If only low-importance candidates are available, return no-publish rather than force output.

Short-window ranking guardrail (hard):
- Claims like “biggest move in 7/14 days” are **candidate flags only**, not publish conclusions by themselves.
- Do not publish from a short-window rank claim unless at least one additional condition holds:
  - cross-window robustness (still notable across longer windows such as 30/90d or seasonal baseline),
  - absolute-magnitude significance (not just rank within a small window),
  - independent confirmation from another source family,
  - clear mechanism + concrete non-specialist decision consequence.

If a candidate fails any gate, discard it and continue searching.

STORY search rule:
- Keep looking for a publishable story until available datasets/source candidates for that run are exhausted.
- If exhausted and nothing passes all three gates, end with no publish (allowed).

## Story novelty and duplication gate (quality upgrade)

Do not publish a new story when it only rephrases a very recent conclusion from the same source stream.

Before drafting, run a **last-72h overlap check** against recent STORY posts:
- If headline claim, core metric, and actor/action implication are substantially unchanged, treat as duplicate and no-publish.
- A follow-on is publishable only with at least one material delta: new official release window, sign/regime change, threshold crossing, or a newly validated mechanism that changes action priority.
- Prefer “continuity noted in FOLLOWUP” over issuing near-duplicate STORY posts.
- In `research-traces/`, record one-line duplicate rationale when rejecting a candidate.

## Story format (AP style, mandatory)

Write story posts in AP-style narrative flow first, then append technical notes.

Plain-language rule (mandatory):
- Assume an informed general reader, not a specialist.
- Define acronyms and specialist terms at first mention (e.g., KEV, CVE, EPSS, BOD).
- Prefer concrete language over insider shorthand.

Required order:
1. Headline
2. Dateline
3. **Story** (clean narrative: lead, nut graf, key findings, implications)
4. **Appendix: Method**
5. **Appendix: Limitations**
6. **Appendix: Confidence**
7. **Appendix: Sources**

Do **not** include editorial throat-clearing in the story body (e.g., “why this is publishable”, “AP preflight”, internal gate checklists). If editorial justification is needed, store it in `research-traces/`.

## Method notes for internet-shutdown stories

When checking outage-duration claims:
- Separate **ordering conclusion** (A longer than B) from **exact-hour precision**.
- Treat decimal-hour values as method outputs unless independently recomputed.
- Look for partial-allowlist phases; “near zero” traffic can still coexist with whitelisted access.
- Triangulate at least two independent measurement families when possible:
  - routing/visibility signals
  - traffic/application-layer signals

## Follow-up slot discipline

- Sample recent high-impact stories (target 3–10, based on available time).
- FOLLOWUP runs do **not** publish docs posts.
- If there is a **meaningful update** (new primary data, official revision, materially changed conclusion), report it in Telegram summary and prioritize as a future STORY candidate.
- If no material updates, explicitly say so for sampled items in Telegram summary.
- **Cadence rotation rule (no exceptions):** always advance to the next slot after completing a FOLLOWUP sampling pass, even when no publishable update is found (no-op FOLLOWUP still rotates state).

## Feed rules (mandatory)

Publication policy source of truth: `/home/pi/.openclaw/workspace/ai-osint/policy/publication_policy.json`.

- Feed includes only STORY and DATASETS_INTEL publications.
- Exclude FOLLOWUP and DATASETS_OPTIMIZE entries from the public story feed.
- In feed-facing dataset headlines, use `Datasets: ...` (never `DATASETS_A/B/OPTIMIZE:` labels).
- Place dataset references at the bottom of index, below the feed (Datasets Catalog first, then Dataset Playbook).

## Publication header format (mandatory)

At the top of every published markdown post, include clickable short links in this exact style:

- `**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/<slug>.html)`
- `**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/<slug>.md)`

Also require dateline exact format:

- `**Dateline:** YYYY-MM-DD HH:MM UTC`

## Verification workflow (mandatory for stories + claim-checks)

1. **Frame the testable question**
   - Write one sentence for the exact proposition being tested.
   - Split into sub-claims if the headline mixes multiple assertions.

2. **Build an evidence ledger (private)**
   - Track each source as: URL, publisher, timestamp, what it proves, known limitations.
   - Mark every item as Observation / Inference / Unknown.

3. **Run contradiction pass before drafting**
   - Seek at least one source that could falsify the working thesis.
   - If disconfirming evidence exists, surface it prominently, not as a footnote.

4. **Check numbers mechanically**
   - Recompute percentages, deltas, ratios, and period-over-period changes.
   - State denominator and timeframe for every statistic in prose.

5. **Assign confidence by evidence quality, not intuition**
   - Confidence must map to source tier strength + method stability + recency.

## Sourcing rigor rules

- Prefer first-party machine-readable sources over screenshots, summaries, or reposts.
- Treat single-source stories as provisional unless the source is a direct primary authority.
- Timestamp sensitivity check: if data can revise, label it explicitly as preliminary.
- Quote claims precisely; do not strengthen wording beyond what the source says.
- Keep attribution close to the claim sentence (reader should not hunt for provenance).

## Claim-check quality guardrails

- Distinguish clearly between:
  - what is directly measured,
  - what is modeled/estimated,
  - what is inferred by context.
- Never let a binary verdict hide important uncertainty bands.
- If a key input is missing, choose **Inconclusive** over forced certainty.
- Include at least one "what would change this verdict" condition in limitations.

## Uncertainty language protocol (quality upgrade)

When evidence is incomplete or mixed, make uncertainty explicit at sentence level instead of burying it in limitations.

- Use **verified-status labels** in drafting notes and map to copy verbs:
  - `Verified (direct evidence)` → use verbs like *shows/measured/recorded*
  - `Likely (supported inference)` → use verbs like *indicates/suggests*
  - `Unverified claim` → use verbs like *claims/alleges/says*
- If a key artifact is user-generated content (UGC), identify it as UGC in the sentence and state what is and is not verified yet.
- For risk reporting, include scale/context in the same paragraph as the claim (avoid alarming framing without denominator/baseline).
- If verification is pending, say so directly and timestamp the latest verified checkpoint.

## Narrative clarity checklist

- Lead with the answer, then the strongest evidence, then why it matters.
- Keep paragraphs short and single-purpose.
- Replace abstract method language with concrete verbs (measured, counted, compared, matched).
- Avoid stacked caveats in one sentence; distribute them where each uncertainty appears.

## Consequence-first test (mandatory for STORY)

Before publish, run this test on paragraph 1:
- It must state a concrete broad real-world consequence (cost/access/safety/mobility/services/policy operations).
- It must identify at least one non-specialist actor decision that could change.
- If paragraph 1 cannot do both clearly, do not publish STORY as-is; rewrite or demote to fallback/hold.

## Weak-point guardrails (quality upgrade)

These rules target recurring weak spots in OSINT reporting quality: overreliance on single artifacts, weak provenance for social content, and under-explained uncertainty.

### 1) UGC provenance fit-for-claim (image/video/social posts)

Do not use a fixed checklist count. Choose checks based on what the claim actually asserts, and cover the dimensions required to validate that claim.

- If a claim depends on **where** something happened, prioritize and document location checks.
- If it depends on **when** it happened, prioritize and document timing checks.
- If it depends on **what** is shown, prioritize and document content/authenticity checks.
- If it depends on **who** posted it or chain-of-custody, prioritize and document source/provenance checks.

Available check families:
- Source check: account history, prior behavior, and whether uploader appears original vs repeater.
- Content check: reverse-image/keyframe search for prior appearances or context shifts.
- Time check: chronolocation cues (sun/shadow/weather/event timing) or upload-time consistency.
- Place check: geolocation cues matched to maps/satellite/street-level references.
- Integrity check: whether metadata is missing/stripped and how that limits certainty.

Minimum standard: evidence must cover every critical dimension of the claim; if any critical dimension remains unverified, downgrade confidence and state exactly what is missing.

### 2) Corroboration floor by claim criticality

- High-impact claims (casualties, state action, cross-border incidents, market-moving assertions): require at least 2 independent evidence families before strong verdicts.
- If all available evidence traces back to one origin, classify as provisional or inconclusive.
- Independence means not just two articles citing the same upstream post.

### 3) Falsification logging (private trace)

In `research-traces/`, add a short **"Could this be wrong because..."** block listing:
- top disconfirming hypothesis,
- what evidence would invalidate the current conclusion,
- whether that evidence was found or missing.

### 4) Attribution precision in copy

- Put attribution in the same sentence as each disputable fact.
- Distinguish verbs by evidence strength: “shows/measured” (direct), “indicates/suggests” (inference), “claims/alleges” (unverified assertion).
- Do not use certainty language (“proves”, “confirms”) unless direct primary evidence is explicit and linked.

## Corrections and updates protocol

- If a published post is materially wrong, correct fast and state what changed.
- For follow-ups, explicitly separate: unchanged findings vs new findings.
- Preserve an audit trail in `research-traces/` for major methodological changes.

## Single-source and rumor discipline (quality upgrade)

- If a high-impact claim relies on one origin (single post, single official statement, single scraper output), label the conclusion as provisional unless independent corroboration is found.
- For market- or conflict-sensitive rumor bursts, explicitly separate:
  - what is verified,
  - what is circulating unverified,
  - what evidence is still missing.
- Do not publish a strong binary verdict when key contradictory evidence is unavailable or blocked by timing gaps.

## Trace-to-copy mapping rule (quality upgrade)

Before publishing, ensure each major claim in the story body has a matching evidence entry in `research-traces/` with:
- source URL,
- timestamp/date,
- classification (Observation / Inference / Unknown),
- one-line limitation note.

If a sentence cannot be mapped, rewrite or remove it.

## Claim-origin and falsification ladder (quality upgrade)

Before drafting, force a short origin-first verification ladder for any social/UGC-sensitive claim:

1. **Origin trace first:** identify the earliest observable source/post, not just the most viral repost.
2. **Claim decomposition:** split into micro-claims (who/what/where/when/impact) and mark each as proven/unproven.
3. **Counter-evidence sweep:** search specifically for evidence that would invalidate each micro-claim.
4. **Source transparency threshold:** if origin cannot be established, cap confidence at provisional/inconclusive.
5. **Narrative fit check:** ensure headline reflects only the strongest still-valid micro-claims.

Rationale alignment:
- Mirrors Reuters standards emphasis on cross-checking, source honesty, and trying to disprove initiative reporting.
- Mirrors Reuters Fact Check methodology of identifying claim origin and linking supporting evidence.
- Mirrors Bellingcat’s originality/source/location/time verification sequence.

## Copy desk pass (mandatory before publish)

Run a final newsroom-style pass focused on accuracy and readability, not prose flourishes:

- **Claim-to-source sweep:** every factual sentence maps to a linked source or is explicitly labeled inference.
- **Attribution verb audit:** use verb strength that matches evidence quality (`shows` vs `suggests` vs `claims`).
- **Numerical hygiene:** units, denominators, and time windows are explicit and internally consistent.
- **Uncertainty placement:** caveats appear where the uncertainty is introduced, not buried later.
- **Headline discipline:** headline states the strongest defensible conclusion, not the most dramatic framing.

## Disconfirming-evidence prominence (quality upgrade)

To reduce confirmation bias and improve trustworthiness, surface the strongest challenge early instead of burying it in limitations.

- In the story body (not just appendix), include a short **"What could overturn this"** sentence/paragraph whenever evidence is mixed or still developing.
- If credible counter-evidence exists, place it in the first half of the story and explain why it does or does not change the current conclusion.
- If no disconfirming artifact was found, say so explicitly and state the exact search gap (time window, missing registry update, unavailable telemetry, etc.).
- Never present a strong verdict without naming the top unresolved contradiction risk.

## Attribution density rule (quality upgrade)

For disputable claims, attribution must be near-immediate and specific.

- Any sentence that could reasonably be contested should contain attribution in the same sentence or immediately adjacent sentence.
- Prefer explicit actor/source nouns over vague references (e.g., "according to IODA outage telemetry" not "data shows").
- If using anonymous/indirect sourcing in rare cases, explain why identity/details are limited and what verification was done independently.

## FOLLOWUP staleness gate (quality upgrade)

When FOLLOWUP cycles repeatedly return unchanged outputs, avoid low-value reruns that only restate the same numbers.

- If the same sampled items have shown **no material update across 2+ consecutive FOLLOWUP runs**, rotate at least one sampled item to a different recent high-impact publication.
- Keep at least one continuity check from prior cycle, but require one freshness check (new source family, new topic, or newly published post) before deciding no-publish.
- If all sampled items are unchanged, explicitly record the staleness condition in `research-traces/` and use concise no-publish language.
- Do not manufacture updates; this gate improves sampling quality, not publication pressure.

## Publication-policy preflight (quality upgrade)

Before finalizing a STORY or DATASETS post, run a quick policy-shape check on the markdown source to avoid preventable publish/commit rejects.

- STORY headlines should be plain-language and should **not** append technical type markers like `(osint-story)`.
- Dataset posts must begin with `Datasets:`.
- Keep top-of-file link block + dateline format exactly compliant.
- If a post fails policy checks, fix markdown first, then regenerate HTML artifacts.

## Working-tree hygiene for cadence reliability (quality upgrade)

To reduce avoidable rebase interruptions and accidental broad diffs:

- Before `git pull --rebase`, check whether unrelated generated HTML drift exists.
- If unrelated drift is present, stash it with a timestamped note, complete the slot task, and avoid mixing that drift into the slot commit.
- Keep slot commits scoped to intentional content + required generated artifacts only.

## Rapid challenge pass (quality upgrade)

Before final draft lock, run a 5-minute adversarial check to reduce confirmation bias:

1. Write the strongest one-sentence counter-thesis to your current conclusion.
2. Attempt one targeted search/query that would support that counter-thesis.
3. If found, surface it in the story body (not only limitations) and adjust confidence.
4. If not found, document exact gap searched (time range/source family/query) in `research-traces/`.

This operationalizes Reuters’ “try to disprove as well as prove your story” guidance as a repeatable newsroom step.

## Disputable-fact attribution SLA (quality upgrade)

For any sentence containing a disputable fact, enforce a strict attribution window:

- Attribution must appear in the **same sentence** or the **immediately adjacent sentence**.
- If attribution is further away, rewrite before publish.
- When multiple consecutive facts come from one source, restate attribution at least once per paragraph.

Goal: readers should never need to scan far to find provenance for contestable claims.

## Evidence independence test (quality upgrade)

When using multiple sources for corroboration, verify true independence:

- Do not count two items that cite the same upstream origin as independent confirmation.
- Mark each source in trace with an `upstream origin` field (if known).
- For high-impact claims, require at least two different upstream origins or downgrade to provisional/inconclusive.

This aligns corroboration practice with AP’s requirement for independent corroboration around sensitive anonymous/secondhand information.

## STORY no-publish exhaust protocol (quality upgrade)

When a STORY slot cannot publish a standard story, do not stop at NO_PUBLISH by default. Use the dataset fallback path.

Minimum trace requirements:
- Show that discovery remained open during the scan window (no fixed upfront candidate cap) and record attempted candidates.
- Before no-publish/fallback decision, check the full local dataset-change cache for this run window (review all cache entries, prioritizing recently changed/unscanned items), or document a concrete technical blocker for any cache segment not checked.
- For each attempted candidate, record:
  - freshness artifact checked,
  - anomaly result (outside range vs routine),
  - mechanism test attempted,
  - concrete decision actor/action impact test,
  - **importance gate result** (pass/fail with one-line rationale),
  - final reject reason tied to failed gate(s).
- Include one-line duplicate check result against last-72h stories for any near-overlap candidate.
- Include one-line anti-convenience check: why the selected publish candidate beat higher-friction alternatives on importance (not ease).

### Mandatory fallback for non-publishing STORY runs

If no standard STORY candidate passes, execute fallback:
1. Before choosing a fallback topic, run a broad comparison set across all available source families/domains in scope for the run and record why each did or did not qualify.
2. Find at least one **new, currently relevant** dataset tied to active world developments.
3. Add it to the catalog in the same run.
4. Publish a dataset-focused **Dataset Brief** (not an event STORY) explaining:
   - what the dataset is,
   - scope/bounds/limitations,
   - how to use it (query/analysis approach),
   - why it is potentially useful/important now.
5. Use clear dataset-intel/dataset-brief framing and naming (avoid `osint-story` slug/type markers); avoid pretending this is an event-anomaly story.
6. Only emit true NO_PUBLISH if both standard STORY and dataset fallback fail, with explicit blockers.

Publishing pressure rule:
- Do not lower significance thresholds to force a weak event story.
- Prefer a high-utility dataset fallback over a low-importance specialist event write-up.

## Mechanism-first claim sentence template (quality upgrade)

For quantitative anomaly stories, the first two paragraphs should follow this order:
1. **Observed change** (measured delta + denominator/time window)
2. **Best-tested mechanism** (what likely explains it, with attribution)
3. **Decision consequence** (who should do what differently now)

If mechanism remains unresolved:
- State unresolved status explicitly in paragraph 2,
- downgrade confidence,
- and include a specific “what evidence is missing” line in body text.

This reduces descriptive-drift stories that report movement without explaining causal relevance.

## Attribution-first paragraph protocol (quality upgrade)

To reduce "fact blob" leads and improve reader trust, enforce attribution structure in the first two paragraphs of any STORY/claim-check draft:

1. **Paragraph 1:** strongest defensible finding with immediate source attribution (same sentence or adjacent).
2. **Paragraph 2:** strongest counterpoint/uncertainty with explicit source attribution and what evidence is still missing.
3. If either paragraph has disputable facts without nearby attribution, rewrite before publish.

Rationale alignment:
- AP guidance emphasizes placing attribution in the same sentence (or immediately adjacent) for disputable facts.
- Reuters standards emphasize honesty/transparency in sourcing and testing whether the story withstands challenge.

## Corroboration independence ledger (quality upgrade)

For high-impact claims, add an explicit mini-ledger in `research-traces/` before final confidence assignment:

- `claim_id`
- `source`
- `upstream_origin`
- `evidence_family` (official record / telemetry / on-scene UGC / media synthesis)
- `independent_of` (list claim_ids it is truly independent from)
- `proves` (micro-claim)
- `limitation`

Hard rule:
- Do not count two items as corroboration if they share the same upstream origin.
- If fewer than two independent evidence families remain after deduplication, cap verdict at provisional/inconclusive.

Rationale alignment:
- Reuters and AP both stress corroboration strength and source credibility over sheer source count.

## Cadence safety checks before push

- Confirm new output has working source links
- Keep commit scope tight (avoid unrelated HTML churn)
- Verify GitHub Pages endpoint reflects latest commit before reporting success
