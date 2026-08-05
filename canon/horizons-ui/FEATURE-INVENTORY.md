---
title: Horizons-UI — Complete Feature Inventory
status: CANON — the enumeration, from the operator's spec-by-spec session
source: Gemini thread 2026-08-04/05 (the later PDF — the full feature enumeration), with the operator's subsequent corrections applied
scope: every named feature, its owner, and its build state
---

# Feature Inventory

> **What this is.** Every feature, enumerated, with an owner and a state tag. The
> checklist form of the system. Composed from the spec-by-spec session where the
> operator went through the architecture feature by feature and corrected it.
>
> **Guiding principle.** This is **the full target list**, not a status report. Most
> of it is `designed-only`. A feature appearing here means it is *wanted*, not that
> it exists.
>
> **Verification rule.** Rows are tagged from
> [`../STATE-OF-EXISTENCE.md`](../STATE-OF-EXISTENCE.md), which is the single build-state
> authority. Where a row says `unverified`, it has **not** been checked against live
> code — do not upgrade it without running a check.

**Corrections applied.** The source enumeration was corrected by the operator
immediately after it was produced. Applied here, not preserved as-was:

- **Archives** and the **Horizons Pane** are rooms in their own right — the draft
  had given their slots to Cloud/API connectors and the browser.
- **The four parameters are Weights / Runtime / Engine / Communication** — the draft
  invented "4 OS-level permissions." Operator: *"you just made up some of that shit."*
- **Launch daemons + recovery daemon** and the **3–5 minute sleep timer with the
  chonk screensaver** were added by the operator afterward.
- Rooms are listed **by name**. Positions are not discussed — the home screen is done.

**Tags:** `built-verified` · `built-unverified` · `partial` · `designed-only` ·
`absent` · `rejected`

---

## 1 · MONITOR — scope gatekeeper, telemetry, browser

| # | Feature | State |
|---|---|---|
| 1.1 | Intercepts every runtime profile and model-init request **before** execution | `partial` |
| 1.2 | `greenLight` — **binary presence** | `built-unverified` |
| 1.3 | `greenLight` — **exec bit set** (`chmod +x`) | `absent` |
| 1.4 | `greenLight` — **asset availability** (`.so`, QAI Hub bundles) | `built-unverified` |
| 1.5 | `greenLight` — **model explicitly plugged in** | `built-unverified` |
| 1.6 | Validates quantization limits, NPU node allocation, thermal constraints, RAM ceiling | `absent` |
| 1.7 | **All Green / N Red** readout that *names* the failed asset | `built-unverified` |
| 1.8 | Continuous health monitor — trips the Router fallback on OOM or thermal throttle | `designed-only` |
| 1.9 | **Main browser** — full Chromium chrome + sidebar | `built-unverified` |
| 1.10 | Multi-window support (links open tabs; unbreaks OAuth popups) | `built-unverified` |
| 1.11 | Pop-out tabs — CONSOLE · TERMINAL · BROWSER | `built-unverified` |
| 1.12 | Oscilloscope signal view | `built-unverified` |
| 1.13 | **Arcade cabinet GUI** — marquee, CRT behind glass, placard, control deck, coin door | `designed-only` (LOCKED spec) |
| 1.14 | Renders the Horizons easter-egg game | `designed-only` |

## 2 · CHAT — agentic interaction

| # | Feature | State |
|---|---|---|
| 2.1 | Multi-modal chat view | `built-unverified` |
| 2.2 | Rich artifact generation | `designed-only` |
| 2.3 | File attachments + image loading | `designed-only` |
| 2.4 | Direct prompt push to the Router | `designed-only` |
| 2.5 | **Embedded web view** — render pages/tools/artifacts inside the conversation | `designed-only` |
| 2.6 | **The OS tool suite** — 26 tools incl. `done` (§9) | `built-unverified` |
| 2.7 | `AccessibilityService` — tap, type, navigate third-party apps | `built-unverified` |
| 2.8 | Rain-splashed slate background · uploadable wallpaper | `built-unverified` |

