---
name: abc-to-audio-plugin
description: Converts ABC music notation to WAV, MIDI, and PostScript files. This
  allows users to input ABC notation and receive corresponding audio files and sheet
  URLs in return.
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, abc_to_audio
    contact: abcchatgpt@karel-hovorka.eu
    legal: https://abcaudio.vynalezce.com/legal/
---

# Abc_To_Audio Plugin

Converts ABC music notation to WAV, MIDI, and PostScript files. This allows users to input ABC notation and receive corresponding audio files and sheet URLs in return.

## When to Use

Use this skill when requiring actions, queries, or workflows supported by abc_to_audio.

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
curl -I -s "https://abcaudio.vynalezce.com/openapi.json"
```
- Verify expected 200 OK or appropriate authentication challenge.
