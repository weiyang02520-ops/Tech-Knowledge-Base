# Overall Status

- Rating: `A` for engineering-method reference; `B` for wholesale installation
- Confidence: High
- Evaluated commit: `7676817c12a1317454ae3898a0c5c1eacf5dd3d5`
- Evaluation date: 2026-08-09

# Evidence

- 24 个 Skill 覆盖完整生命周期，并使用一致的触发、步骤、失败模式和验证结构。
- 核心内容是 Markdown，多工具目录主要承担安装适配。
- README 明确披露：单独安装某些 Skill 时，共享 `references/` 可能缺失。
- 仓库很新且更新活跃，具体 Skill 数量和文本仍可能快速变化。

# Component Status

| Component | Rating | Confidence | Reason | Revalidation Trigger |
| --- | --- | --- | --- | --- |
| Spec/Plan/Incremental 主线 | A | High | 边界和完成条件完整。 | 生命周期结构重构。 |
| TDD/Debug/Review | A | High | 证据优先且包含失败防护。 | 核心工作流重大变化。 |
| Context Engineering | A | High | 与跨工具知识库原则一致。 | 工具上下文机制变化。 |
| 安全/性能/可观察性 | B | Medium | 很好的检查入口，不替代领域专家和实际测量。 | 标准或工具链变化。 |
| 多工具适配 | B | Medium | 覆盖广，但各工具版本动态。 | 安装前每次复核。 |
| 全量自动触发 | B/C | Medium | 可能导致流程和上下文过载。 | 评估真实团队使用效果。 |

# Known Risks

- 机械串联过多 Skill 会把小任务流程化过度。
- 某些数字阈值和团队规范具有情境性。
- 单 Skill 安装可能缺共享引用。
- 插件、hook、命令的权限和供应链需独立审查。

# Needs Verification

- 目标 AI 工具当前支持的 Skill 格式和安装方式。
- 每个团队采用后的实际缺陷率、交付速度和上下文成本。
- 引用清单与最新标准、框架版本和组织政策的匹配程度。

