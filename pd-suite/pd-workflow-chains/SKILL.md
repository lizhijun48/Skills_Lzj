---
name: pd-workflow-chains
version: 1.0.0
description: PD链式工作流索引——5条标准链路+3条专项链路，定义15个PD SKILL之间的调用顺序、前置条件、输入输出和衔接标志。与pm-suite协作路由。触发词：产品工作流、PD链路、产品流程、PD协作路由、产品经理工作流。
governance_id: "PT-016"

triggers:
  - 产品工作流
  - PD链路
  - 产品流程
  - PD协作路由
  - 产品经理工作流
---

# pd-workflow-chains · PD链式工作流索引

> **核心定位**：回答"产品经理的工作流怎么串起来"——定义15个PD SKILL的调用顺序、衔接标志和协作路由。
> **NPDP对标**：全局编排

## 链路概览

### 5条标准链路

| # | 链路 | 流程 | 核心输出 | 触发条件 |
|---|------|------|----------|----------|
| 1 | **发现链** | pd-go-nogo → pd-market-research → pd-user-research | 市场洞察+用户画像+需求池 | 有产品想法/方向 |
| 2 | **规划链** | pd-product-strategy → pd-portfolio-management → pd-requirements-design → pd-prd-writing | 产品战略+需求基线+PRD | Go/No-Go已通过 |
| 3 | **执行链** | pd-innovation-process ←→ pd-product-launch | MVP/产品增量+GTM方案 | PRD已确认(approved) |
| 4 | **运营链** | pd-product-operations ←→ pd-lifecycle-management | 增长数据+迭代决策 | 产品已上线 |
| 5 | **度量链** | pd-tools-metrics ←→ pd-go-nogo | 指标体系+续做/退市决策 | 需要评估产品健康度 |

### 3条专项链路

| # | 链路 | 流程 | 核心输出 | 触发条件 |
|---|------|------|----------|----------|
| 6 | **迭代链** | pd-product-operations → pd-requirements-design → pd-prd-writing | 数据驱动的新需求+PRD更新 | 运营数据发现新机会/问题 |
| 7 | **退市链** | pd-lifecycle-management → pd-portfolio-management → pd-go-nogo | 退市决策+资源释放 | 产品进入衰退期 |
| 8 | **PD→PM桥接链** | pd-integration → pm-integration | 产品→项目交付 | 产品决策需转项目交付 |

---

## 标准链路详细定义

### 链路1：发现链

```
pd-go-nogo ──────→ pd-market-research ──────→ pd-user-research
    │                      │                          │
    │ 8维度Go/No-Go        │ 市场规模+竞品+趋势        │ Persona+CJM+JTBD
    │ 评分卡               │ 12种研究方法选择           │ 访谈脚本+假设验证
    ▼                      ▼                          ▼
Go决策               市场洞察报告                  用户洞察+需求池
> **注**：`pd-user-research` 现含 insight-extraction 子能力——可将访谈/会议**录音转写文本**直接转成结构化洞察（详见"能力模块登记"章节）。
> **注**：发现链中的"市场/用户研究"步骤可用 `pd-ai-research-workflow` (PT-019) 做 3-Tier AI 研究编排快速产出报告（框架方法仍归 PT-003）。
```

**衔接标志**：
- pd-go-nogo → pd-market-research：Go/No-Go决策为"Go"或"Conditional Go"
- pd-market-research → pd-user-research：市场研究完成，确定目标用户范围

**关键质量门**：
- Go/No-Go评分卡必须完整填写
- 市场规模(TAM/SAM/SOM)必须量化
- 用户研究至少完成5人深度访谈

### 链路2：规划链

```
pd-product-strategy → pd-portfolio-management → pd-requirements-design → pd-prd-writing
    │                       │                          │                       │
    │ 愿景+路线图+BMC      │ 组合平衡+优先级          │ KANO+Y模型+用户故事    │ 8模块PRD+埋点
    ▼                       ▼                          ▼                       ▼
产品战略文档           组合评审结论               需求基线(RTM)             PRD(approved)
```

