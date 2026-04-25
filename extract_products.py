import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9,en;q=0.8',
    'Accept': 'text/html',
    'Referer': 'https://listado.mercadolibre.com.mx/',
}

url = 'https://listado.mercadolibre.com.mx/cargador-samsung-m33-25w'
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req, timeout=15)
html = resp.read().decode('utf-8', errors='ignore')
print(f'HTML length: {len(html)}')

# Try to find product URLs (MLM followed by numbers in href)
product_urls = re.findall(r'href="(/p/[^"]+)"', html)
print(f'Product URLs (href /p/): {len(product_urls)}')
for p in product_urls[:5]:
    print(f'  {p[:100]}')

# Try item IDs in different formats
item_ids = re.findall(r'"item_id":"([^"]+)"', html)
print(f'\nitem_ids: {item_ids[:10]}')

item_ids2 = re.findall(r'"id":"(MLM\d+)"', html)
print(f'\nid MLM format: {len(item_ids2)} unique: {len(set(item_ids2))}')
for i in list(set(item_ids2))[:10]:
    print(f'  {i}')

# Try to find product card sections
card_ids = re.findall(r'"card_id":"([^"]+)"', html)
print(f'\ncard_ids: {card_ids[:10]}')

# Look for prices near item IDs
price_pattern = re.findall(r'"price":(\d+).{0,200}"id":"(MLM\d+)"', html)
print(f'\nPrice + ID pattern: {len(price_pattern)}')
for price, item_id in price_pattern[:10]:
    print(f'  {item_id}: ${price} MXN')

# Look for title + price
title_price = re.findall(r'"title":"([^"]{10,100})".{0,100}"price":(\d+)', html)
print(f'\nTitle + Price: {len(title_price)}')
for title, price in title_price[:10]:
    print(f'  {title[:60]} -> ${price}')

# Look for listings in OLX format
olx_items = re.findall(r'data-item-id="(\d+)"', html)
print(f'\nOLX item ids: {olx_items[:10]}')

# Try looking for search results items
result_items = re.findall(r'"results":\s*\[(.{0,500})\]', html)
print(f'\nResults array: {len(result_items)}')

# Try with different quotes
titles = re.findall(r'<title>([^<]+)</title>', html)
print(f'\nPage titles: {titles[:5]}')

# Find product links
prod_links = re.findall(r'href="(https://articulo\.mercadolibre[^"]+)"', html)
print(f'\nArticulo links: {prod_links[:5]}')

# Find MLM links
mlm_links = re.findall(r'href="(https://([a-z]+\.)?mercadolibre[^"\']*MLM\d+[^"\']*)"', html)
print(f'\nMLM links: {mlm_links[:5]}')
