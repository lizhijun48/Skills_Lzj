# 问题类型定义（Problem Types / Issue Types）— v2 标准框架版

> 所有 SKILL 的路由和调度都基于问题类型 + 阶段归属。
> 用户带着一个问题进来，系统先识别阶段（P1-P6），再按问题类型路由到具体 SKILL。
> 更新：2026-06-06

---

## 通用问题类型（跨领域）

| Issue Type 标签 | 中文名称 | 主阶段 | 标准出处 | 用户常见说法（信号词） | 需要的核心能力 | MVP 交付物 |
|----------------|---------|:---:|---------|---------------------|--------------|-----------|
| PROBLEM_UNCLEAR | 问题定义不清 | P1 | PMP.Initiating / NPDP.Discovery | "到底要解决什么""老板说要做X但…" | 问题诊断 / 框架拆解 | 问题陈述 + 假设树 + 需补齐信息清单 |
| PRIORITY_MUD | 优先级混乱 | P3 | PMP.Planning.Scope / NPDP.Portfolio | "需求太多""资源不够""排期吵不完" | 优先级框架 + 约束澄清 | 优先级矩阵 + 砍/延/做三档 + 风险说明 |
| SCOPE_CREEP | 范围蔓延 | P3/P5 | PMP.Planning.Scope + M&C.Scope | "需求又加回来了""MVP 到底砍什么" | 范围界定 + 变更控制 | 范围约束表 + 砍留清单 |
| VALUE_PROP_BLUR | 价值主张模糊 | P2 | NPDP.Strategy / NPDP.Market Research | "跟竞品差不多""卖点讲不清" | 价值定位 / 受众细分 | 受众-痛点-收益草稿 + 差异化假设 |

## 产品经理领域

| Issue Type 标签 | 中文名称 | 主阶段 | 标准出处 | 用户常见说法（信号词） | 需要的核心能力 | MVP 交付物 |
|----------------|---------|:---:|---------|---------------------|--------------|-----------|
| USER_JOURNEY_FRICTION | 旅程断点 | P1 | NPDP.Market Research / NPDP.Tools | "转化掉了""流程太长""用户在XX步流失" | 旅程诊断 + 假设归因 | 旅程图快照 + 根因候选 + 验证方法 |
| MARKET_CONFUSION | 市场定位不清 | P2 | NPDP.Strategy / NPDP.Market Research | "竞品怎么打的""我们优势在哪" | 竞品分析 / 定位梳理 | 竞品对比矩阵 + 定位陈述 |
| DELIVERY_WRITING | 交付物撰写 | P4 | PMP.Executing / NPDP.Development | "帮我写 PRD""需求文档""功能说明" | 规格写作 + 边界异常 | 结构化 PRD / 验收条件 |
| EXPERIMENT_NEEDED | 需要验证 | P5 | NPDP.Testing / PMP.M&C | "这个方案靠不靠谱""怎么低成本验证" | 实验设计 / AB测试 | 验证计划 + 成功标准 |
| METRICS_CONFUSION | 指标困惑 | P5 | NPDP.Metrics / PMP.M&C | "数据说明不了问题""口径不一致" | 指标定义 / 漏斗分析 | 指标口径表 + 异常解读 |

## AI/技术领域

| Issue Type 标签 | 中文名称 | 主阶段 | 标准出处 | 用户常见说法（信号词） | 需要的核心能力 | MVP 交付物 |
|----------------|---------|:---:|---------|---------------------|--------------|-----------|
| SYSTEM_DESIGN | 系统设计 | P3 | PMP.Planning / 一建.项目管理 | "架构怎么搭""模块怎么分" | 架构设计 / 模块拆解 | 架构图 + 模块职责说明 |
| WORKFLOW_OPTIMIZATION | 流程优化 | P4/P5 | PMP.Executing / 一建.施工管理 | "效率太低""流程太繁琐" | 流程分析 + 自动化 | 优化前后对比 + 自动化方案 |
| CODE_QUALITY | 代码质量 | P5 | PMP.M&C.Quality | "代码太乱""怎么重构" | 代码审查 / 重构策略 | 重构方案 + 优先级排序 |

## 行业/商业领域

| Issue Type 标签 | 中文名称 | 主阶段 | 标准出处 | 用户常见说法（信号词） | 需要的核心能力 | MVP 交付物 |
|----------------|---------|:---:|---------|---------------------|--------------|-----------|
| BUSINESS_MODEL | 商业模式 | P2 | NPDP.Strategy / NPDP.Portfolio | "怎么赚钱""盈利模式不清" | 商业模式画布 / 财务模型 | 商业模式图 + 关键假设 |
| LEGAL_COMPLIANCE | 法律合规 | CX-1 | 一建.法规 / NPDP.IP | "这样合不合法""合规风险" | 法律条文 / 合规框架 | 合规风险清单 + 建议 |
| BIDDING_PROCUREMENT | 招投标 | P3/P4 | PMP.Planning.Procurement / 一建.招投标 | "写标书""投标分析" | 标书写作 / 竞标策略 | 标书框架 + 评分分析 |
| COST_ENGINEERING | 工程造价 | CX-2 | 一建.经济 / PMP.Cost | "预算多少""造价估算" | 工程经济 / 财务分析 | 投资估算 + 经济评价 |

## 元能力/基础设施

| Issue Type 标签 | 中文名称 | 主阶段 | 标准出处 | 用户常见说法（信号词） | 需要的核心能力 | MVP 交付物 |
|----------------|---------|:---:|---------|---------------------|--------------|-----------|
| SKILL_CREATION | 技能创建 | CX-8 | 独立 | "怎么做一个新 SKILL""写个 Prompt" | Prompt 工程 / 技能规范 | 标准化 SKILL.md |
| KNOWLEDGE_SYSTEM | 知识体系 | CX-8 | 独立 | "怎么组织知识""知识库怎么搭" | 知识工程 / 分类法 | 知识地图 + IO 契约 |
| AGENT_ORCHESTRATION | 智能体编排 | CX-8 | 独立 | "多个 Agent 怎么协作""调度逻辑" | 多智能体架构 / 路由 | 编排方案 + 调度规则 |
| CONTENT_CREATION | 内容创作 | P4 | PMP.Executing | "帮我写文章""生成内容" | 写作 + 格式化 | 文章/报告/文案 |
| RESEARCH_ANALYSIS | 研究分析 | P1/P2 | NPDP.Market Research | "帮我研究一下""分析趋势" | 信息收集 + 结构化分析 | 分析报告 + 洞察摘要 |

---

## 路由规则

1. **先阶段，后类型：** Dispatcher 先识别用户问题属于 P1-P6 哪个阶段，再在该阶段内按 Issue Type 路由到具体 Skill
2. **信号词匹配：** 每个 Issue Type 的信号词用于第一轮快速匹配
3. **追问兜底：** 如果信号词匹配到多个 Issue Type，通过追问澄清
4. **CX 随时可调用：** CX 类问题类型不受阶段限制，任何阶段均可直接调用

> 此文件可随体系演进持续扩展。
> 新增 Issue Type 时，必须标注主阶段和标准出处。
> 框架基础：[STANDARDS_FRAMEWORK.md](../STANDARDS_FRAMEWORK.md)
