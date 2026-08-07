---
name: pm-skills-reference
description: "【产品经理技能索引】65个产品经理(PdM)技能+36个链式工作流+8个领域插件——注意：本索引覆盖的是产品管理(Product Management)领域，非项目管理(Project Management)。如需项目管理技能，请使用 pm-project-opportunity / pm-bid-proposal / pm-requirements-scope 等 pm- 前缀的项目管理技能。当需要查找产品经理技能、了解产品管理框架、选择适用的产品方法论时使用。触发词：产品经理技能、PM技能市场、产品发现、产品战略、PRD、产品增长。"
---

# 产品经理技能市场：驱动更优产品决策的AI操作系统

> ⚠️ **重要区分**：本索引覆盖的是**产品经理(PdM)**技能——产品发现、战略、执行、GTM等。
> 如需**项目经理(PgM)**技能（立项、招投标、需求、进度、成本、风险、变更、验收等），请使用 `pm-project-opportunity`、`pm-bid-proposal`、`pm-integration`、`pm-requirements-scope`、`pm-schedule-cost`、`pm-team-communication`、`pm-stakeholder-management`、`pm-procurement-quality`、`pm-risk-management`、`pm-project-delivery`、`pm-quality-assurance`、`pm-change-management`、`pm-performance-tracking`、`pm-gov-acceptance`、`pm-project-closure`。
>
> 简记：**PdM = 做什么产品** | **PgM = 怎么交付项目**

> 65个PM技能 + 36个链式工作流，覆盖8大插件领域。从发现到战略，从执行到发布，从增长到数据。兼容 WorkBuddy、Claude Code、Cursor 等多种AI助手。

---

## 快速开始

有新想法？→ `/discover`  
需要战略清晰度？→ `/strategy`  
在写PRD？→ `/write-prd`  
在规划发布？→ `/plan-launch`  
在定义指标？→ `/north-star`

---

## 为什么需要PM技能市场？

通用AI给你文本，PM技能市场给你**结构**。

每个技能内嵌了经过验证的PM框架——发现、假设映射、优先级排序、战略规划——引导你一步步完成。你将获得 Teresa Torres、Marty Cagan、Alberto Savoia 等人的方法论，直接融入日常工作，而不是停留在书架上。

**结果：更优的产品决策，而不只是更快的文档产出。**

---

## 工作原理（技能、命令、插件）

**技能（Skills）** 是市场的基本构建块。每个技能为AI提供领域知识、分析框架或特定PM任务的引导式工作流。部分技能也可作为可复用的基础模块，被多个命令共享。

技能在对话中检测到相关场景时自动加载，无需显式调用。如需强制加载（如优先于通用知识），可使用 `/插件名:技能名` 或 `/技能名` 的方式调用。

**命令（Commands）** 是用户触发的端到端工作流，通过 `/命令名` 调用。它们将多个技能串联成完整流程。例如，`/discover` 将4个技能串在一起：头脑风暴想法 → 映射假设 → 优先级排序 → 设计实验。

**插件（Plugins）** 将相关技能和命令打包成可安装的单元。每个插件覆盖一个PM领域——发现、战略、执行等。安装整个市场即可一次性获得全部8个插件。

命令基于技能构建。部分技能服务于多个命令。部分技能（如 `prioritization-frameworks` 或 `opportunity-solution-tree`）是独立参考资源，AI可在任何时候引用——无需命令触发。

命令遵循PM工作流设计为可顺序衔接。每个命令完成后会建议相关的下一步命令——跟着提示走即可。

---

## 安装方式

### WorkBuddy（推荐）

将需要的技能目录复制到 `~/.workbuddy/skills/` 即可：

```bash
# 示例：安装产品战略技能
cp -r pm-product-strategy/skills/product-strategy ~/.workbuddy/skills/

# 批量安装所有技能
for plugin in pm-*/; do
  cp -r "$plugin/skills/"* ~/.workbuddy/skills/ 2>/dev/null
done
```

### 其他AI助手（仅技能）

