---
title: Source Precedence — what to believe when sources disagree
status: CANON — the ordering, per the operator
scope: every document in the corpus
---

# Source Precedence

> **What this is.** The order to read sources in, and which one wins. One page.
>
> **Guiding principle.** This is not a ranking of quality. It is a ranking of
> **recency and correction depth.** A source is authoritative in proportion to how
> recently the operator went through it and how line-by-line he corrected it.
>
> **Verification rule.** When two sources disagree, apply the order below. Use
> common sense — most divergences are just age and need no adjudication.

---

## The order

### 1 · The shipped code, for anything it actually implements
The home screen is the standing example. **The code is right; the document is
wrong.** Corrections flow document-ward.

### 2 · The spec-by-spec PDFs — the operator's line-by-line corrections
**The most accurate and important material, and the base for chiselling any new
spec.** These are the sessions where the operator went over spec after spec and
corrected them as they went. What makes them authoritative is not the assistant's
prose — it is that the operator *pushed back, item by item*, and each pushback is a
direct statement of intent.

| In the repo | What it settles |
|---|---|
| [`../pending-corpora/transcripts/gemini-architecture-thread-2026-08-04.pdf`](../pending-corpora/transcripts/gemini-architecture-thread-2026-08-04.pdf) (+ `.md`) | rooms, the four parameter layers (Weights/Runtime/Engine/Communication), launch + recovery daemons, the sleep timer, the STT stack. **Corrected twice by the operator, mid-thread.** |
| [`../pending-corpora/transcripts/gemini-metaphor-drift-analysis.md`](../pending-corpora/transcripts/gemini-metaphor-drift-analysis.md) | how the metaphors got over-literalised into gates — the diagnosis behind Rule 7 |
| [`../pending-corpora/transcripts/gemini-dynamic-params-proposal.md`](../pending-corpora/transcripts/gemini-dynamic-params-proposal.md) | device-agnostic parameter packets. **None of it was built.** |

**Read the operator's turns.** The assistant's prose around them is worth nothing
on its own — these tools get used as a scribe, and only omissions that mattered got
corrected. Silence is not endorsement.

### 3 · The Aug-2 master plan
[`../pending-corpora/transcripts/neuromesh-aesop-xi-master-plan-2026-08-02.md`](../pending-corpora/transcripts/neuromesh-aesop-xi-master-plan-2026-08-02.md)

The whole-system architecture — nodes, memory tiers, the W5+H structure, the flow
maps. **The visuals are the good part.** The operator's own read: the prose is
sloppy, the diagrams are not. Structure is canon; implementation claims are not.

### 4 · Locked visual specs and operator-verbatim documents
`HOME-REDESIGN-SPEC.md` · `ROUTER-STEREO-STACK-SPEC.md` ·
`MONITOR-ARCADE-CABINET-SPEC.md` · `TERMINAL-SPEC.md`

Reference image supplied + "this is what it's going to be" = **specification.**
Build order may be deferred; the design is not.

### 5 · Grout — the summarization folders
The Aug-5 `What_it_IS_/What_it_DOES` folder and similar.

**Grout, not tile.** Fills gaps, holds things in position, read *alongside* the
newer material. Genuinely valuable — it's where `greenLight`'s four checks, the
RouterConfig model, and the three failure faces came from. Where it's older, the
newer thing just wins.

### 6 · Everything else
Older repo docs, session logs, AI proposals. Several describe **different
applications** — see `horizons-ui/AGENT-BRIEF.md` §0. History, not instructions.

---

## Two standing rules

**Snapshot what you cite.** Drive is being pruned. Any Drive document used as a
source gets copied into this repo at the point of use — a citation to a deleted
path is a broken citation, and the mechanical check can't verify what isn't there.

**Grade, don't average.** When sources disagree, pick by this order. Never blend
two versions into a third that neither says.
