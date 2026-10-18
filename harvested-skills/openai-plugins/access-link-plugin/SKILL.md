---
name: access-link-plugin
description: Plugin for accessing web page data from a specific URL. Use it whenever
  a user asks something about a specific URL they provide.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, access_link
    contact: dominickmalzone@gmail.com
    legal: https://www.accesslinks.ai/legal-info
---

# Access_Link Plugin

Plugin for accessing web page data from a specific URL. Use it whenever a user asks something about a specific URL they provide.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by access_link.

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
curl -I -s "https://www.accesslinks.ai/.well-known/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
