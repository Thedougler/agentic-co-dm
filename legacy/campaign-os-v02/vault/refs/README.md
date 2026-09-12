---
type: reference
status: canon
publish: false
aliases: []
created: "2026-07-22"
updated: "2026-08-15"
tags: [survival]
summary: "Index of vault/refs/: ideas, stories, per-type vault guides, runbooks, subagents, QC profiles (including qc-beat), lint guidance, random tables, cross-cutting doctrine, GM methodology, and root docs."
uid: f0583a8a-00dc-4f60-924f-5db4e612cd42
---

# References

`vault/refs/` is every reference doc this repo's skills and runbooks point at.
This file is the index: find the section that matches your task, then open
the file or directory it names. Everything below is a real path — confirm
with `ls` before trusting an old copy of this table.

## Ideas — `vault/refs/ideas/`

Craft for collaborating with the DM on a story idea before it has a target
page: campaign-shaping, adventure and villain design, generator tables for
patrons/quests/locations/monsters/treasure, and narrative-device reframing
for sandbox play. No hub file — `ls vault/refs/ideas/` for the full set
([[connecting-characters|connecting-characters.md]],
[[core-adventure-generators|core-adventure-generators.md]] + [[core-adventure-generators-treasures-and-spells|core-adventure-generators-treasures-and-spells.md]],
[[creating-secrets-and-clues|creating-secrets-and-clues.md]], [[genre-conventions|genre-conventions.md]], [[lightning-rods|lightning-rods.md]],
[[npc-generator|npc-generator.md]], [[spiral-campaign-development|spiral-campaign-development.md]],
[[villains-and-themes|villains-and-themes.md]]). Adventure-design checklist and the sandbox-mindset
narrative-device catalog absorbed into
`.claude/skills/composing-beats/references/composition.md`.

## Stories — `vault/refs/stories/`

Story prose craft. [[stories-playbook|Stories Playbook]] is the hub (the
gsarig/ai-playbooks fiction-writing workflow: commands, dev-edit, three-pass
language editing, state tracking). Voice/prose doctrine every prose-producing
skill draws on:

| File | What it governs |
|---|---|
| [[prose-aesthetic\|prose-aesthetic.md]] | The GM's actual prose aesthetic — what's deliberate, what an edit must never suggest. |
| [[banned-patterns\|banned-patterns.md]] | The prose contract — positive instructions for what only judgment catches; Vale owns the mechanical tells. |
| [[banned-patterns-detail\|banned-patterns-detail.md]] | Adjudication record: the reasoning and the GM's wording behind each prose rule. Never drafting material. |
| [[influences\|influences.md]] | Craft moves absorbed from the GM's influences, and what about each work stays behind. |
| [[ai-tells\|ai-tells.md]] | The deduped AI-tell catalog, each with its fix. |
| [[register\|register.md]] | Player-facing vs DM-facing prose register and the failure modes for each. |
| [[developmental-craft\|developmental-craft.md]] | The developmental-editing floor — structure, character, scene, line. |
Story structures (index, classic shapes, campaign/sandbox shapes) moved to
`.claude/skills/draft-story/references/story-structures.md`,
`.claude/skills/draft-story/references/story-structures-classic.md`,
`.claude/skills/draft-story/references/story-structures-campaign.md`.
Diagnosing a stalled or flat journey moved to
`.claude/skills/composing-beats/references/audits.md` § Diagnosing a
stalled or flat journey.

The remaining files in the directory are the playbook's per-command specs
([[new-story|new-story.md]], [[continue-story|continue-story.md]], [[dev-edit|dev-edit.md]], [[language-edit|language-edit.md]],
[[update-chapter|update-chapter.md]], [[audit-story|audit-story.md]], [[publish-and-archive|publish-and-archive.md]]), setup/state
docs ([[setup-and-plugins|setup-and-plugins.md]], [[state-tracking|state-tracking.md]], [[vault-architecture|vault-architecture.md]],
[[global-rules|global-rules.md]], [[story-templates|story-templates.md]]), and further prose craft
([[prose-and-character-craft|prose-and-character-craft.md]], [[literary-adaptation|literary-adaptation.md]],
[[reserved-lines-and-silences|reserved-lines-and-silences.md]], [[exemplar-quality-rubric-prose|exemplar-quality-rubric-prose.md]],
[[prose-aesthetic-source-note|prose-aesthetic-source-note.md]]).

