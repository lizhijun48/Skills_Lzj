---
name: 工业互联网产品经理
governance_id: "PT-017"
description: This skill should be used when the user wants to design a product, create a PRD, analyze user requirements, design system architecture, plan product features, or make decisions about PC vs mobile platform division. It is especially relevant for industrial IoT, MES, micro-manufacturing management systems, or any project requiring clear user role analysis and scenario-driven design.
triggers:
  - 工业互联网产品经理
---

# 工业互联网产品经理

产品经理技能：提供系统性的产品设计方法论、领域知识参考和产品文档模板，帮助完成从需求分析到产品设计的全流程工作。

## 核心原则

产品设计必须同时考虑三个维度，缺一不可：

1. **系统本身的功能逻辑** — 模块划分、数据流转、实体关系
2. **使用人员的工作环境** — 有无电脑、网络条件、工作节奏
3. **操作场景与使用习惯** — 谁在用、怎么用、什么时候用

## 典型触发场景

- 设计和规划新模块/新功能
- 撰写 PRD、产品需求文档、功能规格文档
- 梳理业务流程（订单→派工→报工等）
- 分析用户角色并设计对应的功能分工
- 决定某功能应该放在 PC 端还是移动端
- 评估功能设计的合理性
- 设计用户交互方案（特别是移动端场景）

## 使用方式

### 第一步：加载参考文档

根据具体任务类型，加载对应参考文档：

```
需要微生产/MES 领域知识 → 加载 references/微生产系统域.md
需要 PC/移动端分工参考 → 加载 references/平台分工原则.md
需要产品设计方法论     → 加载 references/产品设计方法论.md
需要文档模板          → 加载 references/PRD模板.md
```

### 第二步：按工作流推进

所有产品设计任务统一遵循以下工作流：

```
1. 明确用户角色
   ↓ 加载 references/产品设计方法论.md 的"用户角色分析"章节
2. 梳理业务流程
   ↓ 参考 references/微生产系统域.md 的实体关系和状态机
3. 确定平台分工
   ↓ 参考 references/平台分工原则.md
4. 输出产品文档
   ↓ 使用 references/PRD模板.md
```

### 第三步：交付具体产出

产出物可以是：
- PRD / 产品需求文档（Markdown）
- 功能规格文档（Feature Spec）
- 业务流程图（Mermaid）
- 页面结构设计（Markdown 表格）
- PC/移动端功能分工表

## 快速决策参考

### PC端 vs 移动端判断

| 判断维度 | → PC端 | → 移动端 |
|---------|--------|---------|
| 操作频率 | 低频，周期性强 | 高频，实时性强 |
| 操作复杂度 | 复杂配置、多字段录入 | 简单操作、单步完成 |
| 输入方式 | 键盘+鼠标 | 触屏+扫码 |
| 用户设备 | 办公室人员，有电脑 | 车间工人，无/少电脑 |
| 网络环境 | 稳定 | 可能不稳定 |
| 典型功能 | 计划排程、报表分析、基础数据配置 | 报工、点检、进度查看 |

### 用户角色快速分层

```
管理层 / 决策者  → 看板看数据为主，PC+移动都行
   ↓
职能人员 / 计划员 → PC端配置+下发，移动端查看
   ↓
班组长           → 移动端为主（审批+管理），PC辅助
   ↓
一线工人         → 移动端（报工+点检），不用PC
```

## 参考文档

| 文档 | 用途 |
|------|------|
| `references/微生产系统域.md` | 微生产/MES 系统的核心实体、流程、状态机 |
| `references/平台分工原则.md` | PC端与移动端的功能划分方法论 |
| `references/产品设计方法论.md` | 用户角色分析、场景设计、需求分析方法 |
| `references/PRD模板.md` | PRD / 功能规格文档的标准模板 |
