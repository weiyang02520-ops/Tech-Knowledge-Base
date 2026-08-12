# Overall Status

- Rating: `A` for architecture research; `C` for end-user or security-critical production use
- Confidence: High for module map, Medium for exact runtime topology
- Evaluated commit: `8d225a329ee852510b4522e04d357c6fdd51d7f7`
- Evaluation date: 2026-08-09

# Evidence

- README 明确标记 `pre-alpha` 且只适合开发者。
- 当前源码有清晰的 UI、Libraries、Services、Tests 分区和独立进程入口。
- 20,293 个测试文件显示标准兼容测试是核心工程资产，但数量不等于全部通过。
- `ProcessArchitecture.md` 明确说明部分内容是目标态；当前代码已超出旧图。
- SECURITY 明确列出尚未完整实现的 Web 安全能力。

# Component Status

| Component | Rating | Confidence | Reason | Revalidation Trigger |
| --- | --- | --- | --- | --- |
| 架构学习地图 | A | High | 模块和入口清晰，覆盖完整浏览器栈。 | 顶层目录重构。 |
| LibWeb pipeline | A/B | High | 文档和源码分区吻合，部分文档仍标 WIP。 | layout/painting 架构重大变化。 |
| LibJS/LibWasm 学习 | A/B | Medium | 独立实现有研究价值，生产性能/兼容需实测。 | runtime 设计变化。 |
| 多进程与 IPC | A/B | Medium | 当前 service 明确，精确拓扑动态。 | site isolation/process manager 变化。 |
| Test corpus | A | High | 大量 WPT/LibJS 测试提供入口。 | 上游测试导入策略变化。 |
| End-user browser | C | High | 上游明确为 pre-alpha。 | 正式稳定发布。 |
| Security-critical runtime | C/UNKNOWN | High | 多项安全能力未完成。 | 安全政策和 sandbox 保证升级。 |

# Known Risks

- 文档可能落后于快速变化的代码。
- pre-alpha API、行为、兼容性和构建要求不稳定。
- 浏览器攻击面巨大，进程分离本身不能证明安全。
- 第三方媒体、图形、国际化等依赖带来额外供应链边界。
- 浅克隆无法用于历史演化和回归时间线研究。

# Needs Verification

- 当前标签/站点隔离粒度和每个平台实际进程拓扑。
- Linux、macOS、Android 和 WSL2 的 sandbox 差异。
- 目标 Web API、网站和 WPT 子集的通过情况。
- 作为库嵌入的 API 稳定性、发布形式和支持承诺。

