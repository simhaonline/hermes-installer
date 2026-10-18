---
name: ablestyle-plugin
description: Able Style Fashion helps you decide what to wear. Able Style answers
  the question, 'What shall I wear?' and gives the user between 1 and 3 stylish outfit
  suggestions.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: service_http
    tags: openai, chatgpt-plugin, AbleStyle
    contact: contact@able.style
    legal: https://able.style/#/terms
---

# Ablestyle Plugin

Able Style Fashion helps you decide what to wear. Able Style answers the question, 'What shall I wear?' and gives the user between 1 and 3 stylish outfit suggestions.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AbleStyle.

## Procedure

### API Operations:
1. Configure authentication credentials (type: `service_http`).
2. Direct requests to the plugin API service.
3. Process and format responses into conversational outputs.

## Pitfalls

- Authentication type `service_http` must be properly supplied in request headers.
- Rate limits and quotas apply to third-party API backends.
- Schema validation: ensure request payload matches OpenAPI specification.

## Verification

- Test API connectivity and status with a probe request:
```bash
curl -I -s "https://styledao-prod.web.app/assets/openai/openai.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
