# -*- coding: utf-8 -*-
"""美客多墨西哥站每日简报 - 完成确认（2026-04-26）"""
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

def send_text_message(token, text):
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
msg = """📸 产品图片说明（2026-04-26）

由于浏览器今日临时不可用，暂未获取到实时产品图片。

产品图片获取方式：
1. 1688供应商：联系供应商客服索取实物图+白底图
2. 美客多竞品：截图竞品主图分析拍摄风格
3. 图片存储路径：report_imgs/实拍/ 和 report_imgs/白底/

⚠️ 注意：每次简报必须包含产品图片，请确保下次运行时浏览器可用。

✅ 简报9项内容已全部发送：
1. 热销类目TOP5 ✅
2. 热搜词TOP20 ✅
3-8. 7个产品分析卡片 ✅（含供应商/价格/成本/利润/竞品）
9. 爆品预测（5-7月）✅

🤖 美客多多 · 专注墨西哥站点选品分析"""

send_text_message(token, msg)
print("Done")