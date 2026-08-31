# SKILL 盘点表（Registry）

> ⚠️ **历史快照 · 非实时注册表**
> 本文件生成于 **2026-06-25**，采用旧版 P1–P6+CX 模型与 1–139 顺序数字编号，且**未反映后续治理体系演进**（pd-/pm- suite 拆分、PT/JT/S 轨道编号、insight-extraction 等最新增改均不在其中）。
> **实时权威注册表请以 `C:\Users\Lee\.workbuddy\skills\SKILL-ID-REGISTRY.md` 为准**（当前 v1.1.1）。本文件仅作全量技能字段的**参考台账**保留，请勿据此做路由 / 编号 / 衔接决策。
>

> 此文件是 SKILL 治理体系的核心索引。
> 共收录 139 个 Skill（含 2 个 PT-P6 Skill + 1 个 data-analyst），按 P1-P6 + CX 阶段模型分组，每个 Skill 已拆解为统一的标准化字段。
> 阶段模型：P1 识别 → P2 论证 → P3 规划 → P4 执行 → P5 控制 → P6 复盘 + CX 专业知识域
> 框架基础：[STANDARDS_FRAMEWORK.md](STANDARDS_FRAMEWORK.md)（PMP + NPDP + 一建 三标准融合）
> 双轨模型：PT（产品轨 / Product Track）| JT（项目轨 / Project Track）| S（共用层 / Shared）
> 双向引用：已部署 Skill 的统一编号映射见 [DEPLOYED_MAPPING.md](DEPLOYED_MAPPING.md)
> 更新时间：2026-06-25

## 盘点总览

| 维度 | 统计 |
|------|------|
| Skill 总数 | 139 |
| P1 - 识别（问题发现/用户研究/市场机会） | 25 |
| P2 - 论证（评估/比较/商业论证/策略分析） | 31 |
| P3 - 规划（计划/优先级/范围/PRD/Backlog） | 3 |
| P4 - 执行（生成文档/执行任务/产出交付物） | 36 |
| P5 - 控制（度量/测试/监控/A-B实验/指标） | 13 |
| P6 - 复盘（回顾/经验教训/知识沉淀） | 4 |
| CX - 专业知识域（独立归属） | 28 |

### 双轨分布总览

| 轨道 | 说明 | Skill 数 |
|------|------|---------|
| PT（产品轨） | 产品创新、市场研究、产品战略与生命周期（NPDP驱动） | 51 |
| JT（项目轨） | 项目交付、建设管理、合规法务（PMP + 一建驱动） | 13 |
| S（共用层） | 双轨共用：需求/优先级/度量/干系人/Agent工具/知识库/数据分析 | 75 |

### CX 专业知识域分布

> "独立 Skill" 指以 CX 子域为主阶段的 Skill；"跨域出现" 指以 P1-P6 为主阶段、但该 CX 子域作为知识跨域被引用的 Skill。

| 子域 | 独立Skill数 | 跨域出现 | 说明 |
|------|------------|---------|------|
| CX-1 法律合规 | 2 | P4×5 | 法律/合规/合同/隐私 |
| CX-2 工程经济 | 0 | P2×5, CX-1×1 | 财务/投资/定价/ROI（全部作为跨域） |
| CX-3 市场研究方法 | 0 | P1×4 | 调研方法论/ICP/画像（全部作为跨域） |
| CX-4 产品战略组合 | 0 | P1×3, P2×7 | 战略框架/北极星/画布（全部作为跨域） |
| CX-5 组织干系人 | 0 | P3×1, P4×2, P1×1 | 团队/干系人/组织协作（全部作为跨域） |
| CX-6 数据度量方法 | 1 | P5×5, P2×1, P1×1 | data-analyst（独立）+ 指标/实验统计（跨域） |
| CX-7 行业领域知识 | 3 | P4×9, P2×1, P1×2, P6×1 | 行业/垂直领域专业知识 |
| CX-8 Agent/Skill工具 | 22 | P4×3, P6×1 | 系统工具/Agent/Skill/方法论 |

---

## 一、P1 - 识别（问题发现 / 用户研究 / 市场机会）

> 25 个 Skill | 核心职责：发现与定义问题、识别用户需求和市场机会

