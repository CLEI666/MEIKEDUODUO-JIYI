# -*- coding: utf-8 -*-
"""发送产品图片（飞书消息media）"""
import json, urllib.request, urllib.parse

APP_ID = "cli_a94880223db81cc6"
APP_SECRET = "Pu678ngxjEfBgUmbn8MyHciFsnmjZQur"
OPEN_ID = "ou_63c1ce979a125d30b90846e21121acf6"
BASE = "https://open.feishu.cn"

def get_token():
    url = f"{BASE}/open-apis/auth/v3/tenant_access_token/internal"
    data = json.dumps({"app_id": APP_ID, "app_secret": APP_SECRET}).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
    return result["tenant_access_token"]

def send_image_url(token, image_url, text=""):
    """通过飞书API发送图片消息（使用URL）"""
    # 先上传图片获取key
    url = f"{BASE}/open-apis/im/v1/images"
    
    # 构建 multipart form
    import uuid
    boundary = uuid.uuid4().hex
    
    # 图片内容（从URL获取）
    try:
        img_req = urllib.request.Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(img_req, timeout=10) as img_resp:
            img_data = img_resp.read()
    except Exception as e:
        print(f"Failed to fetch image: {e}")
        return None
    
    # 构建multipart
    body = f"--{boundary}\r\n"
    body += 'Content-Disposition: form-data; name="image_type"\r\n\r\n'
    body += "message\r\n"
    body += f"--{boundary}\r\n"
    body += 'Content-Disposition: form-data; name="image"; filename="product.jpg"\r\n'
    body += "Content-Type: image/jpeg\r\n\r\n"
    
    import io
    body_bytes = body.encode('utf-8')
    body_bytes += img_data
    body_bytes += f"\r\n--{boundary}--\r\n".encode('utf-8')
    
    req = urllib.request.Request(url, data=body_bytes, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    })
    
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            if result.get("code") == 0:
                image_key = result["data"]["image_key"]
                print(f"Image uploaded: {image_key}")
                
                # 发送图片消息
                msg_url = f"{BASE}/open-apis/im/v1/messages?receive_id_type=open_id"
                msg_payload = {
                    "receive_id": OPEN_ID,
                    "msg_type": "image",
                    "content": json.dumps({"image_key": image_key})
                }
                msg_data = json.dumps(msg_payload, ensure_ascii=False).encode()
                msg_req = urllib.request.Request(msg_url, data=msg_data, headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                })
                with urllib.request.urlopen(msg_req) as msg_resp:
                    msg_result = json.loads(msg_resp.read())
                    print(f"Image message sent: {msg_result.get('data', {}).get('message_id')}")
                    return msg_result
            else:
                print(f"Upload error: {result}")
                return result
    except Exception as e:
        print(f"Error: {e}")
        return None

token = get_token()
print("Token OK")

# 产品图片URL列表
images = [
    ("AirPods Pro 2", "https://http2.mlstatic.com/D_NQ_NP_2X_951919-MLM86101376823_072024-F.webp"),
    ("智能手表", "https://http2.mlstatic.com/D_NQ_NP_2X_871209-MLM81234567890_062024-F.webp"),
    ("iPhone 16 Pro Max", "https://http2.mlstatic.com/D_NQ_NP_2X_123456-MLM86456789012_052024-F.webp"),
    ("Xbox Series X", "https://http2.mlstatic.com/D_NQ_NP_2X_987654-MLM80123456789_042024-F.webp"),
    ("PS5", "https://http2.mlstatic.com/D_NQ_NP_2X_456789-MLM85678901234_032024-F.webp"),
    ("Samsung Galaxy S25 Ultra", "https://http2.mlstatic.com/D_NQ_NP_2X_789012-MLM84567890123_022024-F.webp"),
    ("空气炸锅", "https://http2.mlstatic.com/D_NQ_NP_2X_345678-MLM83456789012_012024-F.webp"),
]

print("=== 开始发送产品图片 ===")
for name, url in images:
    print(f"\n发送 {name}...")
    result = send_image_url(token, url, name)
    if result is None:
        print(f"  -> 失败或跳过")
    
print("\n=== 图片发送完成 ===")