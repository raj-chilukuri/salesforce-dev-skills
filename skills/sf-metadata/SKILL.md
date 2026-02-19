---
name: sf-metadata
description: Use when designing or modifying metadata models, package boundaries, and deployment-safe configuration.
---

# sf-metadata

## Overview

Guidance for object/field architecture, naming consistency, dependency awareness, and environment portability in Salesforce metadata changes.

## When to Use

- New custom object or field design
- Metadata refactors across packages/modules
- Pre-deploy dependency planning and ordering

## Core Responsibilities

- Model metadata for clarity, governance, and scale
- Identify upstream/downstream dependencies before changes
- Plan additive-first migrations for safer rollout
- Produce deployment and rollback sequencing notes

## Workflow

1. Inventory current metadata and reference dependencies.
2. Define target model, naming conventions, and ownership.
3. Stage additive changes before destructive operations.
4. Validate dependent flows, Apex, and permission sets.
5. Prepare deployment order and compatibility notes.
6. Document migration and rollback strategy.

## Commands

```bash
# Retrieve metadata snapshot
sf project retrieve start --metadata CustomObject,CustomField,PermissionSet --target-org <org>

# Dry-run deployment validation
sf project deploy start --dry-run --source-dir force-app --target-org <org>
```

## Guardrails

- Avoid destructive metadata changes without migration plan.
- Keep API names explicit and stable.
- Validate permission dependencies before release.
- Ensure naming remains consistent across related assets.

## Output Contract

- Metadata delta summary
- Dependency and sequence map
- Compatibility and migration assumptions
- Rollback instructions

## Related Skill Handoffs

- `sf-flow` for automation using new metadata
- `sf-permissions` for access alignment
- `sf-deploy` for release execution
