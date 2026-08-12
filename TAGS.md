# Tag Index

本文件是能力入口，不是关键词堆积。先按能力命中候选，再读对应 `30 秒快速判断` 和复用边界。

CLI 会做轻量双语归一化，包括：`后台任务 / background task / long-running task`、`子 Agent / subagent / child agent`、`系统代理 / system proxy / network proxy`、浏览器渲染、Agent Skills、调度、RAG 和 Bot。不使用 embedding；Markdown 仍是唯一权威来源。

## AI Agent

- `long-running-agent` `background-agent` `daemon` `session-resume` -> [Prime Agent Summary](AI-Agent/prime-agent/SUMMARY.md)
- `heartbeat` `scheduler` `persistent-goal` `autonomous-agent` -> [Prime Agent Reuse Guide](AI-Agent/prime-agent/REUSE_GUIDE.md)
- `subagent` `agent-to-agent` `context-compaction` `context-persistence` -> [Prime Agent Architecture](AI-Agent/prime-agent/ARCHITECTURE.md)
- `skills` `continual-harness` -> [Prime Agent Status](AI-Agent/prime-agent/STATUS.md)
- `pi-agent` `coding-agent` `agent-runtime` `tool-system` -> [Pi Architecture](Research/pi-agent/ARCHITECTURE.md)
- `session` `session-persistence` `session-resume` `fork` `branch` -> [Pi Session](Research/pi-agent/SESSION.md)
- `context-compaction` `context-overflow` `token-budget` -> [Pi Compaction](Research/pi-agent/CONTEXT_COMPACTION.md)
- `extensions` `hooks` `plugin-architecture` -> [Pi Extensions](Research/pi-agent/EXTENSIONS.md)
- `skills` `progressive-disclosure` `knowledge-router` -> [Pi Skills](Research/pi-agent/SKILLS.md)
- `provider` `streaming` `sdk` `rpc` -> [Pi Provider and SDK/RPC](Research/pi-agent/PROVIDER_LAYER.md)
- `ai-novel-studio` `chief-writer-reviewer` `architecture-lessons` -> [Pi Lessons for AI Novel Studio](Research/pi-agent/AI_NOVEL_STUDIO_LESSONS.md)

## AI Engineering

- `spec` `planning` `incremental-implementation` `tdd` `ci-cd` `deployment` -> [Addy Agent Skills Reuse Guide](AI-Engineering/addyosmani-agent-skills/REUSE_GUIDE.md)
- `api-design` `frontend` `security` `performance` `observability` `documentation` `git-workflow` -> [Addy Agent Skills Summary](AI-Engineering/addyosmani-agent-skills/SUMMARY.md)
- `grill-me` `requirements` `domain-modeling` `test-seam` -> [Matt Pocock Skills Reuse Guide](AI-Engineering/mattpocock-skills/REUSE_GUIDE.md)
- `debugging` `feedback-loop` `code-review` `handoff` `research` `writing-for-agents` -> [Matt Pocock Skills Summary](AI-Engineering/mattpocock-skills/SUMMARY.md)
- `agent-skills-comparison` -> [Detailed Comparison](Comparisons/agent-skills-comparison.md)

## Browser

- `browser` `web-engine` `renderer` `loading-to-painting` -> [Ladybird Summary](Browser/ladybird/SUMMARY.md)
- `browser-process` `multi-process` `ipc` `site-isolation` `sandbox` -> [Ladybird Architecture](Browser/ladybird/ARCHITECTURE.md)
- `javascript-engine` `wasm` `libjs` `libwasm` -> [Ladybird Reuse Guide](Browser/ladybird/REUSE_GUIDE.md)
- `network-stack` `request-server` `image-decoder` `compositor` `web-worker` -> [Ladybird Architecture](Browser/ladybird/ARCHITECTURE.md)
- `web-platform-tests` `pre-alpha` `security-incomplete` -> [Ladybird Status](Browser/ladybird/STATUS.md)

## Network

- `proxy` `system-proxy` `network-configuration` -> [fanqiang Reuse Guide](Network/fanqiang/REUSE_GUIDE.md)
- `windows` `linux` `android` `ios` `macos` `router` `openwrt` -> [fanqiang Summary](Network/fanqiang/SUMMARY.md)
- `v2ray` `xray` `shadowsocks` `clash` `tor` -> [fanqiang Reuse Guide](Network/fanqiang/REUSE_GUIDE.md)
- `historical` `deprecated` `untrusted-binary` `needs-verification` -> [fanqiang Status](Network/fanqiang/STATUS.md)

## Decision Tags

- `reuse` `adapt` `reference` `replace` `build`: 搜索所有 `REUSE_GUIDE.md` 的决策表。
- `historical` `needs-verification` `security-sensitive`: 搜索所有 `STATUS.md`。
- `architecture`: 先查 Prime Agent 与 Ladybird 的 `ARCHITECTURE.md`，再按具体模块进入本地源码。
