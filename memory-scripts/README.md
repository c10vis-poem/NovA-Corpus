# memory-scripts

Invoking scripts and the dedicated memory/files nano-agent. All scripts that interact with the memory layer (OB1, mem0, OmniRoute), manage inference coordination, or handle housekeeping.

## Sub-folders

| Folder | Role |
|---|---|
| `recursive-kag/` | Recursive KAG scripting — cloud agent → GCP → JSONL → KAG loop |
| `jsonl-compression/` | JSONL compression and merging before KAG ingestion |
| `pdf-compression/` | PDF optimization for corpus pipeline |
| `red-agent-scripts/` | Scripts run by red-agent-auditor in sandboxed audit pass |
| `files-management/` | File system management (migrated from file-management-system/) |
| `npu-management/` | NPU load/unload, TOPS allocation, Hexagon HTP v79 resource mgmt |
| `inference-scripts/` | Peer-server ↔ home-node inference coordination |
| `housekeeping/` | Log rotation, temp cleanup, stale cache pruning |
| `memory-nano-agent/` | Dedicated nano-agent for memory and file ops |
