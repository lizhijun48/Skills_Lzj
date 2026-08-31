# SKILL 重叠分析与合并策略（v4 — 双轨融合版）

> 基于 139 个 Skill 标准化盘点表（含 2 个 PT-P6 Skill + 1 个 data-analyst）+ 逐文件深度处理逻辑比对。
> 框架基础：PMP + NPDP + 一级建造师 三标准融合 · 产品+项目双轨模型。
> 详见 [STANDARDS_FRAMEWORK.md](STANDARDS_FRAMEWORK.md)
> 更新：2026-06-06

**框架版本说明：** 本文档各群组表格中的"所属层"沿用分析时的旧标签（D/S/E/V/I），与新框架的对应关系如下：

| 旧标签 | 新阶段 | 含义 |
|--------|--------|------|
| D（发现诊断） | **P1** 识别 | 立项识别、用户洞察、机会发现 |
| S（方案权衡） | **P2** 论证 / **P3** 规划 | 可行性论证 或 方案设计（视具体 Skill） |
| E（验证证据） | **P5** 控制 | 监控验证、指标分析、实验评估 |
| V（交付协同） | **P4** 执行 | 实施交付、文档生成、任务执行 |
| I（基础设施） | **CX** 专业知识域 | 贯穿层（法律CX-1/经济CX-2/Agent工具CX-8 等） |

---

**核心原则：合并 ≠ 参数化。当处理逻辑因场景产生结构性差异时，必须定义显式分支而非简单合并。**

---

## 设计原则：场景分支判定规则

在决定是否合并两个看似相似的 Skill 之前，必须依次回答三个问题：

1. **处理步骤是否结构相同？** — 步骤数量、顺序、判断条件是否一致（仅文字表述不同不算差异）
2. **输入→输出的映射关系是否同构？** — 同样的输入字段是否能喂入同样的处理管线
3. **差异是否仅为参数级？** — 差异是"填不同值"还是"走不同路径"

判定矩阵：

| 问题 1 | 问题 2 | 问题 3 | 结论 |
|:---:|:---:|:---:|------|
| 是 | 是 | 是 | **安全合并**，用 `context` 参数切换 |
| 是 | 是 | 否 | **合并 + 显式分支**，定义 branch 触发条件 |
| 否 | 否 | — | **保持独立**，仅统一 IO 接口规范 |
| 是 | 否 | — | **管线串联**，上游输出 = 下游输入 |

---

## 总览：14 个重叠群组（修订版）

| 群组 | Skill 数 | 重叠性质 | 策略（修订） | 合并后 | 减少 |
|------|:---:|---------|---------|:---:|:---:|
| A. 商业模式画布变体 | 3 | 块集合结构不同 | **保持独立 + 统一 IO** | 3 | 0 |
| B. 产品发现 existing/new | 6 | 同结构，处理元素切换 | **合并 + 场景分支** | 3 | -3 |
| C. Backlog 条目格式 | 3 | 同结构，模板差异 | **合并 + 格式分支** | 1 | -2 |
| D. 系统控制器 | 6 | 同功能不同平台/架构 | **合并 + 平台分支** | 2 | -4 |
| E. Agent 编排元框架 | 7 | 同层高度理论重叠 | **合并** | 2 | -5 |
| F. 优先级排序 | 4 | 同层同问题类型 | **部分合并** | 2 | -2 |
| G. GTM 上市策略 | 4 | gtm-motions ≈ gtm-strategy | **合并 + 深度分支** | 3 | -1 |
| H. 招投标 | 3 | bidding ≈ bid-assistant | **合并** | 2 | -1 |
| I. 用户研究 | 6 | 画像/分群可合并；访谈独立 | **部分合并** | 5 | -1 |
| J. 价值主张/定位 | 5 | 管线上下游关系 | **保持独立 + 管线串联** | 5 | 0 |
| K. 法律合规 | 4 | 法律域重叠 | **合并** | 2 | -2 |
| L. 竞品分析 | 3 | 不同角色 | **保持独立** | 3 | 0 |
| M. 战略分析框架 | 5 | 不同方法论 | **保持独立** | 5 | 0 |
| N. 知识参考库 | 6 | 不同领域 | **保持独立** | 6 | 0 |

**合计减少约 21 个 Skill（139 → 118）**

> v1 → v2 变化说明：群组 A 从合并改为独立（+2），群组 J 从部分合并改为独立（+2），群组 I 减少合并 1 个（+1），总计比 v1 多保留 5 个 Skill。这是因为深度分析发现这些群组之间的差异不是参数级的，而是结构级的。

---

## A. 商业模式画布变体 — 修订：保持独立 + 统一 IO 接口

