---
name: world-tick
description: Post-session world advancement ritual — walks through active factions, NPCs, and plot threads one at a time, collaborates with the DM on each thread's offscreen goal, uses a real d20 roll to resolve it, then stages reviewed ledger lines and applies only approved surgical changes. Run when Nick asks for off-screen advancement (not auto-chained from session-recap). Trigger on "world tick", "advance the world", "between sessions", "offscreen actions", "faction tick", "what moved while the party was elsewhere", or any request to update the world state after a session.
---

# World Tick
## Work gate

Wrapup. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Off-screen movement is proposed Work grounded in wiki pages and/or D&D 5e rules; cite `[[pages]]`, surface contradictions to the DM, and never present invention as wiki fact. Outcomes remain proposed until accept, then make surgical owner-page updates. Unused prep is not canon.


The world didn't pause while the party played. Now you find out what happened offscreen.

This is a collaborative ritual — efficient, methodical, one thread at a time. You read the situation, propose what that faction or NPC was trying to do, the DM confirms or redirects, the dice decide the outcome, and you stage a reviewed ledger proposal before any write. No gaps, no deferred updates, no vague notes.

## Canon Discipline

This is the most important rule in this skill: **every claim you make must be grounded in something you have read.** Not inferred. Not extrapolated. Read.

Before proposing a thread, read its situation file. Before naming an NPC's status, read their page. Before describing what anyone knows or doesn't know, verify it in the wiki. If you don't have a file open that supports the claim, either go read it or don't make the claim.

The specific failure modes to avoid:

- **Timing errors** — a clock doesn't start until its trigger fires. Read the situation file to find what the trigger actually is before assuming it's in motion.
- **DM notes leaking into world state** — if something is in a DM design note, it is intent, not fact. It has not happened until a session log entry says it happened.
- **Invented consequences** — a fight in open water is invisible. A missed check-in that hasn't happened yet has no consequences yet. Don't generate downstream effects from events that haven't resolved.
- **Assumed destinations** — never state or imply where the party is going next. That is Session N+1's business, not yours.

When in doubt: read the file, then speak. Never the other way around.

---

## Step 1: Find the Session Recap

Look for the most recent session material in this order:

1. `wiki/journal/sessions/<campaign-slug>/<NN>/` — that night’s plan/beats (preferred)
2. `wiki/journal/sessions/<campaign-slug>/<NN>/Session-<NN>-Recap.md` — player-facing recap (`type: recap`)

If neither exists, ask:

> "I don't have a session recap to work from. Give me a quick rundown — what the party did, who they interacted with, what threats are active, what they ignored — and I'll work from that."

Accept whatever they provide. You need: who the party engaged with, what locations they were in, what threats are visibly in motion, what they left alone.

---

## Step 2: Identify Active Threads

Read `wiki/<campaign>/fronts/00 Fronts.md` alongside the recap. Then read the situation file for any thread you're considering before proposing it — don't propose a thread based on the index summary alone.

**Only tick threads the party has touched.** A faction the party has never encountered doesn't get a turn — their drama belongs to a session where it can matter. The world tick is about consequences the players can feel, not background noise they'll never see.

A thread qualifies for this tick if:
- The party directly engaged with it this session or in recent sessions
- A faction or NPC the party knows has clear motivation to react to what the party just did
- The party's absence from a thread they were previously involved in is itself a meaningful choice the world would notice

**Before proposing any thread, read its situation file and verify:**
- The thread's current state is actually what you think it is
- Any clocks or triggers you're referencing have actually fired — check the trigger condition in the file, not your assumption about it
- The thread's key actors are doing what their file says they're doing, not what seems narratively logical

Order threads by proximity to the party's active interests: threads they touched this session first, then threads where their recent actions created pressure, then any with hard ticking clocks confirmed in the file. Leave dormant threads, distant factions, and NPCs the party hasn't met out of the tick entirely.

Present your list before proceeding:

> "I'm planning to tick these threads: [list with one-line summaries]. Anything to add, skip, or reorder?"

Wait for confirmation.

---

## Step 3: Tick Each Thread

