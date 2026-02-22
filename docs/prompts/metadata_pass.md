# Metadata Pass Prompt

Use this prompt to normalize and complete `README.md` metadata before advancing to `sourced`.

---

You are reviewing a probframe pattern module's `README.md` for metadata completeness.

## Input

Pattern ID: {{PATTERN_ID}}
Pattern name: {{PATTERN_NAME}}

Paste current `README.md`:

```
{{README_MD}}
```

Paste current `outline.md` (for cross-reference inference):

```
{{OUTLINE_MD}}
```

## Instructions

1. Verify all required fields are present and non-empty:
   - `Status`
   - `Tags`
   - `Pattern class`
   - `Related patterns` (≥ 1 entry)
   - `Often combined with` (≥ 1 entry)
   - `Degrades into` (≥ 1 entry)
   - `Modframe instances` (≥ 1 entry, or "none applicable" with reasoning)
   - `Last reviewed` (YYYY-MM format)
   - `Domains` (≥ 1 entry)
   - `Actors` (≥ 1 entry with name and type)

2. For `Degrades into`, `Related patterns`, and `Often combined with`: infer from the
   outline content if not already populated. Use 3-digit pattern IDs from the taxonomy.

3. Return the corrected `README.md` only.
