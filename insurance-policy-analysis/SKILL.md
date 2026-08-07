---
name: insurance-policy-analysis
governance_id: "S-012"
description: >
  Comprehensive Chinese life insurance policy analysis and family portfolio optimization.
  Covers: pre-analysis data gathering, PDF contract extraction, single-policy CV+RPU
  dual-dimension analysis, insurance intrinsic value assessment (using Chinese demographic/
  health/medical macro data), rider overlap detection, external product replacement,
  multi-policy portfolio optimization under constraints, lifetime EPV with rate-path
  scenarios, and special-scenario stress testing (divorce, unemployment, minors).
  Built from real contract-driven analysis across 9 policies and 4 insured persons.
  Trigger when: 保单分析, 退保, 减额缴清, RPU, 保单决策, 保险精算, EPV计算,
  保单组合优化, 附加险重叠, 现金价值, 保费评估, 家庭保单规划.
agent_created: true
triggers:
  - insurance
  - policy
  - analysis
---

# Insurance Policy Analysis — 全流程方法论

> Built from 9 policies × 4 insured persons across 6 version iterations.
> Each methodology correction has a real mistake behind it — see `references/case-studies.md`.

---

## 0. Mandatory Rules (Non-Negotiable)

1. **Group by insured person.** Never mix policies across different insured individuals.
2. **All data from contract originals.** Premiums, sums insured, CV, RPU — extract from PDF only. No assumptions or "typical structures".
3. **Extract annual premium from policy front page.** Distinguish "首期保险费合计(年交)" from total premiums. Cross-verify Chinese-character amounts with numeric amounts.
4. **Benefits trigger independently.** Never sum across different risk types unless the contract explicitly states a "total sum insured."
5. **CV continues compounding post-RPU.** Cash value grows at the guaranteed rate (typically 2.5%) after RPU — never assume it stops.
6. **EPV to age 105, always.** Never truncate to policy duration. RPU provides lifelong coverage.
7. **Three scenarios together.** No-claim / CI claim / death — all three must align before concluding.
8. **Never skip Phase 0.** Prompt for missing information before any calculation.
9. **Do not use "RPU sum-insured increase ÷ premium" as ROI.** RPU is a function of CV; its increase is not cash return. Use the CV+RPU dual-dimension framework.
10. **Incorporate macro context.** Use Chinese demographic/health data from `references/actuarial_data.md` to assess insurance value against medical inflation, aging trends, and income levels.

---

## 1. Methodology Evolution

| Version | Issue | Fix |
|---------|-------|-----|
| v1-v2 | Formula-based estimates, premium errors (total vs annual) | Contract data extraction workflow |
| v3.0 | Extracted CV/RPU tables; CI amount off by 10× | All values from contract tables |
| v3.1 | Self-summed "total sum insured" — user corrected | Never cross-type sum |
| v4.0 | "Pay Y8 → RPU up ¥22,890 → ROI 547%" | **Fatal**: RPU increase is not ROI |
| v5.0 | CV-increment framework: ¥4,183 → CV+¥1,765 → 58% loss | Correct framework |
| v6.0 | CV-only incomplete; missed RPU dimension | CV+RPU dual-dimension |

> **Core lesson**: RPU sum insured is "paper face value that only pays out on claims." Never use it as ROI numerator.

---

## 2. Phase 0: Pre-Analysis Information Gathering

### Step 1: Prompt for Policy Inventory

Present this checklist (in Chinese):

```
在开始分析前，请先确认以下信息：

【一、已有保单清单】
  - 被保人姓名、性别、出生日期
  - 保单名称、合同号
  - 年保费（或月保费×12）
  - 已缴几年 / 还剩几年
  - 是否有附加险

【二、外部/普惠保险】
  □ 城市惠民保（如深圳惠民保 ¥88/年）
  □ 学平险 / 公司补充医疗 / 单位团体险
  □ 支付宝/微信意外险、医疗险
  □ 合家欢·樂 等家庭意外险
  □ 城乡居民医保

【三、背景信息】
  - 家庭经济状况（就业状态、现金流压力）
  - 是否有病史
  - 特殊关系（如离婚）
```

### Step 2: Map City to 惠民保

| City | Product | Premium |
|------|---------|---------|
| 深圳 | 深圳惠民保 | ¥88/年 |
| 北京 | 北京普惠健康保 | ¥195/年 |
| 上海 | 沪惠保 | ¥129/年 |
| 广州 | 广州惠民保 | ¥180/年 |
| 成都 | 蓉惠保 | ¥59-99/年 |
| 杭州 | 西湖益联保 | ¥150/年 |

