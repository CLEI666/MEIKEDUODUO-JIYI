import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

url = 'https://www.mercadolibre.com.mx/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9,en;q=0.8',
    'Accept': 'text/html',
    'Accept-Encoding': 'gzip, deflate, br',
}

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req, timeout=15)
html = resp.read().decode('utf-8', errors='ignore')
print('HTML length:', len(html))
print('First 2000 chars:')
print(html[:2000])
print('...')
print('Last 1000 chars:')
print(html[-1000:])
