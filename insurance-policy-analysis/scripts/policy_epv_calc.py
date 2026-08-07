#!/usr/bin/env python3
"""
保单精算EPV计算引擎
核心功能：基于CLT生命表计算人寿保险+重疾的终身期望现值(EPV)
"""
import math, json, argparse


# ============================================================
# CL1(2010-2013) 男性生命表 qx/1000，从0到105岁
# ============================================================
CL1_MALE = {
    0: 0.867, 1: 0.661, 2: 0.478, 3: 0.357, 4: 0.276,
    5: 0.219, 6: 0.177, 7: 0.145, 8: 0.121, 9: 0.103,
    10: 0.090, 11: 0.082, 12: 0.080, 13: 0.083, 14: 0.091,
    15: 0.101, 16: 0.113, 17: 0.126, 18: 0.138, 19: 0.149,
    20: 0.159, 21: 0.168, 22: 0.176, 23: 0.184, 24: 0.190,
    25: 0.196, 26: 0.201, 27: 0.207, 28: 0.213, 29: 0.220,
    30: 0.229, 31: 0.240, 32: 0.254, 33: 0.271, 34: 0.291,
    35: 0.316, 36: 0.345, 37: 0.379, 38: 0.418, 39: 0.462,
    40: 0.512, 41: 0.568, 42: 0.631, 43: 0.701, 44: 0.779,
    45: 0.867, 46: 0.965, 47: 1.076, 48: 1.202, 49: 1.345,
    50: 1.509, 51: 1.698, 52: 1.917, 53: 2.172, 54: 2.468,
    55: 2.807, 56: 3.192, 57: 3.626, 58: 4.112, 59: 4.654,
    60: 5.256, 61: 5.923, 62: 6.662, 63: 7.481, 64: 8.389,
    65: 9.397, 66: 10.517, 67: 11.763, 68: 13.151, 69: 14.698,
    70: 16.425, 71: 18.355, 72: 20.513, 73: 22.928, 74: 25.631,
    75: 28.658, 76: 32.046, 77: 35.838, 78: 40.080, 79: 44.823,
    80: 50.124, 81: 56.044, 82: 62.651, 83: 70.017, 84: 78.220,
    85: 87.345, 86: 97.485, 87: 108.740, 88: 121.218, 89: 135.036,
    90: 150.319, 91: 167.199, 92: 185.815, 93: 206.311, 94: 228.837,
    95: 253.546, 96: 280.594, 97: 310.138, 98: 342.334, 99: 377.337,
    100: 415.300, 101: 456.373, 102: 500.701, 103: 548.425, 104: 599.680,
    105: 1000.000,
}
MAX_AGE = 105


def qx(age, mort_adj=1.0):
    """Get mortality rate for given age, with optional adjustment factor."""
    return CL1_MALE.get(age, 1.0) / 1000.0 * mort_adj


def estimate_cv_at_age(current_age, current_cv, target_age, growth=0.035):
    """Estimate cash value growth before age 18 (pre-adult, CV grows at ~3.5%)."""
    years = target_age - current_age
    if years <= 0:
        return current_cv
    return current_cv * ((1 + growth) ** years)


def calc_life_epv(age, rpu_death, current_cv, discount, mort_adj=0.80):
    """
    Calculate lifetime life insurance EPV.
    
    Uses full mortality table from current age to MAX_AGE (105).
    CRITICAL: This is LIFETIME EPV, not truncated to policy years.
    Before age 18, death benefit is the accumulated cash value (civil law limit).
    After age 18, death benefit is the RPU face amount.
    """
    epv = 0.0
    surv = 1.0
    for a in range(age, MAX_AGE + 1):
        y = a - age
        disc = 1.0 / ((1 + discount) ** y)
        q = qx(a, mort_adj)
        death_prob = surv * q
        benefit = estimate_cv_at_age(age, current_cv, a) if a < 18 else rpu_death
        epv += death_prob * benefit * disc
        surv *= (1 - q)
    return epv


def calc_ci_epv(age, rpu_ci_total, discount, mort_adj=0.80):
    """
    Calculate critical illness insurance EPV.
    
    Uses age-stratified CI incidence rates from China NCI:
    - 0-18: 12/100,000 (pediatric)
    - 18-40: 30/100,000 (young adult) 
    - 40-60: 120/100,000 (middle age)
    - 60-75: 300/100,000 (senior)
    
    Match rate (proportion of all cancers that meet policy CI definition): 65-70%
    """
    stages = [
        (0, 18, 12.0 / 100000, 0.65),
        (18, 40, 30.0 / 100000, 0.65),
        (40, 60, 120.0 / 100000, 0.70),
        (60, 75, 300.0 / 100000, 0.70),
    ]
    epv = 0.0
    surv = 1.0
    for s, e, inc, match in stages:
        if age >= e:
            continue
        eff_s = max(age, s)
        for a in range(eff_s, e):
            y = a - age
            disc = 1.0 / ((1 + discount) ** y)
            claim_p = surv * inc * match
            epv += claim_p * rpu_ci_total * disc
            surv *= (1 - qx(a, mort_adj))
    return epv


def calc_both_epv(person_a, person_b, discount, mort_adj=0.80):
    """
    Calculate combined EPV for two insured persons.
    
    Args:
        person_a: dict with keys age, rpu_death, rpu_ci_total, cv
        person_b: same structure
        discount: annual discount rate (e.g. 0.03 for 3%)
        mort_adj: mortality adjustment factor (0.80 = CLT2025, 20% lower than CL1)
    
    Returns:
        dict with life_epv, ci_epv, total_epv
    """
    a_life = calc_life_epv(person_a["age"], person_a["rpu_death"],
                            person_a["cv"], discount, mort_adj)
    b_life = calc_life_epv(person_b["age"], person_b["rpu_death"],
                            person_b["cv"], discount, mort_adj)
    a_ci = calc_ci_epv(person_a["age"], person_a["rpu_ci_total"],
                        discount, mort_adj)
    b_ci = calc_ci_epv(person_b["age"], person_b["rpu_ci_total"],
                        discount, mort_adj)
    return {
        "life_epv": a_life + b_life,
        "ci_epv": a_ci + b_ci,
        "total_epv": a_life + b_life + a_ci + b_ci,
        "person_a": {"life": round(a_life, 0), "ci": round(a_ci, 0)},
        "person_b": {"life": round(b_life, 0), "ci": round(b_ci, 0)},
    }


def sensitivity_analysis(person_a, person_b, d_range=None, mort_adj=0.80):
    """Run EPV sensitivity across a range of discount rates."""
    if d_range is None:
        d_range = [0.005, 0.008, 0.01, 0.012, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04]
    results = []
    for d in d_range:
        epv = calc_both_epv(person_a, person_b, d, mort_adj)
        results.append({"d": d, "epv": epv})
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Insurance Policy EPV Calculator")
    parser.add_argument("--a-age", type=int, default=14, help="Person A current age")
    parser.add_argument("--a-death", type=float, default=32739, help="Person A RPU death benefit")
    parser.add_argument("--a-ci", type=float, default=56200, help="Person A RPU CI total")
    parser.add_argument("--a-cv", type=float, default=7517, help="Person A current cash value")
    parser.add_argument("--b-age", type=int, default=8, help="Person B current age")
    parser.add_argument("--b-death", type=float, default=24422, help="Person B RPU death benefit")
    parser.add_argument("--b-ci", type=float, default=56200, help="Person B RPU CI total")
    parser.add_argument("--b-cv", type=float, default=5407, help="Person B current cash value")
    parser.add_argument("--discount", type=float, default=0.03, help="Discount rate")
    parser.add_argument("--mort-adj", type=float, default=0.80, help="Mortality adjustment")
    parser.add_argument("--sensitivity", action="store_true", help="Run sensitivity analysis")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    person_a = {"age": args.a_age, "rpu_death": args.a_death,
                 "rpu_ci_total": args.a_ci, "cv": args.a_cv}
    person_b = {"age": args.b_age, "rpu_death": args.b_death,
                 "rpu_ci_total": args.b_ci, "cv": args.b_cv}

    if args.sensitivity:
        results = sensitivity_analysis(person_a, person_b, mort_adj=args.mort_adj)
        if args.json:
            print(json.dumps(results, indent=2, ensure_ascii=False))
        else:
            for r in results:
                epv = r["epv"]
                print(f"d={r['d']*100:.1f}%: Life={epv['life_epv']:,.0f} CI={epv['ci_epv']:,.0f} Total={epv['total_epv']:,.0f}")
    else:
        epv = calc_both_epv(person_a, person_b, args.discount, args.mort_adj)
        if args.json:
            print(json.dumps(epv, indent=2, ensure_ascii=False))
        else:
            print(f"Discount rate: {args.discount*100:.1f}%, Mortality adj: {args.mort_adj}")
            print(f"Life EPV: {epv['life_epv']:,.0f}")
            print(f"CI EPV: {epv['ci_epv']:,.0f}")
            print(f"Total EPV: {epv['total_epv']:,.0f}")
            print(f"  Person A: Life={epv['person_a']['life']:,.0f} CI={epv['person_a']['ci']:,.0f}")
            print(f"  Person B: Life={epv['person_b']['life']:,.0f} CI={epv['person_b']['ci']:,.0f}")
