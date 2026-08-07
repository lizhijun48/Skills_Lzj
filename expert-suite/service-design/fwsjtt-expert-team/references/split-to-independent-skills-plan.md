# FWSJTT V2.4｜拆分为 1 个主技能包 + 9 个独立技能包计划

## 1. 目标

未来产出 1 个专家团主技能包和 9 个专家独立技能包。

## 2. 推荐顺序

### 阶段 A：主技能包固化

- `fwsjtt-chief-consultant`
- 保留路由协议、共享 QA、专家调用说明。

### 阶段 B：高频专家优先独立

1. `fwsjtt-service-designer`
2. `fwsjtt-roi-strategist`
3. `fwsjtt-delivery-qa-reviewer`
4. `fwsjtt-customer-discovery-expert`

### 阶段 C：管理与方法专家独立

5. `fwsjtt-evidence-auditor`
6. `fwsjtt-metrics-architect`
7. `fwsjtt-strategy-growth-advisor`
8. `fwsjtt-theory-distiller`
9. `fwsjtt-chief-consultant` 若已作为主包，则独立版本可作为总控包本体。

## 3. 每个独立 Skill 包必须包含

- `SKILL.md`
- `references/`
- `tests/`
- `README.md`
- 敏感扫描报告
- 回归测试用例

## 4. 不建议立即执行的原因

本阶段只完成专家规格拆解。正式生成 1+9 技能包前，应先确认每个专家的命名、触发词、是否共享 references，以及主包如何调用子包。
