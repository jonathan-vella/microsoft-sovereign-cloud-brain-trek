---
name: unslop
description: Edit training content so it reads like a person wrote it. Removes AI writing patterns, filler, and vague claims from pages under site/src/content/docs. Use on every page you write or materially rewrite, before opening a PR.
---

# Unslop

Edit prose so it is plain, specific, and easy to read. Keep the meaning and every fact.

Adapted for this site from the `unslop` skill in
[cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack/skills/unslop). The rules below are rewritten
for technical training content.

## Scope

- Apply to prose you add or materially rewrite. Do not restyle untouched paragraphs in the same PR; that hides the
  real changes in the diff.
- Never change official product names, Azure Policy initiative names, API names, or quoted legal and regulatory text.
- Do not touch front matter keys, Starlight asides (`:::note`), `KnowledgeCheck` or `DiagramContainer` syntax, code
  blocks, or Mermaid blocks. Edit only the text inside them.
- Front matter `description` follows the same rules and must stay between 20 and 220 characters.

## Process

1. Read the page once for meaning.
2. Check it against the rules below.
3. Rewrite the sentences that break a rule. Keep the tone of a Microsoft Learn module: direct, second person where it
   helps, no hype.
4. Run `npm run lint:content -- --verbose` from `site/` and check the style warnings for the files you changed.

## Rules

### Claims and sources

- **R1. Name the source.** Replace "experts say", "studies show", or "industry analysts" with a named Microsoft source,
   or cut the claim.
- **R2. Cite volatile facts inline.** Status (GA, preview, retired), dates, limits, sizes, prices, and legal claims link
   to the Microsoft Learn or Microsoft blog page they come from. Stable concepts can rely on the page's `## Sources`
   section.
- **R3. No generic endings.** Cut closing lines like "the future of sovereign cloud is bright". End with the next step
   or a concrete fact.
- **R4. Say what it does.** Replace feelings ("gives you peace of mind", "unlocks agility") with the mechanism or a
   number ("keeps encryption keys in a Managed HSM you control", "supports up to 16 machines per instance"). If a
   sentence would fit unchanged in any vendor's docs, cut it.

### Words

- **R5. Plain words.** use (not leverage or utilize), help (not facilitate), many (not numerous), if (not in the event
   that), to (not in order to), because (not due to the fact that).
- **R6. No AI vocabulary.** Avoid: delve, crucial, pivotal, tapestry, testament, underscore, vibrant, showcase,
   seamless, robust, cutting-edge, game-changer, realm, embark, foster, garner, intricate, interplay, paradigm,
   synergy, holistic, landscape (when abstract), journey (when not a learning path).
- **R7. Say "is" and "has".** Replace "serves as", "stands as", "boasts", "features" with "is" or "has".
- **R8. One term per thing.** Pick one name for a concept and repeat it. Do not cycle synonyms such as "cluster",
   "instance", "deployment", and "environment" for the same object. Use the Microsoft Learn term.
- **R9. No metaphor nouns.** Avoid substrate, north star, flywheel, bedrock, nexus, vector (as "way"), surface (as
   "area"), harness (as "use").
- **R10. Cut adverbs that prop up weak verbs.** "significantly improves" becomes the measured change, or goes.
- **R11. Cut hedging stacks.** "could potentially be argued that it may" becomes "may".

### Sentences

- **R12. One idea per sentence.** Split sentences the reader has to read twice.
- **R13. Active voice.** Name the actor: "Azure Policy denies the deployment", not "the deployment is denied". Passive
    is fine when the actor is unknown or irrelevant.
- **R14. No "not just X, but Y".** State the point.
- **R15. No forced threes.** Use the number of items that actually exist.
- **R16. No false ranges.** "From edge sites to national clouds" only works if they sit on one scale. Otherwise list them.
- **R17. No dangling -ing phrases.** Cut trailing "..., ensuring compliance" or "..., highlighting the need for" unless
    the clause adds a fact.
- **R18. Whole sentences.** No arrows, symbol shorthand, or dropped articles in prose. Tables and diagrams can be terse.

### Formatting

- **R19. No em dashes.** Use a period or a comma. Do not swap in en dashes or spaced hyphens.
- **R20. Colons only before a list or an example.**
- **R21. Sentence case headings.** "Plan the management cluster", not "Plan The Management Cluster". Product names keep
    their capitals.
- **R22. No decorative emoji.** Remove emoji from headings and bullets, including ✅ learning-objective bullets.
- **R23. Bold sparingly.** Bold a term the first time it is defined, or a warning. Do not bold every product name.
- **R24. No bold-label lines.** Replace `**Duration:** 2 hours` style lines with a sentence or a table. A bold lead-in
    that names an item and is followed by new detail ("**Data Guardian.** Microsoft engineers...") is fine.
- **R25. Straight quotes.** Use `"` and `'`, not curly quotes.

### Tone

- **R26. No chatbot phrases.** Cut "Great question", "Let's dive in", "I hope this helps", "Happy learning".
- **R27. No sales tone.** Training content informs. Cut "industry-leading", "best-in-class", "world-class" unless quoting
    Microsoft and citing the source.

## Examples

| Before | After |
|---|---|
| Azure Local serves as a robust foundation, seamlessly bridging on-premises and cloud. | Azure Local runs VMs and AKS on your hardware and is managed from Azure through Azure Arc. |
| ✅ **Understand:** Understand disconnected operations. | Explain when to use disconnected operations. |
| It is important to note that EKM is in preview. | External Key Management is in preview ([source](https://learn.microsoft.com/azure/azure-sovereign-clouds/public/external-key-management)). |
| Edge RAG — now Agentic Retrieval — leverages local LLMs. | Agentic Retrieval was called Edge RAG until June 2026. It calls a model endpoint such as Foundry Local on Azure Local. |
