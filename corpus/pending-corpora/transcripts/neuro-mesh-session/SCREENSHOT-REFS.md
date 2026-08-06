# neuro-mesh-session — Screenshot Reference Index

**Source:** "what is a hybridized agentic on device neuro mesh" — Google AI Mode session, August 2, 2026
**Document:** 150-page Gemini AI-generated build guide (NOT canon — AI prose responding to operator prompts)
**Status:** `pending-corpora` — operator quotes inside are canon-eligible; Gemini's prose is NOT
**Artifact anchor:** `40f4cad3-Gemini__direct_access_to_Google_AI.pdf` (Drive upload, this session)

Screenshots shared 2026-08-06. PNGs not yet saved as files — save manually to this folder in Termux.
Filenames to use when saved: `p025.png` through `p076.png` (page numbers visible in screenshots).

---

## Content captured from screenshots (AI-generated — NOT operator spec)

### Pages 25–28 · AESOP XI System Stack (ASCII diagram)

```
[ TIER 1: FRONTEND USER INTERFACE ]
  HORIZON UI (Native Kotlin/Java APK)
  └ The Interface Layer (XI): Captures ambient telemetry and human intent.
          ↓
[ TIER 2: COGNITIVE RATIONALIZATION CORE ]
  NOVUS AGENTI (MoE / MoA Model Architecture)
  └ The Brain: Handles multi-model orchestration, planning, and debating.
          ↓
[ TIER 3: HARDWARE-ABSTRACTED RUNTIME ]
  OMNI CLAW (Native Daemons, SDKs, & Scripts)
  └ The Body: Low-level system hooks, permissions, and tool execution.
          ↓
[ TIER 4: MEMORY FABRIC, AUDITING, & DATA FLYWHEEL ]
  AESOP XI CORE PROTOCOL
  └ The Synthesis Layer: Context routing, sandboxed security, and self-evolution.
```

**Note (Rule 6):** This tier numbering is Gemini's framing. Operator's confirmed architecture differs:
AESOP XI is the governing layer, not Tier 4. Horizons UI is the lifecycle foundation, not just "Tier 1 UI."

---

### Pages 27–28 · Comprehensive Execution Flow Lifecycle (ASCII diagram)

```
[ Human Intent / Telemetry ]
        |
        ▼
( HORIZON UI ) ──→ Triggers Ingress Intent
        |
        ▼
( NOVUS AGENTI ) ──→ Parses Plan ──→ Requests Memory Context via OMNI ROUTE
        |                                           |
        |                                           ▼
        |                          THE AESOP XI TRI-TAILED MEMORY
        |                          • Tier 1: mem0 (Real-time Habits)
        |                          • Tier 2: LLM Wiki / Open Wiki CLI / Obsidian
        |                          • Tier 3: notebooklm-py + Graphify
        ▼
( OMNI CLAW ) ←─────────────────────────────── (Injects Context Logs)
        |
        ▼
[ Native Daemon Tool Execution / Script Call ]
        |
        ▼
( RED AGENT AUDITOR ) ←── Intercepts Execution Traces & Evaluates against NOPE DATA BANK
        |
        ├→ [ REJECT / RE-ROUTE ] ──→ Returns back to Novus Agenti for Self-Correction
        |
        └→ [ APPROVE ]
                ├→ [ COMMIT LOCAL ] ──→ Appends to Open Wiki CLI Vault Network
                └→ [ STREAM CLOUD ] ──→ Pushes .jsonl to GCP Storage Bucket
                                                |
                                                ▼
                                [ RECURSIVE KAG FINE-TUNING LOOP ]
```

---

### Pages 28 · Horizons XI Main System Dashboard Mockup (TUI concept)

