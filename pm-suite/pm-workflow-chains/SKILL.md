---
name: pm-workflow-chains
description: "PM链式工作流索引——1条组织层链路+5条标准链路+2条专项链路，定义16个PM SKILL之间的调用顺序、前置条件、输入输出和衔接标志。组织层治理链(it-governance→opportunity)、立项链(opportunity→tender-analysis→bid-proposal→integration)、规划链(requirements→schedule-cost→team-communication→stakeholder-management→procurement-quality→risk-management)、执行链(delivery+quality-assurance)、监控链(change-management+performance-tracking)、收尾链(gov-acceptance→project-closure)；专项链：变更链(delivery→change-management→delivery)、风险链(risk-management→change-management)。当需要了解PM SKILL的调用顺序、确定下一步该用哪个SKILL、或规划完整项目流程时使用。触发词：PM工作流、链式调用、项目流程、下一步、SKILL顺序、怎么串联。"
agent_created: true
governance_id: "JT-018"

triggers:
  - PM工作流
  - 链式调用
  - 项目流程
  - 下一步
  - SKILL顺序
  - 怎么串联
---

# PM链式工作流索引

## 角色定位

PM SKILL体系的"导航员"，帮助用户理解15个PM SKILL之间的调用顺序和衔接关系。

核心任务：定义标准链路，明确每个SKILL的前置条件、输入输出和衔接标志，确保项目从立项到收尾形成完整闭环。

---

## SKILL全景图（16个）

| 阶段 | SKILL | 核心能力 |
|------|-------|---------|
| **组织层** | pm-it-governance | 信息系统治理（立项前评估+IT审计+体系管理） |
| **启动** | pm-project-opportunity | 项目立项+Go/No-Go |
| **启动** | pm-bid-proposal | 招投标方案编制 |
| **启动** | pm-tender-analysis | 招标文件解析（投标前置，JT-019） |
| **启动** | pm-integration | 项目整合管理（章程+管理计划+整体变更协调+收尾整合） |
| **规划** | pm-requirements-scope | 需求管理+范围定义 |
| **规划** | pm-schedule-cost | 进度管理+成本控制 |
| **规划** | pm-team-communication | 团队管理+沟通协调 |
| **规划** | pm-stakeholder-management | 干系人管理 |
| **规划** | pm-procurement-quality | 采购管理+质量规划 |
| **规划** | pm-risk-management | 风险管理 |
| **执行** | pm-project-delivery | 项目交付管理 |
| **执行** | pm-quality-assurance | 质量保证+过程改进 |
| **监控** | pm-change-management | 变更管理 |
| **监控** | pm-performance-tracking | 绩效跟踪+状态报告 |
| **收尾** | pm-gov-acceptance | 政府项目验收 |
| **收尾** | pm-project-closure | 项目收尾+知识沉淀 |

---

## 组织层链路（立项前）

### 链路0：治理链

```
pm-it-governance ──→ pm-project-opportunity
[IT治理评估]          [立项决策]
```

| 环节 | SKILL | 关键输出 | 衔接标志 |
|------|-------|---------|---------|
| 1 | pm-it-governance | IT战略对齐评估+价值论证+风险评估 | **治理评估通过** |

**前置条件**：
- 企业战略/业务需求触发
- 涉及新 IT 系统建设或 IT 体系评估时启动

**分支可能**：
- 治理评估通过 → 进入链路1立项
- 评估不通过 → 暂缓/否决
- 日常 IT 审计（非立项场景）→ 独立运行，审计报告 → pm-quality-assurance / pm-change-management

> [注] pm-it-governance (JT-020) 为组织级入口，对标高项第3章信息系统治理，骨架版待学习填充。

---

## 5条标准链路

### 链路1：立项链

```
pm-project-opportunity ──→ pm-tender-analysis ──→ pm-bid-proposal ──→ pm-integration
     [立项决策]              [招标文件解析]            [投标方案]          [项目整合启动]
```

| 环节 | SKILL | 关键输出 | 衔接标志 |
|------|-------|---------|---------|
| 1 | pm-project-opportunity | 项目建议书+可研报告+初设概算+Go决策 | **立项批复** |
| 2 | pm-tender-analysis | 招标文件解析报告（废标扫描/资质核查/评分矩阵/风险信号/决策建议） | **招标文件解析完成** |
| 3 | pm-bid-proposal | 投标方案+报价+风险预案 | **中标通知书** |
| 4 | pm-integration | 项目章程+项目管理计划框架+知识管理规划 | **项目章程签发** |

**前置条件**：
- 链路2启动需：立项批复+投标文件（合同）
- pm-tender-analysis启动需：立项批复+招标文件（在决定投标前完成解析）
- pm-integration启动需：中标通知书+合同

**分支可能**：
- Go/No-Go决策后不投标 → 链路终止
- 未中标 → 链路终止
- 中标后转内部交付 → 跳到链路3（跳过投标），但pm-integration仍需执行

---

### 链路2：规划链

