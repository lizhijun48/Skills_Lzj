# Agent 参考库索引

> **定位**：215 个 Agent Prompt + 50 个 Agent 架构教程的快速检索入口
> **使用方法**：按场景定位 → 找到对应 Agent/教程 → 读取源文件
> **更新日期**：2026-06-29

---

## 一、场景速查

### 1.1 产品与项目管理

| 场景 | Agent 推荐 | 文件路径 |
|------|-----------|---------|
| 产品全生命周期管理 | 产品经理 | `agency-agents-zh/product/product-manager.md` |
| Sprint 排序/优先级 | Sprint 排序师 | `agency-agents-zh/product/product-sprint-prioritizer.md` |
| 用户反馈分析 | 反馈分析师 | `agency-agents-zh/product/product-feedback-synthesizer.md` |
| 趋势研究/技术前瞻 | 趋势研究员 | `agency-agents-zh/product/product-trend-researcher.md` |
| 用户行为设计 | 行为助推引擎 | `agency-agents-zh/product/product-behavioral-nudge-engine.md` |
| 高级项目管理 | 高级项目经理 | `agency-agents-zh/project-management/project-manager-senior.md` |
| 跨部门项目协调 | 项目牧羊人 | `agency-agents-zh/project-management/project-management-project-shepherd.md` |
| 实验设计与追踪 | 实验追踪员 | `agency-agents-zh/project-management/project-management-experiment-tracker.md` |
| Jira 工作流 | Jira工作流管家 | `agency-agents-zh/project-management/project-management-jira-workflow-steward.md` |

