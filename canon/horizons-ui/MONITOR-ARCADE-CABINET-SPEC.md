---
title: Monitor — Arcade Cabinet GUI (LOCKED visual specification)
status: CANON — LOCKED visual specification. Build order deferred; design is not.
scope: the Monitor / console tile only (operator-confirmed 2026-07-31)
reference: upright arcade cabinet + CRT oscilloscope screen
---

# Monitor — the Arcade Cabinet

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

Visual/interaction direction for the **Monitor / console tile**, captured
2026-07-31. **Build order deferred** — get it functioning first; the GUI build is its own
session. That is sequencing only. The design below is locked.

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

### Pop-out tabs on the screen

The screen carries a set of **pop-out full-screen views, each one a tab**.
You are in the Monitor, you hit a tab, it takes over the screen, and you
come back to the console face. Confirmed set:

| Tab | Pops out to |
|---|---|
| **CONSOLE** | the default face — library, green lights, status |
| **TERMINAL** | full-screen terminal view |
| **BROWSER** | full-screen browser |

Terminal remains its own tile at 6:00 on the home dock and the browser's
home is still the Monitor — these are **express lanes, not relocations**.
This is the shortcut relationship canon already specifies ("a shortcut for
the browser inside the terminal, but the main browser inside the console"),
read from the Monitor's side.

**Status: BUILT (functionally).** `MonitorPane` now carries a
`MonitorPopout` enum — Console / Terminal / Browser — with both tabs in the
console header and ← to return. Adding a future view is one enum entry. The
cabinet styling is still to come; the behavior is in.

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
