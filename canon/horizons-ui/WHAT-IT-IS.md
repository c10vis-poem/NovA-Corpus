---
title: Horizons-UI — What It IS / What It DOES
status: CANON (summarization) — assembled 2026-08-05 from the operator's curated folder
source: Drive `(*8-5) What_it_IS_/What_it_DOES-Horizons _Ui` (13 files) + prior canon
scope: the end product — what this app is, what it does, and how a job moves through it
---

# Horizons-UI — What It IS / What It DOES

> **What this is.** The end-product definition. If someone asks "what is Horizons,"
> this answers it. Assembled from the operator's own curated summarization folder,
> reconciled against existing canon.
>
> **Guiding principle.** This is **what it should BE**, not what is built. Nothing
> here is a status report — see
> [`../STATE-OF-EXISTENCE.md`](../STATE-OF-EXISTENCE.md) for that. Several
> mechanisms described here have no code behind them.
>
> **Verification rule.** Verified against the operator. The source folder is
> **grout** — it fills gaps and holds the tiles in place, and gets read *alongside*
> the latest information rather than against it. Where it is older, the newer thing
> simply wins; §8 notes the divergences without making a drama of them.

---

## 1 · What it IS, in one paragraph

Horizons is a **manual, modular workbench for on-device AI** — not a black box, not
an assistant that guesses. The Kotlin UI is a visual **operating system**: a
lightweight, stable shell that **boots completely empty**. Every heavy component —
the Chromium browser, the terminal, the inference engines — runs as an independent
**"guest port"** in its own decoupled process *beneath* the UI. Nothing spins up
until the operator explicitly flips a switch.

> **Core law: "Daemons stay dumb, the user is the loader."**

The design exists because the alternative kept failing. Legacy auto-boot behaviour
tried to detect and silently load model weights at startup, producing OOM kills and
silent background failures. Horizons inverts that: **inert on arrival, live only on
command.**

| | Legacy auto-boot | Horizons manual loading |
|---|---|---|
| **Startup** | auto-detects and secretly loads | boots to a clean, empty workbench |
| **Memory** | high, unpredictable, OOM-prone | low and stable; used only on activation |
| **Crash risk** | silent background failures | manual fuses prevent structural crashes |
| **Agency** | system-driven black box | **architect-driven** |

---

## 2 · What it DOES — the three-step workflow

Everything the app does reduces to moving an inert file into a live engine, in
three steps. This is *the* operational loop.

```
   ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
   │  1 · LAND    │─────►│ 2 · VERIFY   │─────►│ 3 · FLIP     │
   │              │      │              │      │              │
   │  SETTINGS    │      │  MONITOR     │      │  ROUTER      │
   │  the Armory  │      │  Checkpoint  │      │  the Fuse Box│
   │              │      │              │      │              │
   │ assets land  │      │ greenLight   │      │ circuit      │
   │ INERT        │      │ 4 checks     │      │ closes       │
   └──────────────┘      └──────────────┘      └──────────────┘
                                                      │
                                              ┌───────┴───────┐
                                              ▼               ▼
                                          RUNNING          fails
                                              │           naturally
                                              ▼          (no lockout)
                                        SLEEP / ARCHIVE
```

**1 · Land.** `Open with → Horizons` on any `.gguf`, `.so`, or plugin. The file
registers in the Armory and sits **inert** — in the pantry, disconnected from power.
It cannot cause memory pressure or a startup crash because nothing loads it.

**2 · Verify.** The Monitor runs `greenLight()` — see §4. **All Green** means valid.
**N Red** names the specific blown fuse.

**3 · Flip.** The Router re-runs every check **at the moment of ignition**, then
closes the circuit. If it can't, it fails naturally and tells you why.

---

## 3 · The rooms — what each one owns

| Room | Metaphor | Owns |
|---|---|---|
| **Monitor** | Checkpoint / Library | `greenLight` verification · the **main browser** (full Chromium chrome + sidebar) for window-shopping and test-driving cloud interfaces · oscilloscope signal view |
| **Chat** | The Stage | agentic engagement, artifacts, the OS tool surface |
| **Settings** | Platform Armory | the vault — model weights, API keys, QAI Hub tokens, SDKs, binaries. **Bake & Export.** |
| **Terminal** | Mod Garage | custom forgings, `.sh` harnesses, runtime definitions, on-device CLI |
| **Archives** | Artifact Vault | `.sh` harnesses, saved environments, snapshots, logs — real files, breadcrumb navigation |
| **Horizons** | Front Desk | legal, credits, Pioneer Tech / system info |
| **Router** | The Fuse Box | plating and ignition — the execution centre |

---

## 4 · greenLight — the four checks, named

This is the concrete verification contract, and it is the **canonical definition of
"all four boxes"**:

