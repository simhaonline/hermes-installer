---
name: summarizeanything-pr-plugin
description: Load content of YouTube videos, web pages, and PDF links to be summarized
  by the assitant.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, SummarizeAnything_pr
    contact: yksu@csdojo.io
    legal: https://SummarizeAnything.ai/legal_info
---

# Summarizeanything_Pr Plugin

Load content of YouTube videos, web pages, and PDF links to be summarized by the assitant.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by SummarizeAnything_pr.

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
curl -I -s "/openapi.json"
```
- Verify expected 200 OK or appropriate authentication challenge.