**衔接标志**：
- pd-product-strategy → pd-portfolio-management：产品战略确认，进入组合评审
- pd-portfolio-management → pd-requirements-design：组合评审通过，进入需求定义
- pd-requirements-design → pd-prd-writing：需求基线锁定，进入PRD编写

**关键质量门**：
- 产品战略必须经过管理层审批
- 组合评审必须确定优先级排序
- 需求必须完成KANO分类
- PRD必须经过评审并状态变为"approved"

### 链路3：执行链

```
pd-innovation-process ←→ pd-product-launch
    │                          │
    │ Stage-Gate/敏捷迭代      │ GTM+定价+渠道+种子用户
    │ MVP/产品增量              │ 竞争战卡+发布计划
    ▼                          ▼
可发布的产品              GTM方案+发布就绪
```

**衔接标志**：
- pd-innovation-process → pd-product-launch：MVP/产品增量达到可发布标准
- pd-product-launch → pd-innovation-process：市场反馈驱动下一轮迭代

**关键质量门**：
- 产品0 P0 Bug
- GTM策略画布已完成
- 种子用户已就绪
- 竞争战卡(Top3)已完成

### 链路4：运营链

```
pd-product-operations ←→ pd-lifecycle-management
    │                          │
    │ AARRR+增长实验+AB测试    │ PLC阶段判断+版本路线图
    │ 灰度发布+用户运营         │ 技术债务+退市评估
    ▼                          ▼
增长数据+运营策略         生命周期管理策略
```

**衔接标志**：
- pd-product-operations → pd-lifecycle-management：运营数据输入PLC阶段判断
- pd-lifecycle-management → pd-product-operations：生命周期策略驱动运营重点

**关键质量门**：
- AARRR指标体系必须建立
- PLC阶段判断必须完成
- 技术债务清单必须维护

### 链路5：度量链

```
pd-tools-metrics ←→ pd-go-nogo
    │                    │
    │ OKR/KPI/北极星     │ 续做/扩展/退市决策
    │ 财务分析(ROI/NPV)  │ 市场验证+技术可行性
    ▼                    ▼
指标体系+度量报告      Go/No-Go决策
```

**衔接标志**：
- pd-tools-metrics → pd-go-nogo：度量数据输入Go/No-Go评估
- pd-go-nogo → pd-tools-metrics：新Go决策需建立新的度量体系

---

## 专项链路详细定义

### 链路6：迭代链

```
pd-product-operations ──→ pd-requirements-design ──→ pd-prd-writing
    │                            │                         │
    │ 运营数据+用户反馈+AB结果    │ 新需求KANO+Y模型        │ PRD增量更新
    ▼                            ▼                         ▼
新需求候选               需求基线更新               PRD版本升级
```

**触发条件**：
- A/B测试发现新机会
- 用户反馈收集到高频需求
- 运营数据发现漏斗断点
- 竞品动态需跟进

**注意**：迭代链是运营→规划的"反向流"，数据驱动需求

### 链路7：退市链

```
pd-lifecycle-management ──→ pd-portfolio-management ──→ pd-go-nogo
    │                              │                         │
    │ PLC衰退期判断+退市评估       │ 资源释放+组合调整        │ 替代产品Go/No-Go
    ▼                              ▼                         ▼
退市决策                 组合重新平衡              新产品/替代方案决策
```

**触发条件**：
- 产品连续6个月收入环比下降
- 月维护成本 > 月收入50%
- 有明确替代产品方案

### 链路8：PD→PM桥接链

```
pd-integration ──→ pm-integration
    │                    │
    │ PRD+需求基线+GTM   │ 项目章程+管理计划
    │ 优先级+AC          │ WBS+范围基线+排期
    ▼                    ▼
产品决策转项目交付     项目启动与执行
```

