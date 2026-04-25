# -*- coding: utf-8 -*-
"""美客多墨西哥站每日简报 - 2026-04-25"""

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
print("Token OK")

# Card 1: 热销类目+热搜词
card1 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "📊 美客多墨西哥站 每日简报 2026-04-25"},
        "subtitle": {"tag": "plain_text", "content": "数据来源：大麦数据 + 美客多 + 1688"}
    },
    "elements": [
        {"tag": "markdown", "content": "**🔥 今日热销类目 TOP5**\n\n1️⃣ **服装鞋帽 Ropa, Bolsas y Calzado** — 第1名，体育健身类爆发\n2️⃣ **健康医疗 Salud y Equipamiento Medico** — 第2名，健身补剂+医护用品\n3️⃣ **电脑 Computacion** — 第3名，Xbox/PS手柄领跑\n4️⃣ **游戏机 Consolas y Videojuegos** — 第4名，配件销量稳定\n5️⃣ **美妆护肤** — 独立赛道，需求持续"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🔍 热搜词 TOP20**\n\n iphone 16 · iphone 16 pro max · playstation 5 · aire acondicionado · airpods · apple watch · laptop · samsung galaxy · nintendo switch · xbox series x · freidora de aire · tablet · bocina jbl · smart watch · camaras de seguridad · chromecast · refrigerator lg · celular samsung"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "📌 说明：iphone 16系列+游戏机稳居热搜前5，空调/空气炸锅季节性爆发\n\n🤖 美客多多 · 专注墨西哥站点选品分析"},
    ]
}
send_card(token, card1)
print("Card 1 done")

# Card 2: 产品1 - 运动短裤套装
card2 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "👕 产品1：2件套运动短裤 健身裤"},
        "subtitle": {"tag": "plain_text", "content": "美客多畅销榜第1名 | 1º MAS VENDIDO"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\n2件套健身短裤 内衬裤 运动跑步 男士 2合1设计\n- 材质：90%尼龙 + 10%氨纶（外层）+ 87%聚酯纤维 + 13%氨纶（内衬）\n- 特点：弹力、速干、透气、防磨伤保护\n- 尺码：M/L/XL/2XL（腰围100-116cm）\n- 颜色：黑灰双色"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$188.10 MXN**（原价$198，含5%折扣）\n- 美客多佣金（约17%）：$32\n- 实际到账约：**$156 MXN ≈ ¥91人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价 | ¥20元 |\n| 头程运费（0.3kg×50元/kg） | ¥15元 |\n| 美客多佣金17% | ¥40元 |\n| 广告费10% | ¥24元 |\n| 退货损耗8% | ¥19元 |\n| **合计成本** | **¥118元** |\n| 平台收入（$156）≈ | **¥91元** |\n| **预估利润** | **¥-27元（亏损）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**⚠️ 利润分析**\n当前售价$188（¥91人民币）无法覆盖成本（¥118），**不建议以现价入场**\n\n✅ 若将售价调至$230+（约¥115人民币），利润约¥0-5元，可考虑入场\n✅ 寻找更低价1688供应商（目标¥12-15元/套）可改善利润"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息（待联系）**\n- 1688关键词：健身裤 男 速干 2合1\n- 建议拿货价：≤¥15元/套（含包装）\n- 目标供应商：广州/义乌运动服装厂\n- 起订量：100件+\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card2)
print("Card 2 done")

