# peer-agent

Home-node twin to `novus-agenti` on the phone. One of the two primary agents in the 4-part operational loop.

## Design

- Runs on Jetson Orin Nano Super
- Swappable: rotates powerful cloud models in (Hydra architecture)
- Enables true MoA / MoE environment
- Recursive loop: actual operational, not just corrective or theoretical

## Peer

Twins with `../../novus-agenti/`. Both feed into `../../files-inference-node/` as part of the 4-part loop.
