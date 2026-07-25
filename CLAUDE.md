# CLAUDE.md — OBSIDIAN Master Wiki

> Central knowledge vault and custom skill registry for the Novus Agenti /
> Omni Claw ecosystem. Cl0vis x Mer0vin6ian production.

## What This Repo Is

The **master wiki** — an Obsidian-format knowledge base that owns the
canonical copies of all three custom-built skills and serves as the
cross-project knowledge hub. Skills here are updated daily, just like
platform skills in `c10vis-poem/claude-skills`.

## Daily Update Protocol

Every session touching this repo MUST:

1. **Update skill content** — review each skill's SKILL.md in `skills/`,
   refresh any stale information, add new learnings from the day's work.
2. **Log the update** — write or append to `daily-updates/YYYY-MM-DD.md`
   with what changed and why.
3. **Sync outward** — copy the updated SKILL.md files to their in-repo
   locations (`Novus-Agenti/skills/<name>/SKILL.md`).
4. **Push everything** — commit and push to all affected repos.

## Skills Inventory

### 1. termux-mobile-dev
**Location:** `skills/termux-mobile-dev/SKILL.md`
**Purpose:** Full reference for the on-device Termux mobile dev environment.
Covers VNC (TigerVNC + XFCE on the phone, AVNC on Samsung Tab S9 FE+),
the Matrix terminal (zsh + tmux + cmatrix + Termux:Float), and on-device
coding agents (OpenClaude + DeepSeek V4 via OpenRouter).
**Target device:** Motorola Razr Ultra 2025 (SM8750, 16GB, Hexagon HTP v79).

### 2. project-memory
**Location:** `skills/project-memory/SKILL.md`
**Purpose:** The project's actual memory layer — retrieval interface to the
hand-distilled `knowledge/` corpus in Novus-Agenti. Two-tier model:
always-read core definition + on-demand retrieval via JSONL grep.

### 3. horizons-wiki
**Location:** `skills/horizons-wiki/SKILL.md`
**Purpose:** Architecture-of-record bundle for the Novus Agenti / Omni Claw
app. Packages CLAUDE.md + daemon reference + NPU runtime paths as a single
cacheable context bundle for sub-agents.

## Repo Policy

- **This repo is the source of truth** for custom skill content.
- Never hardcode tokens or secrets — this is a public repo.
- Skills flow FROM here TO source repos, not the other way around.
- Every push includes a daily-update log entry.

## Linked Repos

| Repo | Role |
|------|------|
| `c10vis-poem/Novus-Agenti` | Horizons app — skills also live at `skills/` there |
| `c10vis-poem/Horizon-s-home-grid` | Home automation grid |
| `c10vis-poem/claude-skills` | Platform skills library (246 skills) |
| `c10vis-poem/aesop` | Aesop project |
| `c10vis-poem/termux-packages` | Termux package configs |

## Hard Rules

- Never push `main` without explicit user permission
- Never hardcode tokens or secrets
- Daily updates are non-negotiable — if you touch a skill, log the change
- Skills here are the canonical copy; sync outward after every update
