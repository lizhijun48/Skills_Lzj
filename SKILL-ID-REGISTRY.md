# SKILL-ID-REGISTRY.md — 技能编号注册表

> 版本：v1.1.5 | 最后更新：2026-07-09
> 用途：统一编号规则 + 已用编号清单（含阶段、备注）+ 新编号分配规则
> 已合并 DEPLOYED_MAPPING.md 的阶段与备注信息
> 查阅此文件即可知编号→路径→阶段→状态，不需要反复扫描技能目录

---

## 1. 编号规则

| 前缀 | 套件 | 含义 | 编号范围 |
|------|------|------|----------|
| PT- | pd-suite/ | 产品轨（Product Track） | PT-001 ~ PT-099 |
| JT- | pm-suite/ | 项目轨（Project Track） | JT-001 ~ JT-099 |
| S- | meta-suite/ + 独立通用技能 | 共用层（Shared） | S-001 ~ S-099 |
| E- | economic-suite/ | 经济决策工具 | E-001 ~ E-099 |
| L- | legal-suite/ | 法律服务 | L-001 ~ L-099 |
| R- | reading-os/ | 阅读操作系统 | R-001 ~ R-099 |
| X- | expert-suite/ | 专家视角 | X-001 ~ X-099 |
| GX- | gaoxiang-suite/ | 高项备考（Gaoxiang Exam） | GX-000 ~ GX-099 |

**编号分配原则**：
1. 每个技能有且仅有一个 `governance_id`
2. 编号一旦分配，不重复使用（即使技能被删除）
3. 新技能按"套件内最大编号+1"分配

---

## 2. 已用编号清单（当前体系）

### PT- 产品轨（pd-suite/）

| 编号 | 技能路径 | 技能名 | 阶段 | 状态 | 备注 |
|------|----------|--------|------|------|------|
| PT-001 | pd-suite/pd-product-strategy | 产品战略与创新管理 | P1 | [有效] | — |
| PT-002 | pd-suite/pd-innovation-process | 新产品开发流程 | P2 | [有效] | — |
| PT-003 | pd-suite/pd-market-research | 市场研究与竞品分析 | P1 | [有效] | — |
| PT-004 | pd-suite/pd-go-nogo | 产品机会评估与Go/No-Go决策 | P1 | [有效] | — |
| PT-005 | pd-suite/pd-portfolio-management | 产品组合管理 | P6 | [有效] | — |
| PT-006 | pd-suite/pd-requirements-design | 需求分析与产品设计 | P2 | [有效] | — |
| PT-007 | pd-suite/pd-prd-writing | PRD与需求文档 | P3 | [有效] | — |
| PT-008 | pd-suite/pd-product-launch | 产品发布与上市管理 | P4 | [有效] | — |
| PT-009 | pd-suite/pd-lifecycle-management | 产品生命周期管理 | P6 | [有效] | — |
| PT-010 | （空） | 待分配 | — | [可用] | — |
| PT-011 | pd-suite/pd-product-operations | 产品运营与增长 | P5 | [有效] | — |
| PT-012 | pd-suite/pd-user-research | 用户研究与需求洞察（含录音/文本洞察抽取子能力 insight-extraction） | P1 | [有效] | 2026-07-06 补充 insight-extraction 子能力 |
| PT-013 | pd-suite/pd-tools-metrics | 工具与度量体系 | CX | [有效] | — |
| PT-014 | pd-suite/pd-team-culture | 产品团队与文化组织 | CX | [有效] | — |
| PT-015 | pd-suite/pd-integration | 产品整合管理 | CX | [有效] | — |
| PT-016 | pd-suite/pd-workflow-chains | PD链式工作流索引 | CX | [有效] | — |
| PT-017 | pd-suite/工业互联网产品经理 | 工业互联网产品经理 | P2 | [有效] | 领域特化 |
| PT-018 | pd-suite/product-solution-evaluator | 产品方案评估专家 | P2 | [有效] | 新部署 |
| PT-019 | pd-suite/pd-ai-research-workflow | AI驱动的市场研究编排 | P1 | [有效] | 2026-07-06 从 ai-pm-exploration-toolkit 提取（执行/编排层，框架方法转 PT-003） |

---

### JT- 项目轨（pm-suite/）

