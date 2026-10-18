---
name: context7
description: Upstash Context7 MCP server for up-to-date documentation lookup. Connects
  to Context7's hosted remote MCP server (https://mcp.context7.com/mcp) — no local
  Node.js or npx required — to pull version-specific documentation and code examples
  directly from source repositories into your LLM context. Authenticate with Context7
  when prompted.
license: Apache License 2.0
metadata:
  hermes:
    category: claude-skills
    provider: anthropic
    author: '{''name'': ''Upstash''}'
    version: 1.0.0
    tags: claude, plugin, context7
---

# Context7

Upstash Context7 MCP server for up-to-date documentation lookup. Connects to Context7's hosted remote MCP server (https://mcp.context7.com/mcp) — no local Node.js or npx required — to pull version-specific documentation and code examples directly from source repositories into your LLM context. Authenticate with Context7 when prompted.

## When to Use

Use this skill when interacting with the context7 plugin capabilities.

## Procedure

1. Enable the context7 integration.
2. Invoke requested plugin commands or actions.
3. Validate output artifacts.

## Pitfalls

- Check for required configuration parameters in .claude-plugin/plugin.json.
- Maintain session state where applicable.

## Verification

- Execute basic health check or verification command for context7.