Work through the list one at a time. Don't move to the next thread until the current one is fully written.

### 3a. Read and Propose

Read the situation file in full. Read the NPC or faction file if one exists. Only after reading both form a single clear sentence about what this entity was trying to accomplish during this interval. Do not rely on what you remember from earlier in the conversation — re-read the file.

> "[Entity] was trying to [specific concrete action] this week. Does that track, or do you see it differently?"

Keep it tight — one action, one sentence. The DM may redirect. If they do, use their version. This is their world and they may have ideas you don't. The goal you confirm here is what the roll is resolving.

### 3b. Roll

Once the goal is agreed:

> "Roll a d20."

Wait for the number. Don't interpret yet.

### 3c. Interpret

| Roll | Outcome |
|------|---------|
| 1–5 | **Setback.** Their attempt failed or backfired. Something went wrong — plans exposed, resources spent badly, opposition stiffened, an unexpected complication arose. |
| 6–15 | **Partial.** They made real progress but hit friction. Something worked, something didn't. A complication or cost accompanies the advance. |
| 16–20 | **Full success.** They accomplished what they set out to do. The world shifts. |

Be specific and interesting. Every result — including setbacks — should shift something the party will eventually feel. Name what changed: which NPC moved and where, what was learned or exposed, what resource was spent or gained, what the party will walk into differently. A low roll isn't "nothing happened" — it's a faction that overreached, tipped their hand, or got hit from a direction they didn't see.

Follow faction logic, not narrative convenience. The Takowan rolls a 4 while mapping Passage contacts? It doesn't just fail quietly — a contact noticed the questions, word is moving, and the next person the Takowan approaches will be warned. The world is honest, and honesty is more interesting than managed drama.

Keep tone consistent with the campaign; outcomes have weight and consequence; outcomes should feel earned and real, not dramatic for its own sake. Read the situation file's voice before writing the result.

**What the result must not do:**
- Reference DM design notes as established world facts — if it hasn't happened in a session log, it hasn't happened
- Imply consequences from unresolved events (the fight isn't over, the ship hasn't been reported missing yet)
- State or imply where the party goes next — you don't know that
- Invent NPC knowledge, locations, or status not supported by their file

### 3d. Stage the reviewed change

Add the proposed change to `inbox/world-tick-<YYYY-MM-DD>.md` before moving to the next thread:

Do not edit the owning pages during this pass. The inbox ledger carries the proposed before/after state, evidence, and fill warning for later confirmation.

### 3e. Confirm and Continue

After staging the proposal:

> "Staged — [one sentence on the proposed change]. Next up: [Thread Name]. Ready?"

Wait for go, then move to the next thread.

---

## Step 4: Close Out

Close out by marking each ledger line with its evidence, the proposed before/after state, and any unresolved fill confirmation. Do not apply it in this skill until Nick/Co-DM approves the ledger.

## ai-co-dm write boundary

Stage proposed advances in `inbox/world-tick-<YYYY-MM-DD>.md` after triage and per-thread review. Do not write a front, faction, NPC, location, or `hot.md` until Nick/Co-DM confirms the interpretation. Once approved, apply only confirmed surgical changes and return a bounded receipt. Never assume a destination, add a new front, or use a raw transcript as evidence. After a resolved faction turn, append a row to that faction's Faction Turn Log. Current Turn at page create is the planned next move with no roll. Agenda clock lives on the faction page; `hot.md` may point at the faction. Quest portents stay with `narrative-islands`.

## Session-to-world spine

Run when Nick asks for off-screen movement — **not** as a mandatory follow-on to `session-recap` (recap is narrative only). Prefer Campaign Editor / `reconciling-session-evidence` for owner-page canon; use the filed `Session-<NN>-Recap.md` as player-safe narrative context. Leave unresolved evidence gated rather than inventing continuity.

## Momentum and echo gate

For each touched thread, record the echo of both action and inaction: what the
party changed, what they left exposed, what independent factions did next, and
which visible consequence or opportunity will meet them later. Strongholds and
resources are political leverage, not static scenery. Advance living factions
from their established motives, then route reviewed clock changes through the
existing ledger and approval boundary.
