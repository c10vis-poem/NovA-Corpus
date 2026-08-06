# novus-agenti

The phone-side agent built on AESOP XI. Defines what the agent IS and how it runs on the Razr Ultra.

## Scope

- Agent identity and architecture
- Runtime manifests (which model, which daemon, which SDK version)
- Device integration (APK reference, daemon config, hardware requirements)
- API and endpoint registry
- Memory layer wiring (connects to OB1/mem0 via AESOP XI)

## Hardware

Razr Ultra (SM8750 / Snapdragon 8 Elite) — 16GB RAM · ~512GB storage · ~45 TOPS (Hexagon HTP v79)

## Peer

Twins with the `home-node/peer-agent/` — two sides of the same operational loop.
See `home-node/README.md` for the 4-part loop architecture.

## Status

See **[`../canon/STATE-OF-EXISTENCE.md`](../canon/STATE-OF-EXISTENCE.md)** — the single ledger for build state.
Nothing in this folder asserts its own build state.
