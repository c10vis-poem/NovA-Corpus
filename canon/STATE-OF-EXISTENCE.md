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
| Kokoro TTS in-process (sherpa AAR) | `built-unverified` | see §3a — a native `exit(-1)` in init was found and patched 2026-08-06 late; the engine's boot path was never clean |
| Moonshine STT in-process | `built-unverified` | CI #353; #354 fixed the int8 filename match |
| Silero VAD endpointing | `absent` | specified; no binding found |
| Whisper base STT | `absent` | **see conflict, §2** |
| STT via daemon on `127.0.0.1:8091` | ⛔ removed | nothing ever bound it; the in-process path replaced it |

### Runtime / execution

| Component | State | Note |
|---|---|---|
| `RouterPane.switchOn()` → `DaemonLauncher` | `built-unverified` | CI #352; **superseded 2026-08-06** — `switchOn()` removed entirely, `loadConfig()` replaces it (Router-as-load-bay, operator-adopted spec, merged to main) |
| `RuntimeDef` shaped to the four canonical layers | `designed-only` | `aesop/PARAMETER-PACKET.md` §2 |
| `temperature` / `verbosity` / `cores` as real params | `absent` | hardcoded at `NpuClient:101`, `CloudLlmRuntime:122`; the verbosity slider reads nothing |
| Monitor `greenLight()` full check | `partial` | checks 2 of 4 (engine, assets); no arch/RAM, no handshake |
| `switchOn()` consulting the Monitor | `absent` | superseded — see above; `loadConfig()` doesn't gate at all by design (Router has no ignition) |
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

**Correction (2026-08-06):** the previous sentence's "Moonshine is materially
smaller" is **false**, measured. Whisper base.en int8 = 161 MB, Moonshine base
int8 = 287 MB — Moonshine base is 78% *larger*. Whisper tiny.en (104 MB) and
Moonshine tiny (124 MB) are the closer pair. This does not resolve §2's open
operator call, it only corrects the size comparison offered in support of it.

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

## 3a · New finding — Kokoro TTS native `exit(-1)` (2026-08-06 late)

**Artifact:** commit `a7869ec` on Horizons-UI branch
`claude/novus-device-file-loading-ij4k4r`, commit message: *"Fix boot crash:
Kokoro TTS init calls native exit(-1) without lang param."* Landed by a separate
session/push, not the one that wrote this entry — discovered via a CI-failure
webhook on a later commit in the same branch.

**Spec.** A native `exit(-1)` call inside Kokoro TTS init produces **exactly**
the symptom §3 attributes to Android LMK: the process dies with no Java stack
trace, because it never throws a catchable JVM exception — native code called
`exit()` directly. This is **code-confirmed, not speculative**: a named call
site was found and patched. It is at least as strong a candidate for the
"~90s first crash" as LMK, and unlike LMK it has a fix already written.

Separately, this session (same branch) fixed a **different** crash path:
`AppStateStore`'s `EncryptedSharedPreferences.create()` throwing on a Keystore
master-key mismatch (reinstall/update-over-install), propagating through
`Application.onCreate()` uncaught. Both fixes are code-confirmed. **Neither
has been device-verified as of this entry** — the operator's most recent
report ("crashed in one split second") was against a build that predates
*both* fixes (commit `34cfac2`, which has neither).

**State:** `partial` — two independent, code-confirmed crash causes now share
one unmerged branch. Do not assume either alone is "the" first-crash trigger,
and do not tag either `built-verified` until an operator confirms on-device
which build (if either) stops crashing. If the newest build still crashes,
get the actual crash log before writing more fixes — see
`/sdcard/Android/data/com.horizons/files/failures/` (CrashRecorder +
FailureMonitor already write there).

**Consequence for §3:** the "LMK, no stack trace, trigger unproven" framing
should be treated as one hypothesis among (now) three candidates — LMK, the
Kokoro native exit, and the Keystore mismatch — until device evidence narrows
it.

---

