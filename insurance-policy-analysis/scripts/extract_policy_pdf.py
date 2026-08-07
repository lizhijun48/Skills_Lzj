#!/usr/bin/env python3
"""
保险合同 PDF 数据提取工具
Extract key data points from Chinese insurance policy PDFs:
- Policy number, effective date, insured person details
- Annual premium (from policy front page)
- Cash value table (逐险种)
- Reduced paid-up (RPU) table (逐险种)
- Rider list
"""

import sys, re, json, argparse
from pathlib import Path

try:
    import fitz  # pymupdf
except ImportError:
    print("ERROR: pymupdf not installed. Run: pip install pymupdf")
    sys.exit(1)


def extract_text(pdf_path):
    """Extract full text from PDF."""
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text


def extract_policy_info(text):
    """Extract policy metadata from front page."""
    info = {}

    # Contract number
    m = re.search(r'合同[号編]号[：:]\s*([\w\d]+)', text)
    if m:
        info['contract_no'] = m.group(1)

    # Effective date
    m = re.search(r'生效日期[：:]\s*(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日', text)
    if m:
        info['effective_date'] = f"{m.group(1)}-{m.group(2).zfill(2)}-{m.group(3).zfill(2)}"

    # Insured person
    m = re.search(r'被保险人[：:]\s*(\S+)', text)
    if m:
        info['insured'] = m.group(1)

    # Policyholder
    m = re.search(r'投保人[：:]\s*(\S+)', text)
    if m:
        info['policyholder'] = m.group(1)

    # Annual premium - primary source
    m = re.search(r'首期保险费[合计]*[（(]年[交缴][）)]\s*[：:]*.*?RMB\s*[\d,]+\.?\d*', text)
    if m:
        digits = re.search(r'RMB\s*([\d,]+\.?\d*)', m.group())
        if digits:
            info['annual_premium'] = float(digits.group(1).replace(',', ''))

    # Payment years
    m = re.search(r'交[费費]年[限期][：:]\s*(\d+)', text)
    if m:
        info['payment_years'] = int(m.group(1))

    return info


def extract_riders(text):
    """Extract rider list from policy text."""
    riders = []
    # Look for rider section - typically after main policy and before "本栏以下空白"
    rider_pattern = re.compile(
        r'(附加\S+?保险\S*?)\s*[（(](\w+)[）)]\s*.*?(?:保险费|保费).*?RMB\s*([\d,]+\.?\d*)',
        re.DOTALL
    )
    for m in rider_pattern.finditer(text):
        riders.append({
            'name': m.group(1).strip(),
            'code': m.group(2),
            'premium': float(m.group(3).replace(',', ''))
        })

    # Also try alternate format
    alt_pattern = re.compile(
        r'(意外\S+?|住院\S+?|豁免\S+?)\s*[（(](\w+)[）)].*?([\d,]+\.?\d*)',
        re.DOTALL
    )
    for m in alt_pattern.finditer(text):
        name = m.group(1).strip()
        if not any(r['name'] == name for r in riders):
            riders.append({
                'name': name,
                'code': m.group(2),
                'premium': float(m.group(3).replace(',', ''))
            })

    return riders


def extract_cv_table(text):
    """Extract cash value and RPU tables.

    Returns dict: {policy_year: {risk_type: {'cv': float, 'rpu': float}}}
    Chinese insurance policies typically have CV and RPU tables side-by-side.
    """
    result = {}

    # Strategy: find all numbers near "现金价值" headers and group them
    # CV and RPU tables share the same policy year column

    # Look for section headers
    cv_section = re.search(r'现金价值[表与和]减额[交缴]清', text)
    if not cv_section:
        cv_section = re.search(r'现金价值表', text)
    if not cv_section:
        return result

    # Extract the section after the header
    start = cv_section.start()

    # Find risk type labels near the table
    risk_types = []
    type_pattern = re.compile(
        r'(平安\S*?终身寿险|附加\S*?重疾\S*?|附加\S*?定期寿险\S*?|附加\S*?恶性肿瘤\S*?|豁免\S+)'
    )
    for m in type_pattern.finditer(text, start, start + 3000):
        risk_types.append(m.group(1))

    if not risk_types:
        # Fallback: generic risk types
        risk_types = ['主险', '重疾', '定寿', '恶性肿瘤']

    # Try to parse numbers near each risk type header
    # Format is typically: 保单年度 | CV | RPU | CV | RPU | ...
    for i, risk in enumerate(risk_types):
        # Find the table block for this risk
        risk_pos = text.find(risk, start)
        if risk_pos < 0:
            continue

        block = text[risk_pos:risk_pos + 2000]
        # Extract numbers: pairs of (year, cv, rpu) or (cv, rpu)
        numbers = re.findall(r'([\d,]+\.?\d*)', block)

        year = 1
        for j in range(0, len(numbers) - 1, 2):
            if year not in result:
                result[year] = {}
            try:
                cv_val = float(numbers[j].replace(',', ''))
                rpu_val = float(numbers[j+1].replace(',', '')) if j+1 < len(numbers) else 0
                result[year][risk] = {'cv': cv_val, 'rpu': rpu_val}
            except (ValueError, IndexError):
                pass
            year += 1

    return result


def main():
    parser = argparse.ArgumentParser(description='Extract data from insurance policy PDF')
    parser.add_argument('pdf_path', help='Path to policy PDF file')
    parser.add_argument('--output', '-o', help='Output text file path')
    parser.add_argument('--json', '-j', action='store_true', help='Output structured JSON')
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        print(f"ERROR: File not found: {pdf_path}")
        sys.exit(1)

    text = extract_text(str(pdf_path))

    # Save full text
    if args.output:
        out_path = Path(args.output)
    else:
        out_path = pdf_path.with_suffix('.txt')
    out_path.write_text(text, encoding='utf-8')
    print(f"Full text saved to: {out_path}")

    # Extract structured data
    info = extract_policy_info(text)
    riders = extract_riders(text)
    cv_data = extract_cv_table(text)

    if args.json:
        output = {
            'policy_info': info,
            'riders': riders,
            'cv_rpu_table': {str(k): v for k, v in cv_data.items()}
        }
        json_path = out_path.with_suffix('.json')
        json_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"Structured data saved to: {json_path}")
    else:
        print("\n--- Policy Info ---")
        for k, v in info.items():
            print(f"  {k}: {v}")
        print(f"\n--- Riders ({len(riders)}) ---")
        for r in riders:
            print(f"  {r['name']} ({r['code']}): ¥{r['premium']}/年")
        print(f"\n--- CV/RPU Table: {len(cv_data)} policy years ---")
        for year in sorted(cv_data.keys())[:10]:
            print(f"  Year {year}: {cv_data[year]}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
