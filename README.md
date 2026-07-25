# OBSIDIAN-Master_Wiki

Obsidian vault — synced to GitHub.

## Structure

Vault files organized by project. Push from Termux:

```bash
cd ~/OBSIDIAN-Master_Wiki
git add -A && git commit -m "vault sync" && git push
```

## Setup (Termux)

```bash
# First time — clone the repo into your Obsidian vault location
termux-setup-storage
cd ~/storage/shared
git clone https://github.com/c10vis-poem/OBSIDIAN-Master_Wiki.git

# Point Obsidian to this folder as a vault
# OR symlink it into your existing vault:
# ln -s ~/storage/shared/OBSIDIAN-Master_Wiki ~/storage/shared/ObsidianVault/OBSIDIAN-Master_Wiki
```

## Git sync from Termux

```bash
# Quick sync alias — add to ~/.bashrc
alias vault-sync='cd ~/storage/shared/OBSIDIAN-Master_Wiki && git add -A && git commit -m "vault $(date +%F)" && git push'
```