## 4 · Suspected root cause — SAF picker scope

**Artifact:** operator observation (2026-08-06). App fails with "app couldn't
find my backend" while the GenieX runtime bits (`hybrid_llama_qnn.pte`, QNN-QAIRT
folder, `geniex-bench-android-arm64`) and Qwen 3.5-9B-Q4_0.gguf are all sitting
in `/storage/emulated/0/LeGRAND_REPOSITORY/HARNESS/` and
`/storage/emulated/0/LeGRAND_REPOSITORY/MODELS/` — **non-hidden internal
storage**, visible to any file manager, no special permissions required.

**Spec.** The likely cause is that Horizons' file-loading path only reads from
its own scoped storage (`context.filesDir` / `/Android/data/com.horizons/files/…`)
rather than exposing a real Storage Access Framework picker
(`ACTION_OPEN_DOCUMENT` / `ACTION_OPEN_DOCUMENT_TREE`) that returns URIs the
app can then resolve. Since Android 11, raw `new File("/storage/emulated/0/…")`
reads fail even for non-hidden files unless the app holds
`MANAGE_EXTERNAL_STORAGE` or the user granted access through SAF.

**State:** `partial (suspected broken)` — the Settings SAF picker row
([[horizons-ui/FEATURE-INVENTORY]] §3.3 / §15D.1) is nominally `built-unverified`
but the operator's on-device failure suggests it either does not reach outside
scoped storage or does not surface URIs the loader can use.

**How to confirm:** grep Horizons-UI for `ACTION_OPEN_DOCUMENT`,
`ACTION_OPEN_DOCUMENT_TREE`, `ContentResolver.openInputStream` and their
callers. If the answer is "only reads from `filesDir`," this is confirmed.

This is the **highest-value single check** for the current failure — it
preempts the daemon-suicide theory (§AGENT-BRIEF §4), because a daemon that
never gets a valid path in the first place will look identical to one that
suicides on missing model.

## 4a · Mitigated via an alternate path, still not confirmed (2026-08-06 late)

**Artifact:** PR #35 (Horizons-UI, `claude/novus-device-file-loading-ij4k4r`),
commit `34cfac2` — new `core/storage/StorageScanner.kt` + a "Scan device
storage" section added to Settings → Import.

**Spec.** §4's grep was **still not run** before this shipped — worth naming
plainly, since §4 itself calls it "cheap, one answer" and it remains
outstanding. What shipped instead is a workaround, not a fix to the loader:
`StorageScanner` does not use SAF at all. It walks `LeGRAND_REPOSITORY/`,
`Download/`, `Documents/`, and the sdcard root (depth 1) directly via
`java.io.File`, relying on the `MANAGE_EXTERNAL_STORAGE` grant the manifest
already declares (the permission row already existed and shows granted in
Settings — see FEATURE-INVENTORY §15D.1). Each found file gets a one-tap
import that copies it into `filesDir`, where the existing loader already
works.

**State:** `built-unverified` — shipped, not confirmed on device (blocked by
the crash described in §3a). If §4's SAF-scope theory is correct, this
scanner sidesteps it rather than closing it: the underlying loader still
only reads `filesDir`, the scanner just makes it trivial to get files there.
The original grep target is unchanged and still worth running.

---

## 5 · 2026-08-06 additions

**Artifact:** operator briefing this session. Items enumerated in
[[horizons-ui/FEATURE-INVENTORY]] §15. Consolidated build-state below.

**All `designed-only` / `absent` unless noted** — nothing here has code yet.
Some retag existing rows:

| Component | Previous | Now |
|---|---|---|
| Router 7.5-as-blocker | `rejected` | unchanged; overflow-bounce added as `absent` |
| Router 7.9 DSP voice panel | `designed-only` (TTS-only) | expanded to include STT tuning, still `absent` |
| §4.3 Terminal "forges packet, never executes" | `partial` | superseded — Terminal now also **configures models, fine-tunes, Termux-executes, pushes to Router, hosts on-device agent**, all `absent` |
| §12.9 Inbound listener / Termux backend absent | `absent` | remains `absent`; concretely to be filled by Termux `RUN_COMMAND_SERVICE` |
| §14.4 four parameter layers first-class in `RuntimeDef` | `absent` | unchanged; adds `max_tokens`, hardware target, provider picker |