| # | SKILL名称 | 来源位置 | 一句话描述 | 问题类型(主) | 问题类型(副) | 触发信号词 | 隐性前提 | 输出形态 | 关系类型 | 阶段 | 轨道 | 跨域 | 成熟度 |
|---|-----------|---------|-----------|-------------|-------------|-----------|---------|---------|------|------|------|--------|
| 71 | polymarket | 其他/polymarket | 查询Polymarket预测市场赔率与趋势 | RESEARCH_ANALYSIS | LIFE_MANAGEMENT | "查赔率""预测市场" | 需python3环境 | 市场数据/观察列表 | ✅核心 ✅ 核心 | | P1 | PT | ✅核心 ✅ 核心 | | CX-3 | 试验 |
| 101 | thesis-topic-selector | 学术技能 | 四种AI模式为任意学科生成创新选题 | RESEARCH_ANALYSIS | EDUCATION | "选题""研究方向""论文题目" | 已确定学科领域 | 结构化选题方案 | ✅核心 ✅ 核心 | | P1 | S | — | 稳定 |
| 24 | beachhead-segment | pm-go-to-market | 识别产品首发滩头市场细分 | MARKET_CONFUSION | BUSINESS_MODEL | "滩头市场""首批客户" | 已有产品描述/市场研究 | 细分评分报告+90天计划 | ✅核心 ✅ 核心 | | P1 | PT | ✅核心 ✅ 核心 | | CX-3 | 稳定 |
| 29 | ideal-customer-profile | pm-go-to-market | 从研究数据定义理想客户画像ICP | MARKET_CONFUSION | USER_JOURNEY_FRICTION | "ICP""理想客户""客户画像" | 已有PMF调研/使用数据 | ICP定义文档+JTBD映射 | ✅核心 ✅ 核心 | | P1 | PT | ✅核心 ✅ 核心 | | CX-3 | 稳定 |
| 30 | competitor-analysis | pm-market-research | 竞争格局分析：5家竞品优劣势 | MARKET_CONFUSION | RESEARCH_ANALYSIS | "竞品分析""竞争格局" | 已有产品/市场/行业上下文 | 竞品分析报告+定位建议 | ✅核心 ✅ 核心 | | P1 | PT | — | 核心 |
| 31 | customer-journey-map | pm-market-research | 端到端客户旅程地图 | USER_JOURNEY_FRICTION | RESEARCH_ANALYSIS | "客户旅程""旅程地图" | 已有用户访谈/客服工单数据 | 旅程地图表格+改进建议 | ✅核心 ✅ 核心 | | P1 | PT | — | 稳定 |
| 32 | market-segments | pm-market-research | 识别3-5个客户细分含JTBD | MARKET_CONFUSION | PROBLEM_UNCLEAR | "市场细分""目标客户" | 已有产品/市场研究数据 | 细分分析报告+匹配评估 | ✅核心 ✅ 核心 | | P1 | PT | — | 稳定 |
| 33 | market-sizing | pm-market-research | TAM/SAM/SOM市场规模估算 | MARKET_CONFUSION | RESEARCH_ANALYSIS | "市场规模""TAM""SAM" | 已有产品/行业边界信息 | 市场规模报告+假设风险表 | ✅核心 ✅ 核心 | | P1 | PT | — | 核心 |
| 35 | user-personas | pm-market-research | 从研究数据生成含JTBD的用户画像 | RESEARCH_ANALYSIS | USER_JOURNEY_FRICTION | "用户画像""用户档案" | 已提供调研数据 | 结构化画像卡片(3个) | ✅核心 ✅ 核心 | | P1 | PT | — | 稳定 |
| 36 | user-segmentation | pm-market-research | 从反馈数据识别用户分群 | RESEARCH_ANALYSIS | MARKET_CONFUSION | "用户分群""行为聚类" | 已提供用户反馈或行为数据 | 分群档案+优先级 | ✅核心 ✅ 核心 | | P1 | PT | — | 稳定 |
| 38 | north-star-metric | pm-marketing-growth | 定义北极星指标及输入指标体系 | METRICS_CONFUSION | BUSINESS_MODEL | "北极星指标""OMTM" | 已提供商业模式及业务背景 | 指标框架+验证 | ✅核心 ✅ 核心 | | P1 | S | CX-4, CX-6 | 稳定 |
| 42 | analyze-feature-requests | pm-product-discovery | 分类评估并优先排序功能需求 | PRIORITY_MUD | SCOPE_CREEP | "功能需求""需求分析" | 已提供产品目标及需求列表 | 主题分类+Top3详析 | ✅核心 ✅ 核心 | | P1 | S | — | 稳定 |
| 47 | identify-assumptions-existing | pm-product-discovery | 识别已有产品功能的四类风险假设 | EXPERIMENT_NEEDED | SCOPE_CREEP | "风险假设""假设识别" | 已提供功能想法及产品背景 | 假设+置信度+测试方法 | ✅核心 ✅ 核心 | | P1 | PT | — | 稳定 |
| 48 | identify-assumptions-new | pm-product-discovery | 识别新产品8大类别风险假设 | EXPERIMENT_NEEDED | BUSINESS_MODEL | "新产品风险""假设地图" | 已提供新产品概念及目标市场 | 8类假设+置信度+测试方法 | ✅核心 ✅ 核心 | | P1 | PT | — | 稳定 |
| 49 | interview-script | pm-product-discovery | 创建遵循Mom Test的客户访谈脚本 | RESEARCH_ANALYSIS | USER_JOURNEY_FRICTION | "访谈脚本""用户访谈" | 已提供研究目标及产品背景 | 脚本+笔记模板 | ✅核心 ✅ 核心 | | P1 | PT | ✅核心 ✅ 核心 | | CX-3 | 稳定 |
| 51 | opportunity-solution-tree | pm-product-discovery | 构建机会→方案→实验的发现树 | WORKFLOW_OPTIMIZATION | PRIORITY_MUD | "机会方案树""OST""发现框架" | 已提供目标指标及客户调研 | 四层树状图 | ✅核心 ✅ 核心 | | P1 | PT | ✅核心 ✅ 核心 | | CX-4 | 核心 |
| 54 | summarize-interview | pm-product-discovery | 将访谈转录结构化为JTBD与行动项 | RESEARCH_ANALYSIS | DELIVERY_WRITING | "访谈总结""转录分析" | 已提供访谈转录文件 | 结构化摘要模板 | ✅核心 ✅ 核心 | | P1 | PT | — | 稳定 |
| 59 | pestle-analysis | pm-product-strategy | 分析政治/经济/社会/技术/法律/环境 | MARKET_CONFUSION | LEGAL_COMPLIANCE | "PESTLE分析""宏观环境" | 已提供行业及地理市场信息 | 六维分析+战略响应 | ✅核心 ✅ 核心 | | P1 | PT | CX-7, CX-1 | 稳定 |
| 60 | porters-five-forces | pm-product-strategy | 波特五力分析行业竞争结构 | MARKET_CONFUSION | BUSINESS_MODEL | "波特五力""行业分析" | 已提供行业定义及竞争信息 | 五力评估+战略建议 | ✅核心 ✅ 核心 | | P1 | PT | ✅核心 ✅ 核心 | | CX-7 | 稳定 |
| 65 | swot-analysis | pm-product-strategy | SWOT分析优势/劣势/机会/威胁 | MARKET_CONFUSION | VALUE_PROP_BLUR | "SWOT分析""优劣势" | 已提供产品现状及竞争信息 | 四象限+战略建议 | ✅核心 ✅ 核心 | | P1 | PT | ✅核心 ✅ 核心 | | CX-4 | 核心 |
| 75 | fwsjtt-chief-consultant | 服务设计专家团 | 澄清复杂任务北极星目标与拆解问题 | PROBLEM_UNCLEAR | SCOPE_CREEP | "帮我澄清目标""拆解任务" | 业务背景、期望交付物、约束 | 北极星目标+问题拆解+路径 | ✅核心 ✅ 核心 | | P1 | PT | — | 核心 |
| 76 | fwsjtt-customer-discovery | 服务设计专家团 | 用JTBD与访谈证据识别客户真实需求 | USER_JOURNEY_FRICTION | EXPERIMENT_NEEDED | "设计客户访谈""验证需求" | 业务背景、目标客户、已有反馈 | 访谈提纲+JTBD卡+证据图 | ✅核心 ✅ 核心 | | P1 | PT | — | 核心 |
| 82 | fwsjtt-service-designer | 服务设计专家团 | 诊断用户旅程与服务蓝图 | USER_JOURNEY_FRICTION | EXPERIMENT_NEEDED | "梳理用户旅程""服务蓝图" | 目标用户、当前服务流程 | 旅程图+服务蓝图+实验方案 | ✅核心 ✅ 核心 | | P1 | PT | — | 核心 |
| 111 | domain-elimination-assessor | 生产技能 | 评估领域是否应被消除而非优化 | WORKFLOW_OPTIMIZATION | SCOPE_CREEP | "领域消除""存在必要性" | 有待评估的业务/技术模块 | 消除/重构/保留决策 | ✅核心 ✅ 核心 | | P1 | S | — | 稳定 |
| 70 | review-resume | pm-toolkit | 按10项最佳实践评审PM简历 | LIFE_MANAGEMENT | CONTENT_CREATION | "帮我改简历""PM简历评审" | 简历文本，可选目标JD | 逐条评审反馈报告 | ✅核心 ✅ 核心 | | P1 | S | ✅核心 ✅ 核心 | | CX-5 | 稳定 |

> 注：review-resume 核心动作为"识别"简历问题与改进点，归入P1；跨域CX-5因其涉及职业/组织场景。
> 注：domain-elimination-assessor 核心动作为"识别"领域存在必要性，归入P1。
> 注：fwsjtt-service-designer 主归P1（旅程诊断），其蓝图规划侧面在P3附录中引用。
> 注：opportunity-solution-tree 主归P1（机会识别），其方案规划侧面在P3附录中引用。

---

## 二、P2 - 论证（评估 / 比较 / 商业论证 / 策略分析）

> 31 个 Skill | 核心职责：评估方案、比较选项、构建商业论证

