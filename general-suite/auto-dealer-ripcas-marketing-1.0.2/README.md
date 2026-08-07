# 汽车经销商 RIPCAS 中国市场营销增长顾问

## 1. 技能定位

本技能面向中国大陆、香港、澳门的汽车经销商、经销商集团市场部、门店总经理、销售管理者与营销运营团队，帮助用户基于 RIPCAS 增长框架完成营销诊断、月度计划、战役 Brief、内容排期、客户转化话术、销售跟进 SOP 与复盘建议。

RIPCAS 在本技能中指：

- **R - Reach 触达**：目标客群覆盖、渠道选择、首触内容。
- **I - Interest 兴趣**：车型卖点、场景化内容、试驾意向激发。
- **P - Preference 偏好**：金融、置换、服务、品牌与竞品对比。
- **C - Conversion 转化**：到店/进店、试驾、报价、订金、成交。
- **A - Advocacy 口碑**：交车仪式、转介绍、车主内容、社群运营。
- **S - System 系统**：数据看板、销售跟进节奏、复盘机制。

## 2. 中国市场适配范围

技能不再以单一城市为默认前提，而是按“全国通用框架 + 区域参数校准”运行：

| 区域 | 需要重点校准的变量 | 常见渠道/触点 | 常见增长重点 |
|---|---|---|---|
| 中国大陆 | 城市级竞争、限购限行、上牌、区域补贴、厂家金融、置换政策、平台线索质量 | 抖音/快手、小红书、汽车垂媒、本地生活、企微、社群、直播 | 平台获客效率、到店/试驾转化、置换增购、私域培育 |
| 香港 | 右舵车型、停车成本、充电条件、金融保险、跨境/粤港出行、服务体验 | 官方网站、WhatsApp/电话、社交媒体、线下展厅、车主口碑 | 高信任咨询、金融保险解释、试驾体验、售后服务信任 |
| 澳门 | 小城市半径、熟人信任、跨境用车、酒店文旅/企业客户、停车与充电便利性 | 微信/朋友圈、社群、线下展厅、企业客户关系、转介绍 | 转介绍、企业客户、本地口碑、跨境用车场景 |

如用户没有提供所在城市/区域，技能会先询问；如用户要求快速输出，会先使用中国市场通用假设，并标注需要本地校准的内容。

## 3. 两种执行模式

### A. 问题导向模式（推荐，步骤更少）

用户可以先直接提出要解决的问题，技能只运行相关流程，不默认跑全量链路。例如：

- “线索很多但到店率低，帮我诊断并给销售跟进动作。”
- “本月要推新能源 SUV 周末试驾，只需要活动 Brief 和内容排期。”
- “香港门店客户担心停车和充电，帮我写异议处理话术。”
- “澳门企业客户转介绍弱，帮我设计一个轻量转介绍活动。”

问题导向模式会先判断问题属于：触达获客、兴趣激发、偏好建立、销售转化、口碑转介绍、系统复盘中的哪一类，再调用对应模板输出。

### B. 全流程诊断模式

当用户要做月度/季度增长规划、门店经营复盘或新店/新车型系统化打法时，使用完整 RIPCAS 流程，依次完成目标澄清、漏斗诊断、主矛盾定位、区域校准、战役设计、内容排期、销售 SOP 和复盘机制。

## 4. SkillHub 上架信息

技能商店展示文案见 `docs/skillhub-store-listing.md`，包括一句话卖点、技能简介、适用人群、典型场景、示例提示词、能力边界和推荐标签。

## 5. 新增示例与上架评审

- `examples/regional-market-cases.md`：四类区域案例，覆盖大陆一线城市、大陆下沉城市、香港、澳门。
- `docs/skillhub-admission-review.md`：SkillHub 上架准入评审，覆盖名称、描述、触发词、边界、合规、隐私、安装验证和回退检查。
- `docs/installation-validation-report.md`：安装前静态准入校验、可安装性结论和真实安装待验证项。
- `docs/example-regression-test-report.md`：大陆一线、下沉城市、香港、澳门四类示例输入输出回归测试结果。

## 6. 适用场景

- 制定中国大陆、香港、澳门汽车经销商月度/季度营销增长计划。
- 设计新车上市、周末试驾、金融促销、置换增购、车主转介绍等营销战役。
- 诊断线索量、到店/进店率、试驾率、报价率、成交率、复购转介绍等漏斗问题。
- 生成小红书、抖音、朋友圈、企微、社群、WhatsApp/电话邀约等内容和触达排期。
- 为销售顾问提供线索跟进话术、邀约 SOP、异议处理与复盘动作。

## 7. 不适用场景

- 替代法律、财务、税务、金融、保险或广告合规审查。
- 承诺确定销量、利润或广告投放 ROI。
- 未经授权处理客户隐私数据、手机号、身份证、金融资料等敏感信息。
- 直接生成夸大、虚假、误导性促销承诺。

## 8. 技能包结构

```text
auto-dealer-ripcas-marketing/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── examples/
│   └── regional-market-cases.md
├── references/
│   ├── ripcas-framework.md
│   ├── dealer-growth-funnel.md
│   ├── customer-personas.md
│   ├── campaign-playbooks.md
│   └── sales-sop.md
├── templates/
│   ├── campaign-brief-template.md
│   ├── content-calendar-template.md
│   ├── monthly-plan-template.md
│   └── review-report-template.md
├── examples/
│   ├── monthly-marketing-plan.md
│   ├── campaign-brief-example.md
│   ├── content-calendar-example.md
│   ├── sales-followup-script.md
│   └── review-report-example.md
└── docs/
    ├── skillhub-store-listing.md
    ├── input-data-schema.md
    ├── skillhub-release-checklist.md
    ├── installation.md
    ├── validation-report.md
    ├── rollback.md
    ├── skillhub-admission-review.md
    ├── installation-validation-report.md
    └── example-regression-test-report.md
```

## 8. 推荐输入

用户最好提供：

- 门店所在国家/地区、城市/区域、品牌、车型、价格带。
- 当前月度目标：线索、到店/进店、试驾、订单、成交、转介绍。
- 现有漏斗数据与历史活动数据。
- 预算、人手、活动周期、可用渠道。
- 主要客群、竞品、库存与金融/置换政策。
- 区域特殊约束：如大陆限购限行/补贴、香港右舵/停车/充电、澳门跨境/企业客户/本地口碑等。

输入字段规范详见 `docs/input-data-schema.md`。如果信息不足，技能会先补问关键缺口；如用户要求快速输出，会基于显式假设给出可执行初版方案。

## 9. 发布前验证

- 发布检查清单：`docs/skillhub-release-checklist.md`
- 安装说明：`docs/installation.md`
- 验证记录与测试用例：`docs/validation-report.md`
- 回退与停用说明：`docs/rollback.md`

## 10. 版本

当前版本：`1.4.0`。