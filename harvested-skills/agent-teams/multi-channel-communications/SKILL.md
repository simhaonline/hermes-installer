---
name: multi-channel-communications
description: Manage conversations across 20+ messaging platforms via OpenClaw gateway
license: Apache License 2.0
metadata:
  hermes:
    category: agent-teams
    provider: agent_team
    repo: 1mancompany/OneManCompany
---

# Multi-Channel Communications

You operate an OpenClaw gateway that connects to multiple messaging platforms simultaneously.

## Supported Channels

WhatsApp, Telegram, Slack, Discord, iMessage (via BlueBubbles), Signal, Google Chat,
Microsoft Teams, Matrix, IRC, LINE, Feishu, Twitch, and more.

## Capabilities

- **Send/receive messages** across all connected channels
- **Session management** — isolated sessions per conversation with persistent state
- **Voice interaction** — wake words, TTS via ElevenLabs
- **Browser automation** — managed Chrome for web tasks
- **Webhooks & cron jobs** — scheduled automation
- **Inter-agent messaging** — route between multiple agent workspaces

## In-Chat Commands

When interacting via channels, users can use: `/think high`, `/status`, `/reset`, `/compact`, `/usage`.

## Best Practices

1. Keep messages concise and platform-appropriate (shorter for chat, detailed for email)
2. Use session isolation to maintain context per conversation
3. Leverage cron jobs for recurring communications
4. Monitor channel health via `/status` and `openclaw doctor`

## When to Use

- When interacting with multi-channel-communications capabilities or automation.
- When required by workflows calling for Manage conversations across 20+ messaging platforms via OpenClaw gateway.

## Procedure

1. Verify prerequisites and runtime environment.
2. Execute relevant operations or CLI actions for multi-channel-communications.
3. Review generated logs or outputs.

## Pitfalls

- Avoid executing unverified configurations or missing required credentials.
- Ensure schema boundaries and timeouts are respected.

## Verification

- Inspect exit status and command outputs.
- Run verification check to confirm multi-channel-communications functions as expected.
