---
name: pd-ai-research-workflow
version: 1.0.0
description: AI 驱动的市场研究编排——把市场/竞品/用户研究用 AI 工具从"数周"压到"分钟级"。覆盖 3-Tier 研究法（快问快答 LLM CLI / 财务对标财经终端 / 自主深研多步研究 agent）、8 个多步研究工作流 prompt（可行性/竞品/用户研究综合/路线图优先级/高管汇报/技术探针/市场进入/PMF 验证）、3 种组合编排范式。执行层，框架方法请转 pd-market-research(PT-003)。触发词：AI 研究编排、市场研究自动化、AI 竞品情报、研究工作流、Gemini 研究、OpenBB 财务对标、Deep Researcher、自主研究 agent、多步研究 prompt、研究自动化、AI 市场研究。
governance_id: "PT-019"
triggers:
  - AI 研究编排
  - 市场研究自动化
  - AI 竞品情报
  - 研究工作流
  - Gemini 研究
  - OpenBB 财务对标
  - Deep Researcher
  - 自主研究 agent
  - 多步研究 prompt
  - 研究自动化
  - AI 市场研究
---

# pd-ai-research-workflow · AI 驱动的市场研究编排

> **核心定位**：回答"怎么用 AI 工具把研究快速跑出来"——它是 **执行/编排层**，不是框架层。
> **与 PT-003 的边界（关键）**：`pd-market-research`(PT-003) 负责"用什么**框架/方法**"（TAM/SAM/SOM、SWOT、波特五力、PESTLE、12 种研究方法…）；本技能负责"用什么 **AI 工具/编排**把这些框架真正跑出来"。两者正交、互补，不重复。
> ⚠️ 若用户问"市场规模怎么算 / 竞品分析用什么框架" → 转 **PT-003**；若问"怎么快速用 AI 做竞品情报 / 编排一个研究工作流" → 用**本技能**。

## 能力模块：AI 研究编排

### 1. 功能
把"市场/竞品/用户研究"从人工数周压缩到分钟级，提供三类可复用资产：
- **3-Tier 研究法**：快问快答（T1，任意 LLM CLI）→ 财务对标（T2，财经数据终端）→ 自主深研（T3，多步研究 agent），按投入/深度递进。
- **8 个多步研究工作流 prompt**：可行性分析、竞品深研、用户研究综合、路线图优先级、高管汇报、技术探针、市场进入、PMF 验证——每个都是"数据采集→模式识别→战略应用"三段式，带明确交付物。
- **3 种组合编排范式**：竞品分析流水线、市场进入决策框架、产品策略验证——把三层能力叠加成端到端研究链。

### 2. 解决的问题
- **研究太慢太贵**：传统市场/竞品研究靠人工，数周起步；本技能用 AI 编排把周期压到分钟~小时级。
- **靠直觉拍脑袋**：提供结构化、可复现的研究流程与交付物模板，让决策有证据支撑。
- **框架有了但跑不起来**：PT-003 给了方法论，但"怎么快速产出一份竞品情报/市场机会报告"缺执行抓手——本技能补这一环。
- **研究不可复用**：多步工作流 prompt 固化了分析骨架，不同 PM 跑出来口径一致。

### 3. 什么情况下使用
**✅ 使用本技能当：**
- 需要快速产出竞品情报、市场机会、用户研究综合等**结构化研究报告**；
- 已有明确研究对象（竞品名/市场/功能），要 AI 辅助完成多步分析；
- 要编排"T1→T2→T3"分层研究，或复用 8 个标准工作流之一；
- 董事会/立项/融资前需要快速补齐市场与竞品证据。

**❌ 不使用本技能（转其他技能）当：**
- 问"用什么**框架/方法**做市场研究"（TAM/SWOT/五力…）→ **PT-003**；
- 输入是**真实访谈/会议录音转写文本**、要抽取结构化洞察 → **PT-012.insight-extraction**；
- 研究结论要落到 **Go/No-Go 决策** → **PT-004**；
- 要生成合成/虚构用户数据来"替代"真实用户研究 → **禁止**（见 §4 红线）。

