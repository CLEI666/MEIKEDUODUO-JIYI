# -*- coding: utf-8 -*-
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$client = New-Object System.Net.WebClient
$client.Encoding = [System.Text.Encoding]::UTF8
$client.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
$client.Headers.Add("Accept", "application/json")
try {
    $resp = $client.DownloadString('https://api.mercadolibre.com/sites/MLM/categories')
    $resp | ConvertFrom-Json | ForEach-Object { $_.id + " - " + $_.name } | Select-Object -First 30
} catch {
    Write-Host "Error: $_"
}
