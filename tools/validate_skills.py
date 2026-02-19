#!/usr/bin/env python3
"""
Validate Agent Skills repository structure and content.

Checks:
1) skills/*/SKILL.md exists
2) YAML frontmatter includes required keys: name, description
3) folder name matches frontmatter name
4) skill names are unique
5) non-empty skill body exists
6) body includes a Workflow section
7) body includes Guardrails or Quality Bar section
"""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", flags=re.DOTALL)


def extract_frontmatter(text: str) -> str | None:
    match = FRONTMATTER_PATTERN.match(text)
    return match.group(1) if match else None


def extract_body(text: str) -> str:
    match = FRONTMATTER_PATTERN.match(text)
    if not match:
        return ""
    return text[match.end() :].strip()


def parse_key(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{key}:\s*(.+)$", frontmatter)
    if not match:
        return None
    return match.group(1).strip().strip('"\'')


def has_section(body: str, title: str) -> bool:
    return re.search(rf"(?im)^##\s+{re.escape(title)}\s*$", body) is not None


def validate_skill(skill_dir: Path, seen_names: set[str]) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return [f"{skill_md}: file missing"]

    text = skill_md.read_text(encoding="utf-8")
    frontmatter = extract_frontmatter(text)
    if not frontmatter:
        return [f"{skill_md}: missing YAML frontmatter"]

    name = parse_key(frontmatter, "name")
    description = parse_key(frontmatter, "description")

    if not name:
        errors.append(f"{skill_md}: frontmatter missing 'name'")
    if not description:
        errors.append(f"{skill_md}: frontmatter missing 'description'")

    if name:
        if name != skill_dir.name:
            errors.append(
                f"{skill_md}: folder '{skill_dir.name}' does not match frontmatter name '{name}'"
            )
        if name in seen_names:
            errors.append(f"{skill_md}: duplicate skill name '{name}'")
        seen_names.add(name)

    body = extract_body(text)
    if not body:
        errors.append(f"{skill_md}: skill body is empty")
    else:
        if not has_section(body, "Workflow"):
            errors.append(f"{skill_md}: missing required 'Workflow' section")
        if not (has_section(body, "Guardrails") or has_section(body, "Quality Bar")):
            errors.append(f"{skill_md}: missing 'Guardrails' or 'Quality Bar' section")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("skills/ directory not found")
        return 1

    skill_dirs = sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir()])
    if not skill_dirs:
        print("No skills found under skills/")
        return 1

    all_errors: list[str] = []
    seen_names: set[str] = set()

    for skill_dir in skill_dirs:
        all_errors.extend(validate_skill(skill_dir, seen_names))

    if all_errors:
        print("Skill validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation passed ({len(skill_dirs)} skills checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
