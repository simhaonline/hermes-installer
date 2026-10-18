---
name: openai
description: Autonomous specialist persona for openai.
role: openai.Agent
division: agent-teams
metadata:
  hermes:
    source: nrslib/takt
    version: 1.0.0
---

interface:
  display_name: "TAKT Workflow Engine"
  short_description: "Multi-agent orchestration via workflow YAML definitions"

policy:
  allow_implicit_invocation: false
