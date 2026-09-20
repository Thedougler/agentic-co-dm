# Batch C eval citations (wiki-ops)

Written under `/workspace/batch-c-evals/` only. Source skills live in
`/home/box/agentic-co-dm/.agents/skills/{wiki-dedup,wiki-ingest,cross-linker,wiki-query,wiki-status,wiki-update,wiki-capture,wiki-synthesize,wiki-agent,llm-wiki}/`
and were **not** modified. Do **not** treat this folder as authorization to
edit `/home/box/agentic-co-dm`. Target install path later:
`.agents/skills/<skill>/evals/evals.json` and
`.agents/skills/_eval-notes/batch-c-citations.md`.

**Audit time:** 2026-09-19 ~01:00 PT  
**Pattern bar:** `.agents/skills/wiki-lint/evals/evals.json` (typed `assertions[{text,type}]`;
process scripts; report shape; refuse destructive; no invent).  
**Theme source:** `/workspace/eval-audit/batch-b-report.md` (wiki-ops audit; filename historical).

---

## Schema (all 10)

- `skill_name` + `evals[{id, prompt, expected_output, assertions[{text,type}]}]`
- Types: `process | structure | content | guardrail | quality`
- **No** `expectations[]` arrays
- ~4 evals per skill (40 total)

---

## Per-skill citations

### wiki-dedup (priority 1)
- **SKILL.md:** Modes Audit/`--merge`; registry excludes; score thresholds; verdicts
  merge/keep-separate/needs-review; Dedup Report; Step 5 pre-write snapshot; 5c delete
  secondary **no redirect stub** (aliases absorb); vault-wide rewrite; index/hot/manifest.
- **Bar themes (batch-b):** audit-only; confirm+manual merge; keep-separate; refuse silent merge.
- **Judgment:** SKILL 5a prose says “replaced with a redirect stub” but **5c + Redirect Stub
  Handling + lint Check 14** say no stubs / aliases absorb. Evals assert **5c / Check 14**.
- **Scripts/paths:** Config Resolution; `hot.md`/`index.md`/`log.md`; `.manifest.json` via
  helpers; `scripts/qmd-maintain.sh` / `qmd update` after writes.

### wiki-ingest (priority 2)
- **SKILL.md:** Content Trust Boundary; append `cache-check` / `manifest.py delta` →
  `manifest.py record`; idea→destination; campaign `wiki/AGENTS.md`; raw mode →
  `wiki/_archive/`; page-scoped `wiki lint <page>`.
- **Bar themes:** append distill; untrusted instructions; no invented names; raw promote
  without foreign outline.
- **READ targets allowed:** taking-on-aruhe, Mercatura, varn, high-eyrie, aruhe (routing only).
- **Scripts/paths:** `scripts/manifest.py`; `obsidian-wiki cache-check`; `scripts/wiki`;
  `wiki/_raw/`; `wiki/attachments/`; `scripts/qmd-maintain.sh`.

### cross-linker (priority 3)
- **SKILL.md:** frontmatter registry; EXTRACTED/INFERRED only; pre-write snapshot; inline
  wrap; no code/FM/self/double links; never target redirect stubs; Cross-Link Report;
  log/hot; misc affinity.
- **Bar themes:** registry+confidence; snapshot abort; wrap rules; report-only dry run.
- **Scripts/paths:** Config Resolution; Retrieval Primitives; `qmd update` /
  `scripts/qmd-maintain.sh`.

### wiki-query (priority 4)
- **SKILL.md:** READ-ONLY (sole write `log.md`); `obsidian-wiki graph-query`; index-only
  mode; visibility filter; Retrieval transparency counts; refuse embedded writes →
  capture/update.
- **Bar themes:** refuse write; graph-query/primitives; citations+counts; public-only.
- **READ targets:** varn, high-eyrie, Mercatura (answer from wiki; no invent).
- **Scripts/paths:** `obsidian-wiki graph-query`; `scripts/manifest.py` lookup only; QMD
  collection `wiki`.

### wiki-status (priority 5)
- **SKILL.md:** `manifest.py` only (no whole `.manifest.json`); Status Report + What to Do
  Next; `token-count.py`; insights → `graph-analyse` + `_insights.md`; skip <20 pages;
  recommend append/rebuild without running rebuild.
- **Bar themes:** delta report; report shape; insights; no destructive rebuild.
- **Scripts/paths:** `scripts/manifest.py`; `scripts/token-count.py`;
  `obsidian-wiki graph-analyse`; `scripts/qmd-maintain.sh` (insights write only).

### wiki-update (priority 6)
- **SKILL.md:** `last_commit_synced` + merge-base rebase fallback; distill decisions not
  lockfiles; `projects/<name>/<name>.md`; prune stale code relationships; never write
  `.codegraph/` / focus-map JSON into vault; optional `code-understand`.
- **Bar themes:** project sync delta; distill filter; project tree shape; no codegraph dump.
- **Scripts/paths:** `scripts/manifest.py`; `obsidian-wiki code-understand` / `ast-extract`;
  `scripts/qmd-maintain.sh`.

