---
name: abridgedduediligence-plugin
description: 'Accepts search query objects array. Break down complex questions into
  sub-questions. Add a filter object to the query with a ticker attribute to get relevant
  results. Leave a link to allow the user to discover more details, in the format:
  abridgeddd.com/details/{acc_no}.'
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: service_http
    tags: openai, chatgpt-plugin, AbridgedDueDiligence
    contact: admin@abridgeddd.com
    legal: abridgeddd.com
---

# Abridgedduediligence Plugin

Accepts search query objects array. Break down complex questions into sub-questions. Add a filter object to the query with a ticker attribute to get relevant results. Leave a link to allow the user to discover more details, in the format: abridgeddd.com/details/{acc_no}.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AbridgedDueDiligence.

## Procedure

### API Operations:
1. Configure authentication credentials (type: `service_http`).
2. Direct requests to the plugin API service.
3. Process and format responses into conversational outputs.

## Pitfalls

- Authentication type `service_http` must be properly supplied in request headers.
- Rate limits and quotas apply to third-party API backends.
- Schema validation: ensure request payload matches OpenAPI specification.

## Verification

- Test API connectivity and status with a probe request:
```bash
curl -I -s "https://vector-api.fly.dev/.well-known/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
