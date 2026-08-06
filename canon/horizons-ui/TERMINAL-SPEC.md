---
title: Terminal — Matrix Cascade GUI (LOCKED visual specification)
status: CANON — LOCKED visual specification. Build order deferred; design is not.
scope: the Terminal tile only (operator-confirmed 2026-07-31)
reference: c10vis-poem/fakesteak (cascading matrix background)
---

# Terminal — Matrix Cascade

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

Visual/interaction direction for the **Terminal tile**, captured 2026-07-31.
**Build order deferred** — sequencing only. The design below is locked.

Third of the three tile treatments captured this session:

| Tile | Hardware metaphor | Job |
|---|---|---|
| **Router** | component stereo stack | load, tune, switch on — ignition |
| **Monitor** | arcade cabinet | walk up, look, inspect — read-only |
| **Terminal** | matrix-cascade console | the mod garage — define, script, save |

## Visual

- Background: the **cascading matrix** from **`c10vis-poem/fakesteak`** —
  the operator's own repo, per the standing preference for using own forked
  assets wherever possible (see [[../MASTER-BUILD-BLUEPRINT]] §Your-fork-first).
- **Top half of the screen is the black terminal monitor**, with the
  cascade **flowing behind it** — visible along the **top edges and
  underneath**, so the console reads as a panel floating over live rain
  rather than a flat background.
- The **tile underneath the monitor is transparent**, so the cascade shows
  through there too.

Operator: *"that's going to be pretty simple."* This is a layering job, not
a new rendering system.

### Oscilloscope-waveform panel treatment (operator 2026-08-06 reference image)

The black terminal monitor is **not a flat text field.** The console
surface reads like a **CRT oscilloscope**: green graticule, a **glowing
warm-amber waveform trace** across the middle, hardware bezel around the
edges. The waveform is live — it responds to command activity (idle = flat
line + graticule, run = active trace), audio input if the mic is engaged,
and streams while the LLM emits tokens.

Speakers/DSP nubs render at the corners of the bezel per the reference —
purely visual, no interaction. Underneath the CRT sits the input row and
the control deck.

This does **not** replace the matrix cascade — the cascade flows behind
the CRT panel the same as before. The CRT is a *panel on top of* the rain,
not a wallpaper swap.

**Boundary with Router.** The Router's tuner-deck LCD already carries live
tokens/sec + memory-draw readout. The Terminal oscilloscope carries
**activity, not telemetry** — it visualizes that *something is happening*,
not the same metrics. Where they overlap (both are green screens with
readouts), Router = numbers, Terminal = wave.

## Interaction

The Terminal is the **mod garage** — where a runtime gets *defined* as
parameters, where scripts get written and stored, where models are
configured and fine-tuned, and where a **Termux-backed agent** actually
executes shell work. **Earlier language limiting Terminal to "defines
only" is superseded (operator 2026-08-06)** — Terminal defines *and*
executes; ignition of a *plated Router runtime* still lives at the Router.

### Baseline

- **Different prompts**, selectable.
- A **drop-down menu for saved bash commands, prompts and scripts** —
  quick access, so you can **retrieve them from the Archives without having
  to exit out** of the terminal. No round-trip through another tile to reuse
  a saved command.

### Configure & fine-tune models from Terminal (operator 2026-08-06)

> *"Build document was slightly incorrect when it defined the terminal.
> Terminal also has an ability to configure models, fine-tune parameters,
> of course push to router. There's going to be menus in the terminal panel
> where you can select preloaded scripts and runtime configurations etc."*

- **Preloaded picker menus** for scripts, runtime configurations, and
  parameter presets — same picker discipline as the rest of the workbench:
  select from a list, don't hand-type syntax (see [[UX-RULES]]).
- **Push-to-Router** action from any prepared config — the Router receives
  it as a plated packet.
- **View Archives contents** without leaving Terminal.
- **Move files from Settings vault → Archives** to free room, without
  leaving Terminal. Same store, second entry point.

### Termux access (operator 2026-08-06)

> *"I'm not sure why the terminal didn't have access to Termux but that
> needs to happen."*

Terminal has direct **Termux** access. Concretely: Termux's
`RUN_COMMAND_SERVICE` intent interface (same pattern
[[../pending-corpora/transcripts/gemini-architecture-thread-2026-08-04|c10vis-llm-hub]]
demonstrates) hands drafted commands into Termux for execution, with
stdout/stderr streamed back into the Terminal panel live. This closes the
"no inbound listener / Termux backend absent" gap flagged in
[[../STATE-OF-EXISTENCE]].

**Critical dependency (operator 2026-08-06).** The Qwen 3.5-0.8B QAIRT
executions model (see [[../MASTER-BUILD-BLUEPRINT]] §9.2) ships as a
**GitHub release-assets JSON**, and the **only tool on the device that
can unpack and load it is Termux**. That promotes Termux access from
"nice-to-have" to a **hard blocking dependency** for anything the Router
tries to plate on the executions-model side. Without functional Termux
integration, the executions model cannot be loaded at all.

