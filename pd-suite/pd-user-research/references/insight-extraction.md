# 录音 / 文本 PM 洞察抽取 · 参考规范

> 本文件为 `pd-user-research` 的**洞察抽取能力模块**的详细实现规范，供 SKILL 主体调用，也可由其他 SKILL 直接读取以复用规则。
>
> **来源说明**：从外部 AI PM 工具集（ai-pm-exploration-toolkit）的音频智能流水线（`audio_transcription.py` + `pm_audio_workflows.py`）提取并适配。原项目用 Whisper 本地转写 + 关键词抽取，**本规范剥离了模型/Docker 依赖，仅保留与部署无关的方法论与规则**——音频需先经任意 STT 转写为文本，本规范只处理**文本**。
>
> **方法性质**：轻量规则法（关键词/句式匹配），结果确定、可复现、可审计，无需大模型。

---

## 1. 能力定位

| 项 | 说明 |
|----|------|
| 输入 | 真实录音的**转写文本** `text` + 场景标识 `use_case` |
| 处理 | 按 `use_case` 选择抽取维度 → 关键词/句式匹配（句级）→ 去重取 Top-N |
| 输出 | 结构化洞察清单（按维度分栏）+ Markdown 格式化报告 + 相关性评分 |
| 不替代 | JTBD 深层动机挖掘、客户访谈设计、Persona 构建（本能力只做表层抽取） |

---

## 2. 六类场景与抽取维度

| # | use_case 标识 | 中文场景 | 抽取维度（pm_insights_focus） | 典型产出物 |
|---|---------------|---------|-------------------------------|-----------|
| 1 | `user_interview` | 用户访谈 | `pain_points` / `feature_requests` / `user_goals` / `usability_issues` | 痛点/功能请求/用户目标/可用性问题 四栏 |
| 2 | `stakeholder_meeting` | 干系人会议 | `decisions_made` / `action_items` / `concerns_raised` / `next_steps` | 决策/行动项/风险担忧/下一步 纪要 |
| 3 | `demo_feedback` | 产品演示 | `reactions` / `questions_asked` / `suggested_improvements` / `positive_feedback` | 反应/提问/改进/正向反馈 |
| 4 | `competitive_research` | 竞品研究 | `product_features` / `pricing_strategy` / `market_positioning` / `competitive_advantages` | 功能/定价/定位/优劣势 情报 |
| 5 | `voice_memo` | 语音备忘 | `key_ideas` / `action_items` / `follow_ups` / `task_categories` | 结构化待办/灵感 |
| 6 | `customer_support` | 客服电话 | `pain_points` / `feature_requests` / `user_goals` / `usability_issues` + 情绪层 | 痛点/问题/功能请求/情绪 |

> ⚠️ **诚实标注（与原项目差异）**：原项目 `audio_transcription.py` 的关键词抽取**仅实现了 1/2/3 三类**；`competitive_research`、`voice_memo` 在原代码中 `pm_specific_analysis` 为空（未接抽取分支），`customer_support` 复用了 `user_interview` 的抽取。本规范**补全了 4/5/6 的抽取词表**（见 §3），使六类能力完整可用。

---

## 3. 关键词 / 句式抽取词表

**匹配规则**：文本转小写 → 按句号切句 → 若某句含该维度任一 indicator，则整句归入该维度 → 同维度去重 → 取 Top-5（不足 5 则全取）。

### 场景 1 · 用户访谈（user_interview）

| 维度 | indicator 词表 |
|------|---------------|
| `pain_points` | difficult, hard, frustrating, annoying, problem, issue, struggle, confusing |
| `feature_requests` | would like, wish, could you, feature, add, include, want |
| `user_goals` | trying to, want to, need to, goal, objective, accomplish |
| `usability_issues` | can't find, don't know how, unclear, confusing, not obvious |

### 场景 2 · 干系人会议（stakeholder_meeting）

| 维度 | indicator 词表 |
|------|---------------|
| `decisions_made` | decided, agreed, determined, resolved, settled |
| `action_items` | will do, action item, follow up, next step, assign, responsible for |
| `concerns_raised` | concerned, worried, risk, issue, problem, challenge |
| `next_steps` | next step, next week, follow up, continue, move forward |

### 场景 3 · 产品演示（demo_feedback）

