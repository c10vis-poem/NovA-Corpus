# files-inference-node — LLM Wiki

## What this is

The system secretary. Collects output from both primary agents, processes it, and hands it to the cloud KAG pipeline — unaware of the red-agent trap door on the way.

## Pipeline

```
novus-agenti + peer-agent
        ↓
files-inference-node
  · compile log manifest
  · sort / strip / compress
  · push to GCP
  · prep JSONL for KAG
        ↓ (trap door intercepts here)
red-agent-auditor → editor → cloud agent → GCP → recursive KAG
```
