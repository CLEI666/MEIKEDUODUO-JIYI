import urllib.request, re, sys

url = 'https://www.mercadolibre.com.mx/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9,en;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}
try:
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=10)
    print('Status:', resp.status)
    print('Final URL:', resp.url[:100])
    html = resp.read().decode('utf-8', errors='ignore')
    print('HTML Length:', len(html))
    # Try to find categories or hot items
    cats = re.findall(r'"category":\s*"([^"]+)"', html)[:10]
    print('Categories found:', cats)
    # Try OG or meta
    titles = re.findall(r'<title>([^<]+)</title>', html)
    print('Page title:', titles[:3])
except Exception as e:
    print('Error:', str(e)[:200])