`skills/*/SKILL.md` 文件遵循通用技能格式，兼容任何读取该格式的工具。

| 工具 | 使用方式 | 可用范围 |
|------|---------|---------|
| **Cursor** | 复制技能文件夹到 `.cursor/skills/` | 仅技能 |
| **Gemini CLI** | 复制技能文件夹到 `.gemini/skills/` | 仅技能 |
| **OpenCode** | 复制技能文件夹到 `.opencode/skills/` | 仅技能 |
| **Codex CLI** | 复制技能文件夹到 `.codex/skills/` | 仅技能 |

---

## 可用插件详情

<details>
<summary><strong>1. pm-product-discovery（产品发现）</strong> — 头脑风暴、实验、假设检验、OST、用户访谈（13个技能，5个命令）</summary>

**技能（13个）：**

- `brainstorm-ideas-existing` — 现有产品的多视角头脑风暴（PM、设计师、工程师）
- `brainstorm-ideas-new` — 新产品初期发现阶段头脑风暴
- `brainstorm-experiments-existing` — 为现有产品设计假设验证实验
- `brainstorm-experiments-new` — 为新产品设计精益创业预型（Alberto Savoia方法论）
- `identify-assumptions-existing` — 识别价值、可用性、可行性、可实现性四类风险假设
- `identify-assumptions-new` — 识别8类风险假设（含GTM、战略、团队）
- `prioritize-assumptions` — 使用影响×风险矩阵排序假设，附带实验建议
- `prioritize-features` — 基于影响力、工作量、风险和战略对齐度排序功能列表
- `analyze-feature-requests` — 按主题和战略匹配度分析和归类客户功能请求
- `opportunity-solution-tree` — 构建机会-解决方案树（Teresa Torres方法论）：结果→机会→方案→实验
- `interview-script` — 生成含JTBD追问的结构化客户访谈脚本
- `summarize-interview` — 将访谈记录总结为JTBD洞察、满意度信号和行动项
- `metrics-dashboard` — 设计含北极星指标、输入指标和告警阈值的产品指标看板

**命令（5个）：**

- `/discover` — 完整发现周期：头脑风暴→假设映射→优先级排序→实验设计
- `/brainstorm` — 多视角头脑风暴（`ideas|experiments` × `existing|new`）
- `/triage-requests` — 分析并排序一批功能请求
- `/interview` — 准备访谈脚本或总结访谈记录（`prep|summarize`）
- `/setup-metrics` — 设计产品指标看板

**使用示例：**

技能触发：
- `我们AI写作助手最危险的假设是什么？`
- `帮我构建一个提升用户激活的机会-解决方案树`
- `帮我排一下这12个企业客户的功能请求 [附CSV]`

命令触发：
- `/discover 面向远程团队的AI会议摘要工具`
- `/brainstorm experiments existing — 我们需要降低新用户引导流程的流失率`
- `/interview prep — 我们要访谈企业采购人员了解他们的采购工作流`

</details>

<details>
<summary><strong>2. pm-product-strategy（产品战略）</strong> — 愿景、商业模式、定价、竞争格局（12个技能，5个命令）</summary>

产品战略、愿景、商业模式、定价和宏观环境分析。覆盖从愿景构思到竞争格局扫描的完整战略工具箱。

**技能（12个）：**

- `product-strategy` — 综合9段产品战略画布（愿景→护城河）
- `startup-canvas` — 创业画布（产品战略9段 + 商业模式），BMC和精益画布的替代方案
- `product-vision` — 撰写鼓舞人心、可实现、有情感共鸣的产品愿景
- `value-proposition` — 6段JTBD价值主张（Who、Why、What before、How、What after、Alternatives）
- `lean-canvas` — 面向创业公司和新产品的精益画布
- `business-model` — 9大构建块的商业模式画布
- `monetization-strategy` — 头脑风暴3-5个变现策略及验证实验
- `pricing-strategy` — 定价模型、竞争分析、支付意愿和价格弹性
- `swot-analysis` — SWOT分析及可执行建议
- `pestle-analysis` — 宏观环境分析：政治、经济、社会、技术、法律、环境
- `porters-five-forces` — 五力竞争分析（竞争、供应商、买家、替代品、新进入者）
- `ansoff-matrix` — 市场与产品交叉的增长策略矩阵