1. **Binary presence** — is the engine file (`libgeniex.so`, `genieX-daemon`,
   `llama.cpp`) actually readable at the storage path?
2. **Exec permissions** — is the **exec bit** set? (`chmod +x` so it can actually run)
3. **Asset availability** — are the required `.so` plugins, libraries and QAI Hub
   bundles all accounted for and correctly linked?
4. **Model plug-in** — has the operator *explicitly* plugged in a weight file?

Feedback is **All Green** or **N Red**, and red **names the failure** — *"Missing
`libgeniex.so`"* — never a generic exit code.

**Just-in-time re-check.** The Router re-runs all four at the instant of ignition.
If a model was unplugged or an SDK moved after the Monitor approved, the switch does
not close. *A series switch has no memory.*

---

## 5 · The data model

**RouterConfig** — what gets "plated":

| Field | Is |
|---|---|
| **Runtime** | the execution environment, defined in Terminal |
| **Backend** | the specific engine — `qnn_sdk_ggml`, `llama.cpp` |
| **Model** | the plugged-in weight file |
| **Assets** | required secondary files — SDKs, tokens, `.so` plugins |

**Router states:** `Ready to Run` · `Running` · `Sleeping` (+ `Archive`).
**Sleep** unloads from memory but keeps the config on the deck.

**RuntimeDef form** (Terminal) — the five fields a custom runtime declares:
**Name · Binary · Port · Health Endpoint · Args Template.**

**Shell history long-press:** Copy · Export to Router (as a temporary runtime) ·
Save to Commands · Archive (writes a real `.sh` into the ArtifactStore).

**ArchiveStore:** a real directory tree at `filesDir/archive`. Real files on disk.

---

## 6 · Process architecture — why it doesn't buckle

The whole point of the decoupling:

- **Engines run as separate native processes** — `:qairt_engine`, `:llamacpp_engine`
  — invisible to the main rendering loop. **JVM GC pauses can't stutter the UI**,
  because the inference isn't in the JVM.
- **Fault isolation.** If an engine panics or hits OOM, **only that daemon dies.**
  The orchestrator detects the process drop, clears the shared memory descriptor,
  and re-initialises — the UI never knows.
- **Zero-copy.** `memfd_create` / `ASharedMemory` — the daemon writes once, the NPU
  reads from the same physical address space. No CPU copy tax.
- **Standardised UNIX socket protocol** between frontends and backends, which is
  what makes engines **swappable without touching the UI**: compile a new daemon
  binary, drop it in, let the orchestrator route to it.
- **CliffordService** — the background daemon manager, an **FGS `specialUse`**
  process. Android silently kills background threads when a UI gets heavy; keeping
  the daemon separate is what keeps inference alive under load.

> ⚠ The `:qairt_engine` / `:llamacpp_engine` / zero-copy detail is **AI-sourced**
> from the folder and unverified against code. The *principle* — separate processes,
> socket protocol, swappable engines — is consistent with everything else. The
> specific mechanisms are candidates (Rule 5).

---

## 7 · Look and feel

**Obsidian.** Volcanic-glass base with **six large angular facets** and specular
glints. Tiles connect to the centre by **layered plasma conduits** — tubes with a
centred glow and **animated nodes/beads travelling along each line**, each in its
tile's colour.

**The Crystal.** Symmetrical quartz at the hub: **30° bevel cap, 45° perspective**,
distinct front face, right side face, top cap facets, bottom taper. **Violet** gem
with a **white sun glow from underneath**. `ROUTER` in white.

**Per-room treatments.** Settings = brushed-steel **vault door**, concentric rings
and bolt circles. Terminal = **Matrix waterfall**, falling green katakana/ASCII.
Chat = **rain-splashed slate** — blue-grey stone, cracks, water droplets. Horizons =
**amber sun** with rays, blue horizon line, pale pinkish-purple arch on a **nebula**.
Monitor = animated **oscilloscope**.

**Banner:**
```
MØ[)u14R_ 11(
*Pioneer_Tech (Next-Gen Certified)
```

### The three failure faces — distinct, do not merge

| Face | Fires when | Is |
|---|---|---|
| **GOAT** | handshake fails / fuse blows on activation | `// GOAT_SAYS_NO` overlay + a **synthesized sawtooth bleat with vibrato and tremolo** — a warbling "meh-eh-eh". A structural failure banner **instead of a crash.** |
| **ASCII 404 CAT** | connection failure or dropped websocket **inside the Monitor's browser** | a browser-scoped network error. **Not** an engine failure. |
| **CHONK** | idle timeout | the chonky cat screensaver, loaded at runtime from `/storage/emulated/0/Download/` (`chonk.jpg`/`.png`/`.webp`) |

---

## 8 · Grout

This material is **grout**, not tile. It fills gaps and holds things in position,
and it gets read alongside the latest information. Where it's older — tile
positions, "four rooms," a five-minute idle timer — the newer thing just wins. Use
common sense; none of that needs adjudicating.

