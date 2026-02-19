---
name: sf-debug
description: Use when analyzing failures through logs, stack traces, and governor metrics to isolate root cause and safe fixes.
---

# sf-debug

## Overview

Guidance for diagnosing runtime issues in Salesforce by correlating log evidence, transaction context, and limit consumption.

## When to Use

- Production errors, test failures, or unexplained behavior
- CPU/SOQL/DML limit exceptions
- Performance regressions and intermittent failures

## Core Responsibilities

- Gather reproducible failure signature
- Parse transaction logs for high-cost operations
- Pinpoint failing method, object interaction, or recursion path
- Recommend minimal-risk remediation strategy

## Workflow

1. Capture context: user, org, time window, transaction type.
2. Retrieve relevant logs and isolate target transaction.
3. Analyze sequence: entry point -> decisions -> DML/SOQL -> exception.
4. Identify root cause and confidence level.
5. Propose fix and verify with focused tests.
6. Document rollback and observability follow-ups.

## Commands

```bash
# List available logs
sf apex list log --target-org <org>

# Fetch a specific log
sf apex get log --log-id <logId> --target-org <org>

# Tail logs live
sf apex tail log --target-org <org>
```

## Guardrails

- Do not propose fixes without evidence chain.
- Keep incident changes narrow and reversible.
- Preserve chronology when summarizing logs.
- Explicitly call out uncertainty when confidence is low.

## Output Contract

- Root cause statement with evidence
- Impact and blast radius estimate
- Fix plan with risk and rollback notes
- Observability/test additions to prevent recurrence

## Related Skill Handoffs

- `sf-soql` for query-level bottlenecks
- `sf-apex` for code remediation
- `sf-testing` for regression hardening