**New rows (all `designed-only` / `absent`):**

- Router: animated CD tray / carousel / tap-a-disc fine-tune popup
- Router: dual-cassette Browse/Load role split with multi-load and execution-mode swap
- Router: hardware-target selector, cloud/local toggle, max-tokens control, STT tuning
- Router: cross-tile pathways (all six tiles push to Router)
- Router: overflow-bounce (Router full → GOAT face + return to origin)
- Router: on/off hotkey per pushed session/hook/script
- Terminal: CRT-oscilloscope panel treatment on console
- Terminal: agent draft-run-fix pattern (LLM-Hub-style)
- Terminal: live chaptered user manual + help-agent
- Terminal: port-over to Router when Router idle
- Provider picker (Terminal + Monitor browser): local / OpenAI / Anthropic / OpenRouter / SambaNova / custom
- UX-wide: no typing outside Terminal/browser; long-press → help popup; zoom on Home/Monitor; inset cropping on every non-Home room
- External-agent detection notification (CLI + compatible agent → direct user to Terminal)
- Old duplicate launcher tile (`.uilocal.LocalHomeActivity`) — **remove**; other launcher wires up as real `VoiceInteractionService`

**Standing rule (documentation only):**

- **Your-fork-first** — see [[MASTER-BUILD-BLUEPRINT]] §14.5. Not a code
  state, a build-time and dependency-choice rule.

**Important caveat added 2026-08-06 late:** every row added in this §5 is a
**specification**, written the same session it was described by the operator.
**None of it has been built.** A follow-up session turned the crash-adjacent
items (insets, storage scanning, boot stability) into real code the same
night; the Router/Monitor/Terminal visual and interaction work described
here (CD tray, tap-a-disc popup, dual-cassette, oscilloscope panel, zoom)
did not get touched in code at all. This is exactly the failure mode §0
of this document exists to prevent — recording it here so the next session
doesn't need to rediscover it by grepping `RouterPane.kt` and finding none
of §15A present.

---

## 6 · Status ledger

- ✅ Section 1 ledger reflects the 2026-08-04 audit + CI #352–354 + `Horizons-UI/CLAUDE.md`.
- ✅ Section 4 SAF-picker-scope hypothesis added 2026-08-06.
- ✅ Section 5 captures 2026-08-06 operator briefing additions.
- ✅ Section 3a — Kokoro native `exit(-1)` crash cause found and patched, 2026-08-06 late.
- ✅ Section 4a — storage-scanner mitigation shipped (not a fix to the SAF gap), 2026-08-06 late.
- ⬜ **Nothing in the `built-unverified` column has been confirmed on device.** That
  is one operator session with the APK, and it would move a dozen rows at once.
- ⬜ First-crash trigger — now **three** candidates (LMK, Kokoro native exit,
  Keystore mismatch), still unconfirmed. Needs the on-device `crash.log` /
  `files/failures/` report on the newest build.
- ⬜ §4 / §4a SAF-picker grep — highest-value single check, **still not run**
  as of 2026-08-06 late despite two sessions calling it out as cheap.

## 7 · Open / to-confirm

- Whisper base vs. Moonshine — operator's call (§2). Both available on
  `Mer0vin8ian` HF per your-fork-first rule.
- Whether Silero VAD gets wired, given it is `absent` under both readings.
- Every `built-unverified` row above is one device session away from resolution.
- SAF-picker scope hypothesis (§4/§4a) — grep pass will confirm or refute;
  the scanner shipped in §4a does not substitute for running it.
- Which of the three first-crash candidates (§3a) actually fires on device,
  once the operator installs a build carrying both known fixes.
