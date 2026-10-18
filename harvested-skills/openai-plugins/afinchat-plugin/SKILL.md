---
name: afinchat-plugin
description: Get information and analyze A-share stocks, like news, quotes, financial
  statement, but search for information only from China.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: service_http
    tags: openai, chatgpt-plugin, AFinChat
    contact: m.linearalgebra@gmail.com
    legal: https://afinchat.chengdoujiang.cn/legal-info
---

# Afinchat Plugin

Get information and analyze A-share stocks, like news, quotes, financial statement, but search for information only from China.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AFinChat.

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
curl -I -s "https://afinchat.chengdoujiang.cn/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
