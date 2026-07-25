# OBSIDIAN Master Wiki

> **Cl0vis x Mer0vin6ian** — the central knowledge vault.

An Obsidian-compatible markdown vault that syncs across four surfaces:

| Surface | App | Path |
|---------|-----|------|
| **Phone** (Razr Ultra 2025) | Markor / Obsidian | `/storage/emulated/0/Documents/OBSIDIAN-Master_Wiki/` |
| **Google Drive** | Drive sync | `My Drive/OBSIDIAN-Master_Wiki/` |
| **GitHub** | git | `c10vis-poem/OBSIDIAN-Master_Wiki` |
| **Claude Code** | session clone | skills loaded from `skills/` |

## Vault Structure

```
OBSIDIAN-Master_Wiki/
├── .obsidian/                 ← Obsidian config (synced)
│   └── app.json
├── README.md                  ← this file
├── CLAUDE.md                  ← Claude Code project instructions
├── skills/                    ← custom Claude Code skills (daily-updated)
│   ├── termux-mobile-dev/
│   │   └── SKILL.md
│   ├── project-memory/
│   │   └── SKILL.md
│   └── horizons-wiki/
│       └── SKILL.md
├── daily-updates/             ← timestamped skill update log
│   └── YYYY-MM-DD.md
├── projects/                  ← per-project knowledge notes
│   ├── novus-agenti.md
│   ├── horizons-home-grid.md
│   └── claude-skills.md
├── devices/                   ← device inventory + setup notes
│   └── razr-ultra-2025.md
├── sync/                      ← sync setup guides
│   └── SYNC-SETUP.md
└── templates/                 ← Obsidian templates
    └── daily-update.md
```

## Custom Claude Code Skills

These three skills are maintained here and loaded by Claude Code sessions.
They get updated every day, just like platform skills.

| Skill | What It Does |
|-------|-------------|
| **termux-mobile-dev** | On-device Termux dev env — VNC, Matrix terminal, OpenClaude agents |
| **project-memory** | Knowledge corpus retrieval from the `knowledge/` folder in Novus-Agenti |
| **horizons-wiki** | Architecture-of-record bundle for the Horizons / Omni Claw app |

## Sync Flow

```
Phone (Markor/Obsidian) ←→ Google Drive ←→ GitHub repo
                                ↑
                          Claude Code sessions
                          (read + update skills,
                           push back to GitHub)
```

On-device: Markor and Obsidian both read/write the same folder.
Google Drive: FolderSync or Autosync mirrors the folder to Drive.
GitHub: `git pull`/`git push` from Termux keeps the repo in sync.
Claude Code: clones the repo each session, updates skills, pushes.

## Quick Sync from Termux

```bash
cd ~/storage/shared/OBSIDIAN-Master_Wiki
git add -A
git commit -m "vault $(date +%F)"
git push
```

Alias for `.bashrc` / `.zshrc`:
```bash
alias vault-sync='cd ~/storage/shared/OBSIDIAN-Master_Wiki && git add -A && git commit -m "vault $(date +%F)" && git push'
```

## Setup (Termux — first time)

```bash
termux-setup-storage
cd ~/storage/shared
git clone https://github.com/c10vis-poem/OBSIDIAN-Master_Wiki.git
```

Then point Obsidian and/or Markor at this folder as a vault.

---

**Last Updated:** 2026-07-25
