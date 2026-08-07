# 汽车经销商输入数据字段规范

## 1. 目的

本规范用于指导用户在调用技能时提供结构化业务信息，帮助技能稳定生成营销诊断、活动方案、销售承接和复盘报告。

用户无需一次性提供全部字段；但信息越完整，输出越可执行。涉及客户个人信息时，应优先使用汇总数据或脱敏数据。

## 2. 最小可用输入

如果时间有限，至少提供以下 6 类信息：

| 字段 | 示例 | 是否必需 |
| --- | --- | --- |
| 城市/区域 | 上海、深圳、香港、澳门 | 必需 |
| 市场区域 | 中国大陆 / 香港 / 澳门 | 必需 |
| 门店/业务类型 | 4S 店、综合展厅、新能源直营店 | 建议提供 |
| 主推品牌/车型 | 家庭 SUV、新能源轿车、MPV | 必需 |
| 核心目标 | 提升到店、提升试驾、消化库存、置换成交 | 必需 |
| 活动周期 | 下月、两周、周末三天 | 必需 |
| 主要约束 | 预算有限、库存不足、销售人手少 | 建议提供 |

## 3. 基础信息字段

| 字段名 | 说明 | 示例 | 数据类型 |
| --- | --- | --- | --- |
| market_region | 市场区域 | 中国大陆 / 香港 / 澳门 | 枚举 |
| city | 城市或经营区域 | 上海 / 深圳 / 香港 / 澳门 | 文本 |
| currency | 币种 | CNY / HKD / MOP | 枚举 |
| compliance_notes | 当地合规/监管限制 | 价格宣传、金融表述、个人信息授权 | 文本 |
| dealer_type | 经销商类型 | 4S 店 / 综合展厅 / 新能源门店 | 枚举/文本 |
| brand | 品牌 | XX 汽车 | 文本 |
| model | 主推车型 | 家庭 SUV | 文本 |
| campaign_period | 计划周期 | 2026 年 3 月 / 下月 / 周末 | 文本 |
| business_goal | 核心业务目标 | 提升到店和试驾转化 | 文本 |
| budget | 可用预算 | 3 万元 / 预算有限 | 数值/文本 |
| team_capacity | 团队资源 | 市场 2 人、销售 8 人 | 文本 |

## 4. 漏斗数据字段

| 字段名 | 说明 | 示例 | 数据类型 |
| --- | --- | --- | --- |
| impressions | 曝光量 | 100000 | 数值 |
| clicks | 点击量 | 5200 | 数值 |
| inquiries | 咨询量 | 850 | 数值 |
| leads | 留资量 | 320 | 数值 |
| valid_leads | 有效线索 | 210 | 数值 |
| appointments | 预约到店 | 95 | 数值 |
| visits | 实际到店 | 68 | 数值 |
| test_drives | 试驾 | 42 | 数值 |
| quotes | 报价 | 35 | 数值 |
| orders | 订单/订金 | 16 | 数值 |
| deliveries | 交付/成交 | 13 | 数值 |
| channel_cost | 渠道花费 | 20000 | 数值 |
| revenue_or_gross_profit | 销售额或毛利，可选 | 180000 | 数值 |

## 5. 渠道数据字段

| 字段名 | 说明 | 示例 |
| --- | --- | --- |
| channel_name | 渠道名称 | 抖音 / 小红书 / 视频号 / 微信生态 / WhatsApp / Instagram / Facebook / 老客户转介绍 |
| channel_goal | 渠道目标 | 拉新 / 留资 / 预约 / 复购 |
| channel_budget | 渠道预算 | 8000 |
| channel_leads | 渠道线索 | 120 |
| channel_visits | 渠道到店 | 28 |
| channel_orders | 渠道成交 | 5 |
| content_type | 内容形式 | 短视频 / 图文 / 直播 / 海报 / 电话邀约 |
| cta | 行动召唤 | 预约试驾 / 领取报价 / 到店评估旧车 |

## 6. 客群字段

