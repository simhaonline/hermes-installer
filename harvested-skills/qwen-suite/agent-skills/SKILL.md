---
name: agent-skills
description: Generic, eval-tested agent skills for CI, quality audits and site work
license: MIT
metadata:
  hermes:
    category: qwen-suite
    provider: anthropic
    author: '{''name'': ''vannifr''}'
    version: 1.0.1
    tags: claude, plugin, agent-skills
---

# Agent Skills

Generic, eval-tested agent skills for CI, quality audits and site work

## When to Use

Use this skill when interacting with the agent-skills plugin capabilities.

## Procedure

1. Enable the agent-skills integration.
2. Invoke requested plugin commands or actions.
3. Validate output artifacts.

## Pitfalls

- Check for required configuration parameters in .claude-plugin/plugin.json.
- Maintain session state where applicable.

## Verification

- Execute basic health check or verification command for agent-skills.
