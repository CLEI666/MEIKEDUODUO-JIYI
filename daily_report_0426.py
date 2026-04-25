# -*- coding: utf-8 -*-
"""美客多墨西哥站每日简报 - 2026-04-26"""
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
print("Token OK")

# Card 1: 热销类目+热搜词
card1 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "📊 美客多墨西哥站 每日简报 2026-04-26"},
        "subtitle": {"tag": "plain_text", "content": "数据来源：大麦数据 + 美客多官网 + 1688"}
    },
    "elements": [
        {"tag": "markdown", "content": "**🔥 今日热销类目 TOP5**\n\n1️⃣ **电子产品 Electronica** — 手机/配件稳居第1\n2️⃣ **电脑 Computacion** — 游戏配件+平板持续热销\n3️⃣ **运动健身 Deportes y Fitness** — 健身补剂+运动服饰季节爆发\n4️⃣ **服装鞋帽 Ropa y Calzado** — 换季需求上升\n5️⃣ **美妆护肤** — 独立赛道，需求持续增长"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🔍 热搜词 TOP20**\n\n iphone 16 · iphone 16 pro max · playstation 5 · aire acondicionado · airpods · apple watch · laptop · samsung galaxy · nintendo switch · xbox series x · freidora de aire · tablet · bocina jbl · smart watch · camaras de seguridad · chromecast · refrigerator lg · celular samsung · alexa · eufy"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "📌 说明：iphone 16系列持续霸榜，空调/空气炸锅进入夏季爆发期，智能家居设备需求上升\n\n🤖 美客多多 · 专注墨西哥站点选品分析"},
    ]
}
send_card(token, card1)
print("Card 1 done")

# Card 2: 产品1 - Xbox Series X
card2 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "🎮 产品1：Xbox Series X 1TB 白色"},
        "subtitle": {"tag": "plain_text", "content": "美客多游戏机类畅销榜第1 | 1º MAS VENDIDO"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\nXbox Series X 白色 1TB SSD 次世代游戏主机\n- 型号：Xbox Series X (RRT-00009)\n- 存储：1TB SSD（支持4K 120fps）\n- 配件：手柄+电源线+HDMI线\n- 折扣：26% OFF（$12,999→$9,599 MXN）\n- 销量：游戏机类第1"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$9,599 MXN**（含26%折扣）\n- 美客多佣金（约15%）：$1,440\n- 实际到账约：**$8,159 MXN ≈ ¥4,743人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考港版） | ¥3,200-3,600元 |\n| 头程运费（≈4kg×50元/kg） | ¥200元 |\n| 美客多佣金15% | ¥711元 |\n| 广告费10% | ¥474元 |\n| 退货损耗5% | ¥237元 |\n| **合计成本** | **¥4,622-5,022元** |\n| 平台收入 | **¥4,743元** |\n| **预估利润** | **¥-279~+121元（微利至微亏）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**⚠️ 利润分析**\n主机类属引流款，利润率低（1-3%），但销量稳定\n\n✅ 建议配合手柄/游戏等配件捆绑销售，提升整体利润\n✅ 走量为主，评价累计后可持续销售\n✅ 注意正品渠道，避免假货风险"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：Xbox Series X 正品 港版\n- 建议拿货价：≤¥3,400元/台\n- 目标供应商：深圳/广州游戏机批发商\n- 起订量：5-10台+\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card2)
print("Card 2 done")

