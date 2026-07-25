# Novus Agenti / Omni Claw

**Repo:** [c10vis-poem/Novus-Agenti](https://github.com/c10vis-poem/Novus-Agenti)
**Package:** `com.horizons`
**Status:** Active development — session 19+

## What It Is

Fully on-device agentic AI assistant for the Motorola Razr Ultra 2025.
Inference runs on the NPU via a detached native daemon. No cloud LLM in
the main app runtime. No CPU fallback.

The **Horizons Workbench** — a manual, modular workbench, NOT a black box.
Core law: "Daemons stay dumb, the user is the loader." The app boots EMPTY
and stable; nothing runs until the user flips a fuse in the Router.

## Architecture

Seven tiles feed a center-hub Router:
- Runtime is DEFINED in Terminal
- LANDS in Settings
- VALIDATED by Monitor (greenLight)
- ENGAGED by the Router flip
- Supervised by CliffordService

## Key Components

| Component | File | Role |
|-----------|------|------|
| CliffordService | `horizons/fgs/CliffordService.kt` | Watchdog daemon |
| NpuClient | `horizons/core/llm/NpuClient.kt` | Model+vision daemon client |
| DaemonLauncher | `horizons/core/shell/DaemonLauncher.kt` | Daemon process management |
| AgentLoop | `horizons/core/agent/AgentLoop.kt` | Agent orchestration |
| ort_engine | `daemon/src/` | Legacy C++ daemon (CI-built) |

## Runtime Decision

**GenieX** on the QAIRT/HTP SDK backend — wired to a separate detached
daemon (`geniex serve`, OpenAI-compatible wire on `:18181/v1`).
`ort_engine` is the legacy runtime, still in the repo, not the path forward.

## Build

AGP 8.8.0 / Kotlin 2.1.0 / compileSdk 35 / minSdk 31 / JDK 17 / arm64-v8a only

## Related Skills

- [[termux-mobile-dev]] — on-device development environment
- [[project-memory]] — knowledge corpus retrieval
- [[horizons-wiki]] — architecture-of-record bundle

## See Also

- `CLAUDE.md` in the repo — full architecture-of-record
- `EXECUTIONS.md` — the running build dock
- `knowledge/omni-claw-defined/` — project definition canon