### wiki-capture (priority 7)
- **SKILL.md:** Quick KEEP/SKIP → `_raw/<date>-<slug>.md` only (no manifest/index/log/hot/QMD);
  Stop-hook errs SKIP; Full declarative page; Correction atomic claim + SHA immutability.
- **Bar themes:** quick stage; full declarative; correction SHA; Stop-hook SKIP.
- **Scripts/paths:** `references/raw-format.md`; Config Resolution; `.manifest.json` (full/
  correction only).

### wiki-synthesize (priority 8)
- **SKILL.md:** co-occurrence skip specials; filter existing `synthesis/`; score table;
  template with Strongest Objection + testable query (no invented citation); back-links;
  index/log/hot.
- **Bar themes:** scan skips; template; no invented citations; top-N rank.
- **Scripts/paths:** `synthesis/`; `_meta/taxonomy.md`; `_insights.md`; `rg`;
  `scripts/qmd-maintain.sh`.

### wiki-agent (priority 9)
- **SKILL.md:** `/wiki-{claude,codex,hermes,openclaw,copilot,pi}` routing; stop if history
  root missing; cheap index then top 3–5; distill + immediate answer; not bulk
  `wiki-history-ingest`; `manifest.py upsert`.
- **Bar themes:** route+stop; cheap score; distill+answer; no bulk ingest / no invent.
- **Scripts/paths:** `scripts/manifest.py`; agent history env vars; companion
  `*-history-ingest` skills (not invoked for bulk).

### llm-wiki (priority 10)
- **SKILL.md:** Config Resolution (`@name` → CWD `.env` → `~/.obsidian-wiki/config` →
  prompt); three-layer architecture; campaign `category` + `type` depth-1; absolute
  manifest keys; Retrieval Primitives; `scripts/context-waste-scan.py`.
- **Bar themes:** config order/no secret leak; three-layer; campaign paths; manifest +
  primitives.
- **Scripts/paths:** `scripts/manifest.py`; `scripts/context-waste-scan.py`;
  `scripts/qmd-maintain.sh`; `.manifest.json` (via helpers).

---

## Ops-eval checklist coverage

| Rule | How covered |
| --- | --- |
| Ground in skill process + live ops paths | Every suite cites named scripts/paths from SKILL.md |
| Prefer fixtures / temp-vault | Dedup, ingest, cross-linker, status, update, synthesize prompts label fixtures |
| ≥1 report-only / refuse-write for write-capable | Dedup audit; cross-linker dry-run; query read-only; status report; update no-op; capture SKIP |
| ≥1 destructive-path guardrail | Dedup silent-merge refuse + snapshot; ingest trust boundary; cross-linker snapshot abort; capture SHA; update no codegraph dump |
| Assert named scripts where mandated | `manifest.py`, `wiki-lint`, `graph-query`, `graph-analyse`, `token-count.py`, `cache-check`, `code-understand` |
| Objectively checkable assertions | Typed; concrete artifacts (report sections, file paths, mode flags) |
| Lint-clean READ targets only (no invent lore) | Query/ingest/llm-wiki cite varn, high-eyrie, aruhe, Mercatura, taking-on-aruhe as READ |

---

## Judgment calls

1. **wiki-dedup redirect stubs:** Assert delete + alias absorption (SKILL §5c / lint Check 14),
   not the contradictory “redirect stub” wording in §5a survivor sentence.
2. **wiki-status writes:** Standard status = report-only; insights may write regenerable
   `_insights.md` + log — evals separate those modes.
3. **cross-linker report-only:** SKILL is write-heavy by default; eval id4 covers explicit
   user “don’t edit yet” as a refuse-write / dry-run guardrail even though SKILL does not
   name a `--check` flag.
4. **llm-wiki as companion contract:** Evals test resolution/architecture/path/retrieval
   rules companions must follow — not a fake “run llm-wiki” ops loop.
5. **No live campaign mutation:** Prompts prefer `/tmp/wiki-ops-*-fixture` or labeled temp
   vaults; campaign pages appear only as READ targets.

---

## Counts

| skill | evals |
| --- | ---: |
| wiki-dedup | 4 |
| wiki-ingest | 4 |
| cross-linker | 4 |
| wiki-query | 4 |
| wiki-status | 4 |
| wiki-update | 4 |
| wiki-capture | 4 |
| wiki-synthesize | 4 |
| wiki-agent | 4 |
| llm-wiki | 4 |
| **Total** | **40** |

## Scripts / tools cited across assertions

- `python3 scripts/manifest.py` (stats/list/delta/has/get/lookup/record/upsert/normalize)
- `wiki lint <page>`
- `obsidian-wiki cache-check`
- `obsidian-wiki graph-query`
- `obsidian-wiki graph-analyse`
- `obsidian-wiki code-understand` / `ast-extract`
- `python3 scripts/token-count.py`
- `scripts/qmd-maintain.sh` / `qmd update`
- `scripts/context-waste-scan.py`

## Repo touch policy

- **Wrote:** `/workspace/batch-c-evals/**` only
- **Did not modify:** `/home/box/agentic-co-dm/**`
