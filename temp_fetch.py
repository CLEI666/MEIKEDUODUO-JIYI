import urllib.request, re, json

search_queries = [
    ('samsung_m33_charger', 'https://www.mercadolibre.com.mx/search?q=samsung+m33+charger'),
    ('iphone_rsim', 'https://www.mercadolibre.com.mx/search?q=rsim+iphone'),
    ('nitrile_gloves', 'https://www.mercadolibre.com.mx/search?q=guantes+nitrilo+reutilizables'),
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for name, url in search_queries:
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        # Find image URLs
        imgs = re.findall(r'https://http2\.mlstatic\.com/[^\"\'>\s]+\.(?:jpg|webp|png|jpeg)', html)
        print(f'=== {name} ===')
        print(f'Found {len(imgs)} images')
        seen = set()
        for img in imgs:
            if img not in seen and len(seen) < 5:
                seen.add(img)
                print(img[:100])
        # Also find price and title
        titles = re.findall(r'"title":"([^"]+)"', html)[:3]
        print('Titles:', titles)
        prices = re.findall(r'"price":(\d+)', html)[:5]
        print('Prices:', prices)
    except Exception as e:
        print(f'{name}: Error - {e}')
    print()
