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
> **Verification rule.** Verified against the operator. Where the source folder
> conflicts with later operator statements, the later statement wins and the
> conflict is recorded in §8 rather than silently resolved.

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

## 8 · Conflicts with the source folder — recorded, not silently resolved

The folder is a **summarization set, not a spec**, and parts of it are superseded.
Later operator statements win.

| Source says | Canon is | Note |
|---|---|---|
| Settings **4:30**, Archives **7:30**, Horizons **Top-Left**, Chat "East of Monitor" | positions are **not discussed** — the home screen is **done** | Doc 4 is marked **`[NEEDS EDIT]`** by the operator himself |
| Router is a **"10-amp fuse" gatekeeper** that "blows" and blocks | **The Router does not say no.** It attempts to close the circuit; failure is a circuit that didn't energise, never a lockout | **Rule 7a.** Compiling this literally produced the hardcoded `AssetCheck` list and the blocking `⚡ FUSE BOX` banner that broke custom runtimes |
| "Four Rooms & Seven-Tile" | seven functional rooms; the four-room framing is superseded | |
| Idle screensaver **5 minutes** | **3–5 minutes** | operator, later |
| `greenLight` runs **five** checks (doc lists three, unfinished) | **four**, as in §4 | the five-check list in doc 4 is visibly truncated |

**The "10-amp fuse" is the single most dangerous line in that folder.** It reads
like an instruction to build a blocker. It is not. See Rule 7a and
[`../aesop/PARAMETER-PACKET.md`](../aesop/PARAMETER-PACKET.md).

---

## 9 · Status ledger

- ✅ Philosophy, workflow, room ownership, `greenLight`'s four checks, RouterConfig,
  RuntimeDef fields, the three failure faces — **operator-curated**.
- ✅ Visual treatments — corroborated by `HOME-REDESIGN-SPEC.md` and the locked GUI specs.
- ⬜ Process architecture (§6) — **AI-sourced, unverified.** Principle sound,
  mechanisms are candidates.
- ⛔ Tile positions from this folder — superseded. Home screen is done.
- ⛔ Router-as-gatekeeper — **rejected** by the operator.
- ⬜ **Nothing here is a build-state claim.** See `../STATE-OF-EXISTENCE.md`.

## 10 · Open

- `greenLight` currently checks **2 of the 4** in §4 (engine, assets) — no exec-bit
  or handshake check. Needs verifying against live code.
- Whether the engine split is `:qairt_engine`/`:llamacpp_engine` as described, or
  the existing `:clifford` process arrangement.
- The remaining folder files not yet mined: `GENIEX-DAEMON-PLAN.md`, `Horizons.txt`,
  `I have created.txt`, `openwiki.md`, the 81 KB Gemini duel doc (which the operator
  notes retracts its own central claim), and docs 1–3 in the numbered sequence.