**触发条件**：
- PRD已确认(approved)
- 产品决策需要项目团队交付
- 超出当前Sprint范围的新功能开发

**桥接协议**：
1. PD提供：PRD+需求基线+优先级+非功能需求+GTM计划
2. PM提供：项目章程+WBS+排期+风险登记+质量标准
3. 冲突解决：PD管What，PM管How（见pd-integration冲突解决矩阵）

---

## 能力模块登记：insight-extraction（PT-012 子能力）

> **来源**：从 ai-pm-exploration-toolkit 提取并并入 `pd-user-research` (PT-012) 的"录音/文本 PM 洞察抽取"能力。
> **功能**：把真实录音/转写文本按 6 类 PM 场景（用户访谈/竞品情报/演示反馈/客服分析/干系人会议/语音备忘）抽取结构化洞察（轻量规则法，无需大模型）。
> **阶段**：P1（用户洞察子定位 P1-b），作为 `pd-user-research` 内部可独立调用的子能力，**不单独占治理编号**。

### 衔接标志（调用关系）

| 调用方向 | 目标 SKILL | 传递内容 | 衔接标志 |
|----------|-----------|---------|---------|
| insight-extraction → | `pm-requirements-scope` (JT-003) | 抽取的需求/功能请求 | 需求条目可入需求池→范围定义 |
| insight-extraction → | `pm-stakeholder-management` (JT-015) | 抽取的决策/行动项/风险 | 行动项→干系人跟进与跟踪 |
| insight-extraction → | `pd-market-research` (PT-003) | 抽取的竞品情报 | 竞品点→竞品分析框架 |

### 触发条件
- 用户提供**访谈/会议/演示/客服/竞品/语音备忘的转写文本**（非凭空生成）
- 需按 PM 维度（痛点/决策/行动项/风险/竞品/功能请求）结构化

### 边界（不做）
- 不造用户画像（走 Persona）；不替代深度动机挖掘（走 JTBD/访谈设计）
- 仅处理**真实文本**，不做"合成数据"

## 能力模块登记：pd-ai-research-workflow（PT-019）

> **来源**：从 ai-pm-exploration-toolkit 的 `playbooks/MARKET_RESEARCH_PLAYBOOK.md` + `PM_GOOSE_WORKFLOWS.md` 提取，新建 `pd-ai-research-workflow` (PT-019)。
> **功能**：AI 驱动的市场研究编排——3-Tier 研究法（快问 LLM / 财务对标 / 自主深研）+ 8 个多步研究工作流 prompt + 3 种组合范式。属**执行/编排层**，框架方法转 `pd-market-research` (PT-003)。
> **阶段**：P1（与 PT-003 同阶段，互补不重叠）。

### 衔接标志（调用关系）
| 调用方向 | 目标 SKILL | 传递内容 | 衔接标志 |
|----------|-----------|---------|---------|
| pd-ai-research-workflow → | `pd-market-research` (PT-003) | 框架/方法选择 | 框架层以此为准，本技能只管执行编排 |
| pd-ai-research-workflow → | `pd-go-nogo` (PT-004) | 研究结论 | 落到 Go/No-Go 决策 |
| pd-ai-research-workflow → | `pd-user-research.insight-extraction` (PT-012) | 真实转写文本 | 若有真实访谈/会议文本，先抽取洞察再入研究 |
| pd-ai-research-workflow → | `pm-requirements-scope` (JT-003) | 需求机会 | 入需求池 |
| pd-ai-research-workflow → | `pm-stakeholder-management` (JT-015) | 高管汇报/决策产出 | 干系人跟进 |

### 触发条件
- 需快速产出竞品情报/市场机会/用户研究综合等结构化研究报告
- 要编排 T1→T2→T3 分层研究，或复用 8 个标准工作流之一

