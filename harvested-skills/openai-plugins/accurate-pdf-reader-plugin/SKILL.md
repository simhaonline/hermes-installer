---
name: accurate-pdf-reader-plugin
description: Ask the user for a URL to a PDF, then take the users input and segment
  it into semantic search queries and call our API. In absence of query, ask 'Summarise
  the PDF'.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, accurate_pdf_reader
    contact: support@avian.io
    legal: https://avian.io/terms/
---

# Accurate_Pdf_Reader Plugin

Ask the user for a URL to a PDF, then take the users input and segment it into semantic search queries and call our API. In absence of query, ask 'Summarise the PDF'.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by accurate_pdf_reader.

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
curl -I -s "https://pdf-plugin.avian.io/openapi.yaml/"
```
- Verify expected 200 OK or appropriate authentication challenge.
