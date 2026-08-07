#!/usr/bin/env python3
"""
利率路径综合决策分析引擎
功能：基于终身EPV的多情景退保vs减额缴清决策分析 + HTML报告
"""
import sys, io, json, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from policy_epv_calc import calc_both_epv, qx, estimate_cv_at_age


# ============================================================
# Default policy data (override via CLI or modify directly)
# ============================================================
PERSON_A = {"name": "Person A", "age": 14, "cv": 7517, "prem": 4183,
            "rpu_death": 32739, "rpu_ci_total": 56200}
PERSON_B = {"name": "Person B", "age": 8, "cv": 5407, "prem": 3846,
            "rpu_death": 24422, "rpu_ci_total": 56200}

TOTAL_CV = PERSON_A["cv"] + PERSON_B["cv"]
TOTAL_PREM = PERSON_A["prem"] + PERSON_B["prem"]
POLICY_YEARS = 12
RPU_RESIDUAL = 4999

# ============================================================
# Interest rate paths (adjustable)
# ============================================================
RATE_PATHS = [
    {"id": "deep_low", "name": "深度低利率（日本化）", "prob": 0.15,
     "d_avg": 0.008, "r_avg": 0.015},
    {"id": "gradual_low", "name": "渐进低利率（基准）", "prob": 0.50,
     "d_avg": 0.015, "r_avg": 0.025},
    {"id": "stable_current", "name": "当前维持", "prob": 0.25,
     "d_avg": 0.020, "r_avg": 0.030},
    {"id": "moderate_recovery", "name": "温和回升", "prob": 0.10,
     "d_avg": 0.025, "r_avg": 0.035},
]

D_GRID = [0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04]
R_GRID = [0.015, 0.02, 0.025, 0.03, 0.035]


def calc_surrender_fv(r):
    """Calculate surrender scenario future value after 12 years."""
    cv_fv = TOTAL_CV * ((1 + r) ** POLICY_YEARS)
    saved_fv = 0
    for t in range(1, POLICY_YEARS + 1):
        saved_fv += TOTAL_PREM * ((1 + r) ** (POLICY_YEARS - t))
    return cv_fv + saved_fv, cv_fv, saved_fv


def calc_rpu_fv(r, d, mort_adj=0.80):
    """Calculate RPU scenario future value after 12 years."""
    epv_data = calc_both_epv(PERSON_A, PERSON_B, d, mort_adj)
    saved_fv = 0
    for t in range(1, POLICY_YEARS + 1):
        saved_fv += TOTAL_PREM * ((1 + r) ** (POLICY_YEARS - t))
    insurance_fv = epv_data["total_epv"] * ((1 + d) ** POLICY_YEARS)
    return saved_fv + RPU_RESIDUAL + insurance_fv, saved_fv, RPU_RESIDUAL, insurance_fv, epv_data


def run_path_analysis(mort_adj=0.80):
    """Analyze all interest rate paths."""
    results = []
    for path in RATE_PATHS:
        d, r = path["d_avg"], path["r_avg"]
        epv_data = calc_both_epv(PERSON_A, PERSON_B, d, mort_adj)
        surr_fv, cv_fv, _ = calc_surrender_fv(r)
        rpu_fv, _, _, ins_fv, _ = calc_rpu_fv(r, d, mort_adj)
        net = surr_fv - rpu_fv
        decision = "退保" if net > 2000 else ("减额缴清" if net < -2000 else "临界")
        results.append({**path, "d": d, "r": r,
            "epv_total": round(epv_data["total_epv"], 0),
            "epv_life": round(epv_data["life_epv"], 0),
            "epv_ci": round(epv_data["ci_epv"], 0),
            "surr_fv": round(surr_fv, 0), "rpu_fv": round(rpu_fv, 0),
            "net": round(net, 0), "cv_fv": round(cv_fv, 0),
            "ins_fv": round(ins_fv, 0), "decision": decision})
    return results


def run_matrix(mort_adj=0.80):
    """Build decision matrix: d x r grid."""
    matrix = []
    for d in D_GRID:
        row = []
        for r in R_GRID:
            _, cv_fv, _ = calc_surrender_fv(r)
            _, _, _, ins_fv, _ = calc_rpu_fv(r, d, mort_adj)
            net_core = cv_fv - RPU_RESIDUAL - ins_fv
            row.append(round(net_core, 0))
        epv = calc_both_epv(PERSON_A, PERSON_B, d, mort_adj)["total_epv"]
        matrix.append({"d": d, "row": row, "epv": round(epv, 0)})
    return matrix


def run_epv_sensitivity(mort_adj=0.80):
    """EPV sensitivity across discount rates."""
    results = []
    for d in [0.005, 0.008, 0.01, 0.012, 0.015, 0.02, 0.025, 0.03, 0.04]:
        epv = calc_both_epv(PERSON_A, PERSON_B, d, mort_adj)
        results.append({"d": d, "epv": epv, "ins_fv": round(epv["total_epv"] * ((1+d)**POLICY_YEARS), 0)})
    return results


def generate_html(path_results, matrix, epv_sens, output_path="rate_path_decision.html"):
    """Generate interactive HTML report."""
    pj = json.dumps([{k: v for k, v in p.items() if k not in ("d_avg","r_avg")}
                      for p in path_results])
    mj = json.dumps([{"d": m["d"], "row": m["row"], "epv": m["epv"]} for m in matrix])
    sj = json.dumps([{"d": s["d"], "life_epv": round(s["epv"]["life_epv"],0),
        "ci_epv": round(s["epv"]["ci_epv"],0),
        "total_epv": round(s["epv"]["total_epv"],0),
        "ins_fv": s["ins_fv"]} for s in epv_sens])
    dj = json.dumps([d*100 for d in D_GRID])
    rj = json.dumps([r*100 for r in R_GRID])

    js_data = ('<script>\nvar PATH_DATA = {:s};\nvar MATRIX_DATA = {:s};\n'
               'var SENS_DATA = {:s};\nvar D_GRID = {:s};\nvar R_GRID = {:s};\n</script>').format(pj, mj, sj, dj, rj)

    css = '''<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:#f7f8fa;color:#1a202c;line-height:1.6}
.container{max-width:1100px;margin:0 auto;padding:20px}
.header{background:linear-gradient(135deg,#1a365d,#2c5282,#3182ce);color:#fff;padding:40px 30px;border-radius:16px;margin-bottom:24px}
.header h1{font-size:28px;margin-bottom:8px}
.header .badge{display:inline-block;background:rgba(255,255,255,.2);padding:4px 12px;border-radius:12px;font-size:13px;margin:8px 4px 0 0}
.card{background:#fff;border-radius:12px;padding:28px;margin-bottom:20px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
.card h2{font-size:20px;margin-bottom:16px;color:#2c5282;border-bottom:2px solid #e2e8f0;padding-bottom:10px}
table{width:100%;border-collapse:collapse;margin:12px 0;font-size:14px}
th{background:#edf2f7;padding:10px 12px;text-align:left;font-weight:600;color:#4a5568;border-bottom:2px solid #cbd5e0}
td{padding:10px 12px;border-bottom:1px solid #e2e8f0}
tr:hover{background:#f7fafc}
.chart-wrap{position:relative;height:400px;margin:16px 0}
.red{color:#e53e3e}.green{color:#38a169}.amber{color:#dd6b20}
.tag{display:inline-block;padding:2px 8px;border-radius:6px;font-size:12px;font-weight:600}
.tag-surrender{background:#fed7d7;color:#c53030}
.tag-rpu{background:#c6f6d5;color:#276749}
.tag-borderline{background:#fefcbf;color:#975a16}
.note{background:#fffbeb;border-left:4px solid #d69e2e;padding:14px 18px;margin:16px 0;border-radius:0 8px 8px 0;font-size:14px}
.note-info{background:#ebf8ff;border-left-color:#3182ce}
.note-danger{background:#fff5f5;border-left-color:#e53e3e}
.grid-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
.path-card{border:2px solid #e2e8f0;border-radius:10px;padding:18px;text-align:center}
.path-card .prob{font-size:28px;font-weight:700;margin:4px 0}
.decision-banner{text-align:center;padding:24px;border-radius:12px;margin:16px 0}
.decision-banner.surrender{background:#fff5f5;border:2px solid #fc8181}
.decision-banner.rpu{background:#f0fff4;border:2px solid #68d391}
.footer{text-align:center;color:#a0aec0;font-size:13px;margin-top:32px;padding:16px}
</style>'''

    body = '''
<div class="container">
<div class="header">
  <h1>利率路径综合决策分析</h1>
  <div style="opacity:.9;font-size:15px">退保 vs 减额缴清 — 终身EPV修正版</div>
  <div style="margin-top:8px">
    <span class="badge">CLT2025生命表(-20%)</span>
    <span class="badge">终身人寿+CI EPV</span>
    <span class="badge">多路径敏感性分析</span>
  </div>
</div>

<div class="card">
  <h2>利率路径卡片</h2>
  <div class="grid-3" id="path-cards"></div>
  <div class="note note-info" style="margin-top:16px">
    <strong>核心逻辑：</strong>折现率d越低，未来保障的现值越高。利率走低时减额缴清更有利。
  </div>
</div>

<div class="card">
  <h2>路径对比表</h2>
  <table><thead><tr><th>路径</th><th>概率</th><th>d</th><th>r</th><th>终身EPV</th><th>退保FV</th><th>RPU_FV</th><th>净差</th><th>决策</th></tr></thead>
  <tbody id="path-table"></tbody></table>
  <div class="chart-wrap"><canvas id="pathChart"></canvas></div>
</div>

<div class="card">
  <h2>决策矩阵 (核心差异: CV投资 - 残值 - 保险FV)</h2>
  <p style="color:#718096;margin-bottom:12px">正值=退保有利，负值=减额缴清有利</p>
  <table id="decision-matrix"></table>
  <div class="note note-danger">
    <strong>关键修正：</strong>EPV必须计算终身而非保单剩余年限，否则会低估17倍以上。
  </div>
</div>

<div class="card">
  <h2>EPV对折现率的敏感度</h2>
  <table><thead><tr><th>折现率d</th><th>人寿EPV</th><th>CI EPV</th><th>总EPV</th><th>12年后FV</th></tr></thead>
  <tbody id="epv-table"></tbody></table>
  <div class="chart-wrap"><canvas id="epvChart"></canvas></div>
</div>

<div class="card">
  <h2>概率加权结论</h2>
  <div id="final-banner"></div>
</div>

<div class="footer">CLT2025生命表 | 中国NCI癌症数据 | 仅供参考</div>
</div>'''

    script = '''
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script>
(function(){
var pc = document.getElementById("path-cards");
PATH_DATA.forEach(function(p) {
    var dec = p.decision, tc = dec==="退保"?"tag-surrender":(dec==="减额缴清"?"tag-rpu":"tag-borderline");
    pc.innerHTML += '<div class="path-card"><div style="font-size:14px">' + p.name + '</div>' +
      '<div class="prob">' + (p.prob*100).toFixed(0) + '%</div>' +
      '<div style="font-size:13px">d=' + (p.d*100).toFixed(1) + '% r=' + (p.r*100).toFixed(1) + '%</div>' +
      '<div style="font-size:13px">净差 ' + (p.net>0?'+':'') + '\\u00a5' + p.net.toLocaleString() + '</div>' +
      '<div style="margin-top:6px"><span class="tag ' + tc + '">' + dec + '</span></div></div>';
});

var pt = document.getElementById("path-table");
PATH_DATA.forEach(function(p) {
    pt.innerHTML += '<tr><td>' + p.name + '</td><td>' + (p.prob*100).toFixed(0) + '%</td>' +
      '<td>' + (p.d*100).toFixed(1) + '%</td><td>' + (p.r*100).toFixed(1) + '%</td>' +
      '<td>\\u00a5' + p.epv_total.toLocaleString() + '</td>' +
      '<td>\\u00a5' + p.surr_fv.toLocaleString() + '</td>' +
      '<td>\\u00a5' + p.rpu_fv.toLocaleString() + '</td>' +
      '<td class="' + (p.net>0?'red':'green') + '">\\u00a5' + p.net.toLocaleString() + '</td>' +
      '<td><span class="tag ' + (p.decision==="退保"?"tag-surrender":"tag-rpu") + '">' + p.decision + '</span></td></tr>';
});

var dm = document.getElementById("decision-matrix");
var dmh = '<thead><tr><th>d \\u2193</th>';
R_GRID.forEach(function(r) { dmh += '<th>r=' + r.toFixed(1) + '%</th>'; });
dmh += '<th>EPV</th></tr></thead><tbody>';
MATRIX_DATA.forEach(function(m) {
    dmh += '<tr><td style="font-weight:700">d=' + (m.d*100).toFixed(1) + '%</td>';
    m.row.forEach(function(v) {
        var cls = v > 2000 ? 'red' : (v < -2000 ? 'green' : 'amber');
        dmh += '<td class="' + cls + '">\\u00a5' + v.toLocaleString() + '</td>';
    });
    dmh += '<td>\\u00a5' + m.epv.toLocaleString() + '</td></tr>';
});
dm.innerHTML = dmh + '</tbody>';

var et = document.getElementById("epv-table");
SENS_DATA.forEach(function(s) {
    et.innerHTML += '<tr><td>' + (s.d*100).toFixed(1) + '%</td>' +
      '<td>\\u00a5' + s.life_epv.toLocaleString() + '</td>' +
      '<td>\\u00a5' + s.ci_epv.toLocaleString() + '</td>' +
      '<td>\\u00a5' + s.total_epv.toLocaleString() + '</td>' +
      '<td>\\u00a5' + s.ins_fv.toLocaleString() + '</td></tr>';
});

var pw = PATH_DATA.reduce(function(s,p){return s + p.prob * p.net;},0);
var fb = document.getElementById("final-banner");
fb.innerHTML = '<div class="decision-banner ' + (pw < 0 ? 'rpu' : 'surrender') + '">' +
  '<div style="font-size:24px;font-weight:700;margin-bottom:8px">概率加权净优势: \\u00a5' + Math.abs(Math.round(pw)).toLocaleString() + '</div>' +
  '<div style="font-size:14px;color:#4a5568">' + (pw < 0 ? '\\u2705 减额缴清更有利' : '\\u274c 退保更有利') + '</div></div>';

new Chart(document.getElementById("pathChart"),{
    type:"bar",
    data:{labels:PATH_DATA.map(function(p){return p.name;}),
        datasets:[
            {label:"退保FV",data:PATH_DATA.map(function(p){return p.surr_fv;}),backgroundColor:"#fc8181"},
            {label:"RPU_FV",data:PATH_DATA.map(function(p){return p.rpu_fv;}),backgroundColor:"#68d391"}
        ]},
    options:{responsive:true,maintainAspectRatio:false,
        plugins:{legend:{position:"bottom"}},
        scales:{y:{ticks:{callback:function(v){return "\\u00a5"+(v/1000).toFixed(0)+"k";}}}}}
});

new Chart(document.getElementById("epvChart"),{
    type:"line",
    data:{labels:SENS_DATA.map(function(s){return (s.d*100).toFixed(1)+"%";}),
        datasets:[
            {label:"人寿EPV",data:SENS_DATA.map(function(s){return s.life_epv;}),borderColor:"#3182ce",tension:.3,fill:false},
            {label:"CI EPV",data:SENS_DATA.map(function(s){return s.ci_epv;}),borderColor:"#dd6b20",tension:.3,fill:false},
            {label:"总EPV",data:SENS_DATA.map(function(s){return s.total_epv;}),borderColor:"#38a169",tension:.3,fill:false,borderWidth:3}
        ]},
    options:{responsive:true,maintainAspectRatio:false,
        plugins:{legend:{position:"bottom"}},
        scales:{y:{ticks:{callback:function(v){return "\\u00a5"+(v/1000).toFixed(0)+"k";}}}}}
});
})();
</script>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n')
        f.write(css)
        f.write('\n</head>\n<body>\n')
        f.write(body)
        f.write('\n')
        f.write(js_data)
        f.write('\n')
        f.write(script)
        f.write('\n</body>\n</html>')
    return output_path


def main(output="rate_path_decision.html", mort_adj=0.80):
    print("=" * 70)
    print("  利率路径综合决策分析")
    print("=" * 70)

    path_results = run_path_analysis(mort_adj)
    matrix = run_matrix(mort_adj)
    epv_sens = run_epv_sensitivity(mort_adj)

    print("\n--- 路径结果 ---")
    for p in path_results:
        print(f"  {p['name']}: d={p['d']*100:.1f}% r={p['r']*100:.1f}% "
              f"EPV={p['epv_total']:,.0f} 净差={p['net']:+,.0f} -> {p['decision']}")

    pw = sum(p["prob"] * p["net"] for p in path_results)
    print(f"\n  概率加权净优势: {pw:+,.0f}")

    print(f"\n--- 决策矩阵 ---")
    print(f"{'d':>6}", end="")
    for r in R_GRID:
        print(f"  r={r*100:4.1f}%", end="")
    print()
    for m in matrix:
        print(f"d={m['d']*100:4.1f}%", end="")
        for v in m["row"]:
            s = "退" if v > 2000 else ("减" if v < -2000 else "~")
            print(f" {v:+,.0f}{s}", end="")
        print(f"  [EPV={m['epv']:,.0f}]")

    html_path = generate_html(path_results, matrix, epv_sens, output)
    print(f"\n  HTML报告: {html_path}")

    return path_results, matrix, epv_sens


if __name__ == "__main__":
    main()
