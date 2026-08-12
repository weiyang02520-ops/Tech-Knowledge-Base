# 一句话说明

Prime Agent 是一个以持久 IPython 控制环境、daemon 后台进程和可恢复会话为核心的编程/研究 Agent，重点解决长任务、子 Agent、调度、目标和上下文连续性。

# 它解决什么问题

普通聊天 Agent 把终端窗口、单轮上下文和任务生命周期绑在一起。Prime Agent 把界面、后台进程、会话运行时、Python 内核和持久化状态拆开，使任务能在界面断开后继续，并在压缩或重启后恢复关键状态。

# 核心功能

- daemon 管理的后台 session worker 与重新连接。
- 持久 IPython，模型通过程序化调用操作文件、命令、技能和子 Agent。
- 原生递归子 Agent、保留的子 Agent 注册表和 Agent 间消息。
- 用户 heartbeat、Agent heartbeat、一次性和 cron schedule。
- Persistent Goal 与有限制、有质量门的 autonomous mode。
- 自动上下文压缩、JSONL transcript、session artifacts 和恢复机制。
- TUI、print、JSON、RPC 等多种接入模式。

# 核心技术

TypeScript/Node.js 负责模型调用、调度、会话、持久化和进程协调；独立 Python/IPython 内核作为模型可编程控制面；本地 daemon protocol 连接客户端和 worker；JSONL 与 artifact 目录保存会话状态。

# 主要目录

重点看 `packages/coding-agent/docs/`、`packages/coding-agent/src/core/`、`packages/coding-agent/src/modes/daemon/`、`packages/coding-agent/src/modes/agent-connection/`、`packages/coding-agent/skills/` 和 `prime-agent-runtime/src/rlm/`。

# 主要模块

- `AgentConnection`：客户端与执行边界。
- daemon supervisor/catalog：发现、路由、附件、健康和恢复。
- session worker / `AgentSessionRuntime`：一个根会话树的生命周期容器。
- `AgentSession`：provider、队列、工具、目标、压缩、子 Agent 和 transcript。
- IPython kernel / host bridge：模型程序化接口与宿主权威状态之间的边界。
- scheduler、goals、autonomous policy：长任务再进入和连续执行。

# 工作方式

客户端把 prompt 交给 supervisor，supervisor 路由到驻留 worker；`AgentSession` 调用模型，模型在需要时使用 IPython。Python 侧通过 typed host request 请求 TypeScript 宿主执行权威操作。会话事件写入 JSONL/artifacts；客户端断开不会自动停止 worker。

# 适合什么场景

- 长时间编程、研究、评测或后台监控任务。
- 需要多个可保留子 Agent 协作的任务。
- 需要心跳、定时重入、持久目标和会话恢复的本地 Agent。
- 研究“界面断开不等于任务结束”的运行时架构。

# 不适合什么场景

- 只需一次模型调用或短脚本的简单任务。
- 需要强安全隔离但没有外部 sandbox 的不可信代码执行。
- 不能接受 Node + Python/IPython 双运行时和多进程复杂度的轻量产品。
- 希望 API 长期稳定且不愿跟随 pre-1.0 快速变化的集成。

# 最值得看的东西

daemon/worker/session/kernel 的所有权边界；同一 prompt queue 接收用户、heartbeat、schedule、goal、autonomous 和 peer-agent 输入；persistent goal 与 autonomous policy 的分离；compaction 不等于完成；子 Agent 的可恢复注册和显式消息返回。

# 可以暂时不看的东西

具体 TUI 渲染、所有模型 provider、安装发布脚本、品牌服务集成和每个第三方 skill。先理解 `architecture.md`、`long-running-agents.md` 和核心 session/daemon 文件即可。

# 对本资料库的价值

它是首批项目中最直接回答“如何避免重新设计长期 Agent 基础设施”的仓库。即使不采用其整套运行时，也能复用生命周期、所有权、恢复、调度和完成语义。

# 30 秒快速判断

需求包含后台运行、断线重连、持久目标、心跳、调度、上下文压缩或子 Agent 时优先查；只做短任务或要求强隔离时，不要直接套用整套架构。

