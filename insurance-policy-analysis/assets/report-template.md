# 家庭保单完整决策汇总报告

**报告日期**：{report_date}（{report_version}）
**投保人**：{policyholder_name}
**分析范围**：{family_scope}
**经济状态**：{economic_status}（所有决策已考虑现金流压力）

---

## 一、总览：{total_count} 张保单决策矩阵

| 序号 | 保单名称 | 被保人 | 年保费 | 策略 | 理由 |
|------|----------|--------|--------|------|------|
{policy_summary_rows}

### 年度现金流影响

| 时间节点 | 年保费合计 | 变化 |
|----------|------------|------|
| 当前（{current_year}） | {current_total}/年 | — |
{timeline_rows}

---

## 二、按被保人详细说明

### 被保人 A: {insured_a_name}（{insured_a_age}岁）

#### 保单 {policy_id}: {policy_name}（{contract_no}）

**基本信息：**

| 项目 | 内容 |
|------|------|
| 合同号 | {contract_no} |
| 生效日期 | {effective_date} |
| 年保费 | {annual_premium}（合同列明：{premium_text}） |
| 缴费期 | {payment_period} |
| 当前保单年度 | {current_year} |
| 已缴 | {paid_years}年，¥{paid_total} |
| 剩余 | {remaining_years}年 |

**保费明细：**

| 险种 | 代码 | 保额 | 年保费 |
|------|------|------|--------|
{premium_detail_rows}

**CV+RPU 双维度分析：**

| 险种 | Y{n1} CV | Y{n2} CV | CVΔ | Y{n1} RPU | Y{n2} RPU | RPUΔ |
|------|----------|----------|-----|-----------|-----------|------|
{cv_rpu_rows}

**综合判断矩阵：**

| 维度 | 评估 | 评判 |
|------|------|------|
| CV 增量 | 缴 ¥{premium} → CV+¥{cv_delta}（亏{cv_loss_pct}%） | {cv_judgment} |
| RPU 增量 | +¥{rpu_delta}（出险赔付面值） | {rpu_judgment} |
| 现金流 | 失去 ¥{premium} 年度现金 | {cashflow_judgment} |
| 外部替代 | {external_coverage} | {external_judgment} |

**三情景分析：**

| | 情景 A：续缴到底 | 情景 B：退保 | 情景 C：RPU |
|------|------|------|------|
| **继续支出** | ¥{continue_cost} | ¥0 | **¥0** |
| **立即回收** | ¥0 | ¥{surrender_cv} | ¥0 |
| 重疾保额 | ¥{ci_continue} | ❌ 无 | ¥{ci_rpu} |
| 身故保额 | ¥{life_continue} | ❌ 无 | ¥{life_rpu} |
| 其他保障 | — | ❌ 无 | {other_rpu} |

**决策确认：**

| # | 确认项 | 状态 | 备注 |
|---|--------|------|------|
| 1 | 是否支持 RPU | {rpu_support} | {rpu_note} |
| 2 | 缴费决定 | {payment_decision} | {payment_reason} |
| 3 | RPU 时机 | {rpu_timing} | {rpu_timing_note} |
| 4 | RPU 后保障 | {rpu_coverage} | {rpu_coverage_note} |
| 5 | 替代保障 | {alt_coverage} | {alt_coverage_note} |

---

## 三、附加险重叠分析

### RPU 后丢失的附加险

| 保单 | 丢失险种 | 年保费 | 同一被保人其他保单有？ | 缺口？ |
|------|----------|--------|------------------------|--------|
{lost_rider_rows}

### 保障缺口总结

{gap_summary}

---

## 四、外部产品替代参考

| 产品 | 保障类型 | 年保费 | 覆盖 | 不覆盖 |
|------|---------|--------|------|--------|
{external_product_rows}

### 推荐组合

{recommended_combo}

---

## 五、待确认事项

{todo_items}

---

## 六、最终建议执行顺序

| 步骤 | 操作 | 涉及保单 | 时间窗口 | 操作方式 |
|------|------|----------|----------|----------|
{action_steps}

---

> **重要提示**：
> 1. 本报告基于{data_date}前提取的合同数据
> 2. 所有保费、保额、CV、RPU 数据直接从保险合同原文提取，非估算
> 3. 分析假设见 references/methodology.md §E
> 4. 人口/健康宏观数据见 references/actuarial_data.md
