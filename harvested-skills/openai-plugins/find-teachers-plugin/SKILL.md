---
name: find-teachers-plugin
description: Find the perfect language teachers and tutors from across the world.
  Lessons and courses are personalized to help achieve your learning goals whether
  it be exams, certifications, business, travel or more.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, find_teachers
    contact: amazingtalker@amazingtalker.com
    legal: https://en.amazingtalker.com/privacy-and-terms
---

# Find_Teachers Plugin

Find the perfect language teachers and tutors from across the world. Lessons and courses are personalized to help achieve your learning goals whether it be exams, certifications, business, travel or more.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by find_teachers.

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
curl -I -s "https://en.amazingtalker.com/.well-known/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
