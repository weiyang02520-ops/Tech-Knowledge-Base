# 何时应该先查这个项目

当你准备实现长期运行 Agent、后台任务、会话恢复、子 Agent、Agent 通信、定时任务、持久目标、上下文压缩或 autonomous loop 时，应先查 Prime Agent。

# 功能：后台与可恢复会话

- 已有方案：客户端与执行分离；daemon supervisor 管理常驻 worker；worker 独占根 session tree。
- 涉及模块：`modes/daemon/daemon-supervisor.ts`、`core/agent-session-runtime.ts`、`modes/agent-connection/`。
- 可以借鉴：所有权模型、generation-aware 重连、恢复快照、worker health 和持久 session catalog。
- 可以改造：替换本地 daemon protocol 或存储格式，保留生命周期边界。
- 不建议复制：在只需要单进程短任务时复制全部多进程基础设施。
- 风险：进程恢复、一致性、重复投递和孤儿进程处理复杂。
- 成熟度：架构 `A`，当前具体 API `B/Needs Verification`。

# 功能：子 Agent 与 Agent 通信

- 已有方案：`rlm(...)` 创建独立子 `AgentSession`，立即返回 handle；结果通过显式消息或文件返回，不伪装成同步函数结果。
- 核心思路：父子注册表持久化，身份和路由由宿主掌握，消息支持 busy steer 与 idle delivery。
- 可以借鉴：显式生命周期、有限递归深度、保留完成子 Agent、可恢复地址和送达回执。
- 不建议复制：把无限层级或无预算并发当作默认能力。
- 仍需开发：领域任务分解、权限策略、资源配额和产品级观测。

# 功能：Heartbeat、Schedule 与 Persistent Goal

- Heartbeat 是重复重入指令；schedule 是通用一次性/cron prompt；goal 保存目标和进度；autonomous mode 决定是否继续运行。
- 可以直接复用的思想：四者分离，统一进入 session prompt queue。
- 关键细节：到期任务先 claim 再交付；错过 tick 合并而不无限堆积；只有显式完成动作能宣告 goal 成功；到达预算不是完成。
- 仍需开发：业务特定的调度持久层、分布式锁、幂等副作用和 SLA。

# 功能：Context Persistence 与 Compaction

- 已有方案：旧消息摘要，保留近期上下文；IPython 状态、child registry、目标和 artifact 独立持久。
- 可以借鉴：区分 conversation summary、execution state、task state 和 child state。
- 不建议复制：把内存中的 Python 对象当成唯一可靠持久层。
- 风险：摘要信息损失、状态 schema 演进、恢复版本兼容。

# 功能：Continual Harness 与 Skills

- 已有方案：补充 prompt、memory、skill description 和 subagent spec 可通过小型、有证据的变更逐步改进；基础系统 prompt 保持不可变。
- 可以借鉴：可审阅增量、快照回滚、说明型 skill 与 Python-backed skill 分层。
- 只应参考：自动自我修改的治理方式；任何执行型 skill 都扩大供应链和权限面。

# 不要重复造轮子的部分

- 客户端断开与后台执行解耦的所有权模型。
- session worker、恢复目录、transcript 和 artifact 的职责划分。
- Heartbeat/schedule/goal/autonomous 的语义拆分。
- 子 Agent handle、注册表、显式消息和递归边界。
- 压缩不等于完成、预算耗尽不等于成功的状态机原则。

# 仍然值得自己实现的部分

- 与自身产品权限、安全域和部署方式匹配的 supervisor。
- 持久层、幂等副作用、审计和多租户隔离。
- 领域特定的完成条件、质量门和失败恢复。
- 轻量需求下更小的单进程实现。
- 真正的安全 sandbox；Prime Agent 的进程隔离不是安全隔离。

# 决策表

| Capability | Decision | Reason |
| --- | --- | --- |
| 生命周期与所有权模型 | Reference / Adapt | 结构成熟，但需匹配自身部署。 |
| daemon 协议和完整运行时 | Reuse only after validation | pre-1.0 且依赖 Node、Python 与多进程。 |
| Goal/heartbeat/schedule 语义 | Reuse concept | 边界清楚，能避免状态混淆。 |
| 子 Agent registry 与消息 | Adapt | 通用价值高，资源和权限策略需自定。 |
| Context compaction | Adapt | 摘要策略依模型和任务而变。 |
| 安全隔离 | Build / external sandbox | 上游明确说明 worker/kernel 不是 sandbox。 |
| 业务 Agent 行为 | Build | 属于产品差异化和领域知识。 |

