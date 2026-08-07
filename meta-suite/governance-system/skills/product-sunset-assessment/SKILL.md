---
name: product-sunset-assessment
description: "Evaluate whether a product should be retired, downsized, or transitioned using a structured sunset decision framework. Covers decline signal detection, financial impact analysis, user migration planning, and communication strategy. Use when considering product retirement, evaluating declining products, planning product transitions, or managing end-of-life decisions."
---

# 产品退市评估（Product Sunset Assessment）

## Metadata
- **Name**: product-sunset-assessment
- **Track**: PT（产品轨）
- **Phase**: PT-P6（产品生命周期管理）
- **Crosscut**: CX-2（工程经济）、CX-4（产品战略与组合）
- **Standard Source**: NPDP Body of Knowledge — Life Cycle Management; PMP — Closing Process Group
- **Triggers**: 产品退市, 产品下线, sunset, end-of-life, 产品要不要砍, 衰退期, 产品转型, 用户迁移

## Instructions

You are a senior product lifecycle strategist conducting a structured sunset assessment for $ARGUMENTS.

Your task is to evaluate whether the product should be retired, downsized, merged, or transitioned — and if so, design a safe, minimally disruptive sunset plan.

## When to Use

- 产品指标持续下滑，考虑是否退市
- 组合评审中识别到"瘦狗"类产品
- 公司战略调整，需要砍掉非核心产品线
- 产品已被新产品替代，需要规划过渡
- 定期产品组合健康检查中的退市评估

## Input Requirements

### Required
- **产品描述**: 产品名称、核心功能、当前版本
- **当前指标**: 至少包含用户数趋势、收入趋势、维护成本（最近 6-12 个月）
- **战略上下文**: 公司当前战略方向、是否有替代产品

### Optional
- **用户反馈**: NPS 趋势、流失率、投诉主题
- **合同义务**: 未到期客户合同、SLA 承诺
- **依赖关系**: 其他产品/服务对该产品的依赖
- **团队配置**: 当前投入该产品的团队人数和成本

## Sunset Decision Framework

### Step 1: 衰退信号检测（Decline Signal Detection）

评估以下 6 个衰退信号维度，每个维度打分 0-3：

| 维度 | 0（健康） | 1（关注） | 2（警告） | 3（危险） |
|------|----------|----------|----------|----------|
| 用户增长 | 正增长 | 增长放缓 | 零增长 | 负增长 |
| 收入趋势 | 正增长或稳定 | 小幅下滑(<10%) | 显著下滑(10-30%) | 急剧下滑(>30%) |
| 维护成本比 | <20% 收入 | 20-40% | 40-60% | >60% |
| 用户满意度 | NPS>30 | NPS 10-30 | NPS 0-10 | NPS<0 |
| 战略对齐 | 核心战略 | 相关但非核心 | 边缘 | 与战略冲突 |
| 替代方案 | 无替代 | 有替代但不成熟 | 替代已成熟 | 用户已在迁移 |

**总分判定：**
- 0-6 分：**维持** — 产品健康，继续运营
- 7-12 分：**优化** — 缩减投入、合并功能到主产品
- 13-18 分：**退市** — 启动退市规划

### Step 2: 财务影响分析（Financial Impact Analysis）

```
退市成本计算：
├── 直接成本
│   ├── 用户迁移支持成本（客服、培训、补偿）
│   ├── 合同违约金 / SLA 赔偿
│   ├── 技术迁移成本（数据迁移、API 兼容层）
│   └── 团队转型成本（再培训、调岗、遣散）
├── 机会成本
│   ├── 释放的资源投入新产品/项目的预期收益
│   └── 品牌声誉影响（正面/负面）
└── 对比基线
    └── 维持现状 12 个月的预期 P&L

决策公式：
  退市 ROI = (维持成本 - 退市成本) / 退市成本
  > 1.0 → 退市划算
  < 1.0 → 维持更划算（但需重评 Step 1）
```

### Step 3: 用户影响评估（User Impact Assessment）

| 用户群体 | 规模 | 迁移难度 | 迁移方案 |
|---------|------|---------|---------|
| 重度用户（日活） | ? | 高 | 一对一迁移支持 + 数据迁移工具 |
| 中度用户（周活） | ? | 中 | 自助迁移指南 + 限时优惠 |
| 轻度用户（月活/不活跃） | ? | 低 | 邮件通知 + 替代产品推荐 |
| 企业客户（合同内） | ? | 很高 | 专属迁移经理 + 合同条款协商 |
| 已流失用户 | ? | 无 | 无需迁移（归档数据） |

### Step 4: 退市方案选择（Sunset Option Selection）

| 方案 | 适用场景 | 时间线 | 风险 |
|------|---------|--------|------|
| **A. 软退市** — 停止获客，现有用户继续使用 | 用户自然衰减，无强制迁移必要 | 12-24 个月 | 低 |
| **B. 引导迁移** — 提供替代产品+迁移激励 | 有成熟替代产品 | 6-12 个月 | 中 |
| **C. 强制退市** — 设定截止日期，到期关闭 | 产品严重亏损或战略冲突 | 3-6 个月 | 高 |
| **D. 合并吸收** — 功能合并到其他产品 | 核心功能仍有价值 | 6-12 个月 | 中 |

### Step 5: 沟通与执行计划（Communication & Execution Plan）

```
退市沟通时间线：
T-6个月：内部通知（管理层 + 产品团队 + 客服）
T-4个月：企业客户一对一沟通
T-3个月：公开公告（博客 + 产品内通知 + 邮件）
T-2个月：迁移工具上线 + 迁移指南发布
T-1个月：最后提醒（邮件 + 产品内弹窗）
T-0：服务关闭（读模式保留 30 天）
T+1个月：数据归档 + 用户确认
T+3个月：退市复盘
```

## Output

### Primary Output
**产品退市评估报告**，包含：
1. 衰退信号评分卡（6 维度 + 总分 + 判定）
2. 财务影响分析（退市 ROI + 成本明细）
3. 用户影响矩阵（5 类用户 + 迁移方案）
4. 推荐退市方案（A/B/C/D + 理由）
5. 沟通与执行时间线（6 个月倒计时）

### Secondary Output
- 退市决策一页纸（给管理层）
- 用户迁移 FAQ（给客服团队）
- 数据归档方案（给技术团队）

### Quality Gate
- 所有数字必须有来源（用户提供的数据或明确标注的估算假设）
- 退市 ROI 必须包含敏感性分析（最好/最坏/基准三种场景）
- 用户迁移方案必须覆盖所有 5 类用户群体

## Boundary

### Does Not
- 不替代财务部门做正式的资产减值评估
- 不替代法务部门审核合同违约条款
- 不替代管理层做最终的退市决策（提供分析和建议）

### Handoff To
- `portfolio-rebalancing` — 退市释放的资源重新分配到组合中
- PMP Closing Process — 项目层面的正式收尾流程
- JT 项目轨 — 退市执行作为项目来管理

## Standard References
- **NPDP**: Body of Knowledge — Product Life Cycle Management — End-of-Life Strategies
- **NPDP**: Portfolio Management — Product Line Rationalization
- **PMP**: PMBOK 6th — Closing Process Group — Close Project or Phase
- **一建**: 项目管理 — 项目收尾 — 竣工验收与保修

## Further Reading
- NPDP Body of Knowledge, Chapter 7: Life Cycle Management Strategies
- "How to Sunset a Product Gracefully" — Harvard Business Review
- PMBOK 6th Edition, §4.7 Close Project or Phase
