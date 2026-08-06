---
title: UX Rules — cross-tile behavior the whole app obeys
status: CANON — operator-dictated 2026-08-06, applies to every tile
scope: rules that don't belong to any single tile because they cut across all of them
---

# UX Rules

> **What this is.** The workbench-wide UX rules that don't belong to any
> single tile spec because they apply to every one of them: no typing
> outside Terminal/browser, long-press-for-help, zoom, inset-cropping. If a
> tile spec ever contradicts one of these, this doc wins.
>
> **Guiding principle — the app is a workbench, not a config editor.** The
> operator's standing complaint against previous builds is that the app got
> over-complicated and expected the user to type technical syntax. That
> expectation is banned. The whole surface is buttons, lists, and pickers.
> Typing is a specialist activity, penned into the two rooms that are for
> specialists.
>
> **Verification rule.** Any UI element that requires the user to type
> outside Terminal or the browser is a Rule 1 violation, regardless of what
> it does. Fix the UI, not the rule.

---

## 1 · No typing outside Terminal or the browser

> **Operator (2026-08-06):** *"Nothing in settings or archives or router
> should have any typing involved. You should be pushing buttons, selecting
> from a list of choices to fine-tune. All those choices you can access [by
> typing only in] the browser, the monitor, or the terminal."*

**Rule.** Free-text entry is only permitted in:

- **Terminal** — the shell, the parameter forge, the AI-drafted command
  editor
- **The browser** — Monitor's Chromium address bar and web forms; the
  Terminal-hosted browser shortcut

**Everywhere else — Settings, Archives, Router, Chat controls, Monitor
faceplate, Horizons — is 100% picker/button-driven.** Loading a model,
choosing a runtime, tuning a parameter, picking a provider, selecting a
voice — all pickers, dropdowns, dials, cassette slots, disc taps. Never a
text box asking the user to know a magic string.

**Concrete implications:**

- `RuntimeDef` is chosen from a menu of *landed* runtimes, not typed.
- The Router's fine-tune popup (`Model_ / Engine_ / Runtime_ / Config._`)
  is `(select)` on every row — no keyboard.
- Provider picker is a chip row / dropdown, not a name-your-provider text
  field.
- Hardware target (`npu` / `hybrid` / `gpu` / `cpu`) is a segmented
  control.
- The verbosity slider in Settings actually **reads and writes** the
  packet — not a decorative widget above a dead text field.

Chat is a mixed case: the chat *composer* is a text box (obviously —
that's what a chat is), but Chat's **controls and configuration** are
pickers, not a settings text form.

## 2 · Long-press → plain-language help popup

> **Operator (2026-08-06):** *"There should be like long-press drop-down
> menus or a little pop-up windows that you can tap on and get a description
> of how to use what you're trying to configure."*

**Rule.** Every non-trivial control anywhere in the app responds to
**long-press** by surfacing a **plain-language description** of what it
does, what it affects, and how to use it. Independent of the full user
manual — the help is right there under the finger.

**Applies to:** every dial on the Router tuner deck, every picker row in
the fine-tune popup, every toggle in Settings, every button on the Monitor
control deck, every cassette slot, every provider chip. If it changes
behaviour, it has help.

**Wording rule.** Written for a user who has never seen this control
before — plain English, no assumed jargon, one sentence of *what it does*
and one sentence of *what happens if you touch it*. Not a technical
reference; a hover-tip.

**Companion to the live manual** (see [[TERMINAL-SPEC]] §Live user
manual) — the manual is the tour; long-press is the definition.

## 3 · Zoom on Home and Monitor (with Floating Tile fallback)

> **Operator (2026-08-06):** *"The entire app should have a zoom function
> on the home screen and the monitor. If that's too difficult to do,
> perhaps utilizing the device assistant to have a zoom press-to-zoom
> function in the floating tile — that would probably be an easy way to do
> it."*

**Rule.**

- **Primary:** **pinch-to-zoom** on the Home screen and Monitor face.
  Compose gesture, matrix / two-finger scale.
- **Fallback (allowed):** if pinch is prohibitive on a given canvas (the
  Compose home grid, the Monitor CRT), the same behaviour is reachable via
  a **press-to-zoom control on the Floating Live Tile** — the Live Tile
  toggles the active room to a scaled view.

Zoom state is per-room. Zooming Home doesn't zoom Monitor, and vice versa.

The other five rooms (Chat, Settings, Terminal, Archives, Horizons) are
**not required** to support zoom — those are text/list surfaces where the
system font scale already handles readability.

## 4 · Inset cropping — every room except Home

> **Operator (2026-08-06):** *"Everything besides the home screen needs to
> be cropped to allow space for the notifications and gestures bars."*

**Rule.** Only the **Home screen** is allowed to draw edge-to-edge under
system UI. Every other room applies `WindowInsets.systemBars` padding so
content clears the notification bar (top) and gesture navigation pill
(bottom).

**Concretely:**

- `MainActivity` / `HorizonsApplication`: keep
  `WindowCompat.setDecorFitsSystemWindows(window, false)` for the
  edge-to-edge Home look, but every non-Home Composable applies
  `.systemBarsPadding()` or an equivalent `WindowInsets` modifier at the
  room-root level.
- The Router's stereo stack, the Monitor's cabinet, the Terminal's console,
  Settings, Archives, Chat, Horizons — all inset-safe.
- The Floating Live Tile ignores insets by design (it's an overlay).

This closes the on-device bug flagged in
[[../STATE-OF-EXISTENCE]] (top/bottom content clipped by system UI).

## 5 · Every tile has a pathway to the Router

> **Operator (2026-08-06):** *"All six tiles should have a pathway to the
> router."*

**Rule.** Every one of the six clock-face tiles has a first-class push
path to the Router — not just the subset drawn in older authority
diagrams. See [[ROUTER-STEREO-STACK-SPEC]] §Cross-tile pathways for the
per-tile behaviour.

## 6 · Failures surface, they don't crash

The three failure faces stay distinct (**GOAT** for handshake / bounce /
fuse-blow, **ASCII 404 CAT** for browser-scoped connection failure inside
the Monitor, **CHONK** for idle timeout). None of them replace an
exception with silence — they replace an *app crash* with a **visible,
recoverable banner**. The user always sees the failure.

**CHONK timeout — 2 minutes** (operator 2026-08-06). Older references to
"3–5 min" in [[HOME-REDESIGN-SPEC]] and [[../aesop/PARAMETER-PACKET]] are
superseded.

---

## Status ledger

- ✅ Rules 1–5 dictated by operator 2026-08-06 in this session.
- ⬜ Rule 6 CHONK timeout — 2 min vs 3–5 min not resolved.
- ⬜ All rules are **canon in the spec**; enforcement against live code
  needs a pass. Rule 1 alone is likely to surface several existing
  violations (e.g., the dead verbosity slider, any manually-typed model
  path fields).

## Related

- [[ROUTER-STEREO-STACK-SPEC]] · [[MONITOR-ARCADE-CABINET-SPEC]] ·
  [[TERMINAL-SPEC]] · [[HOME-REDESIGN-SPEC]] · [[FEATURE-INVENTORY]]
