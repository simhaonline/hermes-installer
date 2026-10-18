---
name: aerodex-plugin
description: This interacts with the an aviation API allowing you to get information
  useful for pilots
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, AeroDex
    contact: davide.zambiasi@gmail.com
    legal: https://www.aerodex.xyz/policy
---

# Aerodex Plugin

This interacts with the an aviation API allowing you to get information useful for pilots

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AeroDex.

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
curl -I -s "https://pilots.aerodex.xyz/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
