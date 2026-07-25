# Motorola Razr Ultra 2025

The primary development and deployment device for Novus Agenti.

## Specs

| Spec | Value |
|------|-------|
| SoC | Snapdragon 8 Elite (SM8750) |
| GPU | Adreno 830 |
| NPU | Hexagon HTP v79 |
| RAM | 16 GB |
| Form Factor | Foldable (clamshell) |

## On-Device Software

| Tool | Purpose |
|------|---------|
| Termux | Linux terminal emulator (no root) |
| Termux:Float | Floating terminal overlay (F-Droid only) |
| Markor | Markdown editor — reads this wiki vault |
| Obsidian | Knowledge base — reads this wiki vault |
| AVNC | VNC client (on Samsung Tab, connects to phone) |
| Xtigervnc + XFCE | VNC server + desktop (in Termux) |

## SDK / Runtime Files (on-device as of 2026-07-13)

Located in `/storage/emulated/0/Download/`:
- `geniex-bench-android-arm64 v0.3.14` (GGML + QAIRT backends)
- Q4_0 GGUF model file
- HTP v79 libraries

Re-verify before trusting exact versions/sizes — this snapshot is from
the device inventory audit of 2026-07-13.

## Paired Devices

| Device | Role | Connection |
|--------|------|------------|
| Samsung Tab S9 FE+ | VNC client, extended screen | WiFi LAN / phone hotspot |

## Related

- [[termux-mobile-dev]] — full Termux setup guide
- [[novus-agenti]] — the app that runs on this device
