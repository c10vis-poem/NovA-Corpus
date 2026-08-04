# NovA-Corpus — Universal Corpora Repository

## Context

Rebuilding the knowledge/documentation pipeline after multiple prior agent sessions reported work
that was never done. Verified this session: the Obsidian vault has ~170 QAIRT/HTP files duplicated
across four parallel top-level trees (`fraqat-paper` ×3, `omni-claw-blueprint` ×2); Repo-Bank has
the same disease (`NovA-openship` ×3, six more ×2).

**Root cause of the "every file is contradictory" problem:** every document describes the *designed*
system as though it were the *built* system. Not 200 independent errors — one systematic error
repeated everywhere. An agent reading them can't distinguish intent from reality, cites features
nobody wrote, and the next doc inherits it. Rule 6 below is the fix.

**⚠️ THE APK IS PRIORITY ONE.** All corpus work is a means to an end — the agent stack. Its purpose
is to make the APK ship *faster*. If the corpus becomes the project, it has failed. The user works
his devices in tandem while the APK gets finished — not sequentially. Never cite a priority number
to explain the app's state; Horizons-UI is the lifecycle root ("nothing lives without it").

---

## 1. Naming — DECIDED

- **Repo slug:** `NovA-Corpus` — prefix-consistent with NovA-Claw / NovA-skills / NovA-code-review-
  graph; `corpus` is the precise ML term; singular = the one unified body.
- **Project name / README title:** **Novus Corpora** — the constituent corpora inside it.
- **Avoid `vault` / `archive`** in naming — both connote frozen storage, contradicting the living
  `CLAUDE.md` / `llm_wiki.md` / daisy-chain model.
- Transform target: `c10vis-poem/obsidian-master_wiki` (cloned at `/workspace/obsidian-master_wiki`,
  1305 files). GitHub auto-redirects on rename; existing clones survive.

## 2. Repo strategy — current thinking (user, latest)

Four repos: **NovA-Claw + Novus-Agenti combined** (one agent) · **Horizons-UI** · **skills/tools** ·
**NovA-Corpus** (this one — the whole framework setup).

*On record and unreconciled:* an earlier statement said NovA-Claw and Novus-Agenti should be two
separate repos. Latest stands unless the user says otherwise; do not silently merge the two records.

## 3. Five sorting dispositions

Folders, not tags — promotion is a `git mv`, visible in history as an event.

| Bucket | Contents |
|---|---|
| **Canon** | Settled truth. Everything trickles down from it. |
| **Pending corpora** | Experimental / unproven |
| **Vault** | Alternative build approaches, possibly usable later |
| **Reverse-engineering** | Salvageable for troubleshooting or failback |
| **Toss** | Stale/dead — deleted, no folder |

**Triage precedes topical filing** — a document can't be placed by subject until its truth status is
known. Buckets sit at the top level during curation; the domain tree lives *inside* canon. Once canon
is defined, sub-agents sweep the remainder against it mechanically.

**Bar for canon is not perfection** — "if it holds truth you can extract," it's usable source
material for the official docs, even if the source document itself is messy.

## 4. Structure — three templates, DO NOT MERGE

"Tier" was previously misapplied as one prefix across two unrelated taxonomies (stack *role* vs.
memory *information-type*). Three separate templates:

**(1) Corpus folder structure** — flat, plain domain names, no `tier-N-` prefix:
```
NovA-Corpus/
├── horizons-ui/            src/ · native-voice-layer/
├── novus-agenti/           executor-core/ · query-core/
├── nova-claw/              daemons/ · runtimes/ · tool-skills/
├── aesop/                  ob1/ · omni-route/ · mem0/ · reasoning-bank/ · memory-tools/
├── nodes/                  jetson/ · rubik-pi/ · razr   [internal split DEFERRED]
├── termux/                 "part of the body" — sits between nodes and skills
├── skills/                 ROUTER.md · base_skill_guideline.md · <skill-name>/
├── clis-and-agents/        open-wiki-tui/ · pi-agent/ · claude-code-local/ · code-review-graph/
├── discovery/              AI-search-tool + intake queue  [name TBD]
├── file-management-system/ memory tiers live HERE ONLY — see (3)
├── recursive-training/     [designed-only]
├── red-agent-auditor/      [designed-only]
├── github-ci-cd/           workflows/
├── global-documentation-vault/  qairt-docs/ · genie-x/ · google-dev-docs/ · llama-docs/ · unsloth-docs/
└── registries/             models.md · repos.md
```
Root also carries: `README.md` · `CLAUDE.md` · `STACK-MAP.md` · `GLOSSARY.md` · `master_blueprint.txt`

