# 一句话说明

Ladybird 是一个从独立 Web 标准实现发展而来的 pre-alpha 浏览器，其最大研究价值是完整展示浏览器 UI、渲染、JavaScript、网络、图片解码、合成、IPC 和 sandbox 如何分层。

# 它解决什么问题

现代网页是不可信的复杂程序。浏览器既要解析 HTML/CSS、执行 JavaScript、布局和绘制，又要访问网络、解码媒体并隔离故障和攻击面。Ladybird 通过专用库和多进程 service 拆分这些职责。

# 核心功能

- 独立的 HTML/CSS 渲染引擎 LibWeb。
- JavaScript 引擎 LibJS 和 WebAssembly 实现 LibWasm。
- UI、WebContent、Compositor、RequestServer、ImageDecoder、WebWorker、WebDriver 等边界。
- IPC 接口、进程管理、站点隔离相关结构和平台 sandbox。
- Qt、AppKit、Android UI 端口。
- 大量 Web Platform Test 导入及引擎测试。

# 核心技术

C++ 为主，使用 CMake；部分组件使用 Rust、JavaScript、HTML、Python 和平台原生语言。引擎按 Web 标准实现 DOM、CSSOM、HTML parser、Fetch、Layout、Painting、JS runtime 和大量 Web API。

# 主要目录

先读 `Documentation/`；浏览器壳和进程管理看 `UI/`、`Libraries/LibWebView/`、`Services/`；网页管线看 `Libraries/LibWeb/`；语言运行时看 `Libraries/LibJS/` 和 `Libraries/LibWasm/`；验证覆盖看 `Tests/`。

# 主要模块

- UI/Browser process：窗口、标签、地址栏、配置、历史和权限交互。
- WebContent：LibWeb + LibJS 所在的页面执行与渲染服务。
- RequestServer：网络请求、缓存、WebSocket 和解析相关入口。
- ImageDecoder：将不可信图片解码移出 renderer。
- Compositor：backing store、帧提交、滚动、vsync 和合成。
- WebWorker：Worker 执行边界。
- LibWeb：从加载到 DOM/CSSOM/layout/paint 的标准实现。

# 工作方式

UI 通过 LibWebView 的进程和连接对象管理页面服务。WebContent 请求网络资源，解析 HTML/CSS，运行 JavaScript，计算样式，构建 layout tree 和 paint tree，再把可显示结果交给 compositor/UI。图片解码和网络访问被拆到专用进程以限制故障面。

# 适合什么场景

- 学习浏览器多进程和 IPC 设计。
- 定位 Web API、HTML、CSS、JS、Wasm、layout 或 painting 的实现入口。
- 设计处理不可信内容的 Web runtime、previewer 或文档渲染器。
- 研究 Web Platform Tests 如何驱动兼容性。

# 不适合什么场景

- 作为普通用户的稳定默认浏览器。
- 假定已完成所有 Web 安全特性或生产级 sandbox。
- 为了一个小型 HTML 预览需求直接复用整个浏览器。
- 通过逐行阅读数千万字节源码来获得“全量理解”。

# 最值得看的东西

进程/权限边界、`LibWebFromLoadingToPainting.md`、`LibWebView::ProcessManager`、各 `Services/*/main.cpp`、LibWeb 的 HTML/CSS/Layout/Painting 目录、IPC 定义和 WPT 测试布局。

# 可以暂时不看的东西

20,000 多个测试输入、所有 Web API 细节、每个平台 UI、构建依赖、字体/媒体/图像格式的全部实现，以及与当前问题无关的标准角落。

# 对本资料库的价值

它提供一张可沿模块逐层深入的浏览器架构地图，使后续 AI 能先定位现有职责和入口，而不是从零猜测 renderer、JS engine、network、IPC 和 sandbox 的关系。

# 30 秒快速判断

需求涉及浏览器/Web runtime 架构、渲染管线、进程隔离或某项 Web 标准实现时值得查；需要可直接嵌入的稳定浏览器内核时，应评估成熟引擎，Ladybird 当前主要用于学习和研究。

