---
title: Router — Stereo Stack GUI (LOCKED visual specification)
status: CANON — LOCKED visual specification. Build order deferred; design is not.
scope: the Router tile only (operator-confirmed 2026-07-31)
reference: Aiwa NSX-V20 style component hi-fi stack
---

# Router — the Stereo Stack

> **STATUS: LOCKED SPECIFICATION — NOT CONCEPTUAL.**
> The operator supplied the reference image and said this is what it is going to
> be. That makes it a **specification**, not a mood board, a direction, or an
> option to be reinterpreted later.
>
> **Build order is deferred. The design is not.** "Not being built this minute" is
> a sequencing call the operator made; it says nothing about whether the design is
> settled. It is settled.
>
> Per **Rule 7b** (`../MASTER-BUILD-BLUEPRINT.md` §7): visual references are
> literal build targets. Build this as described, with animations. Softening it
> into "styling direction" is itself the failure this rule exists to stop.

Visual/interaction direction for the **Router tile**, captured 2026-07-31.
**Build order deferred** — operator: *"Don't worry about building the whole
graphical user interface right now, but this is what it's going to end up
looking like."* Recorded so nothing gets built that contradicts it. The deferral is about
*when*, never about *whether*.

Reference: a 90s Aiwa-style **component stereo stack** — CD deck on top,
tuner/amplifier in the middle, dual cassette deck at the bottom. Retro
skeuomorphic throwback, rendered at a slight 3/4 angle, fully touch-driven.

**Scope: the Router tile, and only the Router tile.** Not the app shell, and
not the Monitor (a separate visual reference is coming for that). The
seven-tile home and its geometry are unaffected — you open the Router and
find a stereo.

## Why the Router is exactly the right home for this

The Router is already **the fuse box / the plate** — the one place in the
canon where things get energized, where completed configs live, and where
Sleep / Archive / Swap happen. A component stereo is the same object: a rack
where you load media, tune it, and switch it on.

So the metaphor needs no compromise. Loading media, turning dials and
pressing play are all **writes and ignition**, which is native Router
behavior. The Monitor stays what canon says it is — the read-only checkpoint
that holds no data, transfers no data, and runs static checks with no side
effects. Nothing here pushes execution into the Monitor.
**"Define → Validate → Execute" survives untouched**, with the stereo as the
Execute surface.

## The three decks

### Top deck — CD player = MODELS

> **Operator (2026-08-06):** *"The changer in the router should be animated
> and interactive so you can actually push the button up by the changer and
> you'll watch it — you can see the deck come out and it could spin and you
> hit the CD spot, you can load. When you hit the CDs, a little pop-up comes
> and it looks like [the Aiwa green overlay reference] — you can fine-tune
> it."*

- The **CD/EJECT button is a real interactive control.** Press it and the
  disc tray **physically slides out**, animated at the same 3/4 angle as the
  reference photo. Not a modal, not a nav transition — the tray as a moving
  object.
- The tray holds a **rotating carousel** — a real spin animation, driven by
  swipe or the changer button. (The reference unit is a **CD3** 3-disc
  changer: several models loaded, one engaged.)
- **Tap a disc in the carousel** → a **fine-tune popup** appears rendered
  over the deck, matching the green LCD-style overlay in the operator's
  reference image (`Model_ / Engine_ / Runtime_ / Config._`, each
  `_(select)_`, with `[load] swap [save] edit` along the bottom, `(#)`
  indicator). See §Fine-tune popup below.
- Close the tray to commit.

**Maps to:** plating a model on the Router. The disc left in the engaged
position is `KEY_ACTIVE_MODEL`.

#### Fine-tune popup (rendered over the CD deck)

Per the operator's reference image (Aiwa faceplate with green terminal-style
overlay). Four selectable rows, five actions:

