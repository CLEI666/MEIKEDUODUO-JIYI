# -*- coding: utf-8 -*-
"""美客多墨西哥站每日简报 - 发送产品图片（2026-04-26）"""
import json, urllib.request

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

def send_image_url(token, image_url, file_name="image"):
    """通过飞书消息发送图片URL"""
    url = f"{BASE}/open-apis/im/v1/messages?receive_id_type=open_id"
    payload = {
        "receive_id": OPEN_ID,
        "msg_type": "image",
        "content": json.dumps({"file_id": image_url})
    }
    data = json.dumps(payload, ensure_ascii=False).encode()
    req = urllib.request.Request(url, data=data, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='ignore')
        print(f"HTTP Error {e.code}: {body[:500]}")
        raise
    if result.get("code") != 0:
        print(f"Error: {result}")
    else:
        print(f"OK: {result.get('data', {}).get('message_id')}")
    return result

def send_text_message(token, text):
    """发送纯文本消息"""
    url = f"{BASE}/open-apis/im/v1/messages?receive_id_type=open_id"
    payload = {
        "receive_id": OPEN_ID,
        "msg_type": "text",
        "content": json.dumps({"text": text})
    }
    data = json.dumps(payload, ensure_ascii=False).encode()
    req = urllib.request.Request(url, data=data, headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='ignore')
        print(f"HTTP Error {e.code}: {body[:500]}")
        raise
    if result.get("code") != 0:
        print(f"Error: {result}")
    else:
        print(f"OK: {result.get('data', {}).get('message_id')}")
    return result

token = get_token()
print("Token OK")

# 发送图片说明
send_text_message(token, "📸 产品图片展示（来自1688/美客多，实物图+白底图）\n\n以下为今日简报产品对应图片参考：")

# 产品图片URL（使用公开图片URL）
products = [
    {"name": "🎮 Xbox Series X 1TB", "url": "https://http2.mlstatic.com/D_NQ_NP_2X_970X725_MLM20714491281_062022-F.webp"},
    {"name": "🎮 PS5 轻薄版套装", "url": "https://http2.mlstatic.com/D_NQ_NP_2X_970X725_MLM20912007657_092022-F.webp"},
    {"name": "📱 iPhone 16 Pro Max 256GB", "url": "https://http2.mlstatic.com/D_NQ_NP_2X_970X725_MLM20714491281_062022-F.webp"},
    {"name": "🎧 AirPods Pro 2 USB-C", "url": "https://http2.mlstatic.com/D_NQ_NP_2X_970X725_MLM20714491281_062022-F.webp"},
    {"name": "📱 Samsung Galaxy S25 Ultra", "url": "https://http2.mlstatic.com/D_NQ_NP_2X_970X725_MLM20714491281_062022-F.webp"},
    {"name": "🍳 空气炸锅 5.5L", "url": "https://http2.mlstatic.com/D_NQ_NP_2X_970X725_MLM20714491281_062022-F.webp"},
    {"name": "⌚ 智能手表 防水款", "url": "https://http2.mlstatic.com/D_NQ_NP_2X_970X725_MLM20714491281_062022-F.webp"},
]

# 图片URL说明：由于今日浏览器故障，暂用美客多通用占位图
# 实际运营中建议使用1688白底图+实物图上传到飞书
note_card = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "📸 产品图片说明"},
        "subtitle": {"tag": "plain_text", "content": "2026-04-26 简报图片备注"}
    },
    "elements": [
        {"tag": "markdown", "content": "**⚠️ 图片说明**\n\n由于今日浏览器临时故障，图片暂用美客多CDN占位图。\n\n**实际运营建议：**\n- 1688实物图：联系供应商索取实物照片\n- 白底图：1688图片下载后用PS/美图处理白底\n- 上传到飞书：使用飞书发图脚本 send_image.py\n- 图片命名规范：`品类_产品名_实拍.jpg` / `品类_产品名_白底.jpg`"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**✅ 图片获取渠道**\n\n1. **1688供应商** — 联系供应商客服，索要实物图+白底图\n2. **美客多竞品** — 截图竞品主图，分析拍摄风格\n3. **1688图片采集** — 用脚本批量采集1688产品图\n4. **供应商样品** — 购买样品后自行拍摄"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📁 图片存储路径**\n\n- 实物图：`report_imgs/实拍/`\n- 白底图：`report_imgs/白底/`\n- 竞品图：`report_imgs/竞品/`\n\n图片准备好后，运行：\n```powershell\n$env:PYTHONIOENCODING=\"utf8\"; python send_image.py <图片路径> <open_id> <app_id> <app_secret>\n```"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "🤖 美客多多 · 专注墨西哥站点选品分析"},
    ]
}

from send_card import send_card as sc
sc(token, note_card)
print("Note card done")

print("=== 图片说明发送完成 ===")