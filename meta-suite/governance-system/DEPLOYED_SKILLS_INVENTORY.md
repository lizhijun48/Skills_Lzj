# Skill 体系全景编目与调度指南

> ⚠️ **引导索引 · 非实时快照**
> 本文件生成于 **2026-06-29**，后续新增/变更（如 JT-019 pm-tender-analysis、P0 编号冲突修复等）可能未同步至此索引。
> **实时权威注册表请以 `SKILL-ID-REGISTRY.md` 为准**（当前 v1.1.4），路由编排请以 `BUSINESS-FLOW-MAP.md`、`pd-workflow-chains`(PT-016)、`pm-workflow-chains`(JT-018) 为准。

> **定位**：引导层主文件 — "用什么技能" + "怎么串联"
> **已部署 Skill 总数**：129（2026-07-07 P2 inbox 搬迁后，含新增 industry/research/expert 等 suite）
> **更新日期**：2026-07-07 (P0/P1 治理审计整改后)

---

## 一、场景速查

> **使用方法**：找到你当前的工作场景 → 按箭头指引找到推荐 Skill → 跳转到对应章节查看详情。

### 1.1 产品决策场景 → 技能推荐

```
我在做什么？
│
├─ 定方向/做战略 ──────────────→ pd-product-strategy (PT-001)
│   └─ 需要市场调研数据 ────────→ pd-market-research (PT-003)
│   └─ 需要理解用户需求 ────────→ pd-user-research (PT-012)
│
├─ 评估这个机会值不值得做 ──────→ pd-go-nogo (PT-004)
│   ├─ 需要算 NPV/回收期 ──────→ + economic-npv (E-001) / economic-payback (E-006)
│   └─ 需要结构化决策 ──────────→ + meta-decision-frameworks (S-001)
│
├─ 评估具体产品方案/MVP/商业化 ──→ product-solution-evaluator (PT-018)
│
├─ 做需求分析/产品设计 ────────→ pd-requirements-design (PT-006)
│   └─ 工业互联网领域 ──────────→ 工业互联网产品经理 (PT-017)
│
├─ 选开发方法(敏捷/瀑布/…) ───→ meta-development-methodology (S-002)
│   └─ 走 Stage-Gate/精益/设计思维 → pd-innovation-process (PT-002)
│       └─ 涉及 IP 保护 ────────→ + ip-protection (L-003)
│
├─ 写 PRD ─────────────────────→ pd-prd-writing (PT-007)
│
├─ 产品上市/定价/GTM ──────────→ pd-product-launch (PT-008)
│   ├─ 需要经济测算 ────────────→ + economic-suite 全套
│   └─ 涉及 IP 保护 ────────────→ + ip-protection (L-003)
│
├─ 产品运营/增长/数据实验 ─────→ pd-product-operations (PT-011)
│
├─ 管理产品生命周期/退市 ──────→ pd-lifecycle-management (PT-009)
│
├─ 管理产品组合/资源分配 ──────→ pd-portfolio-management (PT-005)
│   └─ 需要经济比选 ────────────→ + economic-npv/irr/payback/comparison
│
├─ 设定 OKR/度量指标 ──────────→ pd-tools-metrics (PT-013)
│   └─ 需要经济 ROI 计算 ──────→ + economic-suite 全套
│
├─ 建设产品团队 ───────────────→ pd-team-culture (PT-014)
│   └─ 需要干系人分析 ──────────→ + meta-stakeholder-analysis (S-005)
│
├─ 跨阶段协调/PD-PM 桥接 ─────→ pd-integration (PT-015)
│   └─ 需要职业道德指引 ───────→ + meta-professional-ethics (S-003)
│
└─ 不知道从哪开始/想看全流程 ──→ pd-workflow-chains (PT-016)
    └─ 需要专家视角 ────────────→ high-vision-perspective (S-006)
                                  zhou-hongyi-perspective-v2 (S-007)
```

### 1.2 项目交付场景 → 技能推荐

```
我在做什么？
│
├─ 拿到招标文件要分析 ──────────→ pm-tender-analysis
│
├─ 准备投标/写技术方案 ────────→ pm-bid-proposal (JT-002)
│   └─ 按大纲/模板写技术文档 ───→ + tech-doc-writer (S-021)
│
├─ 项目立项/可行性研究 ────────→ pm-project-opportunity (JT-001)
│
├─ 定义范围/做 WBS ────────────→ pm-requirements-scope (JT-003)
│
├─ 排进度/控成本 ──────────────→ pm-schedule-cost (JT-004)
│   ├─ 需要方案比选 ────────────→ + economic-comparison (E-004)
│   └─ 需要决策框架 ────────────→ + meta-decision-frameworks (S-001)
│
├─ 识别/应对风险 ──────────────→ pm-risk-management (JT-010)
│   ├─ 需要定量分析(EMV) ─────→ + economic-sensitivity (E-003)
│   ├─ 需要蒙特卡洛模拟 ───────→ + tools-monte-carlo (S-009)
│   └─ 涉及 IP 风险 ───────────→ + ip-protection (L-003)
│
├─ 采购/外购/合同/质量规划 ───→ pm-procurement-quality (JT-008)
│   ├─ 需要审查合同 ────────────→ + contract-review (L-002)
│   └─ 需要方案比选 ───────────→ + economic-comparison (E-004)
│
├─ 项目交付/执行管理 ──────────→ pm-project-delivery (JT-009)
│   └─ 需要选择开发方法 ───────→ + meta-development-methodology (S-002)
│
├─ 质量保证/审计/六西格玛 ────→ pm-quality-assurance (JT-012)
│
├─ 处理变更请求 ───────────────→ pm-change-management (JT-006)
│
├─ 跟踪绩效/挣值分析 ────────→ pm-performance-tracking (JT-011)
│
├─ 政府项目验收 ───────────────→ pm-gov-acceptance (JT-016)
│
├─ 项目收尾/知识沉淀 ──────────→ pm-project-closure (JT-017)
│
├─ 团队管理/沟通协调 ──────────→ pm-team-communication (JT-014)
│
├─ 干系人管理 ─────────────────→ pm-stakeholder-management (JT-015)
│   └─ 需要干系人分析方法 ─────→ + meta-stakeholder-analysis (S-005)
│
├─ 项目整合管理/全局协调 ─────→ pm-integration (JT-005)
│   └─ 需要职业道德指引 ───────→ + meta-professional-ethics (S-003)
│
└─ 不知道从哪开始/想看全流程 ──→ pm-workflow-chains (JT-018)
```

### 1.3 通用工具场景 → 技能推荐

```
我在做什么？
│
├─ 需要做决策(加权评分/决策树) → meta-decision-frameworks (S-001)
├─ 需要选开发方法论 ───────────→ meta-development-methodology (S-002)
├─ 需要职业道德/伦理指引 ─────→ meta-professional-ethics (S-003)
├─ 需要风险管理基础方法 ───────→ meta-risk-basics (S-004)
├─ 需要干系人分析工具 ─────────→ meta-stakeholder-analysis (S-005)
│
├─ 需要高格局/战略视角 ───────→ high-vision-perspective (S-006)
├─ 需要颠覆式创新视角 ─────────→ zhou-hongyi-perspective-v2 (S-007)
│
├─ 需要贝叶斯概率更新 ─────────→ tools-bayesian-update (S-008)
├─ 需要蒙特卡洛模拟 ───────────→ tools-monte-carlo (S-009)
│
├─ 需要记录会议纪要 ───────────→ meeting-minutes (S-010)
├─ 需要文档版本化/批量生成 ───→ doc-versioner (S-011)
├─ 需要 Markdown→PDF ─────────→ md-to-pdf-cjk (S-015)
├─ 需要文档→Markdown 转换 ───→ markitdown-skill (S-016)
├─ 需要处理 Excel 工作簿 ─────→ excel-xlsx (S-020)
├─ 需要写技术文档/应标方案 ───→ tech-doc-writer (S-021)
│
├─ 需要创建新技能包 ───────────→ skill-creator-optimized (S-022)
│   └─ 面试式创建+安全审计 ───→ skill-forge (S-024)
├─ 需要改造/重构现有技能 ─────→ skill-refactor (S-023)
│
├─ 需要经济计算 ───────────────→ economic-suite (见第五章)
│   ├─ NPV/IRR/回收期 ────────→ E-001 / E-002 / E-006
│   ├─ 敏感性分析 ─────────────→ economic-sensitivity (E-003)
│   ├─ 方案比选 ───────────────→ economic-comparison (E-004)
│   ├─ 价值工程 ───────────────→ economic-ve (E-005)
│   └─ 不确定用哪个 ──────────→ economic-decision (E-007) 元技能自动调度
│
├─ 需要法律支持 ───────────────→ legal-suite (见第六章)
│   ├─ 法律咨询/起诉状 ────────→ law-skills (L-001)
│   ├─ 合同审查 ───────────────→ contract-review (L-002)
│   ├─ IP 保护 ────────────────→ ip-protection (L-003)
│   └─ 合规自动化(50子技能) ──→ legal-compliance-bundle (L-004)
│
└─ 需要深度阅读/拆书 ─────────→ reading-os (见第七章)
    ├─ 拆一本书 → 资产化输出 ─→ reading-book-deconstruction (R-001)
    ├─ 体检书架 ───────────────→ reading-bookshelf-health (R-002)
    └─ 选阅读路径 ─────────────→ reading-role-path (R-003)
```

### 1.4 个人发展场景 → 技能推荐

```
我在做什么？
│
├─ 创建/优化/定制简历 ─────────→ resume-optimizer (S-018)
│   └─ 需要导出 PDF ───────────→ + md-to-pdf-cjk (S-015)
│
├─ 分析保险保单 ───────────────→ insurance-policy-analysis (S-012)
│
├─ 财税/会计/审计问题 ─────────→ gridman (S-019)
│
├─ 解析微信公众号文章 ─────────→ wechat-article-parser (S-014)
│
└─ 美团优惠券/生活服务 ────────→ meituan-coupon-workbuddy (S-017) [待处理]
```

### 1.5 Agent 参考库（215 个 Agent Prompt + 50 个架构教程）

> 当已部署 SKILL 无法覆盖需求时，查阅 Agent 参考库获取补充能力。
> 索引文件：`meta-suite/governance-system/agent-reference/AGENT-REFERENCE-INDEX.md`

```
需要什么能力？
│
├─ 工程/开发/代码 ─────────────→ agency-agents-zh/engineering/ (35 个 Agent)
├─ 营销/渠道/增长 ─────────────→ agency-agents-zh/marketing/ (36 个 Agent)
├─ 销售/投标/赢单 ─────────────→ agency-agents-zh/sales/ (8 个 Agent)
├─ 设计/UI/UX ─────────────────→ agency-agents-zh/design/ (8 个 Agent)
├─ 财务/法务/合规 ─────────────→ agency-agents-zh/finance/ + legal/ (10 个 Agent)
├─ 供应链/测试/硬件 ───────────→ agency-agents-zh/supply-chain/ + testing/ (13 个 Agent)
├─ 中国平台集成(微信/飞书/钉钉) → engineering/ 下对应 Agent
│
├─ SKILL 转 Agent 架构参考 ───→ genai-agents-tutorials/ (50 个 Notebook)
│   ├─ 项目管理 Agent ─────────→ project_manager_assistant_agent.ipynb
│   ├─ 报价系统 Agent ─────────→ contextual_quoting_agentic_system.ipynb
│   └─ MCP 工具桥 ────────────→ mcp-tutorial.ipynb
│
└─ 完整场景速查 ───────────────→ 读取 AGENT-REFERENCE-INDEX.md
```

---

## 二、产品轨 PT — 18 个 Skill

> **驱动标准**：NPDP（新产品开发）
> **核心使命**："做正确的事" — 产品战略、创新与全生命周期管理

### 快速选择指南

```
当前阶段？
│
├─ P1 启动（战略/调研/评估）
│   ├─ 制定产品战略/创新方向 ──→ PT-001 pd-product-strategy
│   ├─ 市场调研/竞品分析 ──────→ PT-003 pd-market-research
│   ├─ 用户研究/需求洞察 ──────→ PT-012 pd-user-research
│   └─ 产品机会评估/Go-NoGo ──→ PT-004 pd-go-nogo → 调用 S-001, E-001, E-006
│
├─ P2 规划（设计/流程）
│   ├─ 需求分析/产品设计 ──────→ PT-006 pd-requirements-design
│   ├─ 新产品开发流程 ─────────→ PT-002 pd-innovation-process → 调用 L-003
│   └─ 工业互联网产品设计 ────→ PT-017 工业互联网产品经理
│
├─ P3 文档
│   └─ 撰写 PRD ───────────────→ PT-007 pd-prd-writing
│
├─ P4 发布
│   └─ 产品上市/GTM/定价 ─────→ PT-008 pd-product-launch → 调用 E-suite, L-003
│
├─ P5 运营
│   └─ 产品运营/增长实验 ──────→ PT-011 pd-product-operations
│
├─ P6 收尾/战略
│   ├─ 生命周期管理/退市 ──────→ PT-009 pd-lifecycle-management
│   └─ 产品组合管理/资源分配 ─→ PT-005 pd-portfolio-management → 调用 E-suite
│
└─ CX 横切（全程可用）
    ├─ 工具/度量/OKR ──────────→ PT-013 pd-tools-metrics → 调用 E-suite
    ├─ 团队建设/协作 ──────────→ PT-014 pd-team-culture → 调用 S-005
    ├─ 跨阶段协调/PD-PM桥接 ──→ PT-015 pd-integration → 调用 S-003
    └─ 全流程编排/链路索引 ───→ PT-016 pd-workflow-chains
```

### 技能详情表

| # | 治理编号 | Skill 名称 | 阶段 | 核心能力 | 标准来源 | 跨 Suite 调用 |
|---|---------|-----------|------|---------|---------|--------------|
| 1 | PT-001 | pd-product-strategy | P1 | 创新战略4类型、商业模式画布、安索夫矩阵、路线图 | NPDP Ch1 | — |
| 2 | PT-002 | pd-innovation-process | P2 | Stage-Gate、精益BML、设计思维、敏捷Scrum、MVP/MMF | NPDP Ch3 | → L-003 |
| 3 | PT-003 | pd-market-research | P1 | TAM/SAM/SOM、PESTLE、波特五力、SWOT、12种研究方法 | NPDP Ch4 | — |
| 4 | PT-004 | pd-go-nogo | P1 | 8维度量化评估、一票否决项、市场/技术/商业可行性 | NPDP Ch1+Ch2 | → E-001, E-006, S-001 |
| 5 | PT-005 | pd-portfolio-management | P6 | 组合选择4方法、平衡3维度、资源分配、管道管理 | NPDP Ch2 | → E-001/002/004/006 |
| 6 | PT-006 | pd-requirements-design | P2 | KANO模型、Y模型、MoSCoW、用户故事INVEST、RTM | NPDP Ch3 | — |
| 7 | PT-007 | pd-prd-writing | P3 | 8模块PRD模板、BRD/MRD/PRD分层、数据埋点设计 | NPDP Ch3 | — |
| 8 | PT-008 | pd-product-launch | P4 | GTM策略、定价6模型、渠道策略、ICP、创新扩散理论 | NPDP Ch3+Ch7 | → E-suite, L-003 |
| 9 | PT-009 | pd-lifecycle-management | P6 | PLC四阶段、技术S曲线、退市策略、ESG、产品平台战略 | NPDP Ch7 | — |
| 10 | PT-011 | pd-product-operations | P5 | AARRR海盗指标、增长实验、A/B测试、灰度发布、特性开关 | NPDP Ch6 | — |
| 11 | PT-012 | pd-user-research | P1 | Persona、旅程地图CJM、JTBD三层、领先用户、OST机会方案树 | NPDP Ch4 | — |
| 12 | PT-013 | pd-tools-metrics | CX | OKR/KPI/北极星、ROI/NPV/IRR、TRIZ/SCAMPER/QFD | NPDP Ch6 | → E-suite |
| 13 | PT-014 | pd-team-culture | CX | 跨职能协作、产品铁三角、无授权领导力、NPDP团队类型 | NPDP Ch5 | → S-005 |
| 14 | PT-015 | pd-integration | CX | PdM角色定位、跨阶段协调、PD-PM协同桥接 | NPDP 全局 | → S-003 |
| 15 | PT-016 | pd-workflow-chains | CX | 5条标准链路+3条专项链路，15个PD Skill调用编排 | NPDP 全局 | — |
| 16 | PT-017 | 工业互联网产品经理 | P2 | MES、微制造管理、角色分析、场景驱动设计 | NPDP (领域特化) | — |
| 17 | PT-018 | product-solution-evaluator | P2 | 产品方案结构化评估：概念/功能/PRD/MVP/商业化/AI方案 | NPDP Ch2 | — |

