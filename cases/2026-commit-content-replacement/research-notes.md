# R&D notes and unresolved questions

## Research completed

1. Compared the user-supplied root and `/home.html` using public retrieval, then preserved separate HTTP responses.
2. Identified promotional title, body text, external navigation targets, an institutional-support claim, metadata, hidden backlinks and template remnants directly in source.
3. Retrieved a monthly-collapsed existing archive index and four exact historical root captures. Matching `Memento-Datetime` headers support the selected archive dates.
4. Established academy content in March and June, and DEWANAGA content in July and October, followed by a live November observation. The June and July captures use the same HTTPS root URL.
5. Corroborated the proposed administrative contact using academy and Awadh public pages.
6. Saved response bodies, serialized headers, request metadata and SHA-256 manifests, with offline verification scripts and a repeatable limited collector.
7. Added three live browser screenshots with JavaScript disabled and resource requests restricted, alongside the corresponding document responses, capture metadata and request log. See `screenshots.md`.

## Hypotheses requiring owner-side evidence

These are alternative explanations to investigate, not findings of an intrusion mechanism.

| Question / hypothesis | Why it remains relevant | Evidence needed from the owner |
|---|---|---|
| Unauthorised root/default-document replacement | Root and named home page have different identities | Deployed file inventory, trusted backup comparison, file/build history and deployment logs |
| Routing, rewrite or CDN/edge modification | Different paths can be served by different rules; live responses report cache hits | Origin mapping, routing/default-document configuration, edge-function versions and administrative audit logs |
| Hosting or deployment-account misuse | Changes can be deployed without a web-application exploit | Administrative sign-ins, session history, credential/token inventory and deployment events |
| Domain transfer, lapse, intentional repurposing or stale institutional content | Historical use and residual pages do not prove current ownership or lack of authorisation | Registrar history, renewal/transfer records, institutional confirmation and hosting contract history |
| Broader origin compromise or persistence | A public-page symptom alone does not reveal the full affected scope | Owner-led file-integrity review, server logs, scheduled tasks, access review and incident-response findings |

The presence of older ASP.NET-looking markup or historical IIS headers does not demonstrate an ASP.NET vulnerability or an unpatched current server. The WordPress markup on the separate Awadh site is not evidence about the affected domain's underlying implementation.

## Useful follow-up questions for the institute

- Is `commit.org.in` still under your control, and is any gambling-related publication authorised?
- What should a visitor see at `/` today, and what role does `/home.html` have in the current deployment?
- Did a migration, hosting change, domain event or deployment occur around the June–July observation interval?
- Which team or provider can preserve the relevant logs and compare approved deployments?
- Have students or staff reported unexpected destinations, and has the institute already taken corrective action?
- Which factual corrections or publication timing should be reflected in the research record?

## Follow-up research once facts change

- Preserve fresh public root and home-page responses after an owner-reported fix. Check title, academy identity, external destinations and hidden metadata, not just HTTP status.
- Add a separate dated outcome record and new evidence hashes. A single normal response cannot demonstrate removal of every persistence mechanism.
- If the institution supplies an earlier report, approved baseline, or confirmed ownership change, revise the timeline and classification explicitly.
- If JavaScript-enabled behaviour becomes material, obtain a separate controlled capture with recorded URLs and timestamps. Current screenshots use JavaScript-disabled rendering and do not establish normal interactive behaviour.

## Potential research contribution

The supported lesson is that an institution's explicit home-page path can continue to show educational content while its root presents unrelated promotional material. Availability checks or checks of only `/home.html` can miss this identity mismatch. Monitoring expected identity, outbound destinations, and hidden page metadata on key entry points would address the observed gap.

Potential public summary, to be updated after disclosure:

> Passive research documented gambling promotion at an institutional website's root while a named home page continued to serve academy content. Dated archive captures, source excerpts and integrity manifests support the observations. Administrative notification and remediation status are recorded separately from the technical findings.

Do not claim the research secured the institute's systems, identified an attacker, prevented a breach, or resulted in a fix unless later evidence supports those outcomes.
