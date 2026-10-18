---
name: aimaster-plugin
description: If the user provides a character name, such as "psychologist", please
  send the keyword "psychologist" to the plugin. The plugin will return the corresponding
  prompt for this character, and then you can use this prompt to start the subsequent
  conversation.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, AIMaster
    contact: peter@alephf.com
    legal: https://plugin.chat2any.com/.well-known/legal-info.html
---

# Aimaster Plugin

If the user provides a character name, such as "psychologist", please send the keyword "psychologist" to the plugin. The plugin will return the corresponding prompt for this character, and then you can use this prompt to start the subsequent conversation.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AIMaster.

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
curl -I -s "https://plugin.chat2any.com/.well-known/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