> **注**：PT-010 为预留编号（当前未分配）。

### 流程引导

→ **详见 pd-workflow-chains (PT-016)**：5 条标准链路 + 3 条专项链路

| 链路编号 | 链路名称 | 涉及 Skill |
|---------|---------|-----------|
| PT-FLOW-001 | 新产品 0→1 | PT-001 → PT-003 → PT-002 → PT-004 → PT-007 → PT-008 → PT-011 |
| PT-FLOW-002 | 生命周期管理 | PT-009 → PT-013 → PT-005 |
| PT-FLOW-003 | 产品度量与改进 | PT-013 → PT-011 → PT-006 |

---

## 三、项目轨 JT — 18 个 Skill

> **驱动标准**：PMP + 一级建造师 + 55号令（政府投资项目）
> **核心使命**："正确地做事" — 项目全过程交付管理

### 快速选择指南

```
当前阶段？
│
├─ P1 启动（立项/招投标）
│   ├─ 分析招标文件 ───────────→ pm-tender-analysis
│   ├─ 编制投标方案 ───────────→ JT-002 pm-bid-proposal
│   └─ 项目立项/可行性 ───────→ JT-001 pm-project-opportunity
│
├─ P2 规划（范围/进度/风险）
│   ├─ 范围定义/WBS ──────────→ JT-003 pm-requirements-scope
│   ├─ 进度排期/成本估算 ─────→ JT-004 pm-schedule-cost → 调用 E-004
│   └─ 风险识别/应对 ─────────→ JT-010 pm-risk-management → 调用 E-003, S-009, L-003
│
├─ P3 采购
│   └─ 采购/合同/质量规划 ───→ JT-008 pm-procurement-quality → 调用 E-004, L-002
│
├─ P4 执行
│   ├─ 项目交付/现场管理 ─────→ JT-009 pm-project-delivery → 调用 S-002
│   └─ 质量保证/审计 ─────────→ JT-012 pm-quality-assurance
│
├─ P5 监控
│   ├─ 变更管理 ───────────────→ JT-006 pm-change-management
│   └─ 绩效跟踪/挣值分析 ───→ JT-011 pm-performance-tracking
│
├─ P6 收尾
│   ├─ 政府项目验收 ───────────→ JT-016 pm-gov-acceptance
│   └─ 项目收尾/知识沉淀 ─────→ JT-017 pm-project-closure
│
└─ CX 横切（全程可用）
    ├─ 团队管理/沟通协调 ─────→ JT-014 pm-team-communication
    ├─ 干系人管理 ─────────────→ JT-015 pm-stakeholder-management → 调用 S-005
    ├─ 项目整合管理 ───────────→ JT-005 pm-integration → 调用 S-003
    └─ 全流程编排/链路索引 ───→ JT-018 pm-workflow-chains
```

### 技能详情表

| # | 治理编号 | Skill 名称 | 阶段 | 核心能力 | 标准来源 | 跨 Suite 调用 |
|---|---------|-----------|------|---------|---------|--------------|
| 1 | JT-001 | pm-project-opportunity | P1 | 8维度Go/No-Go、项目建议书/可研/初设/详设全流程 | PMP+一建+55号令 | — |
| 2 | JT-002 | pm-bid-proposal | P1 | 投标决策、技术方案4种架构模板、商务标、报价策略 | 招投标法+PMBOK Ch12 | — |
| 3 | — | pm-tender-analysis | P1 | 资质核查、评分矩阵、风险信号、竞标分析 | 招投标法 | — |
| 4 | JT-003 | pm-requirements-scope | P2 | WBS、RTM、MoSCoW、范围基准 | PMBOK Ch5 | — |
| 5 | JT-004 | pm-schedule-cost | P2 | CPM、甘特图、EVM挣值、FPA/COCOMO II估算 | PMBOK Ch6+Ch7 | → E-004 |
| 6 | JT-005 | pm-integration | CX | 项目章程、管理计划9子计划、知识管理、跨SKILL协调 | PMBOK Ch4 | → S-003 |
| 7 | JT-006 | pm-change-management | P5 | CR全流程、CCB运作、六维影响分析、55号令>10%红线 | PMBOK Ch4 | — |
| 8 | JT-008 | pm-procurement-quality | P3 | 自制/外购、RFP/RFQ、合同类型、QC七大工具 | PMBOK Ch8+Ch12 | → E-004, L-002 |
| 9 | JT-009 | pm-project-delivery | P4 | Kick-off、工作包执行、监理例会、Sprint管理、现场签证 | PMP执行过程组 | → S-002 |
| 10 | JT-010 | pm-risk-management | P2 | SWOT/德尔菲识别、PIM定性、EMV/蒙特卡洛定量、4种应对 | PMBOK Ch11 | → E-003, S-009, L-003 |
| 11 | JT-011 | pm-performance-tracking | P5 | WPD→WPI→WPR、SV/CV/SPI/CPI/TCPI、燃尽图 | PMP监控过程组 | — |
| 12 | JT-012 | pm-quality-assurance | P4 | QA审计、COQ、配置管理FCA+PCA、Kaizen/六西格玛 | PMBOK Ch8 | — |
| 13 | JT-014 | pm-team-communication | CX | RACI、塔克曼阶梯、冲突管理、5W1H沟通计划 | PMBOK Ch9+Ch10 | — |
| 14 | JT-015 | pm-stakeholder-management | CX | 权力-利益矩阵、参与度五级评估、参与策略制定 | PMBOK Ch13 | → S-005 |
| 15 | JT-016 | pm-gov-acceptance | P6 | 四大验收、等保测评、绩效评价、整改复验 | 55号令+一建实务 | — |
| 16 | JT-017 | pm-project-closure | P6 | 行政收尾、经验教训登记册、运维交接、质保期 | PMP收尾过程组 | — |
| 17 | JT-018 | pm-workflow-chains | CX | 5条标准链路+2条专项链路，15个PM Skill调用编排 | PMP 全局 | — |
| 18 | — | pm-skills-reference | CX | 产品经理技能索引（65技能+36工作流+8插件） | — | — |

