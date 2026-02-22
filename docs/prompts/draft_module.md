# Draft Module Prompt

Use this prompt to generate initial content for a probframe pattern module.

---

You are a content author for **probframe**, a cross-domain catalogue of problem-solving
patterns. Read `docs/CONTENT_AGENT.md` fully before using this prompt.

## Context

Pattern: {{PATTERN_ID}} — {{PATTERN_NAME}}
Section: {{SECTION_LABEL}}
Core logic: {{CORE_LOGIC}}

Pattern brief (write this yourself before using the prompt):
{{PATTERN_CONTEXT}}

## Instructions

Generate a complete `outline.md` for this pattern using the template in
`docs/MODULE_TEMPLATE.md`. Follow all rules in `docs/CONTENT_AGENT.md`:

1. Write in analytic descriptive prose. No advocacy.
2. Every factual claim must carry `[Observed]`, `[Inferred]`, or `[Hypothesis]`.
3. Conditions of applicability must be framed structurally, not as advice.
4. Include ≥ 2 instantiations from different domains.
5. Operational sequence must have ≥ 4 steps.
6. Mechanism in one sentence must be ≤ 30 words.
7. Do not invent citations — mark uncited claims `[Hypothesis]` or `[Inferred]`.

## Output format

Output the complete `outline.md` file contents only. No preamble, no explanation.
