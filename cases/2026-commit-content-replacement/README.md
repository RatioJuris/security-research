# COMM-IT website: gambling content replacement / SEO spam (2026)

**Public research draft — institutional notification pending.**

Part of [RatioJuris/security-research](https://github.com/RatioJuris/security-research), alongside the repository's other research cases.

| | |
|---|---|
| Website | `commit.org.in`, historically serving COMM-IT Career Academy, New Delhi |
| Observed condition | Root page serves DEWANAGA gambling promotion; `/home.html` serves academy content |
| Classification | Suspected unwanted content replacement / SEO spam; public content verified, authorisation and cause unresolved |
| Research date | 9 November 2026 |
| Earliest reviewed gambling capture | 12 July 2026, 14:26:22 UTC |
| Latest reviewed academy root capture before that | 7 June 2026, 16:27:29 UTC |
| Suggested operational priority | Prompt administrator review: public-facing identity and visitor-navigation impact |
| Disclosure / outcome | Draft prepared; not sent; no remediation confirmed |
| Researcher | Isrg Rajan / RatioJuris |

## Executive summary

On 9 November 2026, ordinary HTTPS GET requests to `https://commit.org.in/` and `https://commit.org.in/home.html` both returned HTTP 200 but substantially different content. The root returned an Indonesian-language DEWANAGA slot-gambling promotion with external login and registration links. The named home page returned COMM-IT Career Academy's educational content and contact details.

The root's gambling text explicitly claims support from academy staff. That statement is **a claim made by the page**, not an established fact about the institution. Its title, social metadata, alternate-page references, and hidden gambling-related backlinks are consistent with an SEO-spam content replacement. The suspicious content is present in the returned HTML itself; it does not depend on a browser extension or script execution to appear in the source.

Existing Internet Archive responses show academy content at the HTTPS root on 7 June 2026 and the DEWANAGA material on 12 July and 2 October 2026. These establish a change between sampled observations, not an exact intrusion date, an uninterrupted incident, or a last-known-secure system state.

The evidence supports notifying the institution promptly. It does not identify the responsible actor, the entry point, current domain ownership, whether the institution authorised the changes, or a breach of student records.

**Visual evidence:** [three browser screenshots](screenshots.md) show the root page, its promotional text, and the academy home page. Capture times, settings and hashes are included.

## Findings

Evidence IDs and exact excerpts are in [`evidence.md`](evidence.md). Confidence here concerns the stated observation, not the cause.

### F1. Gambling content is served directly at the domain root

**Evidence: E1, E7, E8. Confidence: high.**

The live root's HTML title and H1 are “DEWANAGA | Platform Centre of Edukasi Slot Paling Hoki Hari Ini”. The body promotes slot games and registration. The same title and key promotional text occur in the reviewed July and October archive responses.

The live response is HTTP 200. The collector did not follow redirects. Thus the captured behaviour is delivery of promotional HTML at the institutional URL, rather than an observed HTTP redirect to another domain. Browser-triggered navigation was not evaluated.

### F2. Institutional content remains accessible at a separate path

**Evidence: E2, with historical context from E5 and E6. Confidence: high.**

`/home.html` identifies COMM-IT Career Academy as a unit of Awadh Centre of Education and states affiliation to GGS Indraprastha University. Its canonical URL points to `/home.html`. Historical root captures also identify the academy.

This is a **path-dependent content difference**. It does not demonstrate user-agent cloaking, geographic targeting, or a particular default-document configuration. The academy-looking page is a comparison artifact, not a security certification or a verified restoration source.

### F3. Login and registration links send visitors toward an external service

**Evidence: E1 lines 1336–1337 and 1891–1892; also E7 and E8. Confidence: high.**

Links labelled `LOGIN`, `DAFTAR`, `DAFTAR DEWANAGA`, and `LOGIN DEWANAGA` point to `commit[.]dinassosial[.]online`. The same host appears in `amphtml` and Indonesian-language alternate-page references.

The HTML provides a route away from the institutional site. Actual clicks, the destination's current response, credential collection, financial transactions, and downstream harm were not observed.

### F4. The promotion invokes the academy's name as an endorsement

**Evidence: E1 line 2392; also E7 and E8. Confidence: high for the text's presence.**

The phrase `didukung oleh staff COMM-IT Career Academy` approximately means “supported by COMM-IT Career Academy staff”. In context, it appears within a gambling promotion. This creates a risk of misleading visitors about institutional endorsement. Whether any endorsement was actually authorised is unresolved.

### F5. Metadata and hidden links are consistent with SEO spam

**Evidence: E1 lines 8–56 and 3447–3448; also E7 and E8. Confidence: high for markup, moderate for inferred purpose.**

The page advertises `index, follow`, associates its canonical and social URLs with the academy domain, and includes hidden list items using `style="display:none"` with anchor text `slot` and `slot mahjong`. Their destinations are listed, defanged, in [`iocs.csv`](iocs.csv).

These are SEO-spam indicators. No search-engine indexing status, ranking change, traffic volume, or connection between the linked sites has been established. Two web searches during initial contact research returned no results; that is not evidence of deindexing.

### F6. The source contains marketplace-template remnants and a claimed credit

**Evidence: E1 lines 55–74 and 2625. Confidence: high for the strings; attribution unresolved.**

The root includes Bonanza asset references, product metadata, and a `BONZ` configuration object. A credit reads `CREATED BY :SEOMUKSEP X DEWANAGA.` These support the description of a repurposed marketplace-style page, but do not establish where it was copied from or who deployed it. Bonanza, Cloudflare, Google Fonts, and Imgur references are not evidence that those services caused the incident. A page credit is not verified actor attribution.

### F7. Public responses are being served through a cache

**Evidence: E1 and E2 response headers. Confidence: high for reported headers.**

Both live responses report `Server: cloudflare` and `cf-cache-status: HIT`. The root reports a `Last-Modified` value of 11 June 2026; that is server-supplied metadata, **not a verified incident timestamp**. The page's embedded “Rendered at” date is likewise not forensic timing evidence.

An administrator should verify both deployed content and relevant cache/routing configuration when restoring service. The headers do not reveal the origin server or demonstrate compromise of Cloudflare. Historical IIS/ASP.NET headers in E5 describe the archived response, not a confirmed current technology inventory.

## Timeline

Archive observation times are UTC. Live collection times come from the research machine and are recorded alongside response headers.

| Observation time (UTC) | Observed state | Evidence |
|---|---|---|
| 2026-03-01 00:31:29 | HTTP root archive identifies COMM-IT Career Academy | E5 |
| 2026-06-07 16:27:29 | HTTPS root archive identifies COMM-IT Career Academy | E6 |
| 2026-07-12 14:26:22 | HTTPS root archive contains DEWANAGA promotion, external login links, endorsement claim and hidden backlinks | E8 |
| 2026-10-02 00:22:40 | HTTPS root archive contains the same key indicators | E7 |
| 2026-11-09 18:16:22–18:16:25 | Live root and `/home.html` captured; gambling / academy content difference confirmed | E1, E2 |
| 2026-11-09 18:48:24–18:48:29 | Three restricted-browser screenshots captured from fresh live document responses | S1–S3, `screenshots.md` |
| 2026-11-09 | Contact corroborated and notification drafted | E2, E3; `disclosure-email.md` |
| Pending | Actual institutional notification, acknowledgement, and remediation | `disclosure-log.md` |

The archive index was monthly-collapsed and limited. Four archived bodies were reviewed; this is not a complete domain history. No claim is made about earlier unreviewed incidents, states between samples, or the first-ever appearance of the gambling content.

## Impact assessment

**Observed:** replacement of the root's educational identity with gambling promotion; external login/registration links; an institutional-support claim; hidden gambling backlinks.

**Plausible consequences:** visitor confusion, diversion from admissions or institutional information, reputational harm, misleading search/social previews, and visitor exposure to external gambling services.

**Unresolved:** actual traffic affected, financial loss, personal-data exposure, origin-system access, persistence, and the relationship of this domain to any current production admissions or learning system. No exploit or technical vulnerability has been demonstrated, so a CVSS score would be unjustified.

## Administrator investigation and recovery

These are proposed owner-side actions, not actions performed by this research.

1. **Preserve evidence before making changes.** Retain deployed files or build artifacts, a hosting snapshot if available, access/error logs, deployment history, administrator sign-ins, and DNS/CDN audit history. Record timezone and log retention. Include the June–July observation interval, with a wider look-back if records support it.
2. **Confirm ownership and intended service.** Verify current control of the domain, registrar, hosting account, deployment provider and CDN. Confirm whether the academy intended the root to serve its home page or whether the domain was retired, transferred or repurposed.
3. **Compare root handling with known-good configuration.** Review default-document order, route/rewrite rules, edge functions and recent deployments. Compare against trusted backups and approved content, including title, metadata, links and associated assets. Do not treat `/home.html` alone as a verified clean backup.
4. **Contain and restore.** If the content is unauthorised, preserve it first, then replace affected public content with an institution-controlled page or a minimal maintenance notice. Correct the underlying deployment/routing problem and purge affected caches after the origin or deployment is corrected.
5. **Review access and persistence.** Audit administrative accounts, active sessions, hosting/SFTP/SSH credentials, deployment tokens and scheduled jobs. Revoke unexplained access, rotate affected secrets and enable MFA where supported. Apply updates based on the actual inventory and findings rather than assuming a CMS or exploit from the HTML.
6. **Validate recovery.** Capture fresh public responses for both the root and expected home page. Verify identity, navigation, page metadata and removal of unwanted destinations. Have the owner test representative browsers and key institutional workflows. Keep these as new evidence, preserving the original captures.
7. **Repair discovery and improve monitoring.** Through owner-controlled search-console tools, inspect indexing and request recrawling after restoration. Monitor expected page identity and unexpected destination domains, alongside availability. Publish a security contact so later reports reach the responsible team.

See [`research-notes.md`](research-notes.md) for the unresolved hypotheses and evidence needed to resolve them.

## Method and limits

- Preliminary public text/HTML retrieval was followed by preservation of three live pages, one existing archive index, and four existing archive responses: **eight initial preserved responses**, all HTTP 200 and untruncated. A later browser pass preserved two additional document responses and three screenshots.
- `collect.py` uses standard-library HTTPS retrieval with certificate verification, a fixed source list, a disclosed user-agent, no credentials, and no redirect following. It saves bodies as `.txt`, serialized response headers, request metadata, and SHA-256 manifests.
- The initial preservation run fetched no linked scripts or images. The screenshot pass allowed images, stylesheets and fonts from a limited host list and blocked page scripts and other requests. Neither pass visited gambling destinations, administration endpoints or student-service endpoints. There was no scanning, authentication, submission, exploitation, or remote modification. No new public archive submission was made.
- Findings concern returned source, archive records and a restricted-browser view. The [screenshot gallery](screenshots.md) records JavaScript-disabled rendering, the selected resource restrictions and a request log. This is not a JavaScript-enabled behaviour trace or a full malware assessment; interactive elements and layout may differ for other visitors.
- Hashes verify saved bytes against a manifest; they are not digital signatures, trusted timestamps, or proof of who published the content. Archive capture times are supported by CDX entries and matching `Memento-Datetime` headers. Retrieval occurred on 9 November, not on the historical capture dates.

## Evidence verification

Verify all three saved bundles offline in PowerShell:

```powershell
.\verify.ps1
.\verify.ps1 -CaptureDirectory .\captures\history-july
.\verify.ps1 -CaptureDirectory .\captures\browser-initial
```

Or with Bash and `sha256sum`:

```bash
bash verify.sh
bash verify.sh captures/history-july
bash verify.sh captures/browser-initial
```

To make a later, separate observation of only the two live pages:

```powershell
python collect.py captures/follow-up E1 E2
```

To re-fetch only the four existing archive responses into a new directory:

```powershell
python collect.py captures/archive-recheck E5 E6 E7 E8
```

A changed live-response hash is not proof of continuing compromise or recovery; inspect the content. Even archive replay bytes may vary because of transport/replay processing. Compare substantive indicators and archive timestamps as well as hashes. The collector refuses to overwrite an existing directory.

## Files and next step

| File | Purpose |
|---|---|
| [`evidence.md`](evidence.md) | Source register, hashes, exact excerpts and archive links |
| [`screenshots.md`](screenshots.md) | Three unannotated browser screenshots, capture settings and timestamps |
| [`iocs.csv`](iocs.csv) | Defanged, contextual indicators; not an indiscriminate blocklist |
| [`research-notes.md`](research-notes.md) | R&D findings, hypotheses and follow-up questions |
| [`disclosure-email.md`](disclosure-email.md) | Ready-to-review private notification draft |
| [`disclosure-log.md`](disclosure-log.md) | Accurate disclosure and publication status |
| [`collect.py`](collect.py) | Repeatable fixed-scope response preservation |
| [`capture-screenshots.py`](capture-screenshots.py) | Repeatable restricted-browser screenshot capture |
| [`verify.ps1`](verify.ps1), [`verify.sh`](verify.sh) | Offline integrity checks |
| [`captures/initial/`](captures/initial/) | E1–E7 bodies, headers, metadata, CSV and hash manifest |
| [`captures/history-july/`](captures/history-july/) | E8 body, headers, metadata, CSV and hash manifest |
| [`captures/browser-initial/`](captures/browser-initial/) | Screenshot PNGs, corresponding document bodies and headers, browser metadata and hash manifest |

**Next step:** send the reviewed notification to `info@awadh.org.in`, record the actual disclosure, and coordinate follow-up updates. This preliminary case is published in the existing `RatioJuris/security-research` repository. Publication precedes institutional notification; no completed disclosure or remediation is claimed. See `disclosure-log.md` for the current status.
