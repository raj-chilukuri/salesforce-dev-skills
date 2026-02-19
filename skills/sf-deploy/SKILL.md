---
name: sf-deploy
description: Use when planning and executing Salesforce deployments with validation gates, sequencing, rollback strategy, and post-release checks.
---

# sf-deploy

## Overview

Guidance for safe Salesforce release execution across metadata, code, automation, and configuration with explicit deployment order and recovery planning.

## When to Use

- Releasing features across sandbox, UAT, and production
- Coordinating cross-skill changes that require strict order
- Investigating deployment failures and rollback decisions

## Core Responsibilities

- Build deterministic deployment plan with dependencies
- Enforce pre-deploy quality gates and dry-runs
- Execute rollout with verification checkpoints
- Define rollback triggers and restoration actions

## Workflow

1. Define release scope and affected dependencies.
2. Validate metadata and test gates in lower environments.
3. Run dry-run deployment and resolve blockers.
4. Deploy in required sequence (model -> logic -> automation -> access).
5. Verify post-deploy health and business-critical paths.
6. Publish release report and rollback readiness status.

## Commands

```bash
# Validate first
sf project deploy start --dry-run --source-dir force-app --target-org <org>

# Execute deployment
sf project deploy start --source-dir force-app --target-org <org>

# Check deployment status
sf project deploy report --target-org <org>
```

## Guardrails

- Never skip dry-run on high-impact releases.
- Keep rollback plan explicit before production deploy.
- Separate unrelated risky changes into different releases.
- Verify business transactions, not only deploy success status.

## Output Contract

- Deployment scope and sequencing plan
- Gate status (tests, validation, approvals)
- Post-deploy verification results
- Rollback triggers and owner assignments

## Related Skill Handoffs

- `sf-testing` for quality gates
- `sf-metadata` for dependency-aware planning
- `sf-debug` for production incident remediation
