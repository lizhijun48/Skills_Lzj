# pm-bid-proposal 瘦身 v2 方案（GOV v3.6 原则八/九/十）

> 文件现状：1177 行 / 63 KB，用户自有（agent_created: true, governance_id JT-002），已高度模块化（重内容在 references/）
> 制定：2026-09-01 | 关联：law-repository（已入库招投标4部）/ SKILL-SLIMMING-BACKLOG.md
> 本方案为**执行前置判定**，需用户裁决后动 SKILL.md

## 0. 治理判定总览表（原则八）

| # | 瘦身动作 | 治理判定 | 偏离理由 | 裁决 |
|---|---|---|---|---|
| 1 | 第55-67行「法规依据」inline 表精简，改为引用 law-repository | 严格符合（与已建库去重） | 库已入库招投标4部，直接可引 | ⏳待裁决 |
| 2 | 第零~八步中「废标条款/红线」重复提示 精简为「详见 references/招标投标法规依据.md」 | 严格符合（原则九去重叠） | 与 references 重复 | ⏳待裁决 |
| 3 | 第882-906行「禁止内容铁律」与 references/forbidden_content.md 去重 | 严格符合（原则九） | 主文+references 双份 | ⏳待裁决 |
| 4 | 人设通用化（原则十） | **不适用** | 本技能为用户自有（无第三方人设/品牌标识） | — |
| 5 | 工作流 8 步 + 第11步复盘 压缩 | 特殊情况偏离 | 63KB 主要是流程 spine，是核心价值，不宜砍功能 | ⏳待裁决 |
| 6 | 联网获取部分 | **不动** | 本技能无外部 API（monte-carlo/bayesian 为本地 skill 工具）；references 法规核验属数据补全（见 BACKLOG D4） | — |

## 1. 原则九·融合评估
- vs pm-suite 其余15技能：定位唯一（投标方案编制），无功能重叠
- vs law-repository：唯一交叉点=法规依据。#1 动作将其改为引用库，去重且统一版本口径

## 2. 蒸馏数据 relocation（用户要求③：换地方、逻辑不变）
- **不变**：投标流程判断逻辑、评分拆解公式、报价博弈、蒙特卡洛/贝叶斯调用方式 全部保留
- **换地方**：第55-67行 inline 法规要点 → 指向 `legal-suite/law-repository/laws/<法名>.md`（4部已入库）；发改委55号令保留引用（待 BACKLOG D4 入库后迁移）
- **更新逻辑按新规则**：引用处加「来源：law-repository，快照日期 YYYY-MM-DD」，享受库 180天阈值级联标记

## 3. 联网接口处理（用户要求①）
- 本技能无外部联网 API。仅 references/招标投标法规依据.md 的原文核验属「固定数据后续补」（BACKLOG D4）
- monte-carlo / bayesian-update 调用：本地 skill 工具，原样不动

## 4. 执行路径（框架先搭）
- Step 1（立即可做）：#1 法规依据引库 + #2 废标提示去重 + #3 铁律去重
- Step 2（依赖 D4）：发改委55号令 入 law-repository 后迁移引用
- **不动**：工作流 8 步 spine、ITTO 元数据、协作接口、复盘闭环（核心价值）

## 5. 目标体积
63 KB → ~50 KB（去重为主，非砍功能）