### Step 3: Missing Contracts

- **平安**: 平安金管家 App → 我的保单
- **人保**: 中国人保 App / 微信公众号
- **惠民保**: WeChat search "[city]惠民保"

---

## 3. Phase 1: Policy Inventory & Data Extraction

### 3.1 Inventory

List all policies grouped by insured person:

```
For each insured person:
  - Policy name, contract number, effective date
  - Payment years, paid years, remaining years
  - RPU capability? CI type (advance-payment vs independent)?
  - Calculate current policy year: floor((today - effective_date) / 365) + (past anniversary? 1 : 0)
```

### 3.2 PDF Extraction

Use `scripts/extract_policy_pdf.py`:

```bash
python scripts/extract_policy_pdf.py policy.pdf --json -o extract.txt
```

Or use pymupdf directly:
```python
import fitz
doc = fitz.open("policy.pdf")
text = "".join(page.get_text() for page in doc)
```

### 3.3 Mandatory Extraction Per Policy

**Front page:**
- Contract number, effective date, policyholder, insured
- **Annual premium** (ONLY from "首期保险费合计(年交)") — this is the sole authoritative source
- Premium breakdown by risk type (name, code, sum insured, annual premium)
- Payment period

**CV & RPU tables** (typically side-by-side on same page):
- Extract CV and RPU for **each risk type separately**
- Both current (Y_{N-1}) and next (Y_N) year values
- See `references/case-studies.md` for extraction examples

**Rider list:**
- Each rider: name, code, annual premium
- Mark if "本栏以下空白" (no riders)

### ⚠️ Premium Extraction Trap

**Wrong**: Treating total paid premiums as annual premium.
**Right**: Extract only from "首期保险费合计(年交)" on the front page; verify Chinese-character amount matches.

---

## 4. Phase 2: Single-Policy Analysis

### 4.1 Three Scenarios

**Scenario A — No Claim (Baseline):**
- Continue: CV compounds at guaranteed rate to age 105
- RPU: RPU CV compounds at guaranteed rate to age 105

**Scenario B — CI Claim:**
- Continue: CI sum insured paid, subsequent premiums waived (if waiver rider), death benefit reduced
- RPU: RPU CI sum insured paid, no further premiums

**Scenario C — Death:**
- Continue: Death sum insured paid
- RPU: RPU death sum insured paid

All three scenarios must point in the same direction for a robust conclusion.

### 4.2 Surrender Assessment

```
Immediate surrender value = current CV
Surrender loss = total premiums paid - current CV
Loss ratio = (total paid - CV) / total paid × 100%

Loss > 50% → surrender usually bad
Loss > 70% → surrender almost certainly bad
No RPU option → binary choice: continue or surrender
```

### 4.3 CV+RPU Dual-Dimension Framework ⚠️ Core Methodology

**When to use**: Policy is in grace period (past anniversary, premium unpaid, within 60-day window).

**Step 1 — Extract two-year data**: From the CV & RPU table (side-by-side on same contract page), extract Y_{N-1} and Y_N values for each risk type.

**Step 2 — Calculate deltas**:
```
CV_delta = Σ Y_N CV - Σ Y_{N-1} CV  (by risk type)
RPU_delta = Σ Y_N RPU - Σ Y_{N-1} RPU  (by risk type; list individually, do not cross-sum)
```

**Step 3 — CV dimension**:
```
CV_delta > annual premium → CV dimension favorable
CV_delta < annual premium → CV dimension unfavorable
Loss% = (premium - CV_delta) / premium × 100%
```

**Step 4 — RPU dimension**: Present RPU increase per risk type. Note: **RPU increase is claim-face-value, not cash.** The leverage ratio (RPU_delta / premium) reflects extra coverage bought, not ROI.

**Step 5 — Comprehensive judgment matrix**:

| Dimension | What ¥{premium} buys | Nature | Weight in unemployment |
|-----------|---------------------|--------|------------------------|
| CV delta | ¥{cv_delta} realizable value | Cash — real money | Highest |
| RPU delta | ¥{rpu_delta} claim face value | Face value — claim only | Medium |
| Cash flow | Lose ¥{premium} annual cash | Immediate outflow | Decisive |
| External alt | Existing other policies | Risk mitigation | Reduces RPU need |

**Decision rules**:

