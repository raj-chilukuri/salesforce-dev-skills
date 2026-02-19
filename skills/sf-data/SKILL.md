---
name: sf-data
description: Use when creating deterministic test/seed data, factories, and safe org data operations.
---

# sf-data

## Overview

Guidance for repeatable data setup, cleanup safety, and realistic datasets for testing, demos, and migration rehearsal.

## When to Use

- Building test data factories for Apex tests
- Seeding sandboxes/scratch orgs
- Validating migrations with representative data

## Core Responsibilities

- Define object graph and data ownership assumptions
- Build idempotent seed/factory workflows
- Validate referential integrity and cleanup paths
- Protect production data from unsafe operations

## Workflow

1. Define required entities, relationships, and volumes.
2. Choose factory vs fixture vs script approach.
3. Implement deterministic create/update logic.
4. Validate with verification queries and guard checks.
5. Add cleanup/rollback strategy.
6. Publish usage notes for teams and CI.

## Commands

```bash
# Insert records from CSV
sf data upsert bulk --sobject Account --file data/accounts.csv --external-id Id --target-org <org>

# Validate resulting records
sf data query --query "SELECT COUNT() FROM Account WHERE Name LIKE 'Seed-%'" --target-org <org>
```

## Guardrails

- Never run destructive scripts against production without explicit approval.
- Keep seed scripts idempotent.
- Avoid hardcoded org-specific IDs unless unavoidable.
- Ensure test data supports edge-case coverage.

## Output Contract

- Data model and volume assumptions
- Seed/factory strategy and commands
- Validation checks performed
- Cleanup and rollback procedure

## Related Skill Handoffs

- `sf-testing` for test scenario alignment
- `sf-soql` for verification queries
- `sf-deploy` for release-time data tasks