| # | SKILL名称 | 来源位置 | 一句话描述 | 问题类型(主) | 问题类型(副) | 触发信号词 | 隐性前提 | 输出形态 | 关系类型 | 阶段 | 轨道 | 跨域 | 成熟度 |
|---|-----------|---------|-----------|-------------|-------------|-----------|---------|---------|------|------|------|--------|
| 72 | product-solution-evaluator | 其他/product-solution-evaluator | 对产品方案做结构化评估与推进决策 | VALUE_PROP_BLUR | EXPERIMENT_NEEDED | "评估产品方案""方案评审" | 方案名称/目标用户/问题描述/目标指标 | 评分表+评估报告+MVP建议 | ✅核心 ✅ 核心 | | P2 | PT | — | 核心 |
| 2 | auto-dealer-ripcas-marketing | 其他/auto-dealer | 汽车经销商营销转化诊断与增长方案 | BUSINESS_MODEL | USER_JOURNEY_FRICTION | "经销商营销""4S店获客" | 品牌/车型/目标客群/漏斗数据 | 营销计划/Brief/话术/SOP | ✅核心 ✅ 核心 | | P2 | PT | ✅核心 ✅ 核心 | | CX-7 | 稳定 |
| 25 | competitive-battlecard | pm-go-to-market | 销售竞争战术卡：对比/异议/赢单 | MARKET_CONFUSION | VALUE_PROP_BLUR | "竞品战术卡""battlecard" | 已有明确竞争对手 | 竞争战术卡文档 | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |
| 26 | growth-loops | pm-go-to-market | 识别5种增长飞轮 | BUSINESS_MODEL | USER_JOURNEY_FRICTION | "增长飞轮""growth loop" | 已有产品描述/增长数据 | 增长循环分析+路线图 | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |
| 27 | gtm-motions | pm-go-to-market | 评估7种GTM动作 | BUSINESS_MODEL | MARKET_CONFUSION | "GTM动作""PLG""ABM" | 已有产品/定价/团队信息 | GTM评分+组合+90天计划 | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |
| 28 | gtm-strategy | pm-go-to-market | 综合GTM战略：渠道/信息/指标/时间线 | BUSINESS_MODEL | MARKET_CONFUSION | "GTM战略""上市计划" | 已有产品/目标市场/预算 | GTM战略文档+KPI框架 | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |
| 37 | marketing-ideas | pm-marketing-growth | 生成5个低成本创意营销方案 | CONTENT_CREATION | MARKET_CONFUSION | "营销创意""推广方案" | 已提供产品及目标市场 | 创意清单(5个含渠道与理由) | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |
| 39 | positioning-ideas | pm-marketing-growth | 生成差异化产品定位方案 | MARKET_CONFUSION | VALUE_PROP_BLUR | "产品定位""差异化" | 已提供产品、市场及竞品信息 | 定位方案+竞争分析(5个) | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |
| 40 | product-name | pm-marketing-growth | 产品头脑风暴5个独特名称 | CONTENT_CREATION | MARKET_CONFUSION | "产品命名""品牌名""起名" | 已提供品牌调性及目标受众 | 名称清单(5个+域名考量) | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |
| 45 | brainstorm-ideas-existing | pm-product-discovery | 从PM/设计/工程视角脑暴产品创意 | WORKFLOW_OPTIMIZATION | SCOPE_CREEP | "产品创意""头脑风暴" | 已提供产品、目标及机会领域 | 15+创意→Top5详析 | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |
| 46 | brainstorm-ideas-new | pm-product-discovery | 新产品初始发现期多视角功能脑暴 | WORKFLOW_OPTIMIZATION | EXPERIMENT_NEEDED | "新产品创意""初始发现" | 已提供新产品概念及目标市场 | 15+创意→Top5详析 | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |
| 53 | prioritize-features | pm-product-discovery | 按影响力/工作量/风险排序功能 | PRIORITY_MUD | SCOPE_CREEP | "功能排序""Backlog优先级" | 已提供产品目标及功能列表 | Top5排序+理由+取舍 | ✅核心 ✅ 核心 | | P2 | S | — | 稳定 |
| 55 | ansoff-matrix | pm-product-strategy | 安索夫矩阵分析四象限增长策略 | BUSINESS_MODEL | MARKET_CONFUSION | "安索夫矩阵""增长策略" | 已提供当前产品/市场及增长目标 | 四象限分析+路线图 | ✅核心 ✅ 核心 | | P2 | PT | ✅核心 ✅ 核心 | | CX-4 | 稳定 |
| 56 | business-model | pm-product-strategy | 生成9模块商业模式画布 | BUSINESS_MODEL | VALUE_PROP_BLUR | "商业模式画布""BMC" | 已提供产品/服务及市场背景 | 9模块BMC | ✅核心 ✅ 核心 | | P2 | PT | ✅核心 ✅ 核心 | | CX-4 | 核心 |
| 57 | lean-canvas | pm-product-strategy | 生成精益画布验证创业假设 | BUSINESS_MODEL | EXPERIMENT_NEEDED | "精益画布""Lean Canvas" | 已提供产品概念及目标市场 | 9模块Lean Canvas | ✅核心 ✅ 核心 | | P2 | PT | ✅核心 ✅ 核心 | | CX-4 | 稳定 |
| 58 | monetization-strategy | pm-product-strategy | 脑暴3-5种变现策略含验证实验 | BUSINESS_MODEL | EXPERIMENT_NEEDED | "变现策略""收入模型" | 已提供产品描述及目标市场 | 策略对比+实验方案 | ✅核心 ✅ 核心 | | P2 | PT | ✅核心 ✅ 核心 | | CX-2 | 稳定 |
| 61 | pricing-strategy | pm-product-strategy | 设计定价模型与价格弹性 | BUSINESS_MODEL | VALUE_PROP_BLUR | "定价策略""价格模型" | 已提供产品价值及竞品定价 | 定价推荐表+实验计划 | ✅核心 ✅ 核心 | | P2 | PT | ✅核心 ✅ 核心 | | CX-2 | 稳定 |
| 62 | product-strategy | pm-product-strategy | 9模块产品战略画布制定完整战略 | VALUE_PROP_BLUR | BUSINESS_MODEL | "产品战略""战略画布" | 已提供产品、市场及竞争背景 | 9模块战略画布 | ✅核心 ✅ 核心 | | P2 | PT | ✅核心 ✅ 核心 | | CX-4 | 核心 |
| 63 | product-vision | pm-product-strategy | 创建鼓舞人心的产品愿景 | VALUE_PROP_BLUR | CONTENT_CREATION | "产品愿景""愿景声明" | 已提供公司及产品背景 | 3-5个愿景选项+推荐 | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |
| 64 | startup-canvas | pm-product-strategy | 新产品专用画布：战略+商业模式 | BUSINESS_MODEL | VALUE_PROP_BLUR | "创业画布""新产品战略" | 已提供创业想法及市场背景 | 11模块完整画布 | ✅核心 ✅ 核心 | | P2 | PT | ✅核心 ✅ 核心 | | CX-4 | 稳定 |
| 66 | value-proposition | pm-product-strategy | 6步JTBD模板设计价值主张 | VALUE_PROP_BLUR | MARKET_CONFUSION | "价值主张""JTBD价值图" | 已提供产品、目标客户及竞品 | 6步模板+定位声明 | ✅核心 ✅ 核心 | | P2 | PT | — | 核心 |
| 80 | fwsjtt-metrics-architect | 服务设计专家团 | 设计北极星指标、指标树与测量计划 | METRICS_CONFUSION | SYSTEM_DESIGN | "设计指标体系""北极星指标" | 业务目标、用户行为链路 | 指标树+口径定义+测量计划 | ✅核心 ✅ 核心 | | P2 | S | ✅核心 ✅ 核心 | | CX-6 | 核心 |
| 81 | fwsjtt-roi-strategist | 服务设计专家团 | 在数据约束下评估ROI和商值 | BUSINESS_MODEL | METRICS_CONFUSION | "算ROI""投入产出" | 项目投入/成本/收益数据 | ROI测算框架+情景分析 | ✅核心 ✅ 核心 | | P2 | PT | ✅核心 ✅ 核心 | | CX-2 | 核心 |
| 83 | fwsjtt-strategy-growth-advisor | 服务设计专家团 | 诊断战略增长瓶颈与竞争定位 | BUSINESS_MODEL | SCOPE_CREEP | "增长卡在哪""战略诊断" | 业务目标、市场/竞品、资源约束 | 战略诊断报告+90天验证计划 | ✅核心 ✅ 核心 | | P2 | PT | ✅核心 ✅ 核心 | | CX-4 | 核心 |
| 110 | compose-methods | 生产技能 | 清单法与样本法两种内容构成范式 | DELIVERY_WRITING | CONTENT_CREATION | "清单法""样本法" | 需要生成结构化内容 | 清单或样本驱动成品 | ✅核心 ✅ 核心 | | P2 | S | — | 稳定 |
| 112 | innovation-os | 生产技能 | 四种模式驱动的全领域创新操作系统 | EXPERIMENT_NEEDED | RESEARCH_ANALYSIS | "创新""突破""第一性原理" | 需要突破性创新方案 | 创新方案与维度矩阵 | ✅核心 ✅ 核心 | | P2 | S | — | 稳定 |
| 118 | workflow-refactor | 生产技能 | 三步法将传统工作流重构为AI一人完成 | WORKFLOW_OPTIMIZATION | SCOPE_CREEP | "工作流重构""流程简化" | 有复杂多人多环节工作流 | IPO基元链重构报告 | ✅核心 ✅ 核心 | | P2 | S | — | 核心 |
| 121 | solopreneur-os | 生活技能 | AI赋能一人公司全周期操作系统 | BUSINESS_MODEL | WORKFLOW_OPTIMIZATION | "一人公司""超级个体" | 想以一人模式开展商业 | 商业方案+合规+工作流 | ✅核心 ✅ 核心 | | P2 | PT | CX-4, CX-2 | 核心 |
| 122 | wealth-manager | 生活技能 | 财富积累→增值→保全→传承四阶段 | BUSINESS_MODEL | LIFE_MANAGEMENT | "投资策略""财富规划" | 需要系统化财富管理 | 四阶段方案+风控纪律 | ✅核心 ✅ 核心 | | P2 | S | ✅核心 ✅ 核心 | | CX-2 | 稳定 |
| 15 | prioritization-frameworks | pm-execution | 9种优先级框架参考指南 | PRIORITY_MUD | PROBLEM_UNCLEAR | "优先级框架""RICE""ICE" | 已有待排序的需求列表 | 框架对比表/评分模板 | ✅核心 ✅ 核心 | | P2 | S | — | 核心 |
| 13 | outcome-roadmap | pm-execution | 功能列表路线图改写为结果导向路线图 | VALUE_PROP_BLUR | SCOPE_CREEP | "结果路线图""战略路线图" | 已有output型路线图 | 结果导向路线图文档 | ✅核心 ✅ 核心 | | P2 | PT | — | 稳定 |