| Condition | Conclusion |
|-----------|------------|
| CV unfavorable + cash flow tight | **Do NOT pay, RPU directly** (even if RPU delta is large) |
| CV favorable + cash flow allows | Can pay Y_N then RPU |
| CV unfavorable + RPU delta huge + coverage critical | May pay (requires user confirmation) |
| No RPU function | Binary: continue or surrender |

### 4.4 Worked Example

See `references/case-studies.md` for full worked examples (福上福 梦焉 & 落尘).

Summary: 梦焉 ¥4,183 premium → CV+¥1,765 (58% loss), RPU+¥22,890 (5.5× leverage, claim only) → **RPU directly**.

---

## 5. Phase 3: Insurance Value Analysis (Macro Context)

> Reference data: `references/actuarial_data.md`

### 5.1 Medical Inflation Impact

Apply the medical inflation rate (~7%/yr) to assess real CI purchasing power:

```
Real_CI_value(t) = CI_face_amount / (1 + medical_inflation)^t
```

A ¥300K CI policy today: ¥168K after 10 years, ¥94K after 20 years (at 6% inflation).

**Decision implication**: High-premium, low-CI policies may have diminishing real value over decades. RPU preserves the nominal amount but doesn't escape real-value erosion.

### 5.2 Cancer Risk vs Coverage Gap

Using the cancer incidence data from actuarial_data.md §3:

```
Lifetime cancer risk (to age 75): approximately 25-30%
Annual CI incidence at age 40-60: 84 per 100K (effective rate)
Expected CI claim probability over 30-year coverage window: ~2.5-5%
```

**Decision implication**: CI insurance is a low-probability, high-impact product. The EPV of CI coverage tends to be a small fraction of face value — the value is in tail-risk protection, not expected return.

### 5.3 Demographic Context

- Aging rate 23% (60+) → Social security pressure will increase
- Life expectancy 79 → RPU's lifetime-value argument strengthens
- Family size 2.52 → Intra-family risk pooling declining → commercial insurance value rising

### 5.4 Premium Burden Assessment

| Burden Rate | Threshold | Assessment |
|-------------|-----------|------------|
| <5% of household income | — | Comfortable |
| 5-10% | — | Moderate |
| 10-15% | — | Heavy |
| 15-20% | — | Stressed |
| >20% | — | Unsustainable |
| **Unemployed** | Any premium | **Optimize immediately** |

Calculate: `burden_rate = total_annual_premiums / household_annual_income × 100%`

---

## 6. Phase 4: Rider Overlap & External Replacement

### 6.1 Rider Overlap Analysis

For each policy marked for RPU:
1. List all short-term riders (accident medical, hospitalization daily allowance, etc.)
2. Check if other valid policies for the same insured have identical riders
3. If overlap → no coverage gap after RPU
4. If no overlap → mark as coverage gap

### 6.2 External Product Matrix

| Product | Coverage | Cost | Covers | Does NOT Cover |
|---------|----------|------|--------|----------------|
| 合家欢·樂 | Accident | ¥699/yr (family) | Accident medical ¥30K/person + hospitalization allowance | Disease hospitalization |
| City 惠民保 | Major illness reimbursement | ¥88-195/person/yr | 80-90% in-network + 70-75% out-of-pocket | Hospital cash allowance |
| Original riders | Hospital daily allowance | Varies | Disease + accident hospitalization cash | — |

### 6.3 Combination Strategy

```
合家欢 (accident medical + accident hospitalization) + 惠民保 (major illness reimbursement)
  > Original rider combo (accident medical + disease/accident daily allowance)
  AND cheaper: ¥699+¥176 = ¥875/yr vs ¥657×2 = ¥1,314/yr
```

### 6.4 Irreplaceable Core Coverage

- **CI lump-sum** (e.g., 人保无忧人生 ¥300K): Neither 合家欢 nor 惠民保 covers → irreplaceable
- **Whole life insurance** (e.g., 福上福 main policy): No external substitute → irreplaceable
- **Only replaceable**: Short-term riders (accident medical, hospitalization daily allowance)

---

## 7. Phase 5: Portfolio Optimization & Comprehensive Planning

### 7.1 Policyholder Profile

For each policy, build a profile matrix:

| Dimension | Analysis | Impact |
|-----------|----------|--------|
| Age | Current → retirement → life expectancy | EPV parameters, coverage horizon |
| Health | Known conditions, exam abnormalities | Underwriting feasibility for alternatives |
| Income/Employment | Current income, industry outlook, stability | Premium affordability, unemployment risk |
| Family role | Primary / secondary / non-earner | Coverage priority |
| Marital status | Married / divorced | Beneficiary risk, policyholder change needs |

