$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$distRoot = Join-Path $repoRoot 'dist'
$releaseRoot = Join-Path $distRoot 'aj-printers'
$documentsTarget = Join-Path $releaseRoot 'pliki\dokumenty'
$reportsTarget = Join-Path $releaseRoot 'pliki\protokoly-szkody'
$zipPath = Join-Path $distRoot 'aj-printers-wdrozenie.zip'

if (Test-Path $releaseRoot) {
    Remove-Item -LiteralPath $releaseRoot -Recurse -Force
}

New-Item -ItemType Directory -Force -Path $documentsTarget, $reportsTarget | Out-Null
Copy-Item -Path (Join-Path $repoRoot 'public\documents\*') -Destination $documentsTarget
Copy-Item -Path (Join-Path $repoRoot 'public\damage-reports\*') -Destination $reportsTarget

if (Test-Path $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
}

Compress-Archive -Path (Join-Path $releaseRoot '*') -DestinationPath $zipPath
Write-Host "Utworzono paczke: $zipPath" -ForegroundColor Green