## Vault content types — `vault/refs/vault/<type>/`

One directory per wiki content type. Each holds a references subdirectory
with type-specific checklists, examples, and toy-chest specs.
`vault/refs/vault/_common/` holds the rules every type shares.
Authoring guides (the entry point a draft skill reads) moved to
`.claude/skills/draft-content/references/<type>.md` (ADR-0050).

| Type | Covers |
|---|---|
| background | SRD transcription discipline and the one homebrew authoring path. |
| campaign | [[campaign-overview\|Campaign-overview]] / one-shot pages — Six Truths, Icons, session-zero framing, Safety & Tone. |
| event | A discrete world occurrence, played or scheduled, across its eight subtype forks. |
| faction | The faction fields table and the Front (clock/trigger/consequence) mechanic. |
| handout | An in-world document handed to players, verbatim. |
| item | The One-Thing Discipline, rarity budget, attunement tree. |
| location | The three location genres (site, governed-area, dungeon) and subtype-to-template routing. |
| secret | A concealed thing page-worthy enough to earn its own atomic unit; `subtype: cache` when it stores items. |
| lore | Cosmology, history, pantheons, cultures, legends, prophecies — fact pages with no active agenda. |
| monster | The shared template, stat-block placement, recurrence fork, Wants/Morale lines. |
| npc | The Toy Chest spine, mandatory Wants and Opening move lines. |
| puzzle | Puzzles, traps, hazards, trials, and composites under one `type: puzzle` shape; `writing-traps-trials` owns craft. |
| quest | Structural pattern choice and the `quest_status` ladder. |
| season | A run of consecutive sessions under one throughline, ending on a GM-planned Finale. |
| ship | Tier, crew, acquisition. |
| species | SRD transcription discipline and the one homebrew authoring path. |
| table | Random-roll generator tables, vendored or homebrew — see also `table-*.md` below. |
| world | The outermost container a campaign runs in, its canon-vs-homebrew boundary. |

[[_common|_common/]]: [[checklist\|checklist.md]] (the done-bar every
type shares), [[interview\|interview.md]] (questions asked
before drafting), [[hard-rules\|hard-rules.md]],
[[lifecycle\|lifecycle.md]] (draft→pending status ladder and
owned paths), [[degrade\|degrade.md]] (recurring gaps to ask
about rather than guess), [[out-of-scope\|out-of-scope.md]]
and [[handoffs\|handoffs.md]] (work that belongs to another
skill/phase), [[queries\|queries.md]] (the pre-write stub
check).

## Runbooks (`runbook-*.md`)

An agent's guide to a **multi-step operation**: `GATE:` precondition →
numbered steps naming the skill/path each uses → a `Done = <MARKER>:` close.
That shape is the genre contract; this line is where it is stated.

