# Changelog

## 1.4.0

- 新增 `docs/installation-validation-report.md`，记录安装前静态准入校验、可安装性结论、验证范围和真实安装待验证项。
- 新增 `docs/example-regression-test-report.md`，完成大陆一线城市、大陆下沉城市、香港、澳门四类示例输入输出模拟回归测试，并补充触发边界测试。
- 更新 `SKILL.md`、`README.md` 与 `docs/skillhub-store-listing.md`，将安装验证和回归测试报告纳入技能包入口说明。
- 版本升级至 `1.4.0`。

## 1.3.0

- 新增 `examples/regional-market-cases.md`，补充大陆一线城市、大陆下沉城市、香港、澳门四类可直接套用的市场案例。
- 新增 `docs/skillhub-admission-review.md`，完成 SkillHub 上架准入评审，覆盖名称、描述、触发词、适用边界、输入输出、合规风险、隐私数据、安装验证、示例完整性与回退检查。
- 更新 `SKILL.md`、`README.md` 与 `docs/skillhub-store-listing.md`，将案例与准入评审纳入技能入口和商店展示。
- 版本升级至 `1.3.0`。

## 1.2.0

- 将技能定位从单一澳门市场升级为覆盖中国大陆、香港、澳门的中国市场通用版。
- 新增 `references/regional-adaptation-guide.md`，补充三地在渠道、合规、币种、语言、客户关注点与运营节奏上的适配原则。
- 新增 `templates/problem-routing-template.md`，支持用户先提出具体业务问题，再按问题选择轻量诊断、专项流程或全流程诊断。
- 更新 `SKILL.md`、`README.md`、客户分层、营销战役库、销售 SOP、输入数据字段规范和 SkillHub 商店展示文案。
- 自动修复 YAML front matter，新增 `title` 字段，确保技能注册元数据完整。

## 1.1.0

- 新增 `docs/skillhub-store-listing.md`，补齐 SkillHub 技能商店展示文案、示例提示词、适用人群、能力边界和推荐标签。
- 新增 `docs/input-data-schema.md`，提供汽车经销商真实落地所需的最小输入、漏斗数据、渠道数据、客群、销售承接、销售政策与复盘字段规范。
- 修正 `SKILL.md`、`README.md` 和发布清单中的文档引用，确保目录结构与实际文件一致。
- 统一 RIPCAS 定义为 Reach、Interest、Preference、Conversion、Advocacy、System。
- 版本升级至 `1.1.0`。

## 1.0.0

- 补齐 SkillHub 发布所需 YAML front matter。
- 统一技能名称为 `auto-dealer-ripcas-marketing`。
- 统一 RIPCAS 框架命名，避免 RIPCAS 混用。
- 补充 README、安装说明、回退说明、发布验证记录和发布前检查清单。
- 清理原包中被工具摘要污染的参考与示例内容。
- 补充月度计划、战役 Brief、内容排期、销售话术、复盘报告示例。
- 明确合规边界：不承诺销量、不制造虚假优惠、不夸大金融政策。