**The one worth knowing about:** the folder describes the Router as a *"10-amp fuse"
that blows and blocks*. The metaphor is the operator's own and it's a good one — but
a previous agent **compiled it literally** into a hardcoded `AssetCheck` list and a
blocking `⚡ FUSE BOX` banner, which broke custom binaries and fine-tuned weights.

The grout was fine. The reading was wrong. **The Router doesn't say no** — it
attempts to close the circuit, and failure is a circuit that didn't energise, not a
lockout. Rule 7a, and [`../aesop/PARAMETER-PACKET.md`](../aesop/PARAMETER-PACKET.md).

## 9 · Status ledger

- ✅ Philosophy, workflow, room ownership, `greenLight`'s four checks, RouterConfig,
  RuntimeDef fields, the three failure faces — **operator-curated**.
- ✅ Visual treatments — corroborated by `HOME-REDESIGN-SPEC.md` and the locked GUI specs.
- ⬜ Process architecture (§6) — **AI-sourced, unverified.** Principle sound,
  mechanisms are candidates.
- ◻ Tile positions from this folder — older. Home screen is done; not discussed.
- ⛔ Router-as-gatekeeper — **rejected** by the operator. The metaphor is his and it
  is fine; compiling it literally is what was wrong.
- ⬜ **Nothing here is a build-state claim.** See `../STATE-OF-EXISTENCE.md`.

## 10 · Open

- `greenLight` currently checks **2 of the 4** in §4 (engine, assets) — no exec-bit
  or handshake check. Needs verifying against live code.
- Whether the engine split is `:qairt_engine`/`:llamacpp_engine` as described, or
  the existing `:clifford` process arrangement.
- The remaining folder files not yet mined: `GENIEX-DAEMON-PLAN.md`, `Horizons.txt`,
  `I have created.txt`, `openwiki.md`, the 81 KB Gemini duel doc (which the operator
  notes retracts its own central claim), and docs 1–3 in the numbered sequence.

---

## 11 · The daemon lifecycle contract — "alive ≠ ready"

**Operator observation (2026-08-05):** the daemon still looks for a model the
instant it starts, tries to size it up, finds nothing, and crashes out.

That is a **regression against a fix that is already documented.**
`GENIEX-DAEMON-PLAN.md` states the crash-loop fix explicitly:

> **The crash-loop fix** — serve-first: bind `:8080` immediately, load the model
> on a background thread, serve `/health` 503 until ready, **never suicide on a
> bad/missing model.** GenieX's launcher must preserve this **"alive ≠ ready"**
> property so the watchdog never thrashes.

### The contract, in order

1. **Bind the port first.** `:8080` opens **before** any model work begins.
2. **Load on a background thread.** Never on the accept loop, never at start.
3. **Serve `503` until ready.** Port open + not ready is a *valid, healthy state.*
4. **Never suicide on a bad or missing model.** No model is the **normal boot
   state** — the app boots empty by design and the user is the loader. A daemon
   that dies without a model has misread an empty workbench as a fault.
5. **Readiness is a probe, not an assumption.** `GET /v1/models` → 200 once the
   model is registered. Port open but not 200 means **loading**, not **dead**.

### Why violating it is worse than one crash

`CliffordService` is a watchdog: FGS, `START_STICKY`, exponential backoff,
5-strike relaunch. If the daemon exits because no model is plugged in, the
watchdog **relaunches it into the same empty state** — which exits again. That is
a self-feeding crash loop, and it costs battery and log volume on every cycle.

This compounds the diagnostics loop already found and fixed in
[`CRASH-ANALYSIS-2026-07-31.md`](CRASH-ANALYSIS-2026-07-31.md): crash → bigger log
→ heavier boot → more crashes. **A daemon that suicides on no-model plus a
watchdog that relaunches it is a second, independent crash loop feeding the same
log.** It is a strong candidate for the unexplained ~90 s first crash, and unlike
LMK it would leave evidence.

### The anti-pattern, concretely

```kotlin
// WRONG — hard throw on missing model
if (!modelFile.exists()) throw IllegalArgumentException("Target binary not found.")
```

Found in the July-3rd APK material. Under Rule 7a this is the same failure class as
the `AssetCheck` blocker: the *absence of a loaded model is not an error*, it is
Tuesday. The **Monitor** reports it as a red light; the **daemon** must not die of it.

### How to confirm on device

`boot.log` lines are tagged `[main]` / `[clifford]`. A repeating `[clifford]`
start → exit → start pattern with no model plugged in **confirms this**, and
distinguishes it from an LMK kill — LMK leaves no trace, this leaves a rhythm.

**Status:** `⬜ unverified against live code.` The fix is documented; whether it is
implemented, or was implemented and regressed, has not been checked.