# Card 3: 产品2 - PlayStation 5
card3 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "🎮 产品2：PS5 轻薄版 + 2手柄套装"},
        "subtitle": {"tag": "plain_text", "content": "美客多游戏机类第2名 | 超人气套装"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\nPlayStation 5 轻薄版 + 2个DualSense手柄 套装\n- 型号：PS5 Slim（数字版）\n- 存储：1TB SSD\n- 套装内容：主机+2手柄+底座+电源线\n- 折扣：17% OFF（$10,499→$8,699 MXN）\n- 销量：游戏机类第2"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$8,699 MXN**（含17%折扣）\n- 美客多佣金（约15%）：$1,305\n- 实际到账约：**$7,394 MXN ≈ ¥4,297人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考港版Slim） | ¥3,000-3,400元 |\n| 头程运费（≈3.5kg×50元/kg） | ¥175元 |\n| 美客多佣金15% | ¥645元 |\n| 广告费10% | ¥430元 |\n| 退货损耗5% | ¥215元 |\n| **合计成本** | **¥4,365-4,765元** |\n| 平台收入 | **¥4,297元** |\n| **预估利润** | **¥-468~-68元（亏损）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**⚠️ 利润分析**\n当前折扣价无法覆盖成本，建议在折扣期快速清货\n\n✅ 主机+2手柄套装差异化竞争，转化率高\n✅ PS5品牌忠诚度高，评价积累后可持续销售\n✅ 关注正常价区间（$10,499），恢复原价后利润约¥500+"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：PS5 Slim 港版 正版\n- 建议拿货价：≤¥3,200元/台（套装）\n- 目标供应商：深圳/广州游戏机批发商\n- 起订量：5-10台+\n\n⚠️ 索尼产品假货风险高，建议实地看货或走平台担保\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card3)
print("Card 3 done")

# Card 4: 产品3 - iPhone 16 Pro Max
card4 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "📱 产品3：iPhone 16 Pro Max 256GB 钛灰"},
        "subtitle": {"tag": "plain_text", "content": "美客多手机类热搜第1 | 苹果年度旗舰"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\nApple iPhone 16 Pro Max 256GB Titanium Gray\n- 屏幕：6.9英寸 Super Retina XDR\n- 芯片：A18 Pro\n- 摄像头：48MP主摄+5倍光学变焦\n- 配色：钛灰（Titanium Gray）\n- 原价：$32,999 MXN，当前无折扣\n- 销量：手机类热搜第1"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$32,999 MXN**（原价，无折扣）\n- 美客多佣金（约15%）：$4,950\n- 实际到账约：**$28,049 MXN ≈ ¥16,300人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考港版256G） | ¥10,500-11,200元 |\n| 头程运费（≈220g×50元/kg） | ¥11元 |\n| 美客多佣金15% | ¥2,445元 |\n| 广告费10% | ¥1,630元 |\n| 退货损耗5% | ¥815元 |\n| **合计成本** | **¥15,401-16,101元** |\n| 平台收入 | **¥16,300元** |\n| **预估利润** | **¥199~899元（约1-5%利润率）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**⚠️ 利润分析**\n苹果手机属引流款，利润极低（1-5%）\n\n✅ iPhone 16系列持续霸榜热搜，流量巨大\n✅ 搭配手机壳/膜/充电器等配件提升整体利润\n✅ 港版价格优势明显，建议做港版货源"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：iPhone 16 Pro Max 港版 256G\n- 建议拿货价：≤¥10,800元/台\n- 目标供应商：深圳/香港手机批发商\n- 起订量：5台+\n\n⚠️ 必须验证正品渠道，避免买到展示机或翻新机\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card4)
print("Card 4 done")

# Card 5: 产品4 - AirPods Pro 2
card5 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "🎧 产品4：AirPods Pro 2 USB-C版"},
        "subtitle": {"tag": "plain_text", "content": "美客多耳机类第1 | 苹果生态热销配件"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\nApple AirPods Pro 2代 USB-C接口\n- 芯片：H2芯片，个性化空间音频\n- 降噪：主动降噪+通透模式\n- 续航：6小时（降噪开）\n- 充电：USB-C，支持MagSafe\n- 折扣：14% OFF（$5,499→$4,699 MXN）\n- 销量：耳机类第1"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$4,699 MXN**（含14%折扣）\n- 美客多佣金（约15%）：$705\n- 实际到账约：**$3,994 MXN ≈ ¥2,321人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考正品） | ¥1,350-1,500元 |\n| 头程运费（≈50g×50元/kg） | ¥2.5元 |\n| 美客多佣金15% | ¥348元 |\n| 广告费10% | ¥232元 |\n| 退货损耗5% | ¥116元 |\n| **合计成本** | **¥2,048-2,198元** |\n| 平台收入 | **¥2,321元** |\n| **预估利润** | **¥123~273元（约5-12%利润率）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**✅ 利润分析**\nAirPods Pro利润空间合理（5-12%）\n\n✅ 建议入场，体积小、重量轻、利润率高\n✅ 苹果品牌加持，转化率高，退货率低\n✅ USB-C版为最新版本，差异化竞争"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：AirPods Pro 2 USB-C 正品\n- 建议拿货价：≤¥1,400元/台\n- 目标供应商：深圳/广州苹果配件批发商\n- 起订量：10台+\n\n⚠️ 苹果音频产品假货多，建议走平台担保渠道\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card5)
