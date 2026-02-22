# probframe

A cross-domain catalogue of problem-solving patterns — how actors, institutions,
organisms, and systems solve problems, concentrate advantage, and fail.

---

## What this is

Probframe documents recurring structural patterns that appear across domains: politics,
biology, law, economics, military strategy, ecology, organizational behavior, and
elsewhere. Each entry describes one pattern — how it operates, who deploys it and
against what, where it concentrates leverage, under what conditions it works or breaks
down, and where it has been observed in practice.

The goal is pattern recognition that travels. The same structural logic that describes
how a congressional committee controls the legislative agenda also describes how a
keystone species controls an ecosystem and how a platform company controls developer
access. Probframe makes those structural equivalences explicit and traceable.

Entries are **descriptive and conditionally prescriptive**: they document how patterns
operate and the conditions under which they have been observed to succeed or fail. They
do not recommend strategies or evaluate whether outcomes are good or bad.

---

## Relationship to Modframe

Probframe is an independent project with a documented relationship to
[Modframe](../modframe/), a structural map of US federal power mechanics.

Modframe modules appear in probframe entries as **instantiations** — specific
federal-power examples that ground abstract pattern claims in documented, cited evidence.
Every probframe entry that has a plausible federal power instantiation must link to the
relevant Modframe module IDs before it can advance to `sourced` status.

The relationship is reference, not inclusion. Probframe abstracts from Modframe; it does
not duplicate it.

---

## Structure

```
probframe/
  patterns/
    01_Adversarial_Patterns/
      001_Direct_Displacement/
        README.md       ← status, tags, cross-reference metadata
        outline.md      ← full pattern content
        figures/        ← optional visuals
    02_Cooperative_and_Coalition_Patterns/
    ...
  docs/
    CONTENT_AGENT.md            ← authoring guide (read this first)
    SECTION_AND_PATTERN_MAP.md  ← full taxonomy with all 76 patterns
    GOVERNANCE.md               ← lifecycle rules and anti-capture measures
    STYLEGUIDE.md               ← voice, claim labels, neutrality constraints
    CITATIONS.md                ← citation format and source hierarchy
    GLOSSARY.md                 ← shared vocabulary
    MODULE_TEMPLATE.md          ← canonical module structure
    prompts/
      draft_module.md           ← initial content draft prompt
      citation_pass.md          ← citation review and enrichment prompt
      metadata_pass.md          ← structured metadata normalization prompt
      linking_pass.md           ← cross-reference link suggestion prompt
      neutrality_pass.md        ← tone and framing review (human)
      final_polish.md           ← prose quality pass (human)
    schemas/
      readme_schema.json        ← README metadata schema
      outline_schema.json       ← outline completeness schema
    examples/                   ← golden reference modules
  scripts/
    generate_queue.py           ← next module to work on
    validate_completeness.py    ← outline completeness check
    validate_metadata.py        ← README metadata quality check
    build_indexes.py            ← generate actor/domain/pattern indexes
```

---

## 11 sections, 76 patterns

| Section | Patterns | Primary relationship structure |
| --- | --- | --- |
| 01 Adversarial | 001–008 | Zero-sum with an active opponent |
| 02 Cooperative and Coalition | 009–015 | Positive-sum requiring coordination |
| 03 Procedural and Sequencing | 016–023 | Path-dependent, rule-governed, timing-sensitive |
| 04 Information and Signaling | 024–030 | Asymmetric information, revelation, concealment |
| 05 Constraint and Boundary | 031–037 | Operating within, around, or reshaping constraints |
| 06 Resource and Positioning | 038–044 | Scarcity, leverage, positional advantage |
| 07 Hierarchical and Delegative | 045–051 | Principal-agent, authority, accountability gaps |
| 08 Evolutionary and Iterative | 052–058 | Selection, variation, feedback loops |
| 09 Crisis and Exception | 059–064 | Urgency, emergency authority, process suspension |
| 10 Analogical and Transfer | 065–069 | Cross-domain pattern recognition and translation |
| 11 Meta-Strategies | 070–076 | Legitimacy, rule-setting, second-order effects |

