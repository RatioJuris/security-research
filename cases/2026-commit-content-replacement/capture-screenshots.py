"""Capture live pages with page JavaScript disabled and limited asset requests.

Requires Python 3.9+, Playwright and an installed Chromium-family browser.
Usage: python capture-screenshots.py <new-output-directory> <browser-executable>
Screenshots are unannotated browser output, accompanied by capture metadata.
"""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import sys
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


PAGES = [
    ("root", "https://commit.org.in/"),
    ("home", "https://commit.org.in/home.html"),
]
ASSET_HOSTS = {
    "commit.org.in", "assets.bonanza.com", "i.imgur.com",
    "fonts.googleapis.com", "fonts.gstatic.com",
}
ASSET_TYPES = {"image", "stylesheet", "font"}


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    output = Path(sys.argv[1])
    executable = Path(sys.argv[2])
    if not executable.is_file():
        raise SystemExit("Browser executable not found.")
    output.mkdir(parents=True, exist_ok=False)
    record = {
        "started_utc": utc_now(), "source": "live HTTPS pages",
        "javascript_enabled": False, "viewport": {"width": 1440, "height": 1000},
        "device_scale_factor": 1, "locale": "en-GB", "timezone": "UTC",
        "allowed_asset_hosts": sorted(ASSET_HOSTS),
        "allowed_asset_types": sorted(ASSET_TYPES),
        "navigation": "Only the two exact requested document URLs; no form submissions",
        "body_format": "Response.body() bytes after browser content decoding",
        "pages": [],
    }
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(
                executable_path=str(executable), headless=True,
                args=["--disable-background-networking", "--disable-component-update", "--disable-sync"],
            )
            record["browser_version"] = browser.version
            for name, url in PAGES:
                page_record = {"name": name, "requested_url": url, "started_utc": utc_now(), "requests": []}
                record["pages"].append(page_record)
                context = browser.new_context(
                    java_script_enabled=False, viewport=record["viewport"],
                    device_scale_factor=1, locale="en-GB", timezone_id="UTC",
                    service_workers="block", accept_downloads=False,
                )

                def route_request(route):
                    request = route.request
                    parsed = urlparse(request.url)
                    allowed = request.method == "GET" and parsed.scheme == "https" and (
                        (request.resource_type == "document" and request.url == url)
                        or (request.resource_type in ASSET_TYPES and parsed.hostname in ASSET_HOSTS)
                    )
                    page_record["requests"].append({
                        "url": request.url, "type": request.resource_type,
                        "method": request.method, "allowed": allowed,
                    })
                    if allowed:
                        route.continue_()
                    else:
                        route.abort()

                context.route("**/*", route_request)
                page = context.new_page()
                page.on("requestfailed", lambda request: page_record.setdefault("failed_requests", []).append({
                    "url": request.url, "failure": request.failure,
                }))
                try:
                    response = page.goto(url, wait_until="load", timeout=60000)
                    if response is None:
                        raise RuntimeError("Navigation returned no document response.")
                    page_record.update(
                        response_status=response.status, final_url=page.url,
                        title=page.title(), user_agent=page.evaluate("navigator.userAgent"),
                    )
                    (output / f"{name}.body.txt").write_bytes(response.body())
                    (output / f"{name}.headers.json").write_text(
                        json.dumps(response.all_headers(), indent=2) + "\n", encoding="utf-8"
                    )
                    if response.status != 200:
                        raise RuntimeError(f"Unexpected document HTTP status: {response.status}")
                    filename = f"{name}-viewport.png"
                    page.screenshot(path=str(output / filename), full_page=False, timeout=30000)
                    page_record["screenshots"] = [{"file": filename, "captured_utc": utc_now(), "view": "top of page"}]
                    if name == "root":
                        heading = page.get_by_role("heading", name="DEWANAGA | Platform Centre of Edukasi Slot Paling Hoki Hari Ini", exact=True).last
                        heading.scroll_into_view_if_needed(timeout=10000)
                        # Position the heading near the top; only automation runs this
                        # expression. Page-authored JavaScript remains disabled.
                        heading.evaluate("element => element.scrollIntoView({block: 'start'})")
                        filename = "root-promotion.png"
                        page.screenshot(path=str(output / filename), full_page=False, timeout=30000)
                        page_record["screenshots"].append({"file": filename, "captured_utc": utc_now(), "view": "promotional heading and text"})
                    print(f"{name}: HTTP {response.status}, {len(page_record['screenshots'])} screenshots", flush=True)
                except Exception as exc:
                    page_record["error"] = f"{type(exc).__name__}: {exc}"
                    print(f"{name}: {page_record['error']}", flush=True)
                finally:
                    page_record["finished_utc"] = utc_now()
                    context.close()
            browser.close()
    finally:
        record["finished_utc"] = utc_now()
        (output / "browser-capture.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        manifest = "".join(
            f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n"
            for path in sorted(output.iterdir()) if path.is_file()
        )
        (output / "SHA256SUMS").write_bytes(manifest.encode("ascii"))
    if any("error" in page for page in record["pages"]):
        raise SystemExit("Review capture metadata for errors.")


if __name__ == "__main__":
    main()
