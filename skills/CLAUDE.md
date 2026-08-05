# CLAUDE.md — Skills

> **THIS IS WHERE WE'RE AT.** Read this first. It is the State of the Union for
> this folder: what you are supposed to have, what you actually have, and the gap
> between them.

## Gospel

**[`../canon/MASTER-BUILD-BLUEPRINT.md`](../canon/MASTER-BUILD-BLUEPRINT.md)** is
the target. It is the W5+H universal building blueprint — who, what, where, when,
why, how — plus the build map, the action charts, and the file architecture.

**Everything in this folder is a comparison against it.** Nothing here describes
the system in isolation. If this folder and the blueprint disagree, the blueprint
is the target and this folder is the status.

## Where we're at — Skills

SKILL.md corpus, the construction guideline, and the router.

| | |
|---|---|
| **Supposed to have** | see the blueprint sections that cover this domain |
| **Actually have** | see [`../canon/STATE-OF-EXISTENCE.md`](../canon/STATE-OF-EXISTENCE.md) — the one ledger that says what is built |
| **Delta** | anything in the first column not tagged `built-verified` in the second |

⬜ **Not yet filled in for this folder.** The blueprint is still DRAFT and the
"actually have" audit has not been run against live code. Do not infer a status
that isn't written here.

## The kit

Every folder carries four files. This is the second one.

| File | Holds |
|---|---|
| `README.md` | what this folder is, for a human |
| `CLAUDE.md` | **this file** — where we're at, for an agent |
| `llm_wiki.md` | machine-facing index, generated not hand-written |
| `skill_manifest.json` | structured metadata |

## Working rules

- **Read everything, completely, before acting** (Rule 0).
- **One axis on disk** — this tree is organised by **domain**. Format tier and
  corpus type are frontmatter tags, never folders.
- **Four-artifact documents** — `name.pdf` + `name.md` + `name.jsonl` (when large)
  + `skills.md`. **Same basename = same document** is the join key the audit runs.
- **Never promote a metaphor into a constraint** (Rule 7) — but visual references
  supplied with a picture *are* literal specs, and get built exactly.
- **Verify mechanically** (Rule 4). Your own report is not evidence.
