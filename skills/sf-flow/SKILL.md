---
name: sf-flow
description: Use when designing, building, or validating Salesforce Flow automation for reliability, readability, and bulk-safe behavior.
---

# sf-flow

## Overview

Guidance for record-triggered, scheduled, screen, and autolaunched flows with clear branching, fault handling, and deployment safety.

## When to Use

- New declarative automation requirements
- Existing flow is failing, slow, or difficult to maintain
- Migration from process-heavy logic to cleaner orchestration

## Core Responsibilities

- Choose the right flow type for use case and scale
- Keep decisioning explicit and easy to audit
- Ensure robust fault paths and notifications
- Validate transaction behavior under bulk load

## Workflow

1. Confirm trigger context, entry criteria, and expected outputs.
2. Map variables, branches, and subflow dependencies.
3. Implement with explicit decision labels and fault connectors.
4. Validate recursion controls and governor-sensitive actions.
5. Build test scenarios for standard, edge, and failure paths.
6. Prepare deploy notes including activation sequence.

## Commands

```bash
# Validate deployment package before release
sf project deploy start --dry-run --source-dir force-app --target-org <org>

# Deploy flow metadata
sf project deploy start --source-dir force-app --target-org <org>
```

## Guardrails

- Avoid monolithic flows; split reusable logic into subflows.
- Every data write path should have visible error handling.
- Keep naming deterministic and intent-based.
- Do not introduce hidden side effects across unrelated objects.

## Output Contract

- Flow type and entry condition summary
- Decision and fault-path map
- Deployment/activation notes
- Known limits and assumptions

## Related Skill Handoffs

- `sf-metadata` for prerequisite objects/fields
- `sf-testing` for post-change verification
- `sf-deploy` for release sequencing
