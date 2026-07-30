# INBOX — raw dump, temporary

Push everything here, unfiltered, straight from Termux. Preserve your
Drive folder structure underneath this folder — don't flatten, don't
pre-sort, don't skip duplicates or PDFs. One push, everything, done.

Claude processes from here:
1. Dedupe — SCOPED PER FOLDER ONLY. The same file living in two different
   folders is intentional (operator's access pattern) and both copies stay,
   untouched, in both locations. Only flag/move a file that is duplicated
   *within the same folder* (e.g. "X.jsonl" and "Copy of X.jsonl" sitting
   next to each other, or the same file saved 2-3x in one folder). Those
   in-folder dupes get moved to `_DUPLICATES_REVIEW/` at repo root for the
   operator to look at and delete; one canonical copy stays in place.
2. Clean + normalize everything into Markdown in the real vault structure
   at repo root (replacing this folder's flat dump).
3. Large content gets chunked out of the Markdown into JSONL for a
   retrieval library, in its own folder at repo root.

Once all three phases are done and confirmed, this whole `INBOX/` folder
gets deleted.
