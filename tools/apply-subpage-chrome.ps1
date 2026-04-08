$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $root

$headerRaw = Get-Content (Join-Path $root "partials\header-subpage.html") -Raw
$header = ($headerRaw -replace '(?s)^<!--.*?-->\r?\n\r?', "").TrimEnd()

$footerRaw = Get-Content (Join-Path $root "partials\footer-subpage.html") -Raw
$footer = ($footerRaw -replace '(?s)^<!--.*?-->\r?\n\r?', "").TrimEnd()

$oldBody = 'class="bg-cream pb-24 font-sans text-ink antialiased lg:pb-20"'
$newBody = 'class="bg-nn-page pb-28 font-sans text-nn-body antialiased lg:pb-24"'

Get-ChildItem (Join-Path $root "pages\*.html") | ForEach-Object {
  $path = $_.FullName
  $c = Get-Content $path -Raw -Encoding UTF8

  if ($c -notmatch 'id="header-inner"') {
    $c = $c -replace '(?s)<header class="sticky top-0 z-50 border-b border-line bg-paper/95.*?</header>', $header
  }

  $c = $c -replace [regex]::Escape($oldBody), $newBody

  $c = $c -replace '(?s)\r?\n    <footer class="border-t border-stone-200 bg-sand pb-6 pt-14" id="site-footer">.*?\r?\n\r?\n    <script type="module"', "`r`n`r`n    $footer`r`n`r`n    <script type=`"module`""

  Set-Content -Path $path -Value $c -Encoding UTF8 -NoNewline
  Write-Host "Updated: $($_.Name)"
}
