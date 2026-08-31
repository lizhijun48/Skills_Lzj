---
name: portfolio-rebalancing
description: "Evaluate and rebalance a product portfolio using strategic alignment, financial performance, and risk diversification criteria. Covers portfolio health diagnosis, resource reallocation, new product investment prioritization, and portfolio optimization roadmaps. Use when reviewing product portfolio health, reallocating resources across products, prioritizing new product investments, or conducting quarterly portfolio reviews."
---

# 组合再平衡（Portfolio Rebalancing）

## Metadata
- **Name**: portfolio-rebalancing
- **Track**: PT（产品轨）
- **Phase**: PT-P6（产品生命周期管理）
- **Crosscut**: CX-2（工程经济）、CX-4（产品战略与组合）
- **Standard Source**: NPDP Body of Knowledge — Portfolio Management; PMP — Strategic Alignment
- **Triggers**: 产品组合, 组合管理, portfolio, 组合评审, 资源分配, 产品线, 产品矩阵, 投入分配, 组合优化, 产品健康度

## Instructions

You are a senior portfolio strategist conducting a comprehensive product portfolio review and rebalancing assessment for $ARGUMENTS.

Your task is to evaluate the entire product portfolio's health, identify imbalances, and design a reallocation plan that optimizes strategic value, financial return, and risk distribution.

## When to Use

- 季度/年度产品组合评审
- 公司战略调整后需要重新分配资源
- 新产品立项时需要评估对现有组合的影响
- 资源紧张需要在多个产品线之间取舍
- 并购/拆分后需要整合产品组合
- 产品退市后需要重新平衡组合

## Input Requirements

### Required
- **产品清单**: 当前组合中的所有产品/产品线（名称、阶段、主要指标）
- **战略方向**: 公司未来 12-24 个月的战略重点和增长目标
- **资源约束**: 可投入的总预算和人力资源上限

### Optional
- **各产品财务数据**: 收入、成本、利润率、增长率
- **市场数据**: 各产品的市场份额、竞争态势
- **管线数据**: 正在开发中的新产品及其预期上市时间
- **历史决策**: 上几次组合评审的结论和执行情况

## Portfolio Rebalancing Framework

### Step 1: 组合健康度诊断（Portfolio Health Diagnosis）

对组合中的每个产品进行四维评估：

#### 1.1 战略对齐度（Strategic Alignment） — 权重 30%

| 评分 | 标准 |
|:---:|------|
| 3 | 核心战略产品，直接支撑公司主航道 |
| 2 | 战略相关产品，属于主航道延伸或互补 |
| 1 | 边缘产品，与当前战略弱相关 |
| 0 | 战略冲突或无关，存在拖累效应 |

#### 1.2 财务表现（Financial Performance） — 权重 30%

| 评分 | 收入增长 | 利润率 | 资源效率 |
|:---:|---------|--------|---------|
| 3 | >30% YoY | >40% | 高 ROI，每投入 1 元产出 >3 元 |
| 2 | 10-30% YoY | 20-40% | 中等 ROI |
| 1 | 0-10% YoY | 5-20% | 低 ROI |
| 0 | 负增长 | <5% 或亏损 | 资源黑洞 |

#### 1.3 市场势能（Market Momentum） — 权重 20%

| 评分 | 标准 |
|:---:|------|
| 3 | 市场领导者或快速增长的挑战者 |
| 2 | 稳固的市场参与者，有竞争优势 |
| 1 | 市场跟随者，无明确差异化 |
| 0 | 市场份额持续萎缩，竞争力丧失 |

#### 1.4 组合角色（Portfolio Role） — 权重 20%

使用改良 BCG 矩阵定位每个产品的组合角色：

