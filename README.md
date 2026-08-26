# Skills 技能体系

> AI辅助编程与产品经理技能治理仓库。双轨架构（pd-suite产品轨 + pm-suite项目轨）+ general-suite通用层 + meta-suite元技能。

## 仓库结构

| 套件 | 前缀 | 说明 |
|------|------|------|
| pd-suite/ | PT- | 产品轨（Product Track）——产品经理全流程技能 |
| pm-suite/ | JT- | 项目轨（Project Track）——项目管理全流程技能 |
| general-suite/ | S- | 通用层（Shared）——跨领域基础能力 |
| meta-suite/ | S- | 元技能——技能治理与创建工具 |
| economic-suite/ | E- | 经济决策工具 |
| legal-suite/ | L- | 法律服务 |
| reading-os/ | R- | 阅读操作系统 |
| expert-suite/ | S- | 专家视角 |
| gaoxiang-suite/ | GX- | 高项备考 |
| industry-suite/ | I- | 行业技能（代理记账/C2C/代谢慢病/医药/通用业务） |
| research-suite/ | RE- | 研究技能（CDA 因果动力学） |

## 治理文件

| 文件 | 用途 |
|------|------|
| `SKILL-ID-REGISTRY.md` | 编号注册表（唯一事实来源） |
| `SKILL-CATALOG.md` | 技能全量目录 |
| `GOV_SkillGovernance.md` | 治理规则 |

---

## 版本变更记录

### v1.5.0 — 2026-08-26

**剩余40个未治理技能批量纳管：新增 I-/RE- 前缀，治理覆盖率达 100%**

提交：待推送 | 变更：SKILL-ID-REGISTRY.md v1.4.0→v1.5.0（新增 I-/RE- 规则+段）、SKILL-CATALOG.md（40行[未治理]→[有效]）+ 10个技能目录无变动

#### 一、纳管范围

- industry-suite（6）→ I-001~I-006（含 I-005 pharma-doc-reference 参考库）
- research-suite（3）→ RE-001~RE-003
- expert-suite（11）→ X-001~X-011（启用预留 X- 前缀）
- general-suite（19）→ S-051~S-069（含 S-063/064/067/069 四个 references 参考库）
- pm-suite（1）→ PT-010（复用空号登记 pm-skills-reference）

#### 二、治理状态

- 治理前：未治理 40 个
- 治理后：未治理 0 个，已治理 137 个（覆盖率 100%）
- 新增前缀：I-（行业）、RE-（研究）；X- 前缀正式启用

#### 三、关键决策（GOV §2.4 保留判定）

- 40 个技能保留判定全部通过（性质清晰、有独立用途），无折叠/废弃项
- 5 个 references/ 子文件（singlefile/smart-hardware/ultimate-domain/web-novel/pharma-doc-reference）确认为可独立调用技能，归对应套件编号并标注"参考库"

### v0.9.0 — 2026-08-26

**meta-suite 同义簇治理：10技能折叠合并，8新登记**

提交：待推送 | 变更：3 个治理文件更新 + 10 个技能目录删除（已备份）

#### 一、问题诊断

meta-suite 存在 15 个未治理技能，其中 10 个属于"任务执行 OS / 分解编排"同义簇：
- 7 个讲同一件事（universal-task-os / universal-primitives / capability-pipeline-os / ipo-model / cogniexec / compose-methods / workflow-refactor）
- 3 个与已治理工具重叠（workflow-refactor + domain-elimination-assessor ⊆ S-023；domain-payload-generator ⊆ S-024）

直接编号 = 把冗余固化进注册表。

#### 二、折叠合并（10 → 0）

| 源技能 | 目标 | 差异化内容保留位置 |
|--------|------|-------------------|
| universal-primitives | S-043 UTOS | references/universal-primitives.md（2基元哲学+环境自举策略） |
| capability-pipeline-os | S-043 UTOS | references/capability-pipeline-os.md（原已存在） |
| ipo-model | S-043 UTOS | references/ipo-model.md（IPO世界模型+Mode A/B+工具层级） |
| cogniexec | S-043 UTOS | references/cogniexec-orchestration.md + cogniexec-scripts/（17个Python脚本） |
| compose-methods | S-043 UTOS | references/compose-methods.md（原已存在） |
| identity-primitive-chain-prompt | S-043 UTOS | references/identity-primitive-chain-prompt-spec.md（P0消歧+操作钩子） |
| solopreneur-os | S-043 UTOS + S-023 | references/solopreneur-os.md（一人公司场景参考） |
| workflow-refactor | S-023 skill-refactor | references/workflow-refactor-method.md（IPO原语+AI自治标注） |
| domain-elimination-assessor | S-023 skill-refactor | references/domain-elimination-assessor.md（领域特定阈值+DEA模板） |
| domain-payload-generator | S-024 skill-forge | references/ 4文件（R1-R5分类+三层模板+UTOS接口清单+生成工作流） |

