# corpus

Knowledge corpus. Two tiers:

| Folder | Contents |
|---|---|
| `canon/` | Locked specs — operator verbatim word, anchored to a concrete artifact, build state declared |
| `pending/` | Pending-corpora — transcripts, manuals, operator build docs, archives awaiting triage |

## Canon format rule

Canon is not "documents we trust." Canon is the operator's verbatim word, anchored to a concrete artifact, with anything derived visibly separated from it and its build state declared.

Every canon document: artifact anchor → operator verbatim quote → `**Spec.**` derived content → status ledger (`built-verified` / `built-unverified` / `designed-only` / `absent`).
