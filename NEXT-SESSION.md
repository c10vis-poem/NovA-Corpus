# NEXT SESSION — Termux / on-device

**Written:** 2026-08-06, end of cloud session.
**Purpose:** get the next session running *on the phone*, with full context, in one paste.

---

## 0 · The thing that keeps not happening

Claude cannot move itself onto the device. A cloud session stays a cloud session for its
whole life. **Only the operator can start an on-device session**, by running `claude`
inside Termux. That session's container *is* the phone — file reads, git, model files,
`/sdcard`, everything local.

There is no handoff mechanism between the two. The bridge is this file plus the repo.

---

## 1 · Start the session (on device)

```
pkg up -y
```
```
pkg i git nodejs -y
```
```
npm i -g @anthropic-ai/claude-code
```
```
cd ~ && git clone $R corpus
```
> set `R` first: `R=https://github.com/c10vis-poem/NovA-Corpus.git`

```
cd ~/corpus && claude
```

Once `claude` is running, the claude.ai app/browser is just the UI. Execution is on
NODE_ALPHA.

---

## 2 · Paste this as the first message

```
Read NEXT-SESSION.md, CLAUDE.md, and
device-stacks/horizons-ui/DEVICE-INVENTORY.md.
You are on NODE_ALPHA now. Confirm by running:
  ls /sdcard/LeGRAND_REPOSITORY/MODELS
Then work section 3 of NEXT-SESSION.md in order.
```

---

## 3 · Work queue, in order

Ordered so each step unblocks the next. Steps 1–3 are cheap and answer questions that
have been open for two sessions.

### 3.1 · Answer the crash question (5 minutes, unblocks everything)

```
cd /sdcard/Android/data/com.horizons/files/diag
```
```
tail -40 crash.log
```
```
tail -30 boot.log
```

**Decision rule:**
- Stack trace present → JVM exception. Fix it, it's in the code.
- Empty but the app died → killed from outside (LMK / FGS). No trace will ever appear.
  Root cause is memory pressure: Kokoro pulls ~200 MB at boot, then a 326 MB ONNX loads
  in-process. That is a *scheduling* fix, not a bug fix.
- `boot.log` lines are tagged `[main]` / `[clifford]` — that answers "did `:clifford`
  come up?"

This has been the blocking unknown since session 20. It costs one command.

### 3.2 · Reclaim ~5.8 GB

```
cd /sdcard/Download
```
```
rm Qwen3.5-9B-Q4_0.gguf
```
(duplicate — the real one is in `LeGRAND_REPOSITORY/MODELS/`)

```
mv granite-4.0-h-micro-Q4_0.gguf ../LeGRAND_REPOSITORY/MODELS/
```

Then empty the trash in the file manager — 4 × ~106 MB neuro-mesh PDFs = 422 MB.

### 3.3 · Identify the three inference paths

The device carries **three** and the corpus documents **one**. This is the largest
undocumented area in the whole system.

```
cd /sdcard/LeGRAND_REPOSITORY/HARNESS
```
```
ls -la Llama.server QNN-QAIRT
```
```
cat nexa.manifest
```
```
head -c 200 tokenizer_config.json
```

| Path | Artifact | Coverage |
|---|---|---|
| llama.cpp / GGUF | `MODELS/*.gguf`, `Llama.server/` | documented |
| GenieX / QNN | `qwen3_vl_4b_instruct-geniex_*` | `wiki/GENIEX-DAEMON-PLAN.md` — **unread** |
| ExecuTorch / QNN HTP | `hybrid_llama_qnn.pte` (930 MB) | **nothing** |

