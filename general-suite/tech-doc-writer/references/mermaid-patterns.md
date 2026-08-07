# 技术文档常用 Mermaid 图 & 表格模板

选对图类型是关键。先看"何时用什么图"速查表，然后对照模板改。

## 速查：何时用什么图

| 场景 | 推荐类型 |
|------|---------|
| 系统整体架构（分层） | `flowchart TB` + `subgraph` |
| 部署拓扑 | `flowchart LR` + `subgraph` |
| 跨服务调用 / 接口时序 | `sequenceDiagram` |
| 业务流程 / 算法 | `flowchart LR` 或 `TD` |
| 数据模型 | `erDiagram` |
| 状态流转 / 审批流 | `stateDiagram-v2` |
| 项目进度 / 里程碑 | `gantt` |
| 组织结构 / 类继承 | `flowchart` 或 `classDiagram` |

---

## 1. 系统架构图（分层架构）

```mermaid
flowchart TB
  subgraph UI[接入层]
    Web[Web 门户]
    Mobile[移动端]
    API_GW[API 网关]
  end
  subgraph Service[服务层]
    Auth[认证服务]
    Biz[业务服务]
    Audit[审计服务]
  end
  subgraph Data[数据层]
    DB[(业务 DB)]
    Cache[(Redis)]
    Queue[Kafka]
    ES[(Elasticsearch)]
  end

  Web --> API_GW
  Mobile --> API_GW
  API_GW --> Auth
  API_GW --> Biz
  Biz --> DB
  Biz --> Cache
  Biz --> Queue
  Queue --> Audit
  Audit --> ES
```

## 2. 部署拓扑图

```mermaid
flowchart LR
  User((用户))
  subgraph DMZ区[DMZ 区]
    LB[负载均衡<br/>F5/Nginx]
  end
  subgraph App区[应用区]
    App1[应用节点 1]
    App2[应用节点 2]
    App3[应用节点 3]
  end
  subgraph Data区[数据区]
    DB_M[(MySQL 主)]
    DB_S[(MySQL 从)]
    Redis[(Redis 集群)]
  end

  User --> LB
  LB --> App1
  LB --> App2
  LB --> App3
  App1 & App2 & App3 --> DB_M
  App1 & App2 & App3 --> Redis
  DB_M -.异步复制.-> DB_S
```

## 3. 接口调用时序图

```mermaid
sequenceDiagram
  autonumber
  participant C as 客户端
  participant G as API 网关
  participant A as 认证服务
  participant S as 业务服务
  participant D as 数据库

  C->>G: POST /api/order + Token
  G->>A: 验证 Token
  A-->>G: 用户信息 + 权限
  G->>S: 转发请求
  S->>D: 查询/写入
  D-->>S: 返回结果
  S-->>G: 业务响应
  G-->>C: JSON 响应
```

## 4. 业务流程图

```mermaid
flowchart TD
  Start([用户发起申请]) --> A[填写申请表单]
  A --> B{表单校验}
  B -->|失败| A
  B -->|通过| C[提交审核]
  C --> D{一级审核}
  D -->|驳回| A
  D -->|通过| E{二级审核}
  E -->|驳回| A
  E -->|通过| F[进入处理队列]
  F --> G[自动处理]
  G --> H[通知用户]
  H --> End([流程结束])
```

## 5. 数据模型 ER 图

```mermaid
erDiagram
  USER ||--o{ AUDIT_LOG : 产生
  USER ||--o{ ROLE_ASSIGN : 拥有
  ROLE ||--o{ ROLE_ASSIGN : 被分配

  USER {
    bigint id PK
    varchar username UK
    varchar email
    varchar password_hash
    datetime created_at
    tinyint status
  }
  AUDIT_LOG {
    bigint id PK
    bigint user_id FK
    varchar action
    varchar resource
    text detail
    datetime created_at
  }
  ROLE {
    int id PK
    varchar name UK
    varchar description
  }
  ROLE_ASSIGN {
    bigint user_id FK
    int role_id FK
    datetime assigned_at
  }
```

## 6. 状态机（审批流 / 生命周期）

```mermaid
stateDiagram-v2
  [*] --> 草稿
  草稿 --> 待审核: 提交
  待审核 --> 审核中: 领取
  审核中 --> 已通过: 审核通过
  审核中 --> 已拒绝: 审核拒绝
  审核中 --> 待审核: 释放
  已拒绝 --> 草稿: 重新编辑
  已通过 --> [*]
```

## 7. 数据流图

