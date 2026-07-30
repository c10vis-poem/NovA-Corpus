#!/usr/bin/env python3
"""Dedupe (per-folder) + normalize docs to Markdown + relocate into clean vault structure."""
import sys, os, hashlib, shutil, subprocess, collections

DOC_EXTS = {".docx", ".doc"}
PDF_EXTS = {".pdf"}
TXT_EXTS = {".txt"}
PASSTHROUGH_SKIP_CONVERT = {".md", ".jsonl"}  # already fine as-is

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def real_ext(path):
    ext = os.path.splitext(path)[1].lower()
    if ext:
        return ext
    # extensionless files: sniff type
    try:
        out = subprocess.run(["file", "--mime-type", "-b", path], capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        return ""
    if out == "application/pdf":
        return ".pdf"
    if "wordprocessingml" in out:
        return ".docx"
    if out.startswith("text/"):
        return ".txt"
    return ""

def convert_docx(src, dst_md):
    r = subprocess.run(["pandoc", src, "-o", dst_md, "-t", "gfm"], capture_output=True, text=True, timeout=120)
    return r.returncode == 0

def convert_pdf(src, dst_md, title):
    try:
        import fitz
        doc = fitz.open(src)
        text = "\n\n".join(page.get_text() for page in doc)
        doc.close()
    except Exception as e:
        return False
    with open(dst_md, "w") as f:
        f.write(f"# {title}\n\n{text}")
    return True

def process(src_root, dupes_root, dest_root):
    seen_by_dir = collections.defaultdict(dict)  # dirpath -> {hash: kept_relpath}
    stats = collections.Counter()
    for dirpath, dirnames, filenames in os.walk(src_root):
        for fn in filenames:
            src = os.path.join(dirpath, fn)
            rel = os.path.relpath(src, src_root)
            parent = os.path.dirname(rel)
            h = sha256_of(src)
            if h in seen_by_dir[parent]:
                # duplicate within same source folder -> quarantine
                dst = os.path.join(dupes_root, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.move(src, dst)
                stats["duplicate"] += 1
                continue
            seen_by_dir[parent][h] = rel

            ext = real_ext(src)
            base, orig_ext = os.path.splitext(fn)
            if not orig_ext and ext:
                base = fn  # keep whole name as base if no ext originally

            if ext in DOC_EXTS:
                dst = os.path.join(dest_root, os.path.dirname(rel), base + ".md")
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                if convert_docx(src, dst):
                    stats["converted_docx"] += 1
                else:
                    shutil.copy2(src, os.path.join(dest_root, rel))
                    stats["convert_failed_docx"] += 1
            elif ext in PDF_EXTS:
                dst = os.path.join(dest_root, os.path.dirname(rel), base + ".md")
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                if convert_pdf(src, dst, base):
                    stats["converted_pdf"] += 1
                else:
                    dst2 = os.path.join(dest_root, rel)
                    os.makedirs(os.path.dirname(dst2), exist_ok=True)
                    shutil.copy2(src, dst2)
                    stats["convert_failed_pdf"] += 1
            elif ext in TXT_EXTS and orig_ext == ".txt":
                dst = os.path.join(dest_root, os.path.dirname(rel), base + ".md")
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                stats["converted_txt"] += 1
            else:
                dst = os.path.join(dest_root, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
                stats["passthrough"] += 1
    return stats

if __name__ == "__main__":
    src_root, dupes_root, dest_root = sys.argv[1], sys.argv[2], sys.argv[3]
    stats = process(src_root, dupes_root, dest_root)
    for k, v in stats.items():
        print(f"{k}: {v}")
