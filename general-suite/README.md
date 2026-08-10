# general-suite/ 通用技能

> 通用技能套件——跨领域、跨轨道的基础能力层。覆盖AI辅助编程、提示语工程、文档处理、数据分析、绘图制图等通用场景。

## 套件定位

general-suite 是 skills 体系中的**共用基础能力层**，与 pd-suite（产品轨）、pm-suite（项目轨）并列，但服务于更广泛的通用场景。本套件中的技能可被任何轨道的技能调用，也可独立使用。

## 技能全景图

### 已治理技能（有治理编号）

| 编号 | 技能名 | 路径 | 阶段 | 说明 |
|------|--------|------|------|------|
| S-008 | tools-bayesian-update | `tools-bayesian-update/` | CX | 贝叶斯参数更新通用工具 |
| S-009 | tools-monte-carlo | `tools-monte-carlo/` | CX | 蒙特卡洛模拟通用工具 |
| S-010 | meeting-minutes | `meeting-minutes/` | CX | 会议摘要与纪要管理 |
| S-011 | doc-versioner | `doc-versioner/` | P4 | 文档版本化出版工具 |
| S-015 | md-to-pdf-cjk | `md-to-pdf-cjk/` | P4 | Markdown转PDF（CJK支持） |
| S-016 | markitdown-skill | `markitdown-skill/` | P4 | 文档转Markdown |
| S-020 | excel-xlsx | `excel-xlsx/` | CX | Excel/XLSX工作簿处理 |
| S-021 | tech-doc-writer | `tech-doc-writer/` | CX | 技术文档写作助手（含Mermaid图表） |

### 未治理技能（待分配编号）

| 技能名 | 路径 | 说明 |
|--------|------|------|
| academic-thesis-workflow | `academic-thesis-workflow-1.0.1/` | 学术论文生成工作流 |
| ai-dev-workflow | `ai-dev-workflow-1.0.1/` | AI辅助编程三步工作流 |
| auto-dealer-ripcas-marketing | `auto-dealer-ripcas-marketing-1.0.2/` | 汽车经销商营销增长框架 |
| bilingual-buddy | `bilingual-buddy-1.0.1/` | 双语翻译助手 |
| builtin-tools | `builtin-tools-1.0.0/` | 跨平台基础工具集（16个Python脚本） |
| cad-editor | `cad-editor-1.0.6/` | CAD工程制图编辑器（建筑/机械/电气/管道/结构） |
| chat-bus | `chat-bus-1.0.0/` | 共享目录消息总线 |
| find-skills | `find-skills-0.1.0/` | 技能发现与安装 |
| gamebox | `gamebox-1.0.1/` | 多人游戏引擎框架 |
| knowledge-explainer | `knowledge-explainer-1.0.0/` | 知识讲解助手 |
| liurun-writing-assistant | `liurun-writing-assistant-1.0.0/` | 刘润风格商业写作助手 |
| polymarket-trade | `polymarket-trade-1.0.6/` | Polymarket预测市场查询 |
| style-design-generator | `style-design-generator-1.0.0/` | 风格设计生成引擎 |
| thesis-topic-selector | `thesis-topic-selector-1.0.1/` | 论文选题生成器 |
| wealth-manager | `wealth-manager-1.0.2/` | 财富管理四阶段系统 |

### AI辅助编程基础技能（2026-08-09 新增）

基于清华大学《DeepSeek：从入门到精通》提炼的基础技能：

| 技能名 | 路径 | 说明 | 建议编号 |
|--------|------|------|---------|
| prompt-engineering-basics | `prompt-engineering-basics/` | 提示语工程基础——AI咨询师原则、DNA元素模型、五类需求识别（含填空模板）、咨询师工作流、TASTE/ALIGN | S-026 |
| prompt-chain-design | `prompt-chain-design/` | 提示语链设计——CIRS模型、SPECTRA任务分解（含七步技巧+实战案例）、七大机制（反向诊断+诊断式引导）、三链融合（含8维度评估+PM案例）、AIDA框架（含考虑因素+执行技巧） | S-027 |
| creative-prompt-techniques | `creative-prompt-techniques/` | 创意提示语技术——九大框架（含KTT知识转移+RCM随机组合）、语言风格三件套（RSM+EIS+RTA）、元叙事框架、PM产品创新场景映射 | S-028 |
| reasoning-model-strategy | `reasoning-model-strategy/` | 推理模型策略——模型选择、提示语差异、可控性原则、认知外化 | S-029 |
| ai-content-quality | `ai-content-quality/` | AI内容质量管控——幻觉五类七特、五类×七特映射、三重概率交互、PIA/TFM/DES（含理论基础+整合案例） | S-030 |
| ai-collaboration-mindset | `ai-collaboration-mindset/` | AI协作思维——四大核心能力、知识唤醒、三层次突破路径 | S-031 |
| chart-diagram-generator | `chart-diagram-generator/` | 图表绘制元技能——SVG/Mermaid/React三引擎选择与生成 | S-032 |

