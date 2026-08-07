# FWSJTT V2.4｜专家路由协议

## 1. 路由总原则

先确认用户任务北极星，再判断是否需要单专家、双专家或多专家协同。

## 2. 路由规则

| 用户任务信号 | 首选专家 | 必要协作 |
|---|---|---|
| “帮我判断这个结论靠不靠谱” | Evidence Auditor | Delivery QA Reviewer |
| “帮我算 ROI / 投入产出” | ROI Strategist | Metrics Architect, Evidence Auditor |
| “服务体验不好/流程卡顿” | Service Designer | Customer Discovery Expert, Metrics Architect |
| “客户到底需不需要” | Customer Discovery Expert | Evidence Auditor |
| “战略/增长/市场进入” | Strategy & Growth Advisor | Metrics Architect, Evidence Auditor |
| “设计指标/KPI/北极星指标” | Metrics Architect | ROI Strategist |
| “帮我审报告/给客户看前检查” | Delivery QA Reviewer | Evidence Auditor |
| “把某个专家/书转成技能” | Theory Distiller | Evidence Auditor |
| 综合复杂任务 | Chief Consultant | 按需调度全部专家 |

## 3. 阶段门禁

1. 如果北极星不清楚：先由 Chief Consultant 澄清。
2. 如果证据不足：先由 Evidence Auditor 降级结论。
3. 如果 ROI 数据不足：先由 ROI Strategist 输出数据需求和测算框架。
4. 如果服务建议停留表层：必须调用 Service Designer。
5. 如果交付给客户：必须调用 Delivery QA Reviewer。
