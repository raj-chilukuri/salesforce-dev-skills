---
name: sf-connected-apps
description: Use when creating or reviewing connected apps, OAuth flows, scopes, and token security settings for Salesforce API clients.
---

# sf-connected-apps

## Overview

Guidance for secure connected app design, OAuth flow selection, and operational credential governance.

## When to Use

- New API client onboarding
- OAuth failures or token policy issues
- Security review of existing connected app settings

## Core Responsibilities

- Select OAuth flow based on trust and runtime constraints
- Minimize scopes and token lifetime risk
- Define callback and policy hardening controls
- Document ownership, rotation, and incident procedures

## Workflow

1. Identify client type and trust boundary.
2. Choose OAuth flow and required scopes.
3. Configure connected app policies and callback constraints.
4. Validate auth/refresh behavior and failure paths.
5. Document credential management and rotation process.
6. Provide runbook for common auth incidents.

## Commands

```bash
# Retrieve connected app metadata
sf project retrieve start --metadata ConnectedApp --target-org <org>

# Deploy connected app metadata
sf project deploy start --metadata ConnectedApp:<apiName> --target-org <org>
```

## Guardrails

- Use least-privilege scopes only.
- Enforce strict callback URL controls.
- Avoid long-lived tokens unless required.
- Keep secrets out of source control and logs.

## Output Contract

- OAuth flow and scope rationale
- Policy/security configuration summary
- Validation checklist and failure handling
- Credential rotation ownership model

## Related Skill Handoffs

- `sf-integration` for end-to-end API design
- `sf-permissions` for access alignment
- `sf-deploy` for controlled release
