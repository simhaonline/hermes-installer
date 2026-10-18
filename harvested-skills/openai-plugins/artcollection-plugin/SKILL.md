---
name: artcollection-plugin
description: Search through millions of art pieces from The Metropolitan Museum of
  Art.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, ArtCollection
    contact: cpagym@gmail.com
    legal: http://www.cpanlp.com/
---

# Artcollection Plugin

Search through millions of art pieces from The Metropolitan Museum of Art.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by ArtCollection.

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
curl -I -s "https://artcollection--chao-gu-ge-lei.repl.co/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
