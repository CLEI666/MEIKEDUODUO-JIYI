import urllib.request, re, sys, gzip, zlib

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

url = 'https://www.mercadolibre.com.mx/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'es-MX,es;q=0.9,en;q=0.8',
    'Accept': 'text/html',
}

# First try without compression
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req, timeout=15)
print('Status:', resp.status)
print('Headers:', dict(resp.headers))
print('Content-Encoding:', resp.headers.get('Content-Encoding', 'none'))
raw = resp.read()
print('Raw length:', len(raw))

# Check if it's gzip
if raw[:2] == b'\x1f\x8b':
    print('Data is gzip compressed!')
    try:
        decompressed = gzip.decompress(raw)
        print('Decompressed length:', len(decompressed))
        text = decompressed.decode('utf-8', errors='ignore')
    except:
        try:
            decompressed = zlib.decompress(raw, 16 + gzip.MAX_WBITS)
            print('Decompressed (raw) length:', len(decompressed))
            text = decompressed.decode('utf-8', errors='ignore')
        except Exception as e:
            print('Decompress error:', e)
            text = ''
elif raw[:2] == b'PK':
    print('Data is a ZIP file!')
    text = ''
else:
    text = raw.decode('utf-8', errors='ignore')
    print('Decoded as UTF-8')

print('Text length:', len(text))
print('First 300 chars of text:')
print(text[:300])
print('---')
# Look for items in the text
items = re.findall(r'"id":"(MLM\d+)","title":"([^"]+)"', text)
print(f'Items found: {len(items)}')
for item_id, title in items[:10]:
    print(f'  {item_id}: {title[:60]}')
    
# Try finding simple text patterns
prices = re.findall(r'\$(\d{1,4})\s*MXN', text)
print(f'Prices found: {prices[:10]}')

searches = re.findall(r'query["\']?\s*[:=]\s*["\']([^"\']+)["\']', text)
print(f'Search queries: {searches[:5]}')
