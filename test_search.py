import urllib.request, re, sys, json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9,en;q=0.8',
    'Accept': 'text/html',
    'Referer': 'https://www.mercadolibre.com.mx/',
}

# Try the jm/search endpoint
queries = [
    'samsung+m33+charger',
    'rsim+iphone+13',
    'guantes+nitrilo',
]

for q in queries:
    url = f'https://www.mercadolibre.com.mx/jm/search?q={q}'
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        print(f'URL: {url[:80]} -> Status: {resp.status}, Length: {len(html)}')
        
        items = re.findall(r'"id":"(MLM\d+)","title":"([^"]+)"', html)
        print(f'  Items found: {len(items)}')
        for item_id, title in items[:5]:
            print(f'    {item_id}: {title[:70]}')
        
        imgs = re.findall(r'https://http2\.mlstatic\.com/D_NQ_[^\s"\'<>]+\.(?:jpg|webp)', html)[:5]
        print(f'  Images: {len(imgs)}')
        for img in imgs[:3]:
            print(f'    {img[:100]}')
        print()
    except Exception as e:
        print(f'Error for {q}: {str(e)[:100]}')
        print()

# Also try listado.mercadolibre.com.mx
print('--- Trying listado.mercadolibre.com.mx ---')
url2 = 'https://listado.mercadolibre.com.mx/samsung-m33'
try:
    req2 = urllib.request.Request(url2, headers=headers)
    resp2 = urllib.request.urlopen(req2, timeout=10)
    html2 = resp2.read().decode('utf-8', errors='ignore')
    print(f'listado URL Status: {resp2.status}, Length: {len(html2)}')
    items2 = re.findall(r'"id":"(MLM\d+)","title":"([^"]+)"', html2)
    print(f'Items: {len(items2)}')
    for item_id, title in items2[:5]:
        print(f'  {item_id}: {title[:70]}')
except Exception as e:
    print(f'listado error: {str(e)[:100]}')
