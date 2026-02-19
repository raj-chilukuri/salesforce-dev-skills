---
name: sf-ai-agentscript
description: Use when implementing Agent Script DSL artifacts with explicit states, transitions, and deterministic tool/action routing.
---

# sf-ai-agentscript

## Overview

Guidance for code-first agent behavior engineering using Agent Script patterns, finite state transitions, and explicit failure handling.

## When to Use

- Building version-controlled agent logic in `.agent` files
- Stabilizing inconsistent multi-turn behavior
- Enforcing explicit state and routing constraints

## Core Responsibilities

- Model intents, entities, and state transitions
- Define deterministic action invocation contracts
- Prevent ambiguous route loops and dead-end states
- Validate multi-turn conversation continuity

## Workflow

1. Define conversation goals, intents, and slot model.
2. Design finite states with entry/exit/error transitions.
3. Bind actions/tools with input validation.
4. Simulate multi-turn paths and edge interruptions.
5. Add fallback, escalation, and recovery behaviors.
6. Publish state map and unresolved risk list.

## Commands

```bash
# Example deployment validation before publish
sf project deploy start --dry-run --source-dir force-app --target-org <org>
```

## Guardrails

- Keep transitions explicit; avoid implicit hidden jumps.
- Ensure every state has an error/escape path.
- Avoid side-effect-heavy actions without confirmation checks.
- Keep policy constraints separate from generation prompts.

## Output Contract

- State machine summary
- Intent/action contract map
- Multi-turn test scenarios
- Fallback and escalation policy notes

## Related Skill Handoffs

- `sf-ai-agentforce-testing` for scenario validation
- `sf-ai-agentforce-conversationdesign` for persona and tone
- `sf-ai-agentforce-observability` for runtime telemetry
