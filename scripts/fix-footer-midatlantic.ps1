$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$b = [char]0x2022
$oldMid = "Mid-Atlantic Hub $b Northeast Corridor $b Lakeshore Metro"
$newMid = "Quality childcare solutions tailored to your family's needs"
$utf8NoBom = New-Object System.Text.UTF8Encoding $false
$cityPattern = '(?s)(<p class="mx-auto mt-3 max-w-4xl text-center text-xs leading-relaxed text-nn-body sm:text-sm">\s*)Alexandria.*?</p>'
$cityReplace = '$1Nanny Placement ' + $b + ' On Call / Hotel Babysitters ' + $b + ' Newborn Care Specialist NCS ' + $b + ' Personal Assistant Services</p>'

Get-ChildItem -Path $root -Recurse -Filter "*.html" -File | ForEach-Object {
  $t = [System.IO.File]::ReadAllText($_.FullName)
  $o = $t
  $t = $t.Replace($oldMid, $newMid)
  $t = $t -replace $cityPattern, $cityReplace
  if ($t -ne $o) {
    [System.IO.File]::WriteAllText($_.FullName, $t, $utf8NoBom)
  }
}
Write-Host "Footer mid-Atlantic / city list fix complete."
