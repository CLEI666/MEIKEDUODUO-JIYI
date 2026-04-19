import urllib.request, re, json

item_ids = ['MLM73848662275', 'MLM49150785608', 'MLM43924434515']
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json',
    'Referer': 'https://www.mercadolibre.com.mx/'
}

for item_id in item_ids:
    url = f'https://www.mercadolibre.com.mx/item/{item_id}'
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=10)
        html = resp.read().decode('utf-8', errors='ignore')
        # Look for image URLs
        imgs = re.findall(r'https://http2\.mlstatic\.com/[A-Z0-9_\-]+\.(?:webp|jpg|png)', html)
        print(f'{item_id}: {len(imgs)} images found')
        for img in set(imgs[:5]):
            print(f'  {img[:100]}')
        # Find title
        titles = re.findall(r'"title":"([^"]+)"', html)
        if titles:
            print(f'  Title: {titles[0]}')
        # Find price
        prices = re.findall(r'"price":(\d+)', html)
        if prices:
            print(f'  Price: {prices[0]} MXN')
    except Exception as e:
        print(f'{item_id}: Error - {e}')
    print()
