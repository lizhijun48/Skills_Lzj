# FWSJTT V2.4｜专家团队架构

## 1. 本阶段北极星指标

在不改变现有 V2.4 母技能包核心能力的前提下，将其拆解为一组可被总控调度、可独立说明、可后续独立封装的专家子技能规格。

## 2. 架构定位

FWSJTT V2.4 应被理解为“专家团队型技能包”，而不是单一技能。主技能包承担总控职责，专家子技能承担专门判断与产出。

## 3. 三层结构

```text
FWSJTT V2.4 Expert Team
├── 总控层：Chief Consultant
├── 专家层：Evidence / ROI / Service / Discovery / Strategy / Metrics / QA / Theory
└── 共享约束层：来源强度、ROI 权限、QA 评分、回归测试
```

## 4. 设计原则

1. 主技能包负责路由与合成，不吞并专家深度判断。
2. 每个专家必须有明确触发场景、输入、输出、边界和 QA。
3. Evidence Auditor 与 Delivery QA Reviewer 是横向守门专家。
4. 北极星未达成前，不发散到下一阶段。
5. 本阶段只做专家规格拆解，不生成正式独立 Skill 包。
