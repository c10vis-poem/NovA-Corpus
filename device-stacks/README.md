# device-stacks

Physical device layer. Each sub-folder documents one node in the P2P mesh.

## Sub-folders

| Folder | Device | Role |
|---|---|---|
| `horizons-ui/` | Razr Ultra (SM8750) | Android app + phone-side agent environment |
| `home-node/` | Jetson Orin Nano Super + Rubik Pi 3 | Home compute hub + visual output |
| `custom-mcps/` | All nodes | Per-node custom MCP configs |

## Network topology

```
Razr Ultra  ──Tailscale over WiFi──┐
                                   ├── Tailscale P2P mesh
Jetson ──high-speed data cable── Rubik Pi 3
```

All three compute nodes are P2P servers. Network config lives in aesop-xi/ (infrastructure/pathways layer).