| 编号 | 技能路径 | 技能名 | 阶段 | 状态 | 备注 |
|------|----------|--------|------|------|------|
| JT-001 | pm-suite/pm-project-opportunity | 项目立项管理 | P1 | [有效] | — |
| JT-002 | pm-suite/pm-bid-proposal | 招投标方案编制 | P1 | [有效] | 已吸收3个投标技能包 |
| JT-003 | pm-suite/pm-requirements-scope | 需求管理与范围定义 | P2 | [有效] | — |
| JT-004 | pm-suite/pm-schedule-cost | 进度管理与成本控制 | P2 | [有效] | — |
| JT-005 | pm-suite/pm-integration | 项目整合管理 | CX | [有效] | — |
| JT-006 | pm-suite/pm-change-management | 变更管理 | P5 | [有效] | — |
| JT-007 | （空） | 待分配 | — | [可用] | — |
| JT-008 | pm-suite/pm-procurement-quality | 采购管理与质量规划 | P3 | [有效] | — |
| JT-009 | pm-suite/pm-project-delivery | 项目交付管理 | P4 | [有效] | — |
| JT-010 | pm-suite/pm-risk-management | 风险管理 | P2 | [有效] | — |
| JT-011 | pm-suite/pm-performance-tracking | 绩效跟踪与状态报告 | P5 | [有效] | — |
| JT-012 | pm-suite/pm-quality-assurance | 质量保证与过程改进 | P4 | [有效] | — |
| JT-013 | （空） | 待分配 | — | [可用] | — |
| JT-014 | pm-suite/pm-team-communication | 团队管理与沟通协调 | CX | [有效] | — |
| JT-015 | pm-suite/pm-stakeholder-management | 干系人管理 | CX | [有效] | — |
| JT-016 | pm-suite/pm-gov-acceptance | 政府项目验收管理 | P6 | [有效] | — |
| JT-017 | pm-suite/pm-project-closure | 项目收尾与知识沉淀 | P6 | [有效] | — |
| JT-018 | pm-suite/pm-workflow-chains | PM链式工作流索引 | CX | [有效] | — |
| JT-019 | pm-suite/pm-tender-analysis | 招标文件智能解析 | P1 | [有效] | 2026-07-07 从 JT-003 冲突纠正，分配新编号；pm-bid-proposal (JT-002) 前置解析环节 |
| JT-020 | pm-suite/pm-it-governance | 信息系统治理 | CX | [有效] | 2026-07-09 新增·组织级 IT 治理入口；对标高项第3章；骨架版待学习填充；下游→JT-001/JT-013/JT-016 |

---

### S- 共用层（meta-suite/ + 独立通用技能）

