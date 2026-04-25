import urllib.request, re, json

# Try the search API endpoint
url = 'https://www.mercadolibre.com.mx/jmml/search?q=samsung+m33+charger&siteId=MLM&cat=MLM'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json',
    'Accept-Language': 'es-MX,es;q=0.9',
    'Referer': 'https://www.mercadolibre.com.mx/'
}
try:
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=10)
    print('Status:', resp.status)
    data = resp.read().decode('utf-8', errors='ignore')
    print('Length:', len(data))
    if data.startswith('{'):
        j = json.loads(data)
        results = j.get('results', j.get('data', []))[:3]
        for r in results:
            print('Title:', r.get('title', '')[:60])
            print('Price:', r.get('price'))
            print('Thumbnail:', r.get('thumbnail', '')[:80])
            print('---')
    else:
        print(data[:500])
except Exception as e:
    print('Error:', str(e)[:200])

# Also try mercado libre api
url2 = 'https://api.mercadolibre.com/sites/MLM/search?q=samsung+m33+charger&limit=3'
headers2 = {
    'User-Agent': 'Mozilla/5.0',
    'Accept': 'application/json'
}
try:
    req2 = urllib.request.Request(url2, headers=headers2)
    resp2 = urllib.request.urlopen(req2, timeout=10)
    print('\nAPI2 Status:', resp2.status)
    data2 = resp2.read().decode('utf-8', errors='ignore')
    j2 = json.loads(data2)
    results2 = j2.get('results', [])[:3]
    for r in results2:
        print('Title:', r.get('title', '')[:60])
        print('Price:', r.get('price'))
        print('Thumbnail:', r.get('thumbnail', '')[:80])
        print('---')
except Exception as e:
    print('API2 Error:', str(e)[:200])