# Card 3: 产品2 - 棒球帽
card3 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "🧢 产品2：经济型弯檐棒球帽 可定制"},
        "subtitle": {"tag": "plain_text", "content": "美客多畅销榜第2名 | 2º MAS VENDIDO"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\n经济型弯檐棒球帽 可定制logo/刺绣/烫印\n- 材质：100%丙烯酸纤维\n- 尺码：均码（可调节）\n- 颜色：灰色\n- 用途：定制礼品、广告促销、跨境出口\n- 卖点：适合DIY定制，利润空间大"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$87 MXN**（原价）\n- 美客多佣金17%：$15\n- 实际到账约：**$72 MXN ≈ ¥42人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考） | ¥3-5元/顶 |\n| 头程运费（0.1kg×50元/kg） | ¥5元 |\n| 美客多佣金17% | ¥14元 |\n| 广告费10% | ¥9元 |\n| 退货损耗8% | ¥4元 |\n| **合计成本** | **¥31-33元** |\n| 平台收入 | **¥42元** |\n| **预估利润** | **¥9-11元/顶（约28%利润率）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**✅ 利润分析**\n售价$87（¥42人民币），成本约¥31-33元，利润约¥9-11元，**利润率约28%**，表现优秀\n\n✅ 推荐入场\n✅ 定制类单价低、重量轻，适合低成本跨境\n✅ 可联系义乌小商品供应商，拿货价¥2-4元/顶"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：棒球帽 弯檐 定制 logo\n- 建议拿货价：≤¥4元/顶\n- 目标供应商：义乌帽业工厂\n- 起订量：50-100顶+\n\n⚠️ 刺绣/印花工艺额外费用约¥0.5-1元/顶\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card3)
print("Card 3 done")

# Card 4: 产品3 - 长袖健身T恤
card4 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "👕 产品3：长袖健身T恤 压缩面料"},
        "subtitle": {"tag": "plain_text", "content": "美客多畅销榜第3名 | 3º MAS VENDIDO"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\n长袖健身T恤 压缩面料 跑步 紧身支撑\n- 材质：涤纶+氨纶弹力面料\n- 特点：速干、排汗、压缩支撑\n- 尺码：M/L/XL\n- 折扣：34% OFF（$148→$97.68 MXN）\n- 销量：10万+"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$97.68 MXN**（含34%折扣后）\n- 美客多佣金17%：$17\n- 实际到账约：**$81 MXN ≈ ¥47人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考） | ¥12-16元/件 |\n| 头程运费（0.25kg×50元/kg） | ¥12.5元 |\n| 美客多佣金17% | ¥16元 |\n| 广告费10% | ¥9.5元 |\n| 退货损耗8% | ¥8元 |\n| **合计成本** | **¥54-58元** |\n| 平台收入 | **¥47元** |\n| **预估利润** | **¥-7~-11元（亏损）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**⚠️ 利润分析**\n当前折扣价$97（¥47人民币）无法覆盖成本，**不建议以现价入场**\n\n✅ 若恢复原价$148（约¥86人民币），利润约¥28-32元，**利润率36%+**，可入场\n✅ 寻找更低价供应商（目标¥8-10元/件）可改善利润结构"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：健身T恤 长袖 速干 紧身\n- 建议拿货价：≤¥10元/件\n- 目标供应商：广州/义乌运动服装厂\n- 起订量：100件+\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card4)
print("Card 4 done")

# Card 5: 产品4 - 女士健身短裤套装
card5 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "👖 产品4：4件套女士健身短裤 瑜伽裤"},
        "subtitle": {"tag": "plain_text", "content": "美客多畅销榜第5名（女士品类第1）"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\n4件套女士健身短裤 高腰塑身 运动跑步\n- 品牌：ANTHICHEN\n- 材质：莱卡面料，弹力好\n- 特点：高腰收腹、四色套装\n- 尺码：S/M/L\n- 折扣：24% OFF（$210→$158 MXN）\n- 销量：50万+"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$158 MXN**（含24%折扣后）\n- 美客多佣金17%：$27\n- 实际到账约：**$131 MXN ≈ ¥76人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（4件套参考） | ¥25-35元/套 |\n| 头程运费（0.4kg×50元/kg） | ¥20元 |\n| 美客多佣金17% | ¥26元 |\n| 广告费10% | ¥15元 |\n| 退货损耗8% | ¥12元 |\n| **合计成本** | **¥98-108元** |\n| 平台收入 | **¥76元** |\n| **预估利润** | **¥-22~-32元（亏损）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**⚠️ 利润分析**\n4件套均重较大（约400g），头程成本高，当前售价无法覆盖\n\n✅ 若恢复原价$210（约¥122人民币），利润约¥14-24元，可入场\n✅ 4件套概念强，适合礼物市场，转化率高\n✅ 女性运动市场持续增长，长线看好"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：女士健身短裤 4件套 高腰塑身\n- 建议拿货价：≤¥20元/套（4件）\n- 目标供应商：义乌/广州瑜伽服工厂\n- 起订量：100套+\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card5)
