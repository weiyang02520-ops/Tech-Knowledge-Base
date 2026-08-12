# Architecture Overview

```text
Qt / AppKit / Android UI
          |
          v
   LibWebView Browser Layer
   - Profile / history / cookies
   - ProcessManager / SiteIsolationManager
   - ViewImplementation / WebContentClient
          |
          +-------------------- IPC --------------------+
          |                    |                        |
          v                    v                        v
     WebContent            Compositor              WebWorker
  LibWeb + LibJS       frames / backing stores    worker runtime
          |
          +-------------------- IPC --------------------+
          |                                             |
          v                                             v
   RequestServer                                  ImageDecoder
 network/cache/ws                               encoded -> bitmap
          |
          v
      Internet

Optional automation path: WebDriver -> WebContent
```

This map is synthesized from the current source tree. Exact process multiplicity and isolation policy are configuration- and platform-sensitive.

# Module Responsibilities

| Module | Responsibility | Connects To | Source Entry |
| --- | --- | --- | --- |
| UI ports | Native windows, tabs, omnibox, menus and events | LibWebView | `UI/Qt/main.cpp`, `UI/AppKit/main.mm`, `UI/Android/` |
| LibWebView | Browser-owned profile/data, views, process management and connections | UI and services | `Libraries/LibWebView/Application.cpp`, `ProcessManager.cpp`, `ViewImplementation.cpp` |
| WebContent | Page host, input, Web engine and JS execution | UI, compositor, request/image services | `Services/WebContent/main.cpp`, `PageHost.cpp`, `ConnectionFromClient.cpp` |
| Compositor | Frame/backing-store ownership, presentation, scrolling and vsync | UI and WebContent | `Services/Compositor/main.cpp`, `CompositorState.cpp` |
| RequestServer | HTTP(S), WebSocket, cache, DNS coordination and request pipes | WebContent and network | `Services/RequestServer/main.cpp`, `ConnectionFromClient.cpp` |
| ImageDecoder | Decode untrusted image bytes into bitmap results | WebContent | `Services/ImageDecoder/main.cpp`, `ConnectionFromClient.cpp` |
| WebWorker | Dedicated/shared worker execution hosting | WebContent/compositor | `Services/WebWorker/main.cpp`, `WorkerHost.cpp` |
| WebDriver | Automation sessions and WebContent control | external driver and WebContent | `Services/WebDriver/main.cpp`, `Session.cpp` |
| LibWeb | DOM, HTML, CSS, Fetch, layout, painting and Web APIs | LibJS, platform libraries | `Libraries/LibWeb/` |
| LibJS | ECMAScript runtime, bytecode/interpreter and heap | LibWeb bindings | `Libraries/LibJS/` |
| LibWasm | WebAssembly parser and abstract machine | LibWeb/LibJS integration | `Libraries/LibWasm/` |
| LibIPC/LibSandbox | Typed message transport and OS isolation primitives | all processes | `Libraries/LibIPC/`, `Libraries/LibSandbox/`, `Services/*/Sandbox*` |

# Navigation and Render Flow

```text
URL entered in UI
  -> LibWebView chooses/creates WebContent process
  -> WebContent asks RequestServer for resources
  -> response bytes enter HTML parser
  -> DOM is built; scripts may execute through LibJS
  -> CSS parser builds CSSOM
  -> style computer performs matching and cascade
  -> DOM + computed style produce layout tree
  -> formatting contexts calculate used geometry
  -> paint tree + stacking contexts are produced
  -> display data reaches Compositor/backing stores
  -> native UI presents the frame
```

# Image Flow

```text
Encoded image resource
  -> WebContent / image client
  -> isolated ImageDecoder over IPC
  -> decoded bitmap metadata and pixels
  -> layout/painting
  -> compositor frame
```

# Key Data Structures

- DOM tree: parsed document semantics.
- CSSOM and computed style: parsed rules and cascade result.
- Layout tree/state: box structure and used geometry; not 1:1 with DOM.
- Paint tree: visible, finalized painting and hit-testing objects.
- Stacking context tree: z-order and phase-driven painting.
- IPC endpoints: generated/typed contracts in `.ipc` definitions.
- Shared buffers/backing stores: cross-process frame and image transport.

# Research Entry Points

- Multi-process changes: start at `Libraries/LibWebView/ProcessManager.*` and `Services/` entry points; use `Documentation/ProcessArchitecture.md` only as supporting context.
- Page lifecycle: `Services/WebContent/PageHost.*`, then `Libraries/LibWeb/Page/` and `HTML/`.
- CSS: `Libraries/LibWeb/CSS/`, `Layout/`, `Painting/`, plus `Documentation/CSS*.md`.
- JavaScript: `Libraries/LibJS/` and WebIDL/bindings under LibWeb.
- Network: `Services/RequestServer/`, `LibRequests`, `LibHTTP`, `LibTLS`, `LibDNS`.
- Images: `Services/ImageDecoder/`, `LibImageDecoders`, `LibGfx`.
- Compositing/GPU: `Services/Compositor/` and `Libraries/LibWeb/Compositor/`.
- Standards behavior: locate matching tests under `Tests/LibWeb/` before reading implementation.

# Boundaries and Risks

- Official process documentation is partly aspirational and may lag code.
- `SandboxUnimplemented.cpp` files show that platform behavior is not uniform.
- Shared memory and IPC parsers are security boundaries, not ordinary helper APIs.
- Page, worker, network, image and compositor crashes need independent lifecycle handling.
- Web specs and tests are authoritative behavior sources; explanatory docs are navigation aids.

