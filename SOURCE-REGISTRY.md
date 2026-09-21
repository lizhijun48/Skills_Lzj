# SOURCE-REGISTRY.md — 外部来源引入登记表

> 建立日期：2026-09-04（应复盘需求建立：按"来源视角"记录引入过哪些外部文件、对哪些技能做了融入与优化）。
> 定位：全局第四表，与 `SKILL-ID-REGISTRY`（编号）/ `SKILL-CATALOG`（目录）/ `BUSINESS-FLOW-MAP`（流程）并列。
> 四记录分工：`README.md`（有什么/怎么找）· `CHANGELOG.md`（何时改了什么，时间视角）· `DECISION-LOG.md`（为什么改/下一步）· **本表（借鉴了什么、流向哪里，来源视角）**。
> 维护规则：凡"引入外部文件喂养技能"的动作，**登记一行并入当次 commit**；纯内部修改不登记。版本细节不在此重复，只放锚点（CHANGELOG 版本号 + commit），复盘时按锚点回查 CHANGELOG。
> **2026-09-21 起新增前置门禁（GOV v3.7 原则十一）**：引入前须按 **S-072**（`external-source-eval-sop`）完成 8 镜头评估，结论存入本文件「引入评估记录」节，**未过评不得登记入库**——先过评，后登记。

---

## 登记表

