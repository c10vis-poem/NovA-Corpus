# memory-scripts — LLM Wiki

## What this is

The scripting layer between the 4-part operational loop and the memory/storage backend. Handles everything from JSONL compression to NPU resource management to the recursive KAG cycle.

## Sub-system map

```
files-inference-node (secretary)
  → red-agent-scripts/ (audit pass)
  → jsonl-compression/ → recursive-kag/ (cloud tail)
  → pdf-compression/ (corpus input)

home-node
  → npu-management/ (Jetson TOPS allocation)
  → inference-scripts/ (peer ↔ node handoff)
  → housekeeping/ (utilities-agent)
  → memory-nano-agent/ (OB1/mem0 ops)
```