---

## 三、P3 - 规划（计划 / 优先级 / 范围 / PRD / Backlog）

> 3 个 Skill（独立归属）| 核心职责：制定计划、确定优先级、定义范围与Backlog

| # | SKILL名称 | 来源位置 | 一句话描述 | 问题类型(主) | 问题类型(副) | 触发信号词 | 隐性前提 | 输出形态 | 关系类型 | 阶段 | 轨道 | 跨域 | 成熟度 |
|---|-----------|---------|-----------|-------------|-------------|-----------|---------|---------|------|------|------|--------|
| 9 | brainstorm-okrs | pm-execution | 生成对齐战略的团队级OKR三套方案 | PRIORITY_MUD | SCOPE_CREEP | "写OKR""季度目标" | 已有公司战略/团队职责 | OKR文档（3套方案） | ✅核心 ✅ 核心 | | P3 | S | — | 稳定 |
| 18 | sprint-plan | pm-execution | Sprint容量估算与Story选取 | WORKFLOW_OPTIMIZATION | SCOPE_CREEP | "sprint计划""迭代规划" | 已有Backlog/速率数据 | Sprint计划摘要+风险表 | ✅核心 ✅ 核心 | | P3 | JT | — | 稳定 |
| 19 | stakeholder-map | pm-execution | 权力/利益方格干系人映射 | AGENT_ORCHESTRATION | DELIVERY_WRITING | "干系人""stakeholder" | 已有项目/产品/团队上下文 | 干系人矩阵+沟通计划 | ✅核心 ✅ 核心 | | P3 | S | ✅核心 ✅ 核心 | | CX-5 | 稳定 |

> 注：以下 Skill 主归属其他阶段，但规划侧面显著，在P3有交叉引用：
> - #82 fwsjtt-service-designer（主P1-旅程诊断 → P3-服务蓝图规划）
> - #51 opportunity-solution-tree（主P1-机会识别 → P3-方案→实验规划）

---

## 四、P4 - 执行（生成文档 / 执行任务 / 产出交付物）

> 36 个 Skill | 核心职责：产出交付物、执行具体任务、生成内容