| 维度 | indicator 词表 |
|------|---------------|
| `reactions` | wow, great, interesting, cool, impressive, concern, question |
| `questions_asked` | 句式级：含 how / what / why / when / where / can you 的疑问句 |
| `suggested_improvements` | could improve, better if, suggest, recommend, enhance |
| `positive_feedback` | like, love, great, excellent, good, helpful, useful |

### 场景 4 · 竞品研究（competitive_research）【本规范补全】

| 维度 | indicator 词表 |
|------|---------------|
| `product_features` | feature, capability, functionality, supports, integrates, dashboard, api, module, export, workflow |
| `pricing_strategy` | price, pricing, cost, subscription, per month, per user, free tier, enterprise plan, discount |
| `market_positioning` | target, segment, positioning, competitor, alternative, versus, vs, for [role], aimed at |
| `competitive_advantages` | advantage, better, faster, unique, differentiator, strength, weakness, drawback, limitation |

### 场景 5 · 语音备忘（voice_memo）【本规范补全】

| 维度 | indicator 词表 |
|------|---------------|
| `key_ideas` | idea, think, maybe, concept, thought, suppose, what if, why not |
| `action_items` | todo, need to, should, must, action, remind, do, let's |
| `follow_ups` | follow up, check, ask, confirm, sync, loop in, ping, revisit |
| `task_categories` | 按句中主题词归类（如"客户/需求/技术/会议/文档"），无强制词表，交由调用方分类 |

### 场景 6 · 客服电话（customer_support）

复用 `user_interview` 四个维度（pain_points / feature_requests / user_goals / usability_issues），**额外加一层情绪标注**：
- 负面情绪词：angry, frustrated, disappointed, unhappy, complain, terrible, worst
- 正面情绪词：happy, satisfied, thanks, appreciate, glad, love

> 情绪层仅作标记，不参与结构化抽取计数；用于判断反馈整体倾向。

---

## 4. 输出格式（Markdown 报告模板）

### 用户访谈报告骨架
```
# 用户访谈洞察

**时长**：X 分钟  **字数**：Y

## 用户痛点
1. <句子>
## 功能请求
1. <句子>
## 用户目标
1. <句子>
## 可用性问题
1. <句子>
```

### 干系人会议纪要骨架
```
# 会议纪要

## 关键决策
- <句子>
## 行动项
- <句子>
## 风险与担忧
- <句子>
## 下一步
- <句子>
```

### 演示反馈 / 竞品情报 / 语音备忘 / 客服
按对应维度替换为 `reactions`/`questions_asked`/`suggested_improvements`/`positive_feedback` 或 `product_features`/`pricing_strategy`/`market_positioning`/`competitive_advantages` 等栏目，结构同理。

---

## 5. 相关性评分（可选）

抽取完成后按焦点维度命中数给相关性评级：
- `focus_score` = Σ(各焦点维度命中条数)
- `relevance` = high（>5）/ medium（>2）/ low（≤2）

用于快速判断"这段录音是否值得深挖"。

---

## 6. 调用接口约定（供其他 SKILL 复用）

```
能力名：  pd-user-research.insight-extraction
触发条件：持有"真实录音转写文本"且需 PM 结构化洞察
输入：
  {
    "text": "<转写全文>",
    "use_case": "user_interview | stakeholder_meeting | demo_feedback | competitive_research | voice_memo | customer_support",
    "top_n": 5
  }
输出：
  {
    "insights": { "<维度>": ["句子1","句子2",...] },
    "report": "<Markdown 格式化报告>",
    "relevance": "high | medium | low"
  }
前置依赖：音频需先经 STT 转写；本能力只处理文本，无外部模型依赖（纯规则）
注意：
  - 本能力做表层关键词抽取，不替代 JTBD / 访谈设计等深层方法
  - 抽出的句子应回灌真实研究流程，由人核验后再进 PRD / backlog / 纪要
```

---

## 7. 与 pd-user-research 其他步骤的边界

| 本能力做 | 应改走其它步骤 |
|---------|---------------|
| 把**已有真实文本**快速结构化 | 没有真实素材想"造"用户 → Step 2 Persona（基于真实访谈，禁止随机生成） |
| 表层痛点/功能/情绪抽取 | 挖深层动机 → Step 4 JTBD |
| 会议纪要/反馈整理 | 设计访谈提纲 → Step 5 客户访谈 |
| 竞品情报初筛 | 系统化竞品框架 → pd-market-research |
