# ASE method: llm-wiki maintenance loop (#90)

**Status:** design lock for CoS routines + ATE facade (Researcher hygiene practices folded 2026-09-14 — material Layer A/B/C/cadence only).  
**Goal:** continuous vault health — lint → clean → organize → optimize — with minimal Nick babysitting, using **existing** repo skills/CLIs only.  
**Do not invent parallel maintenance skills.**

**Standing constraints:** conflict/redundancy first; no craft/narrative/mechanics thinning; equal-or-better agent output quality on dedupe (#71/#84/#87); scripts ≠ prose (CD); demotion freeze during migration; legacy filename remorph (kebab / Aruhe / `00` strips) **greenlit 2026-09-14**; other mass consolidates still gated; GitHub SoT; objective tokens via tiktoken when labeled (#86).

Layer A MAY apply FR-002 structural repairs unattended. Layer C MUST NOT invent lore the user did not say. User-asked new content files under constitution X.


## Capability boundary

### Input

The loop accepts a resolved vault, an observation request, and the affected
scope. It uses the existing `wiki health`, `wiki lint`, and registered
`wiki lint fix` contracts; it does not create a workflow ledger or planner.

### Work

`wiki health` is the sole action-ordering surface: consume `context.act`, then
`next.path`, then ordered `focus`. `wiki lint` exposes the complete configured
findings for that scope. Registered deterministic repair may run through the
existing fixer; semantic findings return to the artifact owner. Rerun the
affected scope after each repair.

### Done

Maintenance closes only when the rerun is clean. If it cannot close, report a
specific finding-level blocker with path, rule, evidence, and owner. A clean
lint result is structural health evidence, not a claim that craft or canon was
improved.

### Capability Handoff

Route deterministic structure to the registered fixer, semantic page work to
the page owner, dedup to `wiki-dedup`, links to `cross-linker`, and tag audits
to `tag-taxonomy`. Each owner returns bounded evidence to the loop, which
resumes the same health-selected scope.

---

## Architecture

### Layer A — Deterministic (safe auto / report)

Run without fleet chat when clean. Emit compact JSON path+metric (no body dumps).

| Step | Command / tool | Notes |
|---|---|---|
| A1 | `./scripts/wiki lint` | All configured checker findings, including Vale and soft findings |
| A2 | `python3 scripts/context-waste-scan.py` | S3/S4 = **leads** (redundancy/conflict/infra), not shorten mandates |
| A3 | `python3 scripts/token-count.py` (when #86 lands) | Optional footprint rollup; never ÷4 |
| A4 | Filename remorph (#72/#80) | Spaces / `Aruhe` / leading `00` HARD — remorph `--apply` greenlit 2026-09-14 |
| A5 | Empty `_raw/` check | Ingest inbox must clear; report leftover staging files — never overwrite `_raw/` as live canon |
| A6 | Dry-run / plan reports | Dedup audit + structural remorph plans — report first; **filename legacy remorph apply is greenlit**; other applies stay Nick-gated |

Layer A MAY apply FR-002 structural repairs unattended (links, required frontmatter, nearest-valid type, kebab remorph). Classify broken links (near-miss vs planned) as report-never-edit unless a deterministic safe FR-002 fix exists. Lint-green ≠ fidelity (CD/Nick craft gate).

**Quiet rule:** if A1 HARD count = 0 and A5 clear and no P0 waste leads, stay silent (no Nick ping).

Optional thin facade (ATE): `scripts/wiki-maintain --report` → one JSON bundling A1–A6 without new policy.

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
| Prose / fidelity vs raw | Creative Director → Nick | Never auto-apply CD prose; lint-green ≠ fidelity |
| Noted contradictions / rumor forks | Campaign Editor + CD; Nick decides | **Note** conflicts; do not auto-pick winners or collapse public/secret |
| Orphan triage | Wiki Linter / CE | Link, incubate, or archive proposal — not mass-delete |
| Ingest backlog `_raw/` | Wiki Ingest | Clear staging per wiki-ingest; raw stays immutable evidence |

## Anti-thinning (content craft)

When cleaning or remorphing: prune **template fluff, duplicate section jobs, and inactive current-list cruft** only. **Keep** provisional vs revealed, NPC-knows vs party-knows, public vs secret, open threads, incomplete Known Facts, conflicting rumors, multi-clue paths, and expedition/diff history. Fidelity sample vs raw is a CD/Nick craft gate — lint-green ≠ craft quality.

### Layer C — Unsaid invent stays out

- Lore invent the user did not say / Midchain recreate / unapproved names / stubs replaced by invent
- Link demotions during migration freeze; archive/demote ≠ delete without greenlight
- Mass consolidates **other than** greenlit filename legacy remorph (kebab / Aruhe / `00` strips)
- `wiki-dedup --merge` / `--auto`
- Auto-resolve contradictions; collapse conflicting rumors / public-secret into one truth; “enrich” by inventing to fill stubs
- Craft cuts or instruction deletes for token/byte scores; thinning that loses output quality
- Destructive consolidate without dry-run + blast-radius confirm
- Overwrite `_raw/`; silent multi-agent clobber; delete orphans/planned links
- Lint output is the complete checker defect list; do not silently replace it with a hard-only or structural-only pass.

---

## Cadence (CoS routines)

1. **On-save / write-path** — format + structural write lint when filing; not a Nick ping.
2. **Weekday ~09:00 keep-ahead** — Layer A scan; apply FR-002 structural repairs unattended; dry-run non-FR-002. Quiet if clean. Else ranked digest + Layer B packets.
3. **Optional midweek** — ASE context-waste / conflict triage from A2 leads (not byte slim).
4. **Weekly** — `wiki-digest` knowledge summary to Nick (content), separate from tooling status.
5. **Post-session (~15m)** — status/stubs append/diff (CE/Ingest); do not smooth-rewrite history.
6. **Periodic** — contradiction/open-thread / stale lint as **report** (not auto-resolve).
7. **Monthly** — archive inactive / incubate triage proposals (demotion freeze still blocks auto-demote).
8. **Pre-migrate** — full Layer A dry-run + editable plan before any mass remorph/rename apply.

CoS expands the existing Wiki lint keep-ahead routine; do not spawn duplicate ack-only pings. Prefer append/diff over rewrite; one-write entity pages + link-not-copy.

---

## Skill reuse map (no new skills)

| Need | Use |
|---|---|
| All lint findings | `wiki lint` |
| Waste leads | `context-waste-scan.py` + ASE method docs |
| Tokens | `token-count.py` / wiki-status (#86) |
| Orphans / links | `wiki lint`, `cross-linker` |
| Dupes | `wiki-dedup` audit |
| Digest | `wiki-digest` |
| Ingest inbox | `wiki-ingest` |
| Query / pack | `wiki-query`, `wiki-context-pack` |
| Orchestration contract | this doc + `AGENTS.md` |

---

## Report-only / careful apply (mass kebab unlocked 2026-09-14)

- First keep-ahead establishes a **baseline**; later runs prefer **delta-only** digests (new/changed HARD + leads), not full reprint.
- Dry-run / plan default; editable plan JSON for remorph/rename/dedup; blast-radius confirm before apply.
- Confidence labels on packets (deterministic vs judgment).
- Structural remorphs and filename remorphs ship as **GitHub PR diffs** (preferred), not silent multi-agent clobber. Filename legacy apply is greenlit; still prefer PR.
- Dedup stays audit-only; conflicts become report pages / packets — never auto-merge.

## Nick-visible outputs

| When | What |
|---|---|
| Clean keep-ahead | Nothing |
| HARD clusters / decisions | Ranked digest + who owns the packet |
| Weekly | Knowledge digest (`wiki-digest`) |
| Greenlight gates | Dedup merge, demotion thaw, destructive consolidate, contradiction resolution, orphan delete/archive (filename kebab/Aruhe/`00` remorph apply is **already greenlit**) |

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

## Expert-practice grounding

Researcher brief (#90): Layer A = scan + format lint + unattended FR-002 structural repair; lore invent, dedup merge, and contradiction resolution stay Nick-gated (Layer C). Practices mapped from Karpathy llm-wiki, Ranjan fidelity risks, Vault Inspector / vault-cli / Vault Link Check patterns, World Anvil one-write entities, Forte archive≠delete, Matuschak orphan triage, Sly Flourish simplicity ceiling — fleet Researcher packet 2026-09-14.
