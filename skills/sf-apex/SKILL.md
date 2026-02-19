---
name: sf-apex
description: Use when generating, reviewing, or refactoring Apex classes, triggers, async jobs, and test code with bulk-safe and secure patterns.
---

# sf-apex

## Overview

Expert guidance for Apex service design, trigger architecture, governor-limit safety, and maintainable code standards.

## When to Use

- New Apex features (service, selector, domain, trigger handler)
- Trigger stabilization or recursion defects
- Performance tuning and governor-limit risks
- Security hardening (CRUD/FLS/sharing enforcement)

## Core Responsibilities

- Design classes around clear responsibilities and transaction boundaries
- Enforce bulk-safe query and DML patterns
- Apply security checks and explicit exception handling
- Generate meaningful tests for positive, negative, and bulk paths

## Workflow

1. Gather requirements: object model, entry points, expected side effects.
2. Inspect existing patterns and naming in the codebase.
3. Design class boundaries: trigger handler, service, selector, utility.
4. Implement bulk-safe logic and security checks.
5. Add/extend test classes with scenario coverage.
6. Run static checks and summarize residual risks.

## Commands

```bash
# Run focused Apex tests
sf apex run test --class-names AccountServiceTest --code-coverage --result-format human --target-org <org>

# Deploy changed Apex quickly
sf project deploy start --metadata ApexClass:AccountService --target-org <org>
```

## Guardrails

- No SOQL or DML inside loops.
- Keep trigger files thin; delegate logic to handlers/services.
- Do not rely on implicit sharing behavior.
- Never ship without negative-path tests.

## Output Contract

- Changed classes/triggers and rationale
- Test scenarios executed or required
- Security/performance concerns and mitigations
- Follow-up tasks if debt remains

## Related Skill Handoffs

- `sf-soql` for complex query optimization
- `sf-testing` for broader regression strategy
- `sf-deploy` for release orchestration
