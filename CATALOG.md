# Project Catalog

## Lightweight Entry

Do not load this catalog into every conversation. Run `python tools/kb.py search "<capability>"`; it derives results from this catalog, `TAGS.md`, project metadata and project documents, and returns at most three candidates.

| Domain | Project | Upstream | Best For | Research / Adoption | Documents |
| --- | --- | --- | --- | --- | --- |
| Network | fanqiang | [bannedbook/fanqiang](https://github.com/bannedbook/fanqiang) | 跨平台代理概念和历史地图 | `C` / `D-UNKNOWN` | [Summary](Network/fanqiang/SUMMARY.md) · [Reuse](Network/fanqiang/REUSE_GUIDE.md) · [Status](Network/fanqiang/STATUS.md) |
| AI Agent | prime-agent | [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) | 长任务、后台会话、目标、调度和子 Agent | `A` / `B` | [Summary](AI-Agent/prime-agent/SUMMARY.md) · [Reuse](AI-Agent/prime-agent/REUSE_GUIDE.md) · [Architecture](AI-Agent/prime-agent/ARCHITECTURE.md) · [Status](AI-Agent/prime-agent/STATUS.md) |
| AI Agent | pi-agent | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) | Agent runtime、会话树、上下文压缩、工具、扩展、Skills 与 SDK/RPC | `A` / `reference` | [Index](Research/pi-agent/README.md) · [Architecture](Research/pi-agent/ARCHITECTURE.md) · [Source Map](Research/pi-agent/SOURCE_MAP.md) · [Novel Lessons](Research/pi-agent/AI_NOVEL_STUDIO_LESSONS.md) |
| AI Engineering | addyosmani-agent-skills | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 完整软件交付生命周期基线 | `A` / `B` | [Summary](AI-Engineering/addyosmani-agent-skills/SUMMARY.md) · [Reuse](AI-Engineering/addyosmani-agent-skills/REUSE_GUIDE.md) · [Status](AI-Engineering/addyosmani-agent-skills/STATUS.md) |
| AI Engineering | mattpocock-skills | [mattpocock/skills](https://github.com/mattpocock/skills) | 深度追问、领域语言、诊断和交接 | `A` selected / `B` collection | [Summary](AI-Engineering/mattpocock-skills/SUMMARY.md) · [Reuse](AI-Engineering/mattpocock-skills/REUSE_GUIDE.md) · [Status](AI-Engineering/mattpocock-skills/STATUS.md) |
| Browser | ladybird | [LadybirdBrowser/ladybird](https://github.com/LadybirdBrowser/ladybird) | 浏览器进程、Web 引擎和渲染管线 | `A` / `C` | [Summary](Browser/ladybird/SUMMARY.md) · [Reuse](Browser/ladybird/REUSE_GUIDE.md) · [Architecture](Browser/ladybird/ARCHITECTURE.md) · [Status](Browser/ladybird/STATUS.md) |

## Comparison Entry

- [Addy Osmani Agent Skills vs Matt Pocock Skills](Comparisons/agent-skills-comparison.md)

## Reading Rule

`Research` 评价项目作为架构/方法参考的价值；`Adoption` 评价直接采用当前实现的谨慎程度。两者不能互换。例如 Ladybird 的架构研究价值为 A，但上游明确是 pre-alpha，因此直接作为安全关键浏览器只有 C/UNKNOWN。

## Status Scale

- `A`: 当前非常值得优先参考。
- `B`: 仍然值得参考。
- `C`: 思想值得参考，部分实现可能较旧或适用范围有限。
- `D`: 明显较旧，通常只保留历史价值。
- `E`: 当前基本没有使用必要。
- `UNKNOWN`: 证据不足，需要重新验证。
