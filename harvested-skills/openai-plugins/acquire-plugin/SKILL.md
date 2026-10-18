---
name: acquire-plugin
description: Search from hundreds of startups for sale.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, acquire
    contact: support@acquire.com
    legal: https://acquire.com/legal/
---

# Acquire Plugin

Search from hundreds of startups for sale.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by acquire.

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
curl -I -s "https://acquire-chatgpt.fly.dev/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