| # | SKILL名称 | 来源位置 | 一句话描述 | 问题类型(主) | 问题类型(副) | 触发信号词 | 隐性前提 | 输出形态 | 关系类型 | 阶段 | 轨道 | 跨域 | 成熟度 |
|---|-----------|---------|-----------|-------------|-------------|-----------|---------|---------|------|------|------|--------|
| 5 | liurun-writing-assistant | 其他/liurun-writing | 参考刘润风格的商业洞察文章写作 | CONTENT_CREATION | DELIVERY_WRITING | "刘润写作""商业洞察文章" | 已有主题/观点/草稿/素材 | 文章/大纲/改写版本 | ✅核心 ✅ 核心 | | P4 | S | — | 稳定 |
| 87 | tech-doc-writer | 其他/技术文档写作助手 | 基于素材按大纲生成技术文档并评审 | DELIVERY_WRITING | BIDDING_PROCUREMENT | "按大纲写文档""技术方案" | 参考文档目录、大纲/模板 | Markdown文档+评审报告 | ✅核心 ✅ 核心 | | P4 | JT | — | 稳定 |
| 88 | bidding-assistant | 其他/招投标全流程助手 | 从招标资料解析到投标文件生成全流程 | BIDDING_PROCUREMENT | DELIVERY_WRITING | "解析招标文件""生成投标文件" | 招标.docx文件、公司介绍 | 解析报告+投标方案+.docx文件 | ✅核心 ✅ 核心 | | P4 | JT | ✅核心 ✅ 核心 | | CX-7 | 稳定 |
| 89 | bid-assistant | 其他/招投标助手 | 覆盖招投标11大场景的全流程助手 | BIDDING_PROCUREMENT | DELIVERY_WRITING | "招标机会识别""标书审查" | 招标文件、公司素材、知识库 | 机会摘要+评分模型+章节初稿 | ✅核心 ✅ 核心 | | P4 | JT | ✅核心 ✅ 核心 | | CX-7 | 稳定 |
| 86 | legal-compliance-bundle | 其他/法律合规技能包 | 50个中国企业法律合规自动化技能 | LEGAL_COMPLIANCE | BUSINESS_MODEL | "合同审查""劳动合规""PIPL" | 企业法务场景、中国法律体系 | 技能清单+安全审计报告 | ✅核心 ✅ 核心 | | P4 | JT | ✅核心 ✅ 核心 | | CX-1 | 试验 |
| 77 | fwsjtt-delivery-qa-reviewer | 服务设计专家团 | 审查交付物结构、证据与可执行性 | DELIVERY_WRITING | VALUE_PROP_BLUR | "交付前QA""评审这份方案" | 待审查的报告/方案/文件 | QA评分卡+返工建议清单 | ✅核心 ✅ 核心 | | P4 | S | — | 核心 |
| 74 | service-design-expert-team | 服务设计专家团(主) | 服务设计专家团总包入口与分诊调度 | AGENT_ORCHESTRATION | USER_JOURNEY_FRICTION | "调用服务设计专家团" | 具体业务场景、目标、约束 | 分诊结论+专家协作路径 | ✅核心 ✅ 核心 | | P4 | PT | ✅核心 ✅ 核心 | | CX-5 | 核心 |
| 79 | fwsjtt-expert-team | 服务设计专家团 | 专家团总控调度：分诊、协调、合成 | AGENT_ORCHESTRATION | PROBLEM_UNCLEAR | "多专家评审""专家团介入" | 业务背景、决策场景、已有材料 | 分诊结果+协作报告+最终方案 | ✅核心 ✅ 核心 | | P4 | PT | ✅核心 ✅ 核心 | | CX-5 | 核心 |
| 10 | create-prd | pm-execution | 8段式产品需求文档创建 | DELIVERY_WRITING | PROBLEM_UNCLEAR | "写PRD""产品需求文档" | 已有产品/功能想法及背景 | PRD Markdown文档 | ✅核心 ✅ 核心 | | P4 | S | — | 核心 |
| 12 | job-stories | pm-execution | JTBD框架下的Job Story与验收标准 | USER_JOURNEY_FRICTION | DELIVERY_WRITING | "job story""JTBD""用户情境" | 已有功能/场景/设计稿 | Job Story清单+验收标准 | ✅核心 ✅ 核心 | | P4 | S | — | 稳定 |
| 16 | release-notes | pm-execution | 技术工单转用户可读发布说明 | DELIVERY_WRITING | CONTENT_CREATION | "发布说明""release notes" | 已有变更记录 | 发布说明文档 | ✅核心 ✅ 核心 | | P4 | JT | — | 稳定 |
| 17 | retro | pm-execution | 结构化Sprint回顾会引导 | WORKFLOW_OPTIMIZATION | PRIORITY_MUD | "回顾会""retro""复盘" | 已有Sprint数据/团队反馈 | 回顾总结+行动项表 | ✅核心 ✅ 核心 | | P4 | JT | — | 稳定 |
| 20 | summarize-meeting | pm-execution | 会议录音转结构化纪要 | WORKFLOW_OPTIMIZATION | DELIVERY_WRITING | "会议纪要""会议总结" | 已有会议文字稿或录音 | 结构化纪要+行动项 | ✅核心 ✅ 核心 | | P4 | JT | — | 稳定 |
| 22 | user-stories | pm-execution | 3C+INVEST框架User Story与验收标准 | DELIVERY_WRITING | USER_JOURNEY_FRICTION | "user story""用户故事" | 已有功能/设计稿/产品上下文 | User Story清单+验收标准 | ✅核心 ✅ 核心 | | P4 | S | — | 核心 |
| 23 | wwas | pm-execution | Why-What-Acceptance格式的Backlog条目 | DELIVERY_WRITING | SCOPE_CREEP | "WWA""backlog条目" | 已有功能/战略上下文 | WWA Backlog条目清单 | ✅核心 ✅ 核心 | | P4 | S | — | 稳定 |
| 41 | value-prop-statements | pm-marketing-growth | 为营销/销售/入职生成价值主张文案 | DELIVERY_WRITING | VALUE_PROP_BLUR | "价值主张文案""销售说辞" | 已提供核心价值主张 | 分场景文案集 | ✅核心 ✅ 核心 | | P4 | PT | — | 稳定 |
| 67 | draft-nda | pm-toolkit | 起草双方保密协议含法律审查标注 | LEGAL_COMPLIANCE | DELIVERY_WRITING | "NDA""保密协议""合同" | 双方公司信息及共享信息类型 | 摘要+完整NDA+定制说明 | ✅核心 ✅ 核心 | | P4 | JT | ✅核心 ✅ 核心 | | CX-1 | 稳定 |
| 68 | grammar-check | pm-toolkit | 识别文本语法/逻辑/流畅度错误 | DELIVERY_WRITING | CONTENT_CREATION | "语法检查""校对""文字审核" | 已提供待审核文本 | 错误分类+修复建议+优先级 | ✅核心 ✅ 核心 | | P4 | S | — | 稳定 |
| 69 | privacy-policy | pm-toolkit | 为产品起草合规隐私政策 | LEGAL_COMPLIANCE | DELIVERY_WRITING | "隐私政策""GDPR合规" | 产品名称、数据类型、法域 | 隐私政策文档+合规清单 | ✅核心 ✅ 核心 | | P4 | JT | ✅核心 ✅ 核心 | | CX-1 | 稳定 |
| 97 | cad-editor | 创新技能 | 自然语言生成工程DXF图纸 | CONTENT_CREATION | SYSTEM_DESIGN | "画CAD图""建筑平面图" | Python3+ezdxf+matplotlib | DXF文件+PNG预览 | ✅核心 ✅ 核心 | | P4 | S | — | 试验 |
| 107 | ai-dev-workflow | 生产技能 | 三步标准化AI辅助编程工作流 | WORKFLOW_OPTIMIZATION | CODE_QUALITY | "AI编程""需求转代码" | 有明确软件需求和技术栈 | 功能文档+完整代码 | ✅核心 ✅ 核心 | | P4 | S | — | 稳定 |
| 113 | linux-omniscient | 生产技能 | 认知+执行+Linux系统控制三层全能 | AGENT_ORCHESTRATION | SYSTEM_DESIGN | "控制电脑""自动化办公" | Linux环境系统级操控 | 脚本+流水线+认知分析 | ✅核心 ✅ 核心 | | P4 | S | ✅核心 ✅ 核心 | | CX-8 | 试验 |
| 114 | omniscient | 生产技能 | 认知+执行+Windows控制三层全能 | AGENT_ORCHESTRATION | SYSTEM_DESIGN | "控制电脑""截图""操控" | Windows环境系统级操控 | 脚本+流水线+认知分析 | ✅核心 ✅ 核心 | | P4 | S | ✅核心 ✅ 核心 | | CX-8 | 核心 |
| 115 | skill-refactor | 生产技能 | 十一歩法评估并重构技能 | SKILL_CREATION | WORKFLOW_OPTIMIZATION | "技能改造""技能重构" | 有已存在的技能需要评估 | 改造报告+新SKILL.md | ✅核心 ✅ 核心 | | P4 | S | ✅核心 ✅ 核心 | | CX-8 | 稳定 |
| 116 | style-design-generator | 生产技能 | 基于100个风格方案的生成引擎 | CONTENT_CREATION | DELIVERY_WRITING | "风格生成""混搭风格" | 需要视觉风格设计 | 6槽位风格方案文本 | ✅核心 ✅ 核心 | | P4 | S | — | 稳定 |
| 119 | bilingual-buddy | 生活技能 | 四层双语对照格式对话 | EDUCATION | CONTENT_CREATION | "双语""中英文对照" | 中英双语学习需求 | 四层双语对照文本 | ✅核心 ✅ 核心 | | P4 | S | — | 稳定 |
| 120 | knowledge-explainer | 生活技能 | 知识点原子化拆解与专业级讲解 | EDUCATION | RESEARCH_ANALYSIS | "讲解""解释概念""知识点" | 需深入理解某学科知识点 | 结构化讲解文档 | ✅核心 ✅ 核心 | | P4 | S | — | 稳定 |
| 100 | academic-thesis-workflow | 学术技能 | 四步工作流从主题生成完整学术论文 | EDUCATION | CONTENT_CREATION | "写论文""学术论文" | 论文主题、学科领域 | 论证骨架+完整论文 | ✅核心 ✅ 核心 | | P4 | S | — | 稳定 |
| 126 | bookkeeping-agency-skill-system | 行业技能 | 代理记账行业十大集群292个能力单元 | BUSINESS_MODEL | LEGAL_COMPLIANCE | "代理记账""报税""汇算清缴" | 运营或搭建代理记账机构 | 能力单元执行结果 | ✅核心 ✅ 核心 | | P4 | S | CX-7, CX-1 | 稳定 |
| 127 | c2c-platform-skill-system | 行业技能 | C2C本地生活平台十大集群310个单元 | BUSINESS_MODEL | WORKFLOW_OPTIMIZATION | "C2C平台""本地生活" | 运营或搭建C2C本地生活平台 | 能力单元执行结果 | ✅核心 ✅ 核心 | | P4 | S | ✅核心 ✅ 核心 | | CX-7 | 稳定 |
| 128 | metabolic-healing-skill-system | 行业技能 | 代谢慢病非药而愈十大集群267个单元 | LIFE_MANAGEMENT | BUSINESS_MODEL | "代谢慢病""营养干预" | 需代谢慢病非药物逆转方案 | 健康评估+干预方案 | ✅核心 ✅ 核心 | | P4 | S | ✅核心 ✅ 核心 | | CX-7 | 稳定 |
| 129 | pharma-skill-system | 行业技能 | 医药行业十大集群334个能力单元 | BUSINESS_MODEL | LEGAL_COMPLIANCE | "医药""药企""医学事务" | 在医药行业从事市场/医学/合规 | 能力单元执行结果 | ✅核心 ✅ 核心 | | P4 | S | CX-7, CX-1 | 稳定 |
| 130 | universal-business-skill-system | 行业技能 | 通用行业十大集群286个+12行业校准 | BUSINESS_MODEL | WORKFLOW_OPTIMIZATION | "业务运营""行业技能" | 需任意行业结构化业务能力 | 能力单元执行结果 | ✅核心 ✅ 核心 | | P4 | S | ✅核心 ✅ 核心 | | CX-7 | 核心 |
| 132 | pharma-doc-reference | 负载技能 | 医药行业文档知识参考库11域93种 | KNOWLEDGE_SYSTEM | LEGAL_COMPLIANCE | "医药文档""医学写作" | 需产出医药行业专业文档 | 医药文档产出 | ✅核心 ✅ 核心 | | P4 | S | ✅核心 ✅ 核心 | | CX-7 | 稳定 |
| 136 | web-novel-writing-reference | 负载技能 | 网络小说创作知识参考库8域62种 | CONTENT_CREATION | KNOWLEDGE_SYSTEM | "网络小说""写小说""大纲" | 需系统化网络小说创作支持 | 小说大纲/章节/角色档案 | ✅核心 ✅ 核心 | | P4 | S | ✅核心 ✅ 核心 | | CX-7 | 稳定 |
| 139 | data-analyst | 新增（S-CX-6） | 通用数据分析与可视化引擎：Python数据处理+图表生成+缺失数据反馈 | RESEARCH_ANALYSIS | METRICS_CONFUSION | "数据分析""可视化""图表""报表""chart""dashboard" | 结构化数据(CSV/Excel/JSON)+分析需求 | 数据概览+关键发现+图表(PNG/SVG/HTML)+数据表 | ✅核心 ✅ 核心 | | P4 | S | ✅核心 ✅ 核心 | | CX-6 | 稳定 |

