---
name: sf-soql
description: Use when authoring, reviewing, or optimizing SOQL queries for selectivity, performance, and governor-limit safety.
---

# sf-soql

## Overview

Guidance for converting requirements into efficient SOQL, improving query plans, and reducing transaction cost across Apex and automation workloads.

## When to Use

- New data retrieval requirements
- Slow transactions caused by query inefficiency
- Governor-limit incidents tied to query count/selectivity

## Core Responsibilities

- Build selective filters and minimal field sets
- Optimize parent-child and aggregate query structure
- Validate query behavior against expected data volumes
- Ensure secure access-aware query usage

## Workflow

1. Clarify required records, filters, sort order, and cardinality.
2. Draft query with minimal projection and selective predicates.
3. Evaluate relationship depth and aggregate suitability.
4. Check query plan/selectivity and adjust filters/index use.
5. Validate integration points (Apex, Flow, reporting logic).
6. Document assumptions and risk flags for high-volume orgs.

## Commands

```bash
# Run query
sf data query --query "SELECT Id, Name FROM Account LIMIT 10" --target-org <org>

# Check query plan (tooling)
sf data query --query "SELECT Id FROM Account WHERE CreatedDate = THIS_YEAR" --target-org <org> --use-tooling-api --plan
```

## Guardrails

- Avoid unbounded queries in transaction-critical paths.
- Prefer indexed/selective filters where possible.
- Keep selected fields strictly required for downstream logic.
- Review for row-locking and large data skew risks.

## Output Contract

- Final query and optimization reasoning
- Selectivity/performance notes
- Security/access assumptions
- Follow-up indexing or model changes if needed

## Related Skill Handoffs

- `sf-apex` for consumption pattern improvements
- `sf-debug` for runtime evidence correlation
- `sf-data` for volume-aware test data setups
