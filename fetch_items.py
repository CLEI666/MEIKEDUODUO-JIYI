import urllib.request, re, json, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Try specific product URLs we know from previous reports
products = [
    ('samsung_m33', 'MLM1593364022', 'Cargador Samsung M33'),
    ('iphone_rsim', 'MLM1234567890', 'RSIM iPhone'),
    ('nitrile_gloves', 'MLM9876543210', 'Guantes Nitrilo'),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9',
}

# Try fetching search pages which might have current product listings
search_queries = [
    'samsung+m33+charger',
    'rsim+iphone+13',
    'guantes+nitrilo+reutilizables',
    'cargador+celular+25w',
]

for q in search_queries:
    url = f'https://www.mercadolibre.com.mx/search?q={q}'
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        print(f'URL: {url} -> Status: {resp.status}, Length: {len(html)}')
        
        # Find items
        items = re.findall(r'"id":"(MLM\d+)","title":"([^"]+)"', html)
        print(f'  Items found: {len(items)}')
        for item_id, title in items[:3]:
            print(f'    {item_id}: {title[:60]}')
        
        # Find prices
        prices = re.findall(r'"price":(\d+)', html)[:5]
        print(f'  Prices: {prices}')
        
        # Find images
        imgs = re.findall(r'https://http2\.mlstatic\.com/D_NQ_[^\s"\'<>]+\.(?:jpg|webp|png|jpeg)', html)[:5]
        print(f'  Images: {len(imgs)}')
        for img in imgs[:3]:
            print(f'    {img[:100]}')
        print()
    except Exception as e:
        print(f'Error for {q}: {str(e)[:100]}')
        print()
