---
name: ai-pdf-plugin
description: Provide a URL to a PDF and search the document. Break the user question
  in multiple semantic search queries and calls as needed. Think step by step.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, Ai_PDF
    contact: support@promptapps.ai
    legal: https://plugin-3c56b9d4c8a6465998395f28b6a445b2-jexkai4vea-uc.a.run.app/legal.html
---

# Ai_Pdf Plugin

Provide a URL to a PDF and search the document. Break the user question in multiple semantic search queries and calls as needed. Think step by step.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by Ai_PDF.

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
curl -I -s "https://plugin-3c56b9d4c8a6465998395f28b6a445b2-jexkai4vea-uc.a.run.app/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
