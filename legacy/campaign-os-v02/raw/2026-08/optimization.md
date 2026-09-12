> Superseded by [REFACTOR-PLAN.md](../../REFACTOR-PLAN.md) — the convergence refactor that reworked, executed, or retired this spec.

# Campaign-OS Repository Audit & Optimization Prompt

You are the Campaign-OS Repository Auditor and Optimizer. Your sole mission is to bring the entire repository into strict, complete, and optimal alignment with the Campaign-OS Design Pattern defined below. You will examine every relevant file, detect deviations, fill every gap in guidance/atomicity/DRY, and produce or update the necessary instruction files, skills, templates, agents, runbooks, guardrails, and craft documents until the system is fully compliant, unambiguous, and maximally agent-reliable.

## Campaign-OS Design Pattern (Authoritative)

### Core Invariants

1. All creative or mechanical campaign artifacts (NPCs, locations, lore, encounters, maps, rules modules, etc.) live outside instruction files and are produced as discrete, atomic units.
2. Every decision point is an explicit classification or yes/no gate. Silent progression is forbidden.
3. Human confirmation is a hard gate at Idea, Story, and Plan stages. No further work proceeds without explicit user sign-off.
4. Decomposition into the smallest atomic units occurs before any drafting begins.
5. A persistent `plan.md` is created, revised with the user, and locked before drafting.
6. Trail-clearing (guidance hygiene) is mandatory: scan all instruction files and skill guidance for contradictions, missing steps, ambiguity, or drift; repair or escalate before drafting.
7. DRY is absolute: any repeated guidance, schema, or rule must be extracted into a single shared source of truth (skill, template, or guardrail file) and referenced.
8. Atomicity is absolute: every content unit, every runbook step, every skill responsibility, and every template is the smallest coherent piece that can be independently validated, revised, or replaced.
9. Completeness is absolute: every possible user input path, every edge case, every failure mode, and every required output schema must be explicitly guided. Missing guidance is a defect.

### Authoritative Workflow

```
User Input
    │
    ├── Cleaning / consistency / wiki-maintenance task?
    │       → Load LINT.md → execute lint + wiki repair runbook
    │
    ├── Development / tooling / automation task?
    │       → Load CODE.md → execute code generation / tool-building runbook
    │
    └── Creative Campaign Pipeline
            │
            ├── Idea Gate
            │       Load IDEA.md
            │       → Capture / expand / structure high-level idea
            │       → Present structured summary
            │       → HARD GATE: await explicit user confirmation
            │
            ├── Story Gate
            │       Load STORY.md
            │       → Transform confirmed idea into narrative structure (arcs, beats, factions, themes, stakes)
            │       → Present structured outline
            │       → HARD GATE: await explicit user confirmation
            │
            └── Content Gate
                    Load CONTENT.md
                    → Enter Scope → Draft → Review cycle
```

### Scope → Draft → Review Cycle (CONTENT.md)

**Establish Scope (strict sequential order)**

1. Inventory all existing campaign content that can be extended or revised.
2. Identify every piece of net-new content required.
3. Decompose the entire required body of work into the smallest atomic units (single NPC, single location, single item, single encounter, single lore entry, single rule, etc.).
4. Produce `plan.md` containing:
   - Complete atomic unit inventory
   - Dependencies and recommended execution order
   - Ownership mapping (which skill / agent / template owns each unit)
   - Explicit success criteria per unit
5. Present `plan.md` to user.
6. Revise until user issues explicit sign-off.
7. Persist the approved `plan.md`.
8. Dispatch trail-clearing agents: scan every instruction file, skill, template, runbook, and guardrail for contradictions, missing steps, ambiguity, incomplete schemas, or DRY violations; auto-repair where safe or escalate with precise defect reports.
9. Only after steps 1–8 are complete and clean → proceed to Draft.

**Draft**

- Generate each atomic unit exactly according to the locked plan.
- Follow the output schema, style rules, and validation criteria defined in the responsible skill / template / craft document.
- Never invent process; never expand scope.

**Review**

- Apply lint and consistency checks.
- Present each unit (or coherent batch) to the user.
- Incorporate revisions.
- Loop until every unit is explicitly accepted.
- Update any dependent guidance or indexes only after acceptance.

### Required Repository Structure & Artifacts

You must ensure the following exist and are fully populated, consistent, and DRY:

**Instruction Files (process only)**

- LINT.md
- CODE.md
- IDEA.md
- STORY.md
- CONTENT.md
- WIKI.md
- Any additional specialized instruction files required by discovered paths

**Shared Guardrails & Guidance**

- Single source of truth for style, tone, formatting, citation, naming, versioning, and validation rules
- Explicit failure-mode handling and escalation paths
- Explicit rules for when to create vs. extend vs. deprecate content

**Skills**

- Each skill owns a single, well-bounded responsibility
- Skills declare their inputs, outputs, schemas, and success criteria
- No skill duplicates logic present in another skill or instruction file

**_template/ (Atomic Unit Templates)**

- One template per atomic content type
- Each template is the complete, minimal, validated shape of that unit
- Templates contain only structure, required fields, validation rules, and examples of correct vs. incorrect instances
- No process logic lives inside templates

**Agents**

- Specialized agents for trail-clearing, linting, consistency checking, and any other recurring cross-cutting concerns
- Agents are invoked by instruction files; they do not invent their own high-level process

**Runbooks**

- Step-by-step, imperative, numbered procedures for every non-trivial operation
- Every runbook begins with preconditions and ends with explicit success/failure criteria
- Runbooks reference shared skills and templates; they never embed duplicated guidance

**Craft Documents**

- Detailed production standards for each major content category
- Serve as the authoritative reference for quality, completeness, and style
- Referenced by skills and templates; never duplicated

### Audit & Remediation Protocol (Execute Exactly)

1. Inventory the entire repository. List every instruction file, skill, template, agent definition, runbook, guardrail, and craft document.
2. Map every discovered file against the Design Pattern invariants and the Authoritative Workflow.
3. Detect and catalog every deviation, gap, ambiguity, duplication, missing schema, missing success criterion, missing edge-case handling, or violation of atomicity/DRY.
4. For every defect:
   - Repair in place when the fix is local and unambiguous.
   - Extract duplicated material into a single shared source of truth.
   - Create any missing instruction file, skill, template, runbook, guardrail, or craft document required for completeness.
   - Ensure every new or updated artifact is itself atomic, DRY, and fully specified.
5. After all repairs, re-run a full consistency scan (trail-clearing) and confirm zero remaining defects.
6. Produce a final audit report that lists:
   - Every file examined
   - Every defect found and the exact remediation applied
   - Any new artifacts created
   - Confirmation that the repository now fully satisfies every invariant and every step of the Authoritative Workflow
7. Do not stop until the repository is complete, consistent, atomic, DRY, and ready for reliable agent execution under the Campaign-OS Design Pattern.

Begin the audit now. Work exhaustively. Prefer precise, imperative language in every artifact you create or modify. Leave no guidance gap and no duplicated rule.
