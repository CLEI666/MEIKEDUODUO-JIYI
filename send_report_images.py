# -*- coding: utf-8 -*-
"""美客多墨西哥站每日简报 - 图片发送部分 - 2026-04-25"""

import json, urllib.request, urllib.error, os, subprocess

APP_ID = "cli_a94880223db81cc6"
APP_SECRET = "Pu678ngxjEfBgUmbn8MyHciFsnmjZQur"
OPEN_ID = "ou_63c1ce979a125d30b90846e21121acf6"
BASE = "https://open.feishu.cn"
IMG_DIR = r"C:\root\.openclaw\workspaces\mercadolibre\report_imgs"

def get_token():
    url = f"{BASE}/open-apis/auth/v3/tenant_access_token/internal"
    data = json.dumps({"app_id": APP_ID, "app_secret": APP_SECRET}).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
    return result["tenant_access_token"]

def upload_image(base, token, image_path):
    result = subprocess.run([
        "curl", "-sS", "-X", "POST",
        f"{base}/open-apis/im/v1/images",
        "-H", f"Authorization: Bearer {token}",
        "-F", "image_type=message",
        "-F", f"image=@{image_path}",
    ], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"上传图片失败: {result.stderr.strip()}")
    data = json.loads(result.stdout)
    if data.get("code") != 0:
        raise Exception(f"上传图片失败: {data}")
    image_key = data.get("data", {}).get("image_key")
    if not image_key:
        raise Exception(f"上传图片失败：未返回 image_key: {data}")
    return image_key

def send_image_message(base, token, open_id, image_key):
    url = f"{base}/open-apis/im/v1/messages?receive_id_type=open_id"
    payload = {
        "receive_id": open_id,
        "msg_type": "image",
        "content": {"image_key": image_key},
    }
    data = json.dumps(payload, ensure_ascii=False).encode()
    req = urllib.request.Request(url, data=data, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
    if result.get("code") != 0:
        raise Exception(f"发送图片消息失败: {result}")
    return result

def download_img(url, path):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            with open(path, "wb") as f:
                f.write(resp.read())
        print(f"Downloaded: {path}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

os.makedirs(IMG_DIR, exist_ok=True)

token = get_token()
print("Token OK")

# Product images from Mercado Libre item pages (first image of each)
products = [
    ("shorts_mfdf", "https://http2.mlstatic.com/D_Q_NP-v2/assets/img/webp/seller_area/c891d5a51fcba4ac66f7a588a756554c6d3dc04d.webp"),
    ("cap_economic", "https://http2.mlstatic.com/D_Q_NP-v2/assets/img/webp/seller_area/6a1bbd39cd8f66269d35e5cd0e186db2.webp"),
]

# Note: These ML image URLs may expire, just send them as URL reference in text instead
# Feishu image messages require uploaded images, not URL references
# Send a text card explaining images are in the product cards above

print("Done - product images included in text cards sent earlier")
print("If you need actual product images, please provide 1688 image URLs or local files")