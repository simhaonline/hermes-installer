---
name: ad4mat-plugin
description: API to create affilliat links in order to monetize traffic to external
  online stores and services. It´s important to request the right site Id from the
  user. The API give an array of urls back. The structur tell you what is the affilliat
  link for the requested url and its a monitized link. That means the enduser get
  a commission if he use thsi link. Affiliate Marketing, Performance Marketing, Link
  monetization, Referral Marketing.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, ad4mat
    contact: sascha.hoffmann@advanced-store.com
    legal: https://www.ad4mat.com/terms-of-service
---

# Ad4Mat Plugin

API to create affilliat links in order to monetize traffic to external online stores and services. It´s important to request the right site Id from the user. The API give an array of urls back. The structur tell you what is the affilliat link for the requested url and its a monitized link. That means the enduser get a commission if he use thsi link. Affiliate Marketing, Performance Marketing, Link monetization, Referral Marketing.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by ad4mat.

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
curl -I -s "https://ad4mat-api-chatgpt-plugin.ufostart-dev.workers.dev/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
