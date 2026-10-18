---
name: ab-judge-plugin
description: Control and test group for A/B Testing Checker. Confidence intervals
  for conversion rates should be indicated first. Add the following explanation for
  the confidence interval included in the response; Confidence intervals indicate
  the range of conversion ratios. If the question is in Japanese, ab testing should
  be translated to "A/B テスト".
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, ab_judge
    contact: fooqoofooqoo56@gmail.com
    legal: https://ab-judge-chatgpt-plugin.fooqoo56.com/term-of-use.html
---

# Ab_Judge Plugin

Control and test group for A/B Testing Checker. Confidence intervals for conversion rates should be indicated first. Add the following explanation for the confidence interval included in the response; Confidence intervals indicate the range of conversion ratios. If the question is in Japanese, ab testing should be translated to "A/B テスト".

## When to Use

Use this skill when requiring actions, queries, or workflows supported by ab_judge.

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
curl -I -s "https://ab-judge-chatgpt-plugin.fooqoo56.com/openapi.json"
```
- Verify expected 200 OK or appropriate authentication challenge.
