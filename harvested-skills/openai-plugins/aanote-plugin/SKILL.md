---
name: aanote-plugin
description: 'This plugin designed to save conversation summaries, generate articles
  from these summaries, and allow users to retrieve historical chat data. You must
  follow below instructions: 1. Conversation Summarization and Storage: 1.1 When the
  user initiates Summarize this chat, you must provide a concise summary of the conversation.
  1.2 This summary should be stored for easy retrieval. 2. Article Generation: 2.1
  When the user initiates article creation prompt the user for the number of chapters
  and the desired word count per chapter. 2.2 Use the stored conversation summaries
  to generate the article content, ensuring that each chapter meets a minimum of 800
  words unless specified otherwise by the user. 2.3 After every two chapters, present
  article link to the user,Continue this iterative process until the article is complete.
  3. Historical Chat Retrieval: 3.1 If a user requests to Retrieve chat history ,
  ask for specific keywords or phrases to assist in the search. 3.2 Search the stored
  summaries for these keywords...'
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: oauth
    tags: openai, chatgpt-plugin, AANote
    contact: xforward77@gmail.com
    legal: https://aa-note.aier3.com/home/term.txt
---

# Aanote Plugin

This plugin designed to save conversation summaries, generate articles from these summaries, and allow users to retrieve historical chat data. You must follow below instructions: 1. Conversation Summarization and Storage: 1.1 When the user initiates Summarize this chat, you must provide a concise summary of the conversation. 1.2 This summary should be stored for easy retrieval. 2. Article Generation: 2.1 When the user initiates article creation prompt the user for the number of chapters and the desired word count per chapter. 2.2 Use the stored conversation summaries to generate the article content, ensuring that each chapter meets a minimum of 800 words unless specified otherwise by the user. 2.3 After every two chapters, present article link to the user,Continue this iterative process until the article is complete. 3. Historical Chat Retrieval: 3.1 If a user requests to Retrieve chat history , ask for specific keywords or phrases to assist in the search. 3.2 Search the stored summaries for these keywords...

## When to Use

Use this skill when requiring actions, queries, or workflows supported by AANote.

## Procedure

### API Operations:
1. Configure authentication credentials (type: `oauth`).
2. Direct requests to the plugin API service.
3. Process and format responses into conversational outputs.

## Pitfalls

- Authentication type `oauth` must be properly supplied in request headers.
- Rate limits and quotas apply to third-party API backends.
- Schema validation: ensure request payload matches OpenAPI specification.

## Verification

- Test API connectivity and status with a probe request:
```bash
curl -I -s "/com/openai/aa/note/doc/plugin.api"
```
- Verify expected 200 OK or appropriate authentication challenge.
