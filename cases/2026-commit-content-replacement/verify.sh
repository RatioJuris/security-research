#!/usr/bin/env bash
# Offline verification only. Requires Bash and sha256sum.
set -euo pipefail
case_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
capture_dir="${1:-$case_dir/captures/initial}"
cd -- "$capture_dir"
test -s SHA256SUMS
# Windows-generated manifests may use CRLF; normalize only the manifest stream.
tr -d '\r' < SHA256SUMS | sha256sum -c -
printf '%s\n' 'Verified saved files. This checks integrity, not provenance or capture time.'
