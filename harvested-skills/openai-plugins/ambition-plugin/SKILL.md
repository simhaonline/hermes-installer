---
name: ambition-plugin
description: Use the Ambition plugin for anything related to jobs and resumes. You
  will help users find relevant jobs near them. To best use it, first ask clarifying
  questions about what kind of job the user is looking for before making a search.
  If the search results are empty, do not make up jobs. Do not make up details about
  job information. If a user wants to find out more about a job, direct them to the
  job page.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: service_http
    tags: openai, chatgpt-plugin, Ambition
    contact: support@remoteambition.com
    legal: https://remoteambition.com/terms
---

# Ambition Plugin

Use the Ambition plugin for anything related to jobs and resumes. You will help users find relevant jobs near them. To best use it, first ask clarifying questions about what kind of job the user is looking for before making a search. If the search results are empty, do not make up jobs. Do not make up details about job information. If a user wants to find out more about a job, direct them to the job page.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by Ambition.

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
curl -I -s "https://api.remoteambition.com/ai/v1/api.json"
```
- Verify expected 200 OK or appropriate authentication challenge.
