# legal-suite/ 法律服务

> 法律服务套件，编号前缀 `L-`。覆盖法律咨询、合同审查、知识产权、合规，并承载**中央法规库 law-repository**（数据基础设施，不占编号）。

## 技能清单

| 编号 | 技能 | 阶段 | 职责 |
|------|------|------|------|
| L-001 | law-skills | CX | 法律咨询与要素式/通用起诉状起草（法条来源=中央法规库） |
| L-002 | contract-review | CX | 合同审查（类型选择/风险条款/合规/争议解决） |
| L-003 | ip-protection | CX | 知识产权保护（IP类型/归属/侵权/开源协议） |
| L-004 | legal-compliance-bundle | CX | 中国法律合规技能包（50 子技能） |

## 数据基础设施（不占编号）

| 组件 | 说明 |
|------|------|
| `law-repository/` | **中央法规库**——法律内容单一事实来源（SSOT）。三层架构：L1 原文（laws/，含司法解释原文）/ L2 领域解读 / L3 案例引用 + registry 反向登记。入口 `law-manifest.md`，数据源策略与转正流程见其 `README.md` |
| `law-repository-sop/`（用户级） | 法规库三层架构建设 SOP（跨套件可复用） |

> 法规库是原文 SSOT：行业技能（pm-bid-proposal / contract-review 等）蒸馏数据引用库原文 + 溯源（正向），缺口反向登记（registry/reverse-registry.md）。

## 与其他套件协作

| 方向 | 说明 |
|------|------|
| → pm-suite | 招投标/采购调用 contract-review + 法规库 |
| → 通用咨询 | 劳动法/保险法等入库文件支撑独立咨询 |

---

**更新日期**：2026-09-03（依据 SKILL-ID-REGISTRY v1.5.6 生成）