| Row | Selects |
|---|---|
| `Model_` | which weight file is engaged (same set as the carousel — this is the shortcut) |
| `Engine_` | which native engine drives it (`llama_cpp`, `qairt`, cloud connector, terminal agent) |
| `Runtime_` | which loaded runtime file (see cassette deck) executes it |
| `Config._` | which archived parameter packet is applied |

**Actions:** `[load]` · `swap` · `[save]` · `edit` · `(#)` numeric picker.

**All picker-driven. No free-text entry** — per the workbench UX rule, the
Router surface is button-and-list only (see [[UX-RULES]]). Text lives in
Terminal and the browser.

**Naming reconciliation.** These four rows are the *engaged-item shortcut
face* of the four parameter layers in [[../aesop/PARAMETER-PACKET]] §2
(Weights / Runtime / Engine / Communication). The popup uses the shorter
Aiwa-face labels; the parameter packet on disk keeps the canonical four.
`Model_` = the engaged Weights entry; `Config._` folds Communication and any
Weights limits into one archived packet. The popup is a **UI over** the
packet, not a rename of it.

### Middle deck — tuner / amplifier = RUNTIME PARAMETERS

- Touch the middle panel and it **expands**.
- Controls for the Runtime-layer parameters that are currently open in the
  packet: **temperature**, **verbosity**, **core count / thread bindings**,
  **max tokens**, and a **dial to scroll through runtime options**.
- **Hardware target selector** — `npu` / `hybrid` / `gpu` / `cpu`, matching
  GenieX's `--device` aliases. If the loaded runtime advertises multiple
  targets, all three are visibly offered. Currently hardcoded to `"Adreno
  830"` in `HorizonsApplication:116` — that string is a lie on any device
  that isn't a Razr Ultra and has to become device-agnostic; see
  [[../STATE-OF-EXISTENCE]].
- **Cloud-vs-local toggle** — first-class visible switch, not buried.
- **DSP / voice panel** — pitch, speech speed, volume scale, voice-model
  swap. **Extended tonight (operator 2026-08-06): STT tuning as well as
  TTS.** VAD sensitivity, silence-threshold ms, hard-max audio length — the
  Router is the one place these live for the user, not just Kokoro's TTS
  side.
- The **FM / AM band button swaps runtimes** — band = which runtime is live.
- The LCD/VU area is the natural home for live status: green-light readout,
  tokens/sec, memory draw.

**Maps to:** the engaged `RouterConfig` and its tunables (Runtime layer of
the parameter packet).

### Bottom deck — dual cassette = RUNTIME FILES

> **Operator (2026-08-06):** *"The tape decks are where you can load your
> files. One side will have where you can access settings and archives, and
> one will be where you actually load them up. You can load multiple, and
> you can swap between the double-agent query system or a single chatbot or
> mixture of agents. That would also be where you can select the cloud
> connector or terminal agent."*

**Two wells, two distinct roles** — this supersedes the earlier "well A =
RUNNING, well B = SLEEPING" reading:

| Well | Role |
|---|---|
| **Left (Browse/Access)** | reaches into **Settings** (the vault) and **Archives** — browses what's landed, previews, pulls a verified profile back out |
| **Right (Load/Activate)** | where a runtime actually **plates**. Holds multiple loaded runtimes, not just one — you swap between them without unloading |

**Execution modes — swap between them from the Load well:**

- **Double-agent query system** — the two-model NPU ping-pong (executions
  model + query model taking turns; see [[../STATE-OF-EXISTENCE]] for the
  current pairing)
- **Single chatbot** — one model, no ping-pong
- **Mixture of agents (MoA / MoE)** — the composite path from
  [[../MASTER-BUILD-BLUEPRINT]] §1 (Novus-Agenti composite execution core)
- **Cloud connector** — routes through the provider picker (OpenAI /
  Anthropic / OpenRouter / SambaNova / custom — extensible list, not the
  three-hardcoded shortlist the older docs implied)
- **Terminal agent** — a Termux-staged process registered as a Router
  runtime target (new tonight: promotes Terminal-hosted agents to a
  first-class execution backend, not just a script-forging surface)

