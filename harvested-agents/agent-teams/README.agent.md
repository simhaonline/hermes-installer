---
name: README
description: Autonomous specialist persona for README.
role: README.Agent
division: agent-teams
metadata:
  hermes:
    source: nrslib/takt
    version: 1.0.0
---

# Agent evals

Each directory owns evaluations for one TAKT agent step. Upstream reports and
other context are fixed inputs, so only the named agent is executed.

Provider and model combinations remain inside each suite as an execution
matrix. They do not determine the directory structure.

`shared-policy/` contains cross-role policy checks. Each case still executes
only one role against fixed inputs; it is not an executed multi-agent handoff.
