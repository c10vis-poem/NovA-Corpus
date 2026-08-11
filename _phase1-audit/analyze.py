import csv, re, collections, os

FILES = ["aesop.tsv", "horizons-research.tsv", "repo-unnamed.tsv", "archives-junk.tsv"]
BASE = os.path.dirname(os.path.abspath(__file__))

EXCLUDE_PATH_SUBSTR = [
    "Novus -Agenti_HomeGrid",  # separate project, hands off per user
    "/.git/", "/.git\t",
    "/.obsidian/", "/.obsidian ",  # vault-config internals, not documents
]

# Bare/generic filenames that are tool-internal, not "documents" -- these
# collide across unrelated projects by pure coincidence of naming convention.
GENERIC_BLOCKLIST = {
    'head', 'config', 'index', 'main', 'description', 'exclude',
    'packed-refs', 'commit_editmsg', 'app', 'appearance', 'graph',
    'workspace-mobile', 'core-plugins', 'community-plugins', 'daily-notes',
    'backlink', 'canvas', 'manifest', 'data', 'styles.css', 'main.js',
    'gradle.properties', 'build.gradle', 'settings.gradle',
    'local.properties.example', '.gitignore', '.gitkeep', '.gitattributes',
}

rows = []
for fn in FILES:
    with open(os.path.join(BASE, fn), newline='', encoding='utf-8') as f:
        r = csv.reader(f, delimiter='\t')
        for line in r:
            if len(line) < 5:
                continue
            fid, title, size, mime, path = line[0], line[1], line[2], line[3], "\t".join(line[4:])
            if any(x in path for x in EXCLUDE_PATH_SUBSTR):
                continue
            try:
                size = int(size)
            except ValueError:
                size = -1
            rows.append(dict(id=fid, title=title, size=size, mime=mime, path=path, src=fn))

print(f"Total rows after HomeGrid exclusion: {len(rows)}")

# normalize a "family key" from the title
def norm(title):
    t = title.strip()
    t = re.sub(r'\.(md|jsonl|txt|pdf|json|yaml|yml|kt|kts|zip|skill|sh|py|xml|properties|example|gitignore|base|mht)$', '', t, flags=re.I)
    t = re.sub(r'^copy of\s+', '', t, flags=re.I)
    t = re.sub(r'\s*\(\d+\)\s*$', '', t)
    t = re.sub(r'\s+\d+$', '', t)
    t = t.strip().lower()
    return t

def ext(title):
    m = re.search(r'\.([a-zA-Z0-9]+)$', title)
    return m.group(1).lower() if m else '(none)'

GENERIC_NEEDS_PARENT = {
    'readme', 'skill', 'license', 'changelog', 'index', 'contributing',
    'read me', 'notes', 'todo', 'overview',
}

def parent_dir(path):
    parts = path.rstrip('/').split('/')
    return parts[-2].lower() if len(parts) >= 2 else ''

for r in rows:
    fam = norm(r['title'])
    if fam in GENERIC_NEEDS_PARENT:
        fam = parent_dir(r['path']) + '/' + fam
    r['family'] = fam
    r['ext'] = ext(r['title'])

rows = [r for r in rows if r['family'] not in GENERIC_BLOCKLIST]
print(f"Rows after generic-filename blocklist: {len(rows)}")

# Group by (family, ext) -> list of sizes/rows
groups = collections.defaultdict(list)
for r in rows:
    groups[(r['family'], r['ext'])].append(r)

exact_dupe_groups = []   # same family+ext+size, count>1
version_conflict_groups = []  # same family+ext, different sizes present
singletons = 0

for (fam, e), items in groups.items():
    if len(items) == 1:
        singletons += 1
        continue
    sizes = set(i['size'] for i in items)
    if len(sizes) == 1:
        exact_dupe_groups.append((fam, e, items))
    else:
        version_conflict_groups.append((fam, e, items))

