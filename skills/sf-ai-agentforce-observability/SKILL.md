---
name: sf-ai-agentforce-observability
description: Use when defining telemetry, tracing, alerting, and operational diagnostics for Agentforce runtime behavior.
---

# sf-ai-agentforce-observability

## Overview

Guidance for production operations of AI agent systems: session tracing, quality metrics, latency tracking, and incident response readiness.

## When to Use

- Preparing agent workloads for production monitoring
- Diagnosing degraded quality/latency trends
- Defining SLOs and alerting for agent workflows

## Core Responsibilities

- Establish measurable reliability and quality indicators
- Instrument trace points across routing/action lifecycle
- Build dashboards and actionable alert thresholds
- Enable incident triage with evidence-rich telemetry

## Workflow

1. Define SLI/SLO targets for quality and latency.
2. Instrument key events and identifiers.
3. Configure dashboards and alert policies.
4. Validate end-to-end traceability in staging.
5. Document incident triage and ownership routing.
6. Iterate thresholds to reduce alert noise.

## Commands

```bash
# Retrieve recent telemetry-related metadata/assets as needed
sf project retrieve start --source-dir force-app --target-org <org>
```

## Guardrails

- Do not track metrics without operational response owners.
- Keep identifiers stable for cross-system correlation.
- Balance alert sensitivity to avoid fatigue.
- Separate product KPIs from operational health signals.

## Output Contract

- Observability design (metrics/traces/alerts)
- SLO definitions and threshold rationale
- Incident response playbook summary
- Known blind spots and instrumentation backlog

## Related Skill Handoffs

- `sf-ai-agentforce-testing` for pre-release validation signals
- `sf-debug` for runtime issue diagnostics
- `sf-deploy` for rollout guardrails
