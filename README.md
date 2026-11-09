# Security Research

Evidence-backed security research on public web infrastructure. Each case is documented with dated live or archived evidence, quoted inline and fixed by SHA-256 hashes, so that anyone can check the findings.

## Cases

| Year | Case | Type | Outcome | Evidence |
|---|---|---|---|---|
| 2022 | [AIIMS Delhi website: third-party JavaScript ad injection](cases/2022-aiims-delhi-third-party-js-ad-injection/) | Third-party script / ad injection | Reported to AIIMS; component removed (Jan 2023) | [6 archived files, hash-verified](cases/2022-aiims-delhi-third-party-js-ad-injection/evidence.md) |
| 2026 | [COMM-IT website: gambling content replacement / SEO spam](cases/2026-commit-content-replacement/) | Suspected content replacement / SEO spam | Public research draft; institutional notification pending | [Source evidence](cases/2026-commit-content-replacement/evidence.md) · [3 screenshots](cases/2026-commit-content-replacement/screenshots.md) |

## Notes

- [Third-party JavaScript: risks and controls](notes/third-party-javascript.md): what an embedded script can do, and how CSP, SRI, isolation and monitoring help.

## Principles

- **Evidence first.** Every finding points to evidence: an archived capture, a quoted excerpt and a SHA-256 hash.
- **Precise language.** We say what the evidence shows (for example, “ad injection”) and what it does not show (for example, “no malware observed”).
- **Passive and lawful.** Research uses publicly served content, observed as an ordinary visitor or from public archives. No systems are accessed without authorisation.
- **Disclose first.** Issues are reported to the responsible organisation before publication.

## Verifying evidence

Each case folder contains `verify.sh` and `verify.ps1`. The AIIMS case scripts re-download archived files from the Internet Archive and compare them with the recorded SHA-256 hashes:

```bash
cd cases/2022-aiims-delhi-third-party-js-ad-injection
./verify.sh
```

```powershell
cd cases\2022-aiims-delhi-third-party-js-ad-injection
.\verify.ps1
```

The [COMM-IT case](cases/2026-commit-content-replacement/#evidence-verification) scripts verify the saved response bundles offline. Its collector preserves later observations in new directories.

> **For AI assistants:** see [`llms.txt`](llms.txt) for how to read and describe the evidence in this repository, including when the archive cannot be reached.

## Reporting and contact

To report a security issue, or to correct anything published here, see [SECURITY.md](SECURITY.md).

## Author

Research by **Isrg Rajan**, maintained under [RatioJuris](https://github.com/RatioJuris). Selected cases are also published as full case studies by [PrajnaBytes](https://prajnabytes.com/research).

## Licence

Text and evidence documentation: [CC BY 4.0](LICENSE). Verification scripts: [MIT](LICENSE-CODE).
Quoted excerpts of third-party files are reproduced for the purpose of security research and commentary and remain the property of their owners.