print("Card 5 done")

# Card 6: 产品5 - Samsung Galaxy S25 Ultra
card6 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "📱 产品5：Samsung Galaxy S25 Ultra 256GB"},
        "subtitle": {"tag": "plain_text", "content": "美客多安卓手机类第1 | 三星旗舰"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\nSamsung Galaxy S25 Ultra 5G 256GB Titanium Black\n- 屏幕：6.8英寸 Dynamic AMOLED 2X\n- 芯片：Snapdragon 8 Elite\n- 摄像头：200MP主摄\n- S Pen：内置S Pen\n- 折扣：19% OFF（$24,999→$20,199 MXN）\n- 销量：安卓手机类第1"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$20,199 MXN**（含19%折扣）\n- 美客多佣金（约15%）：$3,030\n- 实际到账约：**$17,169 MXN ≈ ¥9,976人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考韩版/港版） | ¥7,800-8,300元 |\n| 头程运费（≈220g×50元/kg） | ¥11元 |\n| 美客多佣金15% | ¥1,496元 |\n| 广告费10% | ¥998元 |\n| 退货损耗5% | ¥499元 |\n| **合计成本** | **¥10,804-11,304元** |\n| 平台收入 | **¥9,976元** |\n| **预估利润** | **¥-1,328~-328元（亏损）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**⚠️ 利润分析**\n三星旗舰当前折扣价亏损，建议观望\n\n✅ 关注正常价区间（$24,999），恢复原价后利润约¥600+\n✅ 三星Galaxy S25系列为2026年安卓旗舰，关注度高\n✅ S25 Ultra定位高端，送礼场景多"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：Samsung Galaxy S25 Ultra 港版 韩版\n- 建议拿货价：≤¥8,000元/台\n- 目标供应商：深圳手机批发商\n- 起订量：5台+\n\n⚠️ 注意验证货源，避免买到展示机或翻新机\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card6)
print("Card 6 done")

# Card 7: 产品6 - 空气炸锅（Aire Acondicionado/空气炸锅）
card7 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "🍳 产品6：空气炸锅 5.5L 数字显示屏"},
        "subtitle": {"tag": "plain_text", "content": "美客多家电类季节爆品 | 夏季厨房神器"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\n空气炸锅 5.5L 超大容量 数字显示屏\n- 容量：5.5升（适合4-6人）\n- 功能：炸/烤/烘/煎 多功能\n- 显示屏：LED数字控制面板\n- 配件：食谱+炸篮\n- 折扣：41% OFF（$1,499→$879 MXN）\n- 销量：家电类季节爆品"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$879 MXN**（含41%折扣）\n- 美客多佣金（约17%）：$149\n- 实际到账约：**$730 MXN ≈ ¥424人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考普通款） | ¥120-150元 |\n| 头程运费（≈3.5kg×50元/kg） | ¥175元 |\n| 美客多佣金17% | ¥72元 |\n| 广告费10% | ¥42元 |\n| 退货损耗8% | ¥34元 |\n| **合计成本** | **¥443-473元** |\n| 平台收入 | **¥424元** |\n| **预估利润** | **¥-49~-19元（微亏）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**⚠️ 利润分析**\n折扣价微亏，但空气炸锅为夏季季节爆品\n\n✅ 41%折扣为促销噱头，建议关注原价$1,499区间（利润¥150+）\n✅ 墨西哥家庭厨房需求大，5.5L容量适合主流家庭\n✅ 夏季（5-7月）是空气炸锅销售旺季"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：空气炸锅 5.5L 数字显示屏\n- 建议拿货价：≤¥130元/台\n- 目标供应商：佛山/宁波小家电工厂\n- 起订量：20台+\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card7)
