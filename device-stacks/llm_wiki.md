# device-stacks — LLM Wiki

## What this is

The physical device layer. Documents each compute node, its hardware specs, its role in the system, and its specific configuration.

## Nodes

**Razr Ultra (horizons-ui/)** — Phone. SM8750, 16GB RAM, ~512GB, ~45 TOPS (Hexagon HTP v79). Runs Horizons-UI app + novus-agenti.

**Jetson Orin Nano Super (home-node/jetson-orin/)** — Main compute hub. 8GB RAM, 512GB DDR4 SSD, ~67 TOPS. Headless; accessed via Rubik Pi 3 (desk) or AVNC from Tab S9 FE+ (couch).

**Rubik Pi 3 / DragonWing (home-node/rubik-pi-3/)** — Visual output for the Jetson. 8GB RAM, ~128GB SSD, ~14 TOPS. Drives dual monitors + keyboard.

**Samsung Galaxy Tab S9 FE+ (thin client, no repo)** — Occasional SSH into Jetson. Termux + AVNC. Wi-Fi only.
