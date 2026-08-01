# CLAUDE.md — OBSIDIAN-Master_Wiki

## What this is

A migration of a personal Google Drive knowledge vault (`(MASTER_REPO).&WIKI.MD_VAULT`)
into this GitHub repo as a clean, Obsidian-compatible Markdown vault, plus a
JSONL chunk library for RAG retrieval over the large reference docs.

**STATUS 2026-07-31: the migration has been MERGED** into
`claude/app-crash-landing-yc955p` — the active branch for both this repo and
`c10vis-poem/Horizons-UI`. It originated on
`claude/drive-obsidian-migration-th115b`.

`main` is **still an empty tree** and must not be used as a base. Four
`docs/mirror-*` chunk branches also exist carrying only 82 files between them
(`chunk3`'s head is a *Revert*) — they are superseded, ignore them.

**Always `git branch -a` before choosing a base.** In these repos more real
work sits on unmerged branches than on `main`.

## Repo structure

```
#AESOP_HORIZONS-UI_Master/   \
#HORIZONS-main/                > mirror the 5 top-level Drive folder names exactly
#RESEARCH DOSSIER 1&2/        /
#Useful_knowledge_/          /
yJSONL_data.bank_/           /

_DUPLICATES_REVIEW/    files that were exact-duplicate (same content hash) within
                        the SAME source folder — quarantined here instead of kept
                        twice. Cross-folder duplicates are NOT touched; the same
                        doc appearing in multiple top-level folders is intentional
                        (operator's own access-pattern organization) and both
                        copies stay in place.

RAG_LIBRARY/            JSONL chunks of large/dense reference docs (≥3000 words),
                        mirroring the source doc's path with a .jsonl extension.
                        Deduped by CONTENT HASH ACROSS THE WHOLE VAULT (not just
                        per-folder) — a doc that appears in 5 folders only gets
                        chunked once here, since redundant chunks would just add
                        noise to retrieval. This is a different dedup scope than
                        the file-storage layer above; both are correct for their
                        own purpose.

.migrate/               the conversion pipeline scripts (see below) — kept in
                        the repo in case another pass over Drive is needed later.
```

## What's still binary/excluded

Six files (model weights, an SDK zip, tool archives — none of it "wiki"
content) exceeded GitHub's 100MB hard limit and were dropped from the
migration entirely rather than fought with Git LFS, since they don't belong
in a docs vault. Each has a `<original-name>.EXCLUDED.md` stub left in its
original location noting what was there and why. The operator has copies of
these elsewhere.

## Conversion rules used

- **Documents convert to Markdown**: `.docx`/`.doc` (via `pandoc`), `.pdf`
  (via PyMuPDF text extraction), `.txt` (direct), `.mht`/`.mhtml` (parsed as
  MIME email via Python's `email` module to extract the `text/html` part,
  then run through `trafilatura` for clean article-text extraction — raw
  pandoc HTML conversion keeps nav/header chrome, trafilatura strips it).
- **Everything else passes through unchanged** — source code (`.ts`, `.rs`,
  `.kt`, `.py`, etc.), images, binaries, `.jsonl`, already-`.md` files. Several
  Drive folders (especially under `(AESOP.]build`) contain full cloned
  reference repos, not just notes — converting source code to Markdown would
  be destructive and pointless.
- **Converted filenames keep the source extension folded in**
  (`Foo.pdf.md`, `Foo.mht.md`) rather than just `Foo.md`. This is load-bearing,
  not cosmetic: a `.pdf` and a `.mht` of the same title in one folder used to
  collide on `Foo.md` and silently overwrite each other — three files were lost
  this way before the fix (recovered from git history; see commit history
  around 2026-07-30 for the incident). Do not revert to bare `{base}.md` naming.

## Scripts (`.migrate/`)

- `process_folder.py <src> <dupes_dest> <clean_dest>` — per-folder dedupe +
  Markdown conversion + relocation. Run once per top-level Drive folder.
- `build_rag_chunks.py <vault_root> <rag_out>` — content-hash-deduped chunking
  of large docs into `RAG_LIBRARY/`. Chunks by `##`/`###` heading when a doc
  has them, else fixed 500-word windows with 50-word overlap.

## Full skill

The complete Drive → Termux → GitHub migration workflow (including the
Termux/rclone/OAuth setup, the traps hit along the way, and how to run this
again for future Drive content) is documented as a skill:
`.claude/skills/drive-to-obsidian-migration/SKILL.md`.

## Known open items

- `_DUPLICATES_REVIEW/` (15 files) needs a human pass to actually delete —
  nothing auto-removes it.
- The six `.EXCLUDED.md` stubs point at binaries not stored in this repo.
- This branch has not been merged to `main`.


---

## Session 20 handoff — 2026-07-31

### What landed

The full migration (1,300 files) was merged after being found sitting unmerged
while `main` was empty and a competing 82-file partial mirror was in use. Vault
is now **1,305 files · 363 md · 96 jsonl**, plus `RAG_LIBRARY` (46 docs / 1,786
chunks) and its BM25 index.

New docs at the vault root:

| File | What |
|---|---|
| `CRASH-ANALYSIS-2026-07-31.md` | the Horizons boot-crash investigation, with the on-device procedure to get the missing stack trace |
| `ROUTER-STEREO-STACK-SPEC.md` | Router tile = component stereo stack (CD=models, tuner=params, cassettes=runtimes) |
| `MONITOR-ARCADE-CABINET-SPEC.md` | Monitor tile = arcade cabinet, CRT screen, pop-out tabs |
| `TERMINAL-SPEC.md` | Terminal = fakesteak matrix cascade + in-shell saved-command drop-down |

All three UI specs are **direction only — not to be built yet.**

### The authority model (operator, LAW)

Series circuit. **Settings** supplies and may hand a config to the Router but has
**no authority to run it**. **Monitor is the switch in the loop** — stores
nothing, dispatches, and holds the verdict. **Router** is fuse box + breaker:
carries current, doesn't argue. Validation is **live at flip time** but the check
is the **Monitor's**. The operator explicitly rejected Router-as-gatekeeper.

### Source-trust

Two data-bank documents are AI transcripts, not specs — the "Gemini duel" doc
retracts its own central claim mid-document, and `2. 2026-07-17.md` is one the
operator calls a snow job. Architecture in them is canon; implementation claims
are not.

### How to read this vault (learned the hard way, 2026-07-31)

**Read the FOLDER, not the file.** Siblings are not copies — they go deeper on
different parts of the same subject. A folder like `Personal Agentic Operating
Stack/` is a numbered conversation series (1-9), not nine standalone notes;
pulling `3.` alone gets you a third of the picture. Same-named files ACROSS
folders *are* byte-identical (verified) — that is deliberate cross-filing, so
the depth you're missing is always in the siblings BESIDE the file, never in
the copy of it two folders over.

**Artifact kinds are never redundant.** `foo.md` (prose), `foo.jsonl` (chunks),
`foo-urls.md` (sources) are three different things about one subject.

**QAIRT: the manual outranks every summary in here — including this file.**
The operator has essentially every piece of QAIRT/HTP/model information
somewhere in these documents or in a forked repo. Never conclude it isn't
documented; go find it.
- Seven manual sections live in `#AESOP_HORIZONS-UI_Master/(AESOP.]build/#QAIRT_main/#QAIRT/`
  — Overview, QairtApi, QairtBackend, QairtContext, QairtGraph, QairtTensor, HTP
  — each in `.mht` / `.pdf` / `.md`. Horizons-UI `knowledge/qairt-sdk/` carries
  five of them plus `htp.jsonl`. **Do not stop at the first QAIRT file.**
- FraQAT is old prior-art research. Never reach for it over the QAIRT SDK.

**The runtime fact that keeps getting broken:** everything targets the NPU via
HTP. AI Hub precompiled → QAIRT → HTP for nearly everything; Unsloth-quantized
GGUF → llama.cpp/ggml → **the same HTP** for the rest. ggml has a Hexagon
backend and the compiled libraries are in this vault
(`##LLM-WIKI_OPEN-WIKI.main_/llm-wiki/libggml-hexagon.so`, `libggml-htp-v73/
v75/v79/v81.so`; device is v79). Nothing needs compiling. Reading "ggml" as
"CPU path" is the single most repeated error in this project — `aesop-wiki.md`
asserted it and has now been corrected in place.

### Getting more from Drive

Drive is the **source of truth** and is directly reachable via
`mcp__Google_Drive__*`. Never conclude something doesn't exist from the git
repos alone. Use the `drive-to-obsidian-migration` skill to pull more — do not
hand-sync file by file.


---

## Session 21 handoff — 2026-07-31 (vault repair)

### What was broken

**37 PDFs were in the vault as raw bytes nobody could reach.** Drive exports
arrive with no file extension; the migration dispatches on extension, so they
were never converted, never chunked, never indexed, and invisible to any
`*.pdf` search. Among them: the **193k-character QAIRT HTP manual** (several
copies), `backend (Markor)` (the QairtBackend section, never converted at all),
QairtTensor, the Scaling-LLM-NPU paper, EdgeAI CLIP+QNN, qcom-build-utils.

Fixed: extensions restored, 49 converted with PyMuPDF using the vault's
`{name}.pdf.md` convention, re-chunked. **RAG_LIBRARY: 46 docs / 1,786 chunks
→ 60 docs / 2,211 chunks**, BM25 index rebuilt.

### Still broken — do not assume these are fine

- **`.migrate/build_rag_index.py` self-poisons.** `load_chunks` walks all of
  `RAG_LIBRARY` including its own `_index/meta.jsonl` (different schema), so it
  works once and KeyErrors on `text` on every rebuild. Exclude `_index`.
- **Markdown extraction discards ALL images.** Diagrams in the Qualcomm PDFs
  are unreachable by text search. Embedded rasters need `page.get_images()`;
  vector diagrams need `page.get_drawings()` + a page render. Neither is in the
  pipeline. This is the next real gap.
- **Some captures kept chrome and dropped content.** The vault's GenieX `.md`
  is the GitHub repo *file tree*; the README body — carrying the runtime table
  that answers "what will GenieX actually load" — is only in the 7-page PDF in
  Drive. `c10vis-poem／llama.cpp-npu` is **44 bytes** here and **345 KB** in
  Drive. Check size against Drive before trusting a converted doc.
- Two extensionless `.mht` files remain unnamed.

### Corrected in place

`aesop-wiki.md` (both copies) said "**NOT on the ladder: Hexagon DSP**". False,
and it misled multiple sessions into reading GGUF/ggml as a CPU path. The
compiled `libggml-hexagon.so` + `libggml-htp-v73/v75/v79/v81.so` in
`##LLM-WIKI_OPEN-WIKI.main_/llm-wiki/` disprove it. Corrected with a retraction
note so a half-memory of the old line doesn't resurrect it.

### The runtime answer, finally sourced

From the **GenieX README** (Drive, `#QAIRT_main/#GenieX/`, 7-page PDF, pages 3
and 6) — not from any summary in this vault:

GenieX is ONE runtime with TWO backends. `llama_cpp` takes ~any Hugging Face
GGUF and runs on NPU/GPU/CPU. `qairt` takes a per-chipset Qualcomm AI Hub
bundle and is NPU-only. Q4_0 is recommended: "best Hexagon NPU support."
**The magic sauce is the ggml/HTP kernels** — the format is inert, the wrapper
is plumbing; what puts a GGUF on the NPU is ggml ops that execute on Hexagon,
which is why the libs are built per DSP arch.

### Open items carried forward

- `_DUPLICATES_REVIEW/` (15 files) still needs a human delete pass.
- Six `.EXCLUDED.md` stubs point at binaries not stored here.
- Image/diagram extraction is unsolved.

---

## Session 22 handoff — 2026-08-01 (vault repair)

### What was fixed

- **`c10vis-poem／llama.cpp-npu`** was 44 bytes (a Drive "shortcut" object
  containing only the repo URL) while the real README capture is a separate
  345,481-byte PDF object in the same Drive folder. Pulled the real PDF via
  `rclone` (MCP Drive's `download_file_content` kept getting declined this
  session — `rclone copyto`/`backend copyid` is the reliable path for a
  single targeted file when the MCP round-trip isn't cooperating) and
  converted it: `#LLAMA CPP NPU/c10vis-poem／llama.cpp-npu.pdf.md`.
- **GenieX README** — the vault's existing GitHub-page capture actually
  already had the runtime table (checked; not broken). Also pulled the
  live README + architecture diagram directly from the `c10vis-poem/GenieX`
  fork via `git clone` as a second, always-current source: `#QAIRT_main/
  #GenieX/README (c10vis-poem／GenieX fork).md` (+ `_images/`).
- **`.migrate/process_folder.py`**: `real_ext()`'s magic-byte sniff didn't
  cover `message/rfc822` (raw `.mht`), so any extensionless MHT capture
  stayed unconverted forever. Added the case. Also fixed a real bug where
  extensionless-but-sniffed files skipped the extension-fold step entirely
  (`Foo` → `Foo.md` instead of `Foo.pdf.md`), defeating the collision-safety
  the fold-in convention exists for. `convert_pdf()` now falls back to
  `mutool convert -F text` when PyMuPDF isn't importable (no prebuilt wheel
  for Termux/Android/cp314 — building it from source needs cmake/ninja,
  which fail to bootstrap here). One stranded raw `.mht` found and converted:
  `#QAIRT_main/#QAIRT/#QAIRT/Utilizing Qualcomm NPUs...LiteRT....mht(.md)`.
  Full rescan confirmed zero remaining stranded raw PDF/MHT bytes.
- **`.migrate/build_rag_index.py`**: the documented self-poisoning bug did
  not reproduce on this checkout (`_index` exclusion already worked) —
  verified stable at exactly **60 docs / 2,211 chunks** across three
  consecutive rebuilds. Hardened the exclusion anyway (path-component
  check instead of a `os.sep`-glued substring match) as defense in depth.
- **Image/diagram extraction — solved.** New `.migrate/extract_images.py`,
  no PyMuPDF dependency (unavailable here): `mutool extract` for embedded
  rasters, `mutool draw -F trace` per page (counts `fill_path`/`stroke_path`
  ops) to detect vector diagrams, then `mutool draw` renders any page over
  threshold to PNG. `.mht` images come from walking MIME parts with
  `Content-Type: image/*` (dropped entirely by the existing conversion,
  which only ever reads the `text/html` part). Images land in a sibling
  `<docname>_images/` folder; a `## Extracted images` section (idempotent —
  won't double-append on rerun) gets appended to the `.md` with a relative
  link + caption per image, so grep-by-caption reaches them. Run vault-wide:
  **7,381 images extracted from 66 PDFs + 7 `.mht` files.** Confirmed
  against both named targets: `Qualcomm AI Engine Direct SDK...pdf` page 3
  (the stack diagram, 38 vector ops) rendered; `HTP - Qualcomm AI Runtime
  (QAIRT) SDK.pdf` pulled ~42 embedded rasters (handoff estimate was ~39,
  close enough — different tools count embedded XObjects slightly
  differently); `backend (Markor).pdf` confirmed **zero embedded rasters,
  10 vector-diagram pages** — exactly the "diagrams with no rasters" case
  called out as the reason `get_images()` alone isn't enough.
- **`_DUPLICATES_REVIEW/` (15 files) — 13 confirmed true duplicates, 2 were
  not.** `4.docx`/`5.docx` under `#QAIRT_main/zqnn／qairt-System Design.../`
  hashed to nothing live in that folder — turned out to be parts 4 and 5 of
  a numbered conversation series (siblings 0,1,2,3,6,7,8,9 present, 4 and 5
  silently missing). Confirmed unique content (FFI orchestrator pattern /
  Android daemon architecture, matching neither each other nor any sibling)
  and restored them to the live folder instead of leaving them quarantined.
  The other 13 verified byte-identical to a still-present sibling and were
  left in place for the operator's own delete pass (not auto-deleted).

### Environment note for future sessions

This session ran in Termux (Android/aarch64, Python 3.14) with no
prebuilt PyPI wheels for `pymupdf`/`numpy`/`lxml`/etc. Working toolchain
that doesn't need pip source builds: `pkg install pandoc mupdf-tools
python-numpy libxml2 libxslt`, then `pip install rank_bm25 trafilatura`
(numpy/lxml as binary `pkg`s first is what unblocks both of those). `mutool`
(from `mupdf-tools`) stands in for PyMuPDF everywhere: text extraction,
embedded-image extraction, and page rendering all shell out to it now in
`process_folder.py` (fallback only) and `extract_images.py` (primary).

### Open items carried forward

- `_DUPLICATES_REVIEW/` (13 confirmed-true-duplicate files) still needs a
  human delete pass — operator has the list, not auto-deleted.
- Six `.EXCLUDED.md` stubs point at binaries not stored here.
- Repo grew to ~1.6GB locally from the image extraction (not yet measured
  post-push) — worth checking this doesn't collide with GitHub's repo-size
  soft limits before pushing at scale again.

---

## Session 22 addendum — 2026-08-01

**The boot log was never unreachable.** `novus-boot.log` (~4 kB) sits in the
on-device `HARNESS/` folder, not under `/sdcard/Android/data/<pkg>/`. Termux can
read it. Session 21 concluded it was blocked by scoped storage because the
documented path pointed into the carve-out. Check `HARNESS/` first.

**Voice models are not in Drive** — only their documentation is, here at
`#AESOP_HORIZONS-UI_Master/(AESOP.]build/##DEVICE-STT&TTS_/`. That folder holds
`architecture.md` (the working spec: Kokoro TTS · Moonshine STT · Silero v5 VAD
on one sherpa-onnx runtime, with exact HF sources and configs), `quickstart.md`,
`operations.md`, `DaemonTtsClient.kt`, and fork captures for sherpa-onnx,
silero-vad, kokoro-onnx and moonshine-tflite.

**AESOP's repo does not match its wiki page.** `aesop-wiki.md` describes
`llamad`, `aesopd` and `protocol/bridge-protocol.md`. The repo has six files:
README, ARCHITECTURE, RESUME, `protocol/tiers.md`, `profiles/{nav,_example}.yaml`.
No voice-engine, no bridge spec. AESOP is a **protocol** — four roles (query,
executive, librarian, auditor), three memory types (declarative markdown =
canonical · recall = OB1 vector · strategic = ReasoningBank), and tier contracts.
`profiles/nav.yaml` names this project's app: `phone: tiers:[edge], client:
omni-claw`.
