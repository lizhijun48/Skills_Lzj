---
name: general-workflow-chains
version: 1.1.0
description: 通用技能链式工作流索引——定义AI辅助编程与内容创作场景下的技能调用顺序、前置条件、输入输出和衔接标志。覆盖3条标准链路（学习链/实战链/质量链）+2条专项链路（图表链/数据链），连接24个通用技能。触发词：AI编程工作流、提示语学习路径、技能串联、下一步学什么、AI协作流程。
governance_id: "S-033"

triggers:
  - AI编程工作流
  - 提示语学习路径
  - 技能串联
  - 下一步学什么
  - AI协作流程
---

# general-workflow-chains · 通用技能链式工作流索引

> **核心定位**：回答"AI辅助编程的技能怎么串起来"——定义AI辅助编程场景下的技能调用顺序、衔接标志和协作路由。
> **对标**：pd-workflow-chains (PT-016) + pm-workflow-chains (JT-018) 的通用技能版本

---

## 技能全景图（24个）

### AI辅助编程基础技能（7个）

| 编号 | 技能 | 核心能力 | 阶段 |
|------|------|---------|------|
| S-026 | prompt-engineering-basics | 提示语DNA、六大类型、五类需求识别（含填空模板）、咨询师工作流、TASTE/ALIGN | 基础 |
| S-027 | prompt-chain-design | CIRS模型、SPECTRA分解（含七步技巧+实战案例）、七大机制（反向诊断+诊断式引导）、三链融合 | 进阶 |
| S-028 | creative-prompt-techniques | 七大创意框架、PM产品创新场景映射、认知理论基础参考 | 进阶 |
| S-029 | reasoning-model-strategy | 模型选择、提示语差异、可控性原则、多模型协同（三种模式）、专用/通用AI决策框架 | 基础 |
| S-030 | ai-content-quality | 幻觉五类七特、五类×七特映射、三重概率交互、PIA/TFM/DES | 进阶 |
| S-031 | ai-collaboration-mindset | 四大核心能力、知识唤醒、三层次突破 | 思维 |
| S-032 | chart-diagram-generator | SVG/Mermaid/React三引擎图表生成 | 应用 |

### 现有通用技能（8个，可被链路调用）

| 编号 | 技能 | 在链路中的角色 |
|------|------|--------------|
| S-021 | tech-doc-writer | 技术文档输出（含Mermaid图表） |
| S-011 | doc-versioner | 文档版本化输出 |
| S-015 | md-to-pdf-cjk | Markdown转PDF |
| S-020 | excel-xlsx | 数据处理与表格 |
| S-008 | tools-bayesian-update | 定量分析工具 |
| S-009 | tools-monte-carlo | 风险分析工具 |
| S-010 | meeting-minutes | 会议记录与行动项 |
| — | cad-editor | 工程制图（与chart-diagram-generator互补） |

### 文案营销与品牌战略技能（6个，2026-08-09 新增）

| 编号 | 技能 | 核心能力 | 在链路中的角色 |
|------|------|---------|--------------|
| S-034 | copywriting | 文案三要素、诊断式模板、六大文案模板、语言风格三件套 | 内容输出 |
| S-035 | marketing-planning | 三大模块（创意/传播/执行）、渠道矩阵、效果评估 | 营销策划 |
| S-036 | brand-positioning | 四大考量、战略层级分层、8组件模板 | 战略输入 |
| S-037 | value-proposition | 战略层级、10组件价值主张画布 | 战略输入 |
| S-038 | future-vision | 战略层级、12组件愿景模板 | 战略输入 |
| S-039 | three-chain-orchestration | 跨Skill质量保障，诊断逻辑链/知识链/创意链偏科 | 质量元Skill |

### 人机共生与渠道内容技能（3个，2026-08-10 新增）

| 编号 | 技能 | 核心能力 | 在链路中的角色 |
|------|------|---------|--------------|
| S-040 | human-ai-collaboration | 四力能力模型、知识唤醒三重机制、进阶路径、人机质量分析 | 认知底座（道层） |
| S-041 | channel-content-strategy | 渠道选择双路径、四平台知识库、内容执行模板 | 渠道适配 |
| S-042 | structured-report-writing | 三大模块九维度提示语模板、语言风格接口 | 报告输出 |

