---
name: sf-ai-agentforce
description: Use when configuring platform-native Agentforce capabilities, topics, actions, prompts, and publish workflows.
---

# sf-ai-agentforce

## Overview

Guidance for setup-driven Agentforce delivery: topic architecture, action contracts, instruction quality, preview validation, and controlled publishing.

## When to Use

- Creating or updating an agent in setup-based workflows
- Defining topics/actions and prompt template behavior
- Preparing publish changes with rollback-safe controls

## Core Responsibilities

- Design topic boundaries and routing clarity
- Configure actions with explicit input/output contracts
- Align instructions with policy and escalation behaviors
- Validate preview behavior before publish

## Workflow

1. Define agent goals, target users, and operating boundaries.
2. Create topic map with non-overlapping responsibilities.
3. Configure actions (Flow/Apex/Prompt) with contract clarity.
4. Author system/topic instructions and escalation conditions.
5. Preview and evaluate representative interactions.
6. Publish with rollback and post-release verification notes.

## Commands

```bash
# Preview and publish examples
sf agent preview --api-name <agentApiName> --target-org <org>
sf agent publish authoring-bundle --api-name <agentApiName> --target-org <org>
```

## Guardrails

- Avoid vague topic descriptions that cause routing ambiguity.
- Keep action contracts explicit and validated.
- Ensure fallback behavior is defined for unsupported tasks.
- Do not publish without preview evidence.

## Output Contract

- Topic/action architecture summary
- Instruction and escalation policy overview
- Preview findings and unresolved issues
- Publish and rollback checklist

## Related Skill Handoffs

- `sf-ai-agentforce-conversationdesign` for persona/intent design
- `sf-ai-agentforce-testing` for release gating
- `sf-ai-agentforce-observability` for production operations