> **注**：pm-tender-analysis 和 pm-skills-reference 当前无治理编号。JT-007/JT-013 为预留编号。

### 流程引导

→ **详见 pm-workflow-chains (JT-018)**：5 条标准链路 + 2 条专项链路

| 链路编号 | 链路名称 | 涉及 Skill |
|---------|---------|-----------|
| JT-FLOW-001 | 项目立项到收尾 | JT-001 → JT-003 → JT-004 → JT-010 → JT-009 → JT-012 → JT-006 → JT-011 → JT-016 → JT-017 |
| JT-FLOW-002 | 政府项目验收 | JT-012 → JT-016 → JT-017 |
| JT-FLOW-003 | 招投标全流程 | pm-tender-analysis → JT-002 → JT-001 → JT-008 |

---

## 四、共用层 S — 24 个 Skill

> **定位**：PD/PM 双轨共享方法论 + 通用工具 + 独立领域能力

### 4.1 Meta-Suite（8 个）— PD/PM 共享方法论 + 治理工具

> 被双轨 Skill 按需调用的"方法基座" + 技能体系治理工具

| # | 治理编号 | Skill 名称 | 核心能力 | 被调用方 |
|---|---------|-----------|---------|---------|
| 1 | S-001 | meta-decision-frameworks | 决策框架：加权评分、MoSCoW+RICE、决策树EMV、成对比较、六顶思考帽 | PT-004, PT-013, JT-004, JT-008 |
| 2 | S-002 | meta-development-methodology | 开发方法选择：预测/迭代/增量/敏捷/混合5种、生命周期映射、决策矩阵 | PT-002, PT-015, JT-009 |
| 3 | S-003 | meta-professional-ethics | PMI四大价值观、利益冲突、数据伦理、法规约束 | PT-015, JT-005 |
| 4 | S-004 | meta-risk-basics | 概率-影响矩阵、4种应对策略、风险登记册、风险分类 | PT-004, JT-010 |
| 5 | S-005 | meta-stakeholder-analysis | 3维度识别、权力-利益矩阵、参与度评估、参与策略 | PT-014, JT-015 |
| 6 | S-022 | skill-creator-optimized | 技能包生成与优化：需求转标准化SKILL、YAML补齐、封装交付 | 治理工具 |
| 7 | S-023 | skill-refactor | 技能改造：领域消除评估 + 工作流重构，十一步法 | 治理工具 |
| 8 | S-024 | skill-forge | 技能锻造：面试式创建 + 安全审计 + SkillHub对标 | 治理工具 |

### 4.2 Expert-Suite（2 个）— 专家视角

> 提供高格局思维与颠覆式创新视角，可在任何阶段叠加使用

| # | 治理编号 | Skill 名称 | 核心能力 | 适用场景 |
|---|---------|-----------|---------|---------|
| 1 | S-006 | high-vision-perspective | 时空升维、终局倒推、认命改运、三层透视（吴军+王志纲） | 战略规划、职业决策 |
| 2 | S-007 | zhou-hongyi-perspective-v2 | 免费模式、颠覆式创新、用户思维、战斗文化（周鸿祎） | 产品创新、竞争策略 |

### 4.3 General-Suite（6 个）— 通用办公

> 文档处理与日常办公工具

| # | 治理编号 | Skill 名称 | 阶段 | 核心能力 |
|---|---------|-----------|------|---------|
| 1 | S-010 | meeting-minutes | CX | 会议摘要与纪要：多格式模板、行动项跟踪、决策记录 |
| 2 | S-011 | doc-versioner | P4 | 文档版本化出版：Markdown快照、模板初始化、批量生成、修订记录 |
| 3 | S-015 | md-to-pdf-cjk | P4 | Markdown→PDF：reportlab渲染、CJK字体支持 |
| 4 | S-016 | markitdown-skill | P4 | 文档→Markdown：PDF/Word/PPT/图片OCR/音频转写 |
| 5 | S-020 | excel-xlsx | CX | Excel/XLSX工作簿：创建/编辑/公式/格式/模板保留 |
| 6 | S-021 | tech-doc-writer | CX | 技术文档写作：应标/招投标/设计文档/接口文档/架构文档 |

### 4.4 独立领域 Skill（8 个）

> 各领域专用工具，独立于 PD/PM 双轨主链路

| # | 治理编号 | Skill 名称 | 核心能力 | 部署状态 |
|---|---------|-----------|---------|---------|
| 1 | S-008 | tools-bayesian-update | 贝叶斯概率更新：先验→后验、动态更新模型参数 | general-suite |
| 2 | S-009 | tools-monte-carlo | 蒙特卡洛模拟：随机抽样、分布拟合、定量风险分析 | general-suite |
| 3 | S-012 | insurance-policy-analysis | 保险保单分析：CV+RPU双维度、EPV精算、组合优化、特殊场景压测 | 已部署 |
| 4 | S-014 | wechat-article-parser | 微信公众号文章解析：内容提取、摘要、可选保存飞书 | 已部署 |
| 5 | S-017 | meituan-coupon-workbuddy | 美团优惠券领取（外部商业 Skill） | 待处理 |
| 6 | S-018 | resume-optimizer | 简历全流程：创建/定制/优化/分析/JD匹配/PDF导出 | 已部署 |
| 7 | S-019 | gridman | 财税超级特工：会计/审计/税务/投行/内控/ESG | 已部署 |

