# red-agent-auditor

Sandboxed auditor. Intercepts at the handoff point between the files-inference-node and the editor — the "trap door" in the 4-part loop.

## Role in the loop

```
files-inference-node  →  [TRAP DOOR]  →  red-agent-auditor  →  editor
```

Receives the same tools the secretary (files-inference-node) just used.
Runs a full system audit before output reaches the editor.
Operates in a sandbox — isolated from live state.

## Status

Designed-only. See `../canon/STATE-OF-EXISTENCE.md`.
