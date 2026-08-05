# CLAUDE.md — File management and memory tiers

> **THIS IS WHERE WE'RE AT.** The State of the Union for this folder, in the same
> **W5+H** schema as the blueprint — so target and status line up header for
> header and the gap is readable at a glance.

## Gospel

**[`../canon/MASTER-BUILD-BLUEPRINT.md`](../canon/MASTER-BUILD-BLUEPRINT.md)** is
the target: the W5+H universal blueprint (§1), the build map (§12.1), the action
chart (§12.2), the flip chart (§12.3), the file architecture (§12).

**This folder is a comparison against it.** Same six headers below. If this folder
and the blueprint disagree, the blueprint is the target and this is the status.

---

## State of the Union — W5+H

### WHO
The corpus itself is the consumer.

### WHAT
tier-1-episodic (mem0) · tier-2-structural (open-wiki, obsidian vault) · tier-3-analytical (graphify, notebooklm-py) · the RAG library.

### WHERE
**'Tier' means information type here, and only here** — never stack role. Do not carry this numbering anywhere else.

### WHEN
Tier 2 is the durable layer this corpus *is*. Tiers 1 and 3 are runtime.

### WHY
Three different kinds of memory need three different stores; collapsing them is what produced the duplication this migration cleaned up.

### HOW
Documents follow the four-artifact convention, joined on shared basename.

---

## Delta

**The RAG library's internal path mirror is stale** — it mirrors the pre-migration tree and needs regenerating.

**Build state is not recorded here.** It is recorded once, in
[`../canon/STATE-OF-EXISTENCE.md`](../canon/STATE-OF-EXISTENCE.md). No folder
asserts its own status.

---

## The kit

| File | Holds |
|---|---|
| `README.md` | what this folder is, for a human |
| `CLAUDE.md` | **this file** — where we're at, W5+H, for an agent |
| `llm_wiki.md` | machine-facing index, generated not hand-written |
| `skill_manifest.json` | structured metadata |

## Working rules

- **Read everything, completely, before acting** (Rule 0).
- **One axis on disk** — organised by **domain**. Format tier and corpus type are
  frontmatter tags, never folders.
- **Four-artifact documents** — `name.pdf` + `name.md` + `name.jsonl` (when large)
  + `skills.md`. **Same basename = same document** is the audit's join key.
- **Metaphors:** behavioural ones never become enforcement code; visual references
  supplied with a picture *are* literal specs and get built exactly (Rule 7).
- **Verify mechanically** (Rule 4). Your own report is not evidence.