---

## 五、P5 - 控制（度量 / 测试 / 监控 / A-B实验 / 指标）

> 13 个 Skill | 核心职责：验证假设、度量结果、控制质量

| # | SKILL名称 | 来源位置 | 一句话描述 | 问题类型(主) | 问题类型(副) | 触发信号词 | 隐性前提 | 输出形态 | 关系类型 | 阶段 | 轨道 | 跨域 | 成熟度 |
|---|-----------|---------|-----------|-------------|-------------|-----------|---------|---------|------|------|------|--------|
| 6 | ab-test-analysis | pm-data-analytics | A/B测试统计分析与决策建议 | EXPERIMENT_NEEDED | METRICS_CONFUSION | "A/B测试""显著性""实验结果" | 已有实验数据 | 分析报告/统计表/决策建议 | ✅核心 ✅ 核心 | | P5 | S | ✅核心 ✅ 核心 | | CX-6 | 稳定 |
| 7 | cohort-analysis | pm-data-analytics | 用户队列留存分析与趋势洞察 | RESEARCH_ANALYSIS | METRICS_CONFUSION | "队列分析""留存曲线""churn" | 已有用户队列数据 | 留存热力图/趋势图表 | ✅核心 ✅ 核心 | | P5 | S | ✅核心 ✅ 核心 | | CX-6 | 稳定 |
| 14 | pre-mortem | pm-execution | 产品上线前风险预演 | SYSTEM_DESIGN | EXPERIMENT_NEEDED | "pre-mortem""风险分析" | 已有PRD或上线计划 | 风险分析报告+行动计划 | ✅核心 ✅ 核心 | | P5 | JT | — | 稳定 |
| 21 | test-scenarios | pm-execution | 从User Story生成QA测试场景 | CODE_QUALITY | DELIVERY_WRITING | "测试场景""test case" | 已有User Story及验收标准 | 测试场景文档 | ✅核心 ✅ 核心 | | P5 | JT | — | 稳定 |
| 34 | sentiment-analysis | pm-market-research | 大规模用户反馈情感分析 | RESEARCH_ANALYSIS | USER_JOURNEY_FRICTION | "情感分析""NPS""满意度" | 已有CSV/问卷/评论数据 | 细分情感报告+改进建议 | ✅核心 ✅ 核心 | | P5 | S | ✅核心 ✅ 核心 | | CX-6 | 稳定 |
| 43 | brainstorm-experiments-existing | pm-product-discovery | 为已有产品设计低成本验证实验 | EXPERIMENT_NEEDED | SCOPE_CREEP | "实验设计""验证假设" | 已提供功能想法及假设 | 假设→实验→指标→阈值 | ✅核心 ✅ 核心 | | P5 | PT | — | 稳定 |
| 44 | brainstorm-experiments-new | pm-product-discovery | 为新产品创建XYZ假设与Pretotype | EXPERIMENT_NEEDED | MARKET_CONFUSION | "新产品验证""Pretotype" | 已提供新产品概念 | XYZ假设+实验方案 | ✅核心 ✅ 核心 | | P5 | PT | — | 稳定 |
| 50 | metrics-dashboard | pm-product-discovery | 设计含指标、可视化及告警的仪表盘 | METRICS_CONFUSION | SYSTEM_DESIGN | "指标仪表盘""KPI看板" | 已提供产品背景及OKRs | 仪表盘规范+布局+工具建议 | ✅核心 ✅ 核心 | | P5 | S | ✅核心 ✅ 核心 | | CX-6 | 稳定 |
| 52 | prioritize-assumptions | pm-product-discovery | 影响×风险矩阵排序假设并设计实验 | PRIORITY_MUD | EXPERIMENT_NEEDED | "假设排序""影响风险矩阵" | 已提供待排序假设列表 | 矩阵分类+实验建议 | ✅核心 ✅ 核心 | | P5 | S | — | 稳定 |
| 78 | fwsjtt-evidence-auditor | 服务设计专家团 | 审计结论来源强度并标注证据等级 | METRICS_CONFUSION | RESEARCH_ANALYSIS | "审计证据""标注证据等级" | 待审查的材料/结论/引用来源 | 证据等级标签+缺口清单 | ✅核心 ✅ 核心 | | P5 | S | ✅核心 ✅ 核心 | | CX-6 | 核心 |
| 124 | cda-code-lab | 研究技能 | CDA架构的可执行Python仿真代码 | CODE_QUALITY | RESEARCH_ANALYSIS | "CDA代码""哈密顿投影" | 需将CDA理论转为可运行代码 | Python仿真代码+self-test | ✅核心 ✅ 核心 | | P5 | S | — | 试验 |
| 125 | cda-data-synth | 研究技能 | 为CDA架构生成标准格式合成数据集 | RESEARCH_ANALYSIS | SYSTEM_DESIGN | "因果数据合成""仿真数据" | 需为CDA准备训练/验证数据 | JSON格式因果数据集 | ✅核心 ✅ 核心 | | P5 | S | — | 试验 |
| 133 | singlefile-output-reference | 负载技能 | 单文件产出参考库7域52种产物 | CODE_QUALITY | CONTENT_CREATION | "HTML单文件""单文件应用" | 需生成自包含单文件代码 | 可运行的HTML/Python单文件 | ✅核心 ✅ 核心 | | P5 | S | — | 稳定 |

---

## 六、P6 - 复盘（回顾 / 经验教训 / 知识沉淀）

> 4 个 Skill | 核心职责：回顾总结、蒸馏经验、归档知识

| # | SKILL名称 | 来源位置 | 一句话描述 | 问题类型(主) | 问题类型(副) | 触发信号词 | 隐性前提 | 输出形态 | 关系类型 | 阶段 | 轨道 | 跨域 | 成熟度 |
|---|-----------|---------|-----------|-------------|-------------|-----------|---------|---------|------|------|------|--------|
| 84 | fwsjtt-theory-distiller | 服务设计专家团 | 从专家/书目中蒸馏可执行方法 | KNOWLEDGE_SYSTEM | SKILL_CREATION | "理论蒸馏""把书整理成方法" | 专家/书目/论文等理论来源 | 来源矩阵+方法卡+技能映射 | ✅核心 ✅ 核心 | | P6 | S | ✅核心 ✅ 核心 | | CX-8 | 核心 |
| 90 | tender-knowledge-framework | 其他/标书分析助手知识框架 | 构建标书分析知识体系与持续学习框架 | KNOWLEDGE_SYSTEM | BIDDING_PROCUREMENT | "标书知识框架""招投标技巧" | 互联网标书知识来源 | 知识框架树+学习汇报 | ✅核心 ✅ 核心 | | P6 | JT | ✅核心 ✅ 核心 | | CX-7 | 试验 |
| 137 | product-sunset-assessment | 新增（PT-P6） | 产品退市决策：6维衰退信号→退市ROI→方案选择 | WORKFLOW_OPTIMIZATION | BUSINESS_MODEL | "产品退市""下线""end-of-life""砍产品""衰退" | 产品线数据/用户趋势/财务指标 | 退市评估报告+方案(A/B/C/D)+沟通时间线 | ✅核心 ✅ 核心 | | P6 | PT | — | 稳定 |
| 138 | portfolio-rebalancing | 新增（PT-P6） | 产品组合再平衡：四维评分→平衡度分析→再分配矩阵 | WORKFLOW_OPTIMIZATION | PRIORITY_MUD | "产品组合""portfolio""组合评审""资源分配""产品线健康度" | 产品组合清单/各产品绩效数据 | 组合诊断+再平衡方案+12-24月路线图 | ✅核心 ✅ 核心 | | P6 | PT | — | 稳定 |

---

## 七、CX - 专业知识域