| Runbook | Phase | Drives |
|---|---|---|
| [[runbook-campaign-os-overview\|runbook-campaign-os-overview.md]] | any | The 60-second orientation map — what the system is, the LLM-wiki pattern, the layers, the session loop, the six laws. |
| [[runbook-session\|runbook-session.md]] | 1 PREP | Grep loose threads, write the session story first, build the run guide and its scenes, template new entities. |
| [[runbook-capture\|runbook-capture.md]] | 3 CAPTURE | Turn session audio into the frozen, speaker-labeled transcript the pipeline ingests. |
| [[runbook-ingest\|runbook-ingest.md]] | 4 INGEST | Extract transcript facts to canon pages at `status: canon`, then human spot-check. |
| [[runbook-recap\|runbook-recap.md]] | 5 RECAP | Write the player recap, length judged not counted, from the session's just-ingested canon. |
| [[runbook-publish\|runbook-publish.md]] | 6 PUBLISH | Proposal → approval → build (strips DM-only) → deploy on a green check. |
| [[runbook-wiki\|runbook-wiki.md]] | any | Any wiki edit: session-start bootstrap, record-a-write, new-page/callout/canonical-term rules, tags. |
| [[runbook-maintain\|runbook-maintain.md]] | any | Whole-wiki health sweep — lint at scale, route findings to owning skills, drive to zero. |
| [[runbook-commands\|runbook-commands.md]] | any | The whole `npm run` surface — which search collection, which lint command, dndsim commands and the retirement gate. |
| [[runbook-ingest-inbox\|runbook-ingest-inbox.md]] | any | Bring non-transcript Inbox sources into the wiki at `status: pending`, archive, record. |
| [[runbook-prep-ladder\|runbook-prep-ladder.md]] | any | Route a prep request to the right scope-rung (campaign/season/quest/session/scene) and owning skill. |
| [[runbook-agents\|runbook-agents.md]] | any | Specs for the repo's instantiated subagents — spawner, tools, input/output, non-goals, anti-patterns. |
| [[runbook-dispatch-wave\|runbook-dispatch-wave.md]] | any | Dispatch one agent per independent problem domain, verify before trusting, integrate or targeted-fix-and-reverify. |
| [[runbook-self-improve\|runbook-self-improve.md]] | any | Friction with this repo's own Claude Code setup, Observe → Diagnose → Fix → Prove. |
| [[runbook-craft-improvement\|runbook-craft-improvement.md]] | any | Recreate an external source as a lint-clean guide page, then challenge this repo's own process with it. |
| [[runbook-issue-triage\|runbook-issue-triage.md]] | any | A product-critic report becomes a labeled, triage-ready GitHub issue queue. |
| [[runbook-encounter-tuning\|runbook-encounter-tuning.md]] | any | Reuse proven per-PC matchups, reflavor, simulate, and tune toward the DM's stated intention. |

Each phase's gate and its `Done = <MARKER>:` close live in that phase's own
runbook above.

Fork-walk lives in `vault/refs/runbook-dispatch-wave.md`. The
[[cold-open|cold open]] scene workflow lives in
`.claude/skills/writing-cold-opens/SKILL.md`.

## Subagents (`.claude/agents/*.md`)

Each agent's own file is its single source of truth — frontmatter,
responsibilities, refusals, output contract, and an `## Acceptance` fixture.
`vault/refs/runbook-agents.md` is the hub: the roster with each agent's tools
and spawner, the clauses every agent inherits, and when an agent beats a
plain skill. Confirm the live set with `ls .claude/agents/`.

## QC profiles (`qc-*.md`)

Read-only verification contracts, dispatched to `content-quality-checker`
per `runbook-agents.md`.

| Profile | Checks |
|---|---|
| [[qc-beat\|qc-beat.md]] | A `type: beat` page — cold-runnability, gravity, consequence, world-acting. |
| [[qc-comparative\|qc-comparative.md]] | Ranking N rival drafts of one brief. |
| [[qc-lore-article\|qc-lore-article.md]] | A vault page with `type: lore`. |
| [[qc-narrative-prose\|qc-narrative-prose.md]] | Staged prose drafts — stories, fragments, handout text. Default when no other row matches. |
| [[qc-recap\|qc-recap.md]] | An episode recap. |
| [[qc-run-guide\|qc-run-guide.md]] | `eNN-run-guide-<slug>.md` — a stretch walk — and `eNN-overview.md` — the episode entry. |
| [[qc-table-run-page\|qc-table-run-page.md]] | A vault page with `type: encounter` or `type: puzzle`, run live at the table. |
| [[qc-wiki-page\|qc-wiki-page.md]] | Any other typed vault page, including `vault/campaigns/shattered-sea/pcs/`. |

## Lint-rule guidance (`lint/`)

Named by the lint rule(s) it explains — what the finding means and how to
fix it. Read the one your lint output names; a single-file lint run prints a
`GUIDE:` pointer to it.

