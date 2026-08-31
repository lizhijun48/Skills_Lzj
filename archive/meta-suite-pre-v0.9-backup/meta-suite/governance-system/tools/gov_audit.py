#!/usr/bin/env python3
"""
体系级治理审计 — 按 GOV_SkillGovernance.md v3.2 质量门禁 QG1-QG13
聚焦可机械化验证的项目。

用法：
  python gov_audit.py                    # 审计并输出报告到 audit/ 目录
  python gov_audit.py --output /path     # 自定义输出路径
  python gov_audit.py --verbose          # 打印详细过程

对应规则基准：GOV §9（每条检查标注来源门禁）

修复记录（v2）：
- QG9 排除 checklist [ ] 和示例标签 [功能X] 假阳性
- 新增 QG7/QG10/QG12 检查项
- 输出路径可配置
"""

import os, re, sys, json, pathlib
from datetime import date

# ── 配置 ────────────────────────────────────────────────
SKILLS_ROOT = pathlib.Path(r"C:\Users\Lee\.workbuddy\skills")
REGISTRY_PATH = SKILLS_ROOT / "SKILL-ID-REGISTRY.md"
BFM_PATH = SKILLS_ROOT / "BUSINESS-FLOW-MAP.md"
PT_PATH = SKILLS_ROOT / "pd-suite" / "pd-workflow-chains" / "SKILL.md"
JT_PATH = SKILLS_ROOT / "pm-suite" / "pm-workflow-chains" / "SKILL.md"
CATALOG_PATH = SKILLS_ROOT / "SKILL-CATALOG.md"
GOV_PATH = SKILLS_ROOT / "GOV_SkillGovernance.md"
DEFAULT_OUTPUT = SKILLS_ROOT / "meta-suite" / "governance-system" / "GOVERNANCE_AUDIT_LATEST.md"

SKIP_DIRS = {".git", ".claude-plugin", ".claude", "__pycache__"}

# 已知例外（不会导致审计失败的合法模式）
KNOWN_CHECKLIST_PREFIXES = {"- [ ]", "- [x]", "- [X]", "* [ ]", "* [x]"}
KNOWN_EXAMPLE_PATTERNS = {"[功能X]", "[功能Y]", "[功能Z]", "[请填写]", "[示例]"}


def parse_fm(content):
    ct = content.lstrip()
    if not ct.startswith("---"):
        return {}
    end = ct.find("---", 3)
    if end == -1:
        return {}
    block = ct[3:end]
    fm = {}
    ck, mm, ml = None, None, []
    for line in block.split("\n"):
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


def scan_skills(root):
    """扫描 root 下所有 SKILL.md（大小写归一去重）"""
    skill_files = list(root.rglob("SKILL.md")) + list(root.rglob("skill.md"))
    seen_lower = set()
    unique = []
    for p in skill_files:
        key = str(p).lower()
        if key in seen_lower:
            continue
        seen_lower.add(key)
        if any(s in p.parts for s in SKIP_DIRS):
            continue
        unique.append(p)
    unique.sort(key=lambda p: str(p))
    return unique