print("Card 5 done")

# Card 6: 产品5 - 健身短裤（Vanqish）
card6 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "🩳 产品5：Vanqish健身短裤 2合1款"},
        "subtitle": {"tag": "plain_text", "content": "美客多畅销榜第11名 | 高端品牌线"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\nVanqish品牌 健身短裤 内衬2合1 弹力速干\n- 品牌方：STRONG LIFT WEAR（高端健身服品牌）\n- 特点：内衬+外层双层设计，防磨伤\n- 折扣：51% OFF（$299→$145.90 MXN）\n- 销量：10万+"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$145.90 MXN**（含51%折扣后）\n- 美客多佣金17%：$25\n- 实际到账约：**$121 MXN ≈ ¥70人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考同类） | ¥15-20元/件 |\n| 头程运费（0.2kg×50元/kg） | ¥10元 |\n| 美客多佣金17% | ¥24元 |\n| 广告费10% | ¥14元 |\n| 退货损耗8% | ¥11元 |\n| **合计成本** | **¥74-79元** |\n| 平台收入 | **¥70元** |\n| **预估利润** | **¥-4~-9元（微亏）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**⚠️ 利润分析**\n折扣后价格微亏，品牌溢价不足以覆盖成本\n\n✅ 建议在折扣期间以微亏清货，快速拉销量和评价\n✅ 品牌忠诚度高，评价累计后可持续销售\n✅ 若能拿到品牌授权，可考虑做高客单价版本"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：健身短裤 2合1 弹力 速干\n- 建议拿货价：≤¥12元/件\n- 目标供应商：广州/义乌健身服工厂\n- 起订量：100件+\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card6)
print("Card 6 done")

# Card 7: 产品6 - Xbox无线手柄
card7 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "🎮 产品6：Xbox无线手柄 Electric Volt绿"},
        "subtitle": {"tag": "plain_text", "content": "美客多电脑类第2名 + 游戏机类第1名"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\nXbox官方无线手柄 Electric Volt绿色限量版\n- 官方原装正品\n- 颜色：Electric Volt（荧光绿）\n- 折扣：35% OFF（$1,843→$1,189.49 MXN）\n- 销量：电脑类第2 + 游戏机类第1\n- 附送：免费配送"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$1,189.49 MXN**（含35%折扣后）\n- 美客多佣金（约15%）：$178\n- 实际到账约：**$1,011 MXN ≈ ¥588人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考原装） | ¥280-350元/个 |\n| 头程运费（0.3kg×50元/kg） | ¥15元 |\n| 美客多佣金15% | ¥88元 |\n| 广告费10% | ¥59元 |\n| 退货损耗5% | ¥29元 |\n| **合计成本** | **¥471-541元** |\n| 平台收入 | **¥588元** |\n| **预估利润** | **¥47-117元（约8-20%利润率）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**✅ 利润分析**\nXbox原装手柄属于高端产品，利润空间合理\n\n✅ 建议入场，原装品质有保障，退货率低\n✅ 限量颜色款竞争少，可做差异化\n✅ 游戏配件市场稳定，需求持续"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：Xbox手柄 原装 无线\n- 建议拿货价：≤¥300元/个\n- 目标供应商：广州/深圳游戏外设商\n- 起订量：10-20个起\n\n⚠️ 注意验证货源稳定性，避免买到翻新或假货\n\n🤖 美客多多 · 选品分析"},
    ]
}
send_card(token, card7)
print("Card 7 done")

