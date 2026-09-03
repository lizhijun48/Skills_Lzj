# Skills 技能体系

> AI辅助编程与产品经理技能治理仓库。**双轨架构**（pd-suite 产品轨 + pm-suite 项目轨）+ **共用层**（general-suite / meta-suite）+ 领域套件（legal / economic / market / industry / expert / gaoxiang / research）。

## 三层文档导航

| 层级 | 文件 | 回答什么 |
|------|------|---------|
| **L0 全局** | 本 `README.md` | 有什么套件、怎么找、入口在哪 |
| **L1 套件** | 各套件目录 `README.md` | 该套件有哪些技能、各自职责、协作关系 |
| **L2 技能** | 各技能目录 `SKILL.md` | 单个技能的职责 / 用法 / 接口 / 变更 |

> 查「技能在哪个套件、负责什么」→ 看 L1 套件 README；查「编号→路径→阶段→状态」→ 看 `SKILL-ID-REGISTRY.md`（唯一事实来源）。

## 仓库结构

| 套件 | 前缀 | 说明 | 套件 README |
|------|------|------|------------|
| pd-suite/ | PT- | 产品轨——产品经理全流程技能 | ✅ |
| pm-suite/ | JT- | 项目轨——项目管理全流程技能 | ✅ |
| general-suite/ | S- | 通用层——跨领域基础能力 | ✅ |
| meta-suite/ | S- | 元技能——技能治理与创建工具 | ✅ |
| legal-suite/ | L- | 法律服务（含中央法规库） | ✅ |
| economic-suite/ | E- | 经济决策工具 | ✅ |
| market-suite/ | MT- | 市场估值工具（与 E- 上下游分工） | ✅ |
| expert-suite/ | S-/X- | 专家视角（视角类 + 服务设计专家团） | ✅ |
| industry-suite/ | I- | 行业解决方案（代账/C2C/代谢/医药/通用） | ✅ |
| gaoxiang-suite/ | GX- | 高项备考 | ✅ |
| reading-os/ | R- | 阅读操作系统（单入口三模块） | ✅ |
| research-suite/ | RE- | 研究技能（CDA 因果动力学） | ✅ |
| resume-optimizer/ | S- | 简历优化助手（独立部署） | ✅ |
| insurance-policy-analysis/ | S- | 保险保单分析（独立部署） | ✅ |
| gridman/ | S- | 财税调度中枢（独立部署，S-019） | ✅（产品文档） |

## 治理与记录文件

| 文件 | 用途 |
|------|------|
| `SKILL-ID-REGISTRY.md` | 编号注册表（唯一事实来源） |
| `SKILL-CATALOG.md` | 技能全量目录 |
| `GOV_SkillGovernance.md` | 治理规则（v3.6，含原则一~十） |
| `BUSINESS-FLOW-MAP.md` | 业务流映射 |
| `DECISION-LOG.md` | 决策日志（Why it was changed + What's next） |
| `CHANGELOG.md` | **版本变更历史**（v0.1.0~，从本文件拆出） |

> 三文件分工：`README.md`（有什么/怎么找）· `CHANGELOG.md`（改了什么）· `DECISION-LOG.md`（为什么改/下一步）。
