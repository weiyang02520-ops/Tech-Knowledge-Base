# Universal AI Tech Knowledge Base

跨 AI 工具通用技术资料库。它把值得研究的开源项目整理成可搜索、可比较、可追溯的技术地图，帮助 AI 在开始开发前先检查已有方案，再决定复用、改造、参考、替换或自行实现。

## 核心原则

- Markdown 是主知识源，不运行脚本也能完整理解。
- 工具无关：不把核心知识锁在 Codex、Claude Code、Trae、WorkBuddy、Cursor 或某个插件中。
- 先检索再实现：`Need -> Capability -> Search -> Existing Wheel -> Evaluate -> Reuse / Adapt / Reference / Build`。
- 事实、分析和建议分开表达；无法确认的内容标记 `Unknown` 或 `Needs Verification`。
- 第三方源码只用于本地静态分析，`source/` 永不进入公开知识库。
- 不复制大段第三方 README、文档或源码；公开内容是独立分析、索引和复用指南。

## 推荐阅读顺序

```text
ROUTER.md (only decides whether retrieval is worthwhile)
  -> python tools/kb.py search "<capability>"
  -> kb.py show / reuse
  -> <project>/ARCHITECTURE.md (如有)
  -> <project>/source/ (仅在确有必要时)
```

平时不预读知识库。普通检索最多返回 3 个候选，并明确下一条命令；没有高相关结果时立即停止本地检索。

## 当前收录

| 领域 | 项目 | 主要用途 |
| --- | --- | --- |
| Network | bannedbook/fanqiang | 网络代理与相关工具的历史和现状地图 |
| AI Agent | PrimeIntellect-ai/prime-agent | 长时间运行、自主和持久化 Agent 架构 |
| AI Engineering | addyosmani/agent-skills | 面向 AI 编程 Agent 的工程方法库 |
| AI Engineering | mattpocock/skills | 需求澄清、诊断、交付与工程工作流 |
| Browser | LadybirdBrowser/ladybird | 独立浏览器及 Web 引擎架构地图 |

## 使用入口

- 自动判断规则：[ROUTER.md](ROUTER.md)
- 轻量跨工具 CLI：`python tools/kb.py --help`
- 按项目浏览：[CATALOG.md](CATALOG.md)
- 按能力和关键词浏览：[TAGS.md](TAGS.md)
- AI 和人工检索方法：[SEARCH_GUIDE.md](SEARCH_GUIDE.md)
- 各类 AI 工具接入方式：[HOW_TO_USE.md](HOW_TO_USE.md)
- 第三方项目与许可说明：[ATTRIBUTION.md](ATTRIBUTION.md)
- 当前建设状态：[PROGRESS.md](PROGRESS.md)
- GitHub 公开发布检查：[PUBLICATION_AUDIT.md](PUBLICATION_AUDIT.md)
- Router 验收记录：[ROUTER_TESTS.md](ROUTER_TESTS.md)

## 数据结构

每个项目目录至少包含：

- `META.md`：上游、版本、许可证、语言和分析范围。
- `SUMMARY.md`：快速理解项目是什么以及是否值得继续阅读。
- `REUSE_GUIDE.md`：已有轮子、复用边界和仍需自行实现的部分。
- `STATUS.md`：项目与组件的当前参考等级和验证状态。
- `ARCHITECTURE.md`：复杂项目的模块、数据流和源码入口地图。
- `source/`：浅克隆的第三方源码，仅存在于本地并被 Git 忽略。

## License

本知识库尚未选择最终许可证。候选方案和边界见 [LICENSE-RECOMMENDATION.md](LICENSE-RECOMMENDATION.md)。在许可证确定前，不应把本仓库描述为已经完成正式开源授权。

## Disclaimer

本仓库不是上游项目的官方文档，也不代表上游作者立场。状态和安全判断仅对应 `META.md` 记录的提交和分析日期。网络、安全及代理相关内容只做静态技术研究，使用者应自行确认当地法律、服务条款和当前安全状态。
