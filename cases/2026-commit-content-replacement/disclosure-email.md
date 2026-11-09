# Private notification draft — not sent

**To:** info@awadh.org.in  
**For:** COMM-IT Career Academy administration / website administrator  
**Subject:** Website security concern: gambling promotion at commit.org.in — request for review

Dear COMM-IT Career Academy / Awadh Centre of Education team,

While reviewing your publicly accessible website on 9 November 2026, I observed a concerning difference between these two pages:

- `https://commit.org.in/` serves a page headed “DEWANAGA | Platform Centre of Edukasi Slot Paling Hoki Hari Ini”, containing slot-gambling promotions and login/registration links to the external domain `commit[.]dinassosial[.]online`.
- `https://commit.org.in/home.html` serves COMM-IT Career Academy content, including its affiliation information and institutional contact details.

The root page also contains Indonesian text claiming support from COMM-IT Career Academy staff. I have not verified that claim and am bringing it to your attention because visitors could interpret it as institutional endorsement.

Existing Internet Archive captures show academy content at the HTTPS root on 7 June 2026 and the DEWANAGA promotion on 12 July and 2 October 2026. These are dated observations, not an exact incident start date.

This is consistent with unwanted website content replacement or SEO spam. I cannot determine from public pages whether the cause is a hosting, deployment, account, domain, or routing issue, or whether the institution authorised any of the content.

I preserved the public responses, timestamps and SHA-256 hashes, and prepared a short technical report. My review used public page retrieval and existing web archives. It did not include login attempts, vulnerability scanning, form submissions, or interaction with the advertised gambling service.

Please forward this message to your website administrator or hosting provider. I suggest preserving relevant files and logs before changing the site, checking the root-page deployment and routing against a known-good backup, and reviewing administrative access. Please also check whether the domain remains under the academy's current management.

Could you acknowledge receipt and identify the technical contact who can review the evidence? A preliminary research draft is available at https://github.com/RatioJuris/security-research/tree/main/cases/2026-commit-content-replacement and currently records institutional notification as pending. I would welcome corrections to any factual point and would like to coordinate follow-up updates after you have had an opportunity to investigate. I will update the disclosure record to reflect this notification and any response.

Regards,  
Isrg Rajan  
RatioJuris — Security Research  
RatioJuris@duck.com  
https://github.com/RatioJuris/security-research

---

## Sending notes

- Confirm the sender name and reply address before sending. This draft has not been emailed.
- The proposed recipient is published on `home.html` (Cloudflare-obfuscated email) and on `https://awadh.org.in/`; this is contact corroboration across two pages, not confirmation of mailbox ownership or a dedicated security desk.
- The shared public telephone number is **+91-9717807222**. It can be used to ask that the message reach the website administrator if email does not reach the right team.
- Attach `README.md`, `evidence.md` and the three screenshot PNGs initially, or export the reports and `screenshots.md` gallery to a document. Offer the captured source files separately; they include page scripts and anonymous response metadata.
- Record the actual sent time and any acknowledgement in `disclosure-log.md`. Avoid describing a draft as a completed disclosure.
