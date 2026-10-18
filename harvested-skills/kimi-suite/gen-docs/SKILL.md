---
name: gen-docs
description: Update Kimi Code CLI user documentation.
license: Apache License 2.0
metadata:
  hermes:
    category: kimi-suite
    provider: kimi
    repo: MoonshotAI/kimi-cli
---

# Gen Docs

Update Kimi Code CLI user documentation.

现在我们正在为当前项目 Kimi Code CLI 编写和维护用户文档，文档内容在 docs 目录下，docs/AGENTS.md 中有对文档的说明。

我们现在对代码库有了一些修改，请你参考最近的 git commit、staged changes、changelog.md 等的内容，根据 AGENTS.md 中的信息，必要时找到实际的代码全文，确保理解了所有变更对产品用户体验的真实改变，然后逐页、逐段地检查和更新文档内容。

你应该首先确保英文 changelog 使用 `node docs/scripts/sync-changelog.mjs` 进行了同步，然后确保中文文档符合最新代码的行为，最后，使用 translate-docs skill 进行双语同步。

## When to Use

- When interacting with gen-docs capabilities or automation.
- When required by workflows calling for Update Kimi Code CLI user documentation..

## Procedure

1. Verify prerequisites and runtime environment.
2. Execute relevant operations or CLI actions for gen-docs.
3. Review generated logs or outputs.

## Pitfalls

- Avoid executing unverified configurations or missing required credentials.
- Ensure schema boundaries and timeouts are respected.

## Verification

- Inspect exit status and command outputs.
- Run verification check to confirm gen-docs functions as expected.
