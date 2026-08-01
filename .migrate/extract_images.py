#!/usr/bin/env python3
"""Extract images/diagrams that Markdown conversion discards, so they're
reachable by grep instead of locked inside binary PDFs/.mht files.

Two source kinds:
  - PDF: embedded rasters (mutool extract) + vector diagrams (page-level
    fill/stroke op count via `mutool draw -F trace`, then a page render for
    any page over the threshold -- a PDF can have zero embedded rasters and
    still be full of diagrams drawn as vector paths, e.g. architecture boxes
    and arrows).
  - .mht/.mhtml: images arrive as MIME parts (Content-Type: image/*) sitting
    alongside the text/html part; the existing conversion only ever reads
    the html part and drops these entirely.

For each source doc, images land in a sibling "<name>_images/" folder next
to its converted .md, and a "## Extracted images" section (with a relative
link per image) is appended to that .md so grep-by-caption finds them.

No PyMuPDF dependency (unavailable on this platform) -- shells out to
`mutool` (mupdf-tools), which is a native binary with no Python wheel needed.
"""
import os, sys, re, glob, subprocess, email, collections

VECTOR_OP_THRESHOLD = 5  # fill_path/stroke_path calls on a page before we treat it as "has a diagram"
RENDER_DPI = 150

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=kw.pop("timeout", 120), **kw)

def page_count(pdf_path):
    r = run(["mutool", "pages", pdf_path])
    return len(re.findall(r'<page pagenum="\d+"', r.stdout))

def page_vector_op_count(pdf_path, page_num, tmp_dir):
    trace_path = os.path.join(tmp_dir, f"__trace_{page_num}.txt")
    r = run(["mutool", "draw", "-F", "trace", "-o", trace_path, pdf_path, str(page_num)])
    if r.returncode != 0 or not os.path.exists(trace_path):
        return 0
    with open(trace_path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    os.remove(trace_path)
    return len(re.findall(r"\b(fill_path|stroke_path)\b", text))

def extract_pdf_images(pdf_path, out_dir):
    """Returns list of (relpath, caption) for images written into out_dir."""
    results = []
    os.makedirs(out_dir, exist_ok=True)
    abs_pdf_path = os.path.abspath(pdf_path)  # cwd=out_dir below would break a relative path

    # 1. embedded rasters
    r = run(["mutool", "extract", "-r", abs_pdf_path], cwd=out_dir, timeout=180)
    if r.returncode != 0:
        print(f"  [warn] mutool extract failed for {pdf_path}: {r.stderr.strip()[:200]}", file=sys.stderr)
    for fn in sorted(os.listdir(out_dir)):
        if fn.startswith("font-"):
            os.remove(os.path.join(out_dir, fn))
            continue
        if fn.startswith("image-"):
            results.append((fn, "embedded raster"))

    # 2. vector-diagram pages: render any page whose fill/stroke op count
    # clears the threshold (covers PDFs with zero embedded rasters that are
    # still full of vector-drawn architecture diagrams)
    n_pages = page_count(pdf_path)
    for p in range(1, n_pages + 1):
        ops = page_vector_op_count(pdf_path, p, out_dir)
        if ops >= VECTOR_OP_THRESHOLD:
            png_name = f"page-{p}-diagram.png"
            png_path = os.path.join(out_dir, png_name)
            rr = run(["mutool", "draw", "-o", png_path, "-r", str(RENDER_DPI), pdf_path, str(p)], timeout=120)
            if rr.returncode == 0 and os.path.exists(png_path):
                results.append((png_name, f"page {p} render ({ops} vector ops)"))
    return results

def extract_mht_images(mht_path, out_dir):
    results = []
    with open(mht_path, "rb") as f:
        msg = email.message_from_binary_file(f)
    idx = 0
    for part in msg.walk():
        ctype = part.get_content_type()
        if not ctype.startswith("image/"):
            continue
        payload = part.get_payload(decode=True)
        if not payload:
            continue
        idx += 1
        ext = ctype.split("/")[-1].split(";")[0] or "bin"
        if ext == "svg+xml":
            ext = "svg"
        name = f"mht-image-{idx:03d}.{ext}"
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, name), "wb") as out:
            out.write(payload)
        loc = part.get("Content-Location", "")
        results.append((name, loc or "mht MIME part"))
    return results

def append_image_section(md_path, images_dir_name, results):
    if not results:
        return
    with open(md_path, encoding="utf-8", errors="replace") as f:
        if "## Extracted images" in f.read():
            return  # already appended by a prior run -- don't duplicate
    lines = ["", "## Extracted images", "",
             f"(pulled from the source doc by `.migrate/extract_images.py` -- "
             f"Markdown conversion drops these; see `{images_dir_name}/`)", ""]
    for name, caption in results:
        lines.append(f"- ![{caption}]({images_dir_name}/{name}) -- {caption}")
    with open(md_path, "a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

def already_done(md_path):
    if not os.path.exists(md_path):
        return False
    with open(md_path, encoding="utf-8", errors="replace") as f:
        return "## Extracted images" in f.read()

def process_pdf(pdf_path):
    md_path = pdf_path + ".md"
    if not os.path.exists(md_path) or already_done(md_path):
        return None
    base = os.path.basename(pdf_path)
    out_dir = os.path.join(os.path.dirname(pdf_path), base + "_images")
    results = extract_pdf_images(pdf_path, out_dir)
    if not results:
        if os.path.isdir(out_dir) and not os.listdir(out_dir):
            os.rmdir(out_dir)
        return (pdf_path, 0)
    append_image_section(md_path, os.path.basename(out_dir), results)
    return (pdf_path, len(results))

def process_mht(mht_path):
    md_path = mht_path + ".md"
    if not os.path.exists(md_path) or already_done(md_path):
        return None
    base = os.path.basename(mht_path)
    out_dir = os.path.join(os.path.dirname(mht_path), base + "_images")
    results = extract_mht_images(mht_path, out_dir)
    if not results:
        if os.path.isdir(out_dir) and not os.listdir(out_dir):
            os.rmdir(out_dir)
        return (mht_path, 0)
    append_image_section(md_path, os.path.basename(out_dir), results)
    return (mht_path, len(results))

SKIP_DIRS = {".git", ".migrate", "RAG_LIBRARY", "_DUPLICATES_REVIEW"}

def iter_source_files(root, exts):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.endswith("_images")]
        for fn in filenames:
            if os.path.splitext(fn)[1].lower() in exts:
                yield os.path.join(dirpath, fn)

def main(root, targets=None):
    stats = collections.Counter()
    total_images = 0
    if targets:
        pdfs = [t for t in targets if t.lower().endswith(".pdf")]
        mhts = [t for t in targets if t.lower().endswith((".mht", ".mhtml"))]
    else:
        pdfs = list(iter_source_files(root, {".pdf"}))
        mhts = list(iter_source_files(root, {".mht", ".mhtml"}))

    for p in pdfs:
        res = process_pdf(p)
        if res is None:
            continue
        stats["pdf_docs"] += 1
        stats["pdf_images"] += res[1]
        total_images += res[1]
        print(f"[pdf] {res[1]:>3} images  {p}")

    for m in mhts:
        res = process_mht(m)
        if res is None:
            continue
        stats["mht_docs"] += 1
        stats["mht_images"] += res[1]
        total_images += res[1]
        print(f"[mht] {res[1]:>3} images  {m}")

    print(f"\nTOTAL: {total_images} images extracted "
          f"({stats['pdf_docs']} PDFs, {stats['mht_docs']} MHTs processed)")

if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    targets = sys.argv[2:] if len(sys.argv) > 2 else None
    main(root, targets)
