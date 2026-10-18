---
name: alchemy-plugin
description: Request real-time blockchain data for chains like Ethereum, Polygon,
  Arbitrum and Optimism through natural language.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: service_http
    tags: openai, chatgpt-plugin, Alchemy
    contact: support@alchemy.com
    legal: https://www.alchemy.com/policies/terms
---

# Alchemy Plugin

Request real-time blockchain data for chains like Ethereum, Polygon, Arbitrum and Optimism through natural language.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by Alchemy.

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
curl -I -s "https://chat-web3-plugin.alchemy.com/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
