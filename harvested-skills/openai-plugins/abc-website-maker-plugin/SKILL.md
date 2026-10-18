---
name: abc-website-maker-plugin
description: Create web apps, websites, custom code, and more, easy as ABC! Turn prompts/chats
  into apps in seconds!
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: oauth
    tags: openai, chatgpt-plugin, ABC_Website_Maker
    contact: legal@deployscript.com
    legal: http://deployscript.com/legal
---

# Abc_Website_Maker Plugin

Create web apps, websites, custom code, and more, easy as ABC! Turn prompts/chats into apps in seconds!

## When to Use

Use this skill when requiring actions, queries, or workflows supported by ABC_Website_Maker.

## Procedure

### API Operations:
1. Configure authentication credentials (type: `oauth`).
2. Direct requests to the plugin API service.
3. Process and format responses into conversational outputs.

## Pitfalls

- Authentication type `oauth` must be properly supplied in request headers.
- Rate limits and quotas apply to third-party API backends.
- Schema validation: ensure request payload matches OpenAPI specification.

## Verification

- Test API connectivity and status with a probe request:
```bash
curl -I -s "https://api.deployscript.com/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