### 边界（不做 / 红线）
- 不提供市场研究**框架方法**（归 PT-003）
- **禁止用随机合成数据替代真实用户研究**（原 8 工作流 prompt 中的 synthetic data 步骤须替换为 PT-012 真实洞察）
- 仅做编排与执行，研究结论须人工校验

---

## 与pm-suite协作路由

### PD SKILL ↔ PM SKILL 映射

| PD SKILL | PM SKILL | 协作内容 |
|----------|----------|----------|
| pd-requirements-design | pm-requirements-scope | 需求基线→WBS+范围基线 |
| pd-prd-writing | pm-schedule-cost | PRD→排期+预算 |
| pd-product-operations | pm-change-management | 运营数据→需求变更 |
| pd-product-launch | pm-project-delivery | GTM→交付里程碑 |
| pd-lifecycle-management | pm-project-closure | 退市→项目收尾 |
| pd-go-nogo | pm-project-opportunity | Go决策→项目立项 |
| pd-tools-metrics | pm-performance-tracking | 度量数据→绩效报告 |
| pd-integration | pm-integration | PD↔PM全局桥接 |
| pd-user-research（insight-extraction 子能力） | pm-stakeholder-management / pm-requirements-scope | 录音/会议转写→行动项/需求 |

### 协作触发规则

```
PD → PM 触发：
1. PRD状态=approved → 启动pm-requirements-scope
2. Go/No-Go=Go → 启动pm-project-opportunity
3. 需求变更(一般/重大) → 启动pm-change-management
4. 退市决策确定 → 启动pm-project-closure
5. 录音/会议转写产出行动项/决策/风险 → 启动 pm-stakeholder-management（跟进）与 pm-requirements-scope（需求入池）

PM → PD 触发：
1. 进度延迟影响上线 → 通知pd-product-launch调整GTM
2. 技术约束影响需求 → 通知pd-requirements-design调整方案
3. 质量问题影响发布 → 通知pd-innovation-process调整迭代
4. 变更请求影响产品 → 通知pd-integration评估影响
```

---

## 链路选择决策树

```
你的情况是什么？
│
├─ "有一个产品想法" → 发现链（链路1）
├─ "已经决定要做" → 规划链（链路2）
├─ "PRD写完了要开发" → 执行链（链路3）+ PD→PM桥接链（链路8）
├─ "产品已上线" → 运营链（链路4）
├─ "需要看产品健康度" → 度量链（链路5）
├─ "运营发现新需求" → 迭代链（链路6）
├─ "产品该不该退" → 退市链（链路7）
└─ "不确定走哪条链" → pd-integration（全局编排）
```

---

## 即用工具

### 工具1：链路启动检查清单

```
发现链启动前：
☐ 有明确的产品想法或方向
☐ 有初步的市场认知
☐ 有资源做市场+用户研究

规划链启动前：
☐ Go/No-Go已通过
☐ 有市场研究结论
☐ 有用户画像

执行链启动前：
☐ PRD状态=approved
☐ 有设计稿
☐ 开发团队已就绪

运营链启动前：
☐ 产品已上线
☐ 埋点已部署
☐ AARRR指标已定义
```

### 工具2：链路进度跟踪表

| 链路 | 当前阶段 | 当前SKILL | 状态 | 下一SKILL | 阻塞项 |
|------|----------|----------|------|----------|--------|
| 发现链 | | | ☐未启动 ☐进行中 ☐完成 | | |
| 规划链 | | | | | |

---

## 核心原则

1. **链路是参考不是教条**——按需组合，不是每条链都要走完
2. **质量门不可跳过**——每个衔接点的质量门是防护栏
3. **数据驱动链路切换**——不是"我觉得该进入下一阶段了"，而是"数据告诉我该进入了"
4. **迭代链是持续运行的**——运营→需求→PRD是常态循环
5. **PD↔PM桥接是双向道**——产品影响项目，项目也影响产品
6. **不确定走哪条链时找pd-integration**——整合管理就是干这个的
7. **链路可并行**——度量链和运营链可以同时运行
