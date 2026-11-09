# Third-party JavaScript: risks and controls

A `<script src="https://other-domain/…">` tag gives the other domain's operator the same power in the visitor's browser as the website's own code. This note sets out what that means in practice, and the controls that reduce the risk. It draws on the [AIIMS Delhi case](../cases/2022-aiims-delhi-third-party-js-ad-injection/), where a visitor counter inserted advertising into a national healthcare website.

## What an included script can do

| Capability | Example from the AIIMS case |
|---|---|
| Read and change any part of the page (DOM) | Removed the page's first `iframe` and elements with ad and notice classes |
| Override the page's own code | Set `window.onload = null`, cancelling the site's load handler |
| Add content that looks like part of the site | Placed a fixed-position advert above the institutional header |
| Load further scripts from anywhere | Loaded Google's ad script and a second helper script |
| Change at any time, without the site owner knowing | The same URL alternated between a 221-byte counter and a 2.7 KB ad-inserting version |

It could equally capture form input, show a fake login or payment form, or redirect visitors. The only limit is the operator's intent.

## Risk factors

- **Inherited trust:** browsers treat the script as the site's own code.
- **Mutable content:** approving a snippet once does not approve what the URL serves later.
- **Conditional serving:** responses can differ by visitor, time or location, so one-off reviews miss behaviour.
- **Scope creep:** a widget added for one purpose can gain unrelated behaviour.
- **Performance and reliability:** `document.write` blocks parsing and is discouraged by browsers.

## Controls

| Control | How it helps | Limits |
|---|---|---|
| **Inventory and review** | Record each external script with an owner, purpose, data access and review date. Remove what has no clear purpose. | A review captures one moment. |
| **Remove or replace** | Produce low-value features (counters, badges) first-party, for example visit counts from server logs. | Small internal effort. Usually the most effective option. |
| **Content Security Policy** | A `script-src` allowlist blocks scripts from unapproved domains. Violation reports raise alerts. | An allowed domain can still serve any code, including code that changes the page. |
| **Subresource Integrity** | `integrity="sha384-…"` makes the browser refuse a file that has changed. | Only practical for versioned, static files. A changing endpoint breaks (safely). |
| **Sandboxed iframe** | Loading the widget on a separate origin in `<iframe sandbox>` stops it from reaching the host page. | Unsuitable for widgets that must write into the page. |
| **Continuous monitoring** | Render key pages regularly; alert on new domains, new scripts or changed script hashes. | Needs repeated sampling, and someone to act on alerts. |
| **Disclosure channel** | Publish `/.well-known/security.txt` (RFC 9116) so outside reports reach the right team. | Speeds response; does not prevent issues. |

### Example: a CSP that would have blocked the second stage

```http
Content-Security-Policy: script-src 'self' https://counter.websiteout.net; report-to csp
```

This would have blocked `pagead2.googlesyndication.com` and reported the attempt. It would **not** have stopped the counter script itself from removing page elements. Only removing the script, or isolating it, does that.

### Example: Subresource Integrity

```html
<script src="https://cdn.example.com/lib-4.2.1.min.js"
        integrity="sha384-…"
        crossorigin="anonymous"></script>
```

## Checklist

- [ ] List every external script on every public page, with owner and purpose.
- [ ] Remove widgets that do not justify running third-party code.
- [ ] Self-host or pin versioned libraries with SRI.
- [ ] Deploy a CSP, starting in report-only mode.
- [ ] Monitor rendered pages for new domains and changed scripts.
- [ ] Publish `security.txt` and a way to report issues.

## References

- OWASP, [Third Party JavaScript Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html)
- OWASP, [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
- MDN, [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) and [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)
- W3C, [Subresource Integrity](https://www.w3.org/TR/SRI/)
- IETF, [RFC 9116: security.txt](https://www.rfc-editor.org/rfc/rfc9116)
- Chrome for Developers, [Uses document.write()](https://developer.chrome.com/docs/lighthouse/best-practices/no-document-write)
