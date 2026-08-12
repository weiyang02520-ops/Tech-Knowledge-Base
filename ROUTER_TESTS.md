# Router Acceptance Tests

The deterministic router simulation is implemented by `python tools/kb.py route "<task>"`; the complete executable suite is in `tests/test_kb.py` and uses only Python's standard library.

## Expected Query

| Task | Expected |
| --- | --- |
| 做一个长期后台 Agent | QUERY |
| 给 QQ Bot 做定时任务系统 | QUERY |
| 设计一个浏览器渲染模块 | QUERY |
| 给项目增加系统代理支持 | QUERY |
| 该选哪种 Agent Skills | QUERY |
| 做一个新的 RAG 框架 | QUERY |
| 设计一个支持故障恢复的数据库任务调度系统 | QUERY |
| 比较几种 MCP 服务架构 | QUERY |
| 集成一套通用自动化工作流 | QUERY |
| 实现一个新的 DevTools 系统 | QUERY |

## Expected Skip

| Task | Expected |
| --- | --- |
| README 改个错别字 | SKIP |
| 变量 foo 改成 bar，简单重命名 | SKIP |
| 这个函数少一个分号 | SKIP |
| 把按钮从左边移动到右边 | SKIP |
| 解释这三行代码 | SKIP |
| 修复当前文件已明确定位的空指针 | SKIP |
| format these imports | SKIP |
| 润色这一段文档 | SKIP |
| 把常量 1 改成 2 | SKIP |
| 给现有测试补一条已经写明的断言 | SKIP |

## Acceptance Result

Executed on 2026-08-09 with Python 3.14.4:

- Correct decisions: 20/20
- Correct QUERY triggers: 10/10
- Correct SKIP decisions: 10/10
- False triggers: 0
- Misses: 0
- Full CLI/unit suite: 14/14 passed

The suite also verifies every documented CLI command, a maximum of three search results, bilingual aliases, unknown projects, empty capability input, missing architecture documents, human-readable errors without tracebacks, no-match stopping, and one-section progressive extraction.