| 角色 | 特征 | 组合功能 | 资源配置 |
|------|------|---------|---------|
| **明星** ⭐ | 高增长 + 高份额 | 未来核心 | 加大投入 |
| **现金牛** 🐄 | 低增长 + 高份额 | 利润来源 | 维持+收割 |
| **问号** ❓ | 高增长 + 低份额 | 未来赌注 | 选择性投入 |
| **瘦狗** 🐕 | 低增长 + 低份额 | 消耗资源 | 缩减或退市 |

**综合评分 = 战略(30%) + 财务(30%) + 市场(20%) + 角色加权(20%)**

### Step 2: 组合平衡度分析（Portfolio Balance Analysis）

#### 2.1 生命周期分布

```
理想组合的生命周期分布：
┌─────────────────────────────────────┐
│  孵化期  成长期  成熟期  衰退期      │
│   10%     30%     45%     15%       │
│  (1-2个) (3-5个) (4-6个) (1-2个)    │
└─────────────────────────────────────┘

检查项：
□ 是否有足够的"未来产品"（孵化+成长 > 30%）
□ 是否有稳定的"利润基础"（成熟期 > 35%）
□ 衰退期产品是否过多（> 25% 需警惕）
□ 是否有明显的"代际断层"（某阶段为空）
```

#### 2.2 风险分散度

| 风险维度 | 集中风险信号 | 健康状态 |
|---------|------------|---------|
| 客户集中 | Top 3 客户贡献 >50% 收入 | 客户分散，单一客户 <20% |
| 产品集中 | Top 1 产品贡献 >60% 收入 | 多产品贡献，Top 1 <40% |
| 市场集中 | 单一市场/地区 >70% | 多市场分布 |
| 技术集中 | 依赖单一技术栈/平台 | 技术多元化 |
| 时间集中 | 多数产品处于同一生命周期阶段 | 阶段分散 |

#### 2.3 资源分配现状 vs 理想

```
当前资源分配热力图：
         投入高 │          │          │
               │ [产品A]  │ [产品B]  │
         ──────┼──────────┼──────────┤
               │ [产品C]  │ [产品D]  │
         投入低 │          │          │
               └──────────┴──────────┘
                 战略高       战略低

理想状态：
- 右上（高投入+高战略）：明星产品 → 应该在这里
- 左上（高投入+低战略）：需要审视 → 减少投入
- 右下（低投入+高战略）：投入不足 → 增加投入
- 左下（低投入+低战略）：瘦狗 → 退市候选
```

### Step 3: 再平衡方案设计（Rebalancing Plan Design）

#### 3.1 资源再分配矩阵

| 动作 | 产品 | 资源变化 | 理由 | 时间线 |
|------|------|---------|------|--------|
| **加码** ⬆️ | [明星产品] | +X 人/+Y 预算 | 高增长+高战略对齐 | 立即 |
| **维持** ➡️ | [现金牛] | 不变 | 稳定利润来源 | 季度review |
| **缩减** ⬇️ | [边缘产品] | -X 人/-Y 预算 | 低战略对齐+低增长 | 下季度 |
| **退市** ❌ | [瘦狗] | 全部释放 | 参考 product-sunset-assessment | 6 个月内 |
| **新投** 🆕 | [新产品候选] | +X 人/+Y 预算 | 填补组合缺口 | 立项评审后 |

#### 3.2 资源释放-再投入闭环

```
退市/缩减释放的资源 → 再投入优先级排序：

1. 填补"代际断层"：某生命周期阶段无产品 → 优先投入孵化期
2. 加码明星产品：高增长产品投入不足 → 追加投入
3. 新产品管线：管线中缺少未来 12-24 月上市产品 → 加速开发
4. 能力建设：共性技术/平台投入不足 → 基础设施投资
```

### Step 4: 组合路线图（Portfolio Roadmap）

设计未来 12-24 个月的组合演进路径：

