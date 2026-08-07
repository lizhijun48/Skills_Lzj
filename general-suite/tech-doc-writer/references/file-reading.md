# 参考文档读取指南

## 核心原则：优先复用已有的专门 skill

读取 docx / xlsx / pptx / pdf 这类专业格式时，**第一步永远是检查当前环境是否已经安装了对应的专门 skill**。如果有，直接委托给它们；没有时才用下面内嵌的 Python 应急脚本。

### 检查方式

扫一下 `available_skills` 列表（或对应目录），看是否存在以下 skill：

| 文件类型 | 首选 skill | Fallback（本文件后面的脚本） |
|---------|-----------|-------------------------|
| `.pdf`（读取为主） | `pdf-reading` | pdfplumber / pymupdf |
| `.pdf`（创建 / 填表 / 合并） | `pdf` | pypdf |
| `.docx` | `docx` | python-docx |
| `.xlsx` / `.xls` / `.csv` | `xlsx` | openpyxl / pandas |
| `.pptx` | `pptx` | python-pptx |
| `.md` | 无需 skill | `view` 工具直接读 |

Skill 在不同环境里的位置：
- **claude.ai**：`/mnt/skills/public/<skill-name>/SKILL.md`
- **Claude Code**（全局）：`~/.claude/skills/<skill-name>/SKILL.md`
- **Claude Code**（项目级）：`<项目>/.claude/skills/<skill-name>/SKILL.md`

### 调用方式

1. 用 `view` 工具读取目标 skill 的 `SKILL.md`
2. 按它的指引执行（这些专门 skill 通常有成熟的脚本和处理流程，会覆盖各种边界情况）
3. 对于读素材这种一次性场景，不需要复杂交互 —— 读 SKILL.md、照它说的做就行

**什么时候不走 skill**：如果只是读一个小 md 或纯文本，直接 `view` 最快，不用拐一道弯。

---

## 读取策略总览（上下文节流）

素材文档多（10-20 个以上）时，**不要一上来就全文读入上下文**，会撑爆。

推荐顺序：
1. **先列目录**：`find <dir> -type f | head -50` 查看文件清单
2. **读 md 和纯文本**：直接 `view` 工具读全文
3. **提取 docx/xlsx/pdf 的结构**（标题层级 / 工作表列表 / 目录）：建立"文档地图"
4. **按需精读具体章节**：等到写对应章节时再读

在工作目录创建一份临时 md（如 `/home/claude/sources-map.md`）记录文档地图：

```
- product-design.docx
  - 第 2 章 架构：审计引擎、规则库、告警模块
  - 第 3 章 数据流：采集 → Kafka → 解析 → ES
  - 第 4 章 接口：P26-P45（稍后精读）
- interface-spec.xlsx
  - Sheet1 「接口清单」：43 行 × 8 列
  - Sheet2 「错误码」：已全量读取
- database-tables.md：所有表结构定义（已全量读取）
- deployment-guide.pdf：部署拓扑、硬件要求（扫描件，需 OCR）
```

---

## Fallback 脚本（没有对应 skill 时用）

> 以下脚本是应急方案。有对应 skill 时一律优先用 skill。

### 1. 读取 .md

直接 `view`。超长（>1000 行）时分段读：

```
view <path> [1, 200]
view <path> [201, 400]
```

### 2. 读取 .docx（无 docx skill 时）

```python
# pip install python-docx
from docx import Document
doc = Document('/path/to/file.docx')

# 正文 + 标题层级
for para in doc.paragraphs:
    if not para.text.strip():
        continue
    style = para.style.name
    if style.startswith('Heading'):
        try:
            level = int(style.replace('Heading ', ''))
            print(f"{'#' * level} {para.text}")
        except ValueError:
            print(f"# {para.text}")
    else:
        print(para.text)

# 所有表格
for i, table in enumerate(doc.tables):
    print(f"\n=== 表格 {i+1} ===")
    for row in table.rows:
        cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
        print(" | ".join(cells))
```

**只提取标题层级**（快速看结构）：

