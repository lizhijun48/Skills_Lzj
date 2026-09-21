# 产品经理 Agent「产品通」分析评估报告

> 分析对象：`product-management-expert-source/`（CodeBuddy Teams 出品的 PM 插件）
> 评估日期：2026-09-21
> 评估视角：对照 Alex 现有技能治理体系（GOV_SkillGovernance v3.6，140 技能）的差距与可借鉴点

---

## 一、结构解剖（它是什么）

| 层 | 文件 | 作用 |
|----|------|------|
| 插件清单 | `.codebuddy-plugin/plugin.json` | 声明 7 个 skill + 1 个 agent，expertType=agent |
| 专家入口 | `agents/product-management-expert.md` | 人设「产品通」+ 能力地图 + 工作方式 + 边界 |
| 强制规则 | `rules/product_management_rules.md` | `alwaysApply:true` 的 system_reminder，强制调用插件能力 |
| 总控路由 | `skills/product-management-workflows/SKILL.md` | 6 大能力的端到端 Workflow 编排（英文） |
| 专项技能 | `feature-spec` / `roadmap-management` / `stakeholder-comms` / `user-research-synthesis` / `competitive-analysis` / `metrics-tracking` | 各能力的方法论下沉（中文 README 指引，SKILL 多英文） |
| 说明文档 | `README.md`（中文，详实） | 能力、场景示例、最佳实践、目标用户、免责声明 |

**架构本质**：`Agent 人设层` + `Rules 强制层` + `Workflow 路由层` + `6 专项技能层`，四层分工清晰，是标准的"专家包（Expert Package）"形态。

---

## 二、为什么写得好（好在哪）

| # | 亮点 | 具体证据 | 价值 |
|---|------|---------|------|
| 1 | **人设锚定（IP 化）** | "产品通"+"产品经理不是需求搬运工，是价值判断官"信条（agent 第 8 行） | 比"你是个 PM 助手"强得多，给 AI 行为定调 |
| 2 | **四层职责分离** | agent/rules/workflow/skills 各司其职 | 可维护、可扩展，避免单文件臃肿 |
| 3 | **先问后做 + Why 优先** | workflow 每步"conversational ask，最重要的先问，不要一次倾倒"；路线图重排先问"what changed" | 与 Alex「AI 辅助不决策」原则高度契合 |
| 4 | **防傲慢/防幻觉显式声明** | 用户研究"不编造用户声音，没数据就提出需要做"；竞品"诚实评估对手优势"；指标"相关≠因果、标置信度" | 直击 AI 最大风险点，质量护栏硬 |
| 5 | **受众适配模板库** | 高管 1 页纸/300 字、工程细节、客户无行话；含 G/Y/R 状态、ROAM 风险框架、ADR 决策记录模板 | "按对象写"是 PM 沟通核心，即插即用 |
| 6 | **驱动行动闭环** | 指标审查"不导致至少一个行动就是没用"；每个产物落到决策 | 避免"分析瘫痪" |
| 7 | **方法论结构化程度高** | PRD 8 段模板、RICE/MoSCoW/ICE/价值-努力矩阵带评分量表、竞品 4 层竞争集合 + 定位 4 层 + 赢/输分析、指标 北极星/L1/L2 + OKR + Dashboard 7 原则 | 降低 AI 输出方差，可直接复用 |
| 8 | **研究综合方法论扎实** | 主题分析 6 步、亲和图、三角验证、定性-定量循环、persona 模板、机会规模估算（影响=用户×频次×严重度） | 把"访谈→洞察"标准化 |
| 9 | **边界与免责清晰** | "不替代专业判断""竞品基于公开信息可能不准""归因是假设需验证" | 防过度承诺 |
| 10 | **文件即文档** | README 含场景示例、最佳实践 ✓/✗、目标用户、注意事项 |  humans 易上手、易复盘 |

---

## 三、不足在哪

| # | 不足 | 说明 | 对你影响 |
|---|------|------|---------|
| 1 | **缺治理骨架** | 无编号体系、CHANGELOG、SOURCE-REGISTRY、质量门（QG） | 纳入你的库需做治理映射（GOV v3.6 原则八/十） |
| 2 | **rules 与 README 内容重复** | rules 的 system_reminder 大段复述 README 的 6 能力（DRY 违反） | 维护易漂移；你可用"引用"而非复制解决 |
| 3 | **无去 AI 味机制** | 输出无风格约束，易有 AI 腔 | 可叠加你的 S-070（expression-purifier） |
| 4 | **缺判定表（可判定化弱）** | "何时用 RICE vs ICE vs MoSCoW"多为叙述，无明确触发判定表 | 你 pm-suite 有更硬触发，可补 |
| 5 | **缺异常/fallback 路径** | 数据矛盾、样本=0 时如何处理未定义 | 鲁棒性弱 |
| 6 | **中文本土化弱** | 偏北美 SaaS 语境（G2/Capterra、North Star）；无 ToG/ToB 售前视角 | 对你售前场景需改造 |
| 7 | **场景覆盖不全（对你最关键）** | 无售前/招投标/技术方案评审/客户画像/招标解析；无产品战略 Go-NoGo 深度；无商业化定价专项 | 你的 pm-bid-proposal / pd-go-nogo 正好补，但它是"PM 通用工种"缺口 |
| 8 | **无质量门自检清单** | 靠 tips 软约束，无强制校验（对比你 QG1-QG13） | 输出下限保障弱 |
| 9 | **中英文混用** | workflow SKILL 全文英文，agent/README 中文 | AI 执行无碍，但一致性略差 |
| 10 | **无版本/依赖声明** | plugin.json 无 skill 间依赖图 | 大改时易漏联动 |

