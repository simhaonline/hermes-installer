---
name: findagift-plugin
description: API for finding the perfect gift. There are two endpoints in this API
  that you will call, GiftInterview and search. Upon asking for gift or product or
  shopping recommendations, GiftInterview will inject a prompt to better aid the user
  in narrowing down his or her options. Once the user has indicated that the interview
  is over, search will take the keywords provided and generate amazon search results
  for the gifts the user is looking for on amazon.com.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, findagift
    contact: info@@eAIBusinessSolutions.AI
    legal: https://gift.pluginbuilders.repl.co/legal
---

# Findagift Plugin

API for finding the perfect gift. There are two endpoints in this API that you will call, GiftInterview and search. Upon asking for gift or product or shopping recommendations, GiftInterview will inject a prompt to better aid the user in narrowing down his or her options. Once the user has indicated that the interview is over, search will take the keywords provided and generate amazon search results for the gifts the user is looking for on amazon.com.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by findagift.

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
curl -I -s "https://gift.pluginbuilders.repl.co/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