| File | Rule(s) |
|---|---|
| [[w22-w23-callouts\|w22-w23-callouts.md]] | W22/W23 — lowercase callout type tokens, play-vs-doc taxonomy. |
| [[w25-w75-wikilinks\|w25-w75-wikilinks.md]] | W25 unlinked entity mentions, W75 dead doc pointers. |
| [[w84-frontmatter-schema\|w84-frontmatter-schema.md]] | W84 — frontmatter-schema failure shapes and the enum-comment mechanism. |
| [[w86-vale-prose\|w86-vale-prose.md]] | W86 — Vale prose findings, the intent-not-regex rule, genuine false positives. |
| [[w114-w116-transclusion\|w114-w116-transclusion.md]] | W114/W115/W116 — session-scene transclusion coverage, naming, broken embeds. |
| [[w119-grandfather-link\|w119-grandfather-link.md]] | W119 — a label slot naming an ancestor above the page's own parent. |
| [[w120-section-count-outlier\|w120-section-count-outlier.md]] | W120 — section-count-outlier neighbour comparison. |
| [[w123-link-footer-section\|w123-link-footer-section.md]] | W123 — a See Also/Related section that's nothing but a wikilink list. |
| [[w78\|w78.md]] | W78 — an empty Session Log section claiming a play history. |
| [[w82\|w82.md]] | W82 — oxlint findings on JS/mjs, and what does not settle one. |
| [[w83\|w83.md]] | W83 — duplicated blocks, transclusion vs wikilink, known boilerplate. |
| [[w85\|w85.md]] | W85 — a markdown link whose relative target no longer exists. |
| [[w87\|w87.md]] | W87 — pymarkdown MD### defects and the standing of a disable call. |
| [[w91\|w91.md]] | W91 — a context-rot marker whose parked condition went stale. |
| [[w139\|w139.md]] | W139 — the Situation contract's governed fields and Beat Chart. |
| [[w140\|w140.md]] | W140 — episode file naming and the overview's session_shape. |
| [[w143\|w143.md]] | W143 — retired session-unit page types and what replaced them. |
| [[dndsim\|dndsim.md]] | dndsim — statblock and combatant-block defects, behind its opt-in flag. |

## Random-generation tables (`table-*.md`)

Vendored d20/d100 generator tables for on-the-fly dressing and encounters —
dungeon chamber types, monster lists by CR band, items, food, names, holidays,
monuments, town events, wilderness finds, traps. `ls vault/refs/table-*.md`
for the full set; each filename names its table's subject
(`table-random-chambers.md`, `table-random-dungeon-monsters.md`,
`table-npc-names.md`, `table-place-names.md`, `table-random-traps.md`, etc.).
The `.claude/skills/draft-content/references/table.md` drafting hub above governs turning one of these
into a `vault/`-tree table page.

## Cross-cutting doctrine

Repo-wide craft standards, not scoped to one content type or phase.

| File | Governs |
|---|---|
| `.claude/skills/writing-player-prose/references/prose-quality.md` | Universal prose floor — Orwell's six rules, four faults (dying metaphors, verbal false limbs, pretentious diction, meaningless words), prose inflation filters. Every word meant to be read. |
| `.claude/skills/composing-beats/references/runtime-surface.md` § Prep-entity floor | The prep-entity craft floor every prep skill must meet — stub check, PC-Connection Requirement, Toy fields, combat calibration, prose pass. |
| `.claude/skills/composing-beats/references/audits.md` § Sandbox doctrine | Anti-railroading doctrine — pressures not plots, the three-clue rule, PC gravity, if-ignored. |
| [[exemplar-quality-rubric\|exemplar-quality-rubric.md]] | The concrete quality bar distilled from 11 published RPG documents; DM-facing output is audited against it. |
| [[exemplar-quality-rubric-structure\|exemplar-quality-rubric-structure.md]] | Structure, retrieval, numbers, mechanics checks (R1–R10). |
| [[exemplar-quality-rubric-running\|exemplar-quality-rubric-running.md]] | Running, improvisation, trust, intent, safety checks (R11–R20). |
| [[exemplar-quality-rubric-layout\|exemplar-quality-rubric-layout.md]] | Markdown-native layout criteria — structure, visual hierarchy, artifact placement. |
| [[exemplar-quality-rubric-packaging\|exemplar-quality-rubric-packaging.md]] | Adoption and packaging criteria — optional content, table-facing artifacts. |
| [[art-style\|art-style.md]] | The campaign's visual identity for visual-aids — base style prompt, era/costume, character rendering. |
| [[lines-and-veils\|lines-and-veils.md]] | The table's content boundaries — Lines (forbidden) and Veils (fade to black). |
| [[safety-tools\|safety-tools.md]] | Safety tools for play — sensitive-topic discussion, hard lines vs off-screen, the "pause" cue. |
| [[homebrewing-mechanics\|homebrewing-mechanics.md]] | The generative method for new 5e mechanics — flavor-first, SRD-splice, iterate, edge-test. |

