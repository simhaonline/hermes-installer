---
name: apexmap-plugin
description: Plugin for checking the current and predicting the future APEX Legends
  Map. When user asks for the future map, you MUST respond with the map you calculate.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, ApexMap
    contact: legal@apexmap.com
    legal: https://apex-map-plugin-d1u8.vercel.app/legal.txt
---

# Apexmap Plugin

Plugin for checking the current and predicting the future APEX Legends Map. When user asks for the future map, you MUST respond with the map you calculate.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by ApexMap.

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
curl -I -s "https://apex-map-plugin-d1u8.vercel.app/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