**涉及 Skill：**
| # | 名称 | 描述 | 所属层 |
|---|------|------|--------|
| 56 | business-model | 9模块商业模式画布 BMC | S |
| 57 | lean-canvas | 精益画布验证创业假设 | S |
| 64 | startup-canvas | 新产品专用画布 11 模块 | S |

**深度分析发现 — 为什么不能简单合并：**

三者的模块（block）集合存在结构性差异，不是"同一个画布换几个格子"：

| 维度 | BMC (#56) | Lean Canvas (#57) | Startup Canvas (#64) |
|------|-----------|-------------------|---------------------|
| 独有模块 | 关键合作伙伴、关键活动、关键资源、客户关系 | 问题、解决方案、关键指标、不公平优势 | 愿景、非目标、权衡取舍、防御策略 |
| 共有模块 | 客户细分、价值主张、渠道通路、收入来源、成本结构 | ← 同左 | ← 同左 |
| 模块总数 | 9 | 9 | 11 |
| 处理重心 | 运营完整性分析 | 假设验证速度 | 战略一致性+商业可行性 |
| 评估标准 | 9 模块间的逻辑自洽 | 风险最高的 3 个假设 | 愿景-商业-技术三角一致性 |

如果强行参数化合并，合并后的 Skill 内部需要写大量 `if branch == BMC then ... else if branch == lean then ...` 的条件分支，实质上等于把三个 Skill 的代码塞进一个文件——这不是合并，而是伪装成合并的拆分。

**策略：保持三个独立 Skill，统一 IO 接口规范**

```yaml
# 统一 IO 接口（三个画布 Skill 共同遵守）
input:
  - product_description: string      # 产品/服务描述
  - market_context: string           # 市场背景
  - stage: mature | startup | new_product_line  # 当前阶段

output:
  - filled_canvas: structured_doc    # 填写完成的画布
  - key_assumptions: list            # 关键假设标注
  - validation_backlog: list         # 待验证项清单

dispatch_hint: |
  Dispatcher 根据 stage 字段路由：
  - mature → business-model (BMC)
  - startup + 需验证假设 → lean-canvas
  - new_product_line + 需完整战略 → startup-canvas
```

---

## B. 产品发现 existing/new 对称对 — 合并 + 场景分支

**涉及 Skill：**
| # | 名称 | 配对 | 所属层 |
|---|------|------|--------|
| 45/46 | brainstorm-ideas-existing / brainstorm-ideas-new | 产品创意脑暴 | S |
| 43/44 | brainstorm-experiments-existing / brainstorm-experiments-new | 实验设计 | E |
| 47/48 | identify-assumptions-existing / identify-assumptions-new | 假设识别 | D |

**深度分析发现 — 处理结构相同，但处理元素按场景切换：**

三对 Skill 的步骤框架完全一致（收集输入 → 结构化分析 → 输出结果），但每个步骤内部使用的"弹药"不同：

### B-1. brainstorm-ideas（合并 #45 + #46）

| 处理元素 | existing_product 分支 | new_product 分支 |
|---------|----------------------|-----------------|
| 创意来源 | 用户反馈、数据分析、竞品缺口 | 趋势洞察、JTBD 未满足需求、类比迁移 |
| 评估维度 | 战略对齐度、ROI、技术可行性 | 核心价值交付、验证速度、资源需求 |
| 风险类别 | 4 类（市场/技术/运营/财务） | 8 类（+团队/时机/监管/平台依赖） |
| 输出结构 | 创意卡 + 对齐度评分 + 路线图建议 | 创意卡 + 假设标注 + 验证优先级 |

```yaml
name: brainstorm-ideas
context_param: product_stage
branches:
  existing_product:
    trigger: "已有产品/功能线，有活跃用户和历史数据"
    idea_sources: ["用户反馈", "数据分析", "竞品缺口分析", "内部利益相关者"]
    risk_categories: 4
    evaluation_focus: "strategic_alignment + ROI"
    output_extras: ["路线图对齐建议"]
  new_product:
    trigger: "新产品/新业务线，无活跃用户或处于 0→1 阶段"
    idea_sources: ["趋势洞察", "JTBD未满足需求", "类比迁移", "跨行业借鉴"]
    risk_categories: 8
    evaluation_focus: "core_value_delivery + validation_speed"
    output_extras: ["验证优先级矩阵"]
```

### B-2. brainstorm-experiments（合并 #43 + #44）

| 处理元素 | existing_product 分支 | new_product 分支 |
|---------|----------------------|-----------------|
| 实验方法集 | A/B 测试、多变量测试、灰度发布、漏斗分析 | Pretotyping、Smoke Test、Wizard of Oz、Concierge MVP |
| 数据要求 | 需要统计显著性的样本量 | 定性信号即可，小样本 |
| 成功标准 | p-value < 0.05 + 效果量 | "有人愿意付钱/预注册/留邮箱" |
| 实验周期 | 1-4 周（依赖流量） | 1-5 天（快速验证） |

```yaml
name: brainstorm-experiments
context_param: product_stage
branches:
  existing_product:
    trigger: "有活跃用户流量，可以做统计分析"
    methods: ["A/B测试", "多变量测试", "灰度发布", "漏斗分析"]
    data_requirement: "统计显著性样本量"
    success_criteria: "p-value < 0.05 + 效果量"
    typical_duration: "1-4 周"
  new_product:
    trigger: "无用户流量，需要快速定性验证"
    methods: ["Pretotyping", "Smoke Test", "Wizard of Oz", "Concierge MVP"]
    data_requirement: "定性信号，小样本"
    success_criteria: "行为承诺（付费/预注册/留邮箱）"
    typical_duration: "1-5 天"
```

### B-3. identify-assumptions（合并 #47 + #48）

| 处理元素 | existing_product 分支 | new_product 分支 |
|---------|----------------------|-----------------|
| 假设类型 | 增长假设、留存假设、变现假设 | 价值假设、需求假设、解决方案假设 |
| 分类框架 | 按业务漏斗阶段分类 | 按风险类型 × 影响程度分类 |
| 优先级排序 | 影响力 × 可测量性 | 风险程度 × 验证成本 |
| 输出深度 | 假设 + 测量方案 + 数据源 | 假设 + 最小验证方案 + 成功标准 |

```yaml
name: identify-assumptions
context_param: product_stage
branches:
  existing_product:
    trigger: "已有产品，需识别增长/留存/变现假设"
    assumption_types: ["增长假设", "留存假设", "变现假设"]
    classification: "按业务漏斗阶段"
    priority_axis: "impact × measurability"
  new_product:
    trigger: "新产品，需识别价值/需求/方案假设"
    assumption_types: ["价值假设", "需求假设", "解决方案假设"]
    classification: "按风险类型 × 影响程度"
    priority_axis: "risk_level × validation_cost"
```

**合并后 IO 契约（三个 Skill 统一模式）：**
- 输入：产品描述 + 目标用户 + 当前指标 + `product_stage: existing | new`
- 输出：结构化结果 + 分支特有的附加输出
- 分支选择：由 Dispatcher 根据用户描述中的信号词自动判断（"我们现有产品…" → existing；"我在做一个新产品…" → new）

---

## C. Backlog 条目格式 — 合并 + 格式分支

**涉及 Skill：**
| # | 名称 | 格式 | 所属层 |
|---|------|------|--------|
| 22 | user-stories | 3C+INVEST 用户故事 | V |
| 12 | job-stories | JTBD 工作故事 | V |
| 23 | wwas | Why-What-Acceptance | V |

**深度分析发现 — 高度可合并，差异仅在模板层面：**

三者输入相同（需求描述 + 用户上下文 + 产品背景），输出相同（结构化 Backlog 条目清单），差异仅在：

| 差异点 | User Story (#22) | Job Story (#12) | WWA (#23) |
|--------|-----------------|-----------------|-----------|
| 模板句式 | As a [角色], I want [功能], so that [价值] | When [情境], I want to [行为], so I can [结果] | Why: [战略原因] / What: [交付物] / Acceptance: [标准] |
| 验收标准数 | 4-6 条 | 6-8 条（含场景变体） | 3-4 条 |
| 战略关联 | 无显式字段 | 无显式字段 | Why 字段直接关联战略目标 |
| 最佳受众 | 开发团队 / Scrum | UX 团队 / 服务设计 | 管理层 / 跨部门对齐 |

```yaml
name: backlog-item-generator
context_param: audience
branches:
  user_story:
    trigger: "面向开发团队/Scrum，需要拆分到可执行粒度"
    template: "As a [role], I want [feature], so that [benefit]"
    acceptance_criteria_count: "4-6"
    strategic_link: false
  job_story:
    trigger: "面向UX/服务设计，关注用户情境和行为"
    template: "When [situation], I want to [action], so I can [outcome]"
    acceptance_criteria_count: "6-8"
    strategic_link: false
  wwa:
    trigger: "面向管理层/业务对齐，需要体现战略意图"
    template: "Why: [reason] / What: [deliverable] / Acceptance: [criteria]"
    acceptance_criteria_count: "3-4"
    strategic_link: true
```

**合并后 IO 契约：**
- 输入：需求描述 + 用户上下文 + 产品背景 + 目标受众（dev/ux/mgmt）
- 输出：结构化 Backlog 条目清单 + 验收标准 + 优先级标注
- 分支选择：Dispatcher 追问"这些条目主要给谁看？"

---

## D. 系统控制器 — 合并 + 平台自动检测分支

**涉及 Skill：**
| # | 名称 | 描述 | 所属层 | 成熟度 |
|---|------|------|--------|--------|
| 94 | system-controller | Windows 桌面控制 | I | 稳定 |
| 92 | linux-system-controller | Linux 桌面控制 | I | 试验 |
| 93 | minimal-agent | 极简 OS 控制代理 | I | 试验 |
| 95 | universal-agent | 自然语言→代码→执行 | I | 试验 |
| 114 | omniscient | 认知+执行+Windows 三层全能 | V | 核心 |
| 113 | linux-omniscient | 认知+执行+Linux 三层全能 | V | 试验 |

**合并策略：**

```yaml
# 合并 Skill 1: 基础系统控制
name: system-controller
sources: ["#94 system-controller", "#92 linux-system-controller", "#93 minimal-agent"]
context_param: platform  # 自动检测，无需用户指定
branches:
  windows:
    trigger: "运行时 OS 检测为 Windows"
    capabilities: ["进程管理", "文件系统", "注册表", "服务控制", "PowerShell"]
    shell: "PowerShell / CMD"
  linux:
    trigger: "运行时 OS 检测为 Linux"
    capabilities: ["进程管理", "文件系统", "systemd", "包管理", "Bash"]
    shell: "Bash"

# 合并 Skill 2: 三层全能系统
name: omniscient
sources: ["#95 universal-agent", "#114 omniscient", "#113 linux-omniscient"]
context_param: platform  # 自动检测
architecture: "认知层 → 编排层 → 执行层"
branches:
  windows:
    trigger: "运行时 OS 检测为 Windows"
    execution_layer: "Windows API + PowerShell + 桌面自动化"
  linux:
    trigger: "运行时 OS 检测为 Linux"
    execution_layer: "Bash + D-Bus + X11/Wayland 自动化"
```

---

## E. Agent 编排元框架 — 合并为 2 个

**涉及 Skill：**
| # | 名称 | 描述 | 所属层 | 成熟度 |
|---|------|------|--------|--------|
| 103 | identity-primitive-chain-prompt | 身份基元链提示词 | I | 核心 |
| 104 | ipo-model | 输入处理输出递归嵌套模型 | I | 核心 |
| 105 | universal-primitives | LLM 两个基元方法论 | I | 稳定 |
| 108 | capability-pipeline-os | 能力管线操作系统 | I | 稳定 |
| 109 | cogniexec | 认知+执行+编排引擎 | I | 核心 |
| 117 | universal-task-os | 三轴任务操作系统 | I | 核心 |
| 106 | adaptive-skill-stack | 自动叠加能力元技能 | I | 试验 |

**合并策略：**

- **`agent-architecture`**（合并 #103 + #104 + #105 + #108）：统一"Agent 架构原理与方法论"——涵盖基元链、IPO 模型、管线编排等理论，按需调用。内部以"理论模块"组织，不做分支，而是根据用户问题引用对应模块。
- **`agent-runtime`**（合并 #106 + #109 + #117）：统一"Agent 运行时引擎"——涵盖认知执行、能力叠加、三轴协同等运行时能力。

```yaml
# agent-architecture 内部模块索引
modules:
  identity_chain:    "当需要定义 Agent 身份→能力→约束链时引用"
  ipo_recursive:     "当需要设计输入→处理→输出递归嵌套结构时引用"
  dual_primitives:   "当需要理解 LLM 的'理解+生成'两个基元时引用"
  capability_pipeline: "当需要设计能力管线和数据流时引用"

# agent-runtime 内部分支
name: agent-runtime
branches:
  cogniexec:
    trigger: "需要认知建模 + 执行编排的完整引擎"
    focus: "思考→计划→执行→反思闭环"
  adaptive_stack:
    trigger: "需要自动组合多个 Skill 完成复杂任务"
    focus: "能力发现→动态叠加→协同执行"
  task_os:
    trigger: "需要多任务调度和资源管理"
    focus: "任务分解→优先级→资源分配→进度跟踪"
```

---

## F. 优先级排序 — 部分合并

**涉及 Skill：**
| # | 名称 | 描述 | 所属层 |
|---|------|------|--------|
| 15 | prioritization-frameworks | 9 种优先级框架参考指南 | S |
| 53 | prioritize-features | 按影响力/工作量/风险排序功能 | S |
| 52 | prioritize-assumptions | 影响×风险矩阵排序假设 | E |
| 42 | analyze-feature-requests | 分类评估功能需求 | D |

**合并策略：**

- **`prioritize-workitems`**（合并 #15 + #53）：统一"工作项优先级排序"

```yaml
name: prioritize-workitems
sources: ["#15 prioritization-frameworks", "#53 prioritize-features"]
context_param: item_type
branches:
  framework_reference:
    trigger: "用户需要了解/选择合适的排序框架"
    output: "框架对比表 + 适用场景分析 + 推荐框架"
    frameworks: ["RICE", "ICE", "MoSCoW", "Kano", "WSJF", "Value/Effort", "Impact/Urgency", "Opportunity Scoring", "Cost of Delay"]
  actual_ranking:
    trigger: "用户已有待排序列表，需要实际执行排序"
    output: "评分表 + 排序结果 + 象限可视化 + 取舍建议"
    default_framework: "RICE"
    customizable: true
```

- **保持独立**：#52（假设排序，E 层验证专用）和 #42（需求分析，D 层诊断专用）各自保留——层级和排序对象都不同

---

## G. GTM 上市策略 — 合并 + 深度分支

**涉及 Skill：**
| # | 名称 | 描述 | 所属层 |
|---|------|------|--------|
| 27 | gtm-motions | 评估 7 种 GTM 动作 | S |
| 28 | gtm-strategy | 综合 GTM 战略 | S |
| 26 | growth-loops | 增长飞轮 | S |
| 24 | beachhead-segment | 滩头市场 | D |

**深度分析发现 — motions 和 strategy 的差异比表面看到的更深：**

| 维度 | gtm-motions (#27) | gtm-strategy (#28) |
|------|-------------------|-------------------|
| 处理范围 | 单一决策：选择哪种 GTM 动作 | 综合规划：制定完整 GTM 战略 |
| 动作库 | 7 种（PLG, SLG, MLG, CLG, ELG, DLG, Partner） | 含 motions + 定价 + 渠道 + 时机 |
| 输出粒度 | 1-2 个推荐动作 + 适配性评估 | 完整 GTM 计划（6-12 个月） |
| 输入深度 | 产品特征 + 目标市场 | 产品+市场+竞品+资源+时间线 |

```yaml
name: gtm-planner
context_param: scope
branches:
  motion_selection:
    trigger: "用户需要选择合适的 GTM 动作（单一决策）"
    input: "产品特征 + 目标市场类型"
    processing: "7 种 GTM 动作适配性评估"
    output: "推荐动作（1-2 个）+ 适配性评分 + 实施要点"
    duration: "快速输出"
  full_strategy:
    trigger: "用户需要制定完整 GTM 战略（综合规划）"
    input: "产品+市场+竞品+资源+时间线"
    processing: "动作选择 + 定价策略 + 渠道规划 + 里程碑 + 风险预案"
    output: "完整 GTM 计划文档（6-12 个月路线图）"
    duration: "深度分析"
```

- **保持独立**：#26（增长飞轮，独特的系统动力学方法论）和 #24（滩头市场，D 层诊断专用）

---

## H. 招投标 — 合并

**涉及 Skill：**
| # | 名称 | 描述 | 所属层 |
|---|------|------|--------|
| 88 | bidding-assistant | 招投标全流程助手 | V |
| 89 | bid-assistant | 招投标 11 大场景 | V |
| 90 | tender-knowledge-framework | 标书知识框架 | I |

**合并策略：**

```yaml
name: bidding-assistant
sources: ["#88 bidding-assistant", "#89 bid-assistant"]
context_param: task_phase
branches:
  analysis:
    trigger: "需要解析招标文件、评估机会"
    processing: "文档解析 → 要求提取 → 机会评分 → 风险分析"
    output: "招标摘要 + 机会评估 + Go/No-Go 建议"
  production:
    trigger: "需要生成投标文件、编写章节"
    processing: "大纲规划 → 素材匹配 → 章节撰写 → 合规检查"
    output: "投标方案 + .docx 文件 + 合规清单"
  full_pipeline:
    trigger: "需要从分析到产出的全流程"
    processing: "analysis 分支 → production 分支，串联执行"
    output: "全流程交付物"
```

- **保持独立**：#90（知识框架，I 层基础设施，为 bidding-assistant 提供知识弹药）

---

## I. 用户研究 — 修订：仅合并画像/分群，访谈工具保持独立

**涉及 Skill：**
| # | 名称 | 描述 | 所属层 |
|---|------|------|--------|
| 35 | user-personas | 生成用户画像 | D |
| 36 | user-segmentation | 识别用户分群 | D |
| 49 | interview-script | 客户访谈脚本 | D |
| 54 | summarize-interview | 访谈总结 | D |
| 31 | customer-journey-map | 客户旅程地图 | D |
| 29 | ideal-customer-profile | 理想客户画像 ICP | D |

**深度分析发现 — 访谈工具不是变体，是工作流中的独立环节：**

| Skill 对 | 分析结论 |
|---------|---------|
| #35 personas + #36 segmentation | **可以合并**。两者输入相同（用户数据/市场数据），处理相同（分析+分类），差异仅在分析视角：personas 侧重"典型个体"深度刻画，segmentation 侧重"群体"统计特征。合并后用 `perspective` 分支切换。 |
| #49 interview-script + #54 summarize-interview | **不应合并**。这两个不是同一能力的变体，而是用户研究工作流中的两个独立环节：一个生成脚本（输入=研究目标，输出=访谈提纲），另一个分析结果（输入=访谈记录，输出=洞察报告）。它们的输入输出完全不同，合并后必须用"是否已有访谈记录"做硬分支——这不是合并，是伪装成合并的工作流串联。 |

**策略：**

```yaml
# 合并 Skill: 用户画像与分群
name: user-profiling
sources: ["#35 user-personas", "#36 user-segmentation"]
context_param: perspective
branches:
  persona:
    trigger: "需要深度刻画典型用户个体（用于共情和设计决策）"
    output: "2-4 个详细人物画像（含目标/痛点/行为模式/引用语）"
    methodology: "定性聚类 + 人物叙事"
  segmentation:
    trigger: "需要识别用户群体统计特征（用于市场策略和优先级）"
    output: "分群矩阵（含维度/规模/价值/行为特征）"
    methodology: "变量选择 + 聚类分析 + 价值评估"

# 保持独立的访谈工具（不合并）
# #49 interview-script — 输入：研究目标 → 输出：访谈提纲
# #54 summarize-interview — 输入：访谈记录 → 输出：洞察报告
# 两者通过工作流串联（先脚本后总结），不是同一能力的分支
```

- **保持独立**：#49 interview-script、#54 summarize-interview（工作流独立环节）、#31 customer-journey-map（方法论独特）、#29 ideal-customer-profile（偏 GTM 场景）

---

## J. 价值主张/定位 — 修订：保持独立 + 管线串联

**涉及 Skill：**
| # | 名称 | 描述 | 所属层 |
|---|------|------|--------|
| 66 | value-proposition | 6 步 JTBD 价值主张设计 | S |
| 39 | positioning-ideas | 差异化定位方案 | S |
| 41 | value-prop-statements | 价值主张文案 | V |
| 63 | product-vision | 产品愿景 | S |
| 13 | outcome-roadmap | 结果导向路线图 | S |

**深度分析发现 — 这不是"同一能力的变体"，而是管线中的三个阶段：**

```
[产品愿景 #63]
      ↓ 输入
[价值主张设计 #66]  →  输出：价值主张画布（JTBD + 痛点 + 收益）
      ↓ 输入
[定位差异化 #39]    →  输出：定位方案（差异化角度 + 竞争壁垒）
      ↓ 输入
[价值主张文案 #41]  →  输出：对外传播文案（标题 + Tagline + Elevator Pitch）
      ↓ 输入
[结果路线图 #13]    →  输出：落地路线图
```

| Skill | 处理核心 | 输入 | 输出 | 为什么不能合并 |
|-------|---------|------|------|--------------|
| #66 value-proposition | 设计：识别用户 JTBD + 痛点 + 收益 → 映射到产品能力 | 用户研究 + 产品功能 | 价值主张画布 | 这是"设计"活动 |
| #39 positioning-ideas | 差异化：在竞品中找到独特定位 | 价值主张 + 竞品分析 | 定位方案 + 差异化策略 | 这是"竞争分析"活动 |
| #41 value-prop-statements | 文案：把定位写成可传播的表达 | 定位方案 | 标题/Tagline/Elevator Pitch | 这是"写作"活动 |

三者的处理逻辑完全不同（设计 vs 分析 vs 写作），输入输出是串行依赖关系。合并后 Skill 内部实际上是在顺序执行三个不同的任务——这不是合并，而是把工作流塞进了一个 Skill。

**策略：保持独立，在 Dispatcher 中定义管线调用链**

```yaml
pipeline: value_proposition_chain
description: "从价值主张设计到传播文案的完整管线"
stages:
  - step: 1
    skill: product-vision (#63)
    optional: true
    output: "产品愿景声明"
  - step: 2
    skill: value-proposition (#66)
    input_from: [step_1_output, "用户研究数据"]
    output: "价值主张画布"
  - step: 3
    skill: positioning-ideas (#39)
    input_from: [step_2_output, "竞品分析"]
    output: "定位方案"
  - step: 4
    skill: value-prop-statements (#41)
    input_from: [step_3_output]
    output: "传播文案集"

dispatch_rule: |
  用户说"帮我做价值主张" → 从 step 2 开始
  用户说"帮我做产品定位" → 从 step 3 开始
  用户说"帮我写产品文案" → 直接 step 4（追问是否有定位方案）
  用户说"从愿景到文案全做" → step 1-4 完整管线
```

---

## K. 法律合规 — 合并为 2 个

**涉及 Skill：**
| # | 名称 | 描述 | 所属层 |
|---|------|------|--------|
| 86 | legal-compliance-bundle | 50 个合规自动化技能 | V |
| 91 | law-skills | 中国法律咨询参考 | V |
| 67 | draft-nda | NDA 保密协议 | V |
| 69 | privacy-policy | 隐私政策 | V |

**合并策略：**

```yaml
# 合并 Skill 1: 法律咨询与合规审计
name: legal-advisor
sources: ["#86 legal-compliance-bundle", "#91 law-skills"]
context_param: task_type
branches:
  consultation:
    trigger: "用户有具体法律问题需要咨询"
    processing: "问题分类 → 法条匹配 → 风险评估 → 建议"
    output: "法律咨询回复 + 法条引用 + 风险提示"
  compliance_audit:
    trigger: "用户需要合规审查或自动化合规流程"
    processing: "合规域识别 → 检查清单 → 差距分析 → 整改建议"
    output: "合规审计报告 + 整改清单 + 优先级"

# 合并 Skill 2: 法律文档生成
name: legal-doc-generator
sources: ["#67 draft-nda", "#69 privacy-policy"]
context_param: doc_type
branches:
  nda:
    trigger: "需要生成保密协议"
    output: "NDA 文档（含双方信息、保密范围、期限、违约条款）"
  privacy_policy:
    trigger: "需要生成隐私政策"
    output: "隐私政策文档（含数据类型、用途、存储、用户权利）"
  other_legal_doc:
    trigger: "需要其他法律文书（合同/协议/声明）"
    output: "法律文书模板 + 填写指引"
```

---

## L. 竞品分析 — 保持独立

**涉及 Skill：** #30 competitor-analysis / #25 competitive-battlecard / #65 swot-analysis

**不合并理由：** 三者服务不同角色（产品经理 vs 销售 vs 管理层），输出结构不同（研究报告 vs 战术卡 vs 战略矩阵），合并后无法对齐不同角色的需求。

**Dispatcher 路由规则：**
- "帮我研究一下竞品" → #30 competitor-analysis
- "做个销售竞争战术卡" → #25 competitive-battlecard
- "做个 SWOT 分析" → #65 swot-analysis
- 模糊请求 → 追问"你是要深度研究报告、销售战术卡、还是战略评估矩阵？"

---

## M. 战略分析框架 — 保持独立

**涉及 Skill：** #65 SWOT / #59 PESTLE / #60 波特五力 / #55 安索夫矩阵 / #62 产品战略画布

**不合并理由：** 每个框架回答不同的战略问题，有独立的方法论。它们是互补关系而非重叠关系。

**Dispatcher 路由规则：** 建立"战略分析工作流"——根据用户问题性质推荐框架或组合调用。

---

## N. 知识参考库 — 保持独立

**涉及 Skill：** #132 医药 / #133 单文件 / #134 硬件 / #136 网文 / #102 综合 / #135 全域

**不合并理由：** 领域知识不可替代。通过统一的 IO 契约规范调用接口即可。

---

## 附：服务设计专家团 vs PM Skills 的跨源层级关系

**核心问题：** 服务设计专家团的 10 个子 Skill 与 pm-skills-main 的 50+ 个 Skill 在多个领域高度重叠。

| 专家团成员 | 与之重叠的 PM Skills |
|-----------|---------------------|
| fwsjtt-strategy-growth-advisor | product-strategy, swot-analysis, business-model, growth-loops |
| fwsjtt-customer-discovery | user-personas, interview-script, customer-journey-map |
| fwsjtt-service-designer | customer-journey-map, opportunity-solution-tree |
| fwsjtt-metrics-architect | north-star-metric, metrics-dashboard |
| fwsjtt-roi-strategist | product-solution-evaluator, monetization-strategy |
| fwsjtt-evidence-auditor | ab-test-analysis, sentiment-analysis |
| fwsjtt-delivery-qa-reviewer | grammar-check, create-prd (QA 维度) |

**整合策略 — 建立层级关系（非合并）：**

```yaml
relationship: hierarchical
description: "专家团 = 深度模式；PM Skills = 快速模式"

dispatch_rule:
  complexity_assessment:
    quick_mode:
      trigger: "单一问题、明确需求、标准化输出"
      route_to: "对应 PM Skill"
      example: "帮我写个 PRD" → create-prd
    deep_mode:
      trigger: "多约束、模糊需求、需要交叉验证、高风险决策"
      route_to: "服务设计专家团"
      example: "我们在考虑转型，需要从用户、商业、技术多维度评估" → expert-team
```

---

## 合并后目标架构（v3 — 六阶段分布）

合并后 118 个 Skill 的六阶段分布（原 139 个，合并减少 21 个）：

| 阶段 | 合并前 | 合并后 | 变化 | 标准出处 |
|------|:---:|:---:|:---:|---------|
| P1 识别 | 25 | 23 | -2 | PMP.Initiating / NPDP.Discovery |
| P2 论证 | 31 | 27 | -4 | PMP.Planning 前端 / NPDP.Business Analysis |
| P3 规划 | 3 | 3 | 0 | PMP.Planning 过程组 |
| P4 执行 | 36 | 33 | -3 | PMP.Executing / 一建.施工管理 |
| P5 控制 | 13 | 11 | -2 | PMP.M&C / NPDP.Metrics |
| P6 收尾 | 4 | 4 | 0 | PMP.Closing / NPDP.Life Cycle |
| CX 专业知识域 | 28 | 17 | -11 | 一建.法规.经济 / NPDP.Strategy / Agent 工具 |
| **合计** | **139** | **118** | **-21** | |

> **注：** P3 规划阶段目前仅 3 个独立 Skill，这是因为多数"规划类"Skill（如 PRD、Backlog、OKR 等）在映射时根据其处理性质被归入 P2（方案论证/决策）或 P4（文档交付）。后续可依据实际使用场景重新校准 P2/P3 边界。

**合并优先级对照（对齐 STANDARDS_FRAMEWORK.md 的落地优先级）：**

| 优先级 | 群组 | 减少 | 分支复杂度 | 对应阶段 | 标准依据 |
|:---:|------|:---:|:---:|---------|---------|
| P0 | D. 系统控制器 | -4 | 低 | CX-8 | 影响面小，平台自动检测 |
| P0 | E. Agent 元框架 | -5 | 低 | CX-8 | 高度理论化，合并风险低 |
| P1 | B. 产品发现对称对 | -3 | 中 | P1/P2 | NPDP 核心场景 |
| P1 | C. Backlog 条目 | -2 | 低 | P3/P4 | PMP.Scope 规划 |
| P1 | H. 招投标 | -1 | 低 | P3/P4 | PMP.Procurement / 一建.招投标 |
| P2 | F. 优先级排序 | -2 | 低 | P3 | PMP.Planning.Scope |
| P2 | G. GTM 策略 | -1 | 中 | P2/P3 | NPDP.Strategy |
| P2 | I. 用户研究 | -1 | 低 | P1 | NPDP.Market Research |
| P2 | K. 法律合规 | -2 | 低 | CX-1 | 一建.法规 |
| — | A. 画布变体 | 0 | — | P2 | 不合并，统一 IO 接口 |
| — | J. 价值主张链 | 0 | — | P2→P4 | 不合并，管线串联 |
| — | L/M/N. 独立群组 | 0 | — | 混合 | 保持独立 |

---

## 分支条件汇总速查表

| 合并后 Skill 名 | context 参数 | 分支选项 | 分支触发信号 |
|----------------|-------------|---------|-------------|
| brainstorm-ideas | product_stage | existing \| new | "现有产品/新功能" vs "新产品/0→1" |
| brainstorm-experiments | product_stage | existing \| new | 同上 |
| identify-assumptions | product_stage | existing \| new | 同上 |
| backlog-item-generator | audience | user_story \| job_story \| wwa | "给开发团队" vs "给UX" vs "给管理层" |
| system-controller | platform | windows \| linux | 运行时 OS 自动检测 |
| omniscient | platform | windows \| linux | 运行时 OS 自动检测 |
| gtm-planner | scope | motion_selection \| full_strategy | "选哪种GTM动作" vs "制定完整GTM战略" |
| bidding-assistant | task_phase | analysis \| production \| full | "分析招标文件" vs "生成投标文件" vs "全流程" |
| user-profiling | perspective | persona \| segmentation | "用户画像/典型用户" vs "用户分群/市场细分" |
| prioritize-workitems | item_type | framework_ref \| actual_ranking | "用什么框架" vs "帮我排序这个列表" |
| legal-advisor | task_type | consultation \| compliance_audit | "法律问题" vs "合规审查" |
| legal-doc-generator | doc_type | nda \| privacy \| other | "保密协议" vs "隐私政策" vs "其他法律文书" |

---

> **下一步行动：**
> 1. 确认本合并策略后，按 P0 → P1 → P2 优先级逐个执行合并
> 2. 为合并后的 Skill 编写完整的 SKILL.md（含标准 ITTO 卡片 + 分支逻辑）
> 3. 为 A/J 群组的独立 Skill 补写统一 IO 接口规范
> 4. 建立 Dispatcher 总控路由表（按 STANDARDS_FRAMEWORK.md 的六阶段调度逻辑）
