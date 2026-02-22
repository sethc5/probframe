# Citation Pass Prompt

Use this prompt after `draft` status to add and verify citations.

---

You are reviewing a probframe pattern module for citation quality.

## Input

Paste the current `outline.md` below:

```
{{OUTLINE_MD}}
```

## Instructions

1. For every `[Observed]` claim, check whether there is a matching entry in
   **Suggested sources**. If not, either:
   - Add a real, verifiable citation (title, author/issuing body, year, URL/identifier), or
   - Downgrade the claim to `[Inferred]` or `[Hypothesis]` and note the downgrade inline.

2. For every source entry, ensure it has all four fields: title, author/issuing body,
   year, and URL or identifier. Flag any incomplete entries.

3. Check that at least 3 sources are listed.

4. Check that `Modframe instances` is populated in `README.md`. If not, flag it.

5. Do not invent citations.

## Output

Return the revised `outline.md` with all citation edits applied. Then list any issues
that require human resolution.