## 3 · SETTINGS — the Armory / vault

| # | Feature | State |
|---|---|---|
| 3.1 | Secret vault folder on device storage — weights, token manifests, config keys | `partial` |
| 3.2 | **OS intent catchers** — `ACTION_VIEW` / `ACTION_SEND`, "Open With → Horizons" | `built-unverified` |
| 3.3 | **SAF picker** — browse internal, SD, external; select and register | `built-unverified` |
| 3.4 | Files land **INERT** — registered, not loaded, cannot cause memory pressure | `designed-only` |
| 3.5 | Key vault — API keys, QAI Hub tokens, bearer tokens | `built-unverified` |
| 3.6 | **Bake & Export** — raw asset + credentials → ready artifact → Router | `designed-only` |
| 3.7 | Verbosity / debug-log sliders **that something actually reads** | `absent` |
| 3.8 | Brushed-steel vault door background · uploadable wallpaper | `built-unverified` |

## 4 · TERMINAL — the Mod Garage

| # | Feature | State |
|---|---|---|
| 4.1 | Termux bridge + native sub-shells | `built-unverified` |
| 4.2 | Tmux session management | `designed-only` |
| 4.3 | **Forges the parameter packet** — parameters only, never executes | `partial` |
| 4.4 | `RuntimeDef` form — **Name · Binary · Port · Health Endpoint · Args Template** | `built-unverified` |
| 4.5 | Manages background C++ daemons (`llama-server`), IPC sockets, CLI utilities | `partial` |
| 4.6 | Executes local scripts to pull weights | `designed-only` |
| 4.7 | Passes manifests to the Router's watch directory | `designed-only` |
| 4.8 | Shell history long-press → **Copy** | `built-unverified` |
| 4.9 | Shell history long-press → **Export to Router** as a temporary runtime | `built-unverified` |
| 4.10 | Shell history long-press → **Save to Commands** (`SavedCommandStore`) | `built-unverified` |
| 4.11 | Shell history long-press → **Archive** as a real `.sh` in the ArtifactStore | `built-unverified` |
| 4.12 | On-device CLI assistant for syntax | `designed-only` |
| 4.13 | **Matrix cascade** background (`fakesteak`) | `built-unverified` (LOCKED spec) |
| 4.14 | Quick-access prompt shortcuts | `designed-only` |

## 5 · ARCHIVES — the artifact vault

| # | Feature | State |
|---|---|---|
| 5.1 | Real file manager over a directory tree (`filesDir/archive`) | `built-unverified` |
| 5.2 | Breadcrumb navigation | `built-unverified` |
| 5.3 | Saves **verified runtime profiles** — restore without rebuilding | `designed-only` |
| 5.4 | Parameter-configuration history | `designed-only` |
| 5.5 | Session / prompt logs | `built-unverified` |
| 5.6 | `.sh` harness + environment storage, foldered | `built-unverified` |
| 5.7 | **The recovery daemon's restore source** | `designed-only` |
| 5.8 | Export an artifact back to the Terminal for modification | `designed-only` |
| 5.9 | Film-strip background · uploadable wallpaper | `built-unverified` |

## 6 · HORIZONS — about, credits, easter egg

| # | Feature | State |
|---|---|---|
| 6.1 | Build version display | `built-unverified` |
| 6.2 | Model credits | `designed-only` |
| 6.3 | Open-source attribution | `designed-only` |
| 6.4 | Model-release info | `designed-only` |
| 6.5 | System updates | `absent` |
| 6.6 | **Hidden unlockable game payload** — pushes to the Router, renders on the Monitor | `designed-only` |
| 6.7 | Butterfly-nebula background (gold + blue-white) · uploadable wallpaper | `built-unverified` |

## 7 · ROUTER — the fuse box