### 7.2 Economic State Stress Matrix

| State | Premium burden threshold | Strategy |
|-------|--------------------------|----------|
| Employed, dual-income | <10% tolerable | Normal; optimize allocation |
| Employed, single-income | <8% tolerable | Watch burden rate |
| **Unemployed** | Any premium = pressure | Minimize cash outflow immediately |
| Unemployed + savings | <3% maintainable | Keep core, RPU rest |
| Unemployed + depleting savings | **Target 0%** | RPU all eligible immediately |
| Long-term unemployed (>6mo) | May need CV access | Priority: RPU > surrender |

### 7.3 Portfolio Optimization Constraints

```
Objective: Minimize annual cash outflow
Constraints:
  1. Each insured: minimum CI ≥ ¥300K
  2. Each insured: minimum life ≥ ¥100K
  3. No coverage blackout for any insured post-RPU
  4. Minor children: coverage must not degrade
  5. Divorced policies: beneficiary risk must be resolved
```

### 7.4 Multi-Policy Coordination

```
Steps:
  1. Group all policies by insured person
  2. Analyze independent optimal strategy for each
  3. Cross-check: after RPU of one policy, do remaining policies still satisfy constraints?
  4. Identify overlapping coverage: same type/same insured → keep best, RPU rest
  5. Calculate combined cash flow: annual premium timeline under different decision combos
```

### 7.5 Cash Flow Timeline Output

```
Current ({year})
├─ Policy A  ¥X,XXX
├─ Policy B  ¥X,XXX  ← RPU → ¥0
└─ Policy C  ¥X,XXX
──────────────────────────
Total        ¥XX,XXX/yr

X years later (Policy A paid off)
──────────────────────────
Total        ¥XX,XXX/yr  ↓Save ¥X,XXX/yr

Y years later (all paid off)
──────────────────────────
Total        ¥0/yr        All coverage effective
```

---

## 8. Phase 6: Lifetime EPV & Rate-Path Analysis

### 8.1 EPV Calculation

Run `scripts/policy_epv_calc.py`:

```bash
python scripts/policy_epv_calc.py --a-age 14 --a-death 32739 --a-ci 56200 --a-cv 7517 \
    --b-age 8 --b-death 24422 --b-ci 56200 --b-cv 5407 --discount 0.03 --sensitivity
```

Key parameters (see `references/methodology.md` §E):
- discount_rate (d) = 2.0% default
- invest_return (r) = 3.0% default
- policy_guaranteed_rate = 2.5%
- MAX_AGE = 105
- mort_adj = 0.80 (CLT2025)
- medical_inflation = 7.0%

Critical rules:
- EPV extends to age 105, never truncated (12-year truncation understates RPU by 10-20×)
- Before age 18: death benefit = CV (minor protection cap)
- After age 18: death benefit = RPU face amount
- RPU CV continues compounding at 2.5%

### 8.2 Rate-Path Scenarios

Run `scripts/rate_path_decision.py`:

```bash
python scripts/rate_path_decision.py
```

4 preset paths:

| Path | Probability | d | r | Description |
|------|-------------|---|---|-------------|
| deep_low | 15% | 0.8% | 1.5% | Japan-style persistent low |
| gradual_low | 50% | 1.5% | 2.5% | Gradual decline (baseline) |
| stable_current | 25% | 2.0% | 3.0% | Maintain current level |
| moderate_recovery | 10% | 2.5% | 3.5% | Moderate recovery |

### 8.3 Probability-Weighted Decision

```
Weighted_net_advantage = Σ(path_prob_i × net_diff_i)

< -2,000 → RPU
-2,000 ~ +2,000 → borderline, comprehensive judgment needed
> +2,000 → surrender
```

---

## 9. Phase 7: Final Report

Generate using `assets/report-template.md` structure:

1. **Overview**: N-policy decision matrix
2. **Per insured person**: One policy per section, with CV+RPU analysis, 3 scenarios, confirmation matrix
3. **Rider overlap summary**: Gaps and how they're addressed
4. **Cash flow impact**: Annual premium timeline
5. **External alternatives**: Recommended replacement combo
6. **Action items**: Ordered by urgency with operational guidance
7. **Pending confirmations**

### Report Format Standards

- Premiums: cite contract source ("合同列明：人民币...")
- RPU amounts: list per risk type, never self-sum
- Decisions: use confirmation matrix (item / status / note)
- All numbers: verify against contract originals before finalizing

For single-policy analysis, use `assets/single-policy-template.md`.

---