---

## 四、对你的可借鉴点（与你的原则契合度）

| 借鉴点 | 对应你现有体系 | 契合度 |
|--------|--------------|--------|
| 专家包形态（Agent+Rules+Skills） | 你 pm-suite 平铺 SKILL，缺"专家入口"层 | 高，可直接建 `product-management-expert` 专家包 |
| "先问后做/Why 优先"纪律 | 「AI 辅助不决策」原则 | 完全一致，可注入 pm 类技能 |
| 防傲慢/防幻觉声明 | S-030(ai-content-quality) 管事实、S-070 管风格 | 互补，可组合 |
| G/Y/R + ROAM + ADR 模板 | pm-stakeholder-management（偏识别，缺产物模板） | 高，直接补强 |
| RICE/ICE/价值-努力矩阵 | pd-portfolio-management（评分/财务/战略法） | 补"轻量优先级"缺口 |
| 机会规模估算 | 无对应 | 新增价值点 |
| 北极星/L1/L2 + OKR + Dashboard | economic-suite 偏财务，无产品健康指标 | 补"产品分析"缺口 |

---

## 五、你现有 skills 的不足评估（对照表）

| 能力域 | 你现有覆盖 | 缺失/弱项 | 本 Agent 能否补 |
|--------|-----------|----------|----------------|
| 产品战略（NPDP） | pd-suite 全流程 ✓ | — | — |
| 项目管控（PMBOK） | pm-suite 16 技能 ✓ | — | — |
| 招投标 | pm-bid-proposal ✓ | — | — |
| **PM 通用工种（PRD/路线图）** | ✗ 无端到端助手 | 明显缺口 | ✓ 强补 |
| **竞品分析（产品视角）** | market-comparable 仅投行 Comps | 缺功能/定位/赢输 | ✓ 补 |
| **产品指标体系** | economic-suite 偏财务 | 缺北极星/OKR/Dashboard | ✓ 补 |
| **用户研究综合** | ✗ 无 | 明显缺口 | ✓ 强补 |
| **利益相关者沟通产物** | pm-stakeholder-management 偏识别 | 缺按受众写+模板库 | ✓ 补 |
| 去 AI 味 | S-070 ✓ | — | 反向：你补它 |
| 治理骨架 | GOV v3.6 + 四表 ✓ | — | 反向：你管它 |

**结论**：本 Agent 补齐你库中「PM 通用工种 / 产品分析」这一明显短板，与你现有「项目管控 + 产品战略 + 招投标」形成互补；其纪律与你的「AI 辅助不决策」原则一致，可吸收。

---

## 六、融合判定（原则九·功能相近必须评估融合）★关键

经读取 pd/pm/market 套件 7 个相近技能头部，确认本 Agent **6/7 技能与现有库高度重叠**，方案A 不能真建 7 个平行技能。融合判定表：

| Agent 技能 | 现有对应（编号） | 重叠度 | 现有已覆盖 | Agent 增量（值得吸收） | 融合判定 |
|----|----|----|----|----|----|
| feature-spec | pd-prd-writing (PT-007) | 高 | 8模块PRD/BRD-MRD-PRD/IEEE830/GB8567/埋点/RTM | 先问后做纪律、SSO示例 | 补强 PT-007，不新建 |
| roadmap-management | pd-product-strategy (PT-001)+pd-portfolio-management | 高 | 路线图3格式/安索夫/迈尔斯-斯诺 | RICE/ICE/价值-努力矩阵明确触发 | 补强 PT-001 加 RICE/ICE |
| stakeholder-comms | pm-stakeholder-management (JT-015) | 中（视角异） | 干系人识别/权力-利益矩阵/参与度 | 按受众写+G/Y/R+ROAM+ADR模板 | 补强 JT-015 加沟通产物模板 |
| user-research-synthesis | pd-user-research (PT-012) | 高 | Persona/CJM/JTBD/假设映射/OST | 主题分析6步/亲和图/三角验证/机会规模估算 | 补强 PT-012 加机会规模估算 |
| competitive-analysis | pd-market-research (PT-003)+market-comparable(MT-001) | 高 | 竞品5-7对比/SWOT/感知图/PESTLE | 竞争4层/定位4层/赢-输分析/趋势信号噪声 | 补强 PT-003 加赢-输+定位 |
| metrics-tracking | pd-tools-metrics (PT-013) | 高 | 北极星/OKR/KPI/9优先级/财务 | Dashboard 7原则/告警卫生/周月季节奏 | 补强 PT-013 加 Dashboard+节奏 |
| product-management-workflows | pd-workflow-chains/pm-workflow-chains | — | 已有链式索引 | 路由编排模式 | 借鉴模式，不新建 |