**(2) Repo structure** — deeper per-repo template (`.github/workflows/`, `app/src/main/...`), used
**only** when a domain graduates into its own git repo with build tooling. Template lives in
`github-ci-cd/README.md`.

**(3) Memory structure** — scoped **only** to `file-management-system/`; "tier" here means
information-type, not stack role:
```
file-management-system/
├── tier-1-episodic/        mem0 storage
├── tier-2-structural/      open-wiki-cli-vault/ · obsidian-vault-network/
├── tier-3-analytical/      graphify-pipelines/ · notebooklm-py-contexts/
└── target-docs/            curation yard
```

### Section kit
Every folder **and** every major subsection: `README.md` · `CLAUDE.md` · `llm_wiki.md` ·
`skill_manifest.json`, plus whatever else that folder requires.

### Four-tier document convention
Sibling files, one folder, shared basename — **not** four subfolders:
```
fragmented-qat/
├── fraqat-paper.pdf      original, untouched
├── fraqat-paper.md       cleaned markdown
├── fraqat-paper.jsonl    only when large/structured enough
└── skills.md             routes the folder
```
**Same basename = same document** is the join key, and makes migration mechanically auditable: walk
every original, assert a matching `.md` exists — output is a list of missing filenames, not an
agent's status claim. Also detects orphans and cross-folder duplicates. This check is what did not
exist during the failed vault runs.

### One axis on disk
Three axes in play — **domain**, **format tier**, **corpus type** (Code/DevOps/Asset/Human-Knowledge,
from the Drive `(Preface) Multi-Corpora Ecosystem` doc). A filesystem expresses one; the others are
frontmatter tags + a generated index. Violating this produced the vault's duplication.

---

## 5. Memory architecture — RESOLVED

**OmniRoute is the shared platform OB1 and mem0 both operate from.** Its MCP + A2A support lets it
front both as an aggregation/dispatch layer: agents talk to one gateway; OmniRoute routes memory
reads/writes to **OB1** (structural — how memory is doled out, the protocol layer) or **mem0**
(episodic — what's being accessed in the moment). No pick-one needed. The old Gemini doc's "Omni
Route decision matrix" now has a real host: this repo's dispatch policy, not a from-scratch build.

**Must persist into the project's `CLAUDE.md`/`GLOSSARY.md` — the user does not want to re-explain
this.**

Verified from the actual OmniRoute doc (an earlier claim that it was "unrelated to memory" was wrong,
based on a listing snippet rather than the document): SQLite FTS5 full-text + int8-quantized vector
embeddings + typed decay (anti-bloat); opt-in, per-request controllable via `x-omniroute-no-memory`;
MCP (stdio/HTTP/SSE) + A2A v0.3. Separately it has connection-level resilience — circuit breakers,
key cooldowns, model lockout — which is a *different* mechanism from memory typed-decay.

**reasoning-bank** is not a backend — it's Google ICLR research code (WebArena/SWE-bench, no server/
API/MCP). The reusable part is the *pattern*: Title/Description/Content memory-item schema, and
**learning from failed trajectories, not just successful ones** — which neither OB1 nor mem0 do.
Layers onto the stack; feeds the recursive loop and Red Agent.

