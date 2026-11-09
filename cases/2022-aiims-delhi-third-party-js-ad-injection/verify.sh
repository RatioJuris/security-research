#!/usr/bin/env bash
# Re-downloads every archived evidence file from the Internet Archive and checks its SHA-256.
# Usage: ./verify.sh            (needs curl and sha256sum)
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p downloads

fail=0
while IFS=, read -r id file capture url bytes sha256 _; do
  [ "$id" = "id" ] && continue
  curl -sSfL --retry 3 "https://web.archive.org/web/${capture}id_/${url}" -o "downloads/${file}"
  actual=$(sha256sum "downloads/${file}" | cut -d' ' -f1)
  if [ "$actual" = "$sha256" ]; then
    echo "OK    $id  $file"
  else
    echo "FAIL  $id  $file  (got $actual)"
    fail=1
  fi
done < evidence.csv

exit $fail
