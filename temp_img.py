import urllib.request, re, json, os

# Try to find real images for our products via search
searches = [
    ('samsung_m33', 'https://www.mercadolibre.com.mx/search?q=cargador+samsung+m33+25w'),
    ('iphone_rsim', 'https://www.mercadolibre.com.mx/search?q=rsim+iphone+卡贴'),
    ('nitrile_gloves', 'https://www.mercadolibre.com.mx/search?q=guantes+nitrilo+reutilizables+100'),
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-MX,es;q=0.9',
}

for name, url in searches:
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=15)
        html = resp.read().decode('utf-8', errors='ignore')
        # Find item IDs
        item_ids = re.findall(r'/p/MLM\d+', html)
        item_ids = list(dict.fromkeys(item_ids))[:3]
        print(f'{name}: items found: {item_ids}')
        # Find images with different patterns
        imgs1 = re.findall(r'https://http2\.mlstatic\.com/D_[^"\'>\s]+\.(?:webp|jpg)', html)
        imgs2 = re.findall(r'"thumbnail":"(https://http2\.mlstatic\.com/[^"]+)"', html)
        imgs3 = re.findall(r'"picture":"(https://http2\.mlstatic\.com/[^"]+)"', html)
        print(f'  Pattern1: {len(imgs1)}, Pattern2: {len(imgs2)}, Pattern3: {len(imgs3)}')
        for img in imgs2[:3]:
            print(f'    {img[:80]}')
        for img in imgs3[:3]:
            print(f'    {img[:80]}')
    except Exception as e:
        print(f'{name}: Error - {e}')
    print()
