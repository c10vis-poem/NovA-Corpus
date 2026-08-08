---
title: Parameter Packet — the fuse, and the four layers it defines
status: CANON — operator-stated; corrects a documented prior misbuild
scope: the config object the Terminal forges, the Router plates, the Monitor checks
sources: Gemini thread 2026-08-04/05 (operator turns) · operator architecture notes (Aug 2)
---

# Parameter Packet — the fuse

> **What this is.** The canonical definition of the **parameter packet** (the
> "fuse"): what it is, what it contains, and who is allowed to do what with it.
>
> **Guiding principle.** The packet is **a plain editable text file.** It is not
> a schema to validate against, not a gate, and not a class. This document exists
> primarily to *stop* the packet being rebuilt as enforcement code — which has
> already happened once and broke the workbench.
>
> **Verification rule.** Any code claiming to implement this is checked against
> one question: **can the operator drop in a custom binary or fine-tuned weight
> the code has never seen, and still close the circuit?** If no, the
> implementation is wrong regardless of what it validates correctly.

---

## 1 · What the packet is — and what was built instead

**Artifact:** the prior build's `AssetCheck` list and its red `⚡ FUSE BOX` banner
(`RouterPane` / `ConfigStatus`), described in the operator's Aug-2 notes.

> **Operator:** *"the 'fuse box' and '10-amp fuse' were never meant to be compiled
> into restrictive UI gates, red warnings, or pre-execution blockers."*

What was actually built: the **"10-amp fuse"** metaphor became a rigid, hardcoded
**four-item `AssetCheck` list**, and the **Router** became an automated gatekeeper
that threw error banners and blocked any configuration not matching its
pre-programmed definitions. That defensive gatekeeping **broke the ability to
build custom runtimes, fine-tune models, or run build-in-place assets**, because
the system red-flagged anything non-standard.

**Spec.** The parameter packet is a **lightweight, editable text configuration
file**. It can be copied, moved, replaced, or pulled out of the **8:00 Archives**
wholesale. It defines four things (§2) and nothing else.

The circuit reads:

- **6:00 Terminal — the forge.** Writes the packet. Parameters only. **Never executes.**
- **4:00 Settings — the supply.** Holds assets and keys; can hand a packet to the
  Router. **No authority to run it.**
- **12:00 Monitor — the switch in the loop.** Verifies wiring, live, at flip time.
  Stores nothing; **dispatches**. Open or loose ⇒ no circuit, however perfect the packet.
- **Centre Router — the fuse box and breaker.** Carries current. **Doesn't argue.**
- **8:00 Archives — the shelf.** Verified profiles, restorable without rebuilding.

> **Operator:** *"The Router's job is simply to close the circuit on command — if
> the assets satisfy the physical requirements ('amperage'), the daemon runs; if
> not, it fails without locking down the workbench."*

**This is Rule 7 in its original instance.** The Router does not say *no*. It
attempts to close the circuit. Failure is a **natural failure to energise**, not
an application-thrown brick wall.

---

## 2 · The four layers

**Artifact:** operator's correction of a draft that had invented "4 OS-level
permissions" instead.

> **Operator:** *"No, you just made up some of that shit. So, that 4 OS level
> permissions in Boost Layer. I don't know what that's all about."*

**Spec.** The four parameters are **configuration layers exposed for modding and
fine-tuning through the 6:00 Terminal** — not permissions, not OS capabilities:

| # | Layer | Carries |
|---|---|---|
| 1 | **Weights** | model paths (absolute, off the device folder), INT8/ONNX quantization limits, tensor file allocations |
| 2 | **Runtime** | zero-TTL execution flags, RAM allocations, thread bindings, **temperature, verbosity, cores, max tokens, hardware target** (`npu` / `hybrid` / `gpu` / `cpu` — matches GenieX `--device` aliases; if the loaded runtime advertises multiple, all are offered) |
| 3 | **Engine** | native JNI/C++ layers (`libsherpa-onnx-jni.so`, `libllama.so`), VAD sensitivity, **STT tuning** (silence threshold ms, hard-max audio length), **TTS DSP** (pitch / speed / volume / voice-model swap) |
| 4 | **Communication** | IPC sockets, WebSocket bridges, **API router endpoints and provider selection** (local / OpenAI / Anthropic / OpenRouter / SambaNova / custom — extensible list, not the older three-hardcoded shortlist) |

> **Operator:** *"If any native logic needs tweaking, code refactoring, or custom
> patch application, it is queried, modded, and pushed to the Router directly
> through terminal access."*

### This closes a known Horizons-UI gap

`Horizons-UI/CLAUDE.md` flags: *"temperature is hardcoded (`NpuClient:101`,
`CloudLlmRuntime:122`). Verbosity HAS a Settings slider that NOTHING READS. Cores
don't exist. These must become real `RuntimeDef` params BEFORE P1.3."*