```
时间轴：        Now          Q+1         Q+2         Q+3         Q+4
               ──────────────────────────────────────────────────────
产品A(明星)    [投入]       [加速]      [扩张]      [收获前期]   [现金牛]
产品B(问号)    [评估]       [验证]      [加码or放弃] [→明星/→瘦狗]
产品C(现金牛)  [维持]       [维持]      [维持]      [收割准备]   [收割]
产品D(瘦狗)    [退市评估]   [退市执行]   [关闭]       —           —
产品E(新品)    [孵化]       [MVP]       [测试]      [上市]       [成长]
               ──────────────────────────────────────────────────────
组合健康度     [当前评分]    [+X分]      [+Y分]      [目标评分]
```

### Step 5: 治理与检查机制（Governance & Review Cadence）

| 频率 | 检查项 | 参与角色 | 输出 |
|------|--------|---------|------|
| 月度 | 各产品 KPI 异常检查 | 产品经理 | 异常报告 |
| 季度 | 组合健康度评审 | 管理层+产品负责人 | 季度评审报告 |
| 半年 | 战略对齐度重评 | 高管层 | 战略对齐更新 |
| 年度 | 全面组合再平衡 | 决策委员会 | 年度组合优化计划 |

## Output

### Primary Output
**产品组合再平衡报告**，包含：
1. 组合健康度评分卡（每个产品四维评分 + 综合分）
2. 组合平衡度分析（生命周期分布 + 风险分散度 + 资源热力图）
3. 资源再分配矩阵（加码/维持/缩减/退市/新投）
4. 12-24 个月组合演进路线图
5. 治理与检查机制建议

### Secondary Output
- 组合一页纸仪表盘（给管理层快速概览）
- 资源释放-再投入闭环方案（给财务和HR）
- 各产品行动计划（给各产品负责人）

### Quality Gate
- 所有产品的四维评分必须有数据支撑（不能仅凭主观判断）
- 资源再分配方案必须量化（具体人数、预算金额、时间线）
- 组合路线图必须标注关键里程碑和决策点
- 退市建议必须交叉引用 `product-sunset-assessment` 的输出

## Boundary

### Does Not
- 不替代 CFO 做正式的资本预算决策
- 不替代 HR 做具体的人员调配方案
- 不替代各产品经理做单个产品的详细规划
- 不处理并购/拆分的具体交易结构（仅评估对组合的影响）

### Handoff To
- `product-sunset-assessment` — 退市候选产品进入退市评估流程
- PT-P2 商业分析 — 新投产品需要商业论证
- JT 项目轨 — 组合调整落地作为项目来管理
- `brainstorm-okrs` — 组合调整后的 OKR 对齐

## Standard References
- **NPDP**: Body of Knowledge — Portfolio Management — Strategic Bucket Allocation
- **NPDP**: New Product Strategy — Innovation Charter & Strategic Alignment
- **PMP**: PMBOK 7th — Principle: Focus on Value; Performance Domain: Planning
- **一建**: 项目管理 — 组织论 — 多项目资源协调

## Branch Conditions

```yaml
context_param: review_scope
branches:
  full_review:
    trigger: "全面组合评审（年度/战略调整后）"
    depth: "所有产品全量评估 + 完整再平衡方案"
    duration: "深度分析"
    output_extras: ["组合演进路线图", "治理机制建议"]
  quick_health_check:
    trigger: "快速组合健康检查（季度/月度）"
    depth: "核心指标异常检测 + 建议调整"
    duration: "快速输出"
    output_extras: ["异常产品清单", "建议行动项"]
  single_product_impact:
    trigger: "评估单个新产品/退市对组合的影响"
    depth: "单产品评估 + 组合影响模拟"
    duration: "中等"
    output_extras: ["组合变化前后对比", "资源影响分析"]
```

## Further Reading
- NPDP Body of Knowledge, Chapter 2: Portfolio Management
- Cooper, R.G. "Winning at New Products" — Strategic Bucket Model
- "The BCG Matrix Still Works" — Harvard Business Review
- PMBOK 7th Edition — Value Delivery System
