# 结构要求清单

每种单文件产出类型的组件槽位定义，供UTOS内容轴清单法使用。标注 `[待补充]` 的字段需根据实际需求定义。

> **重要**：本技能的"结构要求"对HTML产物指HTML/CSS/JS代码结构要素；对Python CLI产物指标准库+argparse代码结构要素。

---

## S1 演示展示

### S1-01 HTML幻灯片(PPT)
- **必选组件（HTML结构）**: `<!DOCTYPE html>` + `<style>`内联CSS + `<body>`幻灯片容器 + JS翻页逻辑
- **CSS组件**: 全屏slide容器、过渡动画(keyframe/transition)、字体系统(无外部字体依赖或用CDN白名单)、暗/亮主题切换
- **JS组件**: 键盘事件监听(←→/Space)、点击翻页、进度条、页码显示、全屏模式(F11)
- **组装顺序**: HTML骨架→CSS样式→翻页JS→内容填充→测试
- **质量约束**: 必须在Chrome/Firefox/Safari最新版正常渲染
- **格式**: 单一.html文件

### S1-02 滚动长海报/落地页
- **必选组件**: 视差滚动层(section)、滚动触发动画(IntersectionObserver)、CTA按钮区、移动端响应式(@media)
- **可选组件**: 导航锚点、计数器动画、视频嵌入占位、表单收集
- **组装顺序**: 页面分区→视差层→动画触发→交互元素→响应式适配
- **质量约束**: 首屏加载<3s，滚动流畅60fps
- **格式**: 单一.html文件

### S1-03~S1-06 （摘要）

| ID | 必选组件摘要 | 格式 |
|----|-------------|------|
| S1-03 信息图 | SVG图表/CSS图表、数据绑定、hover tooltip、图例 | .html |
| S1-04 简历页 | 头像区/简介/时间线/技能条/作品卡片/联系方式 | .html |
| S1-05 作品集 | 筛选栏/卡片网格/模态详情/分类标签/搜索 | .html |
| S1-06 报告可视化 | 侧边导航/章节内容/图表嵌套/目录自动生成 | .html |

---

## S2 游戏娱乐

### S2-01 俄罗斯方块
- **必选组件（HTML结构）**: `<canvas>`游戏画布 + 分数/等级/下一个预览UI + 游戏控制按钮
- **CSS组件**: canvas居中、UI面板布局、游戏结束遮罩、响应式画布缩放
- **JS核心模块**:
  - `Game`类：主循环(requestAnimationFrame)、状态管理(playing/paused/gameover)
  - `Board`类：棋盘数据结构(二维数组)、碰撞检测、行消除
  - `Piece`类：7种标准方块(I/O/T/S/Z/J/L)定义、旋转矩阵
  - `Input`类：键盘控制(方向键/旋转/硬降/暂停)、触摸支持
  - `Score`类：计分规则、等级递增、速度曲线、最高分(localStorage)
  - `Renderer`类：canvas绘制（方块颜色/网格/阴影）
- **组装顺序**: HTML→CSS→Piece定义→Board逻辑→Input处理→Game主循环→Score→Renderer→测试
- **质量约束**: 60fps流畅运行，移动端可触摸操作
- **格式**: 单一.html文件

### S2-02~S2-08 （摘要）

| ID | 核心数据结构 | 关键算法 | 格式 |
|----|-------------|---------|------|
| S2-02 贪吃蛇 | 方向队列/身体坐标数组 | 碰撞检测(自身+边界) | .html |
| S2-03 2048 | 4x4数组/滑动方向向量 | 合并+随机生成新块 | .html |
| S2-04 扫雷 | 二维格数组(-1地雷/0-8数字) | BFS递归展开空白区 | .html |
| S2-05 弹球打砖块 | 挡板/球/砖块对象列表 | 反射角计算/碰撞AABB | .html |
| S2-06 打字练习 | 文本库/当前位置/WPM统计器 | 输入对比/时间测量 | .html |
| S2-07 记忆翻牌 | 卡片数组(值/翻转状态/匹配状态) | 配对检查/洗牌算法 | .html |
| S2-08 Quiz问答 | 题库数组/当前题号/得分/计时器 | 题型路由/答案校验 | .html |

---

## S3 实用工具

