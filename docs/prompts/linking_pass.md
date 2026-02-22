# Linking Pass Prompt

Use this prompt to suggest cross-reference links between pattern modules.

---

You are reviewing a probframe pattern module to suggest cross-reference links.

## Input

Pattern ID: {{PATTERN_ID}}

Paste current `outline.md`:

```
{{OUTLINE_MD}}
```

Taxonomy summary (from SECTION_AND_PATTERN_MAP.md):
{{TAXONOMY_SUMMARY}}

## Instructions

1. Suggest 2–5 patterns for `Related patterns` — structural overlap, similar mechanics.
2. Suggest 1–3 patterns for `Often combined with` — patterns commonly co-deployed.
3. Suggest 1–2 patterns for `Degrades into` — what this pattern becomes when its enabling
   conditions fail.

For each suggestion, give a one-sentence justification.

## Output

Return a structured list of suggestions. Do not modify any files — this is advisory only.
