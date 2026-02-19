---
name: sf-integration
description: Use when implementing resilient Salesforce integrations using callouts, events, named credentials, and asynchronous patterns.
---

# sf-integration

## Overview

Guidance for interface contracts, authentication, retries, idempotency, and operations visibility across external system boundaries.

## When to Use

- New outbound or inbound integration design
- Existing callout pipeline failures
- Event-driven or async processing requirements

## Core Responsibilities

- Define robust interface contracts and schema validation
- Implement named credentials and auth flows safely
- Add retry/idempotency controls and dead-letter handling
- Instrument monitoring and support playbooks

## Workflow

1. Define producer/consumer boundaries and ownership.
2. Specify request/response/event contracts.
3. Implement auth via named credentials and secure secrets.
4. Add retry, timeout, and idempotency strategy.
5. Validate failure modes and partial-success behavior.
6. Deliver runbook and monitoring recommendations.

## Commands

```bash
# Retrieve integration metadata
sf project retrieve start --metadata NamedCredential,ExternalCredential,RemoteSiteSetting --target-org <org>

# Deploy integration metadata
sf project deploy start --source-dir force-app --target-org <org>
```

## Guardrails

- Never trust external payloads without validation.
- Keep retries bounded and observable.
- Ensure every error path has a recovery decision.
- Protect against duplicate message processing.

## Output Contract

- Integration contract summary
- Auth and resilience strategy
- Failure-mode matrix
- Monitoring and ownership checklist

## Related Skill Handoffs

- `sf-connected-apps` for OAuth details
- `sf-apex` for service-layer implementation
- `sf-debug` for production issue analysis
