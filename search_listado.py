import urllib.request, re, sys, json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9,en;q=0.8',
    'Accept': 'text/html',
    'Referer': 'https://listado.mercadolibre.com.mx/',
}

queries = [
    'cargador-samsung-m33-25w',
    'rsim-iphone-13',
    'guantes-nitrilo-reutilizables-100',
    'micas-celular',
    'accesorios-autos',
]

for q in queries:
    url = f'https://listado.mercadolibre.com.mx/{q}'
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        print(f'Query: {q}')
        print(f'  Status: {resp.status}, Length: {len(html)}')
        
        # Find items
        items = re.findall(r'"id":"(MLM\d+)","title":"([^"]+)"', html)
        print(f'  Items found: {len(items)}')
        for item_id, title in items[:5]:
            print(f'    {item_id}: {title[:70]}')
        
        # Find prices
        prices = re.findall(r'"price":(\d+)', html)[:10]
        print(f'  Prices: {prices[:10]}')
        
        # Find images
        imgs = re.findall(r'https://http2\.mlstatic\.com/D_NQ_[^\s"\'<>]+\.(?:jpg|webp)', html)[:5]
        print(f'  Images: {[img[:80] for img in imgs[:3]]}')
        print()
    except Exception as e:
        print(f'Error for {q}: {str(e)[:100]}')
        print()
