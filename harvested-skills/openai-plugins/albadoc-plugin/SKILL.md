---
name: albadoc-plugin
description: This plugin retrieves detailed information about drugs and their active
  ingredients or active ingredients and their correspending drugs that they are used
  in. It can also generate images to help visualize drugs or active ingredients.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, albadoc
    contact: pranav.bhatt@albadoctor.com
    legal: https://docs.google.com/document/d/13csNyS75gECA9ghZByK6KVJmLDzG9hOCcWnmh15VXg8/edit?usp=sharing
---

# Albadoc Plugin

This plugin retrieves detailed information about drugs and their active ingredients or active ingredients and their correspending drugs that they are used in. It can also generate images to help visualize drugs or active ingredients.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by albadoc.

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
curl -I -s "https://gpt-4albadocplugin.pranavbhatt402.repl.co/.well-known/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
