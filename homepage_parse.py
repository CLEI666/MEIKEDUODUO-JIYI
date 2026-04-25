import urllib.request, re, json, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

url = 'https://www.mercadolibre.com.mx/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9,en;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
}

try:
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req, timeout=15)
    print('Status:', resp.status)
    print('Final URL:', resp.url[:100])
    html = resp.read().decode('utf-8', errors='ignore')
    print('HTML length:', len(html))
    
    # Find all item IDs and titles in the page
    all_items = re.findall(r'"id":"(MLM\d+)","title":"([^"]+)"', html)
    print('\nAll items found:', len(all_items))
    for item_id, title in all_items[:20]:
        print(f'  {item_id}: {title[:70]}')
    
    # Find all prices
    all_prices = re.findall(r'"price":(\d+)', html)
    print('\nPrices sample:', all_prices[:20])
    
    # Find category names in navigation
    cat_names = re.findall(r'"name":"([^"]{3,60})"', html)
    print('\nItem names (sample):', cat_names[:20])
    
    # Look for search-related content
    search_data = re.findall(r'"query":"([^"]+)"', html)
    print('\nSearch queries:', search_data[:10])
    
    # Look for dynamic data
    dynamic = re.findall(r'"category":\s*{[^}]{0,200}}', html)[:5]
    print('\nCategory data:', dynamic[:3])
    
    # Look for bestseller/trending sections
    section_titles = re.findall(r'"sectionTitle":"([^"]+)"', html)
    print('\nSection titles:', section_titles[:10])
    
except Exception as e:
    print('Error:', str(e)[:300])
