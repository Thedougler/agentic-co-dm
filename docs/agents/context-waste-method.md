# ASE method: llm-wiki context waste (#71)

**Status:** design lock for ATE (do not score prose quality; CD owns creative language).  
**Rule:** excess tokens for the same job = bug (`AGENTS.md` Token cost + error-ledger sittings).  
**Goal:** max context on **content + reasoning about content**; plumbing stays out of the window unless required.

**Nick constraint (2026-09-14):** Do **not** thin content — especially narrative prose or mechanics. Optimize **without** losing quality of agent instructions/skills. **Agent instructions must not lose output quality** — dedupe conflicts/ambiguity only when the surviving instruction still produces the same or better agent outputs. Never “optimize” by deleting craft that raises output quality. Primary target is **confusion and ambiguity**. **Highest priority:** conflicting or redundant instructions across skills/AGENTS. Byte-count is **not** a success metric.

Prior art (cite, do not reinvent): `scripts/manifest.py`, `hot.md` preference, `entities/{type}/` + kebab filenames (`wiki/AGENTS.md`), Retrieval Primitives / escalate-only (`llm-wiki/SKILL.md`), `WIKI_TOKEN_WARN_THRESHOLD` / wiki-status footprint, error-ledger token doctrine, `scripts/context-waste-scan.py`. Objective token counts: `docs/agents/token-measurement.md` / `scripts/token-count.py` (tiktoken) — scan **bytes/lines** remain structural leads, not token fields.

---

## 1. Taxonomy: waste vs necessary structure

### A. Skill / AGENTS load waste
| Waste | Repo example |
|---|---|
| Load whole skill when one section answers | `llm-wiki` ~35KB; agents load full file for one Retrieval Primitives row |
| Restate CLI contract in prose | Skills that narrate `manifest.py` flags instead of “run `stats`/`has`/`get`” |
| Stack AGENTS + skill + wiki/AGENTS for one claim | Boot loads all three when `hot.md` + one owner path would do |

### B. Data load waste
| Waste | Repo example (measured 2026-09-14) |
|---|---|
| Full `.manifest.json` into chat | ~314KB / 807 sources — forbidden; use `manifest.py` |
| Full `index.md` / `log.md` | ~116KB / 743L and ~142KB / 660L |
| Huge page body for one claim | Session beats ~190–220L; `Hinewai.md` 388L |
| Skills that still say “Read …/index.md” | e.g. `wiki-research`, `wiki-capture`, `wiki-dashboard` (vs escalate-only table) |

### C. Page body infra waste (structural only — not prose quality)
| Waste | Repo example |
|---|---|
| Satellite H1 dumps | `Hinewai.md`: 4× `#` (`Hinewai`, `The Death Bloom`, `History`, `Combat`); 43 pages with >1 H1; PC Layout already: single H1, flatten satellites |
| Foundry dump-copy | PC pages: `## Foundry sheet` ~63–85 lines of live-sheet dump beside Sheet/Combat jobs |
| Nested process asides | Procedure narrating how the page was built inside the owner body |
| Triple-tell / synonym sections | Shared grammar: no synonym headings for same job; dup `## At a Glance` on `Hinewai.md` |
| Empty scaffold left filled-in | Shared grammar + Layout: omit empty; ~10 pages still emptyish `##` → next `##` |

### D. Packet / chat waste
| Waste | Prefer |
|---|---|
| Paste full page / skill / manifest into packet | `path` + line offset/range + capped excerpt |
| Re-dump CLI stdout already on disk | Path to artifact + 1-line metric |

### Necessary structure (NOT waste)
- Thin frontmatter (`type`, `title`, `summary`, lifecycle, sources, tier) — enables cheap retrieval
- Layout jobs / shared headings (`At a Glance`, `Connections`, …) when they carry content
- One-owner numbers (Sheet / Combat Profile once — not a second Foundry novel)
- Wikilinks + title-stem filenames under `entities/{type}/`
- `hot.md` (~2KB semantic snapshot), `manifest.py` thin JSON/TSV rows
- Escalate-only Retrieval Primitives table (when cited, not recopied)

---

## 2. Detection signals (measurable, deterministic)

Prefer heuristics agents/CLIs run **without** loading bodies into chat (path + metric only).

| ID | Signal | Thin measurement | Soft→Hard |
|---|---|---|---|
| S1 | Skill instructs full `.manifest.json` read | `rg` on `.agents/skills/**/SKILL.md` for read/load/cat of `.manifest.json` **without** nearby “do not … whole” | HARD (skill contract) |
| S2 | Skill instructs full `index.md`/`log.md` as first step | `rg` “Read …/index.md” / “Read …/log.md” vs cite Retrieval Primitives | SOFT→HARD after skill slim |
| S3 | Oversized skill (**lead only**) | `stat` byte size; flag `SKILL.md` > ~24KB → investigate for **redundancy/conflict**, not a mandate to shorten | SOFT lead |
| S4 | Oversized page (**lead**) | line count / bytes as a lead to look for **infra** redundancy (multi-H1, Foundry dump, empty scaffolds) — **never** a reason to delete narrative/mechanics | SOFT lead |
| S5 | Multiple H1 in body | count `(?m)^# ` after FM; >1 = hit → structural flatten only; **keep** all narrative/mechanics under one H1 | SOFT (structural); not HARD yet |
| S6 | Satellite facet H1 pattern | `^# .+ — ` or second `#` matching title facet | SOFT |
| S7 | Foundry dump-copy span | lines from `## Foundry` to next `##`; flag >40L on PC/NPC | SOFT (structural remorph) |
| S8 | Empty sections | `## X` then only whitespace/comment before next `##` | SOFT |
| S9 | Dup shared heading | duplicate `## At a Glance` (etc.) | SOFT |
| S10 | Ledger/index bulk files touched as “read whole” in sittings | error-ledger `path-read` includes `.manifest.json`/`index.md`/`log.md` whole | sitting metric |
| S11 | Hot bypass | prep/query sitting with no `hot.md` and full index read | SOFT process |

