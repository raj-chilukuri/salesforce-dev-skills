---
name: sf-ai-agentforce-conversationdesign
description: Use when designing agent persona, intents, utterances, guardrails, and escalation rules for user-facing conversation quality.
---

# sf-ai-agentforce-conversationdesign

## Overview

Guidance for conversational architecture: persona definition, intent taxonomies, route clarity, response style, and safety boundaries.

## When to Use

- Designing a new conversational agent experience
- Improving intent routing quality and response consistency
- Defining escalation and refusal behavior

## Core Responsibilities

- Define persona and communication constraints
- Build intent hierarchy with disambiguation rules
- Create response patterns for normal and edge cases
- Specify human handoff and escalation triggers

## Workflow

1. Set persona goals, tone, and prohibited behavior.
2. Build intent taxonomy and confidence thresholds.
3. Draft canonical utterances and response templates.
4. Define escalation/refusal paths and policy constraints.
5. Validate with representative scripted conversations.
6. Hand off artifacts for implementation and testing.

## Commands

```bash
# No mandatory CLI command; deliverable is design specification consumed by build/test skills.
```

## Guardrails

- Keep instructions unambiguous and policy-safe.
- Prevent inconsistent tone across equivalent intents.
- Require escalation paths for unsupported tasks.
- Distinguish “cannot comply” from “needs clarification.”

## Output Contract

- Persona and behavior guidelines
- Intent routing map
- Canonical utterance set
- Escalation/refusal decision table

## Related Skill Handoffs

- `sf-ai-agentforce` for setup configuration
- `sf-ai-agentscript` for code-first behavior implementation
- `sf-ai-agentforce-testing` for quality validation
