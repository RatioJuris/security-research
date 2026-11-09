# Re-downloads every archived evidence file from the Internet Archive and checks its SHA-256.
# Usage: pwsh ./verify.ps1   (or: powershell -ExecutionPolicy Bypass -File verify.ps1)
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
New-Item -ItemType Directory -Force -Path downloads | Out-Null

$failed = $false
foreach ($row in Import-Csv evidence.csv) {
    $target = Join-Path downloads $row.file
    Invoke-WebRequest -UseBasicParsing -OutFile $target `
        -Uri "https://web.archive.org/web/$($row.capture)id_/$($row.original_url)"
    $actual = (Get-FileHash -Algorithm SHA256 $target).Hash.ToLowerInvariant()
    if ($actual -eq $row.sha256) {
        Write-Host "OK    $($row.id)  $($row.file)"
    } else {
        Write-Host "FAIL  $($row.id)  $($row.file)  (got $actual)" -ForegroundColor Red
        $failed = $true
    }
}

if ($failed) { exit 1 }
