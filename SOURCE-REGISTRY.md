# SOURCE-REGISTRY.md — 外部来源引入登记表

> 建立日期：2026-09-04（应复盘需求建立：按"来源视角"记录引入过哪些外部文件、对哪些技能做了融入与优化）。
> 定位：全局第四表，与 `SKILL-ID-REGISTRY`（编号）/ `SKILL-CATALOG`（目录）/ `BUSINESS-FLOW-MAP`（流程）并列。
> 四记录分工：`README.md`（有什么/怎么找）· `CHANGELOG.md`（何时改了什么，时间视角）· `DECISION-LOG.md`（为什么改/下一步）· **本表（借鉴了什么、流向哪里，来源视角）**。
> 维护规则：凡"引入外部文件喂养技能"的动作，**登记一行并入当次 commit**；纯内部修改不登记。版本细节不在此重复，只放锚点（CHANGELOG 版本号 + commit），复盘时按锚点回查 CHANGELOG。

---

## 登记表

| 源ID | 来源文件 | 类型 | 引入日期 | 版本锚点 | 流向技能 | 融入方式 | 复盘备注 |
|------|----------|------|----------|----------|----------|----------|----------|
| SRC-001 | `DeepSeek-R1从入门到精通_清华.pdf`（本机：`D:\00_Lee\00-Tool\AI_Tools\DeepSeek\`，库外） | PDF | 2026-08-09 | v0.2.0 / `175fced`（主锚）+ v0.1.x | **S-026~S-031**（6个，SKILL.md 声明"基于清华《DeepSeek：从入门到精通》提炼"）+ **S-034~S-039**（6个，v0.2.0 新建）；代表作：S-027「提示语链七大作用机制」、S-028「元叙事提示框架」、S-030「幻觉五类七特」 | 补强 3 + 新建 6（17 files, +3738 行，详见 CHANGELOG v0.2.0） | 体系性融入共 12 技能，是技能库最早的成建制引入；AI辅助编程+文案营销+品牌战略三线均源于此 |
| SRC-002 | `《DeepSeek 使AI变得简单》`（Yash Jain 著，刘彦辰 译） | 书籍 | 2026-08-11 | v0.6.0 | S-029 reasoning-model-strategy v1.2→v1.3（多模型协同三模式 + 专用AI vs 通用AI决策框架）；原始素材存档 `general-suite/reasoning-model-strategy/references/source-material-deepseek.md`（第2/9章） | 补强 + 素材存档 | 全书约 70% 内容与已有 Skills 重叠（提示工程基础、故障排除等），仅提取 2 个增量知识点——重叠度判定先于融入，避免重复建设 |
| SRC-003 | `AI辅助编程与内容创作培训材料`（课程配套资料） | 培训材料 | 2026-08-09~10 | v0.1.0~v0.5.0（各技能建立期） | 6 个技能的素材存档：`ai-content-quality`（三重概率模型）、`channel-content-strategy`（四平台知识库）、`human-ai-collaboration`（能力体系）、`prompt-chain-design`（六步法）、`prompt-engineering-basics`（TASTE/ALIGN框架）、`structured-report-writing`（年终总结提示语） | 素材存档 + 新建技能 | 素材文件位于各技能 `references/source-material*.md`（共 6 份），溯源粒度到技能级；与 SRC-001 同期、来源可能同源（课程材料含清华 PDF），未精确区分 |

---

## 登记统计

- 已登记来源：3 份外部文件/材料组，累计流向 18 个技能（含重复计入：SRC-001 的 12 + SRC-002 的 1 + SRC-003 的 6，去重后约 15 个）
- 待补录：无（2026-09-04 起新引入即时登记）

## 登记操作约定

1. 新引入：在登记表按源ID顺序追加一行，源ID = 上一个 +1（SRC-004 起）
2. 同一来源二次利用（再次融入其他技能）：不新增行，在原行"流向技能"列追加并更新版本锚点
3. 提交：登记改动并入当次功能 commit；若单独登记，message 用 `docs(sources): 登记 SRC-xxx <来源名>`
