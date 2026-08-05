---
title: Router — Stereo Stack UI (visual + interaction direction)
status: DIRECTION CAPTURED — not being built yet
scope: the Router tile only (operator-confirmed 2026-07-31)
reference: Aiwa NSX-V20 style component hi-fi stack
---

# Router — the Stereo Stack

Visual/interaction direction for the **Router tile**, captured 2026-07-31.
**Not to be built yet** — operator: *"Don't worry about building the whole
graphical user interface right now, but this is what it's going to end up
looking like."* Recorded so nothing gets built that contradicts it.

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

- Tap the **CD** button and the **disc tray slides out**, seen at the same
  3/4 angle as the reference photo.
- The tray holds a **rotating carousel** — spin through your models and swap
  them by touch. (The reference unit is a **CD3** 3-disc changer, which is
  exactly right: several models loaded, one engaged.)
- Close the tray to commit.

**Maps to:** plating a model on the Router. The disc left in the engaged
position is `KEY_ACTIVE_MODEL`.

### Middle deck — tuner / amplifier = RUNTIME PARAMETERS

- Touch the middle panel and it **expands**.
- Controls for **temperature**, **verbosity**, **core count**, and a **dial
  to scroll through runtime options**. More dropdowns to come.
- The **FM / AM band button swaps runtimes** — band = which runtime is live.
- The LCD/VU area is the natural home for live status: green-light readout,
  tokens/sec, memory draw.

**Maps to:** the engaged `RouterConfig` and its tunables.

### Bottom deck — dual cassette = RUNTIME FILES

- **Runtimes load as files, into the cassette wells.** "Files run in the
  cassettes."
- Dual well = two runtimes loaded at once, one playing and one on deck —
  which lines up exactly with `RUNNING` vs `SLEEPING` / "on the deck". No new
  concepts needed.

**Maps to:** `RuntimeDef` + the uploadable runtime binary. A cassette *is* a
runtime definition: binary name, port, health path, args template.

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

## Related

- Monitor tile: separate visual reference pending — do not assume it shares
  this treatment.
- [[CRASH-ANALYSIS-2026-07-31]] — current boot-stability work.
