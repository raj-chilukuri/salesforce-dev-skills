---
name: sf-diagram-mermaid
description: Use when creating architecture, data flow, integration, or process diagrams in Mermaid for technical communication and reviews.
---

# sf-diagram-mermaid

## Overview

Guidance for creating clear, implementation-aligned diagrams that support architecture decisions, release planning, and troubleshooting.

## When to Use

- Explaining system architecture or integration flows
- Modeling data relationships and process steps
- Producing visual artifacts for design reviews

## Core Responsibilities

- Select the correct Mermaid diagram type for intent
- Keep labels and relationships implementation-accurate
- Optimize readability for engineering and stakeholder audiences
- Provide concise assumptions and legend notes

## Workflow

1. Define objective, audience, and required detail level.
2. Choose diagram type (`flowchart`, `sequenceDiagram`, `classDiagram`, `erDiagram`).
3. Model entities, transitions, and boundaries.
4. Review for naming consistency and ambiguity.
5. Add assumptions and decision notes.
6. Deliver Mermaid source and optional textual summary.

## Commands

```bash
# No required CLI; output is Mermaid source suitable for markdown rendering.
```

## Guardrails

- Prioritize clarity over decorative complexity.
- Avoid mixing unrelated contexts in one diagram.
- Keep identifiers consistent with actual metadata/API names.
- Document assumptions when data is incomplete.

## Output Contract

- Mermaid diagram source
- Legend and assumptions
- Key decision or risk callouts
- Suggested follow-up diagrams if scope is broad

## Related Skill Handoffs

- `sf-metadata` for schema-grounded diagrams
- `sf-integration` for sequence diagrams
- `sf-deploy` for release flow visualizations
