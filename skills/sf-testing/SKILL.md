---
name: sf-testing
description: Use when creating test plans, executing Apex tests, improving coverage, and hardening regression protection.
---

# sf-testing

## Overview

Guidance for deterministic Salesforce testing across unit, integration, and regression scopes with clear failure triage and release-readiness reporting.

## When to Use

- New feature development requiring test coverage
- Failing tests in CI or pre-deploy checks
- Coverage gaps in critical business logic

## Core Responsibilities

- Define behavior-driven test matrix for critical flows
- Execute targeted and full-suite tests with coverage reporting
- Triage failures to root cause category
- Improve tests for reliability, clarity, and speed

## Workflow

1. Identify scope: changed classes, risk areas, dependencies.
2. Build test matrix: positive, negative, bulk, and security paths.
3. Run tests and collect structured result output.
4. Classify failures: assertion gap, setup issue, logic defect, flake.
5. Apply fixes in tests and/or implementation.
6. Re-run and summarize pass status with residual risks.

## Commands

```bash
# Run all local tests with coverage
sf apex run test --test-level RunLocalTests --code-coverage --result-format json --output-dir test-results --target-org <org>

# Run a specific class
sf apex run test --class-names AccountServiceTest --code-coverage --result-format human --target-org <org>
```

## Guardrails

- Avoid brittle assertions tied to unstable ordering.
- Test behavior, not implementation details.
- Keep test data minimal but representative.
- Treat flaky tests as defects, not noise.

## Output Contract

- Test execution scope and command summary
- Pass/fail matrix by scenario type
- Coverage impact and confidence statement
- Outstanding risks and required follow-up

## Related Skill Handoffs

- `sf-apex` for implementation fixes
- `sf-debug` for log-driven failure diagnosis
- `sf-deploy` for release gate enforcement
