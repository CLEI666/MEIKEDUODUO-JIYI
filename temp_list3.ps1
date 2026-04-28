[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
try {
    $req = [System.Net.HttpWebRequest]::Create('http://localhost:9210/json')
    $req.Timeout = 5000
    $resp = $req.GetResponse()
    $stream = $resp.GetResponseStream()
    $reader = New-Object System.IO.StreamReader($stream, [System.Text.Encoding]::UTF8)
    $content = $reader.ReadToEnd()
    $reader.Close()
    $resp.Close()
    $json = $content | ConvertFrom-Json
    $json | ForEach-Object { Write-Host ($_.id + " | " + $_.title + " | " + $_.url + " | " + $_.webSocketDebuggerUrl) }
} catch {
    Write-Host "Error: $_"
}
