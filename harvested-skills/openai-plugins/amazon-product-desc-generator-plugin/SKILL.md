---
name: amazon-product-desc-generator-plugin
description: Tool for AMAZON product listing, you can write a product description
  in line with AMAZON, which is divided into a title and a five-point advantage description,
  and list the title and advantages in a table. No matter what language the user enters,
  you should reply in English.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, AMAZON_product_desc_generator
    contact: cjyjia@live.cn
    legal: https://turboooo.com/legal
---

# Amazon_Product_Desc_Generator Plugin

Tool for AMAZON product listing, you can write a product description in line with AMAZON, which is divided into a title and a five-point advantage description, and list the title and advantages in a table. No matter what language the user enters, you should reply in English.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AMAZON_product_desc_generator.

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
curl -I -s "https://turboooo.com/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
