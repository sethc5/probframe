# Prompt Pack: Draft Module

**Task type:** Initial content draft
**Moves module from:** `scaffolded` → `draft`
**Input variables:** Replace all `{{VARIABLE}}` blocks before sending.

---

## How to use this prompt

1. Run `python3 scripts/generate_queue.py --next 1` to get the next pattern to draft.
2. Write a pattern brief first (see below) — paste it into `{{PATTERN_CONTEXT}}`.
3. Copy the pattern's `outline.md` into `{{OUTLINE_MD}}`.
4. Fill `{{PATTERN_NAME}}`, `{{PATTERN_ID}}`, `{{SECTION_NAME}}`.
5. Send the completed prompt to the model.
6. Paste the model's output back into `outline.md`, replacing the entire file.
7. Populate README metadata fields:
   - `Related patterns`
   - `Often combined with`
   - `Degrades into`
   - `Modframe instances`
   - `Last reviewed`
   - `Domains`
   - `Actors`
8. Set `Status: draft` in `README.md`.

---

### Writing the pattern brief ({{PATTERN_CONTEXT}})

Before filling the prompt, write 4–6 sentences answering these questions:

- What is the core mechanism? (one sentence — the structural logic, not a domain example)
- Who are the 2–3 most important actor types deploying or experiencing this pattern, and what do they want?
- What is the clearest cross-domain pair of examples — one from politics or institutional power, one from biology, economics, military, or ecology?
- Which primary sources (academic, legal, empirical, historical) are most directly relevant?
- Does this pattern appear in any Modframe modules? Which IDs?
- What does this pattern degrade into when its enabling conditions fail?

Example brief for pattern "Chokepoint Control":

> The deploying actor positions at a bottleneck through which targets must pass,
> extracting rent or exercising veto power over flow. Core actors: the controller
> (incentive: extract value or block opponents), the dependent (incentive: pass through,
> find alternatives), the regulator (incentive: prevent monopoly abuse or enable it).
> Political example: Senate Judiciary Committee controls judicial nomination flow
> (Modframe 108); biological example: keystone predator controls prey population flow
> through a habitat corridor. Key sources: Schelling "The Strategy of Conflict" (1960),
> Modframe modules 018, 039, 108. Degrades into Dependency Creation (040) when the
> controller shifts from extracting toll to building structural lock-in, or into
> Boundary Arbitrage (032) when targets find alternative routes outside the chokepoint.

---

## Prompt

You are drafting a pattern entry for **probframe**, a cross-domain catalogue of
problem-solving patterns. Probframe documents recurring structural patterns that appear
across politics, biology, law, economics, military strategy, ecology, and organizational
behavior. Each entry describes one pattern: how it operates, who deploys it and against
what, where leverage concentrates, under what conditions it works or breaks down, and
where it has been observed in practice.

**This is not domain-specific analysis.** You are documenting the abstract structural
logic, grounded in cross-domain evidence. The political science example and the
biological example are peers — neither is primary.

**Pattern:** {{PATTERN_NAME}} (ID: {{PATTERN_ID}})
**Section:** {{SECTION_NAME}}

**Pattern context (use this as your knowledge base before drafting):**

{{PATTERN_CONTEXT}}

---

### Non-negotiable rules

**1. Structural, descriptive voice.**
Write as a systems analyst would. No advocacy, no moralizing, no domain bias.
Avoid: *dangerous, exploitative, corrupt, predatory* used evaluatively.
Use: structural and incentive language — "the pattern concentrates leverage at X,"
"the deploying actor gains Y," "the target's options are constrained by Z."

**2. Explicit claim types on every factual assertion.**

- `[Observed]` — documented in a primary or high-quality secondary source.
  Attach an inline stub if you don't have the exact citation: `[Observed — source: TBD]`
- `[Inferred]` — follows logically from observed facts. State the reasoning in one sentence.
- `[Hypothesis]` — plausible but unverified. State what evidence would confirm or refute it.

No sentence that makes a factual claim may appear without one of these labels.

**3. Cross-domain instantiations are required.**
Every module must include at least two instantiations from different domains.
Political/institutional examples should link to Modframe module IDs where applicable.
Biological, economic, military, ecological, or organizational examples are equally valid
and equally required.

**4. Conditions of applicability are structural tendencies, not advice.**
Frame as: "This pattern is documented in contexts where [structural condition]."
Not: "Use this pattern when [condition]."
Both enabling and disabling conditions are required. Disabling conditions are as
analytically important as enabling ones.

**5. Scale awareness.**
Note the scale(s) at which the pattern operates where this is relevant and documentable.
Scale affects conditions of applicability — a pattern that works at the interpersonal
scale may fail at the institutional scale due to coordination costs, and vice versa.

**6. Resolution patterns are peers.**
If this pattern has a documented structural response or countermeasure that operates
as a distinct pattern, name it in the `Degrades into` or Analysis outline sections.
Do not treat the deploying actor's perspective as primary — the target's structural
options are equally part of the pattern description.

**7. Word count targets:**
- Summary: 3–5 sentences (60–100 words)
- Mechanism sentence: ≤ 30 words
- Actors and deployment context: 100–300 words total
- Operational sequence: minimum 4 steps, each 15–40 words
- Conditions of applicability: ≥ 3 enabling, ≥ 2 disabling
- Instantiations: ≥ 2 entries from different domains
- All other sections: 80–200 words each

---

### Your task

Fill in the outline below. Replace every placeholder. Do not add, remove, or rename
any section headings — preserve the exact structure.

**Current outline.md:**

```
{{OUTLINE_MD}}
```

**Output:** Return the complete filled `outline.md` in Markdown.
Output only the document — no preamble, commentary, or explanation outside it.

---

## Post-draft checklist (run before updating Status)

- [ ] No placeholder text remains
- [ ] All claims carry `[Observed]`, `[Inferred]`, or `[Hypothesis]` labels
- [ ] Summary is 3–5 original sentences
- [ ] Mechanism sentence is ≤ 30 words
- [ ] Operational sequence has ≥ 4 steps
- [ ] Conditions of applicability has ≥ 3 enabling and ≥ 2 disabling conditions, all labeled
- [ ] At least 2 instantiations from different domains
- [ ] Modframe instances noted (can be stub IDs at this stage)
- [ ] `Degrades into` targets named in failure modes or analysis outline
- [ ] No prescriptive framing in conditions section ("use this" → "documented in contexts where")
- [ ] Scale noted where relevant and documentable
- [ ] README has initial metadata fields populated (refined in citation pass)
- [ ] `Status: draft` set in README.md
