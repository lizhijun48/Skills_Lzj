# 干系人沟通模板库（pm-product-expert / JT-021 · references）

> 来源：fork SRC-004。本文件为 `pm-stakeholder-management`（JT-015）的**增量补充**——JT-015 已有识别/权力-利益矩阵/参与度，本文件补"按受众写更新"的**产物模板**（G/Y/R、ROAM、ADR）。
> 调用：`pm-stakeholder-management` 做识别与策略，本文件做沟通产物。

---

## 1. 状态色 G/Y/R

- **Green（On Track）**：按计划推进，无显著风险，将达承诺。
- **Yellow（At Risk）**：慢于计划或风险已现，缓解中但结果不确定；**首次见风险即转黄**，不等确认坏。
- **Red（Off Track）**：显著落后，无明确缓解，需重大干预（砍范围/加资源/延期限）；需求助时才转红。

> 状态色反映真实评估，不是乐观主义；Yellow 不是失败，是好风险沟通。

## 2. 按受众更新模板

**高管 / 领导层（<300 字）**
```
Status: [Green/Yellow/Red]
TL;DR: [一句话最重要的事]
Progress: [关联目标/OKR 的产出]
Risks: [风险]:[缓解]. [需帮忙的 ask]
Decisions needed: [决策]:[选项+建议]. Need by [日期].
Next milestones: [里程碑]—[日期]
```

**工程团队**（含链接）
```
Shipped: [功能/修复]—[PR 链接].[影响]
In progress: [项]—[owner].[预计完成].[blocker]
Decisions: [已定]:[理由] / [待定]:[选项+建议]
Coming up: [下一批]—[为何是 next]
```

**跨职能伙伴**
```
What's coming: [功能/发布]—[日期].[对你团队含义]
What we need: [具体 ask]—[日期]
Decisions made: [决策]—[对你团队影响]
Open for input: [话题]—[如何反馈]
```

**客户 / 外部**（无行话）
```
What's new: [功能]—[客户视角的好处].[如何用]
Coming soon: [功能]—[预期时间].[为何重要]
Known issues: [问题]—[状态].[workaround]
Feedback: [如何反馈]
```

## 3. 风险沟通 ROAM

- **Resolved**：已解决，记如何解。
- **Owned**：已认领，有人管，记 owner+缓解计划。
- **Accepted**：已知但选择不缓解，记理由。
- **Mitigated**：已行动降到可接受，记做了什么。

**风险表述五步**：①清晰陈述风险 ②量化影响 ③标可能性 ④给缓解 ⑤提具体 ask。

## 4. 决策记录 ADR

```
# [决策标题]
## Status: [Proposed/Accepted/Deprecated/Superseded by ADR-XXX]
## Context: 什么情况需决策？哪些力量在作用？
## Decision: 决定了什么（清晰直接）
## Consequences: 正/负后果；启用或阻断了什么
## Alternatives: 评估过的其他选项及为何拒
```
> 接近决策时写，记谁参与、谁拍板；可记错误决策（加 superseded by 链接）；一页胜五页。