**对应 SKILL**：PT-001~PT-018 (PD-Suite), JT-001~JT-018 (PM-Suite)
**Agent 教程参考**：`genai-agents-tutorials/.../project_manager_assistant_agent.ipynb` (#13, 任务分解+排期+风险评估+自反思)

### 1.2 招投标与销售

| 场景 | Agent 推荐 | 文件路径 |
|------|-----------|---------|
| 投标策略/方案 | 投标策略师 | `agency-agents-zh/sales/sales-proposal-strategist.md` |
| 赢单策略(MEDDPICC) | 赢单策略师 | `agency-agents-zh/sales/sales-deal-strategist.md` |
| 售前技术 Demo/POC | 售前工程师 | `agency-agents-zh/sales/sales-engineer.md` |
| Discovery 技巧 | Discovery 教练 | `agency-agents-zh/sales/sales-discovery-coach.md` |
| 销售教练/通话辅导 | 销售教练 | `agency-agents-zh/sales/sales-coach.md` |
| Pipeline 分析 | Pipeline 分析师 | `agency-agents-zh/sales/sales-pipeline-analyst.md` |
| Outbound 触达 | Outbound 策略师 | `agency-agents-zh/sales/sales-outbound-strategist.md` |
| 客户拓展(Land&Expand) | 客户拓展策略师 | `agency-agents-zh/sales/sales-account-strategist.md` |
| 政务数字化售前 | 政务数字化售前顾问 | `agency-agents-zh/specialized/government-digital-presales-consultant.md` |

**对应 SKILL**：JT-002 (pm-bid-proposal), pm-tender-analysis
**Agent 教程参考**：`genai-agents-tutorials/.../contextual_quoting_agentic_system.ipynb` (#50, 多agent报价+RAG)

### 1.3 营销与增长

| 场景 | Agent 推荐 | 文件路径 |
|------|-----------|---------|
| **国内平台** | | |
| 小红书运营 | 小红书运营专家 | `agency-agents-zh/marketing/marketing-xiaohongshu-operator.md` |
| 抖音短视频 | 抖音策略师 | `agency-agents-zh/marketing/marketing-douyin-strategist.md` |
| 微信公众号/社群 | 微信公众号运营 | `agency-agents-zh/marketing/marketing-wechat-operator.md` |
| B站内容 | B站内容策略师 | `agency-agents-zh/marketing/marketing-bilibili-strategist.md` |
| 快手 | 快手策略师 | `agency-agents-zh/marketing/marketing-kuaishou-strategist.md` |
| 电商运营(淘/拼/京) | 中国电商运营专家 | `agency-agents-zh/marketing/marketing-china-ecommerce-operator.md` |
| 百度 SEO | 百度 SEO 专家 | `agency-agents-zh/marketing/marketing-baidu-seo-specialist.md` |
| 私域流量 | 私域流量运营师 | `agency-agents-zh/marketing/marketing-private-domain-operator.md` |
| 直播电商 | 直播电商主播教练 | `agency-agents-zh/marketing/marketing-livestream-commerce-coach.md` |
| 跨境电商 | 跨境电商运营专家 | `agency-agents-zh/marketing/marketing-cross-border-ecommerce.md` |
| 知识付费 | 知识付费产品策划师 | `agency-agents-zh/marketing/marketing-knowledge-commerce-strategist.md` |
| **出海营销** | | |
| TikTok | TikTok 策略师 | `agency-agents-zh/marketing/marketing-tiktok-strategist.md` |
| Instagram | Instagram 策展师 | `agency-agents-zh/marketing/marketing-instagram-curator.md` |
| LinkedIn | LinkedIn 内容创作专家 | `agency-agents-zh/marketing/marketing-linkedin-content-creator.md` |
| Twitter/X | Twitter 互动官 | `agency-agents-zh/marketing/marketing-twitter-engager.md` |
| Reddit | Reddit 社区运营 | `agency-agents-zh/marketing/marketing-reddit-community-builder.md` |
| **通用** | | |
| 增长黑客 | 增长黑客 | `agency-agents-zh/marketing/marketing-growth-hacker.md` |
| 内容创作(多平台) | 内容创作者 | `agency-agents-zh/marketing/marketing-content-creator.md` |
| SEO(通用) | SEO专家 | `agency-agents-zh/marketing/marketing-seo-specialist.md` |
| 社交媒体策略 | 社交媒体策略师 | `agency-agents-zh/marketing/marketing-social-media-strategist.md` |
| AI搜索优化 | 智能搜索优化师 | `agency-agents-zh/marketing/marketing-agentic-search-optimizer.md` |
| AI推荐优化(AEO) | AI 引文策略师 | `agency-agents-zh/marketing/marketing-ai-citation-strategist.md` |

**付费媒体**：PPC竞价(`paid-media-ppc-strategist.md`)、程序化采买(`paid-media-programmatic-buyer.md`)、广告创意(`paid-media-creative-strategist.md`)、追踪归因(`paid-media-tracking-specialist.md`) 等 7 个，位于 `agency-agents-zh/paid-media/`

### 1.4 工程与开发

| 场景 | Agent 推荐 | 文件路径 |
|------|-----------|---------|
| 前端开发(React/Vue) | 前端开发者 | `agency-agents-zh/engineering/engineering-frontend-developer.md` |
| 后端架构设计 | 后端架构师 | `agency-agents-zh/engineering/engineering-backend-architect.md` |
| 软件架构/系统设计 | 软件架构师 | `agency-agents-zh/engineering/engineering-software-architect.md` |
| 移动应用开发 | 移动应用开发者 | `agency-agents-zh/engineering/engineering-mobile-app-builder.md` |
| AI/ML 工程 | AI 工程师 | `agency-agents-zh/engineering/engineering-ai-engineer.md` |
| DevOps/CI-CD | DevOps 自动化师 | `agency-agents-zh/engineering/engineering-devops-automator.md` |
| 安全工程 | 安全工程师 | `agency-agents-zh/engineering/engineering-security-engineer.md` |
| 数据工程/管线 | 数据工程师 | `agency-agents-zh/engineering/engineering-data-engineer.md` |
| 数据库优化 | 数据库优化师 | `agency-agents-zh/engineering/engineering-database-optimizer.md` |
| 代码审查 | 代码审查员 | `agency-agents-zh/engineering/engineering-code-reviewer.md` |
| Git 工作流 | Git 工作流大师 | `agency-agents-zh/engineering/engineering-git-workflow-master.md` |
| SRE/运维 | SRE | `agency-agents-zh/engineering/engineering-sre.md` |
| 快速原型/MVP | 快速原型师 | `agency-agents-zh/engineering/engineering-rapid-prototyper.md` |
| **中国平台集成** | | |
| 微信小程序 | 微信小程序开发者 | `agency-agents-zh/engineering/engineering-wechat-mini-program-developer.md` |
| 飞书集成 | 飞书集成开发工程师 | `agency-agents-zh/engineering/engineering-feishu-integration-developer.md` |
| 钉钉集成 | 钉钉集成开发工程师 | `agency-agents-zh/engineering/engineering-dingtalk-integration-developer.md` |
| **硬件/嵌入式** | | |
| 嵌入式固件 | 嵌入式固件工程师 | `agency-agents-zh/engineering/engineering-embedded-firmware-engineer.md` |
| 嵌入式Linux驱动 | 嵌入式 Linux 驱动工程师 | `agency-agents-zh/engineering/engineering-embedded-linux-driver-engineer.md` |
| FPGA/ASIC | FPGA/ASIC 数字设计工程师 | `agency-agents-zh/engineering/engineering-fpga-digital-design-engineer.md` |
| IoT 方案 | IoT 方案架构师 | `agency-agents-zh/engineering/engineering-iot-solution-architect.md` |
| 上位机(Qt/QML) | 上位机工程师 | `agency-agents-zh/engineering/engineering-pc-host-engineer.md` |
| 机械设计 | 机械设计工程师 | `agency-agents-zh/engineering/engineering-mechanical-design-engineer.md` |

### 1.5 设计与 UX

| 场景 | Agent 推荐 | 文件路径 |
|------|-----------|---------|
| UI 界面设计 | UI 设计师 | `agency-agents-zh/design/design-ui-designer.md` |
| UX 研究/可用性测试 | UX 研究员 | `agency-agents-zh/design/design-ux-researcher.md` |
| UX 架构/CSS体系 | UX 架构师 | `agency-agents-zh/design/design-ux-architect.md` |
| 品牌策略 | 品牌守护者 | `agency-agents-zh/design/design-brand-guardian.md` |
| AI图像提示词 | 图像提示词工程师 | `agency-agents-zh/design/design-image-prompt-engineer.md` |
| 视觉叙事 | 视觉叙事师 | `agency-agents-zh/design/design-visual-storyteller.md` |

### 1.6 财务与法务

| 场景 | Agent 推荐 | 文件路径 |
|------|-----------|---------|
| 记账/月结/对账 | 簿记与财务总监 | `agency-agents-zh/finance/finance-bookkeeper-controller.md` |
| 财务建模/估值 | 财务分析师 | `agency-agents-zh/finance/finance-financial-analyst.md` |
| 财务预测/场景建模 | 财务预测分析师 | `agency-agents-zh/finance/finance-financial-forecaster.md` |
| 预算/滚动预测 | FP&A 分析师 | `agency-agents-zh/finance/finance-fpa-analyst.md` |
| 投资研究/尽调 | 投资研究员 | `agency-agents-zh/finance/finance-investment-researcher.md` |
| 发票管理(增值税/金税) | 发票管理专家 | `agency-agents-zh/finance/finance-invoice-manager.md` |
| 税务筹划 | 税务策略师 | `agency-agents-zh/finance/finance-tax-strategist.md` |
| 欺诈检测/风控 | 金融风控分析师 | `agency-agents-zh/finance/finance-fraud-detector.md` |
| 合同审查(民法典) | 合同审查专家 | `agency-agents-zh/legal/legal-contract-reviewer.md` |
| 制度文件(个保法) | 制度文件撰写专家 | `agency-agents-zh/legal/legal-policy-writer.md` |

**对应 SKILL**：L-001~L-004 (Legal-Suite), E-001~E-007 (Economic-Suite), S-019 (gridman)

### 1.7 供应链与运营

| 场景 | Agent 推荐 | 文件路径 |
|------|-----------|---------|
| 需求预测/安全库存 | 库存预测专家 | `agency-agents-zh/supply-chain/supply-chain-inventory-forecaster.md` |
| 供应商评估/验厂 | 供应商评估专家 | `agency-agents-zh/supply-chain/supply-chain-vendor-evaluator.md` |
| 物流路线/成本优化 | 物流路线优化师 | `agency-agents-zh/supply-chain/supply-chain-route-optimizer.md` |
| 采购策略/供应商开发 | 供应链采购策略师 | `agency-agents-zh/supply-chain/supply-chain-strategist.md` |

### 1.8 测试与质量

| 场景 | Agent 推荐 | 文件路径 |
|------|-----------|---------|
| API 测试 | API 测试员 | `agency-agents-zh/testing/testing-api-tester.md` |
| 性能基准/容量 | 性能基准师 | `agency-agents-zh/testing/testing-performance-benchmarker.md` |
| 无障碍审核(WCAG) | 无障碍审核员 | `agency-agents-zh/testing/testing-accessibility-auditor.md` |
| 嵌入式测试(HIL/OTA) | 嵌入式测试工程师 | `agency-agents-zh/testing/testing-embedded-qa-engineer.md` |
| 测试结果分析 | 测试结果分析师 | `agency-agents-zh/testing/testing-test-results-analyzer.md` |
| 工具评测选型 | 工具评估师 | `agency-agents-zh/testing/testing-tool-evaluator.md` |

### 1.9 专项工具

| 场景 | Agent 推荐 | 文件路径 |
|------|-----------|---------|
| MCP 服务器开发 | MCP 构建器 | `agency-agents-zh/specialized/specialized-mcp-builder.md` |
| 工作流设计 | 工作流架构师 | `agency-agents-zh/specialized/specialized-workflow-architect.md` |
| 提示词设计 | 提示词工程师 | `agency-agents-zh/specialized/prompt-engineer.md` |
| 文档生成(PDF/PPTX) | 文档生成器 | `agency-agents-zh/specialized/specialized-document-generator.md` |
| 合规审计(SOC2/ISO) | 合规审计师 | `agency-agents-zh/specialized/compliance-auditor.md` |
| 企业风险评估 | 企业风险评估师 | `agency-agents-zh/specialized/specialized-risk-assessor.md` |
| 企业培训课程设计 | 企业培训课程设计师 | `agency-agents-zh/specialized/corporate-training-designer.md` |
| 会议效率 | 会议效率专家 | `agency-agents-zh/specialized/specialized-meeting-assistant.md` |
| 动态定价 | 动态定价策略师 | `agency-agents-zh/specialized/specialized-pricing-optimizer.md` |
| 技术翻译(中英) | 技术翻译专家 | `agency-agents-zh/specialized/technical-translator-agent.md` |
| 智能体编排 | 智能体编排者 | `agency-agents-zh/specialized/agents-orchestrator.md` |
| 自动化治理(n8n) | 自动化治理架构师 | `agency-agents-zh/specialized/automation-governance-architect.md` |

---

## 二、GenAI Agent 教程索引（50 个 Notebook）

> 位于 `genai-agents-tutorials/GenAI_Agents-main/all_agents_tutorials/`
> 主要框架：LangGraph，部分使用 CrewAI / AutoGen / PydanticAI

### 2.1 按架构模式分类

| 模式 | Tutorial | 核心技术 | SKILL 转换价值 |
|------|----------|---------|---------------|
| **状态图基础** | langgraph-tutorial | StateGraph/节点/边/编译 | 所有 LangGraph agent 的起点 |
| **条件路由** | project_manager_assistant_agent | 自反思循环+条件路由 | 任务分解→排期→风险评估，对应招投标 PM |
| **多 Agent 协作** | multi_agent_collaboration_system | 多agent分工+状态传递 | SKILL 组合/委托模式 |
| **RAG 检索** | contextual_quoting_agentic_system | SQLite+ChromaDB+Pydantic | 多agent报价系统，对应投标报价 |
| **MCP 工具桥** | mcp-tutorial | FastMCP/@tool装饰器 | SKILL 暴露为可调用工具的技术路径 |
| **记忆系统** | memory-agent-tutorial | 语义/情景/程序三类记忆 | Agent 记住历史交互 |
| **自我改进** | self_improving_agent | 反思+学习循环 | SKILL 质量持续改进 |
| **对话 Agent** | simple_conversational_agent | ChatMessageHistory | 基础对话模式 |
| **工具调用** | simple_data_analysis_agent | 工具定义+调用 | 数据分析工具封装 |
| **合同分析** | ClauseAI | 条款分析+合规检查 | 对应招投标合同审查 |
| **内容智能** | ContentIntelligence | 多agent内容生产 | 内容自动化流水线 |
| **代码自愈** | self_healing_code | 自动修复+测试 | 代码质量自动维护 |
| **团队协作** | research_team_autogen | AutoGen多agent | 研究团队分工模式 |

### 2.2 按业务场景分类

| 场景 | Tutorial | 适用性 |
|------|----------|--------|
| **项目管理/招投标** | project_manager_assistant_agent | 直接对应：任务分解→依赖→排期→风险→自反思 |
| **报价系统** | contextual_quoting_agentic_system | 多agent报价+RAG+结构化数据 |
| **合同审查** | ClauseAI | 条款分析+合规检查 |
| **客户支持** | customer_support_agent_langgraph | 客服自动化 |
| **销售分析** | sales_call_analyzer_agent | 销售通话分析 |
| **数据分析** | simple_data_analysis_agent / ainsight_langgraph | 数据洞察 |
| **内容生产** | ContentIntelligence / blog_writer_swarm | 多agent内容流水线 |
| **学术研究** | scientific_paper_agent / systematic_review | 论文分析 |
| **HR 助手** | HR_AI-Assistant / Hr_AI_Agent | 人力资源 |

---

## 三、与现有 SKILL 体系的对应关系

| SKILL 领域 | 对应 Agent 集群 | 补充价值 |
|-----------|----------------|---------|
| PD-Suite (18) | 产品部(5) | Agent 更偏执行层（Sprint排序、反馈分析），SKILL 偏战略层 |
| PM-Suite (18) | 项目管理部(6) + 销售部(8) | 投标策略、赢单策略、Jira工作流等实操 |
| Legal-Suite (4) | 法务部(2) + 专项法律(3) | 中国民法典合同审查、个保法制度文件 |
| Economic-Suite (7) | 金融部(8) | 簿记、FP&A、投资研究、发票管理等实操 |
| 无对应 | 工程部(35) + 设计部(8) + 营销部(36) | 填补技术实现、UI/UX、营销渠道执行的空白 |
| 无对应 | 供应链(4) + 测试(9) + 空间计算(6) | 填补供应链、技术测试、AR/VR的空白 |
| 治理工具(S-022~024) | 专项部(MCP构建器/工作流架构师/提示词工程师) | SKILL→Agent 转换的技术参考 |

---

## 四、统计

| 类别 | 数量 |
|------|------|
| Agent Prompt 总数 | 215 |
| 中国市场原创 | 50 (23.3%) |
| 英文翻译 | 165 (76.7%) |
| 部门分类 | 17 |
| GenAI 教程 Notebook | 50 |
| 主要框架 | LangGraph / CrewAI / AutoGen / PydanticAI |

---

*此索引为 Agent 参考库的引导层。读取具体 Agent 时，按文件路径加载对应的 .md 文件。*
*GenAI 教程的 Notebook 按架构模式或业务场景查阅，详见第二章。*
