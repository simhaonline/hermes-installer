---
name: aistrologer-plugin
description: Search for the horoscope for each zodiac sign. You can also specify the
  exact date for which you want the horoscope, and pass a list of comma-separated
  values for both the sign and the date.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: service_http
    tags: openai, chatgpt-plugin, AIstrologer
    contact: info@bootstrapden.com
    legal: https://aistrologer.io/legal.html
---

# Aistrologer Plugin

Search for the horoscope for each zodiac sign. You can also specify the exact date for which you want the horoscope, and pass a list of comma-separated values for both the sign and the date.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AIstrologer.

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
curl -I -s "https://aistrologer.io/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
