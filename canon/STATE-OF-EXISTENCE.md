---
title: State of Existence — what is actually built
status: CANON — the Rule 6 ledger
scope: every named component of the stack, tagged by build state
sources: Gemini thread 2026-08-04/05 (repo audit + operator turns) · Horizons-UI CLAUDE.md · CI runs #352–354
---

# State of Existence

> **What this is.** The single ledger that answers *"does this exist?"* for every
> named component of the stack. Any document may describe a component; **only this
> one says whether it runs.**
>
> **Guiding principle.** This document exists because **every other document in
> the corpus describes the designed system as though it were the built system.**
> That is not two hundred independent errors — it is one systematic error repeated
> everywhere, and it is why agents cite features nobody wrote. Read this before
> citing any capability, from any document, including canon.
>
> **Verification rule.** A row may only be marked `built-verified` if it has been
> **observed working** — a green CI run, an on-device check, or a read of the
> shipping code. **An agent's report that it did something is not evidence.** When
> in doubt the row is `built-unverified`, never `built-verified`.

---

## Tags

| Tag | Means |
|---|---|
| `built-verified` | code exists **and** was observed working |
| `built-unverified` | code exists; **never confirmed on device** |
| `designed-only` | specified, discussed, or drawn — **zero code** |
| `absent` | named in a document but nothing behind it anywhere |
| `partial` | some of it exists; the rest does not |

---

## 1 · The audit

**Artifact:** repository review conducted in the Gemini thread, 2026-08-04, against
the Horizons-UI zip baseline; cross-checked against `Horizons-UI/CLAUDE.md` and CI
runs #352–354.

> **Source verdict:** *"most of those advanced system components are currently
> completely missing, stubbed, or detached from your actual Kotlin code. The repo
> in its current state is primarily a light shell holding UI layouts and basic
> Sherpa-ONNX glue."*

**Spec.**

### App shell / UI

| Component | State | Note |
|---|---|---|
| Compose UI frame, panel transitions | `built-verified` | the salvageable part; *"the visual wrapper, the clock-face multi-room interface, and the panel transitions are solid"* |
| `HomeGrid.kt` home screen | `built-verified` | **FROZEN** at `984b061` |
| Home forefront redesign | `designed-only` | `horizons-ui/HOME-REDESIGN-SPEC.md` §12 |
| Chat room (2:00) | `designed-only` | position + role assigned; no surface |
| Archives room (8:00) | `designed-only` | load-bearing for the recovery daemon |
| Horizons pane (10:00) + Easter-egg payload | `designed-only` | |
| Monitor pop-out tabs (CONSOLE/TERMINAL/BROWSER) | `built-unverified` | shipped, not device-checked |
| WebView browser, multi-window | `built-unverified` | `setSupportMultipleWindows` fixed |
| Floating Horizons Live Tile | `designed-only` | overlay, screen-vision, meta-prompt |
| Screensaver (chonk) | `partial` | `Screensaver.kt` partly wired |
| GOAT crash easter egg | `built-unverified` | `HomeGrid.kt` `showGoat` / `playGoatBleat` |

### Voice

| Component | State | Note |
|---|---|---|
| Kokoro TTS in-process (sherpa AAR) | `built-unverified` | |
| Moonshine STT in-process | `built-unverified` | CI #353; #354 fixed the int8 filename match |
| Silero VAD endpointing | `absent` | specified; no binding found |
| Whisper base STT | `absent` | **see conflict, §2** |
| STT via daemon on `127.0.0.1:8091` | ⛔ removed | nothing ever bound it; the in-process path replaced it |

### Runtime / execution

