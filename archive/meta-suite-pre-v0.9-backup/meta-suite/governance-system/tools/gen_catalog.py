#!/usr/bin/env python3
"""
生成 SKILL-CATALOG.md — 技能全量目录
扫描所有 SKILL.md + 对照注册表，输出按 suite 分组的 markdown 表格

用法：
  python gen_catalog.py              # 生成到 skills/SKILL-CATALOG.md
  python gen_catalog.py --dry-run    # 仅打印统计不写文件
  python gen_catalog.py --output /path/to/output.md

修复记录（v2）：
- 修复 .workbuddy 路径过滤 bug（不再误杀所有文件）
- Windows 大小写去重（rglob SKILL.md + skill.md 合并为同一文件）
- 输出路径可配置（默认 skills/ 根目录）
"""

import os, re, sys, json, pathlib
from datetime import date

# ── 配置 ────────────────────────────────────────────────
SKILLS_ROOT = pathlib.Path(r"C:\Users\Lee\.workbuddy\skills")
REGISTRY_PATH = SKILLS_ROOT / "SKILL-ID-REGISTRY.md"
DEFAULT_OUTPUT = SKILLS_ROOT / "SKILL-CATALOG.md"

# 跳过的隐藏目录（只跳过 skills 内部的，不过滤根路径本身）
SKIP_DIRS = {".git", ".claude-plugin", ".claude", "__pycache__"}


# ── 1. 解析注册表 ──────────────────────────────────────
def parse_registry(path):
    """返回 {gid: {path, name, stage, status, note}}"""
    reg = {}
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    in_table = False
    for line in lines:
        ls = line.strip()
        if ls.startswith("| 编号 |"):
            in_table = True; continue
        if not in_table or not ls.startswith("|"):
            if in_table: in_table = False
            continue
        if re.match(r"^\|[\s\-]+\|", ls):
            continue
        cols = [c.strip() for c in ls.split("|")]
        if len(cols) < 6: continue
        gid = cols[1]
        sp = cols[2]
        if sp in ("", "（空）", "—", "-", "待分配"): continue
        reg[gid] = {
            "registry_path": sp,
            "name": cols[3],
            "stage": cols[4],
            "status": cols[5],
            "note": cols[6].strip() if len(cols) > 6 else "",
        }
    return reg


# ── 2. 解析 front-matter ──────────────────────────────────
def parse_fm(content):
    """解析 front-matter（含多行值），返回 dict"""
    ct = content.lstrip()
    if not ct.startswith("---"):
        return {"_has_fm": False}
    end = ct.find("---", 3)
    if end == -1:
        return {"_has_fm": False}
    block = ct[3:end]
    fm = {"_has_fm": True}
    lines = block.split("\n")
    ck, mm, ml = None, None, []
    for line in lines:
        ls = line.strip()
        if mm:
            if ls == "" or (ls and not ls.startswith(" ") and ":" in ls):
                fm[ck] = " ".join(ml).replace("\n", " ") if mm == ">" else "\n".join(ml)
                mm = None; ml = []; ck = None
                if ls and ":" in ls and not ls.startswith(" "): pass
                else: continue
            else: ml.append(ls); continue
        m = re.match(r"^(\w[\w\-]*):\s*(.*)", line)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if v.startswith('"') and v.endswith('"'): v = v[1:-1]
            elif v.startswith("'") and v.endswith("'"): v = v[1:-1]
            if v in (">", "|"): ck, mm, ml = k, v, []
            else: fm[k] = v; ck = k; mm = None
    if mm and ml:
        fm[ck] = " ".join(ml) if mm == ">" else "\n".join(ml)
    return fm


# ── 3. 推断 suite 分类 ──────────────────────────────────
SUITE_ORDER = ["product", "project", "meta", "industry", "economic",
               "legal", "reading", "general", "expert", "research", "standalone"]

SUITE_NAMES = {
    "product": "产品轨 (pd-suite)",
    "project": "项目轨 (pm-suite)",
    "meta": "元技能 (meta-suite)",
    "industry": "行业技能 (industry-suite)",
    "economic": "经济决策 (economic-suite)",
    "legal": "法律服务 (legal-suite)",
    "reading": "阅读操作系统 (reading-os)",
    "general": "通用技能 (general-suite)",
    "expert": "专家视角 (expert-suite)",
    "research": "研究技能 (research-suite)",
    "standalone": "独立部署",
}

def classify_suite(rel_path):
    p = rel_path.replace("\\", "/")
    for prefix, suite in [
        ("pd-suite/", "product"), ("pm-suite/", "project"),
        ("meta-suite/", "meta"), ("industry-suite/", "industry"),
        ("economic-suite/", "economic"), ("legal-suite/", "legal"),
        ("reading-os/", "reading"), ("general-suite/", "general"),
        ("expert-suite/", "expert"), ("research-suite/", "research"),
        ("inbox/", "inbox"),
    ]:
        if p.startswith(prefix):
            return suite
    return "standalone"


def extract_name(content, fm, dirname):
    name = fm.get("name", "")
    if name:
        return name
    m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    return m.group(1).strip() if m else dirname


def short_desc(desc, maxlen=50):
    if not desc:
        return ""
    s = desc.strip().replace("\n", " ")
    return s[:maxlen] + "..." if len(s) > maxlen else s


