# MASTER_REPO_WIKI_VAULT — index

Obsidian vault for the Novus Agenti / Omni Claw / Horizons build.

## What happened to this repo

`main` was reset to an empty tree ("clean slate for vault sync") and the actual
content was left scattered across four unmerged mirror branches:

| Branch | Held |
|---|---|
| `docs/mirror-master-repo-vault` | 34 files — the data bank + `#HORIZONS-main` |
| `docs/mirror-build-chunk1` | 11 files — device STT/TTS |
| `docs/mirror-build-chunk2` | 13 files — AESOP, reasoning bank, Termux, agents |
| `docs/mirror-build-chunk3` | 26 files — QAIRT/GenieX, Unsloth, Docker, OpenClaude |

All four are now consolidated here as one tree (82 files), so the vault opens as
a single vault instead of requiring four checkouts.

## Layout

```
MASTER_REPO_WIKI_VAULT/
  #AESOP_HORIZONS-UI_Master/
    (AESOP) REPO.data_bank/      ← WHAT THE APP IS. Read this first.
      (1a)-Horizons.Ui-defined/    the conceptualization + spec corpus
      omni-claw-blueprint./
    (AESOP.]build/               ← HOW IT GETS BUILT. Toolchain + sources.
      ##DEVICE-STT&TTS_/           Moonshine / Kokoro / Sherpa / Silero
      ##REASONING-BANK_/  ##TERMUX_main/  ##AESOP/
      #QAIRT_main/                 QAIRT + GenieX (incl. PDFs)
      #UNSLOTH_MEROVINGIAN/  #LLAMA CPP NPU/  #HERMES_AGENT/  #AIDER_AGENT/
      #CLAUDE.CODE_ANDROID-CLI/  #OPEN-CLAUDE_ANDROID/  Docker/  Desktop theme/
    (BUILD.it)_JHA/              ← RUNNING STATE. SOTU, action plan, job log.
  #HORIZONS-main/                ← the app repo's own docs, mirrored
```

## Reading order

1. `(AESOP) REPO.data_bank/(1a)-Horizons.Ui-defined/4. Technical Specification The Four Rooms & Seven-Tile Modular Architecture.md`
2. `.../The Horizons Workflow From Storage to Switch.md` — Landing → Verification → Activation
3. `.../The Horizons Workbench A Guide to Your Modular Intelligence Engine.md`
4. `(BUILD.it)_JHA/SOTU-2026-07-27.md` — most recent state of the union
5. [[CRASH-ANALYSIS-2026-07-31]] — current boot-stability investigation
5. [[ROUTER-STEREO-STACK-SPEC]] — Router tile UI direction (stereo stack)

## The core law

> **Daemons stay dumb, the user is the loader.**
> The app must never auto-grab runtimes or files mid-flight.
> The pipeline is strictly linear: **Define → Validate → Execute.**

## Source-trust warning

Two documents in the data bank are **AI chat transcripts, not specifications**,
and both contain material the operator has explicitly repudiated:

- `Gemini oils up The Builder and challenges Claude to a duel...md` — the author
  **retracts its own central technical claim** partway through (that `geniex` can
  drive the NPU from a Termux shell — it cannot; SELinux blocks non-privileged
  shells from `/vendor/lib64`). Its `GenieX_*` C API is invented and does not
  exist. Treat as historical context only.
- `2. 2026-07-17.md` — the operator's own framing of most of this file is
  "a complete fucking snow job... it failed every single aspect but it made
  everything worse." The **architecture** dictated in it is canon; the **claims
  of implementation** in it are not.

Where these transcripts and the spec documents disagree, **the spec wins** — the
specs were written afterwards specifically to overrule them.

## Vector JSONL

`.jsonl` chunk files are **grep/retrieval only — never a first read.** The `.md`
is always the first read; the `.jsonl` exists so a session can pull one chunk on
demand without loading the corpus. Keep the pair side by side under the same
name when adding new large documents.