## GM craft & methodology reference

Recreated external GM-expert methodology (Sly Flourish's LGMRD, SRD 5.2
DM toolbox) — session-running technique, not this repo's own process.

| File | Covers |
|---|---|
| `.claude/skills/composing-beats/references/runtime-surface.md` § The lazy prep toolkit and eight-step checklist | Checklist-style GM toolkit — prep tools, campaign-building steps, running techniques, the eight-step Lazy RPG Prep checklist and its 3-step reduced version. |
| [[session-zero-checklist\|session-zero-checklist.md]] | Running a D&D session zero — theme, safety tools, patron, relationships table. |
| [[building-an-rpg-group\|building-an-rpg-group.md]] | Finding, screening, and retaining players. |
| [[npc-guidance\|npc-guidance.md]] | How NPCs guide the party — one speaker per moment, the relevance gate. |
| [[combat-encounter-checklist\|combat-encounter-checklist.md]] | Nine elements for building a dynamic set-piece combat encounter. |
| [[lazy-combat-encounter-building\|lazy-combat-encounter-building.md]] | Building and gauging 5e encounters from story context — average-HP formula, deadliness benchmark. |
| [[lazy-encounter-benchmark\|lazy-encounter-benchmark.md]] | Quick mental formula for flagging a deadly encounter. |
| [[quick-encounter-building\|quick-encounter-building.md]] | Quick-reference CR-to-level ratios plus tuning methods. |
| [[gameplay-toolbox\|gameplay-toolbox.md]] | SRD 5.2 DM toolbox — travel pace, backgrounds, hazards, poison, traps, encounter difficulty. |
| [[gameplay-toolbox-combat\|gameplay-toolbox-combat.md]] | SRD 5.2 combat difficulty, XP budgeting, troubleshooting. |
| [[gameplay-toolbox-traps\|gameplay-toolbox-traps.md]] | SRD 5.2 trap design, mechanics, example traps by difficulty. |
| [[zone-based-combat\|zone-based-combat.md]] | Zone-based combat replacing the 5-foot grid with ~25-foot zones. |
| [[theater-of-the-mind-extended\|theater-of-the-mind-extended.md]] | Extended guidelines for running combat without a grid. |
| [[theater-of-the-mind-abbreviated\|theater-of-the-mind-abbreviated.md]] | A separate, shorter treatment — the cautious-movement understanding, the 25-foot default, aphantasia accommodation, and where theater-of-the-mind sits among gridded and zone play. |
| [[tools-for-5e-improvisation\|tools-for-5e-improvisation.md]] | Formulas for improvising DCs, damage, statistics, deadly encounters, hordes, names. |
| [[quick-tricks-for-lazier-5e-games\|quick-tricks-for-lazier-5e-games.md]] | Shortcuts for running 5e faster and looser — initiative, dice math, passive scores. |
| [[stress-effects\|stress-effects.md]] | Stress checks and effects — an alternative to generic madness/frightened/stunned. |
| [[lazy-solo-5e\|lazy-solo-5e.md]] | Playing solo, GM-less 5e dungeon crawls via roll tables. |
| [[read-me-first\|read-me-first.md]] | Orientation notes for the source LGMRD Obsidian vault (Dice Roller plugin, attributions). |

## Root docs

| File | Covers |
|---|---|
| [[domain\|domain.md]] | How engineering skills should consume this repo's domain documentation — the domain is the process, not the campaign. |
| [[triage-labels\|triage-labels.md]] | Maps the five canonical triage roles to this repo's actual GitHub label strings. |
| [[issue-tracker\|issue-tracker.md]] | GitHub issues track the campaign-OS system itself, never campaign content — see the domain doc above. |
