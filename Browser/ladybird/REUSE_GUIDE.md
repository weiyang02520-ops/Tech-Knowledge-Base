# 何时应该先查这个项目

当需求涉及浏览器 renderer、HTML/CSS engine、JavaScript runtime、WebAssembly、网络服务、图片解码、compositor、IPC、site isolation 或处理不可信 Web 内容时，应先查 Ladybird 的模块地图。

# 功能：多进程 Browser Architecture

- 已有方案：UI/browser process 通过 LibWebView 管理 WebContent 和辅助服务；网络、图片解码、合成、Worker 和自动化各有独立边界。
- 可以借鉴：把高复杂度、不同权限和高风险输入拆到进程边界；IPC contract 显式化。
- 可以改造：小型 runtime 可减少进程数，但仍应保留权限边界。
- 不建议复制：旧架构图中的具体 spawn 路径或进程数量；文档已说明部分是目标态。
- 风险：跨进程生命周期、共享图像、backpressure、崩溃恢复和平台 sandbox 差异。
- 成熟度：设计思想 `A`，精确实现状态 `B/Needs Verification`。

# 功能：Browser Renderer / LibWeb

- 对应模块：`Libraries/LibWeb/{Loader,HTML,DOM,CSS,Layout,Painting,Page}`。
- 基本管线：资源加载 -> HTML/DOM -> CSS/CSSOM -> JS -> style -> layout tree -> paint tree/stacking contexts -> compositor。
- 可以学习：规范驱动 parser、CSS cascade、formatting context、layout state、paintable 和 stacking context 的职责。
- 不建议复制：为小型产品复制整个 Web 标准面；兼容性长尾和安全维护成本极高。
- 如果自己做 Web Runtime：复用成熟引擎通常优先；若目标是研究或受限格式，可借鉴管线并严格缩小标准范围。

# 功能：JavaScript Engine 与 WebAssembly

- 对应模块：`Libraries/LibJS/{Bytecode,Heap,Interpreter,Runtime}`、`Libraries/LibWasm/`。
- 可以学习：语言 parser/runtime、GC、host binding 与 Web API 的边界。
- 不要重复造轮子：生产 JS 语义、优化器、GC 和标准兼容通常应复用成熟 runtime。
- 仍可自己实现：教学解释器、受限 DSL、确定性 sandboxed expression runtime。

# 功能：Network / RequestServer

- 对应模块：`Services/RequestServer/`、`Libraries/LibRequests/`、`LibHTTP`、`LibTLS`、`LibDNS`。
- 可以借鉴：把网络权限和 cache/WebSocket 管理移出 renderer，通过 IPC 返回受控数据。
- 不建议复制：把同步网络、DNS、证书和 cookie 处理混入页面执行线程。
- 风险：当前实现细节和第三方库边界需按平台复核。

# 功能：Image Decoder 与 Compositor

- ImageDecoder 展示了如何隔离不可信编码数据；Compositor 展示 backing store、帧、滚动、vsync 和呈现职责。
- 可以借鉴：解码器进程化、按内容类型限制权限、共享缓冲区的显式所有权、UI 与页面绘制解耦。
- 仍需自行实现：目标 GPU/窗口系统的同步、资源预算和崩溃降级。

# 功能：Sandbox 和 Security

**Fact:** 上游安全政策明确指出许多 Web 安全特性尚未完成，并列出当前不按安全漏洞处理的若干类别。README 同时标明 pre-alpha。

**Recommendation:** 学习边界，不要把 Ladybird 当前构建当成已验证的安全容器。生产使用必须有独立威胁建模、平台 sandbox 复核和安全测试。

# 不要重复造轮子的部分

- 完整 HTML/CSS/JS/Wasm 标准实现。
- Web Platform Tests 的生态与兼容性用例。
- 进程、IPC、解码和合成职责划分的基本概念。
- 成熟浏览器已有的安全模型和站点隔离研究。

# 仍然值得自己实现的部分

- 只支持受限文档格式的轻量 renderer。
- 产品特定 UI、权限提示、历史、书签和策略层。
- 业务所需的进程监管、资源配额和崩溃恢复。
- 对既有成熟引擎的薄封装和安全策略。
- 教学或研究目的的 parser/runtime 子集。

# 决策表

| Capability | Decision | Reason |
| --- | --- | --- |
| Browser process model | Reference / Adapt | 结构价值高，当前实现快速演化。 |
| Full LibWeb/LibJS embedding | Needs Evaluation | pre-alpha、API 和兼容性风险高。 |
| Loading-to-painting concepts | Reuse concept | 稳定的浏览器工程知识。 |
| IPC/service boundaries | Adapt | 需匹配平台和威胁模型。 |
| Production security sandbox | Build/Reuse mature platform | Ladybird 当前不构成完整安全保证。 |
| Small product-specific UI | Build | 属于产品差异化。 |
| Web standards tests | Reuse where license/scope permits | 避免自行发明兼容性判断。 |

