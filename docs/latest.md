# Sanctions screening feeds are running on different clocks, creating a measurable update-window risk

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-03-06-sanctions-feeds-out-of-sync-update-clock-risk-osint-story.html)  
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-03-06-sanctions-feeds-out-of-sync-update-clock-risk-osint-story.md)

**Dateline:** 2026-03-06 17:28 UTC

## AP preflight (publishability gate)

1. This is publishable now because sanctions compliance is operationally time-sensitive, and primary-source feeds currently show non-trivial update-clock divergence across major authorities.
2. What is new: this piece quantifies the *metadata-level timing mismatch* (not just list-content differences) between OFAC, Canada, and UN consolidated feeds.
3. Who is affected/what changes: financial institutions, logistics/compliance teams, and OSINT monitors relying on automated screening pipelines may face temporary blind spots if they assume synchronized refresh cycles.
4. Strongest “not a story” counterargument: all screening programs should already account for asynchronous publication, so this is expected operations rather than news.
5. **Editor verdict: Publish** — the cross-source, timestamped evidence provides a concrete, current risk window and a clear process implication for high-impact compliance workflows.

## What changed / why now

As of 2026-03-06, the latest machine-readable sanctions sources are not updating on the same operational clock:
- OFAC SDN export was last modified on **2026-03-06** (same day).
- UN consolidated list reports last substantive update on **2026-02-27**.
- Canada’s consolidated page states list updated **2026-02-19**, while the XML file itself shows a newer file-level modification date (**2026-03-04**), indicating possible transport refresh without clearly stated substantive list change.

This is an OSINT-significant pattern because many downstream screening systems are treated as if “global sanctions data” refreshes as one stream.

## Significance gate

- **If true:** institutions using multi-jurisdiction screening can miss newly effective designations during the asynchronous gap unless they implement jurisdiction-specific freshness rules.
- **If false:** apparent lag is a metadata artifact with little practical impact; current controls are likely sufficient.
- **Who is affected:** sanctions compliance units, correspondent banking operations, maritime/trade screening desks, and investigative analysts.

## Evidence

1. **OFAC Sanctions List Service (SDN CSV export)**
   - Endpoint returns machine-readable SDN rows; retrieved header showed `Last-Modified: Fri, 06 Mar 2026 15:02:59 GMT`.
   - Retrieved 2026-03-06 17:23 UTC.
   - Source: [OFAC SLS SDN.CSV](https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/SDN.CSV)

2. **Consolidated Canadian Autonomous Sanctions List (Global Affairs Canada)**
   - Official page states: “list was last updated on February 19, 2026.”
   - Retrieved 2026-03-06 17:23 UTC.
   - Source: [Canada consolidated sanctions page](https://www.international.gc.ca/world-monde/international_relations-relations_internationales/sanctions/consolidated-consolide.aspx?lang=eng)

3. **Canada XML feed metadata**
   - XML endpoint header showed `Last-Modified: Wed, 04 Mar 2026 17:50:25 GMT`.
   - Retrieved 2026-03-06 17:23 UTC.
   - Source: [Canada XML feed](https://www.international.gc.ca/world-monde/assets/office_docs/international_relations-relations_internationales/sanctions/sema-lmes.xml)

4. **UN Security Council consolidated list**
   - UN consolidated-list page states the list “was last updated on 27 February 2026.”
   - Retrieved 2026-03-06 17:24 UTC.
   - Source: [UNSC Consolidated List page](https://main.un.org/securitycouncil/en/content/un-sc-consolidated-list)

## Method (reproducible)

- Queried primary-source machine endpoints and list pages for three authorities (US OFAC, Canada, UN).
- Recorded two freshness indicators where available:
  1. **Declared substantive update date** on official page text.
  2. **Transport-level file freshness** from HTTP `Last-Modified` header.
- Compared date deltas across authorities to identify asynchronous windows relevant to screening operations.

## Hypotheses and adjudication

1. **H1: Major sanctions sources are currently out of sync by multiple days (supported).**
   - Prediction: latest update markers differ materially across authorities.
   - Result: observed same-day OFAC vs 27 Feb UN vs 19 Feb declared Canada page update.

2. **H2: Canada feed may show file-level refresh without clear substantive-list update (supported).**
   - Prediction: page-declared date and XML `Last-Modified` date diverge.
   - Result: observed 19 Feb (declared) vs 04 Mar (file metadata).

3. **H3 (null/artifact): differences are purely formatting artifacts with negligible operational meaning (mixed).**
   - Prediction: no plausible screening impact from timing offsets.
   - Result: not fully rejected; impact depends on local control design, but asynchronous windows are objectively present.

## Limitations

- This analysis measures **freshness metadata windows**, not full content-level diff of every designation across jurisdictions.
- Jurisdictional sanctions scopes differ by law and mandate; list-size or update-date mismatch does not imply legal inconsistency.
- HTTP `Last-Modified` can reflect file regeneration or hosting-layer changes, not necessarily net-new designations.

## Confidence

**Medium.** Timing divergence is directly observed from primary sources, but operational risk magnitude will vary by institution-specific ingestion and escalation controls.

## One-line decision relevance

Treat sanctions ingestion as jurisdiction-specific clocks, not a single global refresh stream, or accept measurable blind-spot windows.