#### 三、新登记（8个）

| 编号 | 技能名 | 定位 |
|------|--------|------|
| S-043 | universal-task-os | 通用三轴任务操作系统（基座）——执行轴+内容轴+创新轴 |
| S-044 | innovation-os | 通用创新操作系统——4种AI模式+10创新元框架 |
| S-045 | adaptive-skill-stack | 自适应技能叠加——自积累演化机制 |
| S-046 | self-improving-agent | 持续学习代理——错误/纠正/知识缺口捕获 |
| S-047 | comprehensive-knowledge-system | 综合知识体系——投资+提示词+AI编程三域 |
| S-048 | data-analyst | 通用数据分析引擎——Python基础设施级 |
| S-049 | portfolio-rebalancing | 产品组合再平衡——补 JT-005 |
| S-050 | product-sunset-assessment | 产品退市评估——补 PT-009 |

#### 四、数字核对

- 磁盘 SKILL.md：147 → **137**（-10）
- 已治理：89 → **97**（+8）
- 未治理：58 → **40**（-10折叠-8升基座）
- 注册表：105 条（99 有效 / 4 可用空号 / 2 已释放）。注：99 有效含 reading-os 的 R-001~R-003 三模块编号（目录合并为 1 行，故目录"已治理"记 97）；10 个折叠项从未编号，不进注册表。

#### 五、备份位置

`~/.workbuddy/backup/meta-suite-pre-v0.9/`（完整 meta-suite 快照）

---

### v0.8.0 — 2026-08-26

**技能库体检与 P0/P1 整改：账实同步 + 去重收尾 + 幽灵条目清理**

提交：待推送 | 变更：3 个治理文件更新 + 2 个重复技能目录删除（已备份）

#### 一、台账同步（P0）

| 文件 | 变更 |
|------|------|
| SKILL-CATALOG.md | 补 gaoxiang-suite 章节（GX-000 备考总控 / GX-001 术语句式库）；reading-os 行由"未治理"改为已注册（R-001~003 为模块文件）；总计更新为 147 个（已治理 89 + 未治理 58），与磁盘实测一致 |
| SKILL-ID-REGISTRY.md | v1.2.0→v1.3.0；S-014（wechat-article-parser，磁盘不存在）与 S-017（inbox 已清空）按幽灵条目释放编号；R-001~R-003 路径补 .md 后缀并标注模块口径 |

#### 二、去重收尾（P1）

- 删除 `meta-suite/tools-suite/` 下 tools-bayesian-update、tools-monte-carlo 旧副本（无 governance_id 的迁移前版本）；保留 general-suite 治理版（S-008/S-009）为唯一部署
- 备份位置：`~/.workbuddy/backup/skills-dedup-20260826/`；空目录 tools-suite 已移除

#### 三、数字核对

- 磁盘 SKILL.md：149 → **147**（去重后）
- 已治理：86 → **89**（+gaoxiang 2 + reading-os 1）
- 未治理：61 → **58**
- 注册表：97 条（91 有效 / 4 可用空号 / 2 已释放）

#### 四、剩余事项（转入下轮）

- 58 个未治理技能分批纳管（建议首批：industry 6 + research 3 + expert-fwsjtt 11）
- expert-suite X- 前缀启用决策（fwsjtt 12 个技能归 S- 还是 X-）
- 超大技能文件瘦身（gridman 84KB / pm-bid-proposal 63KB / law-skills 45KB）
- 根目录冗余 insurance-policy-analysis.zip 清理

---

### v0.1.0 — 2026-08-07

**基线版本：初始仓库建立**

首次提交，包含已治理技能 76 个 + 未治理技能若干，共计 1052 个文件。

