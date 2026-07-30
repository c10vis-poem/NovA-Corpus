# Novus Agenti {Omni Claw} — Master Vision Blueprint

Source: "Copy of Welcome to the birth of Novus Agenti - {Omni Claw}." (Gemini session export, Drive `1j0lQM69h4eENLX2LKWtRilyQZL1aScyA`). Category: **master architecture reference** — this is the target system; AESOP is its current Termux-scoped implementation.

**Note on source reliability**: this is a Gemini brainstorming/design session, not verified working code — treat every mechanism below as design intent.

## 1. Project Overview

Novus Agenti ("Omni Claw") is a localized, hyper-customized mobile operating environment that treats individual apps, terminal endpoints, and cloud runtimes as modular subroutines. By separating heavy math (model inference) from the UI layer, the phone doesn't act as a simple app container — it acts as an iron-clad local orchestrator for a multi-agent neural mesh.

Core stack: a **Kotlin UI app** (lightweight frontend orchestrator) paired with a **detached native C++ background daemon** (`ort_server`) that runs a **6.2GB Gemma-4 12B QAT model** on the phone's **Hexagon NPU**. The two communicate over a **local loopback WebSocket/HTTP connection at `127.0.0.1:8080`**.

Qualcomm QNN SDK static graph partitioning splits the workload across the SoC: ~5.5GB to the Hexagon NPU, ~0.6GB to the Adreno GPU for custom layers, ~0.1GB to the CPU for housekeeping.

## 2. Core Architecture — The Watchdog Recovery Bridge

```
[Android Low Memory Killer (lmkd)] - Ignores Core Daemon
   |
   [Watchdog App] ---> [Local Loopback TCP: 127.0.0.1:8080] <--- [C++ Engine Daemon]
   | (Unkillable -950)
   +---> Monitors App State & Shared Memory Arena
```

- **The Sandbox Blindspot**: the 6.2GB model runs fully containerized inside the C++ daemon context, communicating purely via JSON over loopback.
- **The Skeleton Crew Failback**: the Watchdog is a featherweight foreground service (~15MB) monitoring the process lifecycle of `NpuClient.kt`.
- **Invisible Hot-Reboot**: the C++ engine is anchored to the root init tree at a privileged **`-950 oom_score_adj`** score.
- **State Preservation via WebSockets**: continually pushes JSON state frames to a micro-database in local storage.

## 3. Agentic Capabilities Map

| Capability | Trigger / Entry Point | Mechanism | Output / Effect |
|---|---|---|---|
| Global voice dictation | Standard Floating Microphone Tile | Raw speech → local cleanup pass → Android Accessibility Service | Types pristine text into active cursor field |
| Meta-prompt compilation (verified) | Internal mic icon inside AI Chat Floating Box | Speech → Silero VAD → local HTTP/loopback stream to C++ engine → pulls Obsidian/Markor skill blocks → compiles structured meta-prompt | Streams back into AI Chat Box as editable text — human reviews before send |
| Local file operations | Model emits tool-call JSON | Android IPC Intents → Tasker Relay | Read/write Markdown in Markor/Obsidian vaults |
| System actions | Model emits tool-call JSON | Android Accessibility Service | Launch camera, downloads, pull git repos |
| Local shell execution | Agent needs bash/git/compile | Termux GLIBC-patched environment, authenticated JSON-RPC on port `8022` | Bash shortcuts, Python transformers, patchelf-glibc |
| Cloud compute offload | Task needs heavy compute/web | Google Colab CLI | — |

(Content truncated at source retrieval point — this is a partial capture from a fast raw-copy pass; the full doc continues beyond what was fetched inline. Re-fetch fileId `1Uo71GU9n13ydxPmRDDoDUa5W_9nKFL6V` for the complete text.)
