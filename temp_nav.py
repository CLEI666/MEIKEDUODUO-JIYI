# -*- coding: utf-8 -*-
import websocket
import json
import time

try:
    # Get tabs
    import urllib.request
    tabs = json.loads(urllib.request.urlopen('http://localhost:9223/json').read())
    target = [t for t in tabs if t['title'] == u'\u65b0\u5efa\u6807\u7b7e\u9875' and t['url'] == 'edge://newtab/'][0]
    ws_url = target['webSocketDebuggerUrl']
    
    ws = websocket.create_connection(ws_url)
    
    # Navigate
    ws.send(json.dumps({'id': 2, 'method': 'Page.navigate', 'params': {'url': 'https://www.mercadolibre.com.mx/mas-vendidos'}}))
    time.sleep(6)
    
    # Get page content
    ws.send(json.dumps({'id': 3, 'method': 'Runtime.evaluate', 'params': {'expression': 'document.title + "|||" + document.body.innerText.substring(0,8000)'}}))
    result = ws.recv()
    data = json.loads(result)
    if 'result' in data and 'resultValue' in data['result']:
        text = data['result']['resultValue']['value']
        parts = text.split('|||')
        print('TITLE:', parts[0])
        print('CONTENT:', parts[1][:5000] if len(parts) > 1 else 'no content')
    elif 'result' in data:
        print('Result:', str(data['result'])[:500])
    
    ws.close()
except Exception as e:
    print('Error: ' + str(e))