| 编号 | 技能路径 | 技能名 | 阶段 | 状态 | 备注 |
|------|----------|--------|------|------|------|
| S-001 | meta-suite/meta-decision-frameworks | 决策框架通用工具集 | CX | [有效] | — |
| S-002 | meta-suite/meta-development-methodology | 开发方法与生命周期选择 | CX | [有效] | — |
| S-003 | meta-suite/meta-professional-ethics | 职业道德与专业行为规范 | CX | [有效] | — |
| S-004 | meta-suite/meta-risk-basics | 风险管理基础通用框架 | CX | [有效] | — |
| S-005 | meta-suite/meta-stakeholder-analysis | 干系人分析通用框架 | CX | [有效] | — |
| S-006 | expert-suite/high-vision-perspective | 高格局思维视角 | CX | [有效] | — |
| S-007 | expert-suite/zhou-hongyi-perspective-v2 | 周鸿祎思维视角 | CX | [有效] | — |
| S-008 | general-suite/tools-bayesian-update | 贝叶斯概率更新工具 | CX | [有效] | 已迁移 |
| S-009 | general-suite/tools-monte-carlo | 蒙特卡洛模拟工具 | CX | [有效] | 已迁移 |
| S-010 | general-suite/meeting-minutes | 会议摘要与纪要 | CX | [有效] | — |
| S-011 | general-suite/doc-versioner | 文档版本化出版工具 | P4 | [有效] | — |
| S-012 | insurance-policy-analysis | 保险保单分析 | CX | [有效] | 独立部署 |
| S-013 | （空，原resume-optimizer已合并至S-018） | 已释放 | — | [可用] | — |
| S-014 | wechat-article-parser | 微信公众号文章解析 | CX | [有效] | 独立部署 |
| S-015 | general-suite/md-to-pdf-cjk | Markdown转PDF（CJK支持） | P4 | [有效] | — |
| S-016 | general-suite/markitdown-skill | 文档转Markdown | P4 | [有效] | — |
| S-017 | inbox/meituan-coupon-workbuddy | 美团生活助手 | Domain | [待处理] | 外部商业Skill |
| S-018 | resume-optimizer | 简历优化助手（合并版） | CX | [有效] | — |
| S-019 | gridman | 财税超级特工（Hyper Agent） | CX | [有效] | — |
| S-020 | general-suite/excel-xlsx | Excel/XLSX工作簿处理 | CX | [有效] | 新部署 |
| S-021 | general-suite/tech-doc-writer | 技术文档写作助手 | CX | [有效] | 新部署 |
| S-022 | meta-suite/skill-creator-optimized | 技能包创建与优化 | CX | [有效] | 新部署 |
| S-023 | meta-suite/skill-refactor | 技能改造方法 | CX | [有效] | 新部署 |
| S-024 | meta-suite/skill-forge | 技能锻造（面试式创建） | CX | [有效] | 新部署 |
| S-025 | meta-suite/skill-extraction-sop | 从外部项目提取可复用技能的SOP | CX | [有效] | 2026-07-06 从 ai-pm-exploration-toolkit 提取实践沉淀；判定净增量→净化→落地→同步治理表 |
| S-026 | general-suite/prompt-engineering-basics | 提示语工程基础 | P1 | [有效] | 2026-08-09 新增；基于清华DeepSeek从入门到精通；DNA元素/六大类型/五大策略/TASTE·ALIGN框架 |
| S-027 | general-suite/prompt-chain-design | 提示语链设计 | P1 | [有效] | 2026-08-09 新增；CIRS模型/SPECTRA分解/三链融合/任务分解七步骤 |
| S-028 | general-suite/creative-prompt-techniques | 创意提示语技术 | P1 | [有效] | 2026-08-09 新增；IDEA/FOCUS/BRIDGE/CMM/CGS/EHS/MCS七大创意框架 |
| S-029 | general-suite/reasoning-model-strategy | 推理模型使用策略 | P1 | [有效] | 2026-08-09 新增；模型选择决策树/提示语差异/可控性原则/认知外化 |
| S-030 | general-suite/ai-content-quality | AI内容质量管控 | P1 | [有效] | 2026-08-09 新增；幻觉五类识别/三重概率交互/PIA·TFM·DES |
| S-031 | general-suite/ai-collaboration-mindset | AI人机协作思维 | P1 | [有效] | 2026-08-09 新增；四大核心能力/知识唤醒/三层次突破路径 |
| S-032 | general-suite/chart-diagram-generator | 图表绘制元技能 | P1 | [有效] | 2026-08-09 新增；SVG/Mermaid/React三引擎选择与生成 |
| S-033 | general-suite/general-workflow-chains | 通用技能链式工作流索引 | CX | [有效] | 2026-08-09 新增；3条标准链路+2条专项链路，连接AI辅助编程技能与现有通用技能 |
| S-034 | general-suite/copywriting | 文案写作 | P1 | [有效] | 2026-08-09 新增；文案三要素（信息传递/情感共鸣/行动引导）、诊断式模板选择、六大文案模板、语言风格三件套调用 |
| S-035 | general-suite/marketing-planning | 营销策划 | P1 | [有效] | 2026-08-09 新增；三大模块（创意概念/传播策略/执行方案）、渠道选择矩阵、传播节奏设计、效果评估框架 |
| S-036 | general-suite/brand-positioning | 品牌定位 | P1 | [有效] | 2026-08-09 新增；四大关键考量、战略层级分层（企业/产品线/单品）、8组件模板、评估标准 |
| S-037 | general-suite/value-proposition | 价值主张 | P1 | [有效] | 2026-08-09 新增；四大关键考量、战略层级分层、10组件价值主张画布、功能-情感平衡模型 |
| S-038 | general-suite/future-vision | 未来愿景 | P1 | [有效] | 2026-08-09 新增；四大关键考量、战略层级分层、12组件愿景模板、远大与可实现平衡 |
| S-039 | general-suite/three-chain-orchestration | 三链平衡编排（元Skill） | P1 | [有效] | 2026-08-09 新增；跨Skill质量保障层，诊断逻辑链/知识链/创意链偏科并调用对应Skill补强 |
| S-040 | general-suite/human-ai-collaboration | 人机共生能力体系（道·认知层） | CX | [有效] | 2026-08-10 新增；四大核心能力（AI思维/整合力/引导力/判断力）+ 知识唤醒 + 进阶路径 + 人机质量分析 |
| S-041 | general-suite/channel-content-strategy | 渠道内容策略（术·应用层） | P1 | [有效] | 2026-08-10 新增；渠道选择决策（双路径）+ 四平台知识库（微信/微博/小红书/抖音）+ 内容执行模板 |
| S-042 | general-suite/structured-report-writing | 结构化报告写作（术·应用层） | P1 | [有效] | 2026-08-10 新增；年终总结/季度汇报/项目复盘/晋升述职，三大模块九维度提示语模板 |

---

### E- 经济决策工具（economic-suite/）

