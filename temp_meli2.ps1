[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$client = New-Object System.Net.WebClient
$client.Encoding = [System.Text.Encoding]::UTF8
$client.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
$client.Headers.Add("Accept", "application/json")
$client.Headers.Add("Accept-Language", "es-MX,es;q=0.9")
$client.Headers.Add("Referer", "https://www.mercadolibre.com.mx")

# Try MLM search API (public endpoint)
try {
    $resp = $client.DownloadString('https://api.mercadolibre.com/sites/MLM/search?q=audifonos&limit=10&offset=0')
    $json = $resp | ConvertFrom-Json
    Write-Host "Results for audifonos:"
    $json.results | ForEach-Object { Write-Host ($_.id + " - " + $_.title + " - $" + $_.price) }
} catch {
    Write-Host "Search Error: $_"
}

# Try categories
try {
    $resp2 = $client.DownloadString('https://api.mercadolibre.com/sites/MLM')
    $json2 = $resp2 | ConvertFrom-Json
    Write-Host "Site info:"
    Write-Host ($json2 | ConvertTo-Json -Depth 3)
} catch {
    Write-Host "Site Error: $_"
}
