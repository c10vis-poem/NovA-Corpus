# red-agent-auditor — LLM Wiki

## What this is

The auditor node in the 4-part operational loop. Sandboxed. Gets same tools as the secretary but uses them to verify, not produce.

## Position in the loop

1. novus-agenti + peer-agent produce output
2. files-inference-node (secretary) compiles, strips, compresses, pushes to cloud
3. **red-agent-auditor intercepts at handoff** — runs full audit on the package
4. Output goes to editor, then cloud KAG pipeline

## Key property

The system (secretary) thinks it's dropping the package in the mailbox.
The red agent is the trap door on the way there.