| Component | State | Note |
|---|---|---|
| `RouterPane.switchOn()` → `DaemonLauncher` | `built-unverified` | CI #352 |
| `RuntimeDef` shaped to the four canonical layers | `designed-only` | `aesop/PARAMETER-PACKET.md` §2 |
| `temperature` / `verbosity` / `cores` as real params | `absent` | hardcoded at `NpuClient:101`, `CloudLlmRuntime:122`; the verbosity slider reads nothing |
| Monitor `greenLight()` full check | `partial` | checks 2 of 4 (engine, assets); no arch/RAM, no handshake |
| `switchOn()` consulting the Monitor | `absent` | re-implements the check; **skips the gate entirely** when no `RuntimeDef` matches |
| Dual-NPU ping-pong orchestrator | `designed-only` | |
| Zero-TTL memory pinning | `designed-only` | |
| Recovery daemon | `designed-only` | restores from 8:00 Archives |
| Launch daemons | `partial` | `DaemonLauncher` exists; not driven from a packet |
| `CliffordService` cross-process config reload | `built-unverified` | `reloadIfChanged()` |
| Diagnostics bounded (`FileTail.kt`, log rotation) | `built-unverified` | the crash amplifier, fixed |

### Not built at all

| Component | State | Note |
|---|---|---|
| Cloud API connectors (Anthropic/OpenAI/OpenRouter) | `absent` | UI points at `localhost:8081`; **no compiled remote client** |
| 22-tool agentic engine | `absent` | no execution engine, no tool parser, no `AccessibilityService` |
| OS assistant (`VoiceInteractionService`) | `absent` | manifest permissions declared, **runtime logic never wired** |
| Game-mode / ADPF performance boost | `absent` | `android:appCategory="game"` not set |
| Termux inbound listener | `absent` | **the app has zero inbound listeners** |
| MediaProjection screen vision | `absent` | |

---

## 2 · Conflict — Whisper base vs. shipped Moonshine

> **Operator (2026-08-04):** *"We're not using Piper. We're using Coqui, Sherpa
> ONNX, Silero VAD, and Whisper base."*

**Artifact:** CI run #353 — *"Integrated in-process Moonshine STT directly through
the sherpa-onnx v1.13.2 AAR"*; run #354 fixed the Moonshine int8 bundle filenames.

**Spec.** The operator states the STT engine is **Whisper base**. The code that
shipped runs **Moonshine**. Both are recorded. **Neither is silently reconciled** —
per `TEMPLATE.md`, resolving this is an operator call, not an agent's.

Note the two are not equivalent in the way a swap implies: Whisper base quantised
is ~140–160 MB (encoder ~29 MB + decoder ~131 MB); Moonshine is materially smaller.
Silero VAD is specified in both readings and is **absent** in both.

## 3 · Conflict — the ~90s first crash

**Artifact:** `horizons-ui/CRASH-ANALYSIS-2026-07-31.md`.

Three amplifiers were found and fixed (synchronous disk-walking `FailureMonitor`
on the main thread; whole-file reads dressed as "tails"; uncapped, unrotated
`crash.log`). **The trigger of the *first* crash remains unproven.** Prime suspect
is Android LMK, which leaves **no stack trace**.

**Spec.** `designed-only` is the wrong tag here; the correct state is
**`unproven`**. The fix is verified in CI and **unverified on device.** Resolving
it needs one on-device read:
`/sdcard/Android/data/com.horizons/files/diag → tail -40 crash.log`. Stack trace
present ⇒ JVM exception. Empty but the app died ⇒ killed from outside, and no trace
will ever appear.

---

## 4 · Status ledger

- ✅ This ledger reflects the 2026-08-04 audit + CI #352–354 + `Horizons-UI/CLAUDE.md`.
- ⬜ **Nothing in the `built-unverified` column has been confirmed on device.** That
  is one operator session with the APK, and it would move a dozen rows at once.
- ⬜ First-crash trigger — `unproven`, needs the on-device `crash.log`.

## 5 · Open / to-confirm

- Whisper base vs. Moonshine — operator's call (§2).
- Whether Silero VAD gets wired, given it is `absent` under both readings.
- Every `built-unverified` row above is one device session away from resolution.
