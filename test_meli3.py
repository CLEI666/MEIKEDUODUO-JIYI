import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

url = 'https://www.mercadolibre.com.mx/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9,en;q=0.8',
    'Accept': 'text/html,application/xhtml+xml'
}
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req, timeout=15)
html = resp.read().decode('utf-8', errors='ignore')
print('HTML length:', len(html))

# Search for trending/searches
trending = re.findall(r'"query":"([^"]+)"', html)[:10]
print('Trending queries:', trending)

# Search for category navigation
cat_nav = re.findall(r'/categorias[^"]*', html)[:10]
print('Category nav:', cat_nav[:5])

# Search for image URLs
imgs = re.findall(r'https://http2\.mlstatic\.com/[^\s"\'<>]+\.(?:jpg|jpeg|webp|png)', html)[:15]
print('Images count:', len(imgs))
for img in imgs[:5]:
    print(' ', img[:100])

# Search for item IDs  
items = re.findall(r'"id":"(MLM\d+)","title":"([^"]+)"', html)[:10]
print('Items count:', len(items))
for item_id, title in items[:5]:
    print(' ', item_id, '-', title[:50])

# Try to find sections/categories in navigation
nav_cats = re.findall(r'/MLM\d+', html)[:20]
print('MLM category IDs:', list(set(nav_cats))[:10])

# Search for top level categories 
top_cats = re.findall(r'"category":\s*"([^"]+)"', html)[:10]
print('Categories:', top_cats[:5])

# Search for bestseller sections
best = re.findall(r'mas-vendido[s]?', html, re.IGNORECASE)
print('Mas vendido matches:', len(best))
