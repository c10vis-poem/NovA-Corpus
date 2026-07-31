---
title: Monitor — Arcade Cabinet UI (visual + interaction direction)
status: DIRECTION CAPTURED — not being built yet
scope: the Monitor / console tile only (operator-confirmed 2026-07-31)
reference: upright arcade cabinet + CRT oscilloscope screen
---

# Monitor — the Arcade Cabinet

Visual/interaction direction for the **Monitor / console tile**, captured
2026-07-31. **Not to be built yet** — same standing instruction as the
Router spec: get it functioning first, the GUI redesign is its own session.

Reference: a **neon upright arcade cabinet** (lit marquee header, CRT screen
behind glass, instruction placard, control deck with joysticks and coloured
buttons, coin door below), with the screen itself reading like a **CRT
oscilloscope** — green graticule, glowing waveform traces, hardware bezel.
"Maybe a little more futuristic" than the raw retro reference.

Companion to [[ROUTER-STEREO-STACK-SPEC]]. Two different pieces of retro
hardware for two different tiles: **Router = component stereo stack**
(load media, tune it, switch it on), **Monitor = arcade cabinet** (walk up,
look at the screen, read the placard, hit a button).

## Why this fits what Monitor already is

Canon calls the Monitor *"where you get to test drive or you can window
shop"* — the library and the checkpoint. An arcade cabinet is precisely a
walk-up-and-try-it surface, which is why the metaphor lands without
straining anything.

It also matches what is **already in the code**: `MonitorPane` already draws
an `OscilloscopeBackground`, and the existing visual canon already assigned
Monitor the oscilloscope treatment (graticule + waveform traces). This
reference extends that rather than replacing it — the oscilloscope becomes
the cabinet's *screen*, and the cabinet is the furniture around it.

## Anatomy

| Cabinet part | Carries |
|---|---|
| **Lit marquee** (top) | the `MONITOR / console` title; the tile's identity |
| **CRT screen** | the main display — browser, model library, green-light readout |
| **Instruction placard** (under glass) | the "what's missing / what to do next" copy |
| **Control deck** (joysticks + buttons) | tabs and toggles — import / export / file access |
| **Corner terminal tile** | shortcut that pops the screen out into terminal view |

## Interactions

### The screen

The main surface. This is where the **browser** lives (already mounted —
the Monitor is the app's main browser home per canon, with the Terminal
keeping only a shortcut). Also the model library and the green-light
readout.

### Pop-out for fine tuning

A **pop-out panel** for finer adjustment, called up when needed rather than
occupying the face permanently. Keeps the default view clean — the cabinet
reads as a screen, not a control panel, until you ask it for more.

### Terminal tile → full-screen terminal

A **terminal tile in the corner** of the screen. Tap it and **the whole
screen pops out into a terminal view**. This is the shortcut-to-Terminal
that canon already specifies ("a shortcut for the browser inside the
terminal, but the main browser inside the console" — the same relationship,
read from the other side). Terminal remains its own tile at 6:00 on the
home dock; this is an express lane, not a relocation.

### Tabs and toggles

Along the control deck: **import / export / file access**, and whatever
other appropriate toggles the pane needs. The physical joystick/button
cluster is the natural home for what is currently a row of plain controls.

## What already exists that this can build on

- `OscilloscopeBackground` — already rendered behind `MonitorPane`.
- `BrowserPane` — already mounted in Monitor behind a `BROWSER` button
  (2026-07-31), shared with the Terminal tile, accent-themed per host.
- The model library scan + `greenLight()` checklist rendering.

None of that needs to be thrown away to get to the cabinet; it is the
cabinet's contents.

## Boundaries

- Monitor stays the **read-only checkpoint**: holds no data, transfers no
  data, static checks with no side effects. The cabinet does not gain
  ignition — that lives in the Router (the stereo). Buttons here navigate
  and inspect; they do not energize a runtime.
- The seven-tile home and its geometry are unaffected.
