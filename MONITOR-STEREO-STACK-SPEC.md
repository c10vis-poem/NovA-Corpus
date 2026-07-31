---
title: Monitor — Stereo Stack UI (visual + interaction direction)
status: DIRECTION CAPTURED — not being built yet
reference: Aiwa NSX-V20 style component hi-fi stack
---

# Monitor — the Stereo Stack

Visual/interaction direction for the Monitor tile, captured 2026-07-31.
**Not to be built yet** — operator: *"Don't worry about building the whole
graphical user interface right now, but this is what it's going to end up
looking like."* Recorded so nothing gets built that contradicts it.

Reference: a 90s Aiwa-style **component stereo stack** — CD deck on top,
tuner/amplifier in the middle, dual cassette deck at the bottom. Retro
skeuomorphic throwback, rendered at a slight 3/4 angle, fully touch-driven.

## The three decks

### Top deck — CD player = MODELS

- Tap the **CD** button and the **disc tray slides out**, seen at the same
  3/4 angle as the reference photo.
- The tray holds a **rotating carousel** — you spin through your models and
  swap them by touch. (The reference unit is a **CD3** 3-disc changer, which
  is exactly the right metaphor: several models loaded, one engaged.)
- Close the tray to commit.

**Maps to:** the Monitor's model library + the explicit **PLUG IN** action.
The disc you leave in the engaged position is `KEY_ACTIVE_MODEL`. Loading a
disc is *landing* an asset; closing the tray is *plugging it in*. Nothing
spins up on its own — same law, new skin.

### Middle deck — tuner / amplifier = RUNTIME PARAMETERS

- Touch the middle panel and it **expands**.
- Controls for: **temperature**, **verbosity**, **core count** in use, and a
  **dial to scroll through runtime options**. More dropdowns to come.
- The **FM / AM band button swaps runtimes** — band = which runtime is live.
- The existing LCD/VU area is the natural home for live status (the
  green-light readout, tokens/sec, memory draw).

**Maps to:** the Router's engaged config + its parameters. The band selector
is the fuse being swapped; the dials are the config's tunables.

### Bottom deck — dual cassette = RUNTIME FILES

- **Runtimes load as files, into the cassette wells.** "Files run in the
  cassettes."
- Dual well = two runtimes loaded at once (one playing, one on deck) — which
  lines up exactly with the canon's `RUNNING` vs `SLEEPING`/"on the deck"
  states, no new concepts needed.

**Maps to:** `RuntimeDef` + the uploadable runtime binary. A cassette *is* a
runtime definition file: binary name, port, health path, args template.

## Why this fits the existing architecture

The metaphor is not a reskin — it's a near-exact match for the data model
that already exists:

| Stereo part | Canon concept | Existing code |
|---|---|---|
| Disc in the tray | landed model asset | Monitor model library scan |
| Disc left engaged | the plugged-in model | `KEY_ACTIVE_MODEL` (pin-only) |
| Cassette in a well | a runtime definition | `RuntimeDef` |
| Two wells | RUNNING + SLEEPING | `ConfigStatus` |
| FM/AM band switch | swap the engaged runtime | Router fuse flip |
| Tuner dials | runtime parameters | *partially missing — see below* |
| Power / green lights | greenLight checklist | `greenLight()` |

Nothing here asks the app to auto-start anything. Inserting media ≠ playing
it; you still press the button. **"Daemons stay dumb, the user is the
loader" survives the reskin intact** — arguably it's a better expression of
it, because a stereo is the most literal possible "user is the loader."

## The one gap this exposes

**Runtime parameters are not first-class yet.** `temperature` exists only as
a hardcoded value inside `NpuClient`'s request body. **Verbosity and core
count do not exist anywhere.** For the tuner deck to be real, these need to
live on the runtime config — either as fields on `RuntimeDef` or as
substitutions in `argsTemplate` (alongside the existing `{model}`/`{port}`).

That is worth knowing *before* the launcher is made runtime-agnostic
(EXECUTIONS P1.3), so the parameter path gets designed in once rather than
retrofitted after.

## Not yet decided

Whether the stereo stack is **the Monitor tile only**, or becomes the shell
for the whole app. The three decks cover models + runtimes + parameters,
which in the seven-tile canon currently spans Monitor, Settings and Router.
Operator call — do not assume either way.