```mermaid
flowchart LR
  DS[(业务数据库)] -->|CDC| Collector[日志采集]
  App[应用系统] -->|syslog| Collector
  Net[网络设备] -->|SNMP| Collector
  Collector --> Queue[Kafka]
  Queue --> Parser[日志解析]
  Parser --> Engine[审计引擎]
  Engine --> ES[(ES 索引)]
  Engine --> Alert[告警系统]
  ES --> Dashboard[审计仪表盘]
```

## 8. 甘特图（项目进度）

```mermaid
gantt
  title 项目实施计划
  dateFormat YYYY-MM-DD
  section 需求与设计
  需求调研       :a1, 2026-05-01, 10d
  方案设计       :a2, after a1, 15d
  section 开发实施
  基础环境搭建   :b1, after a2, 5d
  核心功能开发   :b2, after b1, 30d
  联调测试       :b3, after b2, 15d
  section 验收上线
  性能测试       :c1, after b3, 7d
  试运行         :c2, after c1, 14d
  正式上线       :milestone, after c2
```

---

## 表格模板

### 接口 — 请求参数表

| 参数名 | 类型 | 必选 | 说明 | 示例 |
|--------|------|:----:|------|------|
| user_id | bigint | 是 | 用户 ID | 10086 |
| name | string | 否 | 姓名，最长 50 字符 | 张三 |
| status | int | 否 | 状态，枚举值 0/1/2，默认 0 | 1 |
| created_after | string | 否 | 筛选起始时间，ISO8601 | 2026-04-01T00:00:00Z |

### 接口 — 返回字段表

| 字段名 | 类型 | 说明 |
|--------|------|------|
| code | int | 状态码，0 表示成功 |
| message | string | 提示信息 |
| data | object | 业务数据 |
| data.list | array | 记录列表 |
| data.total | int | 总记录数 |

### 接口 — 错误码表

| 错误码 | HTTP | 含义 | 处置建议 |
|--------|:----:|------|---------|
| 0 | 200 | 成功 | — |
| 40001 | 400 | 参数错误 | 检查请求参数 |
| 40101 | 401 | 未认证 | 重新登录获取 Token |
| 40301 | 403 | 权限不足 | 申请对应角色 |
| 42901 | 429 | 请求过于频繁 | 降低请求频率后重试 |
| 50000 | 500 | 服务内部错误 | 联系技术支持 |

### 数据表 — 字段定义表

| 字段名 | 类型 | 非空 | 默认值 | 说明 |
|--------|------|:----:|--------|------|
| id | bigint unsigned | 是 | AUTO_INCREMENT | 主键 |
| user_id | bigint unsigned | 是 | — | 用户 ID，外键 → user.id |
| action | varchar(64) | 是 | — | 操作类型 |
| detail | text | 否 | NULL | 操作详情 JSON |
| created_at | datetime | 是 | CURRENT_TIMESTAMP | 创建时间 |

### 性能指标表

| 指标 | 目标值 | 测试方法 |
|------|-------|---------|
| 单接口 TPS | ≥ 1000 | JMeter 压测，100 并发持续 10 分钟 |
| 平均响应时间 | ≤ 200ms | 生产环境 APM 7 日均值 |
| P99 响应时间 | ≤ 500ms | 同上 |
| 年可用性 | ≥ 99.9% | 全年累计不可用时间 ≤ 8.76 小时 |

### 方案对比表（架构文档常用）

| 维度 | 方案 A：MySQL | 方案 B：PostgreSQL | 方案 C：TiDB |
|------|--------------|-------------------|-------------|
| 扩展性 | 中等（需分库分表） | 中等 | 强（原生分布式）|
| 事务支持 | 强 | 强 | 强 |
| JSON 查询 | 一般 | 强 | 一般 |
| 团队熟悉度 | 高 | 低 | 中 |
| 运维成本 | 低 | 中 | 高 |
| 推荐度 | ★★★★ | ★★★ | ★★ |

---

## 画图注意事项

1. **节点数量**：一张图尽量不超过 15-20 个节点，多了就拆分
2. **图的方向**：
   - `TB`（上到下）适合分层架构
   - `LR`（左到右）适合流程、部署拓扑
3. **中文**：Mermaid 原生支持中文，但节点 ID 用英文更稳妥（显示内容可以是中文）
4. **样式**：技术文档画图保持朴素，避免过多颜色和装饰
5. **可读性优先**：宁可分成两张简单的图，也不要一张巨复杂的图
