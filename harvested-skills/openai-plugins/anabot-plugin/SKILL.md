---
name: anabot-plugin
description: 'AnaBot is your conversational co-navigator for the well-being industry.
  With AnaBot, you''re not just staying updated, you''re staying ahead. From the latest
  trends to the performance of various organizations, AnaBot equips you with the knowledge
  to make informed decisions. Here are a few examples of the questions you could ask:
  could you give some statistics regarding the opioid usage ? What are some ways to
  help stop the spread of misinformation ? how does my topical product need to conform
  to guidelines in order to sell it to the public? Why are dermatological products
  tested on animals? What is the leading cause of serious disability in the U.S.?'
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, anabot
    contact: contact@langdock.com
    legal: https://www.langdock.com/terms-and-conditions
---

# Anabot Plugin

AnaBot is your conversational co-navigator for the well-being industry. With AnaBot, you're not just staying updated, you're staying ahead. From the latest trends to the performance of various organizations, AnaBot equips you with the knowledge to make informed decisions. Here are a few examples of the questions you could ask: could you give some statistics regarding the opioid usage ? What are some ways to help stop the spread of misinformation ? how does my topical product need to conform to guidelines in order to sell it to the public? Why are dermatological products tested on animals? What is the leading cause of serious disability in the U.S.?

## When to Use

Use this skill when requiring actions, queries, or workflows supported by anabot.

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
curl -I -s "https://anabot-openai.langdock.com/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
