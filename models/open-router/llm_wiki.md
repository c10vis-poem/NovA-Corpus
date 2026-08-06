# models/open-router — LLM Wiki

## What this is

Registry for open-router models in the system. Tracks weight paths, quantization settings, and runtime manifests.

## Parameter taxonomy (per model)

- **Weights** — paths, INT8/ONNX quantization limits, tensor file allocations
- **Runtime** — zero-TTL execution flags, RAM allocations, thread bindings
- **Engine** — native JNI/C++ layers, VAD sensitivity (where applicable)
- **Communication** — IPC sockets, WebSocket bridges, API router endpoints