### S3-01 计算器
- **必选组件**: 显示屏(input readonly或div)、按键网格(0-9+-×÷=C%)、运算逻辑(eval安全替代)
- **JS核心**: 表达式解析（不直接eval，自行实现shunting-yard或简单状态机）、历史记录栈、键盘输入映射
- **组装顺序**: UI布局→按键事件→表达式解析→结果显示→历史记录→键盘支持
- **质量约束**: 支持连续运算、小数精度处理、错误提示
- **格式**: .html

### S3-02~S3-08 （摘要）

| ID | 必选组件摘要 | 格式 |
|----|-------------|------|
| S3-02 单位转换器 | 分类选择/输入框/结果展示/常用快捷转换/反向转换 | .html |
| S3-03 密码生成器 | 选项面板(长度/大小写/数字/符号)/生成按钮/强度指示条/复制按钮 | .html |
| S3-04 Markdown编辑器 | 左右分栏(编辑/预览)/实时渲染/工具栏(粗体/标题/列表/代码)/导出 | .html |
| S3-05 JSON格式化 | 输入区/美化输出/压缩输出/error定位/树形浏览/路径查询(JSONPath) | .html |
| S3-06 正则测试器 | 正则输入/测试文本/匹配高亮(分组色编码)/替换预览/常用正则库 | .html |
| S3-07 颜色选择器 | 拾色器/HEX-RGB-HSL互转/调色板/对比度检查(WCAG)/复制格式化 | .html |
| S3-08 Base64编解码 | 文本输入/Base64输出/双向转换/文件拖放编解码/复制按钮 | .html |

---

## S4 数据可视化

| ID | 必选组件摘要 | 数据源格式 | 格式 |
|----|-------------|----------|------|
| S4-01 图表仪表盘 | 图表类型选择器/数据输入区(canvas或SVG绘制)/多图表联动/导出PNG | JSON数组 | .html |
| S4-02 时间线 | 垂直/水平切换/事件节点(时间+标题+描述+图片)/缩放控制/锚点导航 | JSON数组 | .html |
| S4-03 组织架构树 | 树形数据结构/展开折叠/搜索高亮/缩放平移/drag重排 | 嵌套JSON | .html |
| S4-04 流程图/状态机 | 节点+连线定义/交互式导航/状态高亮/事件触发演示 | JSON图定义 | .html |
| S4-05 地图标注 | 地图画布(Leaflet CDN白名单)/标记点聚类/信息窗口/图层切换 | GeoJSON | .html |
| S4-06 实时监控面板 | 多指标卡片/趋势图/表格/阈值告警闪烁/模拟数据流 | WebSocket模拟 | .html |

---

## S5 Python CLI工具

> **S5域特殊规范**：
> - 仅使用Python标准库（stdlib），零第三方依赖
> - 使用 `argparse` 实现子命令体系：`python tool.py <subcommand> [options]`
> - 支持 `--verbose` / `--quiet` / `--output FORMAT` 通用选项
> - 支持 Unix管道输入输出（stdin/stdout）
> - 包含 `--help` 和 `--version`
> - 错误时 exit code 非0

### S5-01 文件批量重命名
- **必选子命令**: `rename` (主命令)
- **必选参数**: `--pattern` (命名模式, 含{n}序号/{date}{ext}等变量)、`--target-dir`、`--dry-run`(预览)
- **可选参数**: `--regex` (正则捕获组替换)、`--prefix`、`--suffix`、`--case`(upper/lower/title)、`--recursive`
- **核心逻辑**: os.listdir/scandir → 匹配文件名 → 应用变换规则 → 冲突检测 → 执行rename
- **组装顺序**: argparse定义→文件扫描→模式解析→变换执行→冲突检查→dry-run确认→实际执行
- **质量约束**: dry-run默认启用，必须用户确认后才执行
- **格式**: 单一.py文件

### S5-02 目录分析器
- **必选子命令**: `scan` / `stats` / `tree`
- **必选参数**: `--path`(目标目录)、`--output`(json/text/csv/table)
- **可选参数**: `--max-depth`、`--min-size`、`--by-ext`(按扩展名分组)、`--top-n`(Top N大文件)
- **核心逻辑**: os.walk递归遍历 → 收集文件元信息(size/mtime/ext) → 聚合统计 → 格式化输出
- **格式**: 单一.py文件

