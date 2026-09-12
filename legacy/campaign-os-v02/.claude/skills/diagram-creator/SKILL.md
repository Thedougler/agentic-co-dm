---
name: diagram-creator
description: diagram-creator — flowchart, sequence, architecture, ER, class, state, Gantt, Git-graph craft for a Campaign OS repo (vault/ present). Use to document this repo's own process/architecture — docs/adr/, CONTEXT.md, a pipeline/skill-dependency flow — with Mermaid/PlantUML. Not a wiki-page Mermaid diagram (obsidian-markdown) or a battlemap (battlemap-render, visual-aids).
---

# Diagram Creator Skill

Builds text-based diagrams (Mermaid, PlantUML) documenting this repo's own process or
architecture — a pipeline flow in a runbook, a skill-dependency graph, a data-model diagram for
a frontmatter schema. Renders in GitHub, VS Code, and the Mermaid/PlantUML live editors; does
not render raster images directly.

## Workflow

1. **Confirm the target**: what process/system/concept to diagram, for which doc (a
   `vault/refs/runbooks/*.md` step, `docs/adr/*.md`, `CONTEXT.md`), and the audience.
2. **Pick the diagram type** from `.claude/skills/diagram-creator/references/diagram-types.md` —
   flowchart, sequence, architecture, ER, class, state, Gantt, mind map, or Git graph — matched
   to what's being shown (a decision → flowchart; a call sequence → sequence diagram; system
   layout → architecture).
3. **Pick the format**: Mermaid (default — renders natively in GitHub/Quartz) or PlantUML (for
   complex UML this repo's own tooling doesn't need natively).
4. **Write the diagram** from the matching template in
   `.claude/skills/diagram-creator/references/diagram-types.md`, keeping it simple, consistently
   named, and grouped with subgraphs/packages where it helps.
5. **Embed it** in the target doc inside a fenced ` ```mermaid ` (or ` ```plantuml `) block.

## Reference

| Need | File |
|---|---|
| Flowchart, sequence, architecture, ER, class, state, Gantt, mind map, Git-graph templates | `.claude/skills/diagram-creator/references/diagram-types.md` § Diagram Types |
| PlantUML sequence/component examples | `.claude/skills/diagram-creator/references/diagram-types.md` § PlantUML Examples |
| Color themes, direction, styling options | `.claude/skills/diagram-creator/references/diagram-types.md` § Customization |
| Rendering tools by use case | `.claude/skills/diagram-creator/references/diagram-types.md` § Rendering Tools |