```
pm-requirements-scope → pm-schedule-cost → pm-team-communication → pm-stakeholder-management → pm-procurement-quality → pm-risk-management
     [需求+范围]          [进度+成本]          [团队+沟通]            [干系人管理]           [采购+质量规划]         [风险管理]
```

| 环节 | SKILL | 关键输出 | 衔接标志 |
|------|-------|---------|---------|
| 1 | pm-requirements-scope | 需求矩阵+RTM+WBS+范围说明书+范围基准 | **范围基准冻结** |
| 2 | pm-schedule-cost | 进度计划+成本基线+EVM基线+资源需求 | **进度+成本基线冻结** |
| 3 | pm-team-communication | 组织架构+RACI+团队建设计划+沟通矩阵 | **团队组建完成** |
| 4 | pm-stakeholder-management | 干系人登记册+权力-利益矩阵+参与计划 | **干系人参与计划确认** |
| 5 | pm-procurement-quality | 采购计划+RFP+质量管理计划+质量测量指标 | **采购+质量计划确认** |
| 6 | pm-risk-management | 风险登记册+PIM+应对计划+应急储备 | **风险应对计划确认** |

**规划链并行说明**：
- 环节1-2必须串行（范围→进度/成本）
- 环节3-6可部分并行：
  - 团队组建(3)和干系人管理(4)可并行
  - 采购规划(5)需在范围(1)之后
  - 风险管理(6)建议最后（需识别其他规划的输出作为风险输入）

**规划完成标志**：6个SKILL的输出全部完成 → 项目管理计划基线化

---

### 链路3：执行链

```
pm-project-delivery ←──→ pm-quality-assurance
     [交付管理]              [质量保证]
```

| 环节 | SKILL | 关键输出 | 衔接标志 |
|------|-------|---------|---------|
| 1 | pm-project-delivery | 执行进度+交付物+问题日志+偏差数据 | **按计划执行** |
| 2 | pm-quality-assurance | 审计报告+QC检查记录+改进措施 | **质量达标** |

**并行说明**：
- 两个SKILL同时运行，不是先后关系
- delivery负责"做什么+什么时候做"
- quality-assurance负责"做得对不对+怎么改进"

---

### 链路4：监控链

```
pm-performance-tracking ←──→ pm-change-management
     [绩效跟踪]                  [变更管理]
```

| 环节 | SKILL | 关键输出 | 衔接标志 |
|------|-------|---------|---------|
| 1 | pm-performance-tracking | 偏差分析+趋势预测+仪表板+状态报告 | **偏差可接受** |
| 2 | pm-change-management | CR评估+CCB审批+变更实施+基线更新 | **变更闭环** |

**触发规则**：
- performance-tracking发现偏差超阈值 → 触发change-management
- change-management变更实施后 → 回到performance-tracking验证效果
- 形成闭环：**监控→发现偏差→评估变更→实施变更→验证效果**

---

### 链路5：收尾链

```
pm-gov-acceptance ──────→ pm-project-closure
     [政府验收]               [项目收尾]
```

| 环节 | SKILL | 关键输出 | 衔接标志 |
|------|-------|---------|---------|
| 1 | pm-gov-acceptance | 四大验收+专项验收+验收批文 | **验收批文** |
| 2 | pm-project-closure | 合同关闭+归档+经验教训+运维交接+团队解散 | **项目正式关闭** |

**衔接标志**：验收批文是收尾链的"通行证"——没有验收批文不能启动正式收尾。

---

## 2条专项链路

### 专项链A：变更链

```
pm-project-delivery ──→ pm-change-management ──→ pm-project-delivery
     [记录偏差+发起CR]      [六维评估+CCB审批]       [执行变更]
```

| 步骤 | SKILL | 动作 | 输出 |
|------|-------|------|------|
| 1 | pm-project-delivery | 发现偏差，记录问题 | CR（变更请求） |
| 2 | pm-change-management | 六维影响评估+CCB审批 | 批准/拒绝决定 |
| 3a | pm-project-delivery | 实施批准的变更 | 变更后交付物 |
| 3b | pm-change-management | 验证变更结果 | 变更验证记录 |

---

### 专项链B：风险链

```
pm-risk-management ──→ pm-change-management
     [风险触发]           [变更评估]
```

| 步骤 | SKILL | 动作 | 输出 |
|------|-------|------|------|
| 1 | pm-risk-management | 风险触发（应急储备使用/风险发生） | 风险状态更新 |
| 2 | pm-change-management | 如需调整基线→走变更流程 | CR+CCB审批 |

---

## 跨轨能力调用：pd-user-research.insight-extraction（PT-012 子能力，供 JT 调用）

> **调用场景**：JT 技能（尤其 `pm-stakeholder-management` (JT-015)、`pm-requirements-scope` (JT-003)）在**会议/访谈/演示录音转写**场景下，可跨轨调用 PT 轨的 `pd-user-research.insight-extraction` 子能力，把转写文本自动抽成**决策/行动项/风险/需求**，再回到 JT 链路跟进。
> **衔接**：抽取出的"行动项/风险"→ `pm-stakeholder-management` 跟进；"需求/功能请求"→ `pm-requirements-scope` 入池。
> **边界（QG4）**：输入须为真实转写文本；若仅有会议纯文本且只需通用纪要 → 走 `meeting-minutes` (S-010)，不重复触发。

