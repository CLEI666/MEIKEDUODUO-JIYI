[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
# Navigate via CDP
$ws = New-Object System.Net.WebSockets.ClientWebSocket
$ct = [Threading.CancellationToken]::None
$tabs = Invoke-RestMethod 'http://localhost:9223/json' -TimeoutSec 5
$targetTab = $tabs | Where-Object { $_.title -eq '新建标签页' -and $_.url -eq 'edge://newtab/' } | Select-Object -First 1
$wsUrl = $targetTab.webSocketDebuggerUrl
$ws.ConnectAsync($wsUrl, $ct).Wait()

# Navigate to MercadoLibre mas-vendidos
$navCmd = '{"id":2,"method":"Page.navigate","params":{"url":"https://www.mercadolibre.com.mx/mas-vendidos"}}'
$bytes = [System.Text.Encoding]::UTF8.GetBytes($navCmd)
$ws.SendAsync([ArraySegment[byte]]$bytes, 'Text', $true, $ct).Wait()
Start-Sleep 5

# Get page content
$getCmd = '{"id":3,"method":"Runtime.evaluate","params":{"expression":"document.title + \"|\" + document.body.innerText.substring(0,5000)"}}'
$bytes = [System.Text.Encoding]::UTF8.GetBytes($getCmd)
$ws.SendAsync([ArraySegment[byte]]$bytes, 'Text', $true, $ct).Wait()
$buf = New-Object byte[] 65536
$received = $ws.ReceiveAsync([ArraySegment[byte]]$buf, $ct)
if ($received.Wait(8000)) {
    $result = [System.Text.Encoding]::UTF8.GetString($buf,0,$received.Result.Count)
    $parsed = $result | ConvertFrom-Json
    if ($parsed.result.resultValue) {
        Write-Host $parsed.result.resultValue.value
    }
}
$ws.CloseAsync('NormalClosure', '', $ct).Wait()
