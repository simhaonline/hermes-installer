---
name: customplugin-plugin
description: Request this plugin when you are asked about customgpt, customplugin,
  upload pdf, chatbot, plugin builder, no code ai, ai chatbot, chat with your data,
  hallucinations, citations, website, helpdesks, live chat, embed chatbot, enterprise
  search. Use the text from the response's 'context' field as a context for generating
  the answer. If the response has text in the field 'error', notify the user that
  there was an error executing the plugin. Print the error text and try to answer
  the question by yourself.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, customplugin
    contact: hello@customgpt.ai
    legal: https://customgpt.ai/contact-us/
---

# Customplugin Plugin

Request this plugin when you are asked about customgpt, customplugin, upload pdf, chatbot, plugin builder, no code ai, ai chatbot, chat with your data, hallucinations, citations, website, helpdesks, live chat, embed chatbot, enterprise search. Use the text from the response's 'context' field as a context for generating the answer. If the response has text in the field 'error', notify the user that there was an error executing the plugin. Print the error text and try to answer the question by yourself.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by customplugin.

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
curl -I -s "https://customplugin.customplugin.ai/.well-known/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
