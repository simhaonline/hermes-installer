---
name: discord
description: Discord channel for Claude Code — messaging bridge with built-in access
  control. Manage pairing, allowlists, and policy via /discord:access.
license: Apache License 2.0
metadata:
  hermes:
    category: claude-skills
    provider: anthropic
    author: Anthropic Ecosystem
    version: 0.0.4
    tags: claude, plugin, discord
---

# Discord

Discord channel for Claude Code — messaging bridge with built-in access control. Manage pairing, allowlists, and policy via /discord:access.

## When to Use

Use this skill when interacting with the discord plugin capabilities.

## Procedure

1. Enable the discord integration.
2. Invoke requested plugin commands or actions.
3. Validate output artifacts.

## Pitfalls

- Check for required configuration parameters in .claude-plugin/plugin.json.
- Maintain session state where applicable.

## Verification

- Execute basic health check or verification command for discord.
