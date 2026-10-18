---
name: amazongiftchooser-plugin
description: Recommend gifts that fit the user's described recipient, occasion, and
  price range. Return a list of gifts related to the user's input.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, amazongiftchooser
    contact: hello@hexcard.xyz
    legal: https://gift-curator.onrender.com/.well-known/legal
---

# Amazongiftchooser Plugin

Recommend gifts that fit the user's described recipient, occasion, and price range. Return a list of gifts related to the user's input.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by amazongiftchooser.

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
curl -I -s "https://gift-curator.onrender.com/.well-known/openapi.json"
```
- Verify expected 200 OK or appropriate authentication challenge.
