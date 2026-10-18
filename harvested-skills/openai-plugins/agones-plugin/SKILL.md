---
name: agones-plugin
description: 'Access soccer match results from Agones. Keep in mind soccer is called
  football in Europe. Results go back to 2007 until current games being played right
  now and all scheduled matches for the next 10 days. Results cover most countries
  and leagues in the world. Guidelines: - Use single-line string for team1, team2
  and all other parameters. - Pass date_from and date_until in a YYYY-MM-DD format
  - If one team is passed, returned matches will be about this team and any other
  opponent. - If two teams are passed, matches between these two teams will be returned.
  - if date_type is ''latest'', then the most recent match will be returned. - If
  date_type is ''next'', then the next match will be returned. - If date_type is ''range'',
  then all matches between date_from and date_until will be returned. - Only use date_from
  and date_until when date_type is ''range'' - otherwise these are not used. - If
  a match is currently live, the current minute will also be provided. Results are
  an array of dictionaries in the format: { "hom...'
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, Agones
    contact: info@agones.gr
    legal: https://agones.gr/terms
---

# Agones Plugin

Access soccer match results from Agones. Keep in mind soccer is called football in Europe. Results go back to 2007 until current games being played right now and all scheduled matches for the next 10 days. Results cover most countries and leagues in the world. Guidelines: - Use single-line string for team1, team2 and all other parameters. - Pass date_from and date_until in a YYYY-MM-DD format - If one team is passed, returned matches will be about this team and any other opponent. - If two teams are passed, matches between these two teams will be returned. - if date_type is 'latest', then the most recent match will be returned. - If date_type is 'next', then the next match will be returned. - If date_type is 'range', then all matches between date_from and date_until will be returned. - Only use date_from and date_until when date_type is 'range' - otherwise these are not used. - If a match is currently live, the current minute will also be provided. Results are an array of dictionaries in the format: { "hom...

## When to Use

Use this skill when requiring actions, queries, or workflows supported by Agones.

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
curl -I -s "https://agones.gr/.well-known/chatgpt.json"
```
- Verify expected 200 OK or appropriate authentication challenge.
