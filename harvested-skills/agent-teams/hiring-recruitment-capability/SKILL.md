---
name: hiring-recruitment-capability
description: Comprehensive capabilities, procedures, and best practices for hiring-recruitment-capability.
license: Apache License 2.0
metadata:
  hermes:
    category: agent-teams
    provider: agent_team
    repo: 1mancompany/OneManCompany
---

# Hiring — Recruitment Capability

## Responsibilities
- Identify and recruit suitable AI employees based on company needs
- Evaluate candidates' skill fit and cultural alignment
- Assign department, title, and nickname to new employees

## Recruitment Process
1. Call `list_open_positions()` to view current open positions
2. Call `generate_candidate(role_hint)` to generate matching candidates
3. Evaluate whether candidate skills meet position requirements
4. Assign department and title according to the position table
5. Assign a two-character Chinese nickname
6. Confirm hiring and notify the CEO

## Position Table (must be strictly followed)

### Department and Role Mapping

| Role | Department | Title Suffix |
|------|-----------|--------------|
| Engineer | R&D | Engineer |
| DevOps | R&D | Engineer |
| QA | R&D | Engineer |
| Designer | Design | Designer |
| Analyst | Data Analytics | Researcher |
| Marketing | Marketing | Marketing Specialist |

### Level System

All new hires start at Lv.1 (Junior); skipping levels during hiring is not allowed.

| Level | Prefix | Description |
|-------|--------|-------------|
| Lv.1 | Junior | Default level for new hires |
| Lv.2 | Mid-level | Requires performance-based promotion (3.75 for 3 consecutive quarters) |
| Lv.3 | Senior | Highest level for regular employees |

### Title Generation Rules

**Title = Level Prefix + Role Title Suffix**

Examples:
- Lv.1 Engineer → Junior Engineer
- Lv.2 Analyst → Mid-level Researcher
- Lv.3 Designer → Senior Designer
- Lv.1 Marketing → Junior Marketing Specialist

## Recruitment Requirements
- Prioritize high-priority positions
- Ensure team skill diversity
- Nicknames must be two Chinese characters, creative and role-relevant
- Report hiring details to the CEO after each recruitment

## When to Use

- When interacting with hiring-recruitment-capability capabilities or automation.
- When required by workflows calling for Comprehensive capabilities, procedures, and best practices for hiring-recruitment-capability..

## Procedure

1. Verify prerequisites and runtime environment.
2. Execute relevant operations or CLI actions for hiring-recruitment-capability.
3. Review generated logs or outputs.

## Pitfalls

- Avoid executing unverified configurations or missing required credentials.
- Ensure schema boundaries and timeouts are respected.

## Verification

- Inspect exit status and command outputs.
- Run verification check to confirm hiring-recruitment-capability functions as expected.
