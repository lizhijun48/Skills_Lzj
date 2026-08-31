# 三文件瘦身 v2 — 待办 / 问题回溯清单（升级文件）

> 作用：跨三个技能的**待办项 + 已知问题 + 联网接口保留声明**统一记账，便于回溯。
> 制定：2026-09-01 | 关联：legal-suite/law-repository（已建，commit e6aade3）、各技能 SLIMMING-V2.md
> 用户三要求：① 业务可执行 + 联网接口原样不动 ② 三技能全拆解、联网留最后、待办入本文件 ③ 蒸馏数据换地方但逻辑不变、更新按新规则、框架先搭、固定数据后续补

---

## 一、联网接口保留清单（一律原样不动，仅备注）

| # | 技能 | 接口/源 | 位置 | 状态 | 备注 |
|---|---|---|---|---|---|
| N1 | law-skills | flk.npc.gov.cn 国家法律法规数据库 API | A7 节 | ⚠️ **已改版失效**（2026-08-31 实测：GET 返回 SPA HTML / POST 405） | 保留原描述不动；备注「待官方恢复或寻替代源」；内建知识库兜底 |
| N2 | gridman | fgk.chinatax.gov.cn 国家税务总局法规库 | 税务时效性规则 | 在线 | 原样保留 |
| N3 | gridman | docs.maoyanqing.com（MaoDocs 审计文库） | 法规原文查询源 | 在线（外部站点，有失效风险） | 原样保留；备注「依赖外部站点，纳入可用性监控」 |
| N4 | gridman | law.esnai.cn 中国会计视野法规库 | 使用规则 6 | 在线 | 原样保留 |
| N5 | gridman | szse.cn / sse.com.cn / bse.cn 交易所规则 | 法规原文查询源 | 在线 | 原样保留 |
| N6 | gridman | report_download（巨潮接口，无需 Key） | MCP 工具层 | 在线 | 原样保留 |
| N7 | gridman | MinerU 云端 API（document_ocr，需用户 Token） | document_ocr 配置 | 在线（需用户凭证） | 原样保留 |

**规则**：所有联网部分（N1~N7）在瘦身改造中**保持原样**，不重写、不"优化"、不删除。任何失效/风险只在本文档标注，不动运行逻辑。

---

## 二、已知问题（待后续升级处理）

| # | 技能 | 问题 | 影响 | 处理建议 | 状态 |
|---|---|---|---|---|---|
| P1 | law-skills | A7 节吹「flk API 实时查询」但 API 已失效 | 描述失真，误导用户 | 加「2026-08-31 实测失效，暂以内建库+law-repository 兜底」注记 | 待改（Step1 执行） |
| P2 | law-skills | `def # 读取.md模板描述(...)` 函数名含 `#` 语法错误 | 通用诉状填充代码不可运行 | 注释残留，改为 `def _decrypt_template(...)` | 待改（Step1 执行） |
| P3 | law-skills | A3/A9 内嵌大量民商法条文（民法典/劳动合同法等）| 体积大且与 law-repository 重叠 | 待 law-repository 补民商法后下沉引用 | 阻塞于待补 |
| P4 | pm-bid-proposal | 第零~八步含冗余法规要点（与 law-repository 4 部已入库重叠）| 体积偏大 | 法规依据表改为引 law-repository，保留发改委55号令引用（待补库） | 待执行 |
| P5 | gridman | SKILL.md 含大量角色 IP 设定（古立特宇宙/声优/圆谷 Trigger）| 原则十要求通用化 | 人设可识别部分通用化，原版归档留溯源 | 待裁决 |
| P6 | gridman | MaoDocs 为外部站点，URL/结构可能变动 | 原文核实链路脆弱 | 备注监控；优先以 law-repository（财税类后续补）兜底 | 观察中 |

---

## 三、待补数据（框架已搭，固定内容后续获取）

| # | 内容 | 落入 | 阻塞项 | 优先级 |
|---|---|---|---|---|
| D1 | 民法典（合同/物权/侵权/婚姻/继承编） | law-repository | 联网核验通道受限（flk 失效） | P0 |
| D2 | 保险法 | law-repository | 同上 | P1（两孩保单分析用） |
| D3 | 最高法建设工程施工合同司法解释（一） | law-repository | 同上 | P2 |
| D4 | 发改委 55 号令（2007） | law-repository | 同上 | P2（pm-bid-proposal 引用） |
| D5 | 财税类准则/税法原文（CAS/增值税/企税等） | 评估是否入 law-repository 或 gridman references | 领域不同，先评估边界 | P3 |

**框架原则**：law-repository 骨架已就位、更新规程已定（六条）。D1~D4 入库后即可解除 P3/P4 的阻塞，执行「蒸馏下沉」。

---

## 四、执行状态

- [x] 法规库骨架 + 4 部招投标法入库（e6aade3）
- [x] 三技能实况读取与拆解方案产出（law-skills / pm-bid-proposal / gridman 各 SLIMMING-V2.md）
- [ ] 联网部分（N1~N7）一律未改动 ✅
- [ ] 三技能 SKILL.md 实际瘦身（待用户裁决各方案后执行）
- [ ] D1~D4 待补数据入库（网络恢复后）
