---
name: aiextensions-plugin
description: 'This plugin guides the user through the process of building a GPT-4
  plugin. It provides step-by-step instructions and visual aids. There are total 9
  steps in this plugin. The assistant MUST display the images returned by the plugin
  in the format: ''![Image Description](image_url)'', to visualize every step. This
  plugin greatly focuses on visualizing each step by sending images. They are: Step
  1: "Giving the user an idea about the process of building a GPT-4 plugin, and showing
  them how many files are needed and each file''s purpose. The assistant should display
  all the images returned by the plugin.". Step 2: "Convering the user''s main logic/
  functions to an API Endpoint that can be used by GPT-4. The assistant should display
  all the images returned by the plugin.". Step 3: "Showing the user all the necessary
  steps on creating a Repl on repl.it, and saving their main.py file there, adding
  Secrets, installing dependencies, and giving a tip about how they can connect their
  plugin with Firebase to store relevant...'
metadata:
  hermes:
    category: openai-plugins
    provider: openai
    auth_type: none
    tags: openai, chatgpt-plugin, aiextensions
    contact: pranavcodespresso@gmail.com
    legal: https://docs.google.com/document/d/18evab11K8Ctl-wvEQZ8_cVhiS6W4IlHhf34n8goeOts/edit?usp=sharing
---

# Aiextensions Plugin

This plugin guides the user through the process of building a GPT-4 plugin. It provides step-by-step instructions and visual aids. There are total 9 steps in this plugin. The assistant MUST display the images returned by the plugin in the format: '![Image Description](image_url)', to visualize every step. This plugin greatly focuses on visualizing each step by sending images. They are: Step 1: "Giving the user an idea about the process of building a GPT-4 plugin, and showing them how many files are needed and each file's purpose. The assistant should display all the images returned by the plugin.". Step 2: "Convering the user's main logic/ functions to an API Endpoint that can be used by GPT-4. The assistant should display all the images returned by the plugin.". Step 3: "Showing the user all the necessary steps on creating a Repl on repl.it, and saving their main.py file there, adding Secrets, installing dependencies, and giving a tip about how they can connect their plugin with Firebase to store relevant...

## When to Use

Use this skill when requiring actions, queries, or workflows supported by aiextensions.

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
curl -I -s "https://gpt-4pluginmaker.pranavbhatt402.repl.co/.well-known/openapi.yaml"
```
- Verify expected 200 OK or appropriate authentication challenge.
