---
project_name: "Ladybird"
upstream_repository: "LadybirdBrowser/ladybird"
github_url: "https://github.com/LadybirdBrowser/ladybird"
author_or_organization: "Ladybird Browser Initiative and contributors"
default_branch: "master"
analyzed_commit: "8d225a329ee852510b4522e04d357c6fdd51d7f7"
analysis_date: "2026-08-09"
license: "BSD-2-Clause"
main_languages: ["C++", "HTML", "JavaScript", "Rust", "Python", "CMake"]
main_technologies: ["LibWeb", "LibJS", "LibWasm", "IPC", "multi-process browser", "sandbox", "Qt", "AppKit", "Android", "CMake", "Web Platform Tests"]
project_status: "Active pre-alpha; developer use only"
tags: ["browser", "web-engine", "renderer", "javascript-engine", "wasm", "multi-process", "ipc", "network-stack", "image-decoder", "compositor", "sandbox", "web-standards"]
possible_reuse_areas: ["browser process model", "loading-to-painting pipeline", "IPC boundaries", "untrusted-content isolation", "web standards implementation map"]
---

# Metadata

## Documentation Location

- Overview: `source/README.md`
- Documentation index: `source/Documentation/README.md`
- Process model: `source/Documentation/ProcessArchitecture.md`
- Loading to painting: `source/Documentation/LibWebFromLoadingToPainting.md`
- Browsing contexts: `source/Documentation/BrowsingContextsAndNavigables.md`
- Testing: `source/Documentation/Testing.md`
- Security state: `source/SECURITY.md`

## Important Directories

| Directory | Responsibility |
| --- | --- |
| `UI/` | Qt, AppKit and Android browser UI ports. |
| `Libraries/LibWebView/` | Browser-process model, profiles, process management and UI-to-WebContent bridge. |
| `Services/` | Compositor, WebContent, WebWorker, RequestServer, ImageDecoder and WebDriver processes. |
| `Libraries/LibWeb/` | HTML, DOM, CSS, layout, painting, fetch and Web API engine. |
| `Libraries/LibJS/` | JavaScript parser/runtime, bytecode/interpreter and heap. |
| `Libraries/LibWasm/` | WebAssembly parser and abstract machine. |
| `Libraries/LibIPC/`, `Libraries/LibSandbox/` | Inter-process transport and sandbox support. |
| `AK/`, `Base/` | Foundation types and platform support. |
| `Tests/` | Web platform, LibJS and library tests; most repository files are test inputs. |

## Repository Size at Analysis

- Tracked files: 26,471
- Test files: 20,293 tracked files under `Tests/`
- Local shallow-clone size: approximately 195 MB including Git metadata
- Worktree state after clone: clean

## Analysis Scope

Read the overview, documentation index, process architecture, loading/painting pipeline and security policy; inspected current UI, service, WebView, LibWeb, LibJS, LibWasm, IPC, sandbox and test directory maps plus representative process entry points. No build, browser, test, script, binary, fuzzer or dependency was executed.

## Verification Notes

**Fact:** The README labels Ladybird pre-alpha and developer-only. `ProcessArchitecture.md` explicitly says parts are aspirational. Current source contains services and process-management structures beyond that older narrative, including Compositor, WebWorker and `LibWebView::ProcessManager`.

**Recommendation:** Use this analysis as a module and research-entry map. Recheck current code before relying on exact process counts, site-isolation policy or sandbox guarantees.