> 28 个 Skill（独立归属）| 按 CX-1 ~ CX-8 子域分组
> CX-2 至 CX-5 无独立归属 Skill，其知识作为跨域出现在 P1-P5 各阶段中（详见附录速查表）。

### CX-1 法律合规（2）

| # | SKILL名称 | 来源位置 | 一句话描述 | 问题类型(主) | 问题类型(副) | 触发信号词 | 隐性前提 | 输出形态 | 关系类型 | 阶段 | 轨道 | 跨域 | 成熟度 |
|---|-----------|---------|-----------|-------------|-------------|-----------|---------|---------|------|------|------|--------|
| 91 | law-skills | 其他/法律咨询 | 基于中国现行法律提供法律咨询参考 | LEGAL_COMPLIANCE | RESEARCH_ANALYSIS | "法律咨询""民法典""劳动法" | 具体法律问题或场景描述 | 法律咨询回复+法条引用 | ✅核心 ✅ 核心 | | CX-1 | JT | — | 稳定 |
| 1 | Gridman | 会计/Gridman | 中国财税全领域智能助手 | LEGAL_COMPLIANCE | BUSINESS_MODEL | "审计底稿""税务筹划" | 已明确具体财税场景或问题 | 专业判断文档/分录/分析报告 | ✅核心 ✅ 核心 | | CX-1 | S | CX-2, CX-7 | 核心 |

### CX-7 行业领域知识（3）

| # | SKILL名称 | 来源位置 | 一句话描述 | 问题类型(主) | 问题类型(副) | 触发信号词 | 隐性前提 | 输出形态 | 关系类型 | 阶段 | 轨道 | 跨域 | 成熟度 |
|---|-----------|---------|-----------|-------------|-------------|-----------|---------|---------|------|------|------|--------|
| 123 | cda | 研究技能 | 因果动力学架构，替代Transformer提案 | RESEARCH_ANALYSIS | SYSTEM_DESIGN | "CDA架构""因果机制网络" | 研究替代Transformer架构 | 架构参考文档与公式 | ✅核心 ✅ 核心 | | CX-7 | S | — | 试验 |
| 134 | smart-hardware-reference | 负载技能 | 智能硬件开发知识参考库9域68种 | KNOWLEDGE_SYSTEM | SYSTEM_DESIGN | "智能硬件""嵌入式""IoT" | 需智能硬件全生命周期开发 | 硬件技术方案+开发文档 | ✅核心 ✅ 核心 | | CX-7 | S | — | 稳定 |
| 135 | ultimate-domain-payload | 负载技能 | 人类活动全域终极负载物12领域+6跨域 | KNOWLEDGE_SYSTEM | LIFE_MANAGEMENT | "终极负载物""全域""生命领域" | 需跨生命领域综合任务编排 | 跨域价值链方案 | ✅核心 ✅ 核心 | | CX-7 | S | — | 试验 |

### CX-8 Agent/Skill/系统工具（22）

| # | SKILL名称 | 来源位置 | 一句话描述 | 问题类型(主) | 问题类型(副) | 触发信号词 | 隐性前提 | 输出形态 | 关系类型 | 阶段 | 轨道 | 跨域 | 成熟度 |
|---|-----------|---------|-----------|-------------|-------------|-----------|---------|---------|------|------|------|--------|
| 3 | excel-xlsx | 其他/excel-xlsx | 创建、检查和编辑Excel工作簿 | WORKFLOW_OPTIMIZATION | CODE_QUALITY | "Excel""xlsx""电子表格" | 已有或需生成Excel文件 | Excel文件/Python脚本 | ✅核心 ✅ 核心 | | CX-8 | S | — | 稳定 |
| 4 | find-skills | 其他/find-skills | 搜索并安装开源Agent Skills技能包 | SKILL_CREATION | AGENT_ORCHESTRATION | "找个skill""有没有技能" | 已描述需要的功能领域 | 技能列表/安装命令 | ✅核心 ✅ 核心 | | CX-8 | S | — | 稳定 |
| 73 | self-improving-agent | 其他/self-improving-agent | 记录错误与学习以实现Agent持续改进 | CODE_QUALITY | AGENT_ORCHESTRATION | "记录这个错误""保存为skill" | 有项目工作目录 | 结构化Markdown日志 | ✅核心 ✅ 核心 | | CX-8 | S | — | 稳定 |
| 85 | skill-creator-optimized | 其他/skill-creator | AI驱动生成与优化标准化Skill技能包 | SKILL_CREATION | WORKFLOW_OPTIMIZATION | "创建技能""写SKILL.md" | 技能目标/触发场景/输入输出类型 | 完整Skill目录 | ✅核心 ✅ 核心 | | CX-8 | S | — | 稳定 |
| 8 | sql-queries | pm-data-analytics | 自然语言转SQL查询 | WORKFLOW_OPTIMIZATION | CODE_QUALITY | "写SQL""生成查询" | 已有数据库Schema | SQL代码/执行脚本 | ✅核心 ✅ 核心 | | CX-8 | S | — | 稳定 |
| 11 | dummy-dataset | pm-execution | 生成可定制的真实感测试数据集 | WORKFLOW_OPTIMIZATION | CODE_QUALITY | "测试数据""mock数据" | 已明确字段/行数/格式 | CSV/JSON/SQL脚本 | ✅核心 ✅ 核心 | | CX-8 | S | — | 稳定 |
| 92 | linux-system-controller | 其它技能 | Linux系统桌面/硬件/串口/IOT控制 | SYSTEM_DESIGN | WORKFLOW_OPTIMIZATION | "打开应用""截图OCR" | Linux系统、Python3 | 脚本执行结果 | ✅核心 ✅ 核心 | | CX-8 | S | — | 试验 |
| 93 | minimal-agent | 其它技能 | 极简OS控制代理：双模式智能切换 | SYSTEM_DESIGN | AGENT_ORCHESTRATION | "打开应用""控制桌面" | WorkBuddy平台 | 命令执行结果 | ✅核心 ✅ 核心 | | CX-8 | S | — | 试验 |
| 94 | system-controller | 其它技能 | Windows桌面软硬件/IOT/GUI控制 | SYSTEM_DESIGN | WORKFLOW_OPTIMIZATION | "打开应用""关闭窗口" | Windows 10/11、PowerShell | 脚本执行结果 | ✅核心 ✅ 核心 | | CX-8 | S | — | 稳定 |
| 95 | universal-agent | 其它技能 | 自然语言→动态代码生成→自动执行 | AGENT_ORCHESTRATION | SYSTEM_DESIGN | "自动执行任务""万能agent" | Python环境 | 执行结果+错误自修复 | ✅核心 ✅ 核心 | | CX-8 | S | — | 试验 |
| 96 | builtin-tools | 创新技能 | 16个纯Python跨平台基础工具脚本 | SYSTEM_DESIGN | WORKFLOW_OPTIMIZATION | "文件搜索""网页抓取" | Python3环境 | JSON结构化输出 | ✅核心 ✅ 核心 | | CX-8 | S | — | 稳定 |
| 98 | chat-bus | 创新技能 | 基于共享目录的多Agent消息总线 | AGENT_ORCHESTRATION | SYSTEM_DESIGN | "Agent聊天""消息总线" | 共享目录(NAS/云同步) | JSON消息文件 | ✅核心 ✅ 核心 | | CX-8 | S | — | 试验 |
| 99 | gamebox | 创新技能 | 多人游戏引擎：狼人杀/文字冒险等 | CONTENT_CREATION | AGENT_ORCHESTRATION | "狼人杀""文字冒险" | 共享目录、多Agent参与 | 游戏状态JSON | ✅核心 ✅ 核心 | | CX-8 | S | — | 试验 |
| 102 | comprehensive-knowledge-system | 方法技能 | 投资哲学+提示词+编程方法论综合知识库 | KNOWLEDGE_SYSTEM | BUSINESS_MODEL | "投资哲学""提示词体系" | 跨三大域的体系化知识需求 | 知识索引与参考文件 | ✅核心 ✅ 核心 | | CX-8 | S | — | 核心 |
| 103 | identity-primitive-chain-prompt | 方法技能 | 身份基元链提示词，AI认知操作系统内核 | AGENT_ORCHESTRATION | SYSTEM_DESIGN | "执行协议""基元链" | AI自适应任务执行需求 | 提示词协议规范 | ✅核心 ✅ 核心 | | CX-8 | S | — | 核心 |
| 104 | ipo-model | 方法技能 | 输入处理输出递归嵌套模型 | SYSTEM_DESIGN | AGENT_ORCHESTRATION | "IPO""递归拆解" | 结构化分析需求 | 分析框架与树形结构 | ✅核心 ✅ 核心 | | CX-8 | S | — | 核心 |
| 105 | universal-primitives | 方法技能 | LLM两个基元控制一切方法论 | SYSTEM_DESIGN | AGENT_ORCHESTRATION | "AI能力边界""两个基元" | AI工具设计哲学讨论 | 架构原理文档 | ✅核心 ✅ 核心 | | CX-8 | S | — | 稳定 |
| 106 | adaptive-skill-stack | 生产技能 | 自动分析需求并叠加能力的元技能 | AGENT_ORCHESTRATION | WORKFLOW_OPTIMIZATION | "跨领域复合任务""能力积累" | 处理未知领域或跨域任务 | 能力注册表与动态技能 | ✅核心 ✅ 核心 | | CX-8 | S | — | 试验 |
| 108 | capability-pipeline-os | 生产技能 | 万物单元化的通用能力管线操作系统 | AGENT_ORCHESTRATION | SYSTEM_DESIGN | "能力单元""管线编排" | 将复杂任务拆分为管线 | 管线编排方案与框架 | ✅核心 ✅ 核心 | | CX-8 | S | — | 稳定 |
| 109 | cogniexec | 生产技能 | 认知套件+执行框架+编排引擎 | AGENT_ORCHESTRATION | WORKFLOW_OPTIMIZATION | "认知执行""代码自动化" | 认知思考与代码执行融合 | 认知分析+脚本+结果 | ✅核心 ✅ 核心 | | CX-8 | S | — | 核心 |
| 117 | universal-task-os | 生产技能 | 执行+内容+创新三轴任务操作系统 | AGENT_ORCHESTRATION | WORKFLOW_OPTIMIZATION | "三轴""任务系统" | 需要统一框架处理复杂任务 | 三轴协同执行方案 | ✅核心 ✅ 核心 | | CX-8 | S | — | 核心 |
| 131 | domain-payload-generator | 负载技能 | 元技能，从零创建领域负载物技能 | SKILL_CREATION | KNOWLEDGE_SYSTEM | "领域负载物""新领域技能" | 需为新领域创建结构化知识 | 完整技能(SKILL.md+refs) | ✅核心 ✅ 核心 | | CX-8 | S | — | 核心 |