### On-device Terminal agent — describe → draft → confirm → run → auto-fix

> **Operator (2026-08-06):** *"The user should not have to type out a full
> technical syntax runtime — that's silly. As far as loading models we
> shouldn't have to type anything in at all unless it's in the terminal.
> You should be pushing buttons, selecting from a list of choices."*

Reference implementation: the `c10vis-poem/c10vis-llm-hub` **AI Agent
Termux demo** — the pattern is proven and shipping.

1. **Describe** — user says what they want (natural language, or a menu
   pick).
2. **Agent drafts** — the on-device model writes the shell/CLI command.
   User does **not** type it.
3. **Interactive pre-execution editing** — the draft lands in an editable
   field. User inspects and tweaks before running.
4. **Live dark terminal container** — command runs, `stdout`/`stderr` streams
   into the monospace panel as it happens (not a post-hoc log dump).
5. **AI error auto-correction loop** — on failure (permission denied,
   syntax error, missing binary), the error logs feed back into the LLM
   automatically; it drafts a fix command; user confirms; run.

The Terminal-agent execution mode is also selectable at the Router's Load
cassette as a first-class runtime target — see [[ROUTER-STEREO-STACK-SPEC]].

### Port the Terminal agent over to the Router (operator 2026-08-06)

> *"If the router is not currently loading or running a model you can port
> over to the router and become the on-device agent that way — the full
> voice stack."*

When the Router is idle (no plated model running), the Terminal-hosted
agent can **port itself over to the Router** and become the on-device
agent, inheriting the full voice stack (VAD / STT / TTS) that the Router
mediates. This is a soft handoff, not a resource fight — the Terminal
agent stays available in Terminal too; the Router just adopts it as the
active execution target while it's idle.

### Live user manual — accessible from Terminal (operator 2026-08-06)

> *"The user manual needs to be live. There should be pop-up menus you can
> tap on and get a description of how to use what you're trying to configure.
> It's scripted to guide someone through the user manual if needed."*

The user manual lives **inside Terminal**, chaptered, and is scripted so
an on-device help-agent walks the user through it live. Not a static
rendered doc — the manual is a series of chapters the agent can navigate
on demand ("how do I load a model?" → agent opens the relevant chapter,
walks through it, offers to run the pickers with the user).

**Canonical chapter TOC (operator 2026-08-06):**

- **Ch. 0 — README / intro.** What Novus Agenti is. Capabilities overview.
- **Ch. 1 — Home screen.** Clock-face wheel and each position's function;
  Router hub; chat bar (hold-to-mini-UI); status nodes; banner; Floating
  Live Tile; GOAT easter egg; CHONK screensaver.
- **Ch. 2 — Each tile in detail.** Monitor (12) · Chat (2) · Settings (4) ·
  Terminal (6) · Archives (8) · Horizons (10) · Router (centre) — layout,
  functions, every control.
- **Ch. 3 — Launching.** Every pathway to fire something off.
- **Ch. 4 — Pushing from Chat.** How a prompt/task moves from Chat into
  the Router.
- **Ch. 5 — Configuring & fine-tuning from Router.** The stereo-stack
  controls end-to-end (CD deck / tuner deck / cassette deck).
- **Ch. 6 — Configuring from Terminal.** Parameter-forging side.
- **Ch. 7 — Modifying from Terminal.** Hacking on existing configs and
  runtimes.
- **Ch. 8 — How the Monitor works.** greenLight's four checks, the
  browser, pop-out tabs (CONSOLE / TERMINAL / BROWSER).
- **Ch. 9 — Web browser.** Using the Monitor's Chromium, download-to-vault.
- **Ch. 10 — Setting up failback.** Cascade (NPU → GPU → CPU → cloud),
  overflow-bounce behaviour (see [[ROUTER-STEREO-STACK-SPEC]] §Overflow).
- **Ch. 11 — Choosing different runtimes.** `llama_cpp` vs `qairt`, cloud
  providers, terminal agent.
- **Ch. 12 — Optimising for your device.** Device-specific tuning.
- **Ch. N — Packaging & optimised stacks.** Tiered packages by hardware
  (free plug-and-play tier, premium tier for the good stuff); live links
  from the manual out to your own repos with pre-optimised stacks per
  hardware tier. Ties to the commercial-tier picker in
  [[../MASTER-BUILD-BLUEPRINT]].

**Also — long-press for help.** Any control in Terminal (and everywhere
else in the app) surfaces a plain-language description on long-press,
independently of whether the user opens the full manual. Cross-tile rule
lives in [[UX-RULES]].

### Provider picker (Terminal + Monitor browser)

Standard CLI-agent-style first-run picker for **where inference runs**:
local on-device model, or a named cloud provider (OpenAI · Anthropic ·
OpenRouter · SambaNova · custom endpoint). Extensible list, not the old
three-hardcoded shortlist. Reachable from **Terminal itself** and from the
**Monitor's sandboxed web browser**. See
[[../MASTER-BUILD-BLUEPRINT]] §Provider picker.

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
