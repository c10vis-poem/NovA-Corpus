# Sync Setup — OBSIDIAN Master Wiki

Three-way sync between phone, Google Drive, and GitHub.

## On-Device Setup (Razr Ultra 2025)

### Vault Location
```
/storage/emulated/0/Documents/OBSIDIAN-Master_Wiki/
```

Both Markor and Obsidian point at this same folder.

### Markor
1. Open Markor → Settings → General → Notebook
2. Set to `/storage/emulated/0/Documents/OBSIDIAN-Master_Wiki/`
3. Markor reads/writes plain markdown — fully compatible with Obsidian format

### Obsidian
1. Open Obsidian → Open folder as vault
2. Point to `/storage/emulated/0/Documents/OBSIDIAN-Master_Wiki/`
3. The `.obsidian/` config folder syncs with the vault

### Google Drive Sync
Use **FolderSync** or **Autosync for Google Drive** (F-Droid / Play Store):
```
Local:  /storage/emulated/0/Documents/OBSIDIAN-Master_Wiki/
Remote: My Drive/OBSIDIAN-Master_Wiki/
Sync:   Two-way, 15-minute interval
```

Exclude from sync (save bandwidth):
- `.git/` (handled by git, not Drive)
- `.obsidian/workspace.json` (device-specific UI state)

### GitHub Sync (Termux)
```bash
W=~/storage/shared/Documents/OBSIDIAN-Master_Wiki
cd $W
git pull origin main
# edit...
git add -A
git commit -m "update: daily skill refresh"
git push origin main
```

Keep it short — phone-paste friendly.

## Claude Code Sessions

Claude Code clones the repo fresh each session. The daily update workflow:
1. Session clones `c10vis-poem/OBSIDIAN-Master_Wiki`
2. Reviews and updates skills in `skills/`
3. Logs changes in `daily-updates/YYYY-MM-DD.md`
4. Pushes to GitHub
5. Syncs updated skills to `Novus-Agenti/skills/` and pushes there too

## Conflict Resolution

- **Markor vs Obsidian**: both write plain markdown, no conflicts if you
  don't edit the same file simultaneously in both apps.
- **Drive vs GitHub**: Drive sync is for the vault content (notes, skills).
  Git is for version history. If they conflict, git wins — it has history.
- **Claude Code vs on-device edits**: Claude Code pushes to GitHub. Pull
  from Termux before editing on-device. If a conflict happens, git merge
  resolves it.