**Open:** once OB1/mem0 are behind OmniRoute, does OmniRoute's own memory stay on as local cache /
offline fallback (valuable for on-device when cloud isn't reachable), or get disabled per-request?

## 6. Red Agent Auditor — MoA/MoE consensus refinement `[designed-only]`

Mixture of *independently-sourced* models (not multi-sample on one model) for zero-fail auditing.
Sound because a single auditor can't catch its own blind spot — it fails identically every time it
checks itself.

**Two open questions:** (a) **scope** — apply to high-stakes decisions only (pending→canon promotion,
frozen-path changes, single-pass rejections), not all routine traffic, or the audit stack becomes the
project; (b) **disagreement resolution** — auto-reject on split (fail-closed, matches zero-trust) vs.
escalate to HITL. User is already sole conduit *to* the Red Agent; this is the mirror question.

**Tooling:** `NovA-crewAI` (already forked) is built for exactly this orchestration — closer fit than
building consensus/voting from scratch.

## 7. W5+H README template

Root `README.md` uses the approved structure (skeleton from the Gemini doc; content rewritten).
Section READMEs carry a scaled-down W5+H at section scope — same six headers, which is what makes
them diffable.

**§0 Zero-Trust Manifesto — six enforcement rules:**
1. **Unchecked Writes Prohibited**
2. **Decoupled Isolation (One Agent, One Repo)** — enforced at the **output/commit layer, not input**.
   Every agent reads the same documentation vault; no agent writes another's scope.
3. **No Cross-Contamination** — except via Omni Route
4. **Mechanical Verification** — basename audit, never an agent's self-report
5. **Pending Corpora, Not Discard** — Gemini-sourced material is kept and mined; hallucinated
   specifics don't justify discarding a document; promotion to canon requires verification
6. **Designed ≠ Built** — every component tagged `built-verified` / `built-unverified` /
   `designed-only` / `absent`

**§1 Core Architecture Matrix (W5+H)** — corrections vs. the Gemini original: Horizons-UI is the
lifecycle root; OB1 is a protocol spanning both cores, not a storage tier under one branch; Reasoning
Bank included; dual-model executor/query split; HITL is sole conduit to the Red Agent.

**§2** Master Repository & Data Directory Blueprint · **§3** Skill Construction & Dataset Loading
Protocol.

---

## 8. Document placement map (rough first pass)

### From the Obsidian vault (`/workspace/obsidian-master_wiki`, 1305 files)
| Source | Destination |
|---|---|
| `#HORIZONS-main/` + `Repo docs/` (COMPILE-PIPELINE, HOME-REDESIGN-SPEC, FEATURE-SPEC, BUILD-ACTION-PLAN) | `horizons-ui/` |
| `MONITOR-ARCADE-CABINET-SPEC.md`, `ROUTER-STEREO-STACK-SPEC.md`, `TERMINAL-SPEC.md` | `horizons-ui/` (UI specs) |
| `CRASH-ANALYSIS-2026-07-31.md` | `horizons-ui/` |
| `#Useful_knowledge_/…/OMNI.CLAW_DEFINED/` (blueprint, repo-fork-asset-list) | `nova-claw/` |
| `#AESOP_HORIZONS-UI_Master` | split → `aesop/` + `horizons-ui/` |
| `…/Research.NPU/`, `…/#QAIRT/` | `global-documentation-vault/qairt-docs/` |
| `…/Fragmented QAT/`, `#RESEARCH/` | `global-documentation-vault/` (research) |
| `#Useful_knowledge_/…/GEMINI.QUERY/` | **pending-corpora** (transcripts, not spec) |
| `yJSONL_data.bank_/` | dissolve — `.jsonl` files become siblings of their matching docs |
| `RAG_LIBRARY` | `file-management-system/` |
| `#RESEARCH DOSSIER 1&2/` | **dedup first** — largely duplicates of `#Useful_knowledge_/` |
| `_DUPLICATES_REVIEW` | triage, then delete |

### From Drive
| Source | Destination |
|---|---|
| neuromesh PDF (Aug-2 AESOP XI master plan) | **canon** — this is the master plan |
| `-Builders_Guide/` (SKILL.md structure docs) | `skills/` |
| `-Builders_Guide/Files_Management_Corpus/` | `file-management-system/` |
| `#QAIRT_main/#QAIRT`, `Qualcomm user-Guides` | `global-documentation-vault/qairt-docs/` |
| `#QAIRT_main/QAIRT-SDK/GenieX` | `global-documentation-vault/genie-x/` |
| `#QAIRT_main/zqnn/qairt-System Design` | **pending-corpora** (user-labeled "half Gemini slop") |
| `Repo-Bank_/` | `registries/repos.md` + per-domain distribution |
| `---8-4-26/` (22 session excerpts) | **pending-corpora** or reverse-engineering |

### Known duplicates to resolve at intake
`fraqat-paper` ×3 · `omni-claw-blueprint` ×2 · `repo-fork-asset-list` ×2 · `edge-ai-hub-integration` ×3
· `NovA-openship` ×3 · `orca`/`pi`/`claude-skills`/`NovA-skills`/`code-review-graph`/`pm-claude-skills`/`ECC` ×2

---

## 9. Repo-Bank assessment (60+ forks scanned)

- **`OmniRoute`** — see §5. Real memory subsystem; the aggregation layer.
- **`ECC-aesop`** (fork of `affaan-m/ECC`) — cross-agent skills/memory/security harness. **Rename
  needed** — collides with the AESOP protocol name.
- **`NovA-orca`** — candidate for fleet orchestration itself, not just a housekeeper tool.
- **`c10vis--pi`** — home-node coding agent; `tmux-assistant-resurrect` explicitly supports it.
  Hermes/aider/Pi/Claude Code/Open Wiki are **candidates, not redundancy to prune** — depends what
  wins in practice.
- **`kotlin-sdk`** (JetBrains MCP SDK) — load-bearing; likely the real dependency for Horizons-UI's
  known-gap Termux inbound listener.
- **`NovA-crewAI`** — the MoA/consensus orchestration fit (§6).
- **`merovin-generative-ai-poem`** / **`Merovin-genai-for-developers`** — landing point for the $1000
  Vertex credits.
- **`NovA-openship`** — verify: upstream "Openship" is order-routing/fulfillment, may not do what the
  name implies here.
- **`SuperClaude_Framework`** — overlaps the custom `skills/` system; needs an explicit either/or.
- **`anything-llm`** — reference implementation to study, not integrate. Vault.
- **`crawl4ai`** (discovery pipeline) vs **`NovA-browser-use`** (Horizons-UI browser tab) — different
  jobs, both earn a place.
- **`off-grid-ai-mobile`**, **`poem-speech-to-speech`**, **`claude-code-android`** — the interim
  on-device voice path already owned.
- **`nanobot_style_personal_ai_agent`** — read in full. Colab teaching notebook: Provider abstraction,
  `@tool` decorator deriving JSON schema from type hints, session Memory with token-budget compaction,
  Agent tool-loop, `Skill` dataclass matching this project's SKILL.md shape, MCP stand-in. **Hook
  system (`AuditHook`/`TimingHook`/`CensorHook`) is most of what a Red-Agent watcher needs, ~40 lines.**
  Hardening needed: in-process dict memory (wipes on restart), raw `exec()` in the Python tool, mock
  MCP. **Action item:** write the user's requested custom script from this.

## 10. Home stack

- **Jetson = main computer.** Phone = heavy lifter for agent tasking (why the mem0 dual-agent
  architecture lives on the phone).
- Main-compute agent · Jetson inference agent · **Rubik Pi housekeeper** (candidate: pi-agent + aider
  + notebooklm), sandboxed, sharing the universal memory layer.
- **Housekeeper ↔ Red Agent is an open swap, not a merge.** Do not conflate.
- `nodes/` internal layout **deferred** — user hasn't done the Jetson/Rubik-Pi research yet.

## 11. Bookmarklet behavior (user asked)

Verbatim clone of a **subset** — no summarizing. "Cleaning" strips HTML/CSS/buttons. But it selects
only `p, li, h1, h2, h3, pre code` — content in `div`, `table`, `blockquote`, or code blocks not
wrapped in `<pre><code>` is **silently dropped**. Real data loss for threads with ASCII diagrams and
tables.

---

## 12. Next steps

1. **Visual artifact** of the folder tree — the user copies it into Drive by hand.
2. **Canon definition pass** — go through files together, sort into the five buckets.
3. User shows the documentation format/visual style they want; Markdown authoring stays Claude's
   call, presentation follows the user's conventions.
4. Then migration: per-document four-artifact treatment.

## 13. Open items

1. `global-documentation-vault/` weight — QAIRT PDFs ~7MB each, `.mht` ~2MB, dozens. Git LFS inside
   `NovA-Corpus`, or break out as its own repo?
2. Red Agent + recursive-training flows — **user has not defined these.** Folders scaffolded,
   `designed-only`, do **not** populate with invented architecture.
3. `discovery/` folder name — TBD.
4. OmniRoute built-in memory — cache/fallback, or disabled? (§5)
5. Red Agent MoA scope + disagreement resolution (§6).
6. `yt→md` tool not yet forked; PDF-compression and JSONL-structuring utilities named but unselected.
7. NovA-Claw + Novus-Agenti: one repo or two (§2).

## 14. Verification

Mechanical, not self-reported:
- Every folder has `README.md`; every section folder has the full kit.
- Every original document has a sibling `.md` — report missing as a filename list.
- No basename appears under two different folders.
- Every component in the W5+H matrix carries a state tag from Rule 6.