Sections are fuzzy navigation clusters. The cross-reference graph handles the actual
relational structure between entries — a pattern lives in the section that best describes
its primary relationship structure, not every section it touches.

---

## Module anatomy

Each pattern entry has two files:

**README.md** — machine-readable metadata:
- Status in the lifecycle (`empty` → `scaffolded` → `draft` → `sourced` → `reviewed` → `published`)
- Cross-reference links: `Related patterns`, `Often combined with`, `Degrades into`, `Modframe instances`
- Domains, actors, tags

**outline.md** — the pattern content, structured around 9 required headings:
1. Actors and deployment context
2. Operational sequence
3. Where leverage concentrates
4. Conditions of applicability — enabling and disabling conditions
5. Common failure modes
6. What evidence would prove/disprove key claims
7. Instantiations — cross-domain documented examples
8. Suggested sources
9. Analysis outline (6 parts)

The **Conditions of applicability** section is probframe's light prescriptive layer. It
documents the structural conditions under which a pattern has been observed to operate
or fail — framed as tendencies, not recommendations, with claim labels required.

The **`Degrades into`** cross-reference field maps what a pattern becomes when its
enabling conditions fail. Together with `Related patterns` and `Often combined with`, it
turns the catalogue into a navigable knowledge graph rather than a flat list.

---

## Claim types

Every factual assertion carries one of three labels:

| Label | When to use |
| --- | --- |
| `[Observed]` | Documented in a primary or high-quality secondary source |
| `[Inferred]` | Follows logically from observed facts; reasoning stated |
| `[Hypothesis]` | Plausible but unverified; confirming evidence described |

---

## Current status

All 76 patterns are scaffolded as stubs. No modules have reached `draft` status yet.

**Priority build queue:**

| # | Pattern | Reason |
| --- | --- | --- |
| 039 | Chokepoint Control | Documented across all Modframe sections; high cross-domain clarity |
| 047 | Oversight Capture | Deep Modframe grounding in Sections 03, 04, 11 |
| 054 | Ratchet Mechanisms | Documented in emergency powers, regulatory, and judicial modules |
| 021 | Process Capture and Rule-Setting | Grounded in Modframe Sections 02, 03, 06 |
| 010 | Minimum Winning Coalition | Strong academic sourcing (Riker); Modframe Sections 01, 02 |

---

## Contributing

See `docs/CONTENT_AGENT.md` for the full authoring guide.

The short version:

1. Run `python3 scripts/generate_queue.py --next 1` to find your next module
2. Write a pattern brief before drafting (4–6 sentences: mechanism, actors, cross-domain examples, relevant sources, Modframe links)
3. Use `docs/prompts/draft_module.md` to generate the initial outline
4. Run the citation pass, metadata pass, and linking pass in order
5. Stop at `sourced` — `reviewed` and `published` require human approval

**Claim label rules and citation format:** `docs/STYLEGUIDE.md` and `docs/CITATIONS.md`

**Lifecycle and governance:** `docs/GOVERNANCE.md`

---

## Design principles

**Pattern-first, domain-second.** The structural logic comes first; the domain examples
are grounding evidence, not the primary subject.

**Conditions over prescriptions.** Instead of "use this pattern when X," entries document
"this pattern is observed in contexts where X." The conditions are citable claims, not
advice.

**Failure modes are first-class.** The `Degrades into` field and failure modes section
treat pattern breakdown as analytically equal to pattern operation. Most of the
interesting insight lives at the seams where patterns fail.

**Sections are entry points, not categories.** The cross-reference graph is the real
structure of the catalogue. Sections exist for navigation; the graph captures the actual
relationships between patterns.

**Modframe as empirical ground truth.** Every pattern claim that applies to federal power
mechanics should be traceable to a specific Modframe module. This keeps abstraction
honest.

---

## License

CC BY 4.0 — see `LICENSE`.
