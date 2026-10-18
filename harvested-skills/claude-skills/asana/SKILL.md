---
name: asana
description: Asana project management integration. Connects Claude Code to Asana's
  V2 MCP server (https://mcp.asana.com/v2/mcp) to create and manage tasks, search
  projects, update assignments, and track progress. Requires a one-time setup of your
  own Asana OAuth app — run /asana-setup after installing.
license: Apache License 2.0
metadata:
  hermes:
    category: claude-skills
    provider: anthropic
    author: '{''name'': ''Asana''}'
    version: 1.0.0
    tags: claude, plugin, asana
---

# Asana

Asana project management integration. Connects Claude Code to Asana's V2 MCP server (https://mcp.asana.com/v2/mcp) to create and manage tasks, search projects, update assignments, and track progress. Requires a one-time setup of your own Asana OAuth app — run /asana-setup after installing.

## When to Use

Use this skill when interacting with the asana plugin capabilities.

## Procedure

1. Enable the asana integration.
2. Invoke requested plugin commands or actions.
3. Validate output artifacts.

## Pitfalls

- Check for required configuration parameters in .claude-plugin/plugin.json.
- Maintain session state where applicable.

## Verification

- Execute basic health check or verification command for asana.
