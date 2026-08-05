---
title: Terminal — UI direction (matrix cascade + quick-access prompts)
status: DIRECTION CAPTURED — not being built yet
scope: the Terminal tile only (operator-confirmed 2026-07-31)
reference: c10vis-poem/fakesteak (cascading matrix background)
---

# Terminal — Matrix Cascade

Visual/interaction direction for the **Terminal tile**, captured 2026-07-31.
**Not to be built yet** — same standing instruction as the Router and
Monitor specs.

Third of the three tile treatments captured this session:

| Tile | Hardware metaphor | Job |
|---|---|---|
| **Router** | component stereo stack | load, tune, switch on — ignition |
| **Monitor** | arcade cabinet | walk up, look, inspect — read-only |
| **Terminal** | matrix-cascade console | the mod garage — define, script, save |

## Visual

- Background: the **cascading matrix** from **`c10vis-poem/fakesteak`** —
  the operator's own repo, per the standing preference for using own forked
  assets wherever possible.
- **Top half of the screen is the black terminal monitor**, with the
  cascade **flowing behind it** — visible along the **top edges and
  underneath**, so the console reads as a panel floating over live rain
  rather than a flat background.
- The **tile underneath the monitor is transparent**, so the cascade shows
  through there too.

Operator: *"that's going to be pretty simple."* This is a layering job, not
a new rendering system.

## Interaction

Deliberately minimal. The Terminal is the **mod garage** — where a runtime
gets *defined* as parameters and where scripts get written and stored.
Nothing executes a daemon here.

- **Different prompts**, selectable.
- A **drop-down menu for saved bash commands, prompts and scripts** —
  quick access, so you can **retrieve them from the Archives without having
  to exit out** of the terminal. That last clause is the actual requirement:
  no round-trip through another tile to reuse a saved command.

## What already exists

More of this is built than the description implies:

- **`drawMatrixRain` already exists** in `TerminalPanel.kt` (rain columns +
  animated progress, `MatrixGreen = 0xFF00FF41`). The cascade is
  implemented; what changes is **layering** — currently it paints the whole
  pane flat, and the spec wants the black console floating over it with the
  rain visible at the top edges, underneath, and through the tile below.
- **`SavedCommandStore` is real and wired**: the shell saves commands
  (`TerminalPanel.kt:467`, `:815`), the Prompts tab lists and deletes them
  (`:708`, `:751`), and `ArtifactsPane` reads the same store (`:76`).
- **`ArchiveStore`** exists as the artifact file manager.

So the genuinely missing piece is small and specific: **an in-place
drop-down inside the shell view** that surfaces saved commands / prompts /
scripts and pulls from Archives *without leaving the shell*. Today reuse
means switching to the Prompts tab. That is the gap.

## Boundaries

- Terminal **defines**; it does not execute a runtime. Ignition stays in
  the Router. (Operator, on isolating the hacking phase from the execution
  phase: *"if I was going to be trying to hack on it I wouldn't want to be
  using the terminal to try to break its own code."*)
- Terminal keeps a **shortcut to the browser**; the main browser lives in
  the Monitor. The Monitor in turn carries a corner **terminal tile** that
  pops out to a full terminal view — the same relationship from both sides.
- Terminal stays its own tile at 6:00 on the home dock.

## Related

- [[ROUTER-STEREO-STACK-SPEC]]
- [[MONITOR-ARCADE-CABINET-SPEC]]
- Vault reference: `(AESOP.]build/Desktop theme/c10vis-poem-fakesteak.pdf`
