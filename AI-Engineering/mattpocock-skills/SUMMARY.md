# 一句话说明

这是一组偏“强交互和深推理”的工程 Skill，擅长把模糊设计追问清楚、建立领域语言、找到正确测试接缝、用紧反馈环排错，并把工作交接给下一个 Agent。

# 它解决什么问题

即使有标准开发流程，AI 仍可能接受含糊词、从错误接缝测试、没有复现就猜 bug、审查时把“符合规范”和“符合需求”混为一谈，或在长会话结束时丢失状态。该仓库为这些高风险节点提供专用流程。

# 核心功能

- `grill-me` / `grilling` / `grill-with-docs`：持续追问直到设计分支清晰。
- `domain-modeling`：维护 ubiquitous language、情景边界和少量必要 ADR。
- `to-spec` / `to-tickets` / `implement`：从讨论到规格、垂直切片和实现。
- `tdd` / `diagnosing-bugs`：围绕正确 seam 和 tight red-capable loop 工作。
- `code-review`：把 Standards 与 Spec 两个审查轴分开。
- `research`、`handoff`、`writing-for-agents`：来源研究、跨会话交接和 Agent 文档设计。
- 原型、架构改进、冲突解决、triage 和人工操作 wizard。

# 核心技术

主体是 Markdown Skill。部分流程假定能够创建并行子 Agent、访问 issue tracker、写临时文件或调用其它 Skill；这些是执行适配，不是核心工程思想。

# 主要目录

优先看 `skills/engineering/` 和 `skills/productivity/`。`skills/misc/` 较具体，`skills/in-progress/` 应默认视为实验材料。

# 主要模块

需求追问、领域模型、规格/票据、实现、测试、诊断、审查、研究、交接、Agent 文档和少数环境配置流程。

# 工作方式

它不追求一个统一的全生命周期模板，而是为关键认知瓶颈定义强约束动作。例如诊断先制造能捕获真实症状的反馈环；审查固定 diff 基点并分离两个评价轴；领域术语一旦澄清立即写回 glossary。

# 适合什么场景

- 需求复杂、术语模糊或利益相关者认知不一致。
- 难复现 bug、性能回退和需要系统实验的故障。
- 规格与代码规范可能分别失败的审查。
- 长任务跨 Agent、跨会话交接。
- 需要让 Agent 文档保持精简、可触发和可验证。

# 不适合什么场景

- 用户只希望快速完成明确的小改动。
- 环境没有子 Agent、Issue Tracker 或对应命令，却机械照搬执行步骤。
- 把 `in-progress` 内容作为稳定默认规则。
- 无视项目现有流程而强制引入整套术语体系。

# 最值得看的东西

`diagnosing-bugs` 的 tight red loop、`domain-modeling` 的 glossary/ADR 边界、`code-review` 的 Standards/Spec 分轴、`writing-for-agents` 的上下文指针与信息层级、`handoff` 的去重和脱敏。

# 可以暂时不看的东西

具体包迁移、练习脚手架、Claude 专用 Git hook、实验性写作 Skill 和特定 issue tracker 设置。

# 对本资料库的价值

它补足标准生命周期方法中最容易被简化的认知工作，尤其适合成为需求澄清、疑难诊断、知识写作和长任务交接的专项参考。

# 30 秒快速判断

任务的难点是“想清楚、证伪、统一语言或可靠交接”时优先查；需要团队级完整交付基线时，以 Addy 的生命周期体系为主，再按需引入本仓库的专项方法。