### 4. 红线与注意事项
- **禁止用随机合成数据替代真实用户研究**：原项目 8 个工作流 prompt 中含"Generate synthetic user data / personas"步骤。按本体系原则（PT-012），Persona 必须基于 5+ 次真实访谈；此类步骤**必须替换为"基于真实访谈/转录洞察"（见 PT-012 insight-extraction）**，或仅作无真实用户时的占位并明确标注。
- **PoL probe（Proof-of-Life 探针）映射**：原项目的自创框架，在本体系中对应"假设验证探针"，可衔接 PT-003 的假设识别验证 / PT-012 的访谈设计。
- **工具无关**：T1/T2/T3 的工具（Gemini CLI / OpenBB / Deep Researcher）仅为代表性实现，可替换为任意等价 LLM CLI / 财经数据终端 / 多步研究 agent，prompt 结构通用。
- **始终校验**：AI 结论须用领域知识交叉验证，避免信息茧房与确认偏误（详见 references/combination-paradigms.md §研究质量与验证）。

---

## 3-Tier 研究法速览

| 层 | 代表工具（可替换） | 投入 | 适用 | 详细 |
|----|------------------|------|------|------|
| **T1 快问快答** | 任意 LLM CLI（Gemini/Claude/ChatGPT） | 5 分钟 | 董事会前补背景、PRD 竞品段、策略会实时查资料 | `references/research-tiers.md` §T1 |
| **T2 财务对标** | 财经数据终端（OpenBB/手动财报） | 30 分钟 | 竞品财务背景、融资对标、伙伴财务稳定性 | `references/research-tiers.md` §T2 |
| **T3 自主深研** | 多步研究 agent（Deep Researcher/LangGraph/ChatGPT Deep Research） | 数小时 | 重大决策的咨询级报告、年度战略、融资、pivot | `references/research-tiers.md` §T3 |

## 8 个多步研究工作流速览

| # | 工作流 | 核心交付物 | 详细 |
|---|--------|-----------|------|
| 1 | 功能可行性分析 | 技术复杂度评分(1-10)、风险矩阵、Go/No-Go | `references/goose-workflows.md` §1 |
| 2 | 竞品情报深研 | 竞争地图、SWOT、5 项战略行动 | §2 |
| 3 | 用户研究综合 | 痛点频次、功能机会评分、路线图建议 | §3 |
| 4 | 路线图优先级 | 多因子评分矩阵、排名清单、置信区间 | §4 |
| 5 | 高管汇报构建 | 汇报包、演讲备注、FAQ | §5 |
| 6 | 技术探针规划 | 探针成功标准、最小可行测试、复盘模板 | §6 |
| 7 | 市场进入分析 | 进入风险、GTM 策略、验证实验 | §7 |
| 8 | PMF 验证 | 价值实现点、PMF 指标框架、改进优先级 | §8 |

> 每个工作流均为"三段式"（数据采集→模式识别→战略应用），prompt 结构工具无关；使用前务必按 §4 红线处理"合成数据"步骤。

## 3 种组合编排范式速览

- **竞品分析流水线**：T1 快览 → T2 财务 → T3 深研 → 合成高管简报
- **市场进入决策框架**：T3 机会评估 → T2 玩家财务 → T1 假设验证 → Go/No-Go
- **产品策略验证**：T1 竞品功能 → T3 客户需求缺口 → T2 商业模式财务 → 差异化结论

详见 `references/combination-paradigms.md`。

---

## 调用接口约定（供其他 SKILL 调用）

- **能力名**：`pd-ai-research-workflow`
- **输入**：`{ research_objective, tier_preference, target (competitor/market/feature), depth, output_format }`
- **输出**：`{ report (structured markdown), sources, confidence, recommended_next_action }`
- **衔接关系**：
  - → `pd-market-research`(PT-003)：框架/方法层，本技能产出的"框架选择"应回查 PT-003；
  - → `pd-go-nogo`(PT-004)：研究结论要落到 Go/No-Go 决策时；
  - → `pd-user-research.insight-extraction`(PT-012)：若已有真实访谈/会议转写文本，先抽取洞察再喂入本研究；
  - → `pm-requirements-scope`(JT-003)：研究产出的需求机会入需求池；
  - → `pm-stakeholder-management`(JT-015)：高管汇报/决策类产出需干系人跟进。

---

## 参考资料

| 文件 | 内容 |
|------|------|
| `references/research-tiers.md` | 3-Tier 研究法完整 prompt 模板与命令流（工具无关化） |
| `references/goose-workflows.md` | 8 个多步研究工作流 prompt 结构与交付物（含合成数据红线） |
| `references/combination-paradigms.md` | 3 种组合范式 + 研究质量与验证原则 |
