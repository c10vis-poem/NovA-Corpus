# CLAUDE.md — OBSIDIAN-Master_Wiki

## What this is

A migration of a personal Google Drive knowledge vault (`(MASTER_REPO).&WIKI.MD_VAULT`)
into this GitHub repo as a clean, Obsidian-compatible Markdown vault, plus a
JSONL chunk library for RAG retrieval over the large reference docs.

**Everything currently lives on branch `claude/drive-obsidian-migration-th115b`,
NOT `main`.** `main` is still empty — this branch has not been merged. If you
don't see content in the repo, check you're on the right branch.

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
