---
name: algorithma-plugin
description: Shape your virtual life with in this immersive life simulator game. Type
  /start to begin type /start to start, /help, /random
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, Algorithma
    contact: ruv@ruv.net
    legal: https://algorithma.replit.app/legal
---

# Algorithma Plugin

Shape your virtual life with in this immersive life simulator game. Type /start to begin type /start to start, /help, /random

## When to Use

Use this skill when requiring actions, queries, or workflows supported by Algorithma.

## Procedure

### API Operations:
1. Configure authentication credentials (type: `none`).
2. Direct requests to the plugin API service.
3. Process and format responses into conversational outputs.

## Pitfalls

- Authentication type `none` must be properly supplied in request headers.
- Rate limits and quotas apply to third-party API backends.
- Schema validation: ensure request payload matches OpenAPI specification.

## Verification

- Test API connectivity and status with a probe request:
```bash
curl -I -s "https://algorithma.ruvnet.repl.co/openapi.json"
```
- Verify expected 200 OK or appropriate authentication challenge.