主要套件状态：
- pd-suite：19个产品轨技能（PT-001~PT-019），覆盖产品战略到产品运营全流程
- pm-suite：20个项目轨技能（JT-001~JT-020），覆盖项目立项到收尾全流程
- meta-suite：5个元技能（S-001~S-005）+ 4个技能治理工具（S-022~S-025）
- general-suite：8个已治理通用技能（S-008~S-021）+ 14个未治理技能
- economic-suite：7个经济决策工具（E-001~E-007）
- legal-suite：4个法律技能（L-001~L-004）
- reading-os：3个阅读技能（R-001~R-003）
- expert-suite：2个专家视角（S-006, S-007）
- gaoxiang-suite：1个备考总控（GX-000）

---

### v0.2.0 — 2026-08-09

**基于清华DeepSeek PDF构建AI辅助编程 + 文案营销 + 品牌战略技能体系**

提交：`175fced` | 变更：17 files changed, 3738 insertions

#### 一、补强已有Skill（3个）

| Skill | 版本变化 | 主要变更 |
|-------|---------|---------|
| **ai-content-quality** | v1.1→v1.2 | PIA补充言语行为理论基础+第5步应用验证；TFM补充图式理论基础；DES补充双重编码/具身认知/对比效应理论基础；新增PIA+TFM+DES气候变化整合案例（四步闭环） |
| **prompt-chain-design** | v1.3→v1.4 | AIDA补充6个考虑因素+4个执行技巧（5W1H/至少3方向/骨架→血肉/三维度检查表）；三链融合补充好处分析（偏科对照表）+PM智能门锁案例+8维度评估框架 |
| **creative-prompt-techniques** | v1.1→v1.2 | 七大→九大框架（+KTT知识转移+RCM随机组合）；新增"语言风格优化三件套"章节（RSM语体模拟+EIS情感融入+RTA修辞技巧+整合模式）；新增"元叙事提示框架"章节（叙事弧线/角色代入/冲突-解决/多声部叙事）；认知理论基础表扩充至12条；PM场景映射表补充KTT/RCM条目 |

#### 二、新增Skill（6个）

| 编号 | Skill | 说明 |
|------|-------|------|
| S-034 | **copywriting**（文案写作） | 文案三要素模型（信息传递/情感共鸣/行动引导）+ 场景-要素配比矩阵 + 诊断式工作流 + 六大文案模板（产品说明/品牌故事/广告语/社交媒体/长文营销/邮件营销）+ 语言风格三件套调用接口 + 质量评估清单 |
| S-035 | **marketing-planning**（营销策划） | 三大模块（创意概念/传播策略/执行方案）+ 诊断式工作流 + 创意评估矩阵 + 渠道选择矩阵（6类渠道）+ 传播节奏设计（预热→引爆→持续→长尾）+ 内容矩阵 + 执行方案模板（时间表/预算/风险）+ 效果评估框架 |
| S-036 | **brand-positioning**（品牌定位） | 战略层级内部分层（企业级→产品线级→单品级）+ 四大关键考量（目标市场/竞争对手/品牌个性/情感连接点）+ 8组件完整模板 + 4个常见陷阱 + 5维评估标准 + 调用关系定义 |
| S-037 | **value-proposition**（价值主张） | 战略层级内部分层 + 四大关键考量（核心优势/解决痛点/情感功能平衡/可信度）+ 10组件价值主张画布 + 功能-情感平衡原则 + 4个常见陷阱 + 5维评估标准 + 调用关系定义 |
| S-038 | **future-vision**（未来愿景） | 战略层级内部分层 + 四大关键考量（一致性/社会影响/参与感/远大与可实现平衡）+ 12组件愿景模板 + 里程碑拆解（近期/中期/远期）+ 4个常见陷阱 + 5维评估标准 + 调用关系定义 |
| S-039 | **three-chain-orchestration**（三链平衡编排） | 元Skill——跨Skill质量保障层；三链诊断模型（9个弱信号扫描）→ 补强调用映射（逻辑链→prompt-chain-design / 知识链→prompt-engineering-basics / 创意链→creative-prompt-techniques）→ 8维度评估验证 → 闭环编排工作流 |

#### 三、治理文件更新

| 文件 | 变更 |
|------|------|
| SKILL-ID-REGISTRY.md | 新增S-034~S-039共6条注册记录 |
| SKILL-CATALOG.md | 未修改（待下次同步） |
| general-suite/README.md | 新增"文案营销与品牌战略技能"分组（6个Skill）+ 更新已有Skill描述 |

#### 四、品牌三模块架构决策

