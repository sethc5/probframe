# Governance

## Lifecycle

```
empty → scaffolded → draft → sourced → reviewed → published
```

| Step | Meaning | Gate before advancing |
| --- | --- | --- |
| `empty` | Template files only | — |
| `scaffolded` | Headings filled; intent notes in place | All placeholder text removed |
| `draft` | Substantive prose; all claims labeled | No unlabeled claims remain |
| `sourced` | All `[Observed]` claims cited; ≥1 Modframe instance | Every `[Observed]` has a matching source |
| `reviewed` | Second contributor verified tone/sourcing | Different contributor approved PR |
| `published` | Stable | Maintainer merged PR |

## Anti-capture measures

- No module advances to `reviewed` or `published` without a second contributor sign-off.
- Claim labels are mandatory — unlabeled assertions block `draft` advancement.
- The `Degrades into` field must be populated before `sourced` if the degradation pathway
  is documented or clearly inferable.
- Moralizing or prescriptive language is a disqualifying defect at `reviewed`.

## Branching and PR rules

- One module per PR.
- Branch name: `pattern/<id>-<slug>` (e.g., `pattern/039-chokepoint-control`).
- PR must include: updated `outline.md`, updated `README.md`, and passing metadata validation.
- Maintainer merges after `reviewed` sign-off.

## Version policy

The SECTION_AND_PATTERN_MAP.md is locked. Adding, removing, or renaming patterns requires
a governance discussion and maintainer approval.
