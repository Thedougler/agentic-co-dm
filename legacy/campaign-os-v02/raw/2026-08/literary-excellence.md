> Superseded by [REFACTOR-PLAN.md](../../REFACTOR-PLAN.md) — the convergence refactor that reworked, executed, or retired this spec.

# Elevate Campaign-OS Literary Excellence Gate for `status: planned` and `status: canon`

You are a senior systems engineer + literary style architect working inside the **campaign-os** monorepo (D&D campaign wiki + Node/Python tooling). Your sole mission is to implement a new, higher tier of **objective, deterministic literary excellence** that applies **only** to pages whose YAML frontmatter contains `status: planned` or `status: canon`. Pages with `status: prepped` (or any other value) remain under the existing “good enough for play” bar.

This work must respect the founding doctrine (ADR-0002 and its amendment chain 0004/0005/0006/0010/0015):

- Deterministic sensors > prose guides.
- Findings are gated on *presence*, not exit-code severity.
- Ratchet floors only ever decrease.
- Shape lives in `_templates/`; quality judgment that cannot be made fully deterministic stays in companion `-prep` skills.
- Never break the two-producer / one-gate architecture or the opt-in status of `dndsim`.

All new sensors live inside a new Vale style package so they can be switched on/off cleanly and do not pollute the existing advisory/hard Vale configurations.

---

## 1. Research-backed literary standards to encode

The following ten (plus supporting) practices are drawn from:

- Write-good / proselint / Microsoft / Google style packages already present in the repo.
- Established fiction craft (Hemingway “iceberg”, show-don’t-tell, active voice, concrete sensory detail, sentence rhythm, avoidance of filter words & distancing language).
- Contemporary award criteria (Hugo/Nebula short-fiction advice, Writers of the Future unwritten principles, Pulitzer-adjacent craft notes).
- AI-tells research (vale-ai-tells package patterns) because LLM-generated campaign prose is the dominant production path.

They are deliberately chosen to be **fully deterministic** (regex, POS-aware sequences where Vale supports it, occurrence counts, simple metrics). No LLM-in-the-loop judgment is required at lint time; remediation guidance is written so that even Haiku-class models can rewrite cleanly.

### The 12 core sensors (implement all)

Create a new Vale style directory:

docs/vale-styles/CampaignLiterary/
├── meta.json
├── FilterWords.yml
├── WeakAdverbs.yml
├── PassiveVoiceLiterary.yml
├── TellingEmotions.yml
├── AbstractAbstractions.yml
├── ThereIsThereAre.yml
├── HedgingIntensifiers.yml
├── ClichéNarrative.yml
├── PurpleProseDensity.yml
├── SentenceStarterRepetition.yml
├── DialogueTagWeakness.yml
└── Nominalization.yml

(You may split or rename files for clarity, but every rule below must exist.)

#### 1. FilterWords (existence + sequence)

Flag distancing filter constructions that put a cognitive layer between the reader and the fiction:

- `he/she/they (saw|noticed|realized|felt|heard|watched|observed|knew|understood) that`
- `it seemed that`, `it appeared that`, `there was a sense that`
Message: “Filter word distance. Rewrite as direct sensory action or interiority. Example: ‘She realized the door was locked’ → ‘The door did not yield.’”
Level: warning (promote later).

#### 2. WeakAdverbs (existence)

Flag manner adverbs ending in `-ly` that modify a weak verb (especially dialogue and action):

- `said quietly`, `walked slowly`, `looked carefully`, `smiled sadly`, etc. (maintain a curated list of the 40 most common offenders + a catch-all `\b\w+ly\b` with exceptions for necessary domain terms).
Message: “Weak adverb. Prefer a stronger verb or concrete action. ‘said quietly’ → ‘whispered’ or show the lowered voice.”
Level: warning.

#### 3. PassiveVoiceLiterary (existence / sequence)

Stricter than the existing write-good Passive rule. Flag agentless or weakly agented passives in narrative prose (exclude rules text, stat blocks, and mechanical sections via TokenIgnores or scope).
Message: “Passive construction weakens immediacy. Convert to active voice with a clear agent.”
Level: warning.