---

## 跨轨能力调用：pd-ai-research-workflow（PT-019，供 JT 调用）

> **调用场景**：JT 技能（尤其 `pm-requirements-scope` (JT-003)、`pm-stakeholder-management` (JT-015)）在需要**快速产出市场/竞品/用户研究结构化报告**时，可跨轨调用 PT 轨的 `pd-ai-research-workflow` (PT-019) 做 3-Tier AI 研究编排。
> **衔接**：研究产出的"需求机会"→ `pm-requirements-scope` 入池；"高管汇报/决策产出"→ `pm-stakeholder-management` 跟进。
> **边界（QG4）**：框架方法归 PT-003，本技能只管执行编排；涉及真实访谈/会议转写文本时先走 `pd-user-research.insight-extraction` (PT-012)。

---

## 全生命周期链路图

> **组织层（立项前）**：pm-it-governance (JT-020) 在项目全生命周期之前运行，评估 IT 战略对齐、价值、风险，为立项提供组织级输入；并在执行/收尾阶段提供 IT 审计与治理绩效维度。

```
┌─────────────────────────────────────────────────────────────┐
│                      项目全生命周期                            │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│  启动    │  规划    │  执行    │  监控    │  收尾            │
├──────────┼──────────┼──────────┼──────────┼─────────────────┤
│opportunity│requirements│delivery │performance│gov-acceptance  │
│    ↓     │    ↓      │    ↕    │tracking   │    ↓            │
│bid-proposal│schedule-cost│quality  │    ↕     │project-closure │
│    ↓     │    ↓      │assurance│change    │                 │
│integration│team-comm  │         │management│                 │
│(贯穿全程) │    ↓      │         │          │                 │
│          │stakeholder│         │          │                 │
│          │    ↓      │         │          │                 │
│          │procurement│         │          │                 │
│          │    ↓      │         │          │                 │
│          │risk-mgmt  │         │          │                 │
└──────────┴──────────┴──────────┴──────────┴─────────────────┘

衔接标志：Go决策 → 中标通知 → 项目章程 → 范围基线 → 执行基线 → 验收批文 → 项目关闭
注意：pm-integration贯穿启动→收尾全程，协调各子计划与整体变更
```

---

## 快速路由决策表

| 你在做什么 | 下一步 | 调用SKILL |
|-----------|--------|----------|
| 要上新 IT 系统 / 做 IT 体系评估 | 先做 IT 治理评估 | pm-it-governance |
| 收到项目线索 | 评估要不要做 | pm-project-opportunity |
| 决定投标 | 编制投标方案 | pm-bid-proposal |
| 收到招标文件需先解析 | 做招标文件解析（投标前置） | pm-tender-analysis |
| 中标了 | 签发项目章程+整合启动 | pm-integration |
| 项目章程签发 | 制定项目规划 | pm-requirements-scope（先） |
| 需求确认了 | 排进度算成本 | pm-schedule-cost |
| 进度排好了 | 组建团队 | pm-team-communication |
| 团队有了 | 管理干系人 | pm-stakeholder-management |
| 要采购了 | 编制采购方案 | pm-procurement-quality |
| 规划好了 | 识别风险 | pm-risk-management |
| 开始执行了 | 管理交付 | pm-project-delivery |
| 执行中要控质量 | 质量审计+QC | pm-quality-assurance |
| 发现偏差了 | 分析偏差 | pm-performance-tracking |
| 偏差超阈值 | 提变更请求 | pm-change-management |
| 要验收了 | 政府验收 | pm-gov-acceptance |
| 验收通过了 | 项目收尾 | pm-project-closure |
| 有会议/访谈录音转写要整理成行动项/决策 | 跨轨调用PD能力 | pd-user-research.insight-extraction (PT-012 子能力) |
| 要快速用 AI 产出市场/竞品/用户研究结构化报告 | 跨轨调用PD能力 | pd-ai-research-workflow (PT-019) |
| **不确定下一步** | **查这个表** | **pm-workflow-chains** |

---

## 核心原则

1. **链路有顺序**：前置SKILL的输出是后续SKILL的输入，不可跳步
2. **衔接看标志**：每个环节有明确的衔接标志（如"范围基线冻结"），未达标志不进入下一环节
3. **监控贯穿全程**：执行链和监控链是并行的，不是先后关系
4. **变更走闭环**：发现偏差→评估变更→实施变更→验证效果，不可跳过评估直接实施
5. **收尾看批文**：没有验收批文不能启动正式收尾
6. **风险可触发变更**：风险发生可能需要调整基线，走变更流程
7. **质量与交付并行**：交付管理和质量保证是执行阶段的双引擎
