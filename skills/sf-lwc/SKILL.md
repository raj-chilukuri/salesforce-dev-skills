---
name: sf-lwc
description: Use when creating or modifying Lightning Web Components, including Apex integration, state management, accessibility, and Jest testing.
---

# sf-lwc

## Overview

Guidance for shipping production-grade LWC bundles (HTML, JS, CSS, meta.xml) with strong UX quality, predictable data flow, and maintainable tests.

## When to Use

- Building new UI components or pages
- Improving accessibility/performance of existing components
- Integrating LWC with Apex, LDS, or GraphQL data

## Core Responsibilities

- Design stable `@api` contracts and event interfaces
- Implement robust loading/error/empty states
- Ensure accessibility and keyboard-safe interactions
- Add focused Jest tests for behavior-critical paths

## Workflow

1. Define component API: inputs, outputs, events.
2. Choose data strategy: LDS, Apex, or GraphQL.
3. Implement template/controller styles with clear state handling.
4. Add communication patterns (CustomEvent, LMS) as required.
5. Create Jest tests for render and interaction behaviors.
6. Validate responsive behavior and accessibility checks.

## Commands

```bash
# Run LWC unit tests
npm run test:unit

# Deploy updated component bundle
sf project deploy start --metadata LightningComponentBundle:accountSummary --target-org <org>
```

## Guardrails

- Keep business rules out of templates.
- Do not block keyboard navigation or focus flow.
- Avoid over-fetching data in reactive updates.
- Never skip error-state rendering.

## Output Contract

- Component contract summary (`@api`, events)
- Data flow and state management notes
- Test coverage summary for key behaviors
- Accessibility/performance observations

## Related Skill Handoffs

- `sf-apex` for backend service updates
- `sf-testing` for broader test strategy
- `sf-diagram-mermaid` for UI/data flow visuals
