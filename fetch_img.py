import urllib.request, re, json, sys

url = 'https://www.mercadolibre.com.mx/search?q=samsung+m33+charger'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Language': 'es-MX,es;q=0.9',
    'Accept': 'text/html'
})
try:
    resp = urllib.request.urlopen(req, timeout=15)
    html = resp.read().decode('utf-8', errors='ignore')
    
    # Find thumbnail images
    imgs = re.findall(r'"thumbnail":"(https://http2\.mlstatic\.com[^"]+)"', html)
    print(f"Found {len(imgs)} images")
    for img in imgs[:5]:
        print(img[:120])
    
    # Also try picture field
    imgs2 = re.findall(r'"picture":"(https://http2\.mlstatic\.com[^"]+)"', html)
    print(f"\nFound {len(imgs2)} picture images")
    for img in imgs2[:5]:
        print(img[:120])
    
    # Find item IDs
    items = re.findall(r'/p/MLM\d+', html)
    print(f"\nItem IDs: {list(dict.fromkeys(items))[:5]}")
    
except Exception as e:
    print(f"Error: {e}")