# CLAUDE.md — Termux

The on-device shell layer. Part of the body: sits between nodes and skills.

## Before you read anything in this folder

1. **`../canon/STATE-OF-EXISTENCE.md` first.** It is the only document that says
   whether a thing is built. Everything here describes design; most of it is not
   running code.
2. **`../canon/TEMPLATE.md`** defines what canon is and the seven enforcement
   rules, including **Rule 6 (Designed != Built)** and **Rule 7 (Metaphor !=
   Implementation)**.
3. Nothing in this folder outranks `canon/`. If a document here contradicts
   canon, canon wins and the contradiction gets recorded, not silently resolved.

## Writing into this folder

- One axis on disk: this tree is organised by **domain**. Format tier and corpus
  type are frontmatter tags, never folders.
- Four-artifact convention: `name.pdf` (original, untouched) + `name.md` (cleaned)
  + `name.jsonl` (only when large/structured) + `skills.md` (routes the folder).
  **Same basename = same document** is the join key the audit runs on.
- Never promote a metaphor into a constraint (Rule 7).
