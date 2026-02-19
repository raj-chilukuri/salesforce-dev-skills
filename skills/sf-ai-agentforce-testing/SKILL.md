---
name: sf-ai-agentforce-testing
description: Use when validating AI agent behavior with multi-turn scenarios, quality gates, regression suites, and failure classification.
---

# sf-ai-agentforce-testing

## Overview

Guidance for rigorous test design and execution of conversational agent behavior, including routing, tool usage, context retention, and policy compliance.

## When to Use

- Verifying agent readiness before publish
- Investigating regressions in multi-turn flows
- Measuring coverage across intents/actions/policies

## Core Responsibilities

- Define scenario catalog spanning functional and safety requirements
- Execute repeatable multi-turn tests and score outcomes
- Classify failures by intent, context, action, or policy breakdown
- Drive fix loops with clear pass/fail gates

## Workflow

1. Define test objectives and acceptance thresholds.
2. Author scenario sets (happy path, edge, abuse, escalation).
3. Execute tests and capture structured evidence.
4. Analyze failures and prioritize remediation.
5. Re-test until gating criteria are satisfied.
6. Publish release-readiness report.

## Commands

```bash
# Example placeholder for org-side test operations
sf project deploy start --dry-run --source-dir force-app --target-org <org>
```

## Guardrails

- Include policy and refusal tests, not only happy paths.
- Keep scenario data deterministic and versioned.
- Require explicit gating thresholds for release approval.
- Treat unstable tests as quality issues.

## Output Contract

- Test coverage matrix by scenario class
- Failure taxonomy and remediation status
- Regression results against prior baseline
- Release decision with confidence level

## Related Skill Handoffs

- `sf-ai-agentscript` and `sf-ai-agentforce` for implementation fixes
- `sf-ai-agentforce-observability` for runtime monitoring linkage
- `sf-testing` for broader cross-stack quality gates
