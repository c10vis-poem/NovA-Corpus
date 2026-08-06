# DEVICE INVENTORY — NODE_ALPHA (Razr Ultra)

> **Artifact anchor:** operator file-manager screenshots, 2026-08-06 11:37–11:42 local.
> Four captures: `LeGRAND_REPOSITORY/MODELS`, `LeGRAND_REPOSITORY/HARNESS`,
> `Internal storage/Download`, `AESOP_HORIZONS.main/GOOGLE_DEV`.
> Supersedes `knowledge/device-inventory/DEVICE-INVENTORY.md` (2026-07-13), which was
> flagged "re-verify before trusting exact versions/sizes."

**Status:** `built-verified` — this is a direct read of the device filesystem, not a
design doc. Sizes and dates are as displayed by the Android file manager.

---

## 0 · Guiding principle

This document records **what is physically on the device**, nothing else. It does not
say what runs, what works, or what is wired into the app. Presence of a file is
presence of a file. Runtime state belongs in the build ledger, not here.

Per **Rule 6 (Designed ≠ Built)**: a model sitting in `MODELS/` is `present`, not
`working`. Per **Rule 7 (Metaphor ≠ Implementation)**: nothing in this inventory is a
constraint on what the loader may accept.

---

## 1 · On-device directory map

The operator's on-device root for this project is **`LeGRAND_REPOSITORY/`** — the
physical counterpart to `modu14r_inc./` in the corpus. Two sibling trees carry the
research material.

```
Internal storage/
├── LeGRAND_REPOSITORY/          ← project root on device
│   ├── MODELS/                  ← GGUF + GenieX model weights (~32 GB)
│   └── HARNESS/                 ← runtimes, tokenizers, compiled binaries (~1.1 GB)
├── AESOP_HORIZONS.main/
│   └── GOOGLE _DEV/             ← LiteRT / Google AI Edge research (~95 GB incl. tar.gz)
└── Download/                    ← staging + duplicates + source PDFs
```

---

## 2 · `LeGRAND_REPOSITORY/MODELS/` — model weights

Captured 2026-08-06 11:37. **8 files · ~32.0 GB total.**

| File | Size | Date | Family | Format |
|---|---:|---|---|---|
| `Qwen3.5-9B-Q4_0.gguf` | 5.38 GB | Jul 24 | Qwen3.5 9B | GGUF Q4_0 |
| `gemma-4-12B-it-qat-UD-Q4_K_…` | 6.72 GB | Jul 24 | Gemma 4 12B | GGUF UD-Q4_K |
| `gemma-4-12b-it-qat-q4_0.gguf` | 6.98 GB | Jul 24 | Gemma 4 12B | GGUF Q4_0 |
| `gemma-4-E4B_q4_0-it.gguf` | 5.15 GB | Jul 23 | Gemma 4 E4B | GGUF Q4_0 |
| `gemma-4-E2B_q4_0-it.gguf` | 3.35 GB | Jul 23 | Gemma 4 E2B | GGUF Q4_0 |
| `qwen3_vl_4b_instruct-geniex_qa…` | 3.04 GB | Jul 23 | Qwen3-VL 4B | **GenieX / QNN** |
| `Qwen3.5-2B-Q4_0.gguf` | 1.21 GB | Jul 16 | Qwen3.5 2B | GGUF Q4_0 |
| `mtp-gemma-4-E2B-it-BF16.gguf` | 170 MB | Jul 12 | Gemma 4 E2B | **MTP heads only** |

### Notes on individual entries

- **`qwen3_vl_4b_instruct-geniex_qa…`** is the only non-GGUF weight in this folder. The
  `geniex` marker means it was compiled for the Qualcomm AI Engine, not llama.cpp. This
  is a **second inference path** alongside the ORT/llama route and is not documented
  anywhere in the corpus yet. → open question §7.1
- **`mtp-gemma-4-E2B-it-BF16.gguf`** at 170 MB is far too small to be a full E2B model.
  Multi-token-prediction heads only — a speculative-decoding accessory, not a standalone
  model. Do not load it as a primary.
- **Two Gemma 12B quants** (6.72 GB UD-Q4_K + 6.98 GB Q4_0) are near-identical in size
  and neither fits comfortably alongside the OS on a 16 GB device. One is redundant.
- **`Qwen3.5-9B-Q4_0.gguf`** is duplicated in `Download/` (see §4). ~5.4 GB recoverable.

### RAM fit against 16 GB

