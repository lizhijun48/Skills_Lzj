#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""doc-insight 输出契约检查器

校验《资料深度解读》简报是否满足固定契约：六段落齐全、要素矩阵列名逐字一致、
每个要素带合法原文出处、枚举值不越界、行动建议非泛化。

用法：
    python scripts/check_brief.py <brief.md>
    python scripts/check_brief.py --help

退出码：
    0 = 全部必修项通过
    1 = 存在必修项不合规（详见逐条输出）
    2 = 用法或环境错误（参数缺失、文件不可读、编码异常）

契约权威源：references/output-contract.md（改契约须同步改本脚本，反之亦然）
"""

import os
import re
import sys

SECTIONS = [
    "## 0. 决策靶子",
    "## 1. 资料清点",
    "## 2. 红线清单",
    "## 3. 决策要素矩阵",
    "## 4. 矛盾清单",
    "## 5. 决策简报",
]

HEADER_COLS = ["编号", "维度", "要素", "原文出处", "确定性", "影响判断", "行动建议"]
SEP_CELL = "---"

DIMS = ["时间", "金额", "义务", "权限", "风险", "凭证", "口径"]
CERTAINTY = ["明确", "需澄清"]
IMPACT_PREFIX = ["支持", "阻碍", "中性"]

# 出处合法格式：页码 / 条文 / 章节 / 表格 / 纪要段落
CITE_PATTERNS = [
    re.compile(r"^p\d+(?:-\d+)?$"),
    re.compile(r"^第\d+条(?:第\d+款)?$"),
    re.compile(r"^§\d+(?:\.\d+)*$"),
    re.compile(r"^表\d+(?:-\d+)?$"),
    re.compile(r"^\d{4}-\d{2}-\d{2}#\d+$"),
]

# 泛化建议：整句等于其中之一即判不合格
BAD_ADVICE = {
    "建议关注", "待研究", "进一步确认", "加强管理", "注意风险",
    "持续跟进", "视情况处理", "关注", "待定", "无",
}

MIN_ADVICE_LEN = 4
CELL_SEP = "；"

USAGE = (
    "用法: python scripts/check_brief.py <brief.md>\n"
    "  校验资料深度解读简报是否符合输出契约（六段落 + 7 列要素矩阵 + 出处合法）。\n"
    "  退出码 0=通过 1=不合规 2=用法/环境错误\n"
)


def die_env(msg):
    """环境/用法错误 → EXIT 2"""
    sys.stderr.write("[ENV] %s\n" % msg)
    sys.stderr.write(USAGE)
    sys.exit(2)


def split_row(line):
    """把 | a | b | 拆成单元格列表（去首尾空段并 strip）"""
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    return [c.strip() for c in body.split("|")]


def read_lines(path):
    if not os.path.isfile(path):
        die_env("文件不存在: %s" % path)
    try:
        with open(path, "r", encoding="utf-8-sig") as fh:
            return fh.read().replace("\r\n", "\n").replace("\r", "\n").split("\n")
    except UnicodeDecodeError:
        die_env("文件不是合法 UTF-8 编码: %s" % path)
    except OSError as exc:
        die_env("文件不可读: %s (%s)" % (path, exc.__class__.__name__))


def find_matrix_block(lines):
    """返回 (起始行号, 段落内行列表)，起始行号为 1-based；找不到返回 (None, [])"""
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## 3. 决策要素矩阵":
            start_idx = i
            break
    if start_idx is None:
        return None, []
    block = []
    for j in range(start_idx + 1, len(lines)):
        stripped = lines[j].strip()
        if stripped.startswith("## "):
            break
        block.append((j + 1, lines[j]))
    return start_idx + 1, block


def check_citation(cell):
    """出处单元格是否合法（支持 ；分隔的多出处）"""
    parts = [p.strip() for p in cell.split(CELL_SEP) if p.strip()]
    if not parts:
        return False, "原文出处为空"
    for part in parts:
        if not any(pat.match(part) for pat in CITE_PATTERNS):
            return False, "原文出处格式非法: %s" % part
    return True, ""


def main(argv):
    if len(argv) != 2 or argv[1] in ("-h", "--help"):
        if len(argv) == 2 and argv[1] in ("-h", "--help"):
            sys.stdout.write(USAGE)
            sys.exit(0)
        die_env("需要且仅需要一个参数：简报文件路径")

    path = argv[1]
    lines = read_lines(path)

    errors = []
    notes = []

    # S1 六段落齐全
    for sec in SECTIONS:
        if not any(line.strip() == sec for line in lines):
            errors.append("S1 缺少段落标题（逐字）: %s" % sec)
    if not errors:
        print("[PASS] S1 六个段落标题齐全")

    # 定位矩阵
    sec_lineno, block = find_matrix_block(lines)
    if sec_lineno is None:
        errors.append("S2 未找到「## 3. 决策要素矩阵」段落，无法校验矩阵")
        report(errors, notes)
        return

    table_rows = [(ln, txt) for ln, txt in block if txt.strip().startswith("|")]
    if not table_rows:
        errors.append("S2 决策要素矩阵段落内没有表格")
        report(errors, notes)
        return

    # S2 表头逐字
    hdr_ln, hdr_txt = table_rows[0]
    hdr = split_row(hdr_txt)
    if hdr != HEADER_COLS:
        errors.append(
            "S2 表头不符（第 %d 行）：期望 %s，实际 %s"
            % (hdr_ln, " | ".join(HEADER_COLS), " | ".join(hdr))
        )
    else:
        print("[PASS] S2 表头 7 列逐字一致")

    # 分隔行
    data_start = 1
    if len(table_rows) > 1:
        sep = split_row(table_rows[1][1])
        if len(sep) != 7 or not all(c.strip("-:") == "" for c in sep):
            errors.append("S2 分隔行非法（第 %d 行），应为 7 段 ---" % table_rows[1][0])
        data_start = 2

    data_rows = table_rows[data_start:]
    if not data_rows:
        errors.append("S10 决策要素矩阵为空表（至少需要 1 行要素）")

    # 逐行校验
    ids = []
    used_dims = set()
    for ln, txt in data_rows:
        cells = split_row(txt)
        if len(cells) != 7:
            errors.append("S3 第 %d 行有 %d 列，应为 7 列" % (ln, len(cells)))
            continue
        num, dim, factor, cite, cert, impact, advice = cells

        if not re.match(r"^D-\d{2}$", num):
            errors.append("S4 第 %d 行编号非法: %s（应为 D-01 格式）" % (ln, num))
        else:
            ids.append(int(num[2:]))

        if dim not in DIMS:
            errors.append("S5 第 %d 行维度越界: %s（合法值 时间/金额/义务/权限/风险/凭证/口径）" % (ln, dim))
        else:
            used_dims.add(dim)

        if not factor or factor in ("-", "/", "同上", "详见上文"):
            errors.append("S3 第 %d 行要素为空或占位" % ln)

        cite_ok, cite_msg = check_citation(cite)
        if not cite_ok:
            errors.append("S6 第 %d 行 %s" % (ln, cite_msg))

        if cert not in CERTAINTY:
            errors.append("S7 第 %d 行确定性越界: %s（合法值 明确/需澄清）" % (ln, cert))

        if not any(impact.startswith(pre) for pre in IMPACT_PREFIX):
            errors.append("S8 第 %d 行影响判断未以 支持/阻碍/中性 开头: %s" % (ln, impact))

        adv = advice.strip()
        if not adv or adv in BAD_ADVICE:
            errors.append("S9 第 %d 行行动建议缺失或为泛化词: %s" % (ln, advice))
        elif len(adv) < MIN_ADVICE_LEN:
            errors.append("S9 第 %d 行行动建议过短（<%d 字）: %s" % (ln, MIN_ADVICE_LEN, advice))

    # S4 编号连续性
    if ids:
        expect = list(range(1, len(ids) + 1))
        if sorted(ids) != expect:
            errors.append("S4 编号不连续或有重号：实际 %s，期望 D-01..D-%02d"
                          % (["D-%02d" % i for i in sorted(ids)], len(ids)))

    # S11 维度覆盖提示（不影响退出码）
    missing_dims = [d for d in DIMS if d not in used_dims]
    if missing_dims:
        notes.append("S11 以下维度未出现要素，请确认是「本维无内容」还是漏提：%s"
                     % "/".join(missing_dims))

    report(errors, notes)


def report(errors, notes):
    for note in notes:
        print("[NOTE] %s" % note)
    if errors:
        for err in errors:
            print("[FAIL] %s" % err)
        print("结果：FAIL（%d 项必修不合规）" % len(errors))
        sys.exit(1)
    print("[PASS] S3-S10 逐行校验通过")
    print("结果：PASS（全部必修项通过）")
    sys.exit(0)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except SystemExit:
        raise
    except Exception as exc:  # 不裸露 traceback
        sys.stderr.write("[ENV] 检查器内部错误：%s\n" % exc.__class__.__name__)
        sys.exit(2)
