---
name: ai2sql-plugin
description: Converts a natural language text into an SQL query.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: oauth
    tags: openai, chatgpt-plugin, AI2sql
    contact: support@ai2sql.io
    legal: https://ai2sql.io/
---

# Ai2Sql Plugin

Converts a natural language text into an SQL query.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AI2sql.

## Procedure

### API Operations:
1. Configure authentication credentials (type: `oauth`).
2. Direct requests to the plugin API service.
3. Process and format responses into conversational outputs.

## Pitfalls

- Authentication type `oauth` must be properly supplied in request headers.
- Rate limits and quotas apply to third-party API backends.
- Schema validation: ensure request payload matches OpenAPI specification.

## Verification

- Test API connectivity and status with a probe request:
```bash
curl -I -s "https://chatgpt-plugins-ashy.vercel.app/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