```
| HORIZON XI MAIN SYSTEM DASHBOARD                              [ ⚙ ] |
| SYSTEM STATUS: ACTIVE | MESH NODES: [ PHONE_01 ] [ DEV_BOARD_04 ]   |
|                                                                       |
|  NOVUS AGENTI: MOE/MOA COGNITIVE CORE                           |    |
|  Heartbeat: ACTIVE [ 840ms Loop Latency ]                       |    |
|  CURRENT TASK: Processing automated file compilation routine.   |    |
|  ● [████████████      ] DEBATE LAYER: Agent_01 <–→ Agent_02    |    |
|                                                                       |
|  PID 4110: [OB1_SERVER_CON] Syncing Postgres Vector Spaces      |    |
|  ⚙ PERMISSIONS: ROOT_GRANTED | API_GATEWAY: CONNECTED           |    |
|                                                                       |
|  🛡 ADVERSARIAL RED AUDITOR STATE                                |    |
|  STATUS: 🛡 SCREENING TRACES                                    |    |
|  ├─ Log Line #142: Terminal script syntax check...  [ PASS ✓ ]  |    |
|  ├─ Log Line #143: Checking payload vs NOPE DATA BANK [ PASS ✓ ]|    |
|  └─ Output Status: STREAMING DATASTREAM TO GCP BUCKET [ SYNC ↻ ]|    |
|                                                                       |
|  🔄 AESOP XI TRI-TAILED MEMORY FLOW                             |    |
|  🧭 OMNI ROUTE DESTINATION ──→ [ TIER 2: OPEN WIKI CLI VAULT ]  |    |
|  🍊 MEMO CACHE: 42 Active Keys                                  |    |
|  📝 WIKI SYNC: 14 .md mutations pending P2P cluster handshake   |    |
|  📔 NOTEBOOKLM-PY: 3 Remote Context Pools Loaded                |    |
|                                                                       |
| [ ⏸ PAUSE MESH ]    [ 🛡 MANUAL AUDIT MODE ]    [ ⚡ FORCE SYNC ] |
```

**Note (Rule 7):** This is a Gemini-generated mockup concept, not a build spec. The visual design
language (bordered panels, status indicators, monospace layout) is reference material only.

---

### Pages 34 · Zero-Trust Operational Manifesto

Gemini's framing — structure useful, claims not canon. Key rules Gemini proposed:
1. **Unchecked Writes Prohibited** — agent shall not claim a file has been created unless source payload is compiled, written, and verified via structural schema checkers
2. **Decoupled Isolation (One Agent, One Repo)** — each layer compartmentalized; blind to interface layouts or Red Agent eval rules of other layers
3. **No Cross-Contamination** — no specialized model shares a memory layer or skill registry with another unless mediated explicitly by Omni Route

---

### Pages 53 · Master Repository & Data Directory Blueprint (Gemini's layout)

```
master_build-guide/
├── horizons-ui/          README.md · skill_manifest.json · llm_wiki.md · src/
├── aesop-xi-memory/      README.md · skill_manifest.json · llm_wiki.md · ob1-backend/ · omni-route/
├── termux-environment/   README.md · skill_manifest.json · llm_wiki.md · open-wiki-cli/
├── file-management-system/ README.md · skill_manifest.json · llm_wiki.md · target-docs/
├── github-ci-cd/         README.md · skill_manifest.json · llm_wiki.md · workflows/
├── skill-building-protocol/ README.md
├── red-agent-auditor/    README.md · skill_manifest.json · llm_wiki.md · security-perimeter/ · nope_data_bank.json
├── node-beta-jetson/     README.md · skill_manifest.json · llm_wiki.md
├── node-gamma-rubik-pi/  README.md · skill_manifest.json · llm_wiki.md
└── global-documentation-vault/
    ├── unsloth-docs/
    ├── qairt-docs/
    ├── google-dev-docs/
    ├── llama-docs/
    └── master_blueprint.txt
```

**Note:** This is Gemini's proposed layout. Operator's confirmed layout is `modu14r_inc./` — see
`/workspace/obsidian-master_wiki/` for the actual implementation.

---

### Pages 68–76 · Repository Catalog & Agent Scopes (Gemini's proposal)

