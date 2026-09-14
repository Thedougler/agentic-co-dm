# ASE method: llm-wiki maintenance loop (#90)

**Status:** design lock for CoS routines + ATE facade.  
**Goal:** continuous vault health — lint → clean → organize → optimize — with minimal Nick babysitting, using **existing** repo skills/CLIs only.  
**Do not invent parallel maintenance skills.**

**Standing constraints:** conflict/redundancy first; no craft/narrative/mechanics thinning; equal-or-better agent output quality on dedupe (#71/#84/#87); scripts ≠ prose (CD); demotion freeze during migration; mass kebab rename gated until Nick greenlights (#80/#72); GitHub SoT; objective tokens via tiktoken when labeled (#86).

---

## Architecture

### Layer A — Deterministic (safe auto / report)

Run without fleet chat when clean. Emit compact JSON path+metric (no body dumps).

| Step | Command / tool | Notes |
|---|---|---|
| A1 | `./scripts/wiki-lint --json` | HARD keys only for fail-noise; soft findings listed separately |
| A2 | `python3 scripts/context-waste-scan.py` | S3/S4 = **leads** (redundancy/conflict/infra), not shorten mandates |
| A3 | `python3 scripts/token-count.py` (when #86 lands) | Optional footprint rollup; never ÷4 |
| A4 | Filename lint (#72, when ready) | Spaces / `Aruhe -` prefix — **lint-only** until Nick greenlights remorph |
| A5 | Empty `_raw/` check | Ingest inbox must clear; report leftover staging files |

**Quiet rule:** if A1 HARD count = 0 and A5 clear and no P0 waste leads, stay silent (no Nick ping).

Optional thin facade (ATE): `scripts/wiki-maintain --report` → one JSON bundling A1–A5 without new policy.

### Layer B — Fleet route (CoS orchestrates; no ack-only)

| Signal | Owner | Action shape |
|---|---|---|
| HARD structure / broken-link clusters | Wiki Linter → ASE/ATE | Deterministic fix or tooling PR; Linter reports, does not invent lore |
| Conflicting / redundant skill+AGENTS instructions | **ASE** | Dedupe only with equal-or-better output quality |
| Context-waste leads (ambiguity, wrong loads) | ASE (+ ATE CLIs) | Investigate leads; no craft cuts for scores |
| Structural remorph (multi-H1 flatten, Foundry distill) **preserving** content | Campaign Editor | Remorph pages; not prose rewrite |
| Missing links / orphans (connect, not invent) | cross-linker / Wiki Linter | Propose links; no Midchain invent |
| Dedup candidates | `wiki-dedup` **audit only** | Report candidates; **no** `--merge`/`--auto` until Nick confirms |
| Knowledge / weekly summary | `wiki-digest` | Player/DM-facing knowledge digest — not status theater |
| Vault footprint / status | `wiki-status` | Tiktoken when available; threshold warn only |
| Prose quality | Creative Director → Nick | Never auto-apply CD prose |
| Ingest backlog `_raw/` | Wiki Ingest | Clear staging per wiki-ingest |

### Layer C — Never auto without Nick

- Lore invent / Midchain recreate / unapproved names
- Link demotions during migration freeze
- Mass filename kebab rename / `Aruhe -` strip apply
- `wiki-dedup --merge` / `--auto`
- Craft cuts or instruction deletes for token/byte scores
- Destructive consolidate without dry-run + confirm when high blast radius
- Any change that lowers agent output quality or strips narrative/mechanics

---

## Cadence (CoS routines)

1. **Weekday ~09:00 keep-ahead** — Layer A full report. Quiet if clean. Else ranked digest + Layer B packets (specialists only for their rows).
2. **Optional midweek** — ASE context-waste / conflict triage from A2 leads (not byte slim).
3. **Weekly** — `wiki-digest` knowledge summary to Nick (content), separate from tooling status.

CoS expands the existing Wiki lint keep-ahead routine; do not spawn duplicate ack-only pings.

---

## Skill reuse map (no new skills)

| Need | Use |
|---|---|
| HARD/soft structure | `wiki-lint` + `./scripts/wiki-lint` |
| Waste leads | `context-waste-scan.py` + ASE method docs |
| Tokens | `token-count.py` / wiki-status (#86) |
| Orphans / links | `wiki-lint`, `cross-linker` |
| Dupes | `wiki-dedup` audit |
| Digest | `wiki-digest` |
| Ingest inbox | `wiki-ingest` |
| Query / pack | `wiki-query`, `wiki-context-pack` |
| Orchestration contract | this doc + `AGENTS.md` |

---

## Nick-visible outputs

| When | What |
|---|---|
| Clean keep-ahead | Nothing |
| HARD clusters / decisions | Ranked digest + who owns the packet |
| Weekly | Knowledge digest (`wiki-digest`) |
| Greenlight gates | Mass rename, dedup merge, demotion thaw, destructive consolidate |

---

## ATE packet (optional facade)

```text
ATE: optional scripts/wiki-maintain --report
Issue: #90
Bundles Layer A JSON (wiki-lint, context-waste-scan, raw empty check; token-count when present)
No new policy; no prose scoring; no auto remorph/merge
Cite: docs/agents/wiki-maintenance-loop.md
```

## Acceptance

- [ ] This design on main
- [ ] CoS weekday routine runs Layer A + routes; quiet when clean
- [ ] Nick digests only for decisions / HARD clusters / weekly knowledge
- [ ] #71/#84/#87/#86/#80 constraints honored