> **注**：S-008、S-009 已于 2026-06-29 从 `inbox/skills-legacy` 迁移至 `general-suite/`。S-013 为预留编号。

---

## 五、经济决策 E — 7 个 Skill

> **定位**：定量经济分析工具集，被 PD/PM 双轨按需调用
> **元技能**：economic-decision (E-007) 可自动识别场景并调度其余 6 个工具

| # | 治理编号 | Skill 名称 | 核心能力 | 典型调用方 |
|---|---------|-----------|---------|-----------|
| 1 | E-001 | economic-npv | NPV 净现值计算 | PT-004, PT-005, PT-008, PT-013 |
| 2 | E-002 | economic-irr | IRR 内部收益率计算 | PT-005, PT-013 |
| 3 | E-003 | economic-sensitivity | 敏感性分析（龙卷风图、开关分析） | JT-010 |
| 4 | E-004 | economic-comparison | 方案比选（增量分析、年值法、现值法） | JT-004, JT-008 |
| 5 | E-005 | economic-ve | 价值工程（V=F/C 功能成本分析） | — |
| 6 | E-006 | economic-payback | 投资回收期（静态/动态） | PT-004, PT-005 |
| 7 | E-007 | economic-decision | **元技能**：场景识别 → 自动调度 E-001~E-006 | 不确定时首选 |

### 调用关系

```
PT-004 (go-nogo) ──────→ E-001 (NPV) + E-006 (payback)
PT-005 (portfolio) ────→ E-001 + E-002 (IRR) + E-004 (comparison) + E-006
PT-008 (launch) ───────→ E-suite 全套
PT-013 (metrics) ──────→ E-suite 全套
JT-004 (schedule-cost) → E-004 (comparison)
JT-008 (procurement) ──→ E-004 (comparison)
JT-010 (risk) ─────────→ E-003 (sensitivity)
```

---

## 六、法律服务 L — 4 个 Skill

> **定位**：法律支持工具集，覆盖法律咨询、合同审查、IP 保护、合规自动化

| # | 治理编号 | Skill 名称 | 核心能力 | 典型调用方 |
|---|---------|-----------|---------|-----------|
| 1 | L-001 | law-skills | 法律咨询 + 起诉状生成 + 法条查询 | 直接使用 |
| 2 | L-002 | contract-review | 合同审查 + 风险条款识别 + 修改建议 | JT-008 |
| 3 | L-003 | ip-protection | IP保护策略 + 侵权风险分析 + 专利/商标/版权 | PT-002, PT-008, JT-010 |
| 4 | L-004 | legal-compliance-bundle | 50个中国法律合规子技能：合同审查/法规查询/劳动合规/数据保护等 | 直接使用 |

### 调用关系

```
PT-002 (innovation) ──→ L-003 (IP保护)
PT-008 (launch) ──────→ L-003 (IP保护)
JT-008 (procurement) ─→ L-002 (合同审查)
JT-010 (risk) ────────→ L-003 (IP保护)
```

---

## 七、阅读操作系统 R — 3 个 Skill

> **定位**：个人知识管理与阅读体系

| # | 治理编号 | Skill 名称 | 核心能力 | 适用场景 |
|---|---------|-----------|---------|---------|
| 1 | R-001 | reading-book-deconstruction | 深度拆书 · 资产化输出 | 精读一本书并产出结构化笔记 |
| 2 | R-002 | reading-bookshelf-health | 书架体检 · 注意力雷达 | 评估阅读结构是否健康 |
| 3 | R-003 | reading-role-path | 角色适配 · 三层阅读路径 | 根据角色选择阅读策略 |

---

## 八、跨 Suite 调用关系

> 本章节汇总所有跨 Suite 的依赖关系，便于理解 Skill 之间的协作网络。

### 8.1 总览图

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Skill 体系调用全景                            │
│                                                                     │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                      │
│  │ PD-Suite │    │ PM-Suite │    │ S-Suite  │                      │
│  │  (17个)  │    │  (18个)  │    │  (19个)  │                      │
│  └────┬─────┘    └────┬─────┘    └────┬─────┘                      │
│       │               │               │                             │
│       │    ┌──────────┴──────────┐    │                             │
│       │    │    Meta-Suite       │    │                             │
│       ├───→│  S-001~S-005 (5个) │←───┤  (被 PD/PM 共享调用)        │
│       │    └─────────────────────┘    │                             │
│       │                               │                             │
│       │    ┌─────────────────────┐    │                             │
│       ├───→│  Economic-Suite (7) │←───┤  (定量经济分析)             │
│       │    └─────────────────────┘    │                             │
│       │                               │                             │
│       │    ┌─────────────────────┐    │                             │
│       ├───→│   Legal-Suite (3)   │←───┤  (法律支持)                 │
│       │    └─────────────────────┘    │                             │
│       │                               │                             │
│       │    ┌─────────────────────┐    │                             │
│       │    │  Expert-Suite (2)   │    │  (可选叠加)                 │
│       │    └─────────────────────┘    │                             │
│       │                               │                             │
│       │    ┌─────────────────────┐    │                             │
│       │    │  Reading-OS (3)     │    │  (独立)                     │
│       │    └─────────────────────┘    │                             │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.2 PD → Economic 调用明细

