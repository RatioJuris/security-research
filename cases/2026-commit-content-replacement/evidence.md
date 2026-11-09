# Evidence register — COMM-IT content replacement

All responses were preserved on **9 November 2026**. E1–E7 were retrieved at 18:16:22–18:16:43 UTC; E8 at 18:17:20–18:17:24 UTC. Every preserved request returned HTTP 200, with no redirects followed or body truncation. Exact request and completion times are in the two CSV registers and per-response metadata.

Bodies retain the bytes delivered to the HTTP client after transfer framing. The saved response headers are Python's text serialization of parsed fields, not raw wire bytes. All bodies have `.txt` extensions and were inspected as source. Original response bodies and header files have not been redacted or reformatted. No content was executed.

## Source register

E1–E7 are under [`captures/initial/`](captures/initial/); E8 is under [`captures/history-july/`](captures/history-july/).

| ID | Body file | Source / archive observation | Bytes |
|---|---|---|---:|
| E1 | `live-root.body.txt` | Live `https://commit.org.in/` | 136998 |
| E2 | `live-home.body.txt` | Live `https://commit.org.in/home.html` | 116709 |
| E3 | `contact-awadh.body.txt` | Live `https://awadh.org.in/` | 396286 |
| E4 | `archive-index.body.txt` | [CDX query](https://web.archive.org/cdx/search/cdx?url=commit.org.in%2F&matchType=exact&output=json&filter=statuscode%3A200&filter=mimetype%3Atext%2Fhtml&collapse=timestamp%3A6&from=2025&to=2026&limit=24) | 2541 |
| E5 | `archive-20260301.body.txt` | [HTTP root, 2026-03-01 00:31:29 UTC](https://web.archive.org/web/20260301003129id_/http://commit.org.in/) | 120822 |
| E6 | `archive-20260607.body.txt` | [HTTPS root, 2026-06-07 16:27:29 UTC](https://web.archive.org/web/20260607162729id_/https://commit.org.in/) | 117086 |
| E7 | `archive-20261002.body.txt` | [HTTPS root, 2026-10-02 00:22:40 UTC](https://web.archive.org/web/20261002002240id_/https://commit.org.in/) | 136631 |
| E8 | `archive-20260712.body.txt` | [HTTPS root, 2026-07-12 14:26:22 UTC](https://web.archive.org/web/20260712142622id_/https://commit.org.in/) | 137135 |

### Body SHA-256 values

```text
E1 fbf62bcca873b4ec70f73ca22ebc82bd239a81417d40d5a790e53cf44be595a6
E2 3ec740e263b8d7f3ba402d787960c6c9c2d43c595a86bbb426e13518090ce71b
E3 a24d71bd6e88cb1a8525ed93e020237b0f73e1e66b24bd6fd01ba49aa8a3ff5c
E4 79cb1276e69218057941217b1a3ee9a61b381bd3940e9fa4d0aafa4f958b3ee4
E5 290d38e9cdf696de3adabb81b2f26073e8b5d37a575878c72ca20fc0e8607a17
E6 ba311943712201c502c3356a93a3a826aa1e34023b42a3b02d438aa48a635bc0
E7 6f7d02d37fd9349c410c3a64e881296ed9913fab0c7c1d36bf199dbd454f3ddc
E8 2c0c63b29bf34bad91b6da260982aacd90d5cd79c8fbb2c5fb98451387449164
```

The manifests also hash headers, metadata and the CSV registers: [initial manifest](captures/initial/SHA256SUMS), [July manifest](captures/history-july/SHA256SUMS). These hashes establish local integrity, not an independent timestamp or proof of origin.

## E1 — live root: directly served gambling promotion

Source: [`live-root.body.txt`](captures/initial/live-root.body.txt). Line numbers below refer to this preserved file, not a later live response. Snippets are exact selected lines; omitted lines are not implied to be adjacent. Suspicious URLs appear as inert code for exact matching.

Title, description and alternate target, lines 8–11:

```html
<title>DEWANAGA | Platform Centre of Edukasi Slot Paling Hoki Hari Ini</title>
<meta name="description" content="DEWANAGA adalah platform edukasi slot yang berkomitmen untuk memberikan permainan berkualitas tinggi secara berkelanjutan. Dengan menyediakan ini player dapat bermain dengan aman, nyaman, dan hoki." />
<meta name="verify-admitad" content="c032480529" />
<link rel="amphtml" href="https://commit.dinassosial.online/" />
```

Selected metadata at lines 16, 19, 22, 26, 31–33:

```html
<link rel="canonical" href="https://commit.org.in/" />
<link rel="alternate" hreflang="id" href="https://commit.dinassosial.online/" />
<link rel="alternate" hreflang="id-id" href="https://commit.dinassosial.online/" />
<meta name="robots" content="index, follow">
<meta property="og:site_name" content="DEWANAGA" />
<meta property="og:title" content="DEWANAGA | Platform Centre of Edukasi Slot Paling Hoki Hari Ini" />
<meta property="og:url" content="https://commit.org.in/" />
```

Login/registration links, lines 1891–1892 (leading indentation omitted):

```html
<a class="auth-cta-button" href="https://commit.dinassosial.online/"><span>DAFTAR DEWANAGA</span></a>
<a class="auth-cta-button" href="https://commit.dinassosial.online/"><span>LOGIN DEWANAGA</span></a>
```

The first sentence at line 2392:

> DEWANAGA kembali hadir sebagai situs edukasi, sekaligus merangkul player bermain dengan kualitas terbaik yang didukung oleh staff COMM-IT Career Academy.

The staff-support phrase is an unverified claim in the source. This excerpt is not evidence that staff authorised or participated in the promotion.

Hidden links, lines 3447–3448 (leading indentation omitted):

```html
<li class="display:none" style="display:none"><a href="//yonkerschamber.com/the-city-of-yonkers/">slot</a></li>
<li class="display:none" style="display:none"><a href="//locations.alfred.delivery/">slot mahjong</a></li>
```

Claimed credit at line 2625:

```text
CREATED BY :SEOMUKSEP X DEWANAGA.
```

This credit is a matching string, not verified attribution. Marketplace-style source remnants include `twitter:domain` set to `bonanza.com` at line 55 and a `BONZ` object with `cookie_domain: '.bonanza.com'` at lines 66–67. Those remnants do not attribute the unwanted content to Bonanza.

Selected response headers ([full file](captures/initial/live-root.headers.txt)):

```text
Date: Mon, 09 Nov 2026 18:16:23 GMT
Content-Type: text/html; charset=utf-8
Server: cloudflare
last-modified: Thu, 11 Jun 2026 10:37:27 GMT
cf-cache-status: HIT
```

Status 200 is recorded in [`live-root.metadata.json`](captures/initial/live-root.metadata.json). `Last-Modified` is not a reliable compromise timestamp.

## E2 — live `/home.html`: academy identity and contact

Source: [`live-home.body.txt`](captures/initial/live-home.body.txt).

Selected lines 12, 14, and 97–99, with leading indentation omitted:

```html
COMM-IT Career Academy : Best collages in Delhi, BBA, BCA
<link rel="canonical" href="https://commit.org.in/home.html" />
<p class="ACE">COMM-IT Career Academy</p>
<span class="Ivs-Text">(A unit of Awadh Centre of Education)</span>
<p class="GGS">Affiliated to GGS Indraprastha University and Approved By <br/>Govt. Of NCT of Delhi </p>
```

The header publishes `+91-9717807222` at line 59. The email at line 55 is Cloudflare-obfuscated with `data-cfemail="f39a9d959cb3928492979bdd9c8194dd9a9d"`. XORing each subsequent byte with the first byte (`f3`) yields `info@awadh.org.in`. This is decoding a public contact address, not decrypting protected institutional data. The footer contains the same address using another key at line 1647.

The identity text is evidence of what the page says. It does not establish that the entire application is secure or that the current deployment is institution-controlled.

## E3 — contact corroboration on Awadh's website

Source: [`contact-awadh.body.txt`](captures/initial/contact-awadh.body.txt).

Selected header lines 187 and 192, leading indentation omitted:

```html
<span class="elementor-icon-list-text"> info@awadh.org.in</span>
<span class="elementor-icon-list-text"> +91-9717807222</span>
```

The footer repeats the phone at line 2198 and email at line 2202. This provides a plausible administrative reporting route across two separately retrieved pages; no acknowledgement, mailbox validation, or dedicated security-contact status is implied.

## E4 — existing archive index

Source: [`archive-index.body.txt`](captures/initial/archive-index.body.txt).

The query uses exact-root matching, HTML/200 filters, a monthly timestamp collapse, years 2025–2026 and a 24-row limit. It returns 20 data rows, including these selected rows:

```json
["in,org,commit)/","20260301003129","http://commit.org.in/","text/html","200","JXXZJE3A3NSGAIQHUBRLE47BZMRU2K4K","12762"]
["in,org,commit)/","20260607162729","https://commit.org.in/","text/html","200","RGIZ5PIHZL2C5PUJUG7GUBD4D3PGZARR","14994"]
["in,org,commit)/","20260712142622","https://commit.org.in/","text/html","200","OPXEDDRBTNHZWDQOF4XGQBW3K36BE57J","33727"]
["in,org,commit)/","20261002002240","https://commit.org.in/","text/html","200","ORWWKBGXPZNURPQIZEVER74WLFPJ2LJN","29465"]
```

The CDX digest field is an archive-provided digest, not the local SHA-256 recorded above. CDX length is not the saved response body's byte count. Changed digests do not, by themselves, identify malicious changes; the corresponding bodies must be inspected. The monthly collapse is a sampling choice, not a complete inventory.

## E5 and E6 — historical academy content at the root

- **E5:** [`archive-20260301.body.txt`](captures/initial/archive-20260301.body.txt), title at line 14, academy name at line 123.
- **E6:** [`archive-20260607.body.txt`](captures/initial/archive-20260607.body.txt), title at line 12, academy name at line 97.

Both title lines contain exactly:

```text
COMM-IT Career Academy : Best collages in Delhi, BBA, BCA
```

E6 line 14 also contains:

```html
<link rel="canonical" href="https://commit.org.in" />
```

Replay headers identify the selected captures:

```text
E5: memento-datetime: Sun, 01 Mar 2026 00:31:29 GMT
E6: memento-datetime: Sun, 07 Jun 2026 16:27:29 GMT
```

E5's original scheme is HTTP; E6's is HTTPS, matching the scheme of the later gambling captures. These are observations of academy content, not comprehensive clean-site assessments. E5's archived origin headers mention Microsoft-IIS/10.0 and ASP.NET; no current server-version conclusion follows from them.

## E7 and E8 — historical gambling content at the root

- **E7:** [`archive-20261002.body.txt`](captures/initial/archive-20261002.body.txt).
- **E8:** [`archive-20260712.body.txt`](captures/history-july/archive-20260712.body.txt).

Both contain the same title at line 8, external `amphtml` destination at line 11, login/registration links at lines 1891–1892, institutional-support claim at line 2392, credit at line 2625, and hidden links at lines 3447–3448 quoted from E1 above. Full bodies differ in hash; no byte-for-byte identity is claimed.

Their replay headers state:

```text
E7: memento-datetime: Fri, 02 Oct 2026 00:22:40 GMT
E8: memento-datetime: Sun, 12 Jul 2026 14:26:22 GMT
```

This supports the presence of the key promotional indicators on those dates. It does not show continuous delivery between dates, the first modification, or a particular attacker. Headers added by the archive, including its own CSP and cookies, are not the original site's response policy. Origin-header copies are specifically prefixed `x-archive-orig-`.

## Verification and preservation notes

### Supplemental visual evidence

The [screenshot gallery](screenshots.md) adds S1–S3, captured from two fresh HTTP 200 document responses at 18:48:24–18:48:29 UTC on 9 November 2026. The screenshots show a restricted-browser rendering with page JavaScript disabled. Their separate [browser bundle](captures/browser-initial/) preserves PNGs, response bodies and headers, capture metadata, a request log and a SHA-256 manifest. They are not reconstructed images or historical archive screenshots. The browser root-response body matches E1's recorded SHA-256.

Run the offline scripts documented in [`README.md`](README.md). A subsequent live response may change through legitimate editing, cache behaviour, dynamic email obfuscation or response instrumentation. Keep new captures in new directories, and assess content alongside hashes.

Original header files contain anonymous archive routing cookies and network metadata. Retain these originals privately. If a public edition removes unnecessary fields or personal details, produce separately labelled derivatives and record their own hashes; do not silently alter the originals and continue quoting these hashes.