**命令（5个）：**

- `/strategy` — 创建完整的9段产品战略画布
- `/business-model` — 探索商业模式（`lean|full|startup|value-prop|all`）
- `/value-proposition` — 使用6段JTBD模板设计价值主张
- `/market-scan` — 宏观环境分析：SWOT + PESTLE + 波特五力 + 安索夫矩阵
- `/pricing` — 设计定价策略，含竞争分析和实验方案

**使用示例：**

技能触发：
- `比较精益画布、商业模式画布和创业画布，我的平台型创业项目该用哪个？`
- `为面向非英语母语用户的AI写作助手设计价值主张`
- `对项目管理SaaS市场做一次波特五力分析`

命令触发：
- `/strategy 面向广告公司的B2B项目管理工具`
- `/business-model startup — 面向非英语母语用户的AI写作工具`
- `/value-proposition 面向企业客户的SaaS入职引导工具`

</details>

<details>
<summary><strong>3. pm-execution（产品执行）</strong> — PRD、OKR、路线图、Sprint、回顾会、发版说明、干系人管理（15个技能，10个命令）</summary>

日常产品管理：PRD、OKR、路线图、Sprint、回顾会、发版说明、事前验尸、干系人管理、用户故事和优先级框架。

**技能（15个）：**

- `create-prd` — 综合8段PRD模板
- `brainstorm-okrs` — 与公司目标对齐的团队级OKR
- `outcome-roadmap` — 将功能列表转化为结果导向的路线图
- `sprint-plan` — Sprint规划：产能估算、故事选取、风险识别
- `retro` — 结构化Sprint回顾引导
- `release-notes` — 从工单、PRD或变更日志生成用户发版说明
- `pre-mortem` — 风险分析（老虎/纸老虎/大象分类法）
- `stakeholder-map` — 权力×兴趣网格及定制化沟通方案
- `summarize-meeting` — 会议记录→决策+行动项
- `user-stories` — 遵循3C原则和INVEST标准的用户故事
- `job-stories` — 任务故事：当[场景]，我想要[动机]，以便[结果]
- `wwas` — Why-What-Acceptance格式的产品待办项
- `test-scenarios` — 测试场景：正常路径、边界情况、错误处理
- `dummy-dataset` — 真实模拟数据集（CSV/JSON/SQL/Python格式）
- `prioritization-frameworks` — 9种优先级框架参考指南（机会评分、ICE、RICE、MoSCoW、Kano等）

**命令（10个）：**

- `/write-prd` — 从功能想法或问题陈述创建PRD
- `/plan-okrs` — 头脑风暴团队级OKR
- `/transform-roadmap` — 将功能路线图转化为结果导向路线图
- `/sprint` — Sprint生命周期（`plan|retro|release`）
- `/pre-mortem` — 对PRD或发布计划进行事前验尸风险分析
- `/meeting-notes` — 将会议记录整理为结构化笔记
- `/stakeholder-map` — 绘制干系人地图并创建沟通方案
- `/write-stories` — 将功能拆分为待办项（`user|job|wwa`）
- `/test-scenarios` — 从用户故事生成测试场景
- `/generate-data` — 创建真实模拟数据集

**使用示例：**

技能触发：
- `50个待办项应该用哪种优先级框架？`
- `帮我们的平台迁移项目绘制干系人地图`
- `机会评分、ICE和RICE有什么区别？`

命令触发：
- `/write-prd 减少告警疲劳的智能通知系统`
- `/sprint retro — 这是我们上次Sprint的记录`
- `/write-stories job — 将"团队看板"功能拆分为任务故事`

</details>

<details>
<summary><strong>4. pm-market-research（市场研究）</strong> — 用户画像、细分、旅程地图、市场规模、竞品分析（7个技能，3个命令）</summary>