| 编号 | 技能路径 | 技能名 | 阶段 | 状态 | 备注 |
|------|----------|--------|------|------|------|
| E-001 | economic-suite/economic-npv | NPV计算器 | CX | [有效] | — |
| E-002 | economic-suite/economic-irr | IRR计算器 | CX | [有效] | — |
| E-003 | economic-suite/economic-sensitivity | 敏感性分析工具 | CX | [有效] | — |
| E-004 | economic-suite/economic-comparison | 方案比选工具 | CX | [有效] | — |
| E-005 | economic-suite/economic-ve | 价值工程工具 | CX | [有效] | — |
| E-006 | economic-suite/economic-payback | 投资回收期工具 | CX | [有效] | — |
| E-007 | economic-suite/economic-decision | 经济决策元技能 | CX | [有效] | 自动调度E-001~006 |

---

### L- 法律服务（legal-suite/）

| 编号 | 技能路径 | 技能名 | 阶段 | 状态 | 备注 |
|------|----------|--------|------|------|------|
| L-001 | legal-suite/law-skills | 法律咨询与起诉状 | CX | [有效] | — |
| L-002 | legal-suite/contract-review | 合同审查 | CX | [有效] | — |
| L-003 | legal-suite/ip-protection | 知识产权保护 | CX | [有效] | — |
| L-004 | legal-suite/legal-compliance-bundle | 中国法律合规技能包（50子技能） | CX | [有效] | 新部署 |

---

### R- 阅读操作系统（reading-os/）

| 编号 | 技能路径 | 技能名 | 阶段 | 状态 | 备注 |
|------|----------|--------|------|------|------|
| R-001 | reading-os/reading-book-deconstruction | 深度拆书·资产化输出 | CX | [有效] | — |
| R-002 | reading-os/reading-bookshelf-health | 书架体检·注意力雷达 | CX | [有效] | — |
| R-003 | reading-os/reading-role-path | 角色适配·三层阅读路径 | CX | [有效] | — |

---

### X- 专家视角（expert-suite/）

（已分配 S-006, S-007，暂不需 X- 前缀，保留扩展空间）

---

### GX- 高项备考（gaoxiang-suite/）

| 编号 | 技能路径 | 技能名 | 阶段 | 状态 | 备注 |
|------|----------|--------|------|------|------|
| GX-000 | gaoxiang-suite/gx-master-control | 备考总控（学习枢纽） | EX | [建设中] | 学习进度·知识图谱·策略调度·复习节奏；2026-08-06 注册 |

> 编号规划（待按学习进度逐个创建，不建空技能）：
> - GX-001~004：核心能力工具（术语句式库/论文工坊/案例工坊/计算题专项）
> - GX-010~020：知识域技能（按教材章节群组建，交叉引用 pm-suite）
> - GX-030~031：综合题库与错题本/专业英语
> - 详细架构见 `D:\00_Lee\00-04-个人\99_信息系统项目管理师\AI辅助备考\技能体系\技能体系架构.md`

---

## 3. 编号冲突处理记录

以下技能在 SKILLS 体系中有不同编号，合并时**以本表为准**：

| 技能 | SKILLS 编号 | 当前体系编号 | 处理决定 |
|------|-------------|-------------|---------|
| pd-innovation-process | PT-006 | PT-002 | 保留 PT-002 |
| pd-market-research | PT-002 | PT-003 | 保留 PT-003 |
| pd-product-operations | PT-009 | PT-011 | 保留 PT-011 |
| pd-user-research | PT-003 | PT-012 | 保留 PT-012 |
| pd-tools-metrics | PT-014 | PT-013 | 保留 PT-013 |
| pd-team-culture | PT-013 | PT-014 | 保留 PT-014 |
| pd-integration | PT-012 | PT-015 | 保留 PT-015 |
| pm-change-management | JT-010 | JT-006 | 保留 JT-006 |
| pm-procurement-quality | JT-007 | JT-008 | 保留 JT-008 |
| pm-project-delivery | JT-008 | JT-009 | 保留 JT-009 |
| pm-risk-management | JT-006 | JT-010 | 保留 JT-010 |
| pm-quality-assurance | JT-009 | JT-012 | 保留 JT-012 |
| pm-stakeholder-management | JT-016 | JT-015 | 保留 JT-015 |
| 工业互联网产品经理 | PT-016 | PT-017 | 保留 PT-017（文件误写 PT-016，已纠正） |
| pm-tender-analysis | JT-003 | JT-019 | 保留 JT-019（原未登记，文件误写 JT-003，新分配） |

---

## 4. 新编号分配规则

1. **新技能**：取所在套件已用最大编号+1
2. **从 SKILLS 合并过来的独有技能**：分配 S-008 开始的编号
3. **禁止使用已删除技能的编号**（防止混淆）

---

## 5. 查阅说明

- 每次需要查编号时，**先查此文件**，不扫描目录
- 每次分配新编号后，**立即更新此文件**
- 此文件是"唯一事实来源"（Single Source of Truth）