| Repo slug | Agent Role | Zero-Trust Boundary |
|---|---|---|
| horizons-ui-v1.2 | Frontend XI Construction Engineer | Blind to backend DB / Red Agent code |
| termux-building-skills | Local Environment & Terminal Optimization | Blind to Android APK steps / cloud DB |
| file-management-and-skills | System Librarian & Data Schema Architect | Does NOT write operational runtime code |
| obsidian-vault-new | Knowledge Graph Relational Synchronizer | Blind to hardware drivers / cloud compile |
| aesop-xi-protocol | Memory Fabric & Routing Orchestrator | — |
| nova-claw-runtime | Hardware-Abstracted Execution Engine | — |
| red-agent-auditor | Out-of-Band Security Sentinel | — |
| node-beta-jetson | Bare-Metal Infrastructure Provisioning | CUDA core allocations, NVMe benchmarks |
| node-gamma-rubik-pi | Display Environment Server Layers | Dual-monitor scaling, window mapping |

---

### Pages 73–76 · Skill Onboarding Schema (JSON)

Gemini proposed a `skill_onboarding_schema.json` at `skill-construction-factory/`:
```json
{
  "$schema": "https://json-schema.org",
  "title": "AESOP_XI_Priority_Skill_Onboarding_Template",
  "properties": {
    "skill_identity": {
      "technical_identifier": { "type": "string" },
      "primary_reference_document": { "type": "string", "enum": ["QAIRT_SDK_MANUAL", "ANDROID_..."] }
    },
    "hardware_execution_routing": {
      "npu_offload_required": { "type": "boolean" },
      "target_pathway_gateway": { "type": "string", "enum": ["QAIRT_MODELPATH_HTP", "GGML_KOT..."] }
    },
    "runtime_permissions_bounds": {
      "requires_device_shell_access": { "type": "boolean" },
      "requires_screen_vision_allowance": { "type": "boolean" },
      "boosted_power_state_required": { "type": "boolean" }
    }
  }
}
```

---

### Pages 76 · Master Specification Index (NODE hardware specs)

```
AESOP XI MASTER COMPUTATIONAL ENVIRONMENT SPECIFICATION INDEX
CLASSIFICATION: Heterogeneous Edge-Computing Mesh with Asymmetric Memory Paths
ROOT ANCHOR   : Horizons UI Native Device Kernel Execution Engine (Node Alpha)
REVISION CODE : v1.2-Ground-Truth
STATUS        : PRIORITY_01_LOCKED_MANIFEST

NODE_ALPHA (Local Controller): Moto RAZR Ultra 2025
  SoC / NPU Processing Core : Snapdragon 8 Elite [Gen 4] | Hexagon NPU v.79
  Compute Resource Profiling : 40+ INT8 TOPs Hardware Acceleration Engine
  Physical System Memory     : 16 GB Total RAM | Dynamic Weight Bounds: 8.0 - 11.5 GB
  Primary Software System    : Horizons UI Native App (Kotlin/Java APK Layer)
  Audio Ingress / Egress     : Moonshine ONNX [STT] + Kokoro 82m / Sherpa [TTS]
  Local Hardware Gateway     : Qualcomm QAIRT ModelPath / HTP SDK Bare-Metal

NODE_BETA (Persistent Core): Nvidia Jetson Orin Nano Super 8GB

NODE_GAMMA (Display Server): Rubik Pi 3 [Dragonwing]
  Processing Infrastructure : Thundercomm / Qualcomm Systems-on-Chip (SoC)
  Compute Resource Profiling : 14+ TOPs Base Processing Performance
  Local Workstation Setup    : Dual-Monitor Hardware Video Ribbon Display Engine

LOCAL MESH NETWORK ROUTING : Ad-Hoc Peer-to-Peer Topology Linked over Tailscale
```

---

## Master Validation Checksums Registry (Gemini-generated — structure only)

| DIRHASH | VALIDATION |
|---|---|
| horizons-ui-v1.2 | REQUIRED_FOR_NPU_BOOTSTRAP |
| termux-building-skills | REPO_SANITY_SYSTEMS_ACTIVE |
| file-management-and-skills | CANONICAL_KNOWLEDGE_LOCKED |
| obsidian-vault-new | MARKDOWN_GRAPH_VERIFIED |
| nova-claw-runtime | SERVICE_DAEMON_PERSISTENT |
| red-agent-auditor | AIR_GAPPED_OUT_OF_BAND_ISOLATION |
| node-beta-jetson | HEADLESS_CUDA_KERNEL_READY |
| node-gamma-rubik-pi | DISPLAY_SERVER_RIBBON_MAPPED |