用户研究与竞争分析：用户画像、细分、旅程地图、市场规模估算、竞品分析和反馈分析。

**技能（7个）：**

- `user-personas` — 从研究数据中创建精细化用户画像
- `market-segments` — 识别3-5个客户细分（人口统计、JTBD、产品匹配度）
- `user-segmentation` — 根据行为、JTBD和需求从反馈数据中细分用户
- `customer-journey-map` — 端到端旅程地图（阶段、触点、情绪、痛点）
- `market-sizing` — TAM/SAM/SOM（自上而下+自下而上双重估算）
- `competitor-analysis` — 竞品优势、劣势和差异化机会分析
- `sentiment-analysis` — 用户反馈的情感分析和主题提取

**命令（3个）：**

- `/research-users` — 建立用户画像、细分用户、绘制客户旅程
- `/competitive-analysis` — 分析竞争格局
- `/analyze-feedback` — 用户反馈的情感分析和细分洞察

**使用示例：**

技能触发：
- `估算AI代码审查工具在美国市场的TAM/SAM/SOM`
- `为我们电商结账流程创建客户旅程地图`
- `按行为和需求对这些问卷受访者进行细分 [附CSV]`

命令触发：
- `/research-users 我们有12位健身应用用户的访谈数据`
- `/competitive-analysis 设计工具领域的Figma竞品`
- `/analyze-feedback 这是Q4的200条NPS反馈 [附文件]`

</details>

<details>
<summary><strong>5. pm-data-analytics（数据分析）</strong> — SQL生成、同期群分析、A/B测试分析（3个技能，3个命令）</summary>

面向PM的数据分析：SQL查询生成、同期群分析和A/B测试分析。

**技能（3个）：**

- `sql-queries` — 从自然语言生成SQL（BigQuery、PostgreSQL、MySQL）
- `cohort-analysis` — 同期群的留存曲线、功能采纳和参与度趋势
- `ab-test-analysis` — 统计显著性、样本量验证和发布/扩展/停止建议

**命令（3个）：**

- `/write-query` — 从自然语言生成SQL查询
- `/analyze-cohorts` — 对用户参与度数据进行同期群分析
- `/analyze-test` — 分析A/B测试结果

**使用示例：**

技能触发：
- `95%置信度、2% MDE需要多大样本量？`
- `订阅类应用应该跟踪哪些留存指标？`

命令触发：
- `/write-query 显示2025年Q4按国家分组的月活跃用户数（BigQuery）`
- `/analyze-test 这是我们结账流程A/B测试的结果 [附CSV]`
- `/analyze-cohorts 1月与2月注册用户的周留存对比`

</details>

<details>
<summary><strong>6. pm-go-to-market（市场进入）</strong> — 滩头细分、ICP、消息策略、增长循环、GTM模式、竞争战卡（6个技能，3个命令）</summary>

市场进入战略：滩头细分、理想客户画像、消息策略、增长循环、GTM模式和竞争战卡。

**技能（6个）：**

- `gtm-strategy` — 完整GTM战略：渠道、消息策略、成功指标和发布计划
- `beachhead-segment` — 识别第一个滩头市场细分
- `ideal-customer-profile` — ICP：人口统计、行为、JTBD和需求
- `growth-loops` — 设计可持续增长循环（飞轮）
- `gtm-motions` — 评估GTM模式与工具（产品驱动、销售驱动等）
- `competitive-battlecard` — 销售级竞争战卡（异议处理、制胜策略）

**命令（3个）：**

- `/plan-launch` — 从滩头细分到发布计划的完整GTM战略
- `/growth-strategy` — 设计增长循环并评估GTM模式
- `/battlecard` — 创建竞争战卡

**使用示例：**

技能触发：
- `开发者生产力工具的最佳滩头细分是什么？`
- `为有免费版的B2B SaaS设计增长循环`
- `定义AI驱动HR筛选平台的ICP`