---

## 3条标准链路

### 链路1：学习链（从入门到精通）

```
reasoning-model-strategy ──→ prompt-engineering-basics ──→ prompt-chain-design ──→ ai-content-quality ──→ ai-collaboration-mindset
     [理解模型差异]              [掌握提示语基础]              [学会链式设计]              [建立质量意识]              [形成协作思维]
```

| 环节 | 技能 | 关键输出 | 衔接标志 |
|------|------|---------|---------|
| 1 | reasoning-model-strategy | 理解推理vs通用模型差异，掌握选择决策树 | **能判断任务该用什么模型** |
| 2 | prompt-engineering-basics | 掌握提示语DNA、六大类型、TASTE/ALIGN框架 | **能写出结构完整的提示语** |
| 3 | prompt-chain-design | 掌握CIRS、SPECTRA、任务分解七步骤 | **能拆解复杂任务为提示语链** |
| 4 | ai-content-quality | 掌握幻觉识别、三重概率交互、质量检查清单 | **能评估和验证AI输出质量** |
| 5 | ai-collaboration-mindset | 建立四大核心能力认知，掌握知识唤醒方法 | **形成系统化人机协作思维** |

**前置条件**：无（入门级链路）

**适用场景**：
- 初次系统学习AI辅助编程
- 需要建立完整的提示语工程知识体系
- 从"会用AI"到"用好AI"的进阶

---

### 链路2：实战链（从知识到应用）

```
prompt-engineering-basics ──→ creative-prompt-techniques ──→ chart-diagram-generator ──→ tech-doc-writer
     [提示语基础]                [创意激发技术]                [图表生成]                  [文档输出]
```

| 环节 | 技能 | 关键输出 | 衔接标志 |
|------|------|---------|---------|
| 1 | prompt-engineering-basics | 结构化提示语设计能力 | **能设计清晰的提示语** |
| 2 | creative-prompt-techniques | 运用七大框架激发创意 | **能用AI进行创新方案设计** |
| 3 | chart-diagram-generator | 选择合适引擎生成图表 | **能根据任务选择SVG/Mermaid/React** |
| 4 | tech-doc-writer | 生成含图表的技术文档 | **能产出完整的技术文档** |

**前置条件**：
- 已掌握 prompt-engineering-basics 基础
- 有具体的文档/图表输出需求

**适用场景**：
- 需要生成技术文档、方案报告
- 需要将创意转化为可视化成果
- 招投标技术方案、产品设计文档等

---

### 链路3：质量链（从输出到可控）

```
ai-content-quality ──→ reasoning-model-strategy ─→ prompt-chain-design
     [质量评估]              [模型选择优化]              [提示语链优化]
         ↻_____________________________________________↺
                    [迭代优化循环]
```

| 环节 | 技能 | 关键输出 | 衔接标志 |
|------|------|---------|---------|
| 1 | ai-content-quality | 识别输出质量问题（幻觉/偏见/不准确） | **能诊断AI输出的问题类型** |
| 2 | reasoning-model-strategy | 根据问题类型调整模型选择和提示语策略 | **能针对性优化模型和策略** |
| 3 | prompt-chain-design | 重构提示语链，加入验证节点 | **能设计可控的提示语链** |

**前置条件**：
- 已有AI使用经验
- 遇到输出质量不稳定的问题

**适用场景**：
- AI输出质量不稳定，需要系统性提升
- 需要建立可控的AI工作流程
- 从"碰运气"到"可预测"的转变

---

## 2条专项链路

### 链路4：图表链（信息可视化专项）

```
chart-diagram-generator ──→ tech-doc-writer ──→ md-to-pdf-cjk / doc-versioner
     [图表生成]                [文档整合]              [格式输出]
```

