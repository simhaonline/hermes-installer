---
name: apartment-search-with-apartment-list-plugin
description: Tool for searching available apartment for rent in the US, you can search
  for apartments by city, state, amenities, prices, etc. The tool will return a list
  of properties that are relevant for the search query used. If the user is not satisfied
  with the results, they can update their preferences for more personalized recommendations.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: service_http
    tags: openai, chatgpt-plugin, Apartment_Search_With_Apartment_List
    contact: plugin-help@apartmentlist.com.com
    legal: https://www.apartmentlist.com/about/terms
---

# Apartment_Search_With_Apartment_List Plugin

Tool for searching available apartment for rent in the US, you can search for apartments by city, state, amenities, prices, etc. The tool will return a list of properties that are relevant for the search query used. If the user is not satisfied with the results, they can update their preferences for more personalized recommendations.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by Apartment_Search_With_Apartment_List.

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
curl -I -s "https://partner.apartmentlist.com/openai.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