**Out of scope for detectors:** embedding similarity, “is this prose good,” lore inventiveness.

---

## 3. Fix paths (ranked — Nick order)

1. **Deduplicate / reconcile conflicting skill + AGENTS instructions** (highest priority) — Same job stated differently in two places → one owner, others cite. Contradictory paths/types/loads → pick the locked rule, delete the loser. Redundant CLI restates → delete prose, keep one thin invoke line.
2. **Remove ambiguity that causes wrong loads** — Unclear “read the index” / dual homes / optional whole-file dumps that agents interpret as required. Replace with escalate-only primitives and explicit forbids.
3. **Structural infra only when clearly redundant** — Multi-H1 satellites, Foundry dump beside Sheet, empty scaffolds, process asides — **only** when that block is not the sole home of mechanics or narrative. Remorph must **preserve** all craft content (prose, numbers, rulings).
4. **Thin CLIs** — `manifest.py`, `context-waste-scan.py`, context-pack / wiki-status. Optional later: index-query / log-tail. CLIs answer questions; they do not replace skill craft.
5. **Packet format** — `{path, start_line, end_line, excerpt≤K}`; forbid pasting full skill/manifest/index/log.

**Forbidden fix:** “slim for byte count” or any delete that drops instruction craft, narrative, mechanics, or **agent output quality**. Dedupe only with equal-or-better outputs. S3/S4 size flags are **investigation leads**, not delete targets. Byte-count is not a success metric.

---

## 4. One ATE lever first

### `scripts/context-waste-scan.py`

**Job:** emit compact JSON of waste hits; **never** dump file contents beyond path + metric (+ optional ≤120-char excerpt only if `--excerpt` and only for the matching line).

**Inputs:** repo root (default `.`), `--vault wiki`, `--json` (default), `--skills .agents/skills`.

**Emits (schema sketch):**
```json
{
  "version": 1,
  "vault": "wiki",
  "summary": {"skills_scanned": 0, "pages_scanned": 0, "hits": 0},
  "hits": [
    {"signal": "S1_skill_full_manifest_read", "severity": "hard", "path": ".agents/skills/…/SKILL.md", "metric": {"pattern": "…"}},
    {"signal": "S4_oversized_page", "severity": "soft", "path": "wiki/entities/npc/Hinewai.md", "metric": {"lines": 388, "bytes": 16900, "type": "npc"}},
    {"signal": "S5_multi_h1", "severity": "soft", "path": "wiki/entities/npc/Hinewai.md", "metric": {"h1_count": 4}},
    {"signal": "S7_foundry_dump_span", "severity": "soft", "path": "wiki/entities/pc/Jean-Claude Tabarnack.md", "metric": {"foundry_lines": 85}}
  ]
}
```

**Acceptance (ATE):**
- [ ] Exit 0 always on scan success; exit 1 only on IO/usage error (soft gate — does not fail CI until promoted).
- [ ] Stdout is JSON only (or `--text` one-line-per-hit: `signal path metric`); no page/skill bodies.
- [ ] Detects S1 (skill full-manifest read without forbid), S3 (skill bytes), S4 (page lines), S5 (multi H1), S7 (Foundry span) at minimum.
- [ ] Skips `_archive`, `_raw`, `templates/` for page size/H1 (templates may intentionally multi-H1 as scaffolds — report under `templates:` bucket only if `--include-templates`).
- [ ] Runs under ~2s on current vault without loading `.manifest.json` into the process as a printed blob (may `stat` size as metric).
- [ ] Documented one-liner in AGENTS + llm-wiki pointer (section 5).

---

## 5. Where to document (thin; early-dev flexible)

| Location | Add |
|---|---|
| `AGENTS.md` | Short **Context waste** bullet under Token cost / Helpers: excess tokens = bug; prefer `manifest.py` / `hot.md` / escalate-only; run `python3 scripts/context-waste-scan.py` before large wiki jobs; no prose scoring |
| `llm-wiki/SKILL.md` | One pointer under Retrieval Primitives: “anti-patterns scanned by `context-waste-scan.py`; do not load index/log/manifest wholesale” |
| `wiki/AGENTS.md` | Optional one-liner under Layout: multi-H1 / Foundry dump-copy / empty sections = structural waste (see #71) |
| This doc | `docs/agents/context-waste-method.md` — method of record for ASE/ATE |

Thresholds stay soft. Promote S1 (full-manifest reads) when skills are clean. Promote multi-H1 only after structural remorph that **preserves** narrative/mechanics. Never promote raw byte-size to HARD.

---

## ATE packet shape (handoff)

```text
ATE: keep context-waste-scan.py aligned with Nick constraint
Issue: #71
Labels: S3/S4 are leads (redundancy/conflict/infra), not “shorten” mandates
Bounds: detector only; no mass remorph that strips narrative/mechanics; no prose scoring;
        do not add HARD size gates that force craft cuts; do not commit multi-H1 HARD until remorph preserves content
Prove: scan JSON path+metric; document in --help / method that size ≠ delete
Cite: this doc §3 ranked fixes; Retrieval Primitives
```