| 环节 | 技能 | 关键输出 | 衔接标志 |
|------|------|---------|---------|
| 1 | chart-diagram-generator | 根据需求选择引擎生成图表 | **图表已生成并验证** |
| 2 | tech-doc-writer | 将图表嵌入技术文档 | **文档已完成** |
| 3 | md-to-pdf-cjk 或 doc-versioner | 输出PDF或版本化文档 | **最终交付物已生成** |

**分支可能**：
- 需要工程图纸 → 调用 `cad-editor`（建筑/机械/电气/管道/结构）
- 需要数据可视化 → 使用 chart-diagram-generator 的 React 图表
- 需要快速流程图 → 使用 chart-diagram-generator 的 Mermaid 图表

---

### 链路5：数据分析链（定量分析专项）

```
prompt-engineering-basics ──→ excel-xlsx ──→ tools-bayesian-update / tools-monte-carlo ──→ chart-diagram-generator
     [提示语设计]              [数据处理]              [定量分析]                  [结果可视化]
```

| 环节 | 技能 | 关键输出 | 衔接标志 |
|------|------|---------|---------|
| 1 | prompt-engineering-basics | 设计数据分析提示语 | **分析目标已明确** |
| 2 | excel-xlsx | 读取/处理/分析数据 | **数据已准备就绪** |
| 3 | tools-bayesian-update 或 tools-monte-carlo | 执行定量分析 | **分析结果已生成** |
| 4 | chart-diagram-generator | 可视化分析结果 | **图表已生成** |

---

## 与PD/PM套件的协作路由

### → pd-suite 协作

```
general-suite 技能                          pd-suite 技能
     │                                           │
     ├── prompt-engineering-basics ──────────→ pd-ai-research-workflow (PT-019)
     │    [提示语基础支撑AI研究编排]                [3-Tier AI研究法]
     │
     ├── creative-prompt-techniques ─────────→ pd-product-strategy (PT-001)
     │    [创意框架支撑产品创新]                    [创新战略4类型]
     │
     └── chart-diagram-generator ───────────→ pd-market-research (PT-003)
          [图表支撑市场研究报告]                    [竞品分析可视化]
```

### → pm-suite 协作

```
general-suite 技能                          pm-suite 技能
     │                                           │
     ├── prompt-chain-design ────────────────→ pm-bid-proposal (JT-002)
     │    [链式设计支撑方案撰写]                    [招投标方案编制]
     │
     ├── ai-content-quality ─────────────────→ pm-quality-assurance (JT-012)
     │    [质量管控支撑质量保证]                    [QA过程改进]
     │
     └── reasoning-model-strategy ──────────→ pm-risk-management (JT-010)
          [模型选择支撑风险分析]                    [风险识别与评估]
```

---

## 快速导航：我该从哪个技能开始？

| 你的情况 | 推荐入口 | 后续路径 |
|---------|---------|---------|
| 完全新手，刚开始学AI | reasoning-model-strategy | → 学习链 |
| 会用AI但提示语写不好 | prompt-engineering-basics | → 学习链 或 实战链 |
| 需要写技术文档/方案 | prompt-engineering-basics | → 实战链 |
| AI输出质量不稳定 | ai-content-quality | → 质量链 |
| 需要画图表/流程图 | chart-diagram-generator | → 图表链 |
| 想系统提升AI协作能力 | ai-collaboration-mindset | → 学习链（补基础） |
| 需要做数据分析 | excel-xlsx | → 数据分析链 |
| **PM：需求模糊/问题定义** | prompt-chain-design（诊断式引导） | 先反问补全信息 → 机制1+3选路执行 |
| **PM：竞品分析/方案编制** | prompt-chain-design（诊断式引导） | 先反问明确维度和标准 → 机制2+5选路执行 |
| **PM：输出不满意/反复修改** | prompt-chain-design（反向诊断） | 定位失效机制 → 机制6反馈整合 |
| **PM：汇报材料/风险方案** | prompt-chain-design（诊断式引导） | 先反问受众和验收标准 → 机制5+7选路执行 |

---

**创建日期**：2026-08-09
**对标**：pd-workflow-chains (PT-016) + pm-workflow-chains (JT-018)
