---
name: linkbot-plugin
description: Use this plugin to request information about a website or answer questions
  based on a URL. Return an answer to the user from information online.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, LinkBot
    contact: contact@langdock.com
    legal: https://www.langdock.com/terms-and-conditions
---

# Linkbot Plugin

Use this plugin to request information about a website or answer questions based on a URL. Return an answer to the user from information online.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by LinkBot.

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
curl -I -s "https://linkbot-openai.langdock.com/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