**修正后方案A（原则九合规）**：不建 7 平行技能，改为
1. 新建 1 个专家包 `pm-product-expert`（agent 人设 + rules + workflow 路由），归入 pm-suite，内部路由到现有技能；
2. 新增 1 个 `references/` 模板库（G/Y/R、ROAM、ADR、RICE 触发表、机会规模估算、赢/输、Dashboard 原则），以"引用"注入上述 6 技能；
3. 叠加 S-070 去 AI 味。

工作量从"7 新建"降为"1 包 + 1 模板库 + 6 补强注入"。

## 七、执行进度

- ✅ Step 0：原版归档 `_external-archive/product-management-expert-source/`（13 文件）+ SRC-004 登记（SOURCE-REGISTRY）
- ✅ Step 1：融合评估完成（上表）
- ⏳ Step 2：编号归属（pm-suite 序列，查 REGISTRY 定号）
- ⏳ Step 3：建专家包 + 模板库 + 6 补强 + S-070 叠加
- ⏳ Step 4：四表/README 治理更新
- ⏳ Step 5：分批提交（每批中文 commit message）

## 八、待拍板

- 融合判定（建 1 包 + 1 模板库 + 6 补强，而非 7 平行技能）是否确认？
- 确认后从 Step 2 开始，先查 REGISTRY 定专家包编号。

## 九、Agent 写得好四点 + 对你技能的改进映射（用户追问）

聚焦 4 个最值得借鉴的"写得好"点，并对照自身技能看改进空间。

### 1. 防傲慢 / 防幻觉的显式纪律
- **Agent 做法**：用户研究"不编造用户声音，没数据就主动提出需要做"；竞品"诚实评估对手优势，不为了证明我们更强而片面对比"；指标"相关≠因果、标 High/Med/Low 置信度、承认数据局限"；"让数据说话，不强行套入预定叙事"。
- **你的改进**：你已有 S-030(管事实幻觉) + S-070(管风格)，但缺 **PM 专用的"诚实评估对手 / 不编造用户声音 / 标置信度"护栏**。→ 在 `pd-user-research`(PT-012)、`pd-market-research`(PT-003) 补强时注入这些声明（已列入融合补强）。

### 2. 先问后做 / Why 优先的交互纪律
- **Agent 做法**：workflow 每步"conversational ask，最重要的先问，不要一次倾倒所有问题"；路线图重排先问"what changed"（基于新信息，非心血来潮）。
- **你的改进**：你已有"AI 辅助不决策"原则，但**技能层无统一的"先问后做"交互协议**。→ 在 `pm-product-expert` 专家包 agent 层 + 各技能 Step 1 统一加该纪律（建包时落地）。

### 3. 受众适配的沟通产物模板库
- **Agent 做法**：高管 1 页纸/300 字、工程细节、客户无行话；含 G/Y/R 状态、ROAM 风险框架、ADR 决策记录模板（直接可抄的 code block）。
- **你的改进**：`pm-stakeholder-management`(JT-015) 只有"识别 / 权力-利益矩阵 / 参与度"，**缺"按受众写更新"的产物模板**。→ 补强 JT-015 注入 G/Y/R + ROAM + ADR 模板（融合已列）。

### 4. 方法论结构化 + 模板即插即用
- **Agent 做法**：RICE/MoSCoW/ICE 带评分量表、北极星/L1/L2 指标层级、主题分析 6 步、机会规模估算（影响=用户×频次×严重度），全为 code block 模板，降低输出方差。
- **你的改进**：`pd-tools-metrics`(PT-013) 有北极星/OKR 但**缺 Dashboard 7 原则 + 周月季审查节奏**；`pd-product-strategy`(PT-001) **缺 RICE/ICE 明确触发**；`pd-user-research`(PT-012) **缺机会规模估算**。→ 模板库 `references/` 吸收（融合已列）。

**结论**：4 个"写得好"的点，恰好对应融合判定 6 处补强中的 4 类核心增量——**Agent 的优秀之处 = 你技能库的精准短板**。确认融合判定后，建包即把这些吸收进现有体系。
