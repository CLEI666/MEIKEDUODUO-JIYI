import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9',
    'Accept': 'text/html',
    'Connection': 'keep-alive',
}

# Try different URL formats
urls = [
    'https://www.mercadolibre.com.mx/mlmclk?url=https://www.mercadolibre.com.mx/search?q=samsung+m33',
    'https://www.mercadolibre.com.mx/navigation/addresses-gone?url=https%3A%2F%2Fwww.mercadolibre.com.mx%2Fsearch%3Fq%3Dsamsung%2Bm33',
    'https://www.mercadolibre.com.mx/search?q=samsung+m33&siteId=MLM',
    'https://list.mercadolibre.com.mx/samsung-m33',
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req, timeout=10)
        print(f'URL: {url[:80]} -> Status: {resp.status}, Final: {resp.url[:80]}')
        html = resp.read().decode('utf-8', errors='ignore')
        print(f'  HTML length: {len(html)}')
        items = re.findall(r'"id":"(MLM\d+)","title":"([^"]+)"', html)[:3]
        print(f'  Items: {items[:2]}')
        imgs = re.findall(r'https://http2\.mlstatic\.com[^\s"\'<>]+\.(?:jpg|webp)', html)[:3]
        print(f'  Images: {[i[:80] for i in imgs]}')
        print()
    except Exception as e:
        print(f'Error for {url[:60]}: {str(e)[:80]}')
        print()