#### 4. TellingEmotions (existence + substitution suggestions)

Flag “was/were + emotion adjective” and common telling phrases:

- `was angry`, `felt sad`, `was terrified`, `grew furious`, `became afraid`, `looked worried`
Message: “Telling emotion. Show through body, dialogue, or concrete action. ‘He was angry’ → ‘His jaw tightened until the hinge popped.’”
Level: warning. Provide 3–4 canonical rewrites in the message or a linked remediation note.

#### 5. AbstractAbstractions (existence)

Flag high-abstraction nouns that rarely earn their keep in immersive fiction:

- `atmosphere of`, `sense of unease`, `feeling of dread`, `air of mystery`, `aura of`, `quality of`, `nature of the`
Message: “Abstract summary. Replace with concrete, sensory particulars the characters can perceive.”
Level: warning.

#### 6. ThereIsThereAre (existence)

Flag existential openers that delay the real subject:

- `There is/are/was/were [a/an/the] \w+`
Message: “Delayed subject. Lead with the concrete noun or actor. ‘There was a dagger on the table’ → ‘A dagger lay on the table.’”
Level: suggestion → warning after first drain.

#### 7. HedgingIntensifiers (existence)

Flag empty intensifiers and hedges that dilute voice:

- `very`, `really`, `quite`, `somewhat`, `rather`, `a bit`, `sort of`, `kind of`, `just` (when not temporal), `literally` (when not literal)
Message: “Empty intensifier. Delete or replace with a precise concrete detail.”
Level: warning.

#### 8. ClichéNarrative (existence – expand existing)

Extend the current CampaignOS / write-good cliché list with narrative-specific dead phrases common in RPG prose:

- `a dark and stormy night`, `little did he know`, `in the nick of time`, `the rest is history`, `only time will tell`, `at the end of the day`, `the calm before the storm`, `heart skipped a beat`, `blood ran cold`, `eyes widened in horror`, etc.
Message: “Narrative cliché. Invent a fresh image or cut the phrase entirely.”
Level: warning.

#### 9. PurpleProseDensity (occurrence / metric)

Flag paragraphs that contain ≥ 4 stacked adjectives or adverbs before a noun/verb, or consecutive sentences each carrying ≥ 3 modifiers.
Message: “Purple density. Prefer one precise image over a pile of modifiers.”
Level: warning. (Use occurrence + simple regex; metric if needed.)

#### 10. SentenceStarterRepetition (repetition / occurrence)

Within a 5-sentence window, flag three or more sentences that begin with the same pronoun or the same function word (`He`, `She`, `The`, `Then`, `And`, `But`).
Message: “Repetitive sentence rhythm. Vary openings; interleave sensory, dialogue, and action starts.”
Level: suggestion.

#### 11. DialogueTagWeakness (existence)

Flag weak or overused dialogue tags beyond the first two in a scene:

- `said softly`, `exclaimed`, `replied angrily`, `asked curiously`, plus the classic “said + adverb” pattern.
Prefer action beats or bare `said`/`asked`.
Message: “Weak dialogue tag. Replace with an action beat or bare ‘said’.”
Level: warning.

#### 12. Nominalization (existence + substitution)

Flag heavy nominalizations that turn verbs into abstract nouns:

- `the utilization of`, `the implementation of`, `the decision to`, `in the event of`, `for the purpose of`
Message: “Nominalization. Prefer the living verb. ‘the decision to attack’ → ‘they decided to attack’ or simply ‘they attacked’.”
Level: warning.

---

## 2. Integration requirements (must implement)

1. **Status gating**  
   The new style is applied **only** when the file’s frontmatter contains `status: planned` or `status: canon`.  
   - Prefer a small Node helper in `utils/scripts/lib/prose-scope.mjs` (or extend the existing one) that emits a temporary Vale config or uses Vale’s `--filter` / scoped styles.  
   - Do **not** apply these rules to `status: prepped`, mechanical pages, SRD mirrors, or `content/external/`.  
   - Frontmatter schema already exists; do not invent a new schema.

