---
name: amazonfinds-plugin
description: Help the user with searching for products on Amazon. You can ask to search
  for specific Amazon products.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, amazonfinds
    contact: elliesophia1@gmail.com
    legal: https://amazfinds.aitoolbot.repl.co/legal
---

# Amazonfinds Plugin

Help the user with searching for products on Amazon. You can ask to search for specific Amazon products.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by amazonfinds.

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
curl -I -s "https://amazfinds.aitoolbot.repl.co/openapi.json"
```
- Verify expected 200 OK or appropriate authentication challenge.