---

## 附录A：阶段 x 跨域映射速查表

> 下表展示每个 CX 子域的主要承载 Skill 所在阶段，便于快速定位跨域知识。

| CX子域 | 说明 | 主要承载阶段 | 代表Skill |
|--------|------|-------------|-----------|
| CX-1 法律合规 | 法律/合规/合同/隐私 | CX(独立), P4(执行) | law-skills, Gridman, draft-nda, privacy-policy, legal-compliance-bundle, bookkeeping-agency, pharma-skill-system |
| CX-2 工程经济 | 财务/投资/定价/ROI | P2(论证) | fwsjtt-roi-strategist, pricing-strategy, monetization-strategy, wealth-manager, solopreneur-os, Gridman |
| CX-3 市场研究 | 调研方法论/ICP/画像 | P1(识别) | beachhead-segment, ideal-customer-profile, interview-script, polymarket |
| CX-4 产品战略 | 战略框架/北极星/画布 | P1(识别), P2(论证) | swot-analysis, north-star-metric, opportunity-solution-tree, business-model, lean-canvas, product-strategy, startup-canvas, ansoff-matrix, fwsjtt-strategy-growth-advisor, solopreneur-os |
| CX-5 组织干系人 | 团队/干系人/组织协作 | P3(规划), P4(执行) | stakeholder-map, service-design-expert-team, fwsjtt-expert-team, review-resume |
| CX-6 数据度量 | 指标体系/实验统计/证据 | CX(独立), P5(控制), P2(论证) | data-analyst, ab-test-analysis, cohort-analysis, sentiment-analysis, metrics-dashboard, fwsjtt-evidence-auditor, north-star-metric, fwsjtt-metrics-architect |
| CX-7 行业领域 | 行业/垂直领域专业知识 | CX(独立), P4(执行), P1(识别) | cda, smart-hardware-reference, ultimate-domain-payload, 行业技能x5, biddingx2, pharma-doc-reference, pestle-analysis, porters-five-forces, auto-dealer |
| CX-8 Agent/工具 | 系统工具/Agent/Skill/方法论 | CX(独立), P4(执行), P6(复盘) | CX-8组全部22个Skill + linux-omniscient, omniscient, skill-refactor, fwsjtt-theory-distiller |

---

## 附录B：旧层 → 新阶段映射对照

| 旧层 | 名称 | 旧数量 | 主要新阶段 | 说明 |
|------|------|--------|-----------|------|
| D | 发现诊断层 | 25 | P1 识别 | 市场研究、用户研究、竞品分析等归P1；PESTLE/Porter/SWOT等分析框架归P1 |
| ✅核心 | S | 方案权衡层 | 33 | P2 论证 / P3 规划 | 评估选项/商业论证归P2(31)；OKR/Sprint计划归P3(3) |
| E | 验证证据层 | 12 | P5 控制 | A/B测试、实验设计、指标度量归P5(13含跨层)；pre-mortem归P5 |
| V | 交付协同层 | 35 | P4 执行 / P6 复盘 | 文档生成/任务执行归P4(35)；theory-distiller/tender-knowledge归P6(2) |
| I | 基础设施层 | 31 | CX-8 Agent/工具 | 系统工具/Agent/Skill/方法论归CX-8(22)；部分归P4/P5/CX-7 |

---

## 附录C：全量 Skill ID 索引

> 快速按 ID 定位 Skill 所在阶段

| ID范围 ✅ 核心 | | P1 | P2 ✅ 核心 | | P3 | P4 ✅ 核心 | | P5 | P6 | CX |
|--------|----|----|----|----|----|----|----|
| 1-10 | 70 | 2 | 9 | 5,10 | 6,7 | — | 1,3,4,8 |
| 11-20 | — | 13,15 | 18,19 | 12,16,17,20 | 14 | — | 11 |
| 21-30 | 24,29,30 | 25,26,27,28 | — | 22,23 | 21 | — | — |
| 31-40 | 31,32,33,35,36,38 | 37,39,40 | — | — | 34 | — | — |
| 41-50 | 42,47,48,49 | 45,46 | — | 41 | 43,44,50 | — | — |
| 51-60 | 51,54,59,60 | 53,55,56,57,58 | — | — | 52 | — | — |
| 61-70 | 65 | 61,62,63,64,66 | — | 67,68,69 | — | — | — |
| 71-80 | 71,75,76 | 72 | — | 74,77,79 | 78 | — | 73 |
| 81-90 | 82 | 81,83 | — | 86,87,88,89 | — | 84,90 | 85 |
| 91-100 | — | — | — | 97,100 | — | — | 91,92,93,94,95,96,98,99 |
| 101-110 | 101 | 110 | — | 107 | — | — | 102,103,104,105,106,108,109 |
| 111-120 | 111 | 112,118 | — | 113,114,115,116,119,120 | — | — | 117 |
| 121-139 | — | 121,122 | — | 126,127,128,129,130,132,136,139 | 124,125,133 | 137,138 | 123,131,134,135 |

---

> 填写完成。下一步行动建议：
> 1. 审查每个 Skill 的阶段归属是否准确，特别是跨阶段的 Skill（如 fwsjtt-service-designer 横跨 P1/P3）
> 2. 识别重叠的 Skill 并决定合并/淘汰策略
> 3. 为高频核心 Skill 补写标准 IO 契约卡片
> 4. 建立总控 Dispatcher 路由表（按 P1→P2→P3→P4→P5→P6 流程编排）
> 5. 为 CX 知识域建立按需注入机制，与主流程阶段解耦