Android reserves roughly 4–6 GB for OS + system services on this device. Practical
headroom for a model process is **~9–10 GB**, and Horizons UI + voice layer take a
further slice.

| Model | Weights | Verdict |
|---|---:|---|
| Gemma 4 12B (either quant) | ~6.7–7.0 GB | Tight — no KV headroom for long context |
| Qwen3.5 9B Q4_0 | 5.38 GB | **Workable primary** |
| Gemma 4 E4B | 5.15 GB | Workable |
| Gemma 4 E2B | 3.35 GB | Comfortable |
| Qwen3-VL 4B (GenieX) | 3.04 GB | Comfortable — NPU path |
| Qwen3.5 2B | 1.21 GB | Comfortable — fast path |
| Granite 4.0 Micro (in `Download/`) | 1.86 GB | Comfortable — **not yet in MODELS/** |

---

## 3 · `LeGRAND_REPOSITORY/HARNESS/` — runtimes and tooling

Captured 2026-08-06 11:38. All entries dated 7 days prior (~Jul 30). **~1.1 GB total.**

| Entry | Size | Kind | Purpose |
|---|---:|---|---|
| `Llama.server/` | dir | cloned repo | llama.cpp server |
| `QNN-QAIRT/` | dir | cloned repo | Qualcomm AI Runtime toolchain |
| `hybrid_llama_qnn.pte` | 0.93 GB | **ExecuTorch** | Pre-compiled Llama for QNN HTP |
| `geniex-bench-android-arm64-v…` | 89.96 MB | binary | GenieX benchmark harness |
| `qnn_llama_runner.zip` | 35.22 MB | archive | QNN Llama runner |
| `tokenizer.json` | 11.42 MB | tokenizer | — |
| `merges.txt` | 1.67 MB | tokenizer | BPE merges |
| `tokenizer_config.json` | 5.40 kB | tokenizer | — |
| `added_tokens.json` | 707 B | tokenizer | — |
| `special_tokens_map.json` | 613 B | tokenizer | — |
| `Qualcomm AI Runtime (QAIRT) O…` | 1.81 MB | doc | QAIRT reference |
| `snapdragon-npu-llm-main.zip` | 28.12 kB | archive | NPU LLM reference code |
| `nexa.manifest` | 85 B | manifest | **Nexa-era leftover** |
| `novus-boot.log` | 4.01 kB | log | Boot breadcrumb |

### Notes

- **`hybrid_llama_qnn.pte` (930 MB)** is the significant find. A `.pte` is an ExecuTorch
  program — a *third* inference path, distinct from both llama.cpp/GGUF and GenieX/QNN.
  "hybrid" in Qualcomm's ExecuTorch examples means a prefill graph and a decode graph
  compiled together for the HTP. Nothing in the corpus documents this path.
  → open question §7.1
- **`nexa.manifest`** is a leftover from the Nexa SDK era, which `Horizons-UI/CLAUDE.md`
  lists as superseded/dead. 85 bytes — harmless, but it is stale.
- The loose tokenizer files at the HARNESS root belong to *some* model; which one is not
  determinable from the listing. `merges.txt` + `added_tokens.json` is a BPE layout,
  consistent with Qwen rather than Gemma.
- **`novus-boot.log`** is the only runtime trace in this folder. The app's own diagnostics
  live at `/sdcard/Android/data/com.horizons/files/diag/` — separate location.

---

## 4 · `Internal storage/Download/` — staging and duplicates

Captured 2026-08-06 11:39. Mixed staging area; several items are recoverable space.

| File | Size | Date | Disposition |
|---|---:|---|---|
| `Qwen3.5-9B-Q4_0.gguf` | 5.38 GB | 5 days ago | **DUPLICATE** of `MODELS/` copy — delete |
| `granite-4.0-h-micro-Q4_0.gguf` | 1.86 GB | 5 days ago | **MOVE to `MODELS/`** — not yet filed |
| `what is a hybridized agentic on d…` | 106 MB | 3 days ago | Neuro mesh session PDF — the canon source |
| `.trashed-1788414742-what is a h…` | 106 MB | 27 days left | Trashed copy |
| `.trashed-1788414742-what is a h…` | 106 MB | 27 days left | Trashed copy |
| `.trashed-1788414742-what is a h…` | 106 MB | 27 days left | Trashed copy |
| `.trashed-1788414742-what is a h…` | 104 MB | 27 days left | Trashed copy |
| `Granite-4.0-Micro - Qualcomm …` | 1.92 MB | 5 days ago | Qualcomm model card |
| `m qualcomm_Qwen3.5-0.8B · Me…` | 294 kB | 5 days ago | Qualcomm model card |
| `Duplicate from qualcomm_Qwen…` | 1.32 MB | 5 days ago | Model card duplicate |

### Recoverable space

| Action | Frees |
|---|---:|
| Delete duplicate `Qwen3.5-9B-Q4_0.gguf` | **5.38 GB** |
| Empty 4 trashed neuro-mesh PDFs | **422 MB** |
| **Total** | **~5.8 GB** |

The four Qualcomm model cards (Granite-4.0-Micro, Qwen3.5-0.8B) indicate the operator was
evaluating Qualcomm's **pre-optimized AI Hub** builds — models already compiled for the
Hexagon NPU rather than converted locally.

---

## 5 · `AESOP_HORIZONS.main/GOOGLE _DEV/` — LiteRT research

Captured 2026-08-06 11:42. All entries dated 7 days prior. Research corpus, not runtime.

| File | Size | Kind |
|---|---:|---|
| `google-cloud-cli-linux-arm.tar.gz` | 61.13 MB | **ARM64 gcloud CLI** — for Termux/Jetson |
| `model.safetensors` | 561 MB | Unidentified weights — **needs identification** |
| `Automated Build Android Using …` | 5.55 MB | saved page |
| `Google AI Edge _ Google for De…` | 3.77 MB | saved page |
| `generative-ai_gemini_rag-engin…` | 2.97 MB | saved page |
| `LiteRT_litert_kotlin_src_main_kot…` | 2.36 MB | source snapshot |
| `litert-samples_compiled_model_…` | 2.20 MB | source snapshot |
| `litert-samples_compiled_model_…` | 2.18 MB | source snapshot (near-dupe) |
| `multi-agent.html` | 1.72 MB | saved page |
| `LiteRT for Android _ Google AI …` | 1.71 MB | saved page |
| `LiteRT CompiledModel Kotlin API…` | 1.70 MB | saved page |
| `Use Prebuilt C++ library from Lit…` | 1.70 MB | saved page |
| `Run LLMs using LiteRT-LM _ Go…` | 1.74 MB | saved page |
| `Installing LiteRT CLI _ Google AI…` | 1.68 MB | saved page |
| `Scaling LLM Test-Time Compute …` | 1.15 MB | paper |
| `Google.mht` / `Google Image Result*.mht` | 501–586 kB ×4 | saved pages |
| `ai_tracking_sources (Markor).pdf` | 216 kB | operator notes |
| `intro_gemini_3_5_flash_lite.ipyn…` | 58.40 kB | notebook |
| `rag_engine_vector_search.ipynb…` | 24.30 kB | notebook |
| `gitattributes.txt` | 1.63 kB | — |

### Notes

- **`model.safetensors` (561 MB)** is unlabelled. Size is consistent with a small vision
  or embedding model — possibly the LiteHRNet keypoint model, possibly an embedding model
  for the RAG work in this folder. **Cannot be identified from the listing alone.**
  → open question §7.2
- **`google-cloud-cli-linux-arm.tar.gz`** is the ARM64 gcloud CLI. This is the tool for
  the GCP-bucket leg of the recursive-KAG loop, staged but not documented.
- LiteRT appears throughout this folder. `Horizons-UI/CLAUDE.md` lists **LiteRT/LiteRT-LM
  as superseded for the Qwen3.5-9B path** — replaced by the ort_engine daemon. That
  supersession was scoped to one model path; this research folder is consistent with
  LiteRT still being evaluated for other paths. Recorded, not reconciled.

---

## 6 · Cross-reference — HuggingFace vs on-device

The operator's HF account (`Mer0vin8ian`, "Clovis Poem") carries 15 model repos. Mapping
those against what is physically on the device:

| HF repo | On device? | Location |
|---|---|---|
| `Qwen3.5-9B-GGUF` | ✅ | `MODELS/Qwen3.5-9B-Q4_0.gguf` |
| `Qwen3.5-9B` | — | source weights, HF only |
| `Qwen3.5-0.8B` | — | model card in `Download/` only |
| `gemma-4-12B-it-qat-GGUF` | ✅ | `MODELS/` (both quants) |
| `gemma-4-12B-it-qat-q4_0-gguf` | ✅ | `MODELS/gemma-4-12b-it-qat-q4_0.gguf` |
| `Gemma-4-E4B-it` | ✅ | `MODELS/gemma-4-E4B_q4_0-it.gguf` |
| `gemma-4-E2B-it-ONNX` | — | ONNX variant, HF only |
| `Granite-4.0-Micro` | ✅ | `Download/granite-4.0-h-micro-Q4_0.gguf` |
| `Phi-4-Mini-Instruct` | ❌ | **not on device** |
| `moonshine-streaming-small-onnx` | ? | ships inside APK assets, not visible here |
| `moonshine-streaming-small` | ? | as above |
| `sherpa-onnx-whisper-base.en` | ? | as above |
| `kokoro-en-v0_19` | ? | as above |
| `Clovis-LiteHRNet` | ? | possibly the unlabelled `model.safetensors` |
| `hexagon-sdk` *(private)* | ✅ | `HARNESS/QNN-QAIRT/` |

**Not on device but in `MODELS/`:** `Qwen3.5-2B-Q4_0.gguf` and
`qwen3_vl_4b_instruct-geniex_qa…` have no corresponding HF repo — sourced elsewhere or
converted locally without upload.

---

## 7 · Open questions

### 7.1 · Three inference paths coexist, only one is documented

| Path | Artifact on device | Corpus coverage |
|---|---|---|
| llama.cpp / GGUF | `MODELS/*.gguf` + `HARNESS/Llama.server/` | documented |
| GenieX / QNN | `qwen3_vl_4b_instruct-geniex_qa…` + `geniex-bench-…` | `wiki/GENIEX-DAEMON-PLAN.md` — unread |
| **ExecuTorch / QNN HTP** | `hybrid_llama_qnn.pte` (930 MB) | **nothing** |

Which of these is the intended production path for NODE_ALPHA? The `.pte` is the largest
single runtime artifact on the device and has no documentation at all. **Operator call.**

### 7.2 · Unidentified `model.safetensors` (561 MB)

Sitting in `GOOGLE _DEV/` with no label. Needs one command on device to resolve:
```
cd /sdcard/AESOP_HORIZONS.main/GOOGLE\ _DEV && ls -la | grep -i -E 'config|json'
```
A sibling `config.json` names the architecture.

### 7.3 · Which model do the loose HARNESS tokenizers belong to?

`merges.txt` + `added_tokens.json` at the HARNESS root is a BPE layout, consistent with
Qwen. Confirm against `tokenizer_config.json`.

### 7.4 · Two Gemma 12B quants — is one redundant?

6.72 GB UD-Q4_K and 6.98 GB Q4_0. Neither fits with comfortable KV headroom on 16 GB.
Dropping one frees ~7 GB.

---

## 8 · Status ledger

| Item | State |
|---|---|
| `MODELS/` — 8 weight files present, ~32 GB | `built-verified` |
| `HARNESS/` — llama.cpp + QNN-QAIRT cloned | `built-verified` |
| `HARNESS/hybrid_llama_qnn.pte` present | `built-verified` |
| `HARNESS/hybrid_llama_qnn.pte` — *runs* | `absent` — no evidence either way |
| GenieX benchmark binary present | `built-verified` |
| GenieX path — *wired into app* | `designed-only` — `GENIEX-DAEMON-PLAN.md` unread |
| ARM64 gcloud CLI staged | `built-verified` |
| GCP bucket leg of KAG loop | `designed-only` |
| Granite 4.0 Micro downloaded | `built-verified` — but unfiled, in `Download/` |
| Phi-4-Mini on device | `absent` |
| `model.safetensors` identity | **unknown** |
| Voice-layer models on device filesystem | **unknown** — ship in APK assets, not visible here |
| Duplicate Qwen 9B GGUF (5.38 GB) | `built-verified` — recoverable |
| 4 trashed neuro-mesh PDFs (422 MB) | `built-verified` — recoverable |

---

## 9 · Recommended device actions

Short, paste-able, per the Termux rules (`< ~50 chars` where possible).

```
cd /sdcard/Download
rm Qwen3.5-9B-Q4_0.gguf
```
```
mv granite-4.0-h-micro-Q4_0.gguf ../LeGRAND_REPOSITORY/MODELS/
```
```
cd /sdcard/AESOP_HORIZONS.main/GOOGLE\ _DEV
ls | grep -i json
```
```
cd /sdcard/Android/data/com.horizons/files/diag
tail -40 crash.log
```

The last one is still the open item from session 20 — the first-crash trigger. Stack
trace present means JVM exception; empty but app died means killed from outside (LMK/FGS)
and no trace will ever appear.
