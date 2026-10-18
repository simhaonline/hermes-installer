---
name: alagaai-plugin
description: Provides a knowledge base of the programs and services from the Department
  of Health of the Philippines.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, alagaAI
    contact: rogene@1024technologies.ca
    legal: https://1024technologies.ca/legal/terms
---

# Alagaai Plugin

Provides a knowledge base of the programs and services from the Department of Health of the Philippines.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by alagaAI.

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
curl -I -s "https://alaga-ai-h43cosb3ia-uc.a.run.app/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
