---
name: writing-guidelines
description: Review docs/prose for Writing Guidelines compliance. Use when asked to
  "review my docs", "check writing style", "audit prose", "review docs voice and tone",
  or "check this page against the writing handbook".
license: MIT
metadata:
  author: vercel
  version: 1.0.0
  argument-hint: <file-or-pattern>
  hermes:
    category: vercel-agent-skills
    provider: vercel
    repo: vercel-labs/agent-skills
---

# Writing Guidelines

Review files for compliance with Writing Guidelines.

## How It Works

1. Fetch the latest guidelines from the source URL below
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in the fetched guidelines
4. Output findings in the terse `file:line` format

## Guidelines Source

Fetch fresh guidelines before each review:

```
https://raw.githubusercontent.com/vercel-labs/writing-guidelines/main/command.md
```

Use WebFetch to retrieve the latest rules. The fetched content contains all the rules and output format instructions.

## Usage

When a user provides a file or pattern argument:
1. Fetch guidelines from the source URL above
2. Read the specified files
3. Apply all rules from the fetched guidelines
4. Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.

## When to Use

- When interacting with writing-guidelines capabilities or automation.
- When required by workflows calling for Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs voice and tone", or "check this page against the writing handbook"..

## Procedure

1. Verify prerequisites and runtime environment.
2. Execute relevant operations or CLI actions for writing-guidelines.
3. Review generated logs or outputs.

## Pitfalls

- Avoid executing unverified configurations or missing required credentials.
- Ensure schema boundaries and timeouts are respected.

## Verification

- Inspect exit status and command outputs.
- Run verification check to confirm writing-guidelines functions as expected.
