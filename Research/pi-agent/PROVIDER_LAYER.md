# Model and Provider Layer

Use When:
- adding providers, model switching, authentication or capability normalization
- separating runtime logic from API-specific wire formats

[Repo-confirmed] `pi-ai` defines uniform `Model`, `Context`, `Message`, `Usage`, `StopReason`, tool schema and `AssistantMessageEventStream`. Known APIs include Anthropic Messages, OpenAI Completions/Responses/Codex, Azure Responses, Google/Vertex, Bedrock, Mistral and Pi Messages; provider ids are open strings, so extensions can add more.

[Repo-confirmed] A `Provider` owns auth metadata, model catalog, optional refresh/filtering and `stream`/`streamSimple`. `Models`/`ModelRuntime` resolves provider + model, stored or runtime credentials, base URL/headers, model overrides and then delegates streaming. The core loop sees only normalized messages/events.

## Capabilities and Differences

[Repo-confirmed] `Model` carries API id, provider, base URL, input modalities, reasoning support, context window, max output, costs and compatibility flags. Adapter-specific differences—developer/system roles, tool-result requirements, thinking encoding, strict schemas, prompt caching, session affinity and transport—are absorbed in API/provider adapters and model compatibility metadata.

[Repo-confirmed] `AgentSession` is still aware of selected model capability at policy points: it clamps thinking levels, reads context window/max tokens, checks auth and ignores overflow messages from a different selected model. It is provider-agnostic but not model-capability-blind.

## Auth and Configuration

[Repo-confirmed] `ModelRuntime` composes built-in provider definitions, `models.json` overrides and extension registrations. Auth can be API-key or OAuth; request-time resolution supports expiring tokens and header/base-url overrides. Global/project settings choose defaults, transport, thinking budgets and retry/timeouts.

[Repo-confirmed] Extensions can register/unregister providers and intercept provider headers, payloads and response metadata. Registrations made during extension load are queued until runtime binding; later changes take effect immediately.

## Usage

[Repo-confirmed] Assistant usage tracks input, output, cache read/write, total and cost. Session totals also include tool-reported usage and summarization usage, while context accounting uses the main assistant response and excludes nested tool usage.

[Inference] AI Novel Studio has a sound but much narrower seam: `BaseProvider.chat/stream_chat` and uniform `ChatMessage/ChatChunk/Usage`, implemented only for OpenAI-compatible APIs. Adopt Pi's explicit model-capability metadata and provider registry when a second genuinely different API family is required; do not pre-build dozens of adapters.