def read_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def main():
    verbose = "--verbose" in sys.argv
    out_path = DEFAULT_OUTPUT
    for i, a in enumerate(sys.argv):
        if a == "--output" and i + 1 < len(sys.argv):
            out_path = pathlib.Path(sys.argv[i + 1])
    dry_run = "--dry-run" in sys.argv

    today = date.today().isoformat()

    print("=== GOV 治理审计 ===")
    print(f"依据: GOV_SkillGovernance.md v3.2")
    print(f"日期: {today}")

    # ── 扫描 ──
    all_files = scan_skills(SKILLS_ROOT)
    skills = {}
    for fp in all_files:
        rel = str(fp.relative_to(SKILLS_ROOT)).replace("\\", "/", )
        with open(fp, "r", encoding="utf-8") as f:
            content = f.read()
        fm = parse_fm(content)
        skills[rel] = {"fm": fm, "abs": str(fp), "content": content}

    print(f"扫描完成: {len(skills)} 个 SKILL.md")

    # 读全局表
    registry = read_file(REGISTRY_PATH)
    bfm = read_file(BFM_PATH)
    ptc = read_file(PT_PATH)
    jtc = read_file(JT_PATH)
    catalog = read_file(CATALOG_PATH)
    gov = read_file(GOV_PATH)

    results = []

    # ════════════════════════════════════════
    # QG4: 触发词唯一性（§9 规则基准 · 对应 GOV QG4）
    # ════════════════════════════════════════
    if verbose: print("[QG4] Check triggers uniqueness...")
    gid_triggers = {}
    for rel, info in skills.items():
        fm = info["fm"]
        gid = fm.get("governance_id", "")
        triggers_raw = fm.get("triggers", [])
        # 处理 triggers 可能是字符串或列表
        if isinstance(triggers_raw, str):
            triggers = [t.strip() for t in triggers_raw.split(",") if t.strip()] if triggers_raw else []
        elif isinstance(triggers_raw, list):
            triggers = triggers_raw
        else:
            triggers = []
        if gid and triggers:
            track = gid.split("-")[0] if "-" in gid else "X"
            gid_triggers[gid] = {"track": track, "triggers": set(triggers), "rel": rel}

    qg4_conflicts = []
    checked_pairs = 0
    for gid1, info1 in gid_triggers.items():
        for gid2, info2 in gid_triggers.items():
            if gid1 >= gid2: continue
            checked_pairs += 1
            if info1["track"] != info2["track"]: continue
            overlap = info1["triggers"] & info2["triggers"]
            if overlap:
                qg4_conflicts.append((gid1, gid2, overlap, info1["track"]))

    if qg4_conflicts:
        results.append(f"### QG4: 触发词唯一性 🔴 发现 {len(qg4_conflicts)} 组冲突")
        for g1, g2, ov, t in sorted(qg4_conflicts):
            results.append(f"- **{t}**: `{g1}` ↔ `{g2}` 共用触发词: {ov}")
    else:
        results.append("### QG4: 触发词唯一性 ✅ 通过（同 Track 内无冲突，检查 {checked_pairs} 对）")

    # ════════════════════════════════════════
    # QG9: 占位符残留（§9 规则基准 · 排除 checklist 和示例标签）
    # ════════════════════════════════════════
    if verbose: print("[QG9] Check placeholders (excluding checklists)...")
    real_placeholders = []
    for rel, info in skills.items():
        c = info["content"]
        for m in re.finditer(r"\[[^\]]{2,20}\]", c):
            txt = m.group()
            # 排除 checklist
            if any(txt.startswith(p) for p in KNOWN_CHECKLIST_PREFIXES):
                continue
            # 排除示例模板标签
            if txt in KNOWN_EXAMPLE_PATTERNS:
                continue
            real_placeholders.append((rel, txt))

    if real_placeholders:
        results.append(f"### QG9: 可操作交付 🟡 发现 {len(real_placeholders)} 处疑似占位符")
        for rel, txt in real_placeholders[:10]:
            results.append(f"- `{rel}`: `{txt}`")
        if len(real_placeholders) > 10:
            results.append(f"  ...共 {len(real_placeholders)} 处")
    else:
        results.append("### QG9: 可操作交付 ✅ 通过（无残留占位符）")

    # ════════════════════════════════════════
    # QG13: 4 张全局表一致性（§8 联动检查）
    # ════════════════════════════════════════
    if verbose: print("[QG13] Check 4-table consistency...")
    jt19_in_reg = "JT-019" in registry
    jt19_in_bfm = "JT-019" in bfm
    jt19_in_jtc = "pm-tender-analysis" in jtc
    qg13_pass = jt19_in_reg and jt19_in_bfm and jt19_in_jtc

    results.append(f"### QG13: 治理联动一致性 {'✅ 通过' if qg13_pass else '🔴 需修复'}")
    results.append(f"- JT-019 在注册表: {'✅' if jt19_in_reg else '❌'}")
    results.append(f"- JT-019 在路由表: {'✅' if jt19_in_bfm else '❌'}")
    results.append(f"- pm-tender-analysis 在 JT 链路: {'✅' if jt19_in_jtc else '❌'}")

    catalog_skill_count = catalog.count("| `") if catalog else 0
    diff = abs(catalog_skill_count - len(skills))
    results.append(f"- Catalog 列数({catalog_skill_count}) vs 扫描数({len(skills)): 差异={diff} {'✅' if diff < 5 else '⚠️ 需重新运行 gen_catalog.py'}")

    # ════════════════════════════════════════
    # QG1: 同 Track+Phase 密度
    # ════════════════════════════════════════
    if verbose: print("[QG1] Check functional density...")
    phase_matches = re.findall(r"\| (PT-\d+|JT-\d+|S-\d+)\s+\|\s+\S+\s+\|\s+(\S+)\s+\|", registry)
    tp_groups = {}
    for gid, phase in phase_matches:
        track = gid.split("-")[0]
        tp_groups.setdefault(f"{track}+{phase}", []).append(gid)
    high_density = {k: g for k, g in tp_groups.items() if len(g) > 4}
    if high_density:
        results.append(f"### QG1: 同轨同阶段密度 🟡 {len(high_density)} 组需人工确认")
        for k, g in high_density.items():
            results.append(f"- {k}: {len(g)} 个 {g[:5]}...")
    else:
        results.append("### QG1: 同轨同阶段密度 ✅ 无明显密集风险")

    # ════════════════════════════════════════
    # QG7: 方法论一致性（粗检：同 Sub-position 知识源冲突标记）
    # ════════════════════════════════════════
    if verbose: print("[QG7] Quick methodology check...")
    # 收集有明确知识源的技能
    ks_conflicts = []  # 此版本仅做标记，不做深度分析
    results.append("### QG7: 方法论一致性 ℹ️ 需人工深检时调用 qg7_analysis.py")
    results.append("  (本脚本做粗粒度标记；完整分析见 `tools/qg7_analysis.py`)")

    # ════════════════════════════════════════
    # QG10: 动态反馈闭环（投标类技能复盘机制）
    # ════════════════════════════════════════
    if verbose: print("[QG10] Check bid review mechanism...")
    bid_keywords = ["复盘", "回溯", "中标后", "未中标后", "对手画像", "博弈系数"]
    bid_skills = ["pm-bid-proposal", "pm-tender-analysis", "pm-risk-management"]
    qg10_status = "✅ 通过"
    qg10_detail = []
    for bs in bid_skills:
        for rel in skills:
            if bs in rel:
                content = skills[rel]["content"]
                found = sum(1 for kw in bid_keywords if kw in content)
                qg10_detail.append(f"- `{rel}`: 复盘关键词命中 {found}/{len(bid_keywords)}")
                if found < 2:
                    qg10_status = "🟡 关注"
    results.append(f"### QG10: 动态反馈闭环 {qg10_status}")
    for d in qg10_detail:
        results.append(d)

    # ════════════════════════════════════════
    # QG12: 概率风险评估（投标/报价类技能）
    # ════════════════════════════════════════
    if verbose: print("[QG12] Check probabilistic analysis...")
    prob_keywords = ["概率", "蒙特卡洛", "分布", "置信区间", "模拟", "贝叶斯"]
    qg12_status = "✅ 通过"
    qg12_detail = []
    for bs in bid_skills:
        for rel in skills:
            if bs in rel:
                content = skills[rel]["content"]
                found = sum(1 for kw in prob_keywords if kw in content)
                qg12_detail.append(f"- `{rel}`: 概率关键词命中 {found}/{len(prob_keywords)}")
                if found < 1 and "bid" in rel:
                    qg12_status = "🟡 关注"
    results.append(f"### QG12: 概率风险评估 {qg12_status}")
    for d in qg12_detail:
        results.append(d)

    # ════════════════════════════════════════
    # 汇总输出
    # ════════════════════════════════════════
    governed_count = sum(1 for rel, info in skills.items() if info["fm"].get("governance_id"))

    lines = []
    lines.append("# 体系级治理审计报告")
    lines.append("")
    lines.append(f"> 日期: {today} | 依据: GOV_SkillGovernance.md v3.2 (§9 规则基准)")
    lines.append(f"> 覆盖: {len(skills)} 个 SKILL.md | 已治理: {governed_count} | 工具: gov_audit.py v2")
    lines.append("")
    lines.append("## 1. 审计摘要")
    lines.append("")
    lines.append("| 门禁 | 状态 | 说明 | 对应 §9 规则 |")
    lines.append("|------|------|------|-------------|")

    summary = [
        ("QG1", "🟡 关注" if high_density else "✅ 通过", f"{len(high_density)} 组高密度" if high_density else "无明显风险", "密度>4 标记"),
        ("QG4", "🔴 需修复" if qg4_conflicts else "✅ 通过", f"{len(qg4_conflicts)} 组冲突" if qg4_conflicts else "无冲突", "同 Track 交集=空"),
        ("QG7", "ℹ️ 需深检", "调用 qg7_analysis.py", "知识源交叉对比"),
        ("QG9", "🟡 关注" if real_placeholders else "✅ 通过", f"{len(real_placeholders)} 处" if real_placeholders else "无残留", "排除 checklist + 示例"),
        ("QG10", qg10_status, "投标类复盘关键词命中", "复盘/回溯/对手画像"),
        ("QG12", qg12_status, "投标类概率关键词命中", "蒙特卡洛/分布/置信"),
        ("QG13", "✅ 通过" if qg13_pass else "🔴 需修复", "4 表一致性", "§8 联动表清单"),
    ]
    for qg, status, desc, rule in summary:
        lines.append(f"| {qg} | {status} | {desc} | {rule} |")

    lines.append("")
    lines.append("## 2. 详细检查结果")
    lines.append("")
    for r in results:
        lines.append(r)

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 3. 审计结论与建议")
    lines.append("")
    has_p0 = bool(qg4_conflicts) or not qg13_pass
    if has_p0:
        lines.append("🔴 **存在 P0 缺项，须立即修复后再交付。**")
    else:
        lines.append("✅ **无 P0 阻塞项，体系整体健康。**")

    content_out = "\n".join(lines) + "\n"

    if dry_run:
        print("\n--- DRY RUN ---")
        print(content_out[:2000])
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content_out)
    print(f"\n✅ 审计报告已保存: {out_path}")


if __name__ == "__main__":
    main()