### 文案营销与品牌战略技能（2026-08-09 新增）

面向产品经理/营销人员的实战技能体系，遵循"诊断→选路→执行"模式：

| 技能名 | 路径 | 说明 | 建议编号 |
|--------|------|------|---------|
| copywriting | `copywriting/` | 文案写作——三要素模型、诊断式模板选择、六大文案模板、语言风格三件套调用 | S-034 |
| marketing-planning | `marketing-planning/` | 营销策划——三大模块（创意概念/传播策略/执行方案）、渠道矩阵、传播节奏、效果评估 | S-035 |
| brand-positioning | `brand-positioning/` | 品牌定位——四大关键考量、战略层级分层、8组件模板、常见陷阱 | S-036 |
| value-proposition | `value-proposition/` | 价值主张——四大关键考量、战略层级分层、10组件价值主张画布 | S-037 |
| future-vision | `future-vision/` | 未来愿景——四大关键考量、战略层级分层、12组件愿景模板 | S-038 |
| three-chain-orchestration | `three-chain-orchestration/` | 三链平衡编排（元Skill）——跨Skill质量保障层，诊断偏科并调用对应Skill补强 | S-039 |

**调用关系**：品牌定位→价值主张→未来愿景（自下而上支撑链）；文案写作/营销策划可向上调用品牌三模块获取战略输入。

### 人机共生与渠道内容技能（2026-08-10 新增）

基于AI辅助编程与内容创作培训材料提炼，构建"道-法-术"三层架构中的应用层与认知层：

| 编号 | 技能名 | 路径 | 层级 | 说明 |
|------|--------|------|------|------|
| S-040 | human-ai-collaboration | `human-ai-collaboration/` | 道·认知层 | 人机共生能力体系——四大核心能力（AI思维/整合力/引导力/判断力）+ AI进阶路径 + 知识唤醒实践 + 人机质量把控 |
| S-041 | channel-content-strategy | `channel-content-strategy/` | 术·应用层 | 渠道内容策略——渠道选择双路径（已知定位直选/模糊定位测试收敛）+ 四平台知识库（微信/微博/小红书/抖音）+ 内容执行模板 |
| S-042 | structured-report-writing | `structured-report-writing/` | 术·应用层 | 结构化报告写作——年终总结/季度汇报/项目复盘/晋升述职，三大模块九维度提示语模板 |

**调用关系**：human-ai-collaboration 为认知底座，所有 Skill 均可调用；channel-content-strategy 向上调用 brand-positioning/value-proposition 获取战略输入，横向调用 copywriting/creative-prompt-techniques 执行内容创作。

### 已有Skill补强（2026-08-10）

| 技能名 | 版本变化 | 补强内容 |
|--------|---------|---------|
| prompt-engineering-basics | v1.1→v1.2 | +TASTE框架（输出控制）+ ALIGN框架（难度与创新性控制）+ 框架对比选型 |
| prompt-chain-design | v1.4→v1.5 | +提示词工程六步法（完整提示生命周期闭环），与SPECTRA互补 |
| ai-content-quality | v1.2→v1.3 | +三重概率模型增强（三维交互空间）+ 人机共生质量影响因素分析（人65%主导） |

## 路由与编排

### 链式工作流

general-suite 的链式工作流索引见 `general-workflow-chains/SKILL.md`，定义了AI辅助编程场景下的技能调用顺序和衔接关系。

### 与其他套件的协作

| 协作方向 | 说明 |
|---------|------|
| → pd-suite | 提示语工程技能可支撑 `pd-ai-research-workflow` 的AI研究编排 |
| → pm-suite | 提示语链设计可支撑 `pm-bid-proposal` 的方案撰写流程 |
| ← meta-suite | `skill-creator-optimized` 和 `skill-refactor` 可治理本套件技能 |
| ← tech-doc-writer | 技术文档写作可调用 `chart-diagram-generator` 生成图表 |
| ← cad-editor | 工程制图与 `chart-diagram-generator` 形成互补（工程图 vs 信息图） |

## 领域负载物参考库

`references/` 目录存放 UTOS 附属的领域负载物参考库，不独立调用，由 UTOS 消费：

| 参考库 | 领域 | 说明 |
|--------|------|------|
| `singlefile-output-reference-1.0.0/` | 单文件产出 | 7域52种产出类型清单+范本 |
| `smart-hardware-reference-1.0.0/` | 智能硬件 | 9域68种开发任务清单+范本 |
| `ultimate-domain-payload-1.0.0/` | 全域 | 人类活动全域终极领域负载物 |
| `web-novel-writing-reference-1.0.1/` | 网络小说 | 8域62种创作任务清单+范本 |

---

**更新日期**：2026-08-10