| 源ID | 来源文件 | 类型 | 引入日期 | 版本锚点 | 流向技能 | 融入方式 | 复盘备注 |
|------|----------|------|----------|----------|----------|----------|----------|
| SRC-001 | `DeepSeek-R1从入门到精通_清华.pdf`（本机：`D:\00_Lee\00-Tool\AI_Tools\DeepSeek\`，库外） | PDF | 2026-08-09 | v0.2.0 / `175fced`（主锚）+ v0.1.x | **S-026~S-031**（6个，SKILL.md 声明"基于清华《DeepSeek：从入门到精通》提炼"）+ **S-034~S-039**（6个，v0.2.0 新建）；代表作：S-027「提示语链七大作用机制」、S-028「元叙事提示框架」、S-030「幻觉五类七特」 | 补强 3 + 新建 6（17 files, +3738 行，详见 CHANGELOG v0.2.0） | 体系性融入共 12 技能，是技能库最早的成建制引入；AI辅助编程+文案营销+品牌战略三线均源于此 |
| SRC-002 | `《DeepSeek 使AI变得简单》`（Yash Jain 著，刘彦辰 译） | 书籍 | 2026-08-11 | v0.6.0 | S-029 reasoning-model-strategy v1.2→v1.3（多模型协同三模式 + 专用AI vs 通用AI决策框架）；原始素材存档 `general-suite/reasoning-model-strategy/references/source-material-deepseek.md`（第2/9章） | 补强 + 素材存档 | 全书约 70% 内容与已有 Skills 重叠（提示工程基础、故障排除等），仅提取 2 个增量知识点——重叠度判定先于融入，避免重复建设 |
| SRC-003 | `AI辅助编程与内容创作培训材料`（课程配套资料） | 培训材料 | 2026-08-09~10 | v0.1.0~v0.5.0（各技能建立期） | 6 个技能的素材存档：`ai-content-quality`（三重概率模型）、`channel-content-strategy`（四平台知识库）、`human-ai-collaboration`（能力体系）、`prompt-chain-design`（六步法）、`prompt-engineering-basics`（TASTE/ALIGN框架）、`structured-report-writing`（年终总结提示语） | 素材存档 + 新建技能 | 素材文件位于各技能 `references/source-material*.md`（共 6 份），溯源粒度到技能级；与 SRC-001 同期、来源可能同源（课程材料含清华 PDF），未精确区分 |
| SRC-004 | `product-management-expert`（CodeBuddy Teams PM 插件；本机源：`C:\Users\Alex_Lee\WorkBuddy\2026-09-21-20-56-17\product-management-expert-source\`，库外） | 插件/专家包 | 2026-09-21 | v1.6.6（JT-021 建包完成） | **新建** `pm-product-expert` 专家包（agent+rules+workflow 路由，归入 pm-suite）；**补强** pd-prd-writing / pd-product-strategy / pd-user-research / pd-market-research / pd-tools-metrics / pm-stakeholder-management（注入 G/Y/R、ROAM、ADR、RICE 触发、机会规模估算、赢/输分析、Dashboard 原则等模板）；原版归档 `_external-archive/product-management-expert-source/` | 融合吸收（原则九）：6/7 技能与现有 pd/pm/market 套件高度重叠，未另起孤立技能；仅新增专家包外壳 + 差异化模板库；通用化命名（去 CodeBuddy 标识）；叠加 S-070 去 AI 味 | fork SRC-004，原版归档溯源；专家包已建（JT-021 生效；路由表路径全改写指向融合技能 PT-007/PT-001/PT-005/JT-015/PT-012/PT-003/MT-001，防断链）；融合评估溯源文档 `product-management-expert-分析评估.md`（JT-021 建包前的差距/可借鉴点/融合判定分析）已一并归档至 `_external-archive/product-management-expert-source/` |

---

## 引入评估记录（S-072 多视角评估）

> 2026-09-21 起，外部来源引入须按 **GOV v3.7 原则十一 + S-072** 执行 8 镜头评估，结论存档本节（对齐 S-072 §五 第 6 步）。SRC-001~003 为评估机制建立前的历史引入，不做追溯补评；**SRC-004 做回头看复评**，用于验证镜头可用性。

### SRC-004 回头看复评（2026-09-21 · S-072 首次实战）

**复评缘起**：原评估（归档于 `_external-archive/product-management-expert-source/product-management-expert-分析评估.md`）自述视角为"对照我方差距与可借鉴点"，属**单一吸收视角**；用 S-072 的 8 镜头补齐客观评估。

| 镜头 | 判定 | 关键证据 / 说明 |
|------|:----:|-----------------|
| ① 技术正确性 | ⚠️ 待核实 | 吸收的 ROAM（SAFe 风险管理）、ADR（架构决策记录）、RICE（优先级评分）均有业界出处；但**"机会规模 = 用户数 × 频次 × 严重度"仅属启发式估算，非标准公式**，原评估未作标注即注入 pd-tools-metrics / pd-prd-writing。引入时未做独立核验，本次复评亦未完成逐条联网核验 → 列跟踪项 |
| ② 外部基准 | ⚠️ 部分 | 隐式基准存在（我方 pd-suite 基于 NPDP，可作对照），但插件特有的 RICE / ROAM / 机会规模未与同类 PM 框架体系交叉验证；原"写得好 10 点 / 不足 10 点"为**单样本判断**，结论信心须降级 |
| ③ 融合二阶风险 | ❌ 有条件 | **本次最大发现**：JT-021 已入编号注册表与目录，但 `BUSINESS-FLOW-MAP.md` / `pd-workflow-chains/SKILL.md` / `pm-workflow-chains/SKILL.md` **三张路由表均未挂接**（全文检索 `JT-021` 皆 0 命中）。GOV §8 要求同步 4 张表，实际只同步 1 张 → 典型**可发现性债**，直接命中"后续用到有得查、而不是一抹黑"的痛点。另：6 个技能注入段的耦合，已由"路径全改写指向真实技能 ID"纪律部分对冲 |
| ④ 使用者价值 | ✅ 过评 | PRD 撰写 / 干系人沟通 / 优先级排序 / 竞品分析 / 指标看板均为产品经理高频刚需，场景明确、频次高、缺失有实质影响 |
| ⑤ 生命周期 TCO | ✅ 过评 | 永久 fork，上游更新不合并，维护主体=用户本人，废弃成本有界（路径已改写为真实技能 ID，包体移除后仅 6 处注入段需清理）。5 个 references 模板建议明确维护责任人 |
| ⑥ 来源与许可 | ⚠️ 待核实 | CodeBuddy Teams marketplace 插件，作者不可核验、许可条款未核验。缓释：仅本地个人使用、不分发，商用再分发风险低；原版仅本地归档。后续同类引入须前置查许可 |
| ⑦ 战略契合 | ✅ 过评（优先） | 直接服务**产品经理轨**主线，并经 pm-stakeholder-management（JT-015）与 ADR 触及项目经理轨交叉——完全符合"PM + PM 双轨知识库"战略主线 |
| ⑧ 治理自反 | ❌ 发现盲点 | 见下 |

**结论**：**有条件过评** —— 条件为 ①⑥ 标待核实并补标注、③ 联动表补挂。

**镜头⑧ 治理自反发现（3 条）**：

1. **规则无缺口、执行有漏项**：GOV §8 已明确列出 4 张联动表，但缺"纳管后逐表打勾"的复核动作 → 已在 S-072 §五补第 7 步（4 表打勾自检）
2. **引入动作此前无门禁**：GOV v3.6 仅有原则十（外部技能通用化，拆分时触发，属**事后**措施），**没有任何引入前置评估要求**；QG1~QG13 均为技能质量门，非来源准入门 → 由**原则十一**填补
3. **原则八覆盖"修改"、不覆盖"引入"**：新增条目此前落在原则八范围之外 → 原则十一明确覆盖"引入"动作

**跟踪项**：

- **T-002**（DECISION-LOG）：JT-021 联动表补同步 3 张，待用户确认其在双链中的定位后执行
- ①：机会规模估算须在 pd-tools-metrics / pd-prd-writing 显式标注"启发式，非标准公式"
- ⑥：marketplace 插件许可条款核实

---

## 登记统计

- 已登记来源：4 份外部文件/材料组（SRC-001~004），累计流向约 25 个技能（SRC-001 的 12 + SRC-002 的 1 + SRC-003 的 6 + SRC-004 已建 1 + 6 补强）
- 待补录：无（2026-09-04 起新引入即时登记）

## 登记操作约定

1. 新引入：在登记表按源ID顺序追加一行，源ID = 上一个 +1（SRC-004 起）
2. 同一来源二次利用（再次融入其他技能）：不新增行，在原行"流向技能"列追加并更新版本锚点
3. 提交：登记改动并入当次功能 commit；若单独登记，message 用 `docs(sources): 登记 SRC-xxx <来源名>`
