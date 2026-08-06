# novus-agenti — LLM Wiki

## What this is

The phone-side agent. Runs on the Razr Ultra under AESOP XI governance.
Peers with the home node agent across Tailscale.

## Key relationships

- **AESOP XI** (`../aesop/`) — governing layer: provides MCPs, hooks, routing, memory
- **nova-claw** (`../nova-claw/`) — action surface: skills this agent can invoke
- **home-node/peer-agent** — the twin agent on the Jetson side
- **horizons-ui** (`../horizons-ui/`) — the Android app that hosts this agent

## Documents to add here

- Runtime manifest (model + daemon + SDK version in use)
- Daemon lifecycle contract (alive ≠ ready)
- greenLight four-check spec
- API/endpoint registry
- Memory wiring diagram