| 字段名 | 说明 | 示例 |
| --- | --- | --- |
| target_segment | 目标客群 | 家庭首购 / 置换增购 / 新能源尝鲜 / 商务接待 |
| age_range | 年龄段 | 30-45 岁 |
| usage_scenario | 用车场景 | 通勤、接送孩子、周末出游 |
| budget_range | 预算区间 | 20-30 万 |
| decision_factors | 决策因素 | 空间、安全、月供、售后便利 |
| objections | 常见异议 | 价格高、续航焦虑、等待竞品优惠 |

## 7. 销售承接字段

| 字段名 | 说明 | 示例 |
| --- | --- | --- |
| first_response_time | 首响时间 | 5 分钟 / 30 分钟 / 当天 |
| followup_frequency | 跟进频次 | 3 天 3 次 / 每周一次 |
| lead_grade | 线索等级 | A/B/C 或 高/中/低意向 |
| visit_barrier | 未到店原因 | 时间不合适、距离远、价格不清楚 |
| test_drive_barrier | 未试驾原因 | 没时间、车型不在店、路线安排差 |
| deal_barrier | 未成交原因 | 价格、金融、竞品、家人未决策 |
| next_action | 下一步动作 | 二次邀约、发送报价、置换评估 |

## 8. 销售政策字段

| 字段名 | 说明 | 示例 |
| --- | --- | --- |
| inventory_status | 库存情况 | 现车充足 / 指定颜色缺货 |
| price_policy | 价格政策 | 门店审批价，以实际确认为准 |
| finance_policy | 金融政策 | 首付 30%、36 期，需审批 |
| trade_in_policy | 置换政策 | 旧车评估 + 置换补贴 |
| aftersales_benefits | 售后权益 | 免费检测、保养券、延保 |
| campaign_offer | 活动权益 | 到店礼、试驾礼、交车礼 |

## 9. 复盘字段

| 字段名 | 说明 | 示例 |
| --- | --- | --- |
| campaign_name | 活动名称 | 周末家庭试驾日 |
| planned_goal | 原目标 | 到店 35、试驾 25、成交 8 |
| actual_result | 实际结果 | 到店 28、试驾 22、成交 5 |
| best_channel | 表现最好渠道 | 短视频 |
| weak_stage | 最弱环节 | 预约到实际到店 |
| key_learning | 关键经验 | 家庭场景内容优于参数内容 |
| next_optimization | 下次优化 | 加强活动前确认和金融方案表达 |

## 10. 推荐输入模板

```yaml
market_region: 中国大陆
city: 深圳
currency: CNY
compliance_notes: 金融政策、补贴和价格表述以当地法规及门店审批口径为准
dealer_type: 4S 店
brand: XX 汽车
model: 家庭 SUV
campaign_period: 下月
business_goal: 提升到店和试驾转化
budget: 30000
team_capacity: 市场 2 人，销售 8 人
main_constraints:
  - 预算有限
  - 周末展厅接待能力有限
funnel_data:
  leads: 320
  valid_leads: 210
  visits: 68
  test_drives: 42
  orders: 16
channels:
  - channel_name: 短视频
    channel_budget: 12000
    channel_leads: 140
    channel_visits: 30
  - channel_name: 老客户转介绍
    channel_budget: 3000
    channel_leads: 45
    channel_visits: 18
target_segment:
  - 家庭首购
  - 置换增购
sales_policy:
  finance_policy: 以门店审批为准
  trade_in_policy: 提供旧车评估和置换补贴
```

## 11. 数据质量要求

1. 能用真实数据时，优先使用真实汇总数据。
2. 数据缺失时，可以写“未知”，不要编造。
3. 同一指标需保持口径一致，例如“订单”是否包含订金。
4. 金额、预算、补贴、金融政策应注明币种和适用条件。
5. 涉及客户隐私时，应脱敏或汇总，不输入身份证号、银行卡号、完整手机号等敏感信息。

## 12. 输出映射关系

| 输入信息 | 主要影响的输出 |
| --- | --- |
| 主推车型、客群、目标 | 战役主题、内容方向、销售话术 |
| 漏斗数据 | RIPCAS 诊断、主矛盾识别、指标目标 |
| 渠道数据 | 渠道组合、预算分配、ROI 复盘 |
| 销售政策 | 报价话术、置换方案、金融说明 |
| 约束条件 | 优先级、节奏安排、风险提示 |
