# PM场景应用参考

> 本文档汇总各Skill中产品经理/项目经理相关的应用场景、案例和调用路径，便于PM快速定位"什么场景用什么Skill"。

## 一、PM全生命周期 × Skill映射

产品经理的日常工作可按生命周期划分为若干阶段，每个阶段对应不同的Skill组合：

| 生命周期阶段 | 核心任务 | 推荐Skill组合 | 典型产出 |
|------------|---------|-------------|---------|
| **机会发现** | 用户洞察、市场研究、竞品分析 | prompt-engineering-basics + creative-prompt-techniques（CMM多视角+EHS极端场景） | 用户画像、痛点清单、机会矩阵 |
| **产品定义** | 需求分析、产品设计、PRD撰写 | prompt-chain-design（SPECTRA分解）+ prompt-engineering-basics（咨询师工作流） | PRD、用户故事、功能清单 |
| **品牌战略** | 定位、价值主张、愿景 | brand-positioning → value-proposition → future-vision（自下而上） | 品牌定位声明、价值主张画布、愿景模板 |
| **营销策划** | GTM策略、推广方案 | marketing-planning + copywriting | 营销策划方案、渠道矩阵、传播节奏 |
| **内容生产** | 文案、故事、宣传材料 | copywriting（诊断→选路→执行）+ creative-prompt-techniques（语言风格三件套） | 产品文案、品牌故事、社交媒体内容 |
| **项目执行** | 任务分解、进度管理、风险控制 | prompt-chain-design（SPECTRA+CIRS）+ ai-content-quality（质量检查） | WBS、进度表、风险预案 |
| **复盘优化** | 效果评估、经验沉淀 | three-chain-orchestration（三链诊断）+ ai-content-quality（七特检测） | 复盘报告、优化建议 |

## 二、PM高频场景速查

### 场景1：竞品分析

**问题**："帮我分析一下竞品"

**诊断**：机制1（任务分解）缺失——"分析竞品"太笼统。

**引导反问**："你想分析竞品的哪些方面？功能对比、定价策略、用户体验，还是市场定位？你最想通过竞品分析回答什么问题？"

**Skill调用**：
1. `prompt-chain-design` → 诊断式引导，帮用户明确分析维度
2. `prompt-chain-design` → SPECTRA模型分解分析任务
3. `creative-prompt-techniques` → CMM跨域映射，从不同角色视角审视竞品

### 场景2：产品立项报告

**问题**："帮我写一份产品立项报告"

**诊断**：需要逻辑链+知识链+创意链三链协同。

**Skill调用**：
1. `brand-positioning` → 明确产品定位（战略输入）
2. `value-proposition` → 提炼价值主张（核心卖点）
3. `prompt-chain-design` → 三链融合PM案例（智能门锁立项报告）作为参考
4. `prompt-chain-design` → AIDA框架组织报告结构
5. `ai-content-quality` → PIA确保每段意图明确

### 场景3：产品Slogan/宣传语

**问题**："帮我想一个产品slogan"

**诊断**：创意链为主，需要情感共鸣+差异化表达。

**Skill调用**：
1. `brand-positioning` → 获取品牌定位（"你是谁"）
2. `value-proposition` → 获取核心价值（"为什么选你"）
3. `creative-prompt-techniques` → IDEA发散 + FOCUS聚合 + RTA修辞加工
4. `copywriting` → 广告语/Slogan模板

### 场景4：需求文档撰写

**问题**："帮我写一个需求文档"

**诊断**：机制5（质量控制）缺失——不知道验收标准。

**引导反问**："这个需求文档给谁看？开发团队？领导审批？他们最关心什么？你觉得'好需求文档'的标准是什么？"

**Skill调用**：
1. `prompt-chain-design` → 诊断式引导，明确受众和标准
2. `prompt-chain-design` → SPECTRA分解需求为工作包
3. `prompt-engineering-basics` → 咨询师工作流确保需求有针对性

### 场景5：营销策划方案

**问题**："帮我做一个产品推广方案"

**诊断**：需要战略输入+创意发散+执行落地。

**Skill调用**：
1. `brand-positioning` → 品牌定位（战略输入）
2. `value-proposition` → 核心价值主张（卖点提炼）
3. `marketing-planning` → 三大模块（创意概念→传播策略→执行方案）
4. `copywriting` → 各渠道文案生成
5. `creative-prompt-techniques` → 创意激发（MCS约束下创新）

### 场景6：风险应对方案

**问题**："帮我写个风险应对方案"

**诊断**：机制2（知识激活）+ 机制5（质量控制）缺失。

**引导反问**："这个项目的主要风险点你已经识别了哪些？这个方案是给团队内部用还是给领导汇报？"

**Skill调用**：
1. `prompt-chain-design` → 诊断式引导，激活项目知识
2. `prompt-chain-design` → SPECTRA分解风险为可管理的工作包
3. `ai-content-quality` → TFM确保方案始终围绕核心风险

### 场景7：AI输出质量不理想

**问题**："AI写的内容差点什么，但说不清哪里不对"

**诊断**：三链可能偏科。

**Skill调用**：
1. `three-chain-orchestration` → 三链诊断（9个弱信号扫描）
2. 定位短板后，调用对应Skill补强：
   - 逻辑弱 → `prompt-chain-design`
   - 知识弱 → `prompt-engineering-basics`
   - 创意弱 → `creative-prompt-techniques`
3. `ai-content-quality` → 七特快速检测清单扫描

## 三、PM必备Skill最小集

如果不想一次学太多，以下5个Skill覆盖PM 80%的日常场景：

| 优先级 | Skill | 覆盖场景 |
|-------|-------|---------|
| 1 | **prompt-engineering-basics** | 所有需要写提示词的场景（基础能力） |
| 2 | **prompt-chain-design** | 复杂任务分解、多步骤编排、诊断式引导 |
| 3 | **creative-prompt-techniques** | 创意发散、跨界联想、产品创新 |
| 4 | **copywriting** | 文案撰写（产品文案/品牌故事/广告语/社交媒体） |
| 5 | **marketing-planning** | 营销策划（GTM策略/推广方案/渠道选择） |

进阶补充：brand-positioning → value-proposition → future-vision → three-chain-orchestration

## 四、Skill调用关系全景图

```
                    ┌─────────────────────────────────────┐
                    │     three-chain-orchestration        │
                    │     （元Skill·质量保障层）             │
                    └──────┬──────────┬──────────┬────────┘
                           │          │          │
              逻辑链补强    │  知识链补强│  创意链补强
                           ↓          ↓          ↓
                  prompt-chain  prompt-eng  creative-prompt
                   -design      -basics      -techniques
                           ↑          ↑          ↑
                           │          │          │
                    ┌──────┴──────────┴──────────┴────────┐
                    │          基础提示语能力层              │
                    └──────────────────┬──────────────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
              ┌─────┴─────┐    ┌──────┴──────┐    ┌──────┴──────┐
              │  copywriting│    │ marketing-  │    │   品牌三模块  │
              │  (文案写作)  │    │  planning   │    │             │
              └─────┬──────┘    │ (营销策划)   │    │ brand-      │
                    │           └──────┬──────┘    │ positioning │
                    │                  │           │     ↓       │
                    │                  │           │ value-      │
                    │                  │           │ proposition │
                    │                  │           │     ↓       │
                    │                  │           │ future-     │
                    │                  │           │ vision      │
                    └──────────────────┴───────────┴─────────────┘
                          向上调用获取战略输入
```

---

*本文档随Skill体系演进持续更新。最后更新：v0.2.0 (2026-08-09)*