| # | Feature | State |
|---|---|---|
| 7.1 | `RouterConfig` — **Runtime · Backend · Model · Assets** | `built-unverified` |
| 7.2 | States: **Ready to Run · Running · Sleeping** (+ Archive) | `built-unverified` |
| 7.3 | **Sleep** — unload from memory, keep the config on the deck | `designed-only` |
| 7.4 | **Just-in-time re-check at flip** — consult the Monitor, don't re-implement it | `absent` |
| 7.5 | **Fails naturally** — no brick wall, no lockout, no blocking banner | `rejected` (as a blocker) / `designed-only` (as behaviour) |
| 7.6 | **Dual-NPU orchestrator** — ping-pong context switch, no teardown | `designed-only` |
| 7.7 | **NPU manager harness — in-APK**, holds the switch, catches OOM | `designed-only` |
| 7.8 | Multi-tier fallback cascade: NPU → local CPU/Tmux daemon → cloud | `designed-only` |
| 7.9 | **DSP voice panel** — pitch, speech speed, volume scale, voice-model swap | `designed-only` |
| 7.10 | Launches daemons via `DaemonLauncher` from the active `RuntimeDef` | `built-unverified` |
| 7.11 | **Aiwa CD player GUI, animated** — plasma tubes, nodes, platform perimeter, violet crystal, white sun glow | `designed-only` (LOCKED spec) |
| 7.12 | Circuit-board / chip-node background | `built-unverified` |

## 8 · VOICE

| # | Feature | State |
|---|---|---|
| 8.1 | **Silero VAD** — continuous endpointing, 500–800 ms trailing silence | `absent` (forked, not wired) |
| 8.2 | STT in-process on the sherpa AAR | `built-unverified` |
| 8.3 | **Whisper base vs Moonshine** — undecided, measure on CPU/GPU | `open` |
| 8.4 | **Kokoro TTS** in-process, streaming PCM → `AudioTrack` | `built-unverified` |
| 8.5 | **Barge-in** — cancel TTS queue, clear buffer, reopen VAD | `designed-only` |
| 8.6 | Hard max audio length (~60 s) so noise can't hang the stream | `absent` |
| 8.7 | Floating mic tile initiates capture | `designed-only` |
| 8.8 | Voice models load from the **external device folder**, by path | `designed-only` |

## 9 · THE OS TOOL SUITE

Live in `AgentSystemPrompt.kt`, dispatched by `AgentLoop`. **26 including `done`.**

| Group | Tools |
|---|---|
| Apps | `launch_app` · `list_apps` |
| Alarms | `set_alarm` · `set_timer` |
| Calendar | `read_calendar` · `create_event` |
| Contacts | `search_contacts` |
| Device | `wifi` · `bluetooth` · `volume` · `brightness` · `dnd` · `flashlight` |
| Media | `media` |
| Notifications | `read_notifications` · `post_notification` |
| Clipboard | `read_clipboard` · `write_clipboard` |
| Shell | `shell` |
| Cloud | `http_fetch` · `web_search` |
| System | `battery` · `network` · `storage` |
| Tasker | `tasker_task` |
| Control | `done` |

Protocol: `<tool>{"name":…,"args":{…}}</tool>` → wait for `<result>` → next call.
**`http_fetch` is the cloud connector** — SambaNova, OpenRouter, HuggingFace.
State: `built-unverified`.

## 10 · FLOATING HORIZONS LIVE TILE

| # | Feature | State |
|---|---|---|
| 10.1 | Always-on overlay, works across the OS, independent of room state | `designed-only` |
| 10.2 | **Live screen vision** — `MediaProjection` feeding a vision model | `absent` |
| 10.3 | Floating mic trigger | `designed-only` |
| 10.4 | **Live meta-prompt engine** — voice → structured prompt → model → TTS → on-screen actions | `designed-only` |
| 10.5 | Voice-triggered tmux commands while in Live Mode | `designed-only` |

## 11 · DAEMONS & LIFECYCLE