命令触发：
- `/plan-launch 面向中型工程团队的AI代码审查工具`
- `/battlecard 我们的CRM在SMB市场对比Salesforce`
- `/growth-strategy 连接自由职业者和创业公司的双边平台`

</details>

<details>
<summary><strong>7. pm-marketing-growth（营销增长）</strong> — 营销创意、定位、价值主张、命名、北极星指标（5个技能，2个命令）</summary>

产品营销与增长：营销创意、定位、价值主张陈述、产品命名和北极星指标。

**技能（5个）：**

- `marketing-ideas` — 创意且高性价比的营销方案（含渠道和消息策略）
- `positioning-ideas` — 区别于竞争对手的产品定位
- `value-prop-statements` — 面向营销、销售和用户引导的价值主张陈述
- `product-name` — 与品牌价值和受众对齐的产品命名头脑风暴
- `north-star-metric` — 北极星指标+输入指标（含业务博弈分类法）

**命令（2个）：**

- `/market-product` — 头脑风暴营销创意、定位、价值主张和产品名称
- `/north-star` — 定义北极星指标及支撑性输入指标

**使用示例：**

技能触发：
- `头脑风暴5个区别于Notion的定位角度`
- `双边市场平台适合用什么北极星指标？`
- `为销售团队的PPT生成价值主张陈述`

命令触发：
- `/market-product 面向电商经理的B2B分析看板`
- `/north-star 连接自由职业者和客户的双边平台`

</details>

<details>
<summary><strong>8. pm-toolkit（PM工具箱）</strong> — 简历审查、法律文件、校对（4个技能，5个命令）</summary>

核心产品工作之外的PM实用工具：简历审查、法律文件和校对。

**技能（4个）：**

- `review-resume` — 基于10项最佳实践的PM简历审查与优化（XYZ+S公式、关键词、结构）
- `draft-nda` — 含适格法域条款的保密协议
- `privacy-policy` — 覆盖GDPR/CCPA合规的隐私政策
- `grammar-check` — 语法、逻辑和行文流畅度检查及精准修正

**命令（5个）：**

- `/review-resume` — 全面的PM简历审查
- `/tailor-resume` — 针对特定JD定制简历
- `/draft-nda` — 起草保密协议
- `/privacy-policy` — 起草隐私政策
- `/proofread` — 检查语法、逻辑和行文流畅度

**使用示例：**

技能触发：
- `根据最佳实践审查我的PM简历 [附PDF]`
- `检查这篇产品公告的语法和清晰度`

命令触发：
- `/review-resume [附PM简历]`
- `/tailor-resume [附简历+粘贴JD]`
- `/proofread 这是我们Q1投资人更新报告的草稿`

</details>

---

## 方法论来源

本技能市场随产品实践和AI能力持续演进。所选技能基于以下专家的成果：

- Teresa Torres — 《持续发现习惯》
- Marty Cagan — 《启示录》与《转型》
- Alberto Savoia — 《对的那个》
- Dan Olsen — 《精益产品实战》
- Roger L. Martin — 《为赢而战》
- Ash Maurya — 《精益创业实战》
- Strategyzer — 《商业模式新生代》与《价值主张设计》
- Christina Wodtke — 《彻底聚焦》
- Anthony W. Ulwick — 《待完成的任务》
- Alistair Croll & Benjamin Yoskovitz — 《精益数据分析》
- Sean Ellis — 《增长黑客》
- Maja Voje — 《GTM战略家》

由 Paweł Huryn（来自 The Product Compass Newsletter）策划编排。

---

## 使用提示

1. **WorkBuddy中技能自动触发**：当对话涉及匹配的场景时，相应技能会自动加载
2. **强制加载**：如需优先使用技能而非通用知识，用 `/技能名` 显式调用
3. **中文场景**：部分技能原文为英文，建议安装中文翻译版以获得更好体验（见本索引中标注为"中文可用"的技能）
4. **按需安装**：不必一次装完65个技能——根据当前工作需求选择性安装，保持技能库精简