| PD Skill | 调用的 Economic Skill | 场景 |
|----------|----------------------|------|
| PT-004 pd-go-nogo | E-001 (NPV), E-006 (payback) | 产品机会评估时计算财务可行性 |
| PT-005 pd-portfolio-management | E-001, E-002 (IRR), E-004 (comparison), E-006 | 组合选择时进行多维度经济比选 |
| PT-008 pd-product-launch | E-suite 全套 | 上市前全面经济测算 |
| PT-013 pd-tools-metrics | E-suite 全套 | 度量体系中集成经济指标 |

### 8.3 PD → Legal 调用明细

| PD Skill | 调用的 Legal Skill | 场景 |
|----------|-------------------|------|
| PT-002 pd-innovation-process | L-003 (ip-protection) | 创新流程中的 IP 保护策略 |
| PT-008 pd-product-launch | L-003 (ip-protection) | 上市前的 IP 风险评估 |

### 8.4 PM → Economic 调用明细

| PM Skill | 调用的 Economic Skill | 场景 |
|----------|----------------------|------|
| JT-004 pm-schedule-cost | E-004 (comparison) | 方案比选时的增量分析 |
| JT-008 pm-procurement-quality | E-004 (comparison) | 采购方案经济比选 |
| JT-010 pm-risk-management | E-003 (sensitivity) | 风险定量分析-敏感性 |

### 8.5 PM → Legal 调用明细

| PM Skill | 调用的 Legal Skill | 场景 |
|----------|-------------------|------|
| JT-008 pm-procurement-quality | L-002 (contract-review) | 采购合同审查 |
| JT-010 pm-risk-management | L-003 (ip-protection) | 项目 IP 风险识别 |

### 8.6 Meta-Suite 被调用汇总

| Meta Skill | 被 PD 调用 | 被 PM 调用 |
|-----------|-----------|-----------|
| S-001 meta-decision-frameworks | PT-004, PT-013 | JT-004, JT-008 |
| S-002 meta-development-methodology | PT-002, PT-015 | JT-009 |
| S-003 meta-professional-ethics | PT-015 | JT-005 |
| S-004 meta-risk-basics | PT-004 | JT-010 |
| S-005 meta-stakeholder-analysis | PT-014 | JT-015 |

### 8.7 跨轨桥接：PT ↔ JT

| 桥接点 | PT 侧 | JT 侧 | 说明 |
|--------|-------|-------|------|
| PD-PM 协同 | PT-015 pd-integration | JT-005 pm-integration | 产品→项目交接、需求对齐 |
| 需求传递 | PT-007 pd-prd-writing | JT-003 pm-requirements-scope | PRD → WBS 的需求转化 |
| 风险共享 | PT-004 pd-go-nogo | JT-010 pm-risk-management | 产品风险→项目风险的传递 |
| 经济共算 | PT-005 pd-portfolio | JT-004 pm-schedule-cost | 产品组合决策影响项目预算 |

---

## 九、标准业务流程索引

> 以下为完整的端到端业务流程，每条流程标注了经过的 Skill 节点。

### 产品轨流程

| 编号 | 流程名称 | 步骤 | 经过的 Skill |
|------|---------|------|-------------|
| PT-FLOW-001 | 新产品 0→1 | 7步 | PT-001 → PT-003 → PT-012 → PT-002 → PT-004 → PT-007 → PT-008 → PT-011 |
| PT-FLOW-002 | 生命周期管理 | 3步 | PT-009 → PT-013 → PT-005 |
| PT-FLOW-003 | 产品度量与改进 | 3步 | PT-013 → PT-011 → PT-006 |

### 项目轨流程

| 编号 | 流程名称 | 步骤 | 经过的 Skill |
|------|---------|------|-------------|
| JT-FLOW-001 | 项目立项到收尾 | 10步 | JT-001 → JT-003 → JT-004 → JT-010 → JT-009 → JT-012 → JT-006 → JT-011 → JT-016 → JT-017 |
| JT-FLOW-002 | 政府项目验收 | 3步 | JT-012 → JT-016 → JT-017 |
| JT-FLOW-003 | 招投标全流程 | 4步 | pm-tender-analysis → JT-002 → JT-001 → JT-008 |

### 跨轨流程

| 编号 | 流程名称 | 步骤 | 经过的 Skill |
|------|---------|------|-------------|
| PT-JT-FLOW-001 | 产品→项目衔接 | 3步 | PT-015 → JT-005 → JT-003 |

### 共用层流程

| 编号 | 流程名称 | 步骤 | 经过的 Skill |
|------|---------|------|-------------|
| S-FLOW-001 | 简历创建与优化 | 5步 | S-018 → S-015 (PDF导出) |
| S-FLOW-002 | 求职全流程 | 4步 | S-018 → PT-011 (数据跟踪) → S-006 (战略视角) |
| 财税流程 | Gridman 全流程 | — | S-019 (会计/审计/税务/投行/内控/ESG) |

---

## 十、统计摘要

### 10.1 各 Suite 数量统计

| Suite | 数量 | 治理编号范围 | 说明 |
|-------|------|-------------|------|
| PD-Suite (产品轨) | 18 | PT-001 ~ PT-018 | PT-010 预留 |
| PM-Suite (项目轨) | 18 | JT-001 ~ JT-018 | JT-007/JT-013 预留；2个无编号 |
| S-Suite (共用层) | 24 | S-001 ~ S-024 | S-013 预留 |
| Economic-Suite | 7 | E-001 ~ E-007 | 含 1 个元技能 |
| Legal-Suite | 4 | L-001 ~ L-004 | — |
| Reading-OS | 3 | R-001 ~ R-003 | — |
| **合计** | **74** | — | 含 pm-skills-reference 等无编号工具 |

> **注**：体系总览中"62 个"为含治理编号的核心 Skill 数（去除 pm-skills-reference、pm-tender-analysis 等无编号工具后为 62 个核心部署）。

