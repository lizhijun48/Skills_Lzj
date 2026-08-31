# 能力分层说明（Layers）— 已弃用

> **注意：** 本文件已被 `PHASES.md`（六阶段模型）替代。
> D/S/E/V/I 五层模型已升级为基于 PMP + NPDP + 一建的 P1-P6 + CX 六阶段框架。
> 请参考 [PHASES.md](PHASES.md) 获取最新的阶段定义。
> 本文件保留仅作为历史参考。

> SKILL 体系按 D/S/E/V/I 五层组织。
> 每一层回答一个不可替代的问题，层与层之间通过接口契约协作。

## 分层总览

```
         ↑ 抽象/战略
         │
         ↓ 具体/执行
  ─────┴──────────────────────────────────────────────────┘
  发现 & 诊断       方案 & 权衡       验证 & 证据       交付 & 协同
 (Discovery)      (Solution)       (Evidence)       (Delivery)
```

## D. 发现 & 诊断层（Discovery & Diagnosis）

**存在的唯一理由：** 把模糊变清晰 — 问题值不值得做、根因在哪、假设是什么。

**致命错误：** 还没验问题就去写 PRD → 叫"解决方案前置"，死得最快。

**常见槽位：**
- D1 Problem-Framing：问题界定 / 假设树 / 机会陈述
- D2 User-Insight：用户洞察 / 痛点链 / JTBD / 访谈合成
- D3 Opportunity-Screen：机会初筛 / 价值主张草稿 / 竞品定位

## S. 方案 & 权衡层（Solution & Tradeoff）

**存在的唯一理由：** 把"要做"变成"做什么 + 不做什么 + 为什么"。

**致命错误：** 写了巨长 PRD 但没写"为什么这个值、那个不值" → 无法防守。

**常见槽位：**
- S1 Scoping-Priority：范围与优先级（RICE/MoSCoW/约束表/砍留清单）
- S2 Flow-IA：流程与信息架构 / 关键路径 / 状态机
- S3 Spec-Writer：PRD / 验收条件 / 边界与异常

## E. 验证 & 证据层（Evidence & Metrics）

**存在的唯一理由：** 把信念变成可证伪的行动。

**致命错误：** 只讲故事不设计验证 → 产品变成信念系统。

**常见槽位：**
- E1 Experiment-Design：测试设计（AB/影子功能/定向访谈/MVP 探针）
- E2 Metrics-Interpret：漏斗定义 / 指标口径 / 异常解读 / 数据故事

## V. 交付 & 协同层（Delivery Ops）

**存在的唯一理由：** 让方案落地不糊、变更不崩、信息不丢。

**致命错误：** 交付 SKILL 替上游做决策 → 权责链断裂。

**常见槽位：**
- V1 Roadmap-Release：版本规划 / 发布节奏 / 依赖风险
- V2 Handoff-QA：研发评审清单 / 缺陷归因模板 / 变更控制备忘录

## I. 基础设施层（Infrastructure）

**存在的唯一理由：** 支撑整个体系运转的元能力 — 创建技能、编排智能体、管理知识。

**常见槽位：**
- I1 Skill-Creation：技能创建 / Prompt 工程 / SKILL 规范
- I2 Agent-Orchestration：多智能体编排 / 路由调度
- I3 Knowledge-Engineering：知识体系搭建 / 分类法设计

---

> 全局流向偏好：D → S →（E↔S）→ V
> 总控允许"跳层调用"（如用户已自带诊断结论可直达 S 层）
> 每个 SKILL 必须有一个主层归属，可有副层。
