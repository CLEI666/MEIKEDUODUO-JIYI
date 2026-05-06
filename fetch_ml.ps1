$r = Invoke-WebRequest -Uri 'https://www.mercadolibre.com.mx/mas-vendidos' -Method GET -UserAgent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' -TimeoutSec 15
$r.Content | Out-File -FilePath 'C:\root\.openclaw\workspaces\mercadolibre\mercadolibre_home.txt' -Encoding UTF8
'done'