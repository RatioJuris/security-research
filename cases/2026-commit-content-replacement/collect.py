"""Preserve a small, fixed set of public responses without running page content.

Usage: python collect.py captures/<new-run-name> [E1 E2 ...]
The destination must not exist. Redirects are recorded, not followed.
Python 3.9+; standard library only.
"""

import csv
import hashlib
import json
from pathlib import Path
import sys
from datetime import datetime, timezone
from urllib.error import HTTPError
from urllib.request import HTTPRedirectHandler, Request, build_opener


SOURCES = [
    ("E1", "live-root", "https://commit.org.in/"),
    ("E2", "live-home", "https://commit.org.in/home.html"),
    ("E3", "contact-awadh", "https://awadh.org.in/"),
    ("E4", "archive-index", "https://web.archive.org/cdx/search/cdx?url=commit.org.in%2F&matchType=exact&output=json&filter=statuscode%3A200&filter=mimetype%3Atext%2Fhtml&collapse=timestamp%3A6&from=2025&to=2026&limit=24"),
    ("E5", "archive-20260301", "https://web.archive.org/web/20260301003129id_/http://commit.org.in/"),
    ("E6", "archive-20260607", "https://web.archive.org/web/20260607162729id_/https://commit.org.in/"),
    ("E7", "archive-20261002", "https://web.archive.org/web/20261002002240id_/https://commit.org.in/"),
    ("E8", "archive-20260712", "https://web.archive.org/web/20260712142622id_/https://commit.org.in/"),
]
HEADERS = {
    "User-Agent": "RatioJuris-PublicEvidence/1.0 (passive HTML collection)",
    "Accept": "text/html,application/json,text/plain;q=0.9,*/*;q=0.1",
    "Accept-Encoding": "identity",
}
MAX_BYTES = 5 * 1024 * 1024


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python collect.py captures/<new-run-name> [E1 E2 ...]")
    selected = set(sys.argv[2:]) or {source[0] for source in SOURCES}
    unknown = selected - {source[0] for source in SOURCES}
    if unknown:
        raise SystemExit(f"Unknown evidence IDs: {sorted(unknown)}")
    output = Path(sys.argv[1])
    output.mkdir(parents=True, exist_ok=False)
    opener = build_opener(NoRedirect())
    rows = []
    for evidence_id, name, url in SOURCES:
        if evidence_id not in selected:
            continue
        record = {
            "id": evidence_id, "name": name, "requested_url": url,
            "started_utc": utc_now(), "request_headers": HEADERS,
            "method": "GET", "redirects_followed": False,
            "collector": "Python urllib; TLS verification enabled; no browser execution",
            "header_format": "Parsed response headers serialized as text; not wire bytes",
        }
        try:
            try:
                response = opener.open(Request(url, headers=HEADERS), timeout=35)
            except HTTPError as exc:
                response = exc
            with response:
                body = response.read(MAX_BYTES + 1)
                record.update(status=response.status, response_url=response.geturl())
                record["body_truncated"] = len(body) > MAX_BYTES
                body = body[:MAX_BYTES]
                body_name = f"{name}.body.txt"
                header_name = f"{name}.headers.txt"
                (output / body_name).write_bytes(body)
                (output / header_name).write_bytes(str(response.headers).encode("utf-8"))
                record.update(
                    body_file=body_name, headers_file=header_name, body_bytes=len(body),
                    body_sha256=hashlib.sha256(body).hexdigest(),
                    content_type=response.headers.get("Content-Type"),
                    content_encoding=response.headers.get("Content-Encoding"),
                    response_date=response.headers.get("Date"),
                )
        except Exception as exc:
            record["error"] = f"{type(exc).__name__}: {exc}"
        record["finished_utc"] = utc_now()
        (output / f"{name}.metadata.json").write_text(
            json.dumps(record, indent=2) + "\n", encoding="utf-8"
        )
        rows.append({key: record.get(key, "") for key in (
            "id", "name", "requested_url", "started_utc", "finished_utc", "status",
            "body_file", "body_bytes", "body_sha256", "body_truncated", "error"
        )})
        print(f"{evidence_id}: HTTP {record.get('status', '-')} "
              f"{record.get('body_bytes', 0)} bytes {record.get('error', '')}", flush=True)

    with (output / "evidence.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    manifest = "".join(
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n"
        for path in sorted(output.iterdir()) if path.is_file()
    )
    (output / "SHA256SUMS").write_bytes(manifest.encode("ascii"))
    if any(row["error"] or row["status"] != 200 or row["body_truncated"] for row in rows):
        raise SystemExit("Some responses need review; consult saved metadata.")


if __name__ == "__main__":
    main()
