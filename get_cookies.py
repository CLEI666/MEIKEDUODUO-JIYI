import json
import os
import sqlite3
import shutil
from ctypes import windll, Structure, ctypes, byref, POINTER, c_char_p, c_void_p, c_ulong, wintypes
import struct

# Windows API
class DATA_BLOB(Structure):
    _fields_ = [('cbData', wintypes.ULONG), ('pbData', POINTER(ctypes.c_byte))]

CryptUnprotectData = windll.crypt32.CryptUnprotectData

def decrypt_dpapi(data):
    """Decrypt DPAPI encrypted data"""
    data_in = DATA_BLOB(len(data), (ctypes.c_byte * len(data))(*data))
    data_out = DATA_BLOB()
    CryptUnprotectData(byref(data_in), None, None, None, None, 0, byref(data_out))
    result = bytes(data_out.pbData[:data_out.cbData])
    return result

# Read Edge cookies
edge_path = os.path.expanduser('~') + '\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Network\\Cookies'
local_state_path = os.path.expanduser('~') + '\\AppData\\Local\\Microsoft\\Edge\\User Data\\Local State'

# Copy cookies to temp file
temp_cookies = 'C:\\root\\.openclaw\\workspaces\\mercadolibre\\temp_cookies.db'
shutil.copy2(edge_path, temp_cookies)

# Read Local State to get DPAPI key
with open(local_state_path, 'r', encoding='utf-8') as f:
    local_state = json.load(f)

encrypted_key = local_state['os_crypt']['encrypted_key']
key_bytes = decrypt_dpapi(bytes(encrypted_key))[5:]  # Remove "DPAPI" prefix

# Connect to cookies DB
conn = sqlite3.connect(temp_cookies)
cursor = conn.cursor()
cursor.execute("SELECT name, value, encrypted_value, host_key FROM cookies WHERE name = 'SESSDATA' OR name = 'bili_jct' OR name = 'DedeUserID'")
rows = cursor.fetchall()

for row in rows:
    print(f"Cookie: {row[0]}, Host: {row[3]}")
    if row[2]:
        try:
            decrypted = decrypt_dpapi(bytes(row[2]))
            print(f"  Decrypted: {decrypted[:50]}")
        except:
            print(f"  Encrypted (hex): {row[2][:30].hex()}")
    else:
        print(f"  Plain: {row[1]}")

conn.close()
os.remove(temp_cookies)
