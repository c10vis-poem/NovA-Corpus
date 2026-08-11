# Phase 1 Audit — Vault Duplicate & Version Report

Snapshot of the Drive-side duplicate/version audit for the OBSIDIAN-Master_Wiki
vault reorganization, committed early so the work survives a session interruption.

- `vault-report.html` — the interactive report (open directly in a browser)
- `REPORT.md` — same data as plain markdown
- `data.json` — structured data behind the report
- `analyze.py` / `dossier_diff.py` — the scripts that produced them
- `*.tsv` — raw Drive file listings the analysis was built from (fileId, title, size, mimeType, path)

## State as of this commit

- ~850 files audited (Drive's `Novus-Agenti_HomeGrid` folder excluded entirely — separate project, hands off)
- 410 files identified as exact byte-identical duplicates, safe to collapse to one copy each
- 8 genuine version-conflict groups resolved (see REPORT.md "Version conflicts" section):
  resolved by explicit instruction, by timestamp evidence, or folded into the dossier-merge plan below
- Two research-dossier pairs need a **merge**, not a pick-one-delete-the-other:
  - `PRIMARY RESEARCH DOSSIER (a)` vs `(b)` — 55 files match; `(a)` has a unique nested
    `#QAIRT/#QAIRT/` folder, `(b)` has a unique `ANDROID APK_ RESEARCH DOCS` folder
  - `SECONDARY RESEARCH DOSSIER` vs `PSECONDARY RESEARCH DOSSIER` — PSECONDARY has 5 dated
    architecture-review docs + 9 capture files SECONDARY lacks; SECONDARY has 2 files PSECONDARY lacks

## Not yet done

- Actual mirror-copy of Drive content into a reorganized structure
- Folder-by-folder subsection breakdown (in progress, being discussed live)
- Download of vault content into this repo and push of real vault files

This audit folder is scaffolding for the reorg, not the final vault structure —
expect it to be removed once the real content lands.
