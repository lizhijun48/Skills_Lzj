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

## 治理文件

| 文件 | 用途 |
|------|------|
| `SKILL-ID-REGISTRY.md` | 编号注册表（唯一事实来源） |
| `SKILL-CATALOG.md` | 技能全量目录 |
| `GOV_SkillGovernance.md` | 治理规则 |

---

## 版本变更记录

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
