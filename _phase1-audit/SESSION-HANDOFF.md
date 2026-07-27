# Session Handoff — Vault Reorg, AESOP folder in progress

## State of the vault (confirmed facts, not guesses)
- Drive vault intact, nothing lost. `Novus-Agenti_HomeGrid` is a separate project — hands off.
- Phase 1 dedup audit done: see `_phase1-audit/vault-report.html` / `REPORT.md`. 410 exact-duplicate
  files identified, 8 version conflicts resolved (see REPORT.md).
- PRIMARY RESEARCH DOSSIER (a)/(b) and SECONDARY/PSECONDARY need a **merge** (each side has unique
  content), not a pick-one-delete-the-other. Details in REPORT.md footer notes.
- GitHub repos confirmed real (all `c10vis-poem`, all forks except aesop/Novus-Agenti/
  OBSIDIAN-Master_Wiki/Horizon-s-home-grid which are original): `aesop`, `OB1`, `clovis-mem0-vingian`
  (Mem0 fork), `reasoning-bank`, `llm_wiki`, `openwiki`, `graphify`, `obsidian-skills`, `notebooklm-py`.
  All 9 cloned to `/workspace/<name>` this session (shallow, depth 1).
- `Horizon-s-home-grid` = the separate HomeGrid repo referenced earlier, distinct from Novus-Agenti.

## AESOP — naming, now correctly understood
- **AESOP** (current/real) = Agentic Executions Split Operations Protocol — split multi-device
  agent stack (query/executive/librarian/auditor roles, edge/personal/home/cloud tiers, three
  memory types: declarative/recall/strategic). Defined in `c10vis-poem/aesop`
  (README.md, ARCHITECTURE.md, RESUME.md, protocol/tiers.md, profiles/{_example,nav}.yaml).
- **AESOP_Full_Reference** (old) = "Android Edge-Pi System Operations Platform," a prior Termux
  voice-assistant implementation. Confirmed archived at Drive root in `zNO/V4-Archives/
  ZZ-OLD.BUILDS&REF.` and `aesop full reference Wiki` — NOT part of current AESOP, do not merge in.
- Naming chain per RESUME.md: AESOP (umbrella protocol) → Omni-Claw (device client = the
  Novus-Agenti Kotlin app) → Novus Agenti (the agent protocol underneath it).
- 4 files RESUME.md says were in progress (`protocol/roles.md`, `protocol/memory.md`,
  `protocol/audit.md`, `deploy/README.md`) were searched for exhaustively — not found anywhere
  in Drive. Likely genuinely lost (subagent work never pushed/saved). Flag to user if it resurfaces.

## AESOP folder structure — agreed, ready to build
- `AESOP repo/` — the 6 real repo files above, straight from GitHub
- `AESOP Defined/` — deep-dive conceptual docs, one of the ~4 core docs defining what AESOP is:
  `final-memory-layer-p2p-pipeline.md` (peer-to-peer pipeline = inference between models/devices,
  directly matches user's own definition of what AESOP covers). NOT a Components item.
- `Components/` — one subfolder per forked tool repo, each with that repo's real README:
  `OB1/`, `MemO/` (clovis-mem0-vingian + DUAL.AGENT.MEMORY.LAYER),
  `reasoning-bank/`, `LLM Wiki/`, `OpenWiki/`, `Graphify/`, `obsidian-skills/`, `notebooklm-py/`
- `AESOP Wiki/` — current-issues/troubleshooting docs (LangSmith 403s, Graphify Termux compile
  failures — found in "AESOP Vault setup, OPEN WIKI, GRAPHIFY NBLM" doc)

## Not yet done (next session should pick up here)
1. Actually populate the AESOP folder per the structure above (copy Drive files + repo READMEs in)
2. Work out subsections for the other 8 master folders individually, based on each folder's
   actual content — NOT a copy-paste of AESOP's repo/defined/components/wiki structure. User
   explicitly said this pattern was never meant to apply universally. #AGENTS already got its
   own bespoke breakdown (Harness & Orchestration / Runtimes & Inference Engines / Hardware
   Backends / Networking & Cloud Fallback / Voice Engine) grounded in its actual docs — that's
   the model for *how* to do it per-folder, not the specific subsection names to reuse.
3. Execute the actual mirror-copy of deduped Drive content into the new structure
4. Download + reorganize into this git repo, push real vault content (this audit folder is
   scaffolding, not final content — remove once real content lands)

## Key lesson learned this session
Generic filenames (`README.md`, `SKILL.md`, `config`, `HEAD`) collide across unrelated projects
when grouped by bare filename — always qualify by parent folder name before treating same-name
files as duplicates or versions of each other.
