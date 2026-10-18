---
name: reviews-performance-review-capability
description: Comprehensive capabilities, procedures, and best practices for reviews-performance-review-capability.
license: Apache License 2.0
metadata:
  hermes:
    category: agent-teams
    provider: agent_team
    repo: 1mancompany/OneManCompany
---

# Reviews — Performance Review Capability

## Responsibilities
- Conduct performance reviews for employees each quarter (after 3 tasks completed)
- Assign one of three performance tiers
- Provide constructive feedback to help employees improve
- Determine promotions based on performance history

## Performance Scoring System (must be strictly followed)

Only three tiers are allowed; no other scores may be used:

| Score | Tier | Meaning |
|-------|------|---------|
| 3.25 | Needs Improvement | Did not meet basic role requirements, improvement needed |
| 3.50 | Satisfactory | Met role requirements, stable performance |
| 3.75 | Excellent | Exceeded expectations, outstanding performance |

## Review Cycle
- One quarter = 3 tasks
- Employees can only be reviewed for the current quarter after completing 3 tasks
- Retain performance records from the past 3 quarters

## Review Dimensions
- Task completion quality and efficiency
- Teamwork and communication
- Skill growth and learning ability
- Contribution to company objectives

## Promotion System (must be strictly followed)

**Promotion criteria**: 3 consecutive quarters of 3.75 (Excellent) → automatic promotion by one level

**Regular employee level cap**: Lv.3 (Senior)

| Level | Prefix | Example Titles |
|-------|--------|---------------|
| Lv.1 | Junior | Junior Engineer, Junior Researcher, Junior Marketing Specialist |
| Lv.2 | Mid-level | Mid-level Engineer, Mid-level Researcher, Mid-level Marketing Specialist |
| Lv.3 | Senior | Senior Engineer, Senior Researcher, Senior Marketing Specialist |
| Lv.4 | Founding | Founding employee (cannot be achieved through promotion) |
| Lv.5 | CEO | CEO (cannot be achieved through promotion) |

**Note**: Lv.4 (Founding) and Lv.5 (CEO) are not part of the performance promotion system.

## Output Format
Review results must include JSON format:
```json
{"action": "review", "reviews": [{"id": "employee_id", "score": 3.5, "feedback": "..."}]}
```

## When to Use

- When interacting with reviews-performance-review-capability capabilities or automation.
- When required by workflows calling for Comprehensive capabilities, procedures, and best practices for reviews-performance-review-capability..

## Procedure

1. Verify prerequisites and runtime environment.
2. Execute relevant operations or CLI actions for reviews-performance-review-capability.
3. Review generated logs or outputs.

## Pitfalls

- Avoid executing unverified configurations or missing required credentials.
- Ensure schema boundaries and timeouts are respected.

## Verification

- Inspect exit status and command outputs.
- Run verification check to confirm reviews-performance-review-capability functions as expected.
