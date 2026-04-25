import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

url = 'https://www.mercadolibre.com.mx/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9,en;q=0.8',
    'Accept': 'text/html',
}
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req, timeout=15)
html = resp.read().decode('utf-8', errors='ignore')

# Find all links with search patterns
search_links = re.findall(r'href="([^"]*(?:search|buscar)[^"]*)"', html, re.IGNORECASE)
print('Search links:', search_links[:10])

# Find all data-item or product links
product_links = re.findall(r'href="(/p/[^"]+)"', html)
print('Product links:', product_links[:10])

# Find all links
all_links = re.findall(r'href="([^"]+)"', html)
print('\nAll links count:', len(all_links))
# Filter interesting ones
interesting = [l for l in all_links if any(x in l.lower() for x in ['search', 'celular', 'cargador', 'auto', 'iphone', 'samsung', 'nitrilo', 'rsim'])]
print('Interesting links:', interesting[:15])

# Also look for the search form action
form_actions = re.findall(r'action="([^"]*(?:search|buscar)[^"]*)"', html, re.IGNORECASE)
print('Form actions:', form_actions[:5])

# Look for data in scripts
scripts = re.findall(r'<script[^>]*>([^<]+)</script>', html)[:5]
for i, s in enumerate(scripts):
    if len(s) > 50:
        print(f'\nScript {i} (first 200 chars):')
        print(s[:200])

# Look for JSON data blocks
json_blocks = re.findall(r'window\.__\w+__\s*=\s*(\{.{0,3000\});', html)
print(f'\nJSON blocks found: {len(json_blocks)}')
