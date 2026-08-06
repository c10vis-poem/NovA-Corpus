# models — LLM Wiki

## What this is

Central model registry. All models in the system are catalogued here by provider, with their weights paths, quantization settings, and runtime manifests.

## Design rule

Backend is always swappable — no hardcoded inference paths. Runtime manifests point to the currently active backend; switching models means pointing to a different manifest, not changing app code.

## Providers

- `google/` — Gemini, Gemma
- `meta-llama/` — Llama variants
- `open-router/` — cloud-routed (Hydra rotation for MoA/MoE)
- `anthropic/` — Claude variants
