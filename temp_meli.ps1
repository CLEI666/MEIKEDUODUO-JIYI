# -*- coding: utf-8 -*-
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$client = New-Object System.Net.WebClient
$client.Encoding = [System.Text.Encoding]::UTF8
$client.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
$client.Headers.Add("Accept", "application/json")
$client.Headers.Add("Accept-Language", "es-MX,es;q=0.9")
$client.Headers.Add("Referer", "https://www.mercadolibre.com.mx")
try {
    # Try trending searches API
    $resp = $client.DownloadString('https://ml.damaishuju.com/')
    Write-Host "Got response from damaishuju"
    Write-Host ($resp | Select-Object -First 500)
} catch {
    Write-Host "Error: $_"
}

try {
    # Try MercadoLibre API - trending searches
    $resp2 = $client.DownloadString('https://api.mercadolibre.com/trends/MLM')
    $resp2 | ConvertFrom-Json | ForEach-Object { $_.query + " - " + $_.name } | Select-Object -First 20
} catch {
    Write-Host "API Error: $_"
}
