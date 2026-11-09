# Evidence register: AIIMS Delhi third-party JavaScript ad injection

Every item below is an Internet Archive capture, fetched in raw form (the `id_` URL returns the bytes exactly as originally archived, without the Wayback toolbar).
Each file's SHA-256 hash was computed and **re-verified on 9 November 2026**. Anyone can repeat the check with [`verify.sh`](verify.sh) or [`verify.ps1`](verify.ps1).

The relevant parts of each file are quoted below, so the findings can be read and checked here, even where archive.org is unavailable.

| ID | Capture (UTC) | Original URL | Bytes | SHA-256 |
|---|---|---|---:|---|
| E1 | 2022-12-20 14:28:57 | `counter.websiteout.net/js/30/10/22368976/0` | 2,728 | `a098293a97b6d02250cc315382a385593ee99335baa682b2022f72e932cf4069` |
| E2 | 2022-11-25 07:45:11 | `counter.websiteout.net/js/30/10/22368976/0` | 221 | `e8806ccf19a17f9e7b78b4e59820a9dcc6ebf6ac7e86eb3d11f66a5e37d9e3e1` |
| E3 | 2022-12-28 11:41:26 | `counter.websiteout.net/close-firstchild.js` | 963 | `80c372bf5391596d9fb3a4bd1f7f96649323b32c334f79d1c096f5218b445cb9` |
| E4 | 2023-01-01 05:40:16 | `websiteout.net/ads.txt` | 59 | `6a6b4e8f7baebf2e50a3ab3b7cbd512d50bf4010d5ffa85a9f6d38ca3f90fbee` |
| E5 | 2023-01-12 05:44:27 | `www.aiims.edu/en.html` | 219,640 | `6c996ac405eafb6fc3a2d4ba89a14940b1c9e13c2cd94fc87de69f9f0349cce0` |
| E6 | 2023-01-27 06:58:21 | `www.aiims.edu/en.html` | 236,631 | `c812d7035998ac3877abb447b59c7c73896e96790f6dba38715bfbc07ac376f1` |

Machine-readable copy: [`evidence.csv`](evidence.csv) · Hash manifest: [`SHA256SUMS`](SHA256SUMS)

---

## E5: the counter embedded in the AIIMS Delhi footer

[Archived page](https://web.archive.org/web/20230112054427/https://www.aiims.edu/en.html), excerpt from the footer:

```html
<div style="float:left; margin-right:5px;">You are Visitor No. &nbsp;&nbsp;<div style="float:right;">
<script type="text/javascript" src="//counter.websiteout.net/js/30/10/22368976/0"></script></div>
```

## E6: the counter removed

[Archived page](https://web.archive.org/web/20230127065821/https://www.aiims.edu/en.html). The string `websiteout` does not appear anywhere in this 236,631-byte capture.

## E2: the counter-only version (221 bytes, complete file)

[Archived script](https://web.archive.org/web/20221125074511/https://counter.websiteout.net/js/30/10/22368976/0):

```js
document.write('<a href="https://www.websiteout.net/counter.php"><img src="//counter.websiteout.net/compte.php?S='+encodeURI(window.location.hostname)+'&C=30&D=10&N=22368976&M=0" alt="web hit counter" border="0" /></a>');
```

## E1: the ad-inserting version (2,728 bytes)

[Archived script](https://web.archive.org/web/20221220142857/https://counter.websiteout.net/js/30/10/22368976/0). It starts with the same counter line as E2, then continues. Excerpt, verbatim, with helper functions and two hostname-specific lines omitted (`…`):

```js
…
window.onload=null;
doc=window.document;
xx=doc.getElementsByTagName("iframe");
if (xx.length) xx[0].parentNode.removeChild(xx[0]);
removeByClassName("header-ads");
…
removeByClassName("adsbygoogle");
removeByClassName("notice"); removeByClassName("notice-overlay");
…
doc.write('<'+'div id="ChromeBrowser" '+'style="position:fixed;top:0px;left:0px;width:750px;overflow:visible;z-index:2147483644;"'+'>');
google_ad_client = "ca-pub-5486891678306037"; google_ad_slot = "9781413410"; google_ad_width = 728; google_ad_height = 90;
doc.write('<' + 'script');doc.write(' language="javascript"');doc.write(' type="text/javascript"');doc.write(' src="//pagead2.googlesyndication.com/pagead/show_ads.js">');doc.write('</' + 'script' + '>');
…
doc.write('<');doc.write('script language="javascript"');doc.write(' type="text/javascript"');doc.write(' src="//counter.websiteout.net/close-firstchild.js"'+'>');document.write('</' + 'script' + '>');
```

What this code does to the host page: it cancels the page's `window.onload` handler, removes the first `iframe`, removes elements with ad and notice classes, then writes a fixed-position container at the top-left with a near-maximum `z-index`, and loads a 728×90 Google AdSense unit for publisher `ca-pub-5486891678306037`.

## E3: moving the ad to the top of the page

[Archived script](https://web.archive.org/web/20221228114126/https://counter.websiteout.net/close-firstchild.js), the active lines:

```js
document.write("<" + "/" + "div" + ">");
xx=document.getElementById("ChromeBrowser");
document.body.insertBefore(document.getElementById("ChromeBrowser"), document.body.firstChild);
setTimeout("…insertBefore(xx, …body…firstChild);…removeByClassName('expand');…", 1000);
```

## E4: the advertising account belongs to the counter operator

[Archived ads.txt](https://web.archive.org/web/20230101054016/https://websiteout.net/ads.txt), complete file:

```text
google.com, pub-5486891678306037, DIRECT, f08c47fec0942fa0
```

The publisher ID matches the one in E1. This indicates that the advertising was configured by the counter operator, not by AIIMS.

## Additional archive observations

- The Internet Archive holds 110 captures of the counter URL from 2022. Large (ad-inserting) and 221-byte (counter-only) responses alternate throughout the year. The earliest large capture in 2022 is from 2 March 2022.
- The capture of 28 November 2022 (`20221128191953`) names the container `ggoggo`. By 20 December 2022 (E1) it is `ChromeBrowser`.
- Capture index: [CDX query](https://web.archive.org/cdx/search/cdx?url=counter.websiteout.net/js/30/10/22368976/0&from=2022&to=2022).
