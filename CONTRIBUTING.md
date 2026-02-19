# Contributing

Thanks for contributing to this skills catalog.

## Contribution Rules

- Open focused PRs that change one skill area at a time.
- Keep `SKILL.md` frontmatter valid (`name`, `description`).
- Keep workflows actionable and testable.
- Update README when adding or removing skills.

## AI-Assisted Contributions Policy

AI-assisted contributions are welcome when they are reviewed and verified by a human.

- Allowed: Drafting, refactoring, and generating examples that you validate.
- Required: Confirm correctness, consistency, and practical usefulness before opening a PR.
- Not allowed: Low-effort bulk submissions without review.

## Testing Checklist

Before opening a PR:

1. Run `python3 tools/validate_skills.py`.
2. Confirm folder name equals frontmatter `name`.
3. Confirm each skill has `Workflow` and `Guardrails` or `Quality Bar`.
4. Confirm there are no references to external source branding.

## Pull Request Checklist

1. Describe what changed and why.
2. Include validation output summary.
3. Keep skill descriptions concise and domain-specific.
4. Avoid introducing duplicate skill names.

