# {policy_name}（{contract_no}）— 单保单分析

## 基本信息

| 项目 | 内容 |
|------|------|
| 合同号 | {contract_no} |
| 被保人 | {insured}（{birth_date}，{age}岁） |
| 投保人 | {policyholder} |
| 生效日期 | {effective_date} |
| 缴费期 | {payment_period} |
| 年保费 | {annual_premium}（合同列明：{premium_text}） |
| 已缴年数 | {paid_years}年，共 ¥{paid_total} |
| 当前保单年度 | 第 {current_year} 年 |

## 保费明细

| 险种 | 代码 | 基本保额 | 年保费 |
|------|------|----------|--------|
{premium_rows}

## 现金价值与减额交清保额（合同原文）

| 险种 | Y{n1} CV | Y{n2} CV | CVΔ | Y{n1} RPU | Y{n2} RPU | RPUΔ |
|------|----------|----------|-----|-----------|-----------|------|
{cv_rpu_rows}

## CV+RPU 双维度分析

### 维度一：CV 增量（现金价值，可变现）

缴 ¥{annual_premium} → CV 增加 ¥{cv_delta} → {cv_analysis}

### 维度二：RPU 增量（减额交清保额，出险才兑现）

缴 ¥{annual_premium} → RPU 合计增加 ¥{rpu_delta} → {rpu_analysis}

## 综合判断

| 维度 | 结论 |
|------|------|
| CV 增量 | {cv_conclusion} |
| RPU 增量 | {rpu_conclusion} |
| 现金流 | {cashflow_conclusion} |
| 外部替代 | {external_conclusion} |

**最终决策**：{final_decision}

## 三情景对照

| 情景 | 续缴 | RPU | 退保 |
|------|------|-----|------|
| 无出险 | — | CV 按 2.5% 复利 | 立即拿 ¥{cv} |
| CI 出险 | ¥{ci_continue} | ¥{ci_rpu} | ¥0 |
| 身故 | ¥{life_continue} | ¥{life_rpu} | ¥0 |