| # | Feature | State |
|---|---|---|
| 11.1 | **Launch daemons** — init C++ env, IPC sockets, load models | `partial` |
| 11.2 | **Recovery daemon** — trap OOM/crash, flush buffer, restore from Archives | `designed-only` |
| 11.3 | **Serve-first / "alive ≠ ready"** — bind port, load on background thread, 503 until ready, **never suicide on a missing model** | `unverified — suspected regressed` |
| 11.4 | `CliffordService` watchdog — FGS `specialUse`, `START_STICKY`, backoff, 5-strike | `built-unverified` |
| 11.5 | Cross-process config reload (`reloadIfChanged`) | `built-unverified` |
| 11.6 | Separate engine processes, UNIX socket protocol, zero-copy shared memory | `unverified` |
| 11.7 | **Zero-TTL pinning** — superseded: models live in an external device folder, loaded by path | `superseded` |
| 11.8 | **Boots empty and stable** — nothing heavy until the operator flips a fuse | `built-unverified` |

## 12 · OS INTEGRATION

| # | Feature | State |
|---|---|---|
| 12.1 | `VoiceInteractionService` — replace the system assistant | `built-unverified` |
| 12.2 | `RecognitionService` | `built-unverified` |
| 12.3 | `AccessibilityService` | `built-unverified` |
| 12.4 | Notification listener | `built-unverified` |
| 12.5 | TTS service (`TTS_SERVICE`) | `built-unverified` |
| 12.6 | Quick-settings tile | `built-unverified` |
| 12.7 | **Game mode / ADPF** — `appCategory="game"` + `PerformanceHintManager` | `built-unverified` |
| 12.8 | Runtime permission requests actually wired | `unverified` |
| 12.9 | **Inbound listener** — gives Termux mic / voice / WebView-OAuth | `absent` |

## 13 · GUARDIANS & FAILURE FACES

| # | Feature | State |
|---|---|---|
| 13.1 | **GOAT** — `// GOAT_SAYS_NO`, synthesized sawtooth bleat w/ vibrato + tremolo, on handshake failure | `built-unverified` |
| 13.2 | 7 banner taps → `// GOAT_UNLOCKED` | `built-unverified` |
| 13.3 | **ASCII 404 CAT** — browser-scoped connection failure / dropped websocket | `designed-only` |
| 13.4 | **CHONK** — 3–5 min idle screensaver from `/storage/emulated/0/Download/` | `partial` |
| 13.5 | Failure surfaces as a **banner, not a crash** | `built-unverified` |

## 14 · CROSS-CUTTING

| # | Feature | State |
|---|---|---|
| 14.1 | **The APK's whole job**: screen timeout · permissions · browser · WebSockets | `designed-only` |
| 14.2 | Models in an **external device folder**, drag-and-drop swap, no rebuild | `designed-only` |
| 14.3 | APK ships native libs only (~20 MB) | `designed-only` |
| 14.4 | The four parameter layers first-class in `RuntimeDef` | `absent` |
| 14.5 | `temperature` / `verbosity` / `cores` as real Runtime params | `absent` |
| 14.6 | WebSocket loopback bridges (`ws://localhost:…`) | `absent` |
| 14.7 | Download-to-vault — browser writes straight into the vault | `designed-only` |
| 14.8 | Sideloaded — no 200 MB Play ceiling | `built-verified` |

---

## Status ledger

- ✅ Enumeration — from the operator's feature-by-feature session, corrections applied.
- ⬜ **Every `built-unverified` row is one device session from resolution.**
- ⬜ 11.3 (serve-first) is the highest-value single check — cheap, and it may be the crash.
- ⛔ 7.5-as-blocker and 11.7 (zero-TTL) — superseded or rejected; listed so nobody rebuilds them.

## Open

- Whether the tool count is 26 or the "22" of earlier documents — the prompt lists 26
  including `done`. Cosmetic, but the docs should agree.
- Every `unverified` row in §11–§12 came from a stale snapshot, not live code.