**Maps to:** `RuntimeDef` + the uploadable runtime binary in the Load well;
the Browse well is a live read into `SettingsPane` + `ArchiveStore` without
leaving the Router.

**RUNNING / SLEEPING** is still meaningful — it's the state of items in the
Load well, not the identity of the wells themselves.

## Why this fits the existing data model

Near-exact match, not a reskin:

| Stereo part | Canon concept | Existing code |
|---|---|---|
| Disc in the tray | landed model asset | model library scan |
| Disc left engaged | the plugged-in model | `KEY_ACTIVE_MODEL` (pin-only) |
| Cassette in a well | a runtime definition | `RuntimeDef` |
| Two wells | RUNNING + SLEEPING | `ConfigStatus` |
| FM/AM band switch | swap the engaged runtime | Router fuse flip |
| Tuner dials | runtime parameters | *partially missing — see below* |
| Power / green lights | greenLight checklist | `greenLight()` |

Critically, this does **not** ask the app to auto-start anything. Inserting
media is not playing it; you still press the button. **"Daemons stay dumb,
the user is the loader" survives the reskin intact** — a stereo is arguably
the most literal possible expression of it.

## The one gap this exposes

**Runtime parameters are not first-class yet.** `temperature` exists only as
a hardcoded value inside `NpuClient`'s request body. **Verbosity and core
count do not exist anywhere in the codebase.** For the tuner deck to be
real, these must live on the runtime config — either as fields on
`RuntimeDef` or as substitutions in `argsTemplate` alongside the existing
`{model}` / `{port}`.

Worth designing in *before* the launcher is made runtime-agnostic
(EXECUTIONS P1.3), since it is the same code path. Otherwise the launcher
gets reopened a second time to retrofit the parameter channel.

## Cross-tile pathways to the Router

> **Operator (2026-08-06):** *"All six tiles should have a pathway to the
> router."*

All six clock-face tiles push to the Router — not just the subset drawn in
the older circuit diagrams. Concretely: Chat pushes prompts and drafted
runs; Settings hands over supplied assets/keys; Terminal forges packets and
pushes them; Archives restores verified profiles; Horizons pushes its
unlockable Easter-egg payload; Monitor dispatches on greenLight pass. The
Router is the common sink.

## Overflow — bounce, don't refuse

> **Operator (2026-08-06):** *"If the router's device storage is full it'll
> just load back into archives or settings or wherever it was pushed from,
> and the 404 goat can pop up."*

If the Router (or the device the Router is loading into) is full when
something arrives, it **bounces back to the origin tile** (Archives,
Settings, wherever it was pushed from) rather than failing hard. A failure
face surfaces — GOAT for the bounce event. The Router still doesn't say
*no*; overflow is a naturally failed close, and the packet is preserved at
its source.

## Router hotkey for pushed items

> **Operator (2026-08-06):** *"If any sessions or hooks or scripts are
> pushed to the router there should be a hotkey there so you can turn it on
> or off."*

Anything landed on the Router by push (a Terminal session, a hook, a
script, a cloud connector) surfaces with its own **on/off hotkey right on
the Router face**. No trip back to Terminal/Archives to disable it. The
hotkey is a toggle, not a delete — the item stays plated, it just doesn't
carry current until the hotkey flips.

## Related

- [[MONITOR-ARCADE-CABINET-SPEC]] — the read-only checkpoint the Router
  consults at flip time.
- [[TERMINAL-SPEC]] — the mod garage that forges packets and now also hosts
  the on-device agent that can port over to the Router.
- [[UX-RULES]] — the workbench-wide rules (no typing outside Terminal /
  browser, long-press-for-help, zoom, inset-cropping) that this Router
  surface obeys.
- [[../aesop/PARAMETER-PACKET]] — the four-layer packet the popup and tuner
  are UIs over.
- [[CRASH-ANALYSIS-2026-07-31]] — current boot-stability work.
