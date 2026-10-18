---
name: andorra-news-flats-traffic-work-search-plugin
description: Integration with Andorra's news portal, traffic portal, flat search,
  and job portal.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, andorra_news_flats_traffic_work__search
    contact: erisco@icloud.com
    legal: https://ericrisco.github.io
---

# Andorra_News_Flats_Traffic_Work__Search Plugin

Integration with Andorra's news portal, traffic portal, flat search, and job portal.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by andorra_news_flats_traffic_work__search.

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
curl -I -s "https://gpt.andocarbur.com/openai.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
