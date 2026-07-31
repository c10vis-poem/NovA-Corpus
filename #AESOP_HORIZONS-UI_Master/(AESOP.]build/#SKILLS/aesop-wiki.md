---
name: aesop-wiki
description: "Aesop on-device deploy stack — Termux daemons, llama-server supervision, WebSocket bridge, voice pipeline, and model management for Snapdragon 8 Elite."
---

# Aesop Wiki

## What Aesop Is

Aesop is the **deploy and runtime stack** for on-device AI running in Termux on Snapdragon 8 Elite. It owns the GGML inference plane (llama-server with Gemma 4 12B), the WebSocket bridge to the Horizons app, daemon supervision via runit/termux-services, and the voice pipeline wiring.

Repo: `c10vis-poem/aesop`. Termux operational knowledge is in the `termux-helper` skill.

## Repo Structure

```
deploy/phone/daemons/
├── llamad-run          — runit run script for llama-server
├── aesopd-run          — runit run script for WebSocket bridge
└── install-daemons.sh  — symlinks services into termux-services
protocol/
└── bridge-protocol.md  — aesopd wire spec (JSON over RFC 6455)
skills/
└── termux-helper/      — canonical copy of the termux-helper skill
```

## llamad — The GGML Plane

llama-server on port 8081, supervised by runit.

**Model:** Gemma 4 12B IT QAT, Q4_0 quant. Runtime-repacks into i8mm/dotprod on SD 8 Elite. K-quants don't get that optimization.

**Memory:** mmap ON (reclaimable pages), `-fa -ctk q8_0 -ctv q8_0`, `-t 6` (big cores only). Resident: ~7GB model + ~0.5-1GB KV cache.

**Backend ladder:** Hexagon HTP → Adreno 830 via OpenCL → CPU big cores.

> **CORRECTED 2026-07-31.** This line previously read "NOT on the ladder: Hexagon
> DSP." That was wrong and it misled at least two sessions into treating GGUF/ggml
> as a CPU-only path. ggml HAS a Hexagon backend, and the compiled libraries for it
> are in this vault: `##LLM-WIKI_OPEN-WIKI.main_/llm-wiki/libggml-hexagon.so` plus
> `libggml-htp-v73/v75/v79/v81.so` (this device is v79). DEVICE-INVENTORY.md agrees:
> GenieX ships dual backends, llama.cpp (ggml, **HTP v68-v81** + CPU + OpenCL) and
> QAIRT (HTP v79/v81). BOTH end at HTP.
>
> The rule for this project: everything targets the NPU via HTP. AI Hub precompiled
> → QAIRT → HTP for nearly everything; Unsloth-quantized GGUF → llama.cpp/ggml → the
> same HTP for the rest. Nothing needs compiling. The voice layer is a separate
> plane (ORT/ONNX, in-process). For any backend claim, the QAIRT manual outranks
> this file — see `#QAIRT_main/` (seven sections) and Horizons-UI
> `knowledge/qairt-sdk/`.

## aesopd — The Bridge

WebSocket on 8765. Routes `llm.generate` to GGML (:8081) or NPU (:8080) based on `backend` field.

llama-server applies the GGUF's embedded chat template server-side.

## Recent History

| Commit | Change |
|--------|--------|
| `f28c303` | Version-controlled termux-helper; corrected NPU architecture |
| `08cb9f9` | Dropped Hexagon-from-Termux framing, named real HTP path |
| `49a958a` | Full accelerator offload (-ngl) + honest backend-ladder docs |
| `dc80402` | Q4_0 preference, mmap + q8_0 KV cache for tight-RAM survival |

## Credit

Mer0vin8ian Production — Cl0vis/Claude collab.