**Spec.** They are not four new ad-hoc fields to invent. **`temperature`,
`verbosity`, `cores`, `max_tokens`, and hardware target all belong under layer
2 — Runtime.** Provider selection (OpenAI / Anthropic / OpenRouter / ...) belongs
under layer 4 — Communication. `RuntimeDef` should be shaped to the four
canonical layers, so the launcher is written once against a stable taxonomy
rather than reopened each time a parameter is discovered missing.

### Router fine-tune popup — UI over the packet, not a rename of it

The Router's tap-a-disc fine-tune popup (see
[[../horizons-ui/ROUTER-STEREO-STACK-SPEC]] §Fine-tune popup) uses the
Aiwa-face labels `Model_ / Engine_ / Runtime_ / Config._`. Those are the
**engaged-item shortcut face** of the four canonical layers here, not a
replacement taxonomy:

| Popup row | Canon layer |
|---|---|
| `Model_` | the engaged Weights entry (which weight file is active) |
| `Engine_` | Engine (native engine driver: `llama_cpp`, `qairt`, cloud connector, terminal agent) |
| `Runtime_` | Runtime (which loaded runtime file executes it) |
| `Config._` | an archived parameter packet — folds Communication endpoints + any Weights limits into one restorable snapshot |

The popup is a **UI over** the packet. The packet on disk keeps the
canonical four-layer shape.

---

## 3 · Daemons

> **Operator:** *"It operates with launch demons and recovery demon, and it also
> has a slight time to [timeout]."*

**Spec.**

- **Launch daemons** — managed from the 6:00 Terminal. Initialise local C++
  execution environments, set up IPC sockets, load zero-TTL models into memory.
- **Recovery daemon** — a dedicated watcher. When an active NPU tensor op or
  native JNI thread hits OOM or crashes, it traps the exception, flushes the
  corrupted execution buffer, and **restores the runtime from the latest verified
  snapshot in the 8:00 Archives.**
- **Sleep** — **2 min** inactivity pauses active processing into a low-power state;
  the chonk screensaver covers it; tap or floating-mic wakes it. (Operator
  2026-08-06 — supersedes older "3–5 min".)

The recovery daemon is **why Archives is a room and not a folder** — it is the
restore source, so it is load-bearing in the execution path.

---

## 4 · Zero-TTL

> **Operator (context):** *"I'm already going to have two freaking models bouncing
> back and forth on the NPU. I'm not going to add the speech [layer to it]."*

**Spec.** Models are **pinned** — no time-to-live, no auto-eviction. Weights stay
resident (or `mmap`-ed from storage), so voice input and output stay hot and there
is no cold start. The dual-NPU orchestrator ping-pongs context between the two
on-device models **without teardown**. The operator's constraint stands: the NPU
carries the two text/tensor models, and the voice layer is **not** to be added on
top of that budget.

---

## 5 · Status ledger

- ✅ Packet-as-editable-file — operator-stated, and the prior misbuild documented.
- ✅ Four layers (Weights / Runtime / Engine / Communication) — operator-dictated.
- ✅ Launch + recovery daemons, Archives-as-restore-source — operator-stated.
- ✅ Zero-TTL pinning + NPU budget constraint — operator-stated.
- ✅ Runtime layer expanded with `max_tokens` + hardware target (operator 2026-08-06).
- ✅ Communication layer expanded with provider picker (operator 2026-08-06).
- ✅ Router popup ↔ four-layer mapping (operator 2026-08-06 reference image).
- ⛔ `AssetCheck` four-item hardcoded list + `⚡ FUSE BOX` blocking banner —
  **rejected by the operator.** Rule 7 violation, kept here as the worked example.
- ⛔ Router-as-hardened-gatekeeper — **explicitly rejected.**
- ⬜ `RuntimeDef` reshaped to the four layers — **not built.**
- ⬜ `temperature` / `verbosity` / `cores` / `max_tokens` / hardware target as
  real Runtime params — **not built.**
- ⬜ Provider picker in `RuntimeDef.Communication` — **not built.**
- ⬜ Recovery daemon — **not built.**
- ⬜ Zero-TTL pinning — **not built.**
- ⬜ `RouterPane.switchOn()` consulting the Monitor instead of re-implementing the
  check — **not built.** It also **skips the gate entirely** when no `RuntimeDef`
  matches, so cloud/PWA/terminal configs bypass the Monitor today.
- ⬜ Router hotkey for pushed sessions/hooks/scripts — **not built** (operator
  2026-08-06).
- ⬜ Overflow-bounce (Router full → return to origin tile + GOAT face) —
  **not built** (operator 2026-08-06).

## 6 · Open / to-confirm

- Whether the packet is JSON, YAML, or plain key=value. The operator said
  *"lightweight JSON/YAML spec file"* in one turn and *"just an editable text
  file"* in another — **either satisfies canon; the format is not the point.**
  Pick one at implementation time and record it here.
- Whether Settings hands the packet to the Router directly, or stages it through
  the Archives first.
