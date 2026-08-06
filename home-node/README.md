# home-node

The home compute setup — parallel to `horizons-ui/` on the phone side.
Two SOCs working as one logical unit, connected by high-speed cable.

## Hardware

| Board | Chipset | RAM | Storage | TOPS | Role |
|---|---|---|---|---|---|
| Jetson Orin Nano Super | — | 8GB | 512GB DDR4 SSD | ~67 | Main compute, runs headless |
| Rubik Pi 3 | DragonWing | 8GB | ~128GB built-in | ~14 | Visual OS, dual monitor, keyboard |

Jetson ↔ Rubik Pi 3: direct high-speed data cable (wired)
Razr ↔ home node: Tailscale over WiFi
All nodes: P2P servers on the same Tailscale mesh

## Sub-folders

- `jetson-orin/` — Jetson Orin Nano Super setup, VNC server config, headless config
- `rubik-pi-3/` — Rubik Pi 3 (DragonWing) setup, visual OS, display config
- `utilities-agent/` — housekeeping agent: load/unload operator agents (user guides, help desk, task mgmt, file management)
- `peer-agent/` — twins with novus-agenti; swappable cloud models; Hydra MoA/MoE rotation

## The 4-part operational loop

```
[1] novus-agenti (phone)  <peer>  [2] peer-agent (here, Jetson/cloud)
               └──────────┬──────────┘
                          ▼
         [3] files-inference-node  (secretary — manifest, logs, KAG prep)
                          │ [trap door — red agent intercepts at handoff]
                          ▼
         [4] red-agent-auditor  (sandboxed — same tools, full audit)
                          ↓ editor → cloud agent → GCP → JSONL → recursive KAG
```

## Status

See **[`../canon/STATE-OF-EXISTENCE.md`](../canon/STATE-OF-EXISTENCE.md)**.
Nothing in this folder asserts its own build state.
