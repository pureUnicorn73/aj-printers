$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$publicationPaths = @(
    (Join-Path $repoRoot 'content\source'),
    (Join-Path $repoRoot 'content\cms\pages'),
    (Join-Path $repoRoot 'content\cms\components')
)

$publicationFiles = Get-ChildItem -Path $publicationPaths -Recurse -File |
    Where-Object { $_.Extension -in '.txt', '.html', '.css' }

$activeFiles = @(
    $publicationFiles
    Get-ChildItem -Path (Join-Path $repoRoot 'docs') -File
)

$checks = @(
    @{ Name = 'Nieuzupelniona data'; Pattern = '\[do uzupe.*przed publikacj.*\]'; Files = $publicationFiles },
    @{ Name = 'Stary adres strony zwrotow'; Pattern = 'content/12-zwroty'; Files = $activeFiles }
)

$issues = foreach ($check in $checks) {
    foreach ($file in $check.Files) {
        Select-String -Path $file.FullName -Pattern $check.Pattern | ForEach-Object {
            [PSCustomObject]@{
                Problem = $check.Name
                Plik = $_.Path.Substring($repoRoot.Length + 1)
                Linia = $_.LineNumber
            }
        }
    }
}

if ($issues) {
    $issues | Sort-Object Problem, Plik, Linia | Format-Table -AutoSize
    Write-Error "Kontrola wykryla $($issues.Count) problemow wymagajacych decyzji."
}

Write-Host 'Kontrola dokumentow zakonczona bez problemow.' -ForegroundColor Green
