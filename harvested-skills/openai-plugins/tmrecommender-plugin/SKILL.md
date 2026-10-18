---
name: tmrecommender-plugin
description: Help users with trademark registration recommendation on NICE classifications
  and preapproved Goods & Services items. The recommendation is based on the business
  description given by the users.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, tmRecommender
    contact: vincent.chen@aiplux.com
    legal: https://inpas.aiplux.com/termsofuse
---

# Tmrecommender Plugin

Help users with trademark registration recommendation on NICE classifications and preapproved Goods & Services items. The recommendation is based on the business description given by the users.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by tmRecommender.

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
curl -I -s "https://inta.aiplux.com/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
