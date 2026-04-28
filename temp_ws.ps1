[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$ws = New-Object System.Net.WebSockets.ClientWebSocket
$ct = [Threading.CancellationToken]::None
$ws.ConnectAsync((Invoke-RestMethod 'http://localhost:9210/json' -TimeoutSec 5 | Where-Object { $_.title -eq 'data' } | ForEach-Object { $_.webSocketDebuggerUrl }), $ct).Wait()
if ($ws.State -eq 'Open') {
    '{"id":1,"method":"Target.getTargets"}' | ForEach-Object { $bytes = [System.Text.Encoding]::UTF8.GetBytes($_); $ws.SendAsync([ArraySegment[byte]]$bytes, 'Text', $true, $ct).Wait() }
    $buf = New-Object byte[] 32768
    $received = $ws.ReceiveAsync([ArraySegment[byte]]$buf, $ct)
    if ($received.Wait(5000)) {
        $json = [System.Text.Encoding]::UTF8.GetString($buf,0,$received.Result.Count)
        Write-Host $json
    }
    $ws.CloseAsync('NormalClosure', '', $ct).Wait()
} else {
    Write-Host "WS not open: $($ws.State)"
}
