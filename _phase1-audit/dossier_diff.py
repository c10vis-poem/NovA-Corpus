import csv, os, collections

BASE = os.path.dirname(os.path.abspath(__file__))

def load(fn):
    rows = []
    with open(os.path.join(BASE, fn), newline='', encoding='utf-8') as f:
        for line in csv.reader(f, delimiter='\t'):
            if len(line) < 5: continue
            fid, title, size, mime, path = line[0], line[1], line[2], line[3], "\t".join(line[4:])
            rows.append(dict(id=fid, title=title, size=size, path=path))
    return rows

all_rows = load('horizons-research.tsv') + load('repo-unnamed.tsv') + load('archives-junk.tsv') + load('aesop.tsv')

def subtree(prefix):
    out = {}
    for r in all_rows:
        if r['path'].startswith(prefix):
            rel = r['path'][len(prefix):]
            out[rel] = r
    return out

def compare(name_a, prefix_a, name_b, prefix_b):
    a = subtree(prefix_a)
    b = subtree(prefix_b)
    only_a = sorted(set(a) - set(b))
    only_b = sorted(set(b) - set(a))
    common = sorted(set(a) & set(b))
    diff_size = [rel for rel in common if a[rel]['size'] != b[rel]['size']]
    print(f"\n=== {name_a} ({len(a)} files) vs {name_b} ({len(b)} files) ===")
    print(f"Only in {name_a}: {len(only_a)}")
    for rel in only_a[:50]:
        print(f"  + {rel}  ({a[rel]['size']}B)")
    print(f"Only in {name_b}: {len(only_b)}")
    for rel in only_b[:50]:
        print(f"  + {rel}  ({b[rel]['size']}B)")
    print(f"Common paths: {len(common)}, of which size differs: {len(diff_size)}")
    for rel in diff_size[:20]:
        print(f"  ~ {rel}: {name_a}={a[rel]['size']}B  {name_b}={b[rel]['size']}B")

compare(
    "PRIMARY (a)", "#RESEARCH DOSSIER 1&2/PRIMARY RESEARCH DOSSIER (a)/",
    "PRIMARY (b)", "#RESEARCH DOSSIER 1&2/PRIMARY RESEARCH DOSSIER (b)/",
)
compare(
    "SECONDARY", "#RESEARCH DOSSIER 1&2/SECONDARY RESEARCH DOSSIER/",
    "PSECONDARY", "#RESEARCH DOSSIER 1&2/PSECONDARY RESEARCH DOSSIER/",
)
