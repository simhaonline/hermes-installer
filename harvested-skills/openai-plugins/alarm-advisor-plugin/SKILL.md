---
name: alarm-advisor-plugin
description: Get expert advice on Telenot alarm systems and personalized support for
  your home and business security.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: service_http
    tags: openai, chatgpt-plugin, alarm_advisor
    contact: info@metzsicherheitstechnik.de
    legal: https://metzsicherheitstechnik.de/#plugin-legal-info
---

# Alarm_Advisor Plugin

Get expert advice on Telenot alarm systems and personalized support for your home and business security.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by alarm_advisor.

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
curl -I -s "https://plugin.metzsicherheitstechnik.de/.well-known/openapi.json"
```
- Verify expected 200 OK or appropriate authentication challenge.
