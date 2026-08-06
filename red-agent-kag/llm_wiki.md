# red-agent-kag — LLM Wiki

## What this is

The audited tail of the 4-part operational loop. Combines:

- **red-agent-auditor** — sandboxed auditor that intercepts at the files-inference-node → editor handoff. Receives the same tools the secretary just used; runs full system audit before editor sees output.
- **recursive KAG** — cloud agent → GCP bucket → JSONL compression → recursive knowledge-augmented generation scripting.
- **MoE/MoA configs** — Hydra rotation configs for swapping cloud models into the peer-agent slot; MoE routing for the recursive KAG pass.

## Pipeline position

```
files-inference-node (secretary)
  → [TRAP DOOR]
  → red-agent-auditor (sandboxed)
  → editor / review checkpoint
  → cloud agent → GCP → JSONL → recursive KAG
```
