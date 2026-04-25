import urllib.request, re, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9,en;q=0.8',
    'Accept': 'text/html',
    'Referer': 'https://listado.mercadolibre.com.mx/',
}

queries = [
    ('samsung_m33', 'cargador-samsung-m33-25w'),
    ('iphone_rsim', 'rsim-iphone-13'),
    ('nitrile_gloves', 'guantes-nitrilo-reutilizables'),
    ('micas_celular', 'micas-celular'),
]

for name, q in queries:
    url = f'https://listado.mercadolibre.com.mx/{q}'
    print(f'\n=== {name}: {q} ===')
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=15)
    html = resp.read().decode('utf-8', errors='ignore')
    print(f'HTML length: {len(html)}')
    
    # Get item_ids (these are the listing IDs)
    item_ids = re.findall(r'"item_id":"(MLM\d+)"', html)
    print(f'item_ids found: {len(item_ids)}')
    
    # Get articulo links which contain the titles
    articulo_links = re.findall(r'href="(https://articulo\.mercadolibre[^"]+)"', html)
    print(f'articulo links: {len(articulo_links)}')
    
    # Extract titles from articulo links
    for link in articulo_links[:5]:
        # Extract the title slug from the URL
        match = re.search(r'MLM-\d+-(.+?)(?:-_JM|$)', link)
        if match:
            title = match.group(1).replace('-', ' ')
            print(f'  Title from URL: {title[:80]}')
    
    # Get prices 
    prices = re.findall(r'"price":(\d+)', html)
    print(f'Prices (first 20): {prices[:20]}')
    
    # Look for the price next to specific item IDs
    # Pattern: price followed by item_id within some characters
    for i, item_id in enumerate(item_ids[:10]):
        # Find position of item_id in HTML
        pos = html.find(f'"item_id":"{item_id}"')
        if pos > 0:
            # Get surrounding context
            context = html[max(0, pos-200):pos+100]
            price_match = re.search(r'"price":(\d+)', context)
            if price_match:
                print(f'  {item_id}: price={price_match.group(1)}')
