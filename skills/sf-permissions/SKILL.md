---
name: sf-permissions
description: Use when analyzing or implementing Salesforce access control through profiles, permission sets, and sharing design.
---

# sf-permissions

## Overview

Guidance for least-privilege permission architecture, access troubleshooting, and auditable entitlement changes.

## When to Use

- Users cannot access required objects/fields/actions
- Access model needs cleanup or standardization
- Compliance review requires explicit entitlement mapping

## Core Responsibilities

- Map required permissions by persona and business function
- Audit current grants and assignment paths
- Design minimal required permission set changes
- Validate both allow and deny behavior for key actions

## Workflow

1. Define persona matrix and required capabilities.
2. Inventory existing profiles, permission sets, and assignments.
3. Identify gaps, over-permissioning, and conflicts.
4. Design/update permission sets and assignment model.
5. Validate with scenario-based user tests.
6. Deliver audit-ready change summary.

## Commands

```bash
# Retrieve permission metadata
sf project retrieve start --metadata PermissionSet,Profile --target-org <org>

# Query assignments (example)
sf data query --query "SELECT AssigneeId, PermissionSet.Name FROM PermissionSetAssignment" --target-org <org>
```

## Guardrails

- Prefer permission sets over profile sprawl for incremental grants.
- Avoid broad admin-level grants as shortcuts.
- Capture rationale for every entitlement increase.
- Ensure revocation path exists for temporary access.

## Output Contract

- Persona-to-access matrix
- Proposed permission changes
- Validation evidence (allow/deny)
- Residual risk and governance actions

## Related Skill Handoffs

- `sf-metadata` for object/field dependencies
- `sf-connected-apps` for API scope alignment
- `sf-deploy` for controlled rollout