品牌定位/价值主张/未来愿景分别建独立Skill，各自按战略层级（企业级→产品线级→单品级）内部分层，通过"场景诊断→层级匹配→模板执行"选路。三者形成"定位→主张→愿景"自下而上支撑链，文案写作和营销策划Skill向上调用获取战略输入。

---

### v0.7.0 — 2026-08-11

**治理体系优化：执行欠差补齐 + §10原则扩展**

提交：待推送 | 变更：治理体系v3.5 + 4张全局表同步 + 2条新原则 + 层级矛盾修复

#### 一、执行欠差补齐（§8.1 / QG13 要求的全局表同步）

| 全局表 | 修复内容 |
|--------|---------|
| SKILL-ID-REGISTRY.md | 头部版本 v1.1.5→v1.2.0，日期同步到 2026-08-11 |
| BUSINESS-FLOW-MAP.md | 新增 §7 共用层业务流映射（GS-FLOW-001~004：AI辅助编程/内容创作/报告写作/能力体系建设），版本 v1.0.6→v1.1.0 |
| general-workflow-chains (S-033) | 技能全景图从15个扩展到24个，补入S-034~S-042三个分组，更新S-029描述，版本 v1.0.0→v1.1.0 |
| SKILL-CATALOG.md | 全量同步，新增S-034~S-042（9个）+ JT-020，总计从137更新到147 |

#### 二、§10 原则扩展（GOV_SkillGovernance.md v3.4→v3.5）

| 新原则 | 内容 |
|--------|------|
| **原则六：Skill章节规范** | 定义 SKILL.md 必选章节（frontmatter/核心原则/定位与适用场景/使用建议）和可选章节（调用关系/参考来源/质量评估/常见陷阱） |
| **原则七：分层标注** | 在 Track/Phase 体系基础上，general-suite 增加 layer 字段（道/法/术/元），解决认知层与方法层的区分 |

#### 三、矛盾修复

- human-ai-collaboration §7.4 表中 prompt-chain-design 层级从"术层"修正为"法层"，与 §1.1 ASCII图一致

---

### v0.6.0 — 2026-08-11

**推理模型策略增强：多模型协同 + 专用/通用AI决策框架**

提交：待推送 | 变更：补强1个Skill + 新增1个参考文档 + 交叉引用更新

#### 一、补强Skill（1个）

| Skill | 版本变化 | 新增内容 |
|-------|---------|---------|
| **reasoning-model-strategy** | v1.2→v1.3 | +多模型协同工作模式（发散+收敛/创作+分析/教学+学习三种模式）+ 专用AI vs 通用AI决策框架（选择决策树+通用定策略专用精执行+工作流自动化三步法+个人AI工具生态构建） |

#### 二、交叉引用更新

| Skill | 版本变化 | 更新内容 |
|-------|---------|---------|
| **human-ai-collaboration** | v1.0→v1.0.1 | 整合力章节新增S-029交叉引用（多模型协同+专用/通用AI选择）；调用关系表新增reasoning-model-strategy |

#### 三、参考文档

- `reasoning-model-strategy/references/source-material-deepseek.md`（《DeepSeek 使AI变得简单》第2/9章，多模型协同与工具生态原始素材）

#### 四、来源说明

本次增强素材来自《DeepSeek 使AI变得简单》（Yash Jain著，刘彦辰翻译）。全书约70%内容与已有Skills重叠（提示工程基础、故障排除等），提取了第2章"ChatGPT与DeepSeek协同模式"和第9章"专用AI vs 通用AI决策框架"两个增量知识点。

---

### v0.5.0 — 2026-08-10

**渠道内容策略 + 人机共生能力体系 + 结构化报告写作 + 已有Skill补强**

提交：待推送 | 变更：新建3个Skill + 补强3个Skill + 6个参考文档

#### 一、新增Skill（3个）

| 编号 | Skill | 层级 | 说明 |
|------|-------|------|------|
| S-040 | **human-ai-collaboration**（人机共生） | 道·认知层 | 四大核心能力（AI思维/整合力/引导力/判断力）+ AI进阶路径（基础→进阶→创新三层金字塔+四步突破）+ 知识唤醒实践（情感/经验/关联三重唤醒+具身-形式知识桥接）+ 人机协作质量把控（人65% vs 机器35%） |
| S-041 | **channel-content-strategy**（渠道内容策略） | 术·应用层 | 渠道选择双路径（已知定位→直选/模糊定位→测试收敛）+ 四平台知识库（微信深度阅读/微博短平快/小红书种草/抖音短视频）+ 各渠道内容执行模板 + 传播策略与数据反馈闭环 |
| S-042 | **structured-report-writing**（结构化报告写作） | 术·应用层 | 覆盖年终总结/季度汇报/项目复盘/晋升述职；三大模块（业绩回顾/成就展示/未来规划）× 九维度提示语模板 + 语言风格调用接口 |

