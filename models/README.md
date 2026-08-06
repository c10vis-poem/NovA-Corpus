# models

Model registry, organized by provider. Each sub-folder tracks weights, quantization configs, and runtime manifests for that provider's models in the system.

## Sub-folders

| Folder | Provider |
|---|---|
| `google/` | Google — Gemini, Gemma variants |
| `meta-llama/` | Meta — Llama variants |
| `open-router/` | OpenRouter — cloud-routed models |
| `anthropic/` | Anthropic — Claude variants |

## Parameter taxonomy

Every model entry follows the four-layer parameter packet:

1. **Weights** — paths, INT8/ONNX quantization limits, tensor file allocations
2. **Runtime** — zero-TTL execution flags, RAM allocations, thread bindings
3. **Engine** — native JNI/C++ layers (`libsherpa-onnx-jni.so`, `libllama.so`), VAD sensitivity
4. **Communication** — IPC sockets, WebSocket bridges, API router endpoints

Design constraint: never hardcode inference backend — keep swappable.
