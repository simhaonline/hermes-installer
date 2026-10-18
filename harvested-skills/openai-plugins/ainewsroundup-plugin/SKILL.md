---
name: ainewsroundup-plugin
description: Get Today's AI News Headlines As A Clickable Link Roundup!
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, AINewsRoundup
    contact: hello@orrenprunckun.com
    legal: https://ai-news.orrenprunckun.com/terms.php
---

# Ainewsroundup Plugin

Get Today's AI News Headlines As A Clickable Link Roundup!

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AINewsRoundup.

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
curl -I -s "https://ai-news.orrenprunckun.com/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
