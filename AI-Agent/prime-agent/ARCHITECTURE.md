# Architecture Overview

```text
TUI / Print / JSON / RPC
          |
          v
    AgentConnection
          |
          v
  Daemon Supervisor <----> Session Catalog
          |
          v
  Session Worker (one root session tree)
    |       |        |          |
    |       |        |          +--> Scheduler / Heartbeats
    |       |        +-------------> Persistent IPython Kernel
    |       +----------------------> Child AgentSessions
    +------------------------------> Root AgentSession
                                         |
                            +------------+------------+
                            v                         v
                      Model Providers        JSONL / Artifacts
```

进程分离用于生命周期和故障约束，不等于安全 sandbox。

# Module Responsibilities

| Module | Responsibility | Connects To | Source Entry |
| --- | --- | --- | --- |
| Client modes | 渲染、键盘、headless/RPC 接入 | AgentConnection | `packages/coding-agent/src/modes/` |
| AgentConnection | 隔离客户端与执行，处理命令、事件、快照和重连 | supervisor 或 in-process runtime | `modes/agent-connection/` |
| Daemon supervisor | session 发现、路由、附件、worker 健康、跨 Agent 消息 | catalog、worker、client | `modes/daemon/daemon-supervisor.ts` |
| Session worker | 拥有一个根 session tree、scheduler、kernels 和 descendants | supervisor、AgentSessionRuntime | `core/agent-session-runtime.ts` |
| AgentSession | provider 流、prompt queue、tools、compaction、goals、children、transcript | provider、kernel、storage | `core/agent-session.ts` |
| RLM runtime | 创建子 session，维护 child lifecycle 和 host bridge | AgentSession、IPython | `core/rlm-runtime.ts` |
| Python harness | 暴露模型可编程的 skills 和 RLM 接口 | typed host request | `prime-agent-runtime/src/rlm/` |
| Scheduler | heartbeat、cron 和一次性 prompt 的持久交付 | session queue | `core/cron-jobs.ts` and daemon heartbeat modules |
| Continuation policy | goal/autonomous 状态和继续条件 | prompt queue、quality gates | `core/goals.ts`, `core/autonomous.ts` |
| Compaction | 压缩旧上下文但保留外部状态 | AgentSession、transcript | `core/compaction/` |

# Prompt and Control Flow

```text
User / schedule / heartbeat / goal / autonomous / peer agent
                          |
                          v
                   Session prompt queue
                          |
                          v
                     AgentSession
                          |
                    model stream
                          |
                optional IPython call
                          |
       ordinary Python or typed host request
                          |
              host-authoritative operation
                          |
            transcript + event + artifact
```

# Persistence Boundaries

- Conversation events: append-oriented JSONL transcript.
- Feature state: session artifact directory.
- Execution state: resident IPython kernel, with selected snapshots/recovery mechanisms.
- Child identity: parent-scoped registry designed to survive compaction and restoration.
- Schedule state: session-owned persisted jobs.
- UI state: client concern, not execution ownership.

# Long-task State Machine

```text
Active turn ends
  -> goal active? preserve objective and progress
  -> autonomous policy requests continuation? check limits and gates
  -> scheduled/heartbeat prompt due? claim then enqueue
  -> context near limit? compact, do not mark complete
  -> client detached? worker continues
  -> explicit completion / pause / clear / terminal error
```

# Extension Points

- Model providers in `packages/ai/`.
- Instruction-only and Python-backed skills under `packages/coding-agent/skills/`.
- Custom extensions under coding-agent examples and extension loader.
- JSON/RPC/ACP-style headless integrations under `modes/`.

# Research Entry Points

- Background continuity: `docs/long-running-agents.md`, then `modes/daemon/`.
- Reconnect protocol: `docs/agent-connection.md`, then `modes/agent-connection/`.
- Subagents: `docs/rlm.md`, `docs/rlm-runtime.md`, then `core/rlm-runtime.ts`.
- Goals/autonomy: `core/goals.ts`, `core/autonomous.ts`, `core/agent-session.ts`.
- Compaction: `core/compaction/`.
- Skills and host bridge: `docs/skills.md`, `prime-agent-runtime/src/rlm/`.

# Boundaries and Risks

- The kernel and worker normally inherit user permissions.
- A persistent process increases credential, filesystem and prompt-injection exposure.
- Exactly-once external effects are not guaranteed merely by claiming a scheduled prompt; product code still needs idempotency.
- Recovery across schema or binary versions requires explicit migration policy.
- Long-lived Agent state needs retention, redaction and deletion controls.

