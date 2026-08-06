# home-node — LLM Wiki

## What this is

The operator's home compute setup. Two SOCs wired together, functioning as a single logical workstation.
Eventually replaces the laptop entirely. ARM64 + commercial GPU is the planned v2 unlock.

## Network topology

- Jetson ↔ Rubik Pi 3: direct high-speed cable
- Razr ↔ home node: Tailscale (WiFi)
- Tab S9 FE+: SSH / AVNC into Jetson (thin client, couch use)
- All three compute nodes: P2P servers on the same Tailscale mesh

## Roadmap

ARM64 + commercial GPU (modular, form factor TBD). Goal: custom-designed workstation
replacing the laptop. Includes theoretical metamaterials and novel thermal management
designs — potentially patentable, kept offline until filed.

## Sub-folders

- `jetson-orin/` — setup, VNC server, headless config, SD card flash procedure
- `rubik-pi-3/` — DragonWing setup, visual OS, dual monitor, keyboard config
- `utilities-agent/` — housekeeping: loads/unloads operator agents
- `peer-agent/` — twins with novus-agenti; Hydra model rotation; MoA/MoE
