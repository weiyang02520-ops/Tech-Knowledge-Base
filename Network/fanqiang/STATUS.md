# Overall Status

- Rating: `C`
- Confidence: Medium
- Evaluated commit: `3eed6fb9871dcda66f2071b7ce3977c62501d603`
- Evaluation date: 2026-08-09
- Security sensitivity: High

仓库作为概念、平台和历史地图仍有价值；作为当前安装源或安全指南不应直接使用。最近提交时间只说明仓库活跃，不代表所有 1,874 个文件都已复核。

# Evidence

- 根目录按多个平台和场景组织，覆盖面广。
- 存在明确的 `deprecated/`，但非 deprecated 区域也包含旧工具、推广链接和未绑定版本的教程。
- 仓库混有 Android 应用源码、脚本、压缩/可执行资产入口，不是纯文档库。
- 没有明确的仓库级标准许可证；组件许可证不能覆盖全部内容。
- 若干当代上游仍活跃，但 Clash/Mihomo 名称和仓库关系出现明显变化，证明动态复核不可省略。

# Component Status

| Component | Rating | Confidence | Reason | Revalidation Trigger |
| --- | --- | --- | --- | --- |
| 跨平台能力地图 | B | High | 分类覆盖系统、客户端、协议和网关层。 | 平台目录结构大幅变化。 |
| V2Ray/Xray 线索 | B | Medium | 当前仍有活跃上游；仓库教程版本不统一。 | 核心协议或官方上游迁移。 |
| Shadowsocks 线索 | B/C | Medium | 生态仍在，但具体实现维护方向不同。 | 客户端或核心停止维护。 |
| Clash-family 线索 | UNKNOWN | High | 名称、仓库和继任关系动态变化。 | 每次形成实际推荐前。 |
| Tor 概念 | B | Medium | 架构和官方入口仍有参考价值。 | 安装和平台支持问题。 |
| 路由器/旁路由概念 | B | Medium | 网络拓扑思想稳定，命令和插件动态。 | 固件、插件或硬件变化。 |
| `deprecated/` | D | High | 明确为历史资料。 | 仅历史研究时。 |
| 一键包、APK、脚本、二进制 | E/UNKNOWN | High | 未在本次验证来源、构建链、签名和安全性。 | 不建议直接使用。 |

# Known Risks

- 高权限网络软件的供应链和隐私风险。
- 推广、免费节点和第三方服务链接可能存在商业偏向或失效。
- 旧截图和旧配置可能误导当前用户。
- 仓库级许可不清晰，不能公开再分发第三方内容。

# Needs Verification

- 每个具体客户端的官方仓库、当前名称、支持平台和稳定版本。
- 所有外部下载链接、签名、哈希和发布主体。
- 各地区法律、服务条款以及网络环境适用性。
- 仓库内每个应用子项目的独立许可证边界。

