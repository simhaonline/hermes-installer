---
name: aa-card-creator-plugin
description: AA_Card_creator can create a social media card or cheatsheet from a given
  title and a list of summarization points as input.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, AA_Card_creator
    contact: contact@for.io
    legal: https://for.io/legal/tos
---

# Aa_Card_Creator Plugin

AA_Card_creator can create a social media card or cheatsheet from a given title and a list of summarization points as input.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AA_Card_creator.

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
curl -I -s "https://cards.for.io/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
