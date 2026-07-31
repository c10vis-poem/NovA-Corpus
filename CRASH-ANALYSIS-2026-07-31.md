---
title: Crash analysis — landing-screen crash, 2026-07-31
status: fixes pushed, unverified on device
pr: c10vis-poem/Horizons-UI#32
---

# Crash analysis — 2026-07-31

**Symptom (operator):** app crashes ~90 s after landing on the home screen,
gets worse over repeated launches, appears to still be trying to connect.

**Operator's hypothesis:** "the thing that's actually logging the crashes is
probably helping to cause it."

**Verdict: that hypothesis is correct.** Confirmed by code inspection with
file:line evidence. It is not the whole story, but it is real and it explains
the specific "gets worse" part of the symptom.

## The feedback loop (explains "gets worse every launch")

Three defects that compose into a closed loop:

1. **`FailureMonitor.install()` built a full report synchronously on the main
   thread** inside `HorizonsApplication.onCreate()` — walking every crash file
   and every log file on every app start.
2. **Every "tail" read was actually a whole-file read.** `File.tailText()`
   called `readText()` on the entire file before taking the last 2 KB;
   `collectRecorded()` / `collectErrorLogLines()` called `readLines()` on whole
   append-only logs. Cost scaled with all history ever recorded.
3. **`Breadcrumb`'s `crash.log` had no size cap and no rotation at all**, while
   `boot.log` had a 256 KiB one. Every crash appended a full stack trace forever.

```
crash  →  crash.log grows  →  next boot's main-thread read is bigger
  ↑                                          ↓
  └──────────  more likely to crash  ←  slower, heavier startup
```

Each of the three is now bounded independently, so the loop cannot close.

A fourth, separate waste: `Breadcrumb.last()` streamed the **entire** boot.log
to get its last line, and `CliffordService` re-posted its notification
unconditionally every 15 s — so an idle app did a full-log read every tick.

## The cross-process bug (explains "still trying to connect")

`CliffordService` runs in the **`:clifford` process** (`android:process=":clifford"`
in the manifest). Android constructs a **separate `HorizonsApplication`** in that
process, so `CliffordService` sees a **different `RouterConfigStore` instance**
than the UI does.

`RouterConfigStore` loaded `router_configs.json` **once in `init`** and never
re-read it. Therefore:

> **A Router flip performed in the UI process was permanently invisible to the
> launcher. Flipping a fuse could not start a daemon, under any circumstances.**

This independently matches the operator's own recorded evidence in
`I have created.txt`: the model path *was* written successfully to the vault
(`genie.active_model_path = /storage/.../Qwen_Qwen...`), but Clifford never
acted on it. The selection side worked; the act-on-it side was structurally
disconnected.

Fixed via `RouterConfigStore.reloadIfChanged()` (mtime/length check, re-parse
only on actual change), called by Clifford before it decides.

## What is NOT yet explained

**The trigger of the first ~90 s crash on a clean install.** The four defects
above explain degradation and the connect-forever state; they do not by
themselves prove what kills a fresh process at ~90 s. Live candidates:

- **Android Low Memory Killer.** Leaves *no stack trace* — the app just
  vanishes. Would look exactly like this. The corpus flags KV cache adding
  0.5–1 GB *on top of* model weights against a 6 GB bloated floor, and nothing
  in the code budgets for it. There is still **no amperage/RAM check** in
  `greenLight()` (EXECUTIONS P3).
- **`KokoroModelManager.ensureReady()`** pulls a **~200 MB** archive from GitHub
  at boot, then extracts it; `SherpaOnnxTtsClient.init()` then loads the ONNX
  model in-process.
- **`:clifford` being killed by Android** before it posts its notification.

## How to settle it — on device, no laptop, no adb

The evidence already exists on the phone. Both files are in per-app scoped
storage, readable by any file manager or Termux:

```
/sdcard/Android/data/com.horizons/files/diag/crash.log   ← stack traces
/sdcard/Android/data/com.horizons/files/diag/boot.log    ← where it died
```

Termux:

```sh
cd /sdcard/Android/data/com.horizons/files/diag
tail -40 crash.log
```

- **`crash.log` has a stack trace** → it's a JVM exception; the trace names it.
- **`crash.log` is empty but the app died** → it was killed from outside
  (LMK / FGS timeout). Not an exception; no trace will ever appear.

`boot.log` lines are now **tagged with the writing process** (`[main]` /
`[clifford]`). Previously both processes appended to the same file with no way
to tell them apart, which is why triage kept stalling on "did `:clifford` ever
come up at all?" That question is now answerable by reading the file.

Also check: **is the CLIFFORD notification in the shade?** If not, `:clifford`
is not alive.

## Contradictions found — operator decisions, not silently resolved

1. **Router gatekeeper.** The operator explicitly rejected hard-refusal at flip:
   *"I don't like the hardened gatekeeper aspect... it's just another thing that
   can break"* — the Router should *"simply let the current flow"* and a mismatch
   should *"fail to bridge the connection naturally, without the app itself
   throwing an artificial crash or block."* But the formal build map at the
   bottom of the **same document** still specifies strict re-validation at flip,
   and `EXECUTIONS.md` records that behavior as "canon-correct, keep exactly."
   **The shipped behavior was built from the half of the document the operator
   overruled.**
2. **Auto-detection was left in deliberately.** In `2026-07-17.md` the model
   offered: *"that's a two-line change; say the word and I'll flip it to
   hard-manual."* **The operator never answered, and it was left in** — this is
   the P0 boot regression. (`resolveNpuModelPath()` is now pin-only, so this
   specific one is closed.)
3. **`HomeGrid` reports ready when there is no backend.** `HomeGrid.kt:69`
   computes `npuReady` as `backendStatus.startsWith("Adreno 830")`, and the
   *fallback* runtime's status string is `"Adreno 830 · no backend"`. So the
   no-backend state reads as ready. **`HomeGrid.kt` is operator-frozen — reported,
   not touched.**
4. **Retry/poll behavior has no design authority.** No timeout, retry loop,
   reconnect, or health-poll cadence appears anywhere in the conceptualization
   corpus. The CRS loop and the boot-time health polling are emergent
   implementation, not specified design.

## Branch note

`main` does **not** contain the frozen home screen (`984b061`). The working-UI
lineage is `FROZEN-correct-home-screen-984b0610` /
`RELEASE-correct-home-screen-984b0610`. The two lineages differ in app code
**only** in `HomeGrid.kt` + its two font assets. Work must branch off the frozen
lineage, not `main`.
