# INBOX — raw dump, temporary

Push everything here, unfiltered, straight from Termux. Preserve your
Drive folder structure underneath this folder — don't flatten, don't
pre-sort, don't skip duplicates or PDFs. One push, everything, done.

Claude processes from here:
1. Dedupe — duplicates get moved to `_DUPLICATES_REVIEW/` at repo root
   for you to look at and delete, one canonical copy stays in the real
   vault structure.
2. Clean + normalize everything into Markdown in the real vault structure
   at repo root (replacing this folder's flat dump).
3. Large content gets chunked out of the Markdown into JSONL for a
   retrieval library, in its own folder at repo root.

Once all three phases are done and confirmed, this whole `INBOX/` folder
gets deleted.
