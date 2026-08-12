# How To Use This Knowledge Base

## Universal Workflow

1. 用 `ROUTER.md` 判断当前任务是否值得查库；简单局部任务直接跳过。
2. 把需求概括成能力，运行 `python tools/kb.py search "<capability>"`。
3. 按输出建议运行 `show` 或 `reuse`，不要打开整个项目文档。
4. 只有需要模块边界时运行 `architecture`。
5. 只有公开分析不足时才用 `path` 定位本地 `source/`，并核对 `status` 中的提交与新鲜度。

所有命令都可从知识库根目录执行：

```powershell
python tools/kb.py search "background agent scheduler"
python tools/kb.py show prime-agent
python tools/kb.py reuse prime-agent "subagent"
python tools/kb.py architecture prime-agent "session persistence"
python tools/kb.py path prime-agent
python tools/kb.py status prime-agent
```

## Codex

本机已在 `%USERPROFILE%\.codex\AGENTS.md` 最小追加 Router。非简单技术任务会先调用 `kb.py search`；简单任务不查库。适配说明见 `Adapters/Codex/`。

## Claude Code

本机已在 `%USERPROFILE%\.claude\CLAUDE.md` 最小追加 Router，未导入知识正文或启动时预读。适配说明见 `Adapters/Claude-Code/`。

## Trae

本机版本未确认稳定的文件级 Rules 格式，因此未修改配置。按 `Adapters/Trae/SETUP.md` 在 UI 中做一次设置后即可自动判断。

## WorkBuddy

本机版本未确认稳定的文件级持久规则格式，因此未修改 Memory、Identity 或 Settings。一次性操作见 `Adapters/WorkBuddy/SETUP.md`。

## Cursor 和其他工具

任何能读取本地文件并进行文本搜索的 Agent 或 IDE 都可使用。专有规则文件只能作为入口，不能成为知识的唯一载体。

## Example: Long-running Agent

```text
Need: long-running background AI agent
  -> search TAGS for long-running-agent / heartbeat / scheduler
  -> open AI-Agent/prime-agent/SUMMARY.md
  -> open REUSE_GUIDE.md
  -> classify each capability as Reuse / Adapt / Reference / Build
  -> implement only the remaining product-specific work
```

## Example: Network Proxy

```text
Need: manage system proxy configuration
  -> search TAGS for system-proxy / windows / linux
  -> open Network/fanqiang/SUMMARY.md and STATUS.md
  -> use only currently verified concepts and official upstream links
  -> revalidate dynamic security and compatibility facts online
  -> never execute binaries or scripts merely because they are archived in source/
```