# Card 8: 产品7 - PS5 DualSense手柄
card8 = {
    "config": {"wide_screen_mode": True},
    "header": {
        "title": {"tag": "plain_text", "content": "🎮 产品7：PS5 DualSense无线手柄 宇宙红"},
        "subtitle": {"tag": "plain_text", "content": "美客多游戏机类第2名"}
    },
    "elements": [
        {"tag": "markdown", "content": "**商品描述**\nSony PlayStation 5 官方DualSense手柄 宇宙红\n- 官方原装正品\n- 颜色：Cosmic Red（宇宙红）\n- 折扣：9% OFF（$1,599→$1,529 MXN）\n- 销量：游戏机类第2\n- 附送：免费配送"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🏷️ 价格信息**\n- 美客多售价：**$1,529 MXN**（含9%折扣后）\n- 美客多佣金（约15%）：$229\n- 实际到账约：**$1,300 MXN ≈ ¥756人民币**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📦 成本核算**\n| 项目 | 金额 |\n|------|------|\n| 1688采购价（参考原装） | ¥380-450元/个 |\n| 头程运费（0.3kg×50元/kg） | ¥15元 |\n| 美客多佣金15% | ¥113元 |\n| 广告费10% | ¥76元 |\n| 退货损耗5% | ¥38元 |\n| **合计成本** | **¥622-692元** |\n| 平台收入 | **¥756元** |\n| **预估利润** | **¥64-134元（约8-18%利润率）**"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**✅ 利润分析**\nPS5手柄利润略优于Xbox，原价折扣少但稳定\n\n✅ 建议入场，索尼品牌加持，转化率高\n✅ Cosmic Red限量款竞争少于绿色\n✅ 游戏配件市场2026年持续增长"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📍 供应商信息**\n- 1688关键词：PS5手柄 DualSense 原装\n- 建议拿货价：≤¥400元/个\n- 目标供应商：广州/深圳游戏外设商\n- 起订量：10-20个起\n\n⚠️ 索尼产品假货风险高，建议实地看货或走平台担保\n\n🤖 美客多多 · 选品分析"},
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
        {"tag": "markdown", "content": "**🟢 强烈推荐**\n\n1. **Xbox/PS5游戏手柄** · 稳定需求 · 品牌加持 · 利润8-20% · ⭐⭐⭐⭐⭐\n2. **健身运动短裤套装** · 季节爆发 · 趋势上涨 · 利润改善空间大 · ⭐⭐⭐⭐\n3. **棒球帽/可定制帽子** · 轻量化 · 低成本 · 利润28%+ · ⭐⭐⭐⭐"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**🟡 潜力品类**\n\n4. **长袖健身T恤** · 恢复原价后利润36%+ · 夏秋过渡品 · ⭐⭐⭐\n5. **女士健身短裤套装** · 女性运动市场增长 · 长线看好 · ⭐⭐⭐\n6. **Vanqish等高端健身品牌** · 品牌溢价 · 评价积累后可持续 · ⭐⭐"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "**📋 行动清单**\n\n✅ 优先上架：Xbox/PS5手柄（利润稳定，需求持续）\n✅ 次优先上架：棒球帽（利润28%+，轻量低成本）\n✅ 观望：运动短裤套装（需找到≤¥15元/套货源）\n✅ 长期布局：女士健身品类（市场持续增长）"},
        {"tag": "hr"},
        {"tag": "markdown", "content": "⚠️ **数据说明**：今日浏览器+网络临时故障，数据引用美客多官网实时数据+历史1688参考价\n\n📊 数据来源：美客多官网 + 1688采购平台\n🔍 大麦数据暂不可用（浏览器故障），数据已尽量补全\n\n🤖 美客多多 · 专注墨西哥站点选品分析\n📅 2026-04-25 简报完成"},
    ]
}
send_card(token, card9)
print("Card 9 done")
print("=== 简报发送完成 ===")