```python
from docx import Document
doc = Document('/path/to/template.docx')
for para in doc.paragraphs:
    style = para.style.name
    if style.startswith('Heading'):
        try:
            level = int(style.replace('Heading ', ''))
            print(f"{'#' * level} {para.text}")
        except ValueError:
            print(f"# {para.text}")
```

**识别模板中的占位符**（招投标 / 设计模板常见 `【请填写】`、`<XXX>`、`XXX 公司`）：

```python
from docx import Document
import re
doc = Document('/path/to/template.docx')
patterns = [r'【[^】]+】', r'<[^>]+>', r'X{2,}(公司|项目|系统|产品)']
for i, para in enumerate(doc.paragraphs):
    for pat in patterns:
        if re.search(pat, para.text):
            print(f"段落 {i}: {para.text}")
            break
```

### 3. 读取 .xlsx / .xls（无 xlsx skill 时）

```python
# pip install openpyxl pandas
import pandas as pd

# 列出所有工作表
xl = pd.ExcelFile('/path/to/file.xlsx')
print("工作表列表:", xl.sheet_names)

# 读取某个工作表
df = pd.read_excel('/path/to/file.xlsx', sheet_name='Sheet1')
print(df.shape)          # (行数, 列数)
print(df.columns.tolist())
print(df.head(10))

# 读取所有工作表
all_sheets = pd.read_excel('/path/to/file.xlsx', sheet_name=None)
for name, df in all_sheets.items():
    print(f"\n=== {name} ({df.shape[0]} 行 × {df.shape[1]} 列) ===")
    print(df.head(5))
```

**带合并单元格的复杂表格**（Excel 接口清单常见）：

```python
# pip install openpyxl
from openpyxl import load_workbook
wb = load_workbook('/path/to/file.xlsx', data_only=True)  # data_only=True 取公式计算结果
for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    print(f"\n=== {sheet_name} ===")
    for row in ws.iter_rows(values_only=True):
        print(row)
```

### 4. 读取 .pdf（无 pdf-reading skill 时）

```python
# pip install pdfplumber
import pdfplumber
with pdfplumber.open('/path/to/file.pdf') as pdf:
    for i, page in enumerate(pdf.pages):
        print(f"\n--- Page {i+1} ---")
        text = page.extract_text()
        if text:
            print(text)
        for j, table in enumerate(page.extract_tables()):
            print(f"\n[Table {j+1}]")
            for row in table:
                print(" | ".join(str(c) if c else "" for c in row))
```

扫描版 PDF（`extract_text()` 返回空）需要 OCR。pdf-reading skill 直接支持；应急方案用 `pytesseract` + `pdf2image`，配置较麻烦，尽量走 skill。

### 5. 读取 .pptx（无 pptx skill 时）

```python
# pip install python-pptx
from pptx import Presentation
prs = Presentation('/path/to/file.pptx')
for i, slide in enumerate(prs.slides):
    print(f"\n=== Slide {i+1} ===")
    for shape in slide.shapes:
        if shape.has_text_frame:
            for para in shape.text_frame.paragraphs:
                if para.text.strip():
                    print(para.text)
        if shape.has_table:
            for row in shape.table.rows:
                cells = [cell.text.strip() for cell in row.cells]
                print(" | ".join(cells))
```

---

## 常见坑

| 问题 | 解决 |
|------|------|
| docx 表格有合并单元格 | `python-docx` 会重复返回同一单元格内容，手动去重；或首选 `docx` skill |
| docx 有修订痕迹未接受 | `docx2txt` 忽略修订；或让用户先在 Word 里"接受所有修订" |
| PDF 是扫描件 | 必须 OCR，强烈建议用 `pdf-reading` skill |
| PDF 双栏/图文混排 | `pdfplumber` 顺序可能混乱，换 `pymupdf`（`fitz`）的 `page.get_text("blocks")` |
| docx 打不开 | 可能是 `.doc`（老格式），用 `libreoffice --headless --convert-to docx` 先转换 |
| Excel 公式而非结果 | `openpyxl.load_workbook(..., data_only=True)` 或 `pandas.read_excel`（默认取结果）|
| Excel 多级表头 | `pd.read_excel(..., header=[0, 1])` 传列表指定多行为表头 |
