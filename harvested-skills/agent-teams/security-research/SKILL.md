---
name: security-research
description: Comprehensive capabilities, procedures, and best practices for security-research.
license: MIT License
metadata:
  hermes:
    category: agent-teams
    provider: agent_team
    repo: Orkas-AI/Orkas
---

# Security Research

Read with `market-data` for a company thesis, comparison, factor screen, or
watchlist. The goal is a decision-ready evidence map, not a forced rating.

## Research contract

- Lock security, listing, market, horizon, currency, and comparison set.
- Prefer filings, exchange notices, and issuer releases for current business
  facts. Distinguish filing period from retrieval date.
- Separate business quality, growth, balance sheet, cash generation, valuation,
  price/volume behavior, ownership/liquidity, and event risk.
- Reconcile conflicts rather than averaging them away. Missing a field lowers
  coverage; it is not neutral or zero.
- End with base/bull/bear cases, catalysts, invalidation conditions, and the
  next evidence that would change the view.

Run deterministic time-series and supplied-fundamental analysis:

```bash
"$ORKAS_NODE" "$ORKAS_PC_DIR/bin/run-skill.cjs" market-data stock -- analyze --input history.json --symbol 600519.SH --source user-file
```

Run a cross-sectional screen:

```bash
"$ORKAS_NODE" "$ORKAS_PC_DIR/bin/run-skill.cjs" market-data stock -- screen --input universe.json
```

For a requested historical price cutoff, use `--cutoff YYYY-MM-DD` on `analyze`
or `screen`. The core selects bars in memory, preserves the source file and
reports excluded-bar counts. `--as-of` alone remains strict validation and
rejects later bars. Neither option proves point-in-time availability of
fundamentals or universe membership; keep those evidence gaps explicit.

The screen uses only covered factors, reports eligibility and coverage, and
produces a relative research priority—not a buy/sell instruction. Explain each
rank through its factor components and name survivorship, point-in-time, FX,
and sector-comparability limits when applicable.

For event/news questions, retrieve fresh evidence; do not infer today's event
state from historical bars. Rumors remain labeled and never override filings.

## When to Use

- When interacting with security-research capabilities or automation.
- When required by workflows calling for Comprehensive capabilities, procedures, and best practices for security-research..

## Procedure

1. Verify prerequisites and runtime environment.
2. Execute relevant operations or CLI actions for security-research.
3. Review generated logs or outputs.

## Pitfalls

- Avoid executing unverified configurations or missing required credentials.
- Ensure schema boundaries and timeouts are respected.

## Verification

- Inspect exit status and command outputs.
- Run verification check to confirm security-research functions as expected.
