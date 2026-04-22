#!/usr/bin/env python3
"""飞书发送爆品预测卡片 - 2026-04-23"""

import json, urllib.request, urllib.error

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

def send_card(token, card):
    url = f"{BASE}/open-apis/im/v1/messages?receive_id_type=open_id"
    payload = {
        "receive_id": OPEN_ID,
        "msg_type": "interactive",
        "content": json.dumps(card, ensure_ascii=False)
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
print(f"Token OK")

# ─────────────────────────────────────────────
# Card 5: 爆品预测
# ─────────────────────────────────────────────
card5 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "🔮 爆品预测（未来3个月 5-7月）"},
        "subtitle": {"tag": "plain_text", "content": "基于热销榜+热搜趋势综合判断"}
    },
    "elements": [
        {"tag": "markdown", "content": "**🟢 强烈推荐**"},
        {"tag": "markdown", "content": "1. **iPhone卡贴** · 136竞品超级蓝海 · 暴涨280% · ⭐⭐⭐⭐⭐\n2. **三星/小米手机充电器** · 386竞品蓝海 · 暴涨280% · 品牌加持 · ⭐⭐⭐\n3. **汽车点火系统配件** · GMV 1551K · 稳定增长8%+ · 市场成熟 · ⭐⭐⭐\n4. **燃油喷射系统配件** · GMV 1188K · 涨幅9%+ · 利润空间大 · ⭐⭐⭐"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🟡 潜力品类**"},
        {"tag": "markdown", "content": "5. **复用丁腈手套** · 涨幅141% · 工业蓝海 · ⭐⭐\n6. **网络线缆/配件** · GMV 414K · 涨幅17.7% · 持续增长 · ⭐⭐\n7. **牙科设备** · GMV 352K · 涨幅17.88% · 小众专业蓝海 · ⭐⭐"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📋 行动清单**\n\n✅ 联系iPhone卡贴供应商（深圳卡贴王科技），测试产品质量\n✅ 联系三星M33供应商（深圳华信电子），确认拿货价和交货周期\n✅ 优先上架：iPhone卡贴（竞品最少136个，利润高，上手快）\n✅ 次优先上架：三星M33充电器（品牌加持，转化率高）"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "⚠️ **数据说明**：今日浏览器+网络临时故障，数据引用4月22日大麦数据\n\n📊 数据来源：大麦数据 + 美客多 + 1688\n🤖 美客多多 · 专注墨西哥站点选品分析"},
    ]
}
send_card(token, card5)
print("Card 5 done")
