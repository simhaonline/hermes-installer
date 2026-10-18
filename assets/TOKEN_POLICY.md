# Predict-A-Trade Hermes Usage & Token Optimization Policy

All supplied skills, agent profiles, catalogs, existing MCP registrations, API credentials
and memory providers remain available. Capability retention does not require sending every
tool schema and every skill description on every API request.

## 1. Core Token Governance & Efficiency
- **Native Tool Search**: Enabled, 2000-token listing budget. Tool bodies are discovered on demand.
- **Compression Policy**: Supported lean tail, threshold 0.75, target ratio 0.20, recent message protection.
  Compression is lossy; save exact decisions, paths and unfinished work in handoff files.
  Do not force micro-compaction every turn; it repeatedly breaks prompt caching.
- **Selective Skill Indexing**: Specialist profiles keep all skill files in storage, with unrelated
  names hidden from their initial prompt index via `skills.disabled`. The local catalog (`hermes-skill-catalog`)
  locates any hidden skill and enables it on demand without token bloat.
- **Search & Tool Hygiene**: Search with `rg` / `grep`; read relevant line ranges rather than full dumps;
  save large output to disk; return concise paths and synthesized findings.

## 2. Terminal Output Compression (`token-saver`)
Hermes includes the **Token-Saver** compression engine (via `token-saver` and `hermes-token-saver`),
powered by 36 specialized local processors (supporting git diff, pytest, jest, cargo, go test, docker,
kubectl, terraform, npm/pip/cargo, linters, and search tools):
- Compresses noisy execution output locally with zero API cost, saving **60% to 99%** of output tokens.
- Pipe verbose output directly through compression:
  ```bash
  git diff | token-saver compress "git diff"
  pytest | token-saver compress "pytest"
  cargo build | token-saver compress "cargo build"
  ```
- Benchmark compression on any command: `token-saver benchmark "<cmd>"`
- Review lifetime token savings: `token-saver stats`

## 3. Progressive Disclosure Architecture
Following `skill-progressive-disclosure-design`:
- **Triggering (YAML description)**: Kept concise and keyword-dense in the main prompt index.
- **Workflow (SKILL.md body)**: Stays under ~400 lines; provides decision paths and step sequences.
- **Reference Data (`references/*.md`)**: Schemas, matrices, and large lookup tables are loaded only on demand when a sub-decision requires them.
- **Deterministic Scripts (`scripts/*`)**: Formatting, regex parsing, and validation run directly as scripts with **zero context cost**.

## 4. Routine Task Delegation
Following `token-saver-delegation`:
- Routine, low-judgment tasks (boilerplate scaffolding, DTOs/interfaces, CRUD templates, form validation schemas, test fixtures) are delegated to fast/free sub-models or subagents.
- Frontier reasoning models are reserved for architecture, complex algorithms, security boundaries, and debugging.

## 5. Built-in Production Ecosystem
- **Retained Skills Library**: 317 Verified Skills in core index + 1,450+ Skills across Predict-A-Trade Ops, Quant Trading, Pine Script, Databases, Modern Backend, UI/UX, Security, Omnichannel Messaging, Microsoft Fabric, Web Scraping, Knowledge Graphs, and Workflows.
- **Specialist Profiles**: 42 Specialist Agent Profiles (incl. `pat-operations`, `token-optimizer`, `tradingview-quant`, `fabric-engineer`, `metatrader-quant`, `database-optimizer`, `backend-architect`, `web-scraping-specialist`, `knowledge-graph-architect`).
- **Agent Personas**: 411+ Agents (329 Agency Agents + 63 Specialist Personas + 13 Trading Specs + 5 Fabric Agents + Personal AI Employee).
- **Curated MCP Suite**: 18 Production-Ready Servers in `mcp-library/recommended-mcp-servers.json` (MetaTrader5, TimescaleDB, QuestDB, Redis, WhatsApp, Telegram, Discord, TradingView Signals, Conda CLI, Microsoft Fabric, Postgres, SQLite, Puppeteer, Playwright, Brave Search, Docker).
- **Native Plugins**: `homeassistant`, `token-saver`, `superpowers`, `quantmind`, `memstack`, `deer-flow`, `agent-cron`, `open-company`, `scrapling`, `tradingview-pinescript`, `mql5-libraries`, `fabric-plugins`, `conda-plugins`.
- **Persistent State**: Full Predict-A-Trade operational memories (`MEMORY.md`, `USER.md`, 73 pending memories) and automated cron watchdogs (`jobs.json`, `executions.db`, payment-symmetry monitor).

## 6. On-Demand Usage Commands
- `hermes-skill-catalog categories`
- `hermes-skill-catalog search <query>`
- `hermes-skill-catalog enable <name> --profile <profile>`
- `hermes-skill-catalog disable <name> --profile <profile>`
- `token-saver stats`
- `token-saver explain "<command>"`
- `hermes-mcp-universe search <query>`
