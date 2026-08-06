# files-inference-node

The "secretary" in the 4-part operational loop. Compiles manifests, processes logs, preps for cloud KAG. Does NOT know about the red-agent-auditor trap door at handoff.

## Responsibilities

- Compile manifest of all log scripts from novus-agenti + peer-agent
- Sort, strip, compress log output
- Push to cloud storage
- Prepare KAG (Knowledge-Augmented Generation) audit package
- Hand off to editor (via the trap door the red agent controls)

## Status

Designed-only. See `../canon/STATE-OF-EXISTENCE.md`.
