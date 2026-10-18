---
name: portfolio-risk
description: Comprehensive capabilities, procedures, and best practices for portfolio-risk.
license: MIT License
metadata:
  hermes:
    category: agent-teams
    provider: agent_team
    repo: Orkas-AI/Orkas
---

# Portfolio Risk

Read with `market-data` for a portfolio review, stress test, or rebalance
question. Keep account values and holdings private and use only what is needed.

Choose the calculation from the supplied data: `--mode historical` (default)
requires aligned daily decimal returns; `--mode scenario` uses weights and
declared shocks, returns no historical statistics, and needs no return series.
Do not manufacture a series to make a scenario request fit historical mode.

Historical input uses weights that sum to one and aligned daily decimal returns:

```json
{"positions":[{"symbol":"700.HK","weight":0.4,"currency":"HKD","sector":"Technology","returns":[0.01,-0.02]}],"scenarios":{"tech_down":{"Technology":-0.15}}}
```

Run:

```bash
"$ORKAS_NODE" "$ORKAS_PC_DIR/bin/run-skill.cjs" market-data stock -- portfolio-risk --input portfolio.json --confidence 0.95
```

The core calculates portfolio return series from aligned observations, annual
volatility, max drawdown, historical VaR/CVaR, HHI and top-name concentration,
sector/currency exposure, and declared linear scenario losses. VaR is a sample
statistic, not a loss ceiling.

For weight-only concentration or declared stress, use the same command with
`--mode scenario`. For simultaneous local-price and FX shocks, supply weights
already measured in `base_currency` NAV and a compound scenario:

```json
{"base_currency":"USD","positions":[{"symbol":"700.HK","weight":1,"currency":"HKD"}],"scenarios":{"stress":{"local":{"700.HK":-0.1},"fx":{"HKD":-0.05}}}}
```

The core multiplies local and FX returns and also reports their separate
contributions. Unspecified shocks are zero assumptions; the base currency
cannot move against itself. Prepare this structured input from supplied facts
without changing the source or inventing currency conversions. If the weight
basis is unknown, resolve it before a cross-currency calculation.

Review missing positions, stale prices, derivatives, leverage, FX translation,
liquidity, tax lots, and correlation regime change before recommending action.
Frame rebalance ideas as constraint-aware options with trade-offs. Do not
silently normalize invalid weights, fabricate correlations, or assume an
investor's suitability, tax status, or loss capacity.

## When to Use

- When interacting with portfolio-risk capabilities or automation.
- When required by workflows calling for Comprehensive capabilities, procedures, and best practices for portfolio-risk..

## Procedure

1. Verify prerequisites and runtime environment.
2. Execute relevant operations or CLI actions for portfolio-risk.
3. Review generated logs or outputs.

## Pitfalls

- Avoid executing unverified configurations or missing required credentials.
- Ensure schema boundaries and timeouts are respected.

## Verification

- Inspect exit status and command outputs.
- Run verification check to confirm portfolio-risk functions as expected.