### 10.2 阶段分布

| 阶段 | PD-Suite | PM-Suite | S-Suite | 合计 |
|------|----------|----------|---------|------|
| P1 启动 | 3 (PT-001/003/012) + PT-004 | 3 (JT-001/002, tender) | 0 | **7** |
| P2 规划 | 3 (PT-002/006/017) + PT-018 | 3 (JT-003/004/010) | 0 | **7** |
| P3 文档/采购 | 1 (PT-007) | 1 (JT-008) | 0 | **2** |
| P4 发布/执行 | 1 (PT-008) | 2 (JT-009/012) | 3 (S-011/015/016) | **6** |
| P5 运营/监控 | 1 (PT-011) | 2 (JT-006/011) | 0 | **3** |
| P6 收尾/战略 | 2 (PT-005/009) | 2 (JT-016/017) | 0 | **4** |
| CX 横切 | 6 (PT-011~016) | 7 (JT-005/014/015/018, skills-ref, integration, tender) | 21 (全部 S-Suite) | **34** |

### 10.3 跨 Suite 调用统计

| 调用方向 | 调用次数 | 涉及 Skill 对 |
|---------|---------|--------------|
| PD → Economic | 10 | PT-004(2), PT-005(4), PT-008(全), PT-013(全) |
| PD → Legal | 2 | PT-002→L-003, PT-008→L-003 |
| PM → Economic | 3 | JT-004→E-004, JT-008→E-004, JT-010→E-003 |
| PM → Legal | 2 | JT-008→L-002, JT-010→L-003 |
| PD → Meta | 5 | PT-004→S-001/S-004, PT-013→S-001, PT-014→S-005, PT-015→S-003, PT-002→S-002 |
| PM → Meta | 5 | JT-004→S-001, JT-005→S-003, JT-008→S-001, JT-009→S-002, JT-010→S-004, JT-015→S-005 |

### 10.4 特殊标注

| 标注项 | 说明 |
|--------|------|
| 已迁移 | S-008 (tools-bayesian-update), S-009 (tools-monte-carlo) 已于 2026-06-29 迁移至 `general-suite/` |
| 新部署 | PT-018, L-004, S-020~S-024 于 2026-06-29 从 inbox 部署至主目录 |
| 待处理 | S-017 (meituan-coupon-workbuddy) 为外部商业 Skill，待处理 |
| 无治理编号 | pm-tender-analysis, pm-skills-reference 当前无治理编号 |
| 预留编号 | PT-010, JT-007, JT-013, S-013 |
| 元技能 | E-007 (economic-decision) 可自动调度 E-001~E-006 |
| 领域特化 | PT-017 (工业互联网产品经理) 为 NPDP 领域特化版本 |

---

## 七、新增 Suites 索引（2026-07-07 P2 搬迁）

2026-07-07 完成 inbox 54 个技能搬迁，新增以下 suite 目录：

### 7.1 `industry-suite/` — 行业技能（5 个）

| 技能 | 说明 |
|------|------|
| bookkeeping-agency | 代理记账行业十大功能集群 |
| c2c-platform | C2C 本地生活服务平台十大功能集群 |
| metabolic-healing | 代谢慢病调理十大功能集群 |
| pharma（含 references/pharma-doc-reference） | 医药行业十大功能集群 |
| universal-business | 通用行业业务能力框架（抽象层） |

### 7.2 `research-suite/` — 研究技能（3 个）

| 技能 | 说明 |
|------|------|
| cda/cda (根) | CDA 因果动力学架构知识参考 |
| cda/cda-code-lab | CDA 架构代码生成 |
| cda/cda-data-synth | CDA 因果数据合成器 |

### 7.3 `expert-suite/service-design/` — 服务设计专家天团（11 个）

| 技能 | 说明 |
|------|------|
| service-design | 总入口·SkillHub |
| fwsjtt-chief-consultant | 总咨询顾问·目标澄清 |
| fwsjtt-customer-discovery-expert | 客户发现专家 |
| fwsjtt-delivery-qa-reviewer | 交付质量审查 |
| fwsjtt-evidence-auditor | 证据审计 |
| fwsjtt-expert-team | 专家团总控调度 |
| fwsjtt-metrics-architect | 指标体系架构师 |
| fwsjtt-roi-strategist | ROI 测算师 |
| fwsjtt-service-designer | 服务体验设计师 |
| fwsjtt-strategy-growth-advisor | 战略增长顾问 |
| fwsjtt-theory-distiller | 理论萃取师 |

### 7.4 `general-suite/` 新增工具（14 个 + 4 个 references）

工具类：builtin-tools, cad-editor, chat-bus, gamebox, academic-thesis-workflow, thesis-topic-selector, bilingual-buddy, knowledge-explainer, wealth-manager, ai-dev-workflow, style-design-generator, auto-dealer-ripcas-marketing, find-skills, liurun-writing-assistant, polymarket-trade  
参考类：singlefile-output-reference, smart-hardware-reference, ultimate-domain-payload, web-novel-writing-reference

### 7.5 `meta-suite/` 新增方法技能（16 个）

adaptive-skill-stack, capability-pipeline-os, cogniexec, compose-methods, comprehensive-knowledge-system, domain-elimination-assessor, domain-payload-generator, identity-primitive-chain-prompt, innovation-os, ipo-model, self-improving-agent, solopreneur-os, universal-primitives, universal-task-os, workflow-refactor

---

*本文档为 Skill 体系的引导层主文件。详细链路编排请参见 PT-016 (pd-workflow-chains) 和 JT-018 (pm-workflow-chains)。*
*建议每季度或在 Skill 增删时更新。*