# ── 4. 扫描（修复：正确处理 .workbuddy 根路径） ─────────
def scan_skills(root):
    """扫描 root 下所有 SKILL.md，返回排序列表 [(path_obj, rel_path), ...]

    关键修复：
    - 只跳过 SKIP_DIRS 中的隐藏目录（如 .git），不误杀 .workbuddy 根路径
    - Windows 大小写不敏感：SKILL.md 和 skill视为同一文件
    """
    skill_files = list(root.rglob("SKILL.md")) + list(root.rglob("skill.md"))
    # 去重：Windows 大小写不敏感 → 用 lower() 做 key
    seen_lower = set()
    unique = []
    for p in skill_files:
        key = str(p).lower()
        if key in seen_lower:
            continue
        seen_lower.add(key)
        # 跳过隐藏目录内的文件
        if any(s in p.parts for s in SKIP_DIRS):
            continue
        unique.append(p)

    # 二次排序保证稳定
    unique.sort(key=lambda p: str(p))
    return unique


# ── 5. 主流程 ──────────────────────────────────────────
def main():
    dry_run = "--dry-run" in sys.argv
    out_path = DEFAULT_OUTPUT
    for i, a in enumerate(sys.argv):
        if a == "--output" and i + 1 < len(sys.argv):
            out_path = pathlib.Path(sys.argv[i + 1])

    print(f"Loading registry from {REGISTRY_PATH}...")
    registry = parse_registry(REGISTRY_PATH)
    path_to_gid = {info["registry_path"]: gid for gid, info in registry.items()}
    print(f"  Registry: {len(registry)} entries")

    print("Scanning SKILL.md files...")
    all_files = scan_skills(SKILLS_ROOT)
    print(f"  Found: {len(all_files)} files")

    rows = []  # (suite_order_idx, sort_key, suite, gid, name, rel_path, stage, status, desc)

    for fp in all_files:
        try:
            rel = str(fp.relative_to(SKILLS_ROOT)).replace("\\", "/")
        except ValueError:
            # 文件不在 SKILLS_ROOT 下（不应发生），跳过
            continue

        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()

        fm = parse_fm(content)
        gid = fm.get("governance_id", "")
        name = extract_name(content, fm, fp.parent.name)
        desc = fm.get("description", "")
        suite = classify_suite(rel)

        # 查注册表补充信息
        reg_info = None
        if gid and gid in registry:
            reg_info = registry[gid]
        elif not gid:
            dir_path = os.path.dirname(rel).replace("\\", "/")
            for rgid, ri in registry.items():
                if ri["registry_path"] == dir_path:
                    reg_info = ri
                    gid = rgid
                    break

        stage = reg_info["stage"] if reg_info else ("未治理" if suite != "inbox" else "-")
        status = reg_info["status"] if reg_info else ("未治理" if suite != "inbox" else "-")
        note = reg_info.get("note", "") if reg_info else ""

        sort_key = gid if gid else f"zzz_{suite}_{name}"
        suite_order = SUITE_ORDER.index(suite) if suite in SUITE_ORDER else 99
        rows.append((suite_order, sort_key, suite, gid or "—", name, rel, stage, status,
                     short_desc(desc, 60)))

    # 排序
    rows.sort(key=lambda r: (r[0], r[1]))

    # ── 输出 markdown ──
    today = date.today().isoformat()
    governed = sum(1 for r in rows if r[3] != "—")

    lines = []
    lines.append("# SKILL-CATALOG.md — 技能全量目录")
    lines.append("")
    lines.append(f"> 生成日期：{today} | 覆盖范围：所有 SKILL.md（含已治理和未治理）")
    lines.append("> **已治理编号以 `SKILL-ID-REGISTRY.md` 为准**，此目录作为全局检索补充。")
    lines.append("> **生成命令**：`python meta-suite/governance-system/tools/gen_catalog.py`")
    lines.append("")
    lines.append("| 编号 | 技能名 | 路径 | 阶段 | 状态 | 说明 |")
    lines.append("|------|--------|------|------|------|------|")

    current_suite = None
    for suite_order, sk, suite, gid, name, rel, stage, status, desc_short in rows:
        if suite != current_suite:
            current_suite = suite
            lines.append("")
            lines.append(f"### {SUITE_NAMES.get(suite, suite)}")
            lines.append("")
            lines.append("| 编号 | 技能名 | 路径 | 阶段 | 状态 | 说明 |")
            lines.append("|------|--------|------|------|------|------|")

        lines.append(f"| {gid} | {name} | `{rel}` | {stage} | {status} | {desc_short} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"**总计**：{len(rows)} 个 SKILL.md（含已治理 {governed} 个，未治理 {len(rows)-governed} 个）")

    content_out = "\n".join(lines) + "\n"

    if dry_run:
        print("\n--- DRY RUN OUTPUT ---")
        print(content_out[:2000])
        if len(content_out) > 2000:
            print(f"... (truncated, total {len(content_out)} chars)")
        print(f"\nTotal: {len(rows)} skills, governed: {governed}")
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content_out)
    print(f"\n✅ SKILL-CATALOG.md 已生成: {out_path}")
    print(f"   总计: {len(rows)} 个 SKILL.md, 已治理: {governed}, 未治理: {len(rows)-governed}")


if __name__ == "__main__":
    main()