Read `GENIEX-DAEMON-PLAN.md` (it's in Drive, `(*8-5)` folder). Then ask the operator
which path is production for NODE_ALPHA. Do not guess — this decides the launcher.

Also resolve the 561 MB mystery:
```
cd /sdcard/AESOP_HORIZONS.main/GOOGLE\ _DEV
```
```
ls | grep -i json
```

### 3.4 · Close the voice loop — Moonshine STT in-process

The one real, known, scoped code fix. Repo: `c10vis-poem/Horizons-UI`,
branch `claude/undo-init-command-ye6ejs`.

**The defect:** STT points at `127.0.0.1:8091`. Nothing binds it. The loop silently falls
back to `llmRuntime.streamAudio`, which makes it look like a model problem. It is not.
TTS already works in-process on the sherpa AAR.

**The fix:** run Moonshine STT in-process on the AAR that already ships. The model repos
exist: `Mer0vin8ian/moonshine-streaming-small-onnx`.

**Do not touch `HomeGrid.kt`.** Frozen at `984b061`. Not for a layout tweak, not for a
CI-breaking fix. If it's implicated: stop, report, wait for sign-off.

### 3.5 · Termux backend listener

The app has **zero inbound listeners**. Termux already shares loopback with the app's UID,
and the app-spawned daemon already binds `127.0.0.1:8080` — so **NPU access needs no
inversion**. What Termux cannot get on its own is **mic, voice, and WebView-OAuth**. That
is what the listener is for. Scope it to exactly those three.

### 3.6 · Runtime params first-class — before P1.3

`temperature` is hardcoded at `NpuClient:101` and `CloudLlmRuntime:122`. `verbosity` has
a Settings slider **nothing reads**. Cores don't exist.

Per canon these are not four ad-hoc fields — they belong under the operator's four-layer
parameter taxonomy:

1. **Weights** — paths, INT8/ONNX quant limits, tensor allocations
2. **Runtime** — execution flags, RAM allocations, thread bindings ← temperature/verbosity/cores live here
3. **Engine** — native JNI/C++ (`libsherpa-onnx-jni.so`, `libllama.so`), VAD sensitivity
4. **Communication** — IPC sockets, WebSocket bridges, API router endpoints

Make them real `RuntimeDef` params **before** the runtime-agnostic launcher, or the
launcher gets reopened twice.

---

## 4 · Standing law — do not relitigate

**Authority model (series circuit).** Settings supplies assets/keys and may hand a config
to the Router, but has **no authority to run it**. Terminal writes the fuse spec, never
executes. **Monitor is the switch in the loop** — stores nothing, dispatches, holds the
verdict. Router is fuse box + breaker: carries current, doesn't argue. Validation is live
at flip time (a series switch has no memory) but the check belongs to the **Monitor**.
`RouterPane.switchOn()` re-implementing it is the one real defect. The operator
**explicitly rejected** Router-as-gatekeeper.

**Known bypass:** `switchOn()` skips the gate entirely when no `RuntimeDef` matches — so
cloud/PWA/terminal configs never reach the Monitor today.

**Rule 6 · Designed ≠ Built.** Never overwrite an `absent` or `designed-only` row with
intent prose. A file being present is not the file working.

**Rule 7 · Metaphor ≠ Implementation.** Fuse box, 10-amp fuse, breaker, arcade cabinet,
stereo stack — these are interface and config-file design language. They are **not**
specifications for enforcement code. A prior agent compiled "10-amp fuse" into a hardcoded
four-item `AssetCheck` and broke custom runtimes. Record the metaphor; never promote it
into a constraint.

**Frozen.** `HomeGrid.kt` at `984b061`. Also `HomeGrid.kt:69` computes `npuReady` from
`startsWith("Adreno 830")`, which the NO-BACKEND fallback string also matches —
**report, don't fix**.

**Base branch trap.** Horizons-UI: `main` does **not** carry the working home screen. Base
is `RELEASE-correct-home-screen-984b0610`. Run `git branch -a` before choosing a base.

**Never** push `main` without permission. Never `--no-verify`, `push --force`, or
`reset --hard` without confirming.

**Patent flag.** Metamaterials designs and novel thermal management stay out of every
public or shared repo until filed. Private local storage or the GCP enterprise bucket only.

**Red Agent Auditor is air-gapped.** The operator is the only conduit in. Not reachable
from Horizons UI or any shared platform.

**AI transcripts are sources, not canon.** Operator turns inside them are canon and get
quoted with attribution. The AI prose around them goes to `pending-corpora/`.

---

## 5 · Where things are

| Thing | Location |
|---|---|
| Corpus repo | `c10vis-poem/NovA-Corpus` *(renamed from OBSIDIAN-Master_Wiki)* |
| App repo | `c10vis-poem/Horizons-UI` |
| Protocol | `c10vis-poem/aesop` |
| Skills | `c10vis-poem/nova-skills` |
| Branch, all repos | `claude/undo-init-command-ye6ejs` |
| On-device root | `/sdcard/LeGRAND_REPOSITORY/` |
| Models on device | `/sdcard/LeGRAND_REPOSITORY/MODELS/` — 8 files, ~32 GB |
| Runtimes on device | `/sdcard/LeGRAND_REPOSITORY/HARNESS/` |
| App diagnostics | `/sdcard/Android/data/com.horizons/files/diag/` |
| HF account | `Mer0vin8ian` — 15 model repos |
| Published artifacts | `claude.ai/code/artifacts` (private) |

**Open PR:** #6 on NovA-Corpus, draft, this branch. Operator monitors it — do not
schedule check-ins.

---

## 6 · Artifacts published (private, operator's gallery)

| Artifact | Style |
|---|---|
| modu14r Master Index | document |
| AESOP XI Protocol Brief | document + sidebar |
| AESOP XI System Dashboard | TUI panels |
| Nova Corpus Device Stack | TUI panels |

TUI is the confirmed direction. Still queued: Memory Layer deep-dive (OB1 + mem0 +
OmniRoute), NovA-Claw execution surface, corpus/canon format.

---

## 7 · Still open — operator calls, not agent calls

1. Which inference path is production for NODE_ALPHA? (§3.3 — three exist, one documented)
2. Whisper-base vs shipped Moonshine — canon says Whisper, CI run #353 shipped Moonshine
3. Two launcher icons: `.MainActivity` + `.uilocal.LocalHomeActivity` both carry
   MAIN/LAUNCHER and run different code. Remove the second?
4. Two Gemma 12B quants (6.72 + 6.98 GB) — drop one, free ~7 GB?
5. NovA-Claw + Novus-Agenti — one repo or two?
6. `global-documentation-vault/` weight — LFS or separate repo?
7. OmniRoute built-in memory — cache/fallback, or disabled?
