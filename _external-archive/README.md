# _external-archive — 外部技能来源归档案馆

> 定位：全局外部来源「原版归档溯源」专用目录（对应 GOV_SkillGovernance 原则十）。
> 凡从外部引入、经融合吸收进技能库的插件 / 资料，其**原始未改动版本**整包存放于此，保留可追溯性；融合结果记入 `SOURCE-REGISTRY.md`（SRC-xxx 编号）。
> 铁律：本目录下各来源的**原版文件（含各自自带的 README.md）一律保持不动**，仅在此根 README 登记溯源信息；差异化改造发生在技能库内的融合技能中，不在归档副本上。

## 归档清单

### 1. product-management-expert-source（SRC-004）

| 项 | 内容 |
|----|------|
| 来源 | CodeBuddy Teams 出品「产品经理 Agent 产品通」PM 插件（expertType=agent，声明 7 skill + 1 agent） |
| 本机源目录 | `C:\Users\Alex_Lee\WorkBuddy\2026-09-21-20-56-17\product-management-expert-source\` |
| 归档日期 | 2026-09-21 |
| 原版结构 | 13 文件 / 4 子目录：`.codebuddy-plugin/`（plugin.json）、`agents/`（product-management-expert.md 人设）、`rules/`（product_management_rules.md alwaysApply）、`skills/`（feature-spec / roadmap-management / stakeholder-comms / user-research-synthesis / competitive-analysis / metrics-tracking / product-management-workflows）、`README.md`（原版·未改动）、`LICENSE`、`.downloaded_at` |
| SRC 登记 | SOURCE-REGISTRY SRC-004（版本锚点 v1.6.6 / JT-021 建包完成） |
| 融合吸收 | 新建专家包 `pm-product-expert`（JT-021，归入 pm-suite）：agent 人设 + rules + workflow 路由，内部路由到现有技能 PT-007 / PT-001 / PT-005 / JT-015 / PT-012 / PT-003 / MT-001；6 技能补强注入 pd-prd-writing / pd-product-strategy / pd-user-research / pd-market-research / pd-tools-metrics / pm-stakeholder-management（G/Y/R、ROAM、ADR、RICE 触发、机会规模估算、赢/输、Dashboard 原则等模板）；叠加 S-070 去 AI 味 |
| 路径纪律 | 专家包内不再引用原插件 6 独立路径，统一指向融合后真实技能 ID（防断链） |
| 评估文档 | `product-management-expert-分析评估.md`（JT-021 建包前的差距 / 可借鉴点 / 融合判定分析，已一并归档于此目录） |
| 提交 | 原版归档 `430f5a5`；评估报告 + 溯源补记 `ae80e61` |

### SRC-004 评估与本地 skill 优化映射

- **评估报告**：`product-management-expert-分析评估.md`（同目录；JT-021 建包前的差距 / 可借鉴点 / 融合判定分析，含 Section 九「写得好四点 + 改进映射」）
- **融合判定**：原插件 6/7 技能与现有库高度重叠，按原则九不另起孤立技能，改为「1 专家包 JT-021 + 5 references 模板库 + 6 技能补强 + S-070」

| 本地 skill | 编号 | 吸收的增量（references/） | 解决的我方短板 | 评估依据 |
|-----------|------|--------------------------|---------------|----------|
| pd-prd-writing | PT-007 | 协同段 + 先问后做/Why 优先纪律 | 缺统一"先问后做"交互协议（§九②） | 评估报告 §九② |
| pd-product-strategy | PT-001 | prioritization-frameworks.md（RICE/ICE/MoSCoW 触发+价值-努力） | 缺 RICE/ICE 明确触发（§九④） | 评估报告 §九④ |
| pm-stakeholder-management | JT-015 | stakeholder-templates.md（G/Y/R+ROAM+ADR+按受众模板） | 偏识别，缺沟通产物模板（§九③） | 评估报告 §九③ |
| pd-user-research | PT-012 | research-methodology.md（主题分析6步/三角验证/机会规模估算）+ 防傲慢护栏 | 缺用户研究综合方法论（§九①④） | 评估报告 §九①④ |
| pd-market-research | PT-003 | competitive-frameworks.md（竞争4层/定位4层/赢-输/趋势信号噪声）+ 防傲慢护栏 | 缺产品视角竞品分析（§五） | 评估报告 §五 |
| pd-tools-metrics | PT-013 | metrics-dashboard.md（Dashboard 7原则/告警/周月季节奏） | 缺 Dashboard 原则+审查节奏（§九④） | 评估报告 §九④ |

> 各 skill 的"版本/基于什么/何时/改了什么/解决什么问题"见其 SKILL.md 末尾「来源吸收记录（SRC-004）」段（双向溯源：本表 → skill，skill → 本报告 + SRC-004）。

## 维护约定

1. 新增外部来源：在此根 README 追加一条归档清单（来源 / 日期 / 原版结构 / SRC 编号 / 融合落点 / commit）。
2. 原版文件只读：严禁为「补充说明」改动各来源自带 README.md 或任何原版文件；溯源信息统一记在本文件。
3. 对应四表：`SOURCE-REGISTRY.md`（来源视角登记）、`SKILL-ID-REGISTRY.md`（编号）、`SKILL-CATALOG.md`（目录）、`CHANGELOG.md`（时间视角）。
