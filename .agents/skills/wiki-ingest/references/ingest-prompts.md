# Ingest Prompt Templates

These are the mental frameworks to use when distilling a source into wiki pages. The source is **evidence**. Extract **ideas** and route them; do not copy the file as a wiki note.

## Knowledge Extraction Frame

When reading a source document, ask yourself:

1. **What are the discrete ideas in this document?**
   Claims, creative decisions, mechanics, descriptions, relationships. Each idea gets a destination: an existing page, a justified new page, staged/unresolved, or canon under the rule in `llm-wiki`.

2. **Who or what is mentioned that already has a page, or deserves a justified new one?**
   Prefer the existing page. People, tools, organizations, projects → entity pages only when the idea has coherent standalone scope.

3. **What does this document teach you how to do?**
   Procedures, workflows, techniques → skills pages, or updates to existing skill pages.

4. **What claims does this document make, and with what confidence?**
   Each claim needs a source attribution. Extracted claims need no marker. Synthesized claims are `^[inferred]`. Unclear or conflicting claims are `^[ambiguous]`.

5. **How does this connect to what the wiki already knows?**
   This is the most important question. Route by topic, not by the source outline. The value of the wiki compounds through connections.

## Paper Extraction Frame

For academic papers (ML/AI/LLM/VLM and similar), the generic frame above misses what makes a paper legible. Add these questions:

1. **What problem does it solve, and what's new?** The one-sentence thesis + the single most important result.
2. **What is the method?** Which figure shows the architecture/pipeline? Sketch it as a Mermaid flowchart — capture the data flow, not just the component names.
3. **What are the core equations?** The 1–3 that define the mechanism — keep them as math (`$$…$$`), not prose.
4. **What's the experimental setup and the headline numbers?** Datasets, baselines, and the metric table the paper is judged on.
5. **What are the ablations and limitations?** What did they vary, and what does the method *not* do?

These map onto the Paper Deep-Dive Template in `llm-wiki/SKILL.md`. The goal is a page a reader could study instead of the PDF — figures, equations, and results included.

## Synthesis Frame

When a new source covers ground that existing pages already cover:

- Prefer the existing page; do not duplicate
- If the new source agrees, strengthen claims with additional attribution
- If it disagrees with established **canon**, keep the existing fact, mark `^[ambiguous]`, and surface a **proposal** for the DM (`docs/agents/work.md`). Do not overwrite. Named ingest approves those sources; it does not grant silent canon edits
- If it disagrees on a non-campaign knowledge page, note both positions without dropping either
- If it adds nuance without conflict, weave it into the existing narrative
- Polish expression and structure; keep settled intent and stated mechanics

## Cross-Reference Discovery

After extracting knowledge, look for these connection patterns:

- **Is-a**: "Transformers are a type of neural network" → link from transformer page to neural-network page
- **Uses**: "RLHF uses reward models" → link from RLHF to reward-models
- **Contrasts-with**: "CNNs vs. Transformers for vision" → mutual links
- **Part-of**: "Attention is a component of transformers" → link from attention to transformers
- **Created-by**: "Transformers were introduced by Vaswani et al." → link to entity page
- **Applied-in**: "Transformers are used in GPT" → link from transformers to GPT
