# Module Template

## README.md

```text
# [Pattern Name]

Purpose: [One sentence — what problem-solving structure this pattern documents.]

Status: empty

Tags: [comma-separated; see docs/schemas/readme_schema.json for recommended values]

Pattern class: [Section name, e.g., "01 Adversarial Patterns"]

Outline: see `outline.md`

Contributors: [names / links]

Related patterns: [comma-separated 3-digit pattern IDs]
Often combined with: [comma-separated 3-digit pattern IDs]
Degrades into: [comma-separated 3-digit pattern IDs]
Modframe instances: [comma-separated Modframe module IDs, e.g., 001, 047, 073]
Last reviewed: [YYYY-MM]

Domains:
  - [e.g., political, biological, economic, legal, military, organizational]

Actors:
  - name: [Actor type]
    type: [deployer | target | enabler | regulator | observer]

How to contribute:

- Use docs/prompts/draft_module.md to generate initial content
- Add citations under "Suggested sources" in outline.md
- Populate Modframe instances with relevant Modframe module IDs
- Propose visuals in figures/ and link from here
```

## outline.md

```markdown
# [Pattern Name]

**Summary:** 3–5 sentences. What this pattern is, why it recurs across domains, and
what structural feature makes it recognizable. Descriptive voice — no advocacy.

**Mechanism in one sentence:** ≤ 30 words. How the pattern operates at its core.

### Actors and deployment context

- **[Deploying actor type]** — [role]; incentive: [what drives deployment];
  constraint: [what limits deployment]. [claim label]
- **[Target actor type]** — [role]; response options: [what target can do];
  constraint: [what limits response]. [claim label]
- **[Enabling actor / infrastructure]** — [what enables the pattern to operate];
  constraint: [limits]. [claim label]

### Operational sequence

- **Step 1 — [Phase name]:** [concrete action — who does it, what triggers it,
  what changes in the environment]. [claim label]
- **Step 2 — [Phase name]:** [next concrete action and its structural effect]. [claim label]
- **Step 3 — [Phase name]:** [next concrete action]. [claim label]
- **Step 4 — [Outcome or consolidation phase]:** [how the advantage is locked in or
  extended]. [claim label]

### Where leverage concentrates

- **Chokepoints:** [where the deploying actor gains disproportionate control]. [claim label]
- **Bottlenecks:** [where delays, resource constraints, or information gaps concentrate]. [claim label]
- **Veto points:** [who can block, reverse, or escape the pattern]. [claim label]

### Conditions of applicability

**Enabling conditions** — documented when the pattern operates:

- [Structural condition 1]. [claim label]
- [Structural condition 2]. [claim label]
- [Structural condition 3]. [claim label]

**Disabling conditions** — documented when the pattern fails or degrades:

- [Condition under which the pattern collapses or reverses]. [claim label]
- [Second disabling condition]. [claim label]

### Common failure modes

- **[Mode name]** — [claim label] — [explanation; what it degrades into]
- **[Mode name]** — [claim label] — [explanation]

### What evidence would prove/disprove key claims

- [Dataset, case record, or cross-domain comparison that would confirm or refute the
  central mechanism claim]
- [What a contrary finding would look like across domains]
- [Comparative evidence that would test the conditions of applicability]

### Instantiations

- **[Domain A]:** [specific case]. [claim label — source]
- **[Domain B]:** [specific case]. [claim label — source]
- **[Domain C]:** [specific case]. [claim label — source]

*Modframe links:* See `Modframe instances` in README for specific federal power module IDs.

### Suggested sources

- [Full title]. [Author / Issuing body], [Year]. [URL or identifier].
- [Full title]. [Author / Issuing body], [Year]. [URL or identifier].
- [Full title]. [Author / Issuing body], [Year]. [URL or identifier].

### Analysis outline (6 parts)

1. **Pattern** — [what this pattern is and what relationship structure it operates on]
2. **Mechanism** — [why the pattern works — the structural logic]
3. **Instantiation** — [a specific, real cross-domain case study]
4. **Evidence** — [primary sources or data to show across domains]
5. **Countermeasures** — [≥ 2 documented structural responses or reforms — describe neutrally]
6. **Takeaway** — [the structural insight a reader should retain]
```
