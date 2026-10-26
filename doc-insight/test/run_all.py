#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""doc-insight 契约检查器回归套件

设计原则（对齐收敛关卡纪律）：按「坏法」而非按「字段」组织用例。
每种坏法一条规则、一个夹具变异；新增同义写法只需在同一格里加断言，不改判据。

用法：
    python test/run_all.py

退出码：
    0 = 全部用例符合预期
    1 = 有用例不符合预期
    2 = 环境错误
"""

import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CHECKER = os.path.join(os.path.dirname(HERE), "scripts", "check_brief.py")

BASE = """# 示例简报

## 0. 决策靶子

- 决策问题：本次变更是否批准
- 决策时点：2026-04-10
- 决策人：业主项目办
- 已知立场：倾向批准

## 1. 资料清点

| 文件 | 类型 | 版本 | 范围 |
|---|---|---|---|
| 变更申请单 | 单据 | V1 | p1-4 |
| 监理月报 | 月报 | 第12期 | p1-18 |

- 缺口：缺预算调整批复 → 无法判断超概算与否 → 可能导致结算核减

## 2. 红线清单

未发现一票否决项。扫描依据：核对变更申请单 p1-4 的时限与罚则表述。

## 3. 决策要素矩阵

| 编号 | 维度 | 要素 | 原文出处 | 确定性 | 影响判断 | 行动建议 |
|---|---|---|---|---|---|---|
| D-01 | 时间 | 变更申请于 03-20 提交，在 14 日有效期内 | p2 | 明确 | 支持 程序合规 | 由资料员归档受理回执 |
| D-02 | 金额 | 变更增加 86 万元，超原合同 8% | 第12条第2款 | 明确 | 阻碍 触发重新报批 | 由造价岗出具超概算测算表 |
| D-03 | 凭证 | 变更单缺监理签认 | 2026-03-20#2 | 需澄清 | 阻碍 不能作为结算依据 | 由监理于本周例会补签认 |

## 4. 矛盾清单

| 类型 | 冲突内容 | 以谁为准 | 谁去确认 |
|---|---|---|---|
| 资料间 | 申请单金额与月报金额差 3 万 | 以申请单为准 | 造价岗 |

## 5. 决策简报

**结论倾向**：建议补充签认后批准。

| 动作 | 归口 | 完成判据 | 时限 |
|---|---|---|---|
| 补监理签认 | 监理 | 3 份签认齐备 | 04-03 |

**待澄清清单**
1. 超概算是否需重新报批
"""


def _drop_last_section(text):
    idx = text.find("## 5. 决策简报")
    return text[:idx]


def _empty_matrix(text):
    start = text.find("## 3. 决策要素矩阵")
    end = text.find("## 4. 矛盾清单")
    head = (
        "## 3. 决策要素矩阵\n\n"
        "| 编号 | 维度 | 要素 | 原文出处 | 确定性 | 影响判断 | 行动建议 |\n"
        "|---|---|---|---|---|---|---|\n\n"
    )
    return text[:start] + head + text[end:]


def _renumber_skip(text):
    return text.replace("| D-02 |", "| D-05 |")


CASES = [
    ("good_base", None, 0, "合格基线，应通过"),
    ("S1_missing_section", _drop_last_section, 1, "缺第5段"),
    ("S2_header_rename", lambda s: s.replace("| 维度 |", "| 分类 |"), 1, "表头列名被改"),
    ("S4_number_skip", _renumber_skip, 1, "编号跳号 D-01/D-05"),
    ("S5_dim_out_of_range", lambda s: s.replace("| 金额 |", "| 合同 |"), 1, "维度越界"),
    ("S6_bad_citation", lambda s: s.replace("| p2 |", "| 相关资料 |"), 1, "出处非法"),
    ("S7_bad_certainty", lambda s: s.replace("| 明确 |", "| 待定 |", 1), 1, "确定性越界"),
    ("S8_bad_impact", lambda s: s.replace("支持 程序合规", "重要 程序合规"), 1, "影响判断无枚举前缀"),
    ("S9_generic_advice", lambda s: s.replace("由资料员归档受理回执", "建议关注"), 1, "泛化建议"),
    ("S10_empty_matrix", _empty_matrix, 1, "矩阵空表"),
]


def run_one(name, mutator, expect, desc):
    text = BASE if mutator is None else mutator(BASE)
    if mutator is not None and text == BASE:
        print("[FAIL] %-20s 变异未生效（替换未命中），用例本身失效：%s" % (name, desc))
        return False
    fd, tmp = tempfile.mkstemp(suffix=".md", prefix="docinsight_")
    os.close(fd)
    try:
        with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        proc = subprocess.run(
            [sys.executable, CHECKER, tmp],
            capture_output=True,
        )
        got = proc.returncode
        out = (proc.stdout + proc.stderr).decode("utf-8", "replace").strip()
        ok = got == expect
        print("[%s] %-20s 期望 EXIT %d，实际 %d ｜ %s"
              % ("PASS" if ok else "FAIL", name, expect, got, desc))
        if not ok:
            for line in out.split("\n")[:6]:
                print("         > %s" % line)
        return ok
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass


def main():
    if not os.path.isfile(CHECKER):
        sys.stderr.write("[ENV] 找不到检查器: %s\n" % CHECKER)
        return 2
    print("检查器: %s" % CHECKER)
    print("用例数: %d\n" % len(CASES))
    results = [run_one(*case) for case in CASES]
    passed = sum(1 for r in results if r)
    print("\n结果: %d/%d 通过" % (passed, len(results)))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:
        sys.stderr.write("[ENV] 回归套件内部错误：%s\n" % exc.__class__.__name__)
        sys.exit(2)
