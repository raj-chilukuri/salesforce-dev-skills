# Salesforce Skills Hub for Codex and Gemini

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Validation](https://img.shields.io/badge/skills-validation-blue)](.github/workflows/validate-skills.yml)
[![Agent Skills](https://img.shields.io/badge/Standard-Agent%20Skills-orange)](https://agentskills.io)

Production-ready Salesforce skills for agentic development, testing, deployment, AI automation, and architecture workflows.

## Why This Repository

- Curated `sf-*` skill catalog with strict quality standards
- Works in Codex and Gemini through Agent Skills format
- Includes validation automation for consistent skill quality
- Organized for fast handoff across development, QA, integration, and AI operations

## Quick Start

```bash
# Add to your agent environment
npx skills add github:<your-username>/<your-repo>

# Validate local skill integrity
python3 tools/validate_skills.py
```

## Available Skills

### Development

| Skill | Purpose | Typical Trigger |
|------|---------|-----------------|
| [`sf-apex`](skills/sf-apex/SKILL.md) | Apex architecture, trigger patterns, secure code | New class/trigger implementation, refactor, code review |
| [`sf-flow`](skills/sf-flow/SKILL.md) | Flow design and validation | Record-triggered/scheduled/autolaunched automation |
| [`sf-lwc`](skills/sf-lwc/SKILL.md) | LWC implementation and testing | UI components, events, accessibility, Jest |
| [`sf-soql`](skills/sf-soql/SKILL.md) | SOQL generation and optimization | Query tuning, selective filters, query plans |

### Quality

| Skill | Purpose | Typical Trigger |
|------|---------|-----------------|
| [`sf-testing`](skills/sf-testing/SKILL.md) | Test strategy and execution | Coverage gaps, failing tests, regression hardening |
| [`sf-debug`](skills/sf-debug/SKILL.md) | Log-driven troubleshooting | Governor limits, runtime errors, performance issues |

### Foundation

| Skill | Purpose | Typical Trigger |
|------|---------|-----------------|
| [`sf-metadata`](skills/sf-metadata/SKILL.md) | Metadata modeling and deployment readiness | Object/field design, package organization |
| [`sf-data`](skills/sf-data/SKILL.md) | Data seeding and factory patterns | Test setup, sandboxes, migration prep |
| [`sf-permissions`](skills/sf-permissions/SKILL.md) | Access design and audits | Permission gaps, least-privilege cleanup |

### Integration

| Skill | Purpose | Typical Trigger |
|------|---------|-----------------|
| [`sf-connected-apps`](skills/sf-connected-apps/SKILL.md) | OAuth and connected app security | API app setup, token policy review |
| [`sf-integration`](skills/sf-integration/SKILL.md) | Callouts, events, resilient interfaces | External API integration, retry/idempotency design |

### AI and Automation

| Skill | Purpose | Typical Trigger |
|------|---------|-----------------|
| [`sf-ai-agentscript`](skills/sf-ai-agentscript/SKILL.md) | Agent Script DSL implementation | Code-first agent behaviors and state machines |
| [`sf-ai-agentforce-conversationdesign`](skills/sf-ai-agentforce-conversationdesign/SKILL.md) | Conversational architecture | Persona, intent maps, escalation behavior |
| [`sf-ai-agentforce-observability`](skills/sf-ai-agentforce-observability/SKILL.md) | Runtime telemetry and operations | Session traces, SLOs, alerting |
| [`sf-ai-agentforce-testing`](skills/sf-ai-agentforce-testing/SKILL.md) | Agent quality gates and scenario testing | Multi-turn regressions, policy validation |
| [`sf-ai-agentforce`](skills/sf-ai-agentforce/SKILL.md) | Setup-based Agentforce delivery | Topics/actions, prompt templates, publish flow |

### DevOps and Tooling

| Skill | Purpose | Typical Trigger |
|------|---------|-----------------|
| [`sf-deploy`](skills/sf-deploy/SKILL.md) | Deployment orchestration and rollback | Release planning and production promotion |
| [`sf-diagram-mermaid`](skills/sf-diagram-mermaid/SKILL.md) | Mermaid architecture diagrams | System/data flow visualization |
| [`sf-diagram-nanobananapro`](skills/sf-diagram-nanobananapro/SKILL.md) | High-fidelity visual artifacts | Design reviews and architecture communication |

## Suggested Skill Routing

```text
Feature Build: sf-metadata -> sf-apex/sf-flow/sf-lwc -> sf-testing -> sf-deploy
Issue Triage: sf-debug -> sf-soql/sf-apex -> sf-testing -> sf-deploy
Agent Delivery: sf-ai-agentforce-conversationdesign -> sf-ai-agentforce/sf-ai-agentscript -> sf-ai-agentforce-testing -> sf-ai-agentforce-observability
```

## Repository Layout

```text
.
├── skills/
│   └── sf-*/SKILL.md
├── tools/
│   └── validate_skills.py
├── .github/workflows/
│   └── validate-skills.yml
├── CONTRIBUTING.md
└── LICENSE
```

## Quality Rules

- `skills/<folder>/SKILL.md` must exist
- frontmatter requires `name` and `description`
- folder name must match frontmatter `name`
- each skill requires a non-empty `Workflow` section
- each skill requires `Guardrails` or `Quality Bar`

## Contribution Expectations

- Keep content practical, implementation-first, and concise
- Add command examples only when they reduce ambiguity
- Prefer deterministic workflows over vague guidance
- Run validation before opening a pull request