## 10. Special Scenarios

### 10.1 Divorce Policies

**Risk checklist:**
1. Beneficiary control: Policyholder can unilaterally change beneficiary
2. Moral hazard: Paying premiums but can't ensure payout direction
3. Property division: CV as marital asset → needs divorce agreement clarity

**Resolution path (priority order):**

```
1st: Transfer policyholder to ex-spouse (within 30 days)
  ↓ unwilling
Fallback: Surrender (recover CV, immediate stop-loss)
  ↓ willing to take over
Best: Ex-spouse becomes new policyholder, self-pays
       You exit completely, free up annual cash flow
```

**Suggested divorce clause**: "双方确认，以甲方为投保人、乙方为被保险人的 XX 保险合同（合同号：XXX），自本协议签署之日起 30 日内，双方配合办理投保人变更为乙方的手续。变更完成后，甲方不再承担保费缴纳义务。如乙方未在约定期限内配合，甲方有权自行退保，退保所得现金价值归甲方所有。"

### 10.2 Unemployment

| Tier | Trigger | Action |
|------|---------|--------|
| Yellow | Expected <3mo, have savings | Pause non-core (use grace period), maintain core |
| Orange | 3-6mo, savings depleting | RPU all eligible; evaluate surrender for non-RPU |
| Red | >6mo, savings exhausted | RPU everything; surrender remainder; 惠民保 backfill |

### 10.3 Minor Insured

- Death benefit < age 18: capped at CV (not face amount)
- EPV calculation: segment <18 (CV-based) vs ≥18 (RPU-based)
- 惠民保 availability: check city-specific product

### 10.4 CI Type Distinction

- **Advance-payment** (提前给付): CI payout reduces death benefit equally (e.g., 平安福)
- **Independent** (独立给付): CI and death benefits are separate (e.g., 人保无忧人生)
- Affects Scenario B (CI claim) net benefit calculation

---

## 11. Common Pitfalls

| Pitfall | Consequence | Fix | Source |
|---------|-------------|-----|--------|
| RPU increase ÷ premium = "ROI" | False 500%+, wrong recommendation | CV+RPU dual-dimension; RPU increase is face value | v4→v5 |
| CV only or RPU only | Incomplete analysis | Both dimensions always | v5→v6 |
| Self-summing "total sum insured" | No contract basis | List per risk type | v3.1 |
| Annual vs total premium confusion | 10× premium error | Front page "首期保险费合计(年交)" only | v3→v4 |
| EPV truncated to payment period | 10-20× undervaluation | Always to age 105 | — |
| RPU CV assumed static | Undervalued terminal value | CV continues at 2.5% | — |
| Rider overlap guessed | Wrong gap analysis | Always read actual contract PDF | — |
| Discount rate direction reversed | Wrong rate-path conclusions | d moves WITH market rates | — |
| Mixed insured analysis | Chaotic results | Always group by insured | — |
| Minor death cap forgotten | Overstated <18 death benefit | CV as death benefit for <18 | — |
| Formula estimates vs contract | 10× CI error (¥3,500 vs ¥27,980) | Contract RPU tables only | v2→v3 |
| Ignoring medical inflation | Overvalued long-term CI | Apply 7% medical inflation decay | New |
| Ignoring premium burden ratio | Unsustainable recommendations | Calculate vs household income | New |

---

## 12. Bundled Resources

| Resource | Path | Use When |
|----------|------|----------|
| Macro data (life tables, cancer rates, demographics, medical costs) | `references/actuarial_data.md` | Phase 3 insurance value analysis; EPV parameters |
| Full methodology (EPV, rate paths, value framework, stress tests) | `references/methodology.md` | Detailed formula reference; comprehensive planning |
| Case studies (9 policies, 4 insured persons) | `references/case-studies.md` | Worked examples; methodology validation |
| PDF extraction script | `scripts/extract_policy_pdf.py` | Phase 1 contract data extraction |
| EPV calculator | `scripts/policy_epv_calc.py` | Phase 6 lifetime EPV |
| Rate-path decision engine | `scripts/rate_path_decision.py` | Phase 6 scenario analysis + HTML report |
| Full report template | `assets/report-template.md` | Phase 7 multi-policy final report |
| Single-policy template | `assets/single-policy-template.md` | Single-policy analysis |

---

## 13. Skill Integration

- `pm-project-opportunity` — Go/No-Go quantification for surrender vs RPU decisions
- `pm-bid-proposal` — Structured thinking for report organization
- `resume-optimizer` — Clear decision rationale presentation
