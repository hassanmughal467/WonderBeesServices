$r = Invoke-WebRequest -Uri 'https://miraclenanniesandsitters.com/' -UseBasicParsing -TimeoutSec 30
$c = $r.Content
[regex]::Matches($c, 'href="([^"]+\.css[^"]*)"') | ForEach-Object { $_.Groups[1].Value } | Select-Object -First 30
[regex]::Matches($c, 'fonts\.googleapis\.com[^"]+') | ForEach-Object { $_.Value } | Select-Object -First 5
