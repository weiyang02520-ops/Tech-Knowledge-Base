# Agent Skills Repositories Comparison

## Scope

- Addy Osmani: `addyosmani/agent-skills` at `7676817c12a1317454ae3898a0c5c1eacf5dd3d5`
- Matt Pocock: `mattpocock/skills` at `84fdeffd12f2ee307994d1eb6feb48173b6e0502`
- Analysis date: 2026-08-09

这不是逐行内容对照，而是判断哪些工程方法适合抽成所有 AI 工具都能使用的普通 Markdown 知识。

## Executive Difference

Addy 的仓库回答“一个团队应怎样建立完整、可重复的软件交付主线”；Matt 的仓库回答“在最需要思考的节点，Agent 应怎样逼近真实问题并留下可接手的决策”。前者宽而统一，后者窄而锋利。

## Feature Matrix

| Dimension | addyosmani/agent-skills | mattpocock/skills | Recommended Use |
| --- | --- | --- | --- |
| Overall shape | 24 个平铺 Skill，按生命周期路由 | 35 个 Skill，按 engineering/productivity/misc/in-progress 分组 | Addy 做主干，Matt 做专项补强 |
| Requirements | interview + idea refine + formal spec | relentless grilling + domain scenarios | 模糊需求优先 Matt，稳定落档采用 Addy spec |
| Planning | 依赖图、原子任务、验收与验证 | wayfinder、to-tickets、垂直切片 | 合并为“地图 + 可验证切片” |
| Implementation | incremental slices + TDD + verification | implement at agreed seams + TDD | 复用共同的薄切片与局部高频验证 |
| TDD | 完整通用流程与测试层级 | 强调最高有效 seam 和外部行为 | Addy 提供流程，Matt 校准 seam |
| Debugging | reproduce/localize/reduce/fix/guard | 先建立 tight red-capable loop，再最小化和证伪 | 疑难问题优先 Matt 的严格反馈环 |
| Code review | 正确性、可读性、架构、安全、性能、验证 | Standards 与 Spec 两轴隔离 | 先分轴，再在每轴内使用 Addy 检查项 |
| Architecture | 生命周期中的架构质量与简化 | deep modules、domain model、architecture grilling | 复杂领域优先 Matt，常规守门用 Addy |
| Context | 明确的五层上下文结构 | context pointers、information hierarchy、pruning | 两者互补，均应纳入通用规则 |
| Security | 独立 hardening 工作流和清单 | 诊断/交接强调脱敏，另有 Git guardrail | 安全基线用 Addy，局部脱敏原则取 Matt |
| Delivery | Git、CI/CD、observability、shipping 完整 | 偏重 issue、tickets、implementation handoff | 生产交付主线用 Addy |
| Handoff | 分散在文档和上下文管理中 | 独立 handoff Skill，引用现有成果避免重复 | 长任务优先复用 Matt |
| Research | source-driven development | primary-source research 写入 Markdown | 合并为“官方源优先 + 结论落盘” |
| Cross-tool packaging | 非常全面，多种插件/规则适配 | 核心内容通用，但部分流程带特定假设 | 只借鉴包装，不让知识依赖包装 |
| Automation assumptions | slash commands、persona、可选自动模式 | subagents、issue tracker、slash commands | 适配层必须降级可用 |
| Maturity signaling | 主 Skill 集合统一呈现 | 显式 `in-progress/` 隔离 | 借鉴 Matt 的实验区隔离 |

## Overlap

两者共同认可：先澄清再实现、任务要小且可验证、测试证明外部行为、排错先复现、审查不能橡皮图章、上下文必须按需加载、长期决策必须写入文件。重叠部分应抽成一次性的通用工程原则，不在本知识库重复两份近义结论。

## Major Tensions

### Human gates

Addy 的 spec 工作流强调阶段审批；Matt 的部分 Skill 强调持续追问。高风险架构适合这些门，明确小任务则应压缩为一次假设说明和最终验证，避免流程成为目标。

### Stable documents

Addy 的 spec 模板可包含项目结构和命令；Matt 的 `to-spec` 刻意避免易过时的文件路径。推荐把稳定决策写进 spec，把当前路径写进可更新的项目地图或任务计划。

### Review output

Matt 保持 Standards/Spec 报告分离，避免互相遮蔽；Addy 更强调统一严重度和完整质量轴。推荐先独立取证，再统一 triage，不丢失原始轴。

### Tool dependence

两者都声称可服务 AI 工程，但具体流程可能需要 plugin、subagent、Issue Tracker 或共享引用文件。通用版本必须提供“只用文件搜索和 Markdown 也能执行”的降级路径。

## Universal Workflow Extracted

```text
Clarify need and domain language
  -> write stable success criteria and boundaries
  -> map dependencies and choose vertical slices
  -> load only relevant context and primary sources
  -> implement at the highest useful test seam
  -> establish evidence: red test / tight repro / runtime measurement
  -> review Standards and Spec independently
  -> triage correctness, architecture, security, performance
  -> update durable docs and produce a redacted handoff
  -> ship with rollback and observation
```

## Recommendation

- `Reuse`: 生命周期阶段、证据门、反馈环、测试 seam、审查分轴、上下文指针、脱敏交接。
- `Adapt`: 审批次数、文件路径、PR 大小、issue tracker、subagent 和插件调用。
- `Reference`: 具体工具安装、persona 包装和实验性 Skill。
- `Build`: 团队自己的风险策略、领域词汇、CI/发布集成和完成标准。

## 30-second Decision

要建立默认工程流程，先查 Addy；要解决模糊需求、领域语言、疑难 bug、分轴审查或跨会话交接，先查 Matt。不要全量安装后期待自动获得工程质量，真正有价值的是被项目采用并验证过的少数流程。

