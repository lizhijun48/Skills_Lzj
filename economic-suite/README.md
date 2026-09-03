# economic-suite/ 经济决策工具

> 经济决策计算工具套件，编号前缀 `E-`。覆盖 NPV/IRR/回收期/敏感性/方案比选/价值工程等量化决策工具，由 `economic-decision` 元技能统一调度。

## 技能清单

| 编号 | 技能 | 阶段 | 职责 |
|------|------|------|------|
| E-001 | economic-npv | CX | 净现值（NPV）计算工具 |
| E-002 | economic-irr | CX | 内部收益率（IRR）计算工具 |
| E-003 | economic-sensitivity | CX | 敏感性分析工具（单变量扰动/BEP/Tornado） |
| E-004 | economic-comparison | CX | 方案比选工具 |
| E-005 | economic-ve | CX | 价值工程（VE）工具 |
| E-006 | economic-payback | CX | 投资回收期计算工具（静态/动态） |
| E-007 | economic-decision | CX | 经济决策顾问（元技能，自动调度 E-001~006） |

## 与 market-suite 的分工

| 套件 | 前缀 | 职责 |
|------|------|------|
| economic-suite | E- | DCF / 时间价值计算（NPV/IRR/回收期） |
| market-suite | MT- | 市场倍数与隐含估值基准（可比公司对标） |

两者上下游协作：MT- 提供行业倍数与隐含估值，E- 做现金流与时间价值计算。

---

**更新日期**：2026-09-03（依据 SKILL-ID-REGISTRY v1.5.6 生成）