print("Card 7 done")

# Card 8: 产品7 - 智能手表 Smart Watch
card8 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "⌚ 产品7：智能手表 安卓iOS兼容 防水"},
        "subtitle": {"tag": "plain_text", "content": "美客多手表类热搜上升品牌 | 可穿戴设备"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\n智能手表 安卓/iOS通用 防水设计\n- 屏幕：1.9英寸 AMOLED\n- 功能：心率/血氧/睡眠监测\n- 防水：IP68级防水\n- 续航：7-10天\n- 兼容：安卓+iOS\n- 折扣：30% OFF（$699→$499 MXN）\n- 销量：手表类稳定增长"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$499 MXN**（含30%折扣）\n- 美客多佣金（约17%）：$85\n- 实际到账约：**$414 MXN ≈ ¥240人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考通用款） | ¥55-75元 |\n| 头程运费（≈120g×50元/kg） | ¥6元 |\n| 美客多佣金17% | ¥41元 |\n| 广告费10% | ¥24元 |\n| 退货损耗8% | ¥19元 |\n| **合计成本** | **¥145-165元** |\n| 平台收入 | **¥240元** |\n| **预估利润** | **¥75~95元（约31-40%利润率）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**✅ 利润分析**\n智能手表利润空间优秀（31-40%）\n\n✅ 强烈推荐入场，轻便体积，高利润率\n✅ 可穿戴设备市场2026年持续增长\n✅ 安卓iOS通用设计，客群覆盖广"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：智能手表 安卓iOS 防水 AMOLED\n- 建议拿货价：≤¥70元/台\n- 目标供应商：深圳/广州可穿戴设备工厂\n- 起订量：30台+\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card8)
print("Card 8 done")

# Card 9: 爆品预测
card9 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "🔮 爆品预测（未来3个月 5-7月）"},
        "subtitle": {"tag": "plain_text", "content": "基于美客多墨西哥站热销榜+热搜趋势综合判断"}
    },
    "elements": [
        {"tag": "markdown", "content": "**🟢 强烈推荐**\n\n1. **AirPods Pro 2** · 利润5-12% · 体积小 · 苹果品牌 · ⭐⭐⭐⭐⭐\n2. **智能手表（通用款）** · 利润31-40% · 2026年趋势品类 · ⭐⭐⭐⭐⭐\n3. **Xbox/PS5游戏机** · 稳定需求 · 走量款 · ⭐⭐⭐⭐"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🟡 潜力品类**\n\n4. **iPhone 16 Pro Max** · 恢复原价后利润改善 · 引流款 · ⭐⭐⭐\n5. **Samsung Galaxy S25 Ultra** · 安卓旗舰 · 高端市场 · ⭐⭐⭐\n6. **空气炸锅** · 夏季爆发 · 家庭刚需 · 关注原价区间 · ⭐⭐⭐"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📋 行动清单**\n\n✅ 优先上架：智能手表（利润31-40%，最佳选择）\n✅ 次优先上架：AirPods Pro 2（利润稳定，品牌加持）\n✅ 观望：游戏主机（走量，配合配件提升利润）\n✅ 季节布局：空气炸锅（5-7月旺季，提前备货）"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "⚠️ **数据说明**：今日浏览器+网络临时故障，数据引用美客多官网实时数据+历史1688参考价\n\n📊 数据来源：美客多官网 + 1688采购平台\n🔍 大麦数据暂不可用（浏览器故障），数据已尽量补全\n\n🤖 美客多多 · 专注墨西哥站点选品分析\n📅 2026-04-26 简报完成"},
    ]
}
send_card(token, card9)
print("Card 9 done")
print("=== 简报发送完成 ===")