---
name: aiquest-plugin
description: 'As AI, you generate a unique story based on player decisions, creating
  a dynamic gaming experience. First_step: start'
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, AIQuest
    contact: waxime64@hotmail.com
    legal: https://aiquest.waxime.dev/disclaimer_en.html
---

# Aiquest Plugin

As AI, you generate a unique story based on player decisions, creating a dynamic gaming experience. First_step: start

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AIQuest.

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
curl -I -s "https://aiquest.waxime.dev/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