#### 二、补强已有Skill（3个）

| Skill | 版本变化 | 新增内容 |
|-------|---------|---------|
| **prompt-chain-design** | v1.4→v1.5 | 提示词工程六步法（目标设定→角色激活→任务拆解→深入推理→参考材料→迭代优化），与SPECTRA形成互补（SPECTRA解决"怎么拆"，六步法解决"怎么写和迭代"） |
| **prompt-engineering-basics** | v1.1→v1.2 | TASTE框架（Task/Audience/Structure/Tone/Example，侧重输出控制）+ ALIGN框架（Aim/Level/Input/Guidelines/Novelty，侧重难度与创新性控制）+ 框架对比选型指南 |
| **ai-content-quality** | v1.2→v1.3 | 三重概率模型增强（三维交互空间详解）+ 人机共生质量影响因素分析（人65%主导：输入质量70%人/基础能力80%机器/迭代优化90%人） |

#### 三、参考文档

每个Skill目录下创建 `references/` 子目录，存放原始素材的文本转录，便于追溯内容出处：
- `human-ai-collaboration/references/source-material.md`（11张图，人机共生能力体系全量内容）
- `channel-content-strategy/references/source-material.md`（18张图，四平台内容生产全量内容）
- `structured-report-writing/references/source-material.md`（1张图，年终总结提示语设计）
- `prompt-chain-design/references/source-material-six-step.md`（六步法）
- `prompt-engineering-basics/references/source-material-frameworks.md`（TASTE/ALIGN框架）
- `ai-content-quality/references/source-material-probability.md`（三重概率+人机质量分析）

#### 四、架构决策

- **Skill体系"道-法-术"三层架构确立**：道=认知层（human-ai-collaboration），法=方法层（prompt-engineering等），术=应用层（channel-content等）
- **渠道内容策略采用方案A**：四平台内容模板作为 channel-content-strategy 内部知识库，不拆分为独立Skill
- **平台只是工具，目标才是目的**：Skill解决"怎么选渠道+怎么根据渠道适配内容"，而非"在某个平台怎么写"

---

### v0.4.0 — 2026-08-09

**治理体系统一入口：GOV_ArchitecturePrinciples.md 合并至 GOV_SkillGovernance.md**

#### 变更内容

| 文件 | 变更 |
|------|------|
| `GOV_SkillGovernance.md` | v3.3→v3.4；新增 §10「Skill架构原则（全局）」——合并5条原则（质量检查点/动态路由/CIRS闭环/MECE/WBS优化）+ 后续治理计划；修复重复v3.3条目 |
| `general-suite/GOV_ArchitecturePrinciples.md` | 已删除（内容合并至 GOV_SkillGovernance.md §10） |

#### 架构决策

治理内容统一入口为 `GOV_SkillGovernance.md`，不再拆分为多个治理文件。后续所有架构原则、治理规则均在同一文件中维护。

---

### v0.3.0 — 2026-08-09

**PM场景参考文档 + 架构治理原则统一落地**

#### 一、新增参考文档

| 文件 | 说明 |
|------|------|
| `general-suite/pm-scenarios-reference.md` | PM场景应用参考——汇总各Skill中PM相关的应用场景、调用路径、Skill调用关系全景图、PM必备Skill最小集（5个覆盖80%日常场景）、7个高频场景速查（竞品分析/立项报告/Slogan/需求文档/营销策划/风险应对/质量诊断） |

#### 二、新增治理原则文档

| 文件 | 说明 |
|------|------|
| `general-suite/GOV_ArchitecturePrinciples.md` | Skill架构治理原则（general-suite补充）——定义5条统一落地原则：①质量检查点（workflow-chains衔接标准）②动态路由（条件分支+回环机制）③Skill内部CIRS闭环 ④MECE原则（相互独立+完全穷尽）⑤WBS优化（渐进复杂性+100%规则+可交付物导向）。含各原则在当前Skill中的落地状态表。 |

---

*版本规则：每次 git commit 对应一个版本号，格式 v0.X.0。变更记录按版本号倒序排列。*
