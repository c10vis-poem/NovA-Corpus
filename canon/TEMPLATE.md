# CANON TEMPLATE — the required shape of every document in `canon/`

> **Scaffolding. Delete when the cleanup is done.** This exists to get the corpus
> sorted once. It is not part of the system and shouldn't outlive the migration —
> once the documents are right, they're right, and a document about how to write
> documents is just overhead.

> **Where this came from.** This template was **not designed**. It was extracted
> from `HOME-REDESIGN-SPEC.md` (the Aiwa-CD-player / arcade-cabinet session),
> which was already doing all of it before the rules were written. That document
> is the reference implementation; this file is only its structure made explicit
> so other documents can be conformed to it.

---

## What canon is

Canon is **not** "documents we trust." Canon is:

> **the operator's verbatim word, anchored to a concrete artifact, with anything
> derived visibly separated from it, and its build state declared.**

If a document has no operator quote in it, it is not canon — it is derived work,
and it belongs in `pending-corpora/` until an operator statement backs it.

---

## Required document shape

### Header block — always first

```markdown
# <NAME> — <one-line what-this-is>

> **What this is.** <scope: what it governs, what reads it, when>
>
> **Guiding principle.** <what this artifact is NOT — the misreading to prevent>
>
> **Verification rule.** <who checks, how, and what counts as "done">
```

The **guiding principle** is load-bearing. `HOME-REDESIGN-SPEC.md` opens by saying
its own renders are *"a visual TARGET / mockup — REFERENCE ONLY … NOT screenshots
of a live or near-complete app."* That single line is what stops the next reader
from citing a mockup as a shipped feature. Every canon doc needs its equivalent.

### Body sections — artifact, then operator, then spec

```markdown
## N · <thing>

![reference](path/to/artifact.webp)          ← 1. the artifact, on top

> **Operator:** *"...verbatim..."*            ← 2. the operator's own words
> *"...second quote, if the point took two..."*

**Spec.** <distilled, actionable, unambiguous>  ← 3. derived — clearly labelled
```

Rules for the body:

- **The artifact leads.** Image, file path, commit hash, log excerpt — something
  that exists and can be checked.
- **Quotes are verbatim.** Including the operator's phrasing, emphasis, and typos
  (`"12 o'clck"` stays). Do not clean them up. Paraphrase destroys the evidence.
- **`**Spec.**` is the only place derived content lives**, and it is always
  labelled. A reader must be able to tell, at a glance, what the operator said
  from what an agent concluded.
- **Contradictions are recorded, not resolved.** When the operator's word conflicts
  with shipped code or another document, state both and mark the conflict. Silently
  picking one is how the corpus started lying.

### Closing sections — always last

```markdown
## N · What is PERFECT — do not touch
<the frozen surface, in the operator's words>

## N+1 · Status ledger
- ✅ <shipped>
- ⛔ <reverted / rejected>
- ⬜ <PENDING>

## N+2 · Open / to-confirm
<known-unknowns, named — never quietly filled in>
```

The **status ledger** is the Rule 6 (`Designed ≠ Built`) enforcement point at
document scope. Every claim in the document must be reachable from one of these
three marks.

---

## The rules, applied here

| Rule | How this template enforces it |
|---|---|
| 1 · Unchecked writes prohibited | `**Spec.**` may not contradict the quote above it |
| 2 · Decoupled isolation | one canon doc per domain; no doc rewrites another's scope |
| 3 · No cross-contamination | cross-domain claims link, they don't restate |
| 4 · Mechanical verification | the verification rule names a *check*, not a reviewer's opinion |
| 5 · Pending corpora, not discard | AI-sourced material cites its source and stays out of `canon/` |
| 6 · Designed ≠ built | the status ledger; every row tagged |
| **7 · Metaphor ≠ implementation** | behavioural vs visual — see below |

### Rule 7 · Metaphor ≠ Implementation — two kinds, opposite handling

**Behavioural — never compile.** *Fuse box · 10-amp fuse · breaker · amperage.*
These describe how the circuit behaves; they are config-file and interaction
language. Prior sessions compiled "10-amp fuse" into a hardcoded four-item
`AssetCheck` and turned the Router into a gatekeeper that threw red `⚡ FUSE BOX`
banners and blocked anything non-standard — killing custom binaries and
fine-tuned weights.

> **Operator:** *"the 'fuse box' and '10-amp fuse' were never meant to be compiled
> into restrictive UI gates, red warnings, or pre-execution blockers."*

**Visual — build literally.** *Aiwa CD player · arcade cabinet · stereo stack.*
Reference images were supplied with "this is what it's going to be." That is a
**specification**. Build it as described, with animations. Softening these into
"styling direction" is itself the failure.

**The test:** behaviour → never compile. Appearance → build exactly.

---

## Conformance check

A document is in `canon/` only if all five hold:

1. It has a header block with a **guiding principle** and a **verification rule**.
2. Every body section leads with an **artifact**.
3. It contains at least one **verbatim operator quote**.
4. Derived content appears **only** under `**Spec.**`.
5. It ends with a **status ledger** in which every claim is tagged.

Anything failing these belongs in `pending-corpora/`.
