---
name: aitickerchat-document-retrieval-plugin
description: Plugin for searching through SEC filings as well as Earnings Call Transcripts
  to find answers to stock market questions and retrieve relevant information. Use
  it whenever a user asks for stock information that could be found in any SEC document
  filing or Earnings Call Transcript.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: service_http
    tags: openai, chatgpt-plugin, aitickerchat_document_retrieval
    contact: scooper@intuitivecloudsolutions.com
    legal: https://aitickerchat.com/terms-of-service
---

# Aitickerchat_Document_Retrieval Plugin

Plugin for searching through SEC filings as well as Earnings Call Transcripts to find answers to stock market questions and retrieve relevant information. Use it whenever a user asks for stock information that could be found in any SEC document filing or Earnings Call Transcript.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by aitickerchat_document_retrieval.

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
curl -I -s "https://stock-advisor.com/.well-known/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
