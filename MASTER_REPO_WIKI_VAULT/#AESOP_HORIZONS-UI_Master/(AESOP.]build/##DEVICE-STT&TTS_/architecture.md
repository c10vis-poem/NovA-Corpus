# Architecture

## Runtime Topology

AESOP runs on Android via a two-layer stack:

```
┌─────────────────────────────────────────────────┐
│ Termux (Android host)                            │
│  bionic libc, Python 3.14                        │
│  ~/repos/aesop/voice-engine/ (this repo)          │
│  ~/models/ ──symlink──→ proot rootfs/models       │
│                                                    │
│  proot-distro login debian ─────────────────┐    │
│  ┌─────────────────────────────────────────┐│    │
│  │ Debian proot                             ││    │
│  │  glibc, Python 3.13                      ││    │
│  │                                          ││    │
│  │  sherpa-onnx 1.13.4                      ││    │
│  │  numpy, huggingface_hub, sounddevice     ││    │
│  │                                          ││    │
│  │  /root/models/                           ││    │
│  │    kokoro-multi-lang-v1.0/ (TTS)         ││    │
│  │    moonshine-base-en-int8/ (STT)         ││    │
│  │    silero-vad/ (VAD)                     ││    │
│  └─────────────────────────────────────────┘│    │
└─────────────────────────────────────────────────┘
```

**Why proot?** sherpa-onnx has no prebuilt wheels for Termux's bionic libc + Python 3.14. The Debian proot provides glibc + Python 3.13 where sherpa-onnx installs cleanly via pip. Model files are ABI-agnostic ONNX data — one copy is shared via symlink/bind-mount between the Termux home and the proot rootfs.

Source: `voice-engine/README.md` lines 43–65.

## Models

All three models are ONNX files downloaded from HuggingFace and stored under `~/models/` (symlinked to `/root/models/` inside the proot).

| Component | Model | Size | HuggingFace Source | Key Files |
|---|---|---|---|---|
| **TTS** | Kokoro multi-lang v1.0 | ~382 MB | `csukuangfj/kokoro-multi-lang-v1_0` | `model.onnx`, `voices.bin`, `tokens.txt`, `espeak-ng-data/`, `lexicon-us-en.txt` |
| **STT** | Moonshine base-en int8 | ~273 MB | `csukuangfj/sherpa-onnx-moonshine-base-en-int8` | `preprocess.onnx`, `encode.int8.onnx`, `uncached_decode.int8.onnx`, `cached_decode.int8.onnx`, `tokens.txt` |
| **VAD** | Silero VAD v5 | ~629 KB | `R4kSo1997/sherpa-onnx-silero-vad-v5` | `silero_vad.onnx` |

Model paths are resolved at runtime via the `AESOP_MODELS_DIR` environment variable (default `~/models`). Each script constructs subdirectory paths by joining the models directory with a fixed directory name (e.g., `kokoro-multi-lang-v1.0`).

Source: `voice-engine/README.md` lines 6–15; all scripts read `MODELS_DIR = os.environ.get("AESOP_MODELS_DIR", ...)`.

## Pipeline

The voice pipeline chains three stages. The core flow is **VAD → STT → (callback) → TTS → playback**.

### 1. Voice Activity Detection (VAD)

- **Model:** Silero VAD v5
- **Config:** threshold 0.5, min_silence_duration 500 ms, max_speech_duration 30 s, sample_rate 16000 Hz
- **Window:** 512 samples per window (Silero requirement)
- **API:** `sherpa_onnx.VoiceActivityDetector` — feed audio via `accept_waveform()`, segments come out via `vad.front` / `vad.pop()`
- **Segment data:** each segment has `.start` (sample offset) and `.samples` (list of float audio samples)

Source: `voice-engine/scripts/vad_test.py` lines 22–74; `live_voice_loop.py` lines 47–55.

### 2. Speech-to-Text (STT)

- **Model:** Moonshine base-en int8 (offline recognition)
- **Config:** greedy_search decoding, configurable thread count (default 2)
- **API:** `sherpa_onnx.OfflineRecognizer.from_moonshine()` — create a stream, `accept_waveform()`, then `decode_stream()`
- **Input:** float32 samples at native sample rate (resampling to 16 kHz happens in VAD, not STT)

Source: `voice-engine/scripts/stt_test.py` lines 27–53; `live_voice_loop.py` lines 58–68.

### 3. Text-to-Speech (TTS)

- **Model:** Kokoro multi-lang v1.0 (offline synthesis)
- **Config:** `length_scale` controls speed (1.0 = normal), `sid` selects voice
- **API:** `sherpa_onnx.OfflineTts` — `tts.generate(text=..., sid=..., speed=...)`
- **Output:** float32 samples at Kokoro's native sample rate; scripts convert to int16 WAV

Source: `voice-engine/scripts/tts_test.py` lines 27–58; `live_voice_loop.py` lines 71–85.

### Pipeline Variants

| Script | Pipeline | Audio I/O |
|---|---|---|
| `tts_test.py` | TTS only | Text input → WAV file output |
| `stt_test.py` | STT only | WAV file input → text output |
| `vad_test.py` | VAD only | WAV file input → segment list |
| `voice_loop.py` | TTS → STT (self-test) | File-based, no mic/speaker |
| `live_voice_loop.py` | Mic → VAD → STT → TTS → Speaker | Real-time via sounddevice + PulseAudio |

(Copied verbatim from Drive fast-copy pass — original file also present twice as "Copy of architecture.md"; see manifest.)
