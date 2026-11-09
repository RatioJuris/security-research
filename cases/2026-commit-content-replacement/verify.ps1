param(
    [string]$CaptureDirectory = (Join-Path $PSScriptRoot 'captures/initial')
)

# Offline verification only. No live responses are re-downloaded.
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath $CaptureDirectory).Path
$manifest = Join-Path $root 'SHA256SUMS'
$count = 0
foreach ($line in Get-Content -LiteralPath $manifest) {
    if ($line -notmatch '^([0-9a-f]{64})  ([A-Za-z0-9][A-Za-z0-9._-]*)$') {
        throw "Invalid manifest line: $line"
    }
    $expected = $Matches[1]
    $name = $Matches[2]
    $actual = (Get-FileHash -LiteralPath (Join-Path $root $name) -Algorithm SHA256).Hash
    if ($actual.ToLowerInvariant() -ne $expected) {
        throw "SHA-256 mismatch: $name"
    }
    Write-Output "OK $name"
    $count++
}
if ($count -eq 0) { throw 'Manifest is empty.' }
Write-Output "Verified $count saved files. This checks integrity, not provenance or capture time."
