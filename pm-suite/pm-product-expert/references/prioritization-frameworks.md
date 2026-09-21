# 优先级框架模板库（pm-product-expert / JT-021 · references）

> 来源：fork SRC-004（CodeBuddy Teams PM 插件）。本文件为 `pd-product-strategy`（PT-001）的**增量补充**——PT-001 已有路线图 3 格式与安索夫，本文件补 RICE/ICE/价值-努力的明确评分与触发判定。
> 调用：`pd-product-strategy` 做战略与路线图，本文件做细粒度优先级打分。

---

## 1. RICE 评分

`RICE = (Reach × Impact × Confidence) / Effort`

- **Reach**：给定时间段内影响的用户/客户数，用具体数字（如"500 用户/季度"）。
- **Impact**：对每个被触达者移动多大的指针，量表：3=巨大、2=高、1=中、0.5=低、0.25=极小。
- **Confidence**：对 Reach/Impact 估计的置信度，100%=高（有数据）、80%=中（有些证据）、50%=低（直觉）。
- **Effort**：人月工作量，含工程/设计/其他职能。

**何时用**：需要量化、可辩护的优先级排序；对比大 backlog 时。战略型赌注（影响难估）不擅长。

## 2. ICE 评分

`ICE = Impact × Confidence × Ease`（每项 1-10）

- **Impact**：对目标指标移动多大；**Confidence**：对影响估计的置信；**Ease**：实现难易（Effort 反比，越高越易）。

**何时用**：功能 backlog 快速排序；早期产品或缺 RICE 数据时用。

## 3. MoSCoW

- **Must**：没有它功能不成立，不可协商。
- **Should**：重要但非上线关键，常作快速跟进。
- **Could**：有余力再做，不影响交付。
- **Won't（this time）**：本周期明确不做，未来可重议。

## 4. 价值-努力矩阵（2×2）

- 高价值低努力（速赢）→ 先做
- 高价值高努力（大赌注）→ 谨慎规划
- 低价值低努力（填充）→ 有余力做
- 低价值高努力（黑洞）→ 不做，移出 backlog

## 5. 触发判定表（何时用哪个）

| 情境 | 框架 |
|------|------|
| 大 backlog、需向老板辩护 | RICE |
| 早期产品、数据少 | ICE |
| 发布/季度范围谈判 | MoSCoW |
| 团队工作坊可视化取舍 | 价值-努力矩阵 |
| 战略型、影响难量化 | 定性讨论 + MoSCoW，不强行打分 |

**铁律**：If everything is P0, nothing is P0。对每项 Must 追问"砍了它还解决核心问题吗？"。