2. **Configuration surface**  
   - Add `CampaignLiterary` to `.vale-hard.ini` (or a new `.vale-literary.ini` that the hard path can opt into).  
   - Keep the existing advisory Vale path untouched.  
   - Update `lint-findings.mjs` `collectFindings()` so the new producer is visible and participates in the single baseline/ratchet/drain pipeline.  
   - Document the severity lifecycle in `utils/scripts/lint-rules/README.md` and the new style’s own `meta.json`.

3. **Remediation guidance**  
   Every rule message must contain:
   - One-sentence diagnosis.
   - One concrete “before → after” rewrite example.
   - A one-line pointer to the relevant craft principle (e.g. “Show, don’t tell – Hemingway iceberg”).

   Store longer remediation notes in `docs/vale-styles/CampaignLiterary/remediation.md` so agents can open them.

4. **Ratchet & promotion path**  
   - Ship every rule as `warning`.  
   - Seed a floor only for files that already have `status: planned|canon`.  
   - After a successful `/drain` wave that reaches zero live findings on the new rules, the promote step may flip them to `error` (presence gate) exactly as ADR-0006 describes.  
   - Mark any purely corpus-relative metric (if you add one) as `nonPromotable`.

5. **False-positive hygiene**  
   - Extend `UNLINKED_MENTION_STOPLIST` / vocabulary accept lists only if a new rule collides with legitimate domain language.  
   - Exclude fenced code, callouts of type `check`/`statblock`/`spell`, and tables by default (reuse existing TokenIgnores / prose-scope logic).  
   - Dialogue inside `[!read-aloud]` may keep a slightly higher tolerance for tags; document the exception.

6. **Tests**  
   - Add unit tests under `utils/scripts/lint-rules/` (or a new `CampaignLiterary.test.mjs`) that feed known-good and known-bad excerpts and assert the expected findings.  
   - Include at least one `status: prepped` file that must produce **zero** findings from the new style.

7. **Documentation & ADRs**  
   - Write a short ADR (next free number) that records the decision: “Literary excellence sensors for planned/canon content”.  
   - Update `docs/guardrails/PROJECT.md` (or the relevant PJ entry) and the `llm-wiki-lint` skill so agents know the higher bar exists.  
   - Fix the two stale runbook pointers noted in the context pack (session_health.sh and build_site.sh) as a free side-effect while you are touching the scripts tree.

8. **Do not**  
   - Touch the dndsim opt-in status (ADR-0015).  
   - Re-enable the currently commented pre-commit markdownlint hooks until the W25 scope problem is solved.  
   - Introduce any non-deterministic (LLM) check into the lint path.  
   - Lower the bar for `prepped` content.

---

## 3. Execution order (follow strictly)

1. Read the live sources of truth:
   - `utils/scripts/lint-rules/README.md`
   - `.obsidian-linter.jsonc`
   - `.vale.ini` / `.vale-hard.ini`
   - `utils/scripts/lib/lint-findings.mjs`
   - `utils/scripts/lib/prose-scope.mjs` (or equivalent)
   - The existing CampaignOS Vale styles
2. Create the `CampaignLiterary` style with the 12 rules above (messages must be Haiku-friendly).
3. Wire status gating.
4. Integrate into `collectFindings` and the ratchet pipeline.
5. Add tests + seed baseline only for planned/canon files.
6. Write the ADR + update the two stale shell comments.
7. Run a full `lint:worklist --include-vale` on a representative set of planned/canon pages and confirm the new findings appear and are actionable.
8. Commit with a message of the form:  
   `feat(lint): CampaignLiterary Vale style – higher bar for planned/canon prose`

After the commit, print a short summary of:

- New rule files created
- How the status gate works
- Any residual false-positive risk and how it is mitigated
- The exact promote path for the new rules

You have full permission to edit any file or install any dep.

Begin by reading the live registry files listed in step 1.
