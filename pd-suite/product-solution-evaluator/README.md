# Product Solution Evaluator Skill

中文名：产品方案评估专家

## Purpose

This skill helps product leaders, business owners, and management teams evaluate whether a product idea, feature proposal, PRD, MVP, or commercial product initiative is worth pursuing.

## Core Evaluation Dimensions

- User value
- Business value
- Feasibility
- Strategic alignment
- Risk controllability
- Investment return
- MVP validation readiness

## Typical Inputs

- Product idea
- Feature proposal
- PRD draft
- MVP plan
- Commercialization proposal
- AI product concept
- Growth initiative

## Typical Outputs

- Clear recommendation
- 100-point score
- Dimension-by-dimension analysis
- Top risks
- MVP validation plan
- Decision checklist

## Installation

Place this folder under your user skills directory:

```text
~/.box-agent/skills/product-solution-evaluator/
```

Make sure `SKILL.md` exists and contains valid YAML front matter.

## Minimal Test Prompt

```text
请评估以下产品方案：

方案名称：酒店会员智能升舱推荐功能
目标用户：酒店会员和前台运营人员
方案描述：系统根据会员等级、历史入住偏好、当前房态、订单价格和酒店收益策略，自动推荐是否为用户提供升舱权益或付费升舱选项。
目标：提升会员满意度，提高升舱收入，优化房态利用率。

请从用户价值、商业价值、可行性、风险、投入产出和 MVP 验证角度评估是否值得推进。
```