total_dupe_files_removable = sum(len(items) - 1 for _, _, items in exact_dupe_groups)

print(f"Distinct (family, ext) groups: {len(groups)}")
print(f"Singleton groups (no dupes): {singletons}")
print(f"Exact-duplicate groups (same size): {len(exact_dupe_groups)}  -> {total_dupe_files_removable} files removable")
print(f"Version-conflict groups (different sizes, same family+ext): {len(version_conflict_groups)}")

with open(os.path.join(BASE, "REPORT.md"), "w", encoding='utf-8') as out:
    out.write("# Vault Duplicate & Version Report\n\n")
    out.write(f"Source rows analyzed: {len(rows)} (Novus-Agenti_HomeGrid excluded per instruction)\n\n")
    out.write(f"- Exact-duplicate groups: {len(exact_dupe_groups)} ({total_dupe_files_removable} files safe to remove, keeping one each)\n")
    out.write(f"- Version-conflict groups (need a human call): {len(version_conflict_groups)}\n")
    out.write(f"- Singleton files (no action needed): {singletons}\n\n")

    out.write("## Version conflicts (same document+format, DIFFERENT sizes — real edits, not junk)\n\n")
    for fam, e, items in sorted(version_conflict_groups, key=lambda x: -len(x[2])):
        out.write(f"### `{fam}`.{e}\n\n")
        by_size = collections.defaultdict(list)
        for i in items:
            by_size[i['size']].append(i)
        for size, its in sorted(by_size.items(), key=lambda x: -x[0]):
            out.write(f"- **{size} bytes** x{len(its)}:\n")
            for i in its:
                out.write(f"  - `{i['id']}` — {i['path']}\n")
        out.write("\n")

    out.write("## Exact duplicate groups (same document+format+size — pure copies)\n\n")
    for fam, e, items in sorted(exact_dupe_groups, key=lambda x: -len(x[2])):
        keep = items[0]
        dupes = items[1:]
        out.write(f"### `{fam}`.{e}  ({len(items)} copies, {items[0]['size']} bytes each)\n")
        out.write(f"- KEEP: `{keep['id']}` — {keep['path']}\n")
        for d in dupes:
            out.write(f"- dup: `{d['id']}` — {d['path']}\n")
        out.write("\n")

print("Wrote REPORT.md")

import json

def short_loc(path):
    return path.split('/')[0]

dup_table = []
total_reclaim = 0
for fam, e, items in exact_dupe_groups:
    size = items[0]['size']
    reclaim = size * (len(items) - 1)
    total_reclaim += reclaim
    locs = sorted(set(short_loc(i['path']) for i in items))
    dup_table.append(dict(
        family=fam, ext=e, copies=len(items), size=size, reclaim=reclaim,
        locations=locs,
        keep_path=items[0]['path'], keep_id=items[0]['id'],
        dup_paths=[dict(id=i['id'], path=i['path']) for i in items[1:]],
    ))
dup_table.sort(key=lambda x: -x['reclaim'])

version_table = []
for fam, e, items in version_conflict_groups:
    by_size = collections.defaultdict(list)
    for i in items:
        by_size[i['size']].append(i)
    sizes_sorted = sorted(by_size.items(), key=lambda x: -x[0])
    version_table.append(dict(
        family=fam, ext=e,
        variants=[dict(size=s, files=[dict(id=i['id'], path=i['path']) for i in its]) for s, its in sizes_sorted],
    ))

data = dict(
    total_rows=len(rows),
    singletons=singletons,
    exact_dupe_group_count=len(exact_dupe_groups),
    total_reclaimable_files=total_dupe_files_removable,
    total_reclaim_bytes=total_reclaim,
    version_conflict_count=len(version_conflict_groups),
    dup_table=dup_table,
    version_table=version_table,
)

with open(os.path.join(BASE, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f)

print(f"Total reclaimable bytes: {total_reclaim:,}")
print("Wrote data.json")