### S5-03 日志解析器
- **必选子命令**: `parse` / `stats` / `errors` / `timeline`
- **必选参数**: `--file`(日志文件路径, 支持stdin管道)、`--format`(日志格式: apache/nginx/json/syslog/custom)
- **可选参数**: `--level`(过滤级别)、`--since`/`--until`(时间范围)、`--grep`(关键词过滤)、`--top`(Top N)
- **核心逻辑**: 行读取→正则解析→结构化(dict)→聚合/过滤/排序→输出
- **格式**: 单一.py文件

### S5-04 CSV处理工具
- **必选子命令**: `read` / `filter` / `sort` / `join` / `agg`(aggregate) / `transpose` / `convert`
- **必选参数**: `--file`(CSV路径)、`--delimiter`(分隔符)、`--encoding`(编码)
- **可选参数**: `--where`(过滤条件)、`--columns`(指定列)、`--group-by`/`--agg-func`(聚合)、`--on`(join键)
- **核心逻辑**: csv.DictReader读写 → 内存DataFrame式操作(纯dict/list实现) → csv.writer输出
- **格式**: 单一.py文件

### S5-05~S5-10 （摘要）

| ID | 子命令 | 核心功能 | 关键stdlib模块 |
|----|--------|---------|---------------|
| S5-05 图片批处理 | `resize`/`crop`/`convert`/`watermark`/`rename` | PIL(Pillow允许时)或跳过 |
| S5-06 HTTP客户端 | `get`/`post`/`put`/`delete`/`head` | urllib.request/ssl/json |
| S5-07 定时调度 | `run`/`list`/`remove`/`status` | sched/time/threading |
| S5-08 配置管理 | `read`/`write`/`validate`/`diff`/`merge` | configparser/json/yaml(toml如可用) |
| S5-09 代码生成 | `generate`from`--template` | string.Template/jinja2(内置简化版) |
| S5-10 全文搜索 | `search`/`replace`/`preview`/`count` | re/os/pathlib/glob |

---

## S6-S7 结构要求（摘要版）

### S6 开发辅助（8种）

| ID | 必选组件摘要 | 格式 |
|----|-------------|------|
| S6-01 代码高亮查看器 | 语言选择/代码输入区/语法高亮渲染(手写keyword正则)/行号/复制/暗色模式 | .html |
| S6-02 API Mock服务 | 路由定义(JSON)/延迟模拟/状态码/CORS/请求日志/动态响应模板 | .html |
| S6-03 Diff对比 | 左右文本区/并排统一切换/行级diff算法(LCS)/颜色编码(增/删/改)/统计 | .html |
| S6-04 正则可视化 | 正则输入/测试文本/步骤分解可视化(匹配过程动画)/分组捕获展示 | .html |
| S6-05 Cron解析器 | Cron表达式输入/人类可读解释/未来N次执行时间列表/逆推最近执行 | .html |
| S6-06 URL编解码 | URL输入/各组件拆解(scheme/host/path/query/hash)/encode/decode/Punycode | .html |
| S6-07 Markdown预览 | 编辑/预览分栏/GFM扩展/数学公式(KaTeX CDN)/代码块高亮/TOC | .html |
| S6-08 Schema校验 | YAML/JSON输入/Schema定义(内联)/错误定位(行+列)/修复建议/路径高亮 | .html |

### S7 教学与交互（6种）

| ID | 必选组件摘要 | 格式 |
|----|-------------|------|
| S7-01 交互式教程 | 步骤卡片/进度条/代码示例(executable sandbox)/下一步按钮/完成庆祝 | .html |
| S7-02 步骤向导 | 步骤条/每步表单/校验/上一步下一步/分支条件/最终汇总 | .html |
| S7-03 概念图解动画 | SVG图形+CSS/JS动画序列/播放控制/步骤说明/循环播放 | .html |
| S7-04 算法可视化 | 数组可视化(柱状图)/比较/交换高亮/速度控制/步数统计/复杂度标注 | .html |
| S7-05 语法树可视化 | 代码输入→解析→SVG树形绘制(节点=非终结符/叶=token)/展开折叠 | .html |
| S7-06 状态机演示 | 状态节点(圆圈)+转移箭头(带事件标签)/点击触发转移/历史轨迹高亮/当前态标识 | .html |
