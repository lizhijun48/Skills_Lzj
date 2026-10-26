# 体系级治理审计报告

> 日期: 2026-10-26 | 依据: GOV_SkillGovernance.md v3.2 (§9 规则基准)
> 覆盖: 178 个 SKILL.md | 已治理: 83 | 工具: gov_audit.py v2

## 1. 审计摘要

| 门禁 | 状态 | 说明 | 对应 §9 规则 |
|------|------|------|-------------|
| QG1 | ✅ 通过 | 无明显风险 | 密度>4 标记 |
| QG4 | ✅ 通过 | 无冲突 | 同 Track 交集=空 |
| QG7 | ℹ️ 需深检 | 调用 qg7_analysis.py | 知识源交叉对比 |
| QG9 | 🟡 关注 | 1215 处 | 排除 checklist + 示例 |
| QG10 | 🟡 关注 | 投标类复盘关键词命中 | 复盘/回溯/对手画像 |
| QG12 | ✅ 通过 | 投标类概率关键词命中 | 蒙特卡洛/分布/置信 |
| QG13 | ✅ 通过 | 4 表一致性 | §8 联动表清单 |

## 2. 详细检查结果

### QG4: 触发词唯一性 ✅ 通过（同 Track 内无冲突，检查 {checked_pairs} 对）
### QG9: 可操作交付 🟡 发现 1215 处疑似占位符
- `_external-archive/product-management-expert-source/skills/competitive-analysis/SKILL.md`: `[Area 1]`
- `_external-archive/product-management-expert-source/skills/competitive-analysis/SKILL.md`: `[Feature 1]`
- `_external-archive/product-management-expert-source/skills/competitive-analysis/SKILL.md`: `[Feature 2]`
- `_external-archive/product-management-expert-source/skills/competitive-analysis/SKILL.md`: `[Area 2]`
- `_external-archive/product-management-expert-source/skills/competitive-analysis/SKILL.md`: `[Feature 3]`
- `_external-archive/product-management-expert-source/skills/competitive-analysis/SKILL.md`: `[target customer]`
- `_external-archive/product-management-expert-source/skills/competitive-analysis/SKILL.md`: `[need/problem]`
- `_external-archive/product-management-expert-source/skills/competitive-analysis/SKILL.md`: `[Product]`
- `_external-archive/product-management-expert-source/skills/competitive-analysis/SKILL.md`: `[category]`
- `_external-archive/product-management-expert-source/skills/competitive-analysis/SKILL.md`: `[key benefit]`
  ...共 1215 处
### QG13: 治理联动一致性 ✅ 通过
- JT-019 在注册表: ✅
- JT-019 在路由表: ✅
- pm-tender-analysis 在 JT 链路: ✅
- Catalog 列数(154) vs 扫描数(178): 差异=24 ⚠️ 需重新运行 gen_catalog.py
### QG1: 同轨同阶段密度 ✅ 无明显密集风险
### QG7: 方法论一致性 ℹ️ 需人工深检时调用 qg7_analysis.py
  (本脚本做粗粒度标记；完整分析见 `tools/qg7_analysis.py`)
### QG10: 动态反馈闭环 🟡 关注
- `pm-suite/pm-bid-proposal/SKILL.md`: 复盘关键词命中 5/6
- `pm-suite/pm-tender-analysis/SKILL.md`: 复盘关键词命中 1/6
- `pm-suite/pm-risk-management/SKILL.md`: 复盘关键词命中 0/6
### QG12: 概率风险评估 ✅ 通过
- `pm-suite/pm-bid-proposal/SKILL.md`: 概率关键词命中 6/6
- `pm-suite/pm-tender-analysis/SKILL.md`: 概率关键词命中 1/6
- `pm-suite/pm-risk-management/SKILL.md`: 概率关键词命中 4/6

---

## 3. 审计结论与建议

✅ **无 P0 阻塞项，体系整体健康。**
