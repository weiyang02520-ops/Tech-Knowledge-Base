# 何时应该先查这个项目

当标准开发流程仍无法回答“需求到底是什么”“在哪个 seam 测”“为什么这个 bug 发生”“审查基准是什么”或“下一个 Agent 如何无损接手”时，先查本项目。

# 功能：Grilling 与需求澄清

- 已有方案：持续追问设计树的未决分支；`grill-with-docs` 同时维护领域词汇和 ADR。
- 可以复用：一次聚焦一个真正改变设计的分支；用具体场景暴露含糊语言。
- 可以改造：普通任务应设停止条件，避免无休止访谈。
- 不建议复制：把强追问用在用户已经给出完整、已批准规格的阶段。
- 成熟度：核心思想 `A`。

# 功能：Domain Modeling

- 已有方案：`CONTEXT.md` 只保存领域 glossary；实现决策另进 ADR；仅在难逆、反直觉且存在真实权衡时写 ADR。
- 可以复用：术语与实现分离、情景压力测试、代码与口头模型冲突时立即上报。
- 需要适配：文件名和 bounded-context 布局可按项目现状调整。
- 成熟度：`A`。

# 功能：Spec、Tickets 与实现

- 已有方案：规格写用户问题、用户故事、实现/测试决定和范围；票据按垂直切片；实现围绕预先同意的 seam 做 TDD。
- 可以复用：不在长期规格里写易腐烂的具体文件路径；优先高层行为 seam；完整测试只在最终阶段跑一次，局部测试高频运行。
- 风险：部分流程要求发布到 issue tracker，属于外部写操作，不能默认执行。
- 成熟度：`A/B`。

# 功能：Bug Diagnosis

- 已有方案：先建立能对用户真实症状变红的、快速、确定、Agent 可运行的反馈环；最小化后再列 3-5 个可证伪假设；一次改变一个变量。
- 可以复用：没有 red-capable loop 就不进入猜原因阶段；调试日志加唯一标记并在结束时清除；性能问题先测量。
- 需要适配：无法自动化的生产问题可能需要脱敏 trace 或经批准的临时观测。
- 成熟度：`A`。

# 功能：Two-axis Code Review

- 已有方案：固定 merge-base 后独立检查 Standards 和 Spec，避免一个轴的好结果掩盖另一个轴的失败。
- 可以复用：固定比较点、追溯需求来源、区分规范违反和启发式 smell。
- 可以改造：没有子 Agent 时可串行执行，但必须保持上下文和报告分区。
- 风险：只原样聚合两个报告可能缺少统一严重度排序，实际团队仍需最终 triage。
- 成熟度：`A/B`。

# 功能：Handoff 与 Agent 文档

- 已有方案：交接只写尚未被 spec/plan/ADR/commit 捕获的内容，引用现有成果而不重复，且必须脱敏。
- 可以复用：上下文指针、渐进披露、明确完成条件、单一事实源和主动删减陈旧内容。
- 需要改造：本知识库的长期结论必须写入项目目录，不能只放操作系统临时目录。
- 成熟度：`A` for principles, `C` for the original temp-only storage rule in this use case。

# 不要重复造轮子的部分

- tight/red-capable feedback loop 的诊断框架。
- glossary 与 ADR 的边界。
- Standards/Spec 两轴审查。
- 交接文档的引用、去重和脱敏原则。
- Agent 文档的 context pointer、信息层级和 completion criteria。

# 仍然值得自己实现的部分

- 与团队实际 issue tracker、审批和权限匹配的发布步骤。
- 没有子 Agent 时的顺序化执行方案。
- 任务复杂度对应的访谈停止条件。
- 领域自己的词汇、测试 seam 和验收证据。

# 决策表

| Capability | Decision | Reason |
| --- | --- | --- |
| 需求 grilling | Selective reuse | 高价值但不应对明确小任务强制使用。 |
| Domain glossary/ADR | Reuse | 能显著减少跨会话语义漂移。 |
| Bug diagnosis loop | Reuse | 证据优先，适用于多技术栈。 |
| Two-axis review | Adapt | 无子 Agent 时仍可保留分轴。 |
| Issue tracker 发布 | Adapt / Ask first | 是外部写操作且平台不同。 |
| Temp-only handoff | Replace | 长期资料必须进入项目主知识源。 |
| `in-progress` Skills | Reference | 尚未达到稳定默认级别。 |

