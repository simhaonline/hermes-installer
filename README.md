# 🌌 Hermes Agent Enterprise Platform & Hybrid Vector Registry

[![Release](https://img.shields.io/badge/release-v1.0.0-blue.svg?style=for-the-badge&logo=github)](https://github.com/simhaonline/hermes-installer/releases/tag/v1.0.0)
[![Curated Skills](https://img.shields.io/badge/curated_skills-19%2C840-success.svg?style=for-the-badge&logo=codementor)](https://github.com/simhaonline/hermes-installer)
[![Community Skills](https://img.shields.io/badge/community_skills-64%2C687-purple.svg?style=for-the-badge&logo=buffer)](https://github.com/simhaonline/hermes-installer)
[![Domain Classifications](https://img.shields.io/badge/skill_domains-56_categories-blueviolet.svg?style=for-the-badge&logo=databricks)](https://github.com/simhaonline/hermes-installer)
[![Specialist Profiles](https://img.shields.io/badge/specialist_profiles-66-orange.svg?style=for-the-badge&logo=probot)](https://github.com/simhaonline/hermes-installer)
[![Agent Personas](https://img.shields.io/badge/agent_personas-554-informational.svg?style=for-the-badge&logo=openai)](https://github.com/simhaonline/hermes-installer)
[![Production MCPs](https://img.shields.io/badge/production_mcps-45_%2F_4%2C842-yellow.svg?style=for-the-badge&logo=fastapi)](https://github.com/simhaonline/hermes-installer)
[![Active Plugins](https://img.shields.io/badge/active_plugins-35-blueviolet.svg?style=for-the-badge&logo=puzzle)](https://github.com/simhaonline/hermes-installer)
[![Precompiled Engines](https://img.shields.io/badge/native_engines-17-red.svg?style=for-the-badge&logo=gnubash)](https://github.com/simhaonline/hermes-installer)
[![Interactive Dashboard](https://img.shields.io/badge/web_ui-port_8998-brightgreen.svg?style=for-the-badge&logo=html5)](http://localhost:8998)
[![Architecture](https://img.shields.io/badge/security-Rootless_Docker_%2B_UID_1001-brightgreen.svg?style=for-the-badge&logo=docker)](https://github.com/simhaonline/hermes-installer)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg?style=for-the-badge)](LICENSE)

An enterprise-grade AI agent platform and hybrid vector ecosystem engineered for high-assurance autonomous workflows. Features **19,840 curated skills** meticulously indexed across **56 operational domains**, **64,687 community packages**, **554 agent personas**, **66 specialist profiles**, **45 production MCP servers** (from an indexed universe of 4,842), **35 active plugins**, and **17 pre-compiled native engines** (AST parsing, 99.2% token context compression, binary reverse engineering, autonomous penetration testing, and holographic AI memory).

Operates with **strict non-root process isolation** (`predictatrade`, `UID=1001`), **Rootless Docker**, an **Interactive Web Dashboard / UI (`0.0.0.0:8998`)**, and a **hybrid dense-sparse vector registry** (SQLite FTS5 + ChromaDB ONNX embeddings) for zero-copy, just-in-time (JIT) skill discovery and execution.

---

## 🏛️ Platform Architecture

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        HERMES ENTERPRISE USER INTERFACES                               │
│   Web Dashboard (Port 8998)    hermes CLI             hermes-registry     hermes-vault │
│   (Visual Search & 1-Click)    (Interactive Agent)    (Dense/Sparse JIT)  (FTS5 SQLite)│
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        HYBRID DENSE-SPARSE KNOWLEDGE VAULT                             │
│  ┌────────────────────────────────────────────────┐  ┌───────────────────────────────┐ │
│  │   Master SQLite FTS5 Database (305 MB)         │  │  ChromaDB Dense Vectors (71MB)│ │
│  │   • 19,840 Curated Skills (Full Text Markdown) │  │  • all-MiniLM-L6-v2 Embeddings│ │
│  │   • 64,687 Community Skill Package Pool        │  │  • Cosine Similarity Search   │ │
│  │   • 554 Personas & 66 Specialist Profiles      │  │  • Instant Intent Resolution  │ │
│  │   • BM25 Porter Stemmer Full-Text Indexes      │  │  • Zero External API Calls    │ │
│  └────────────────────────────────────────────────┘  └───────────────────────────────┘ │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        17 PRE-COMPILED NATIVE ENGINES                                  │
│   CodeGraph (AST)   •  MCPToon (99.2% Token Compression)  •  MemPalace (AAAK Memory)   │
│   REA (Reverse Eng) •  Trim-1 (Line Trimmer)              •  PentAGI (Auto Pentest)    │
│   AutoAgent (Swarm) •  Cactus (Edge Kernels)              •  MiroFish (Simulation)     │
│   NVIDIA OpenShell  •  Laya (Notification Command Ctr)    •  6x Localization Suites    │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        SECURITY & ISOLATION RUNTIME                                    │
│   • Dedicated User: predictatrade (UID=1001, GID=1001)                                 │
│   • Rootless Docker Daemon: unix:///run/user/1001/docker.sock                          │
│   • Strict AppArmor Profiles, cgroup v2, & Non-Privileged Host Execution               │
│   • Automatic Privilege Dropping from Root to predictatrade on all CLI tools           │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🖥️ Interactive Web Dashboard & UI (`hermes-registry`)

Hermes includes a built-in, zero-dependency **Interactive Web Dashboard** served on port `8998` via `hermes-registry.service`:

```text
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│  🌌 HERMES HYBRID VECTOR REGISTRY                                  [Port 8998: ACTIVE]   │
│  [ 🔎 Search across 19,840 Skills, 554 Personas, 45 MCPs... ] [ Filter: 56 Domains ▼ ]   │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│  📊 19,840 Curated Skills  •  64,687 Community Pool  •  66 Profiles  •  35 Plugins       │
├────────────────────────────────────────┬─────────────────────────────────────────────────┤
│  CATEGORIES & DOMAINS                  │  SKILL DETAILS & JIT ACTIONS                    │
│  ► Foundation Systems (13,748)         │  Name: web3-audit                               │
│  ► MiniMax Audio & Voice (1,292)       │  Category: security-audit                       │
│  ► Laravel & PHP Ecosystem (810)       │  Vector Similarity: 0.942 [Dense ChromaDB]      │
│  ► Quantitative Trading (574)          │  Full Description: Smart contract security      │
│  ► Office, Excel & PDF (383)           │  auditing suite covering reentrancy, oracle     │
│  ► Community Elite (327)               │  manipulation, and liquidation math.            │
│  ► Kimi Suite Long-Context (309)       │  ─────────────────────────────────────────────  │
│  ► SEO & GEO Optimization (262)        │  [ ⚡ Install to Profile ]  [ 📖 View SKILL ]  │
│  ► Manus Autonomous Agent (241)        │  [ 🗑️ Evict from Profile ]  [ 📋 Copy Prompt ] │
│  ► Workbuddy Suite (193)               │                                                 │
│  ► React Ecosystem (18)                │                                                 │
│  ► Agent Teams (46)                    │                                                 │
│  ► Graph Database (1)                  │                                                 │
│  ► OpenAI Plugins (55)                 │                                                 │
└────────────────────────────────────────┴─────────────────────────────────────────────────┘
```

### Dashboard Capabilities
- **🔎 Real-Time Hybrid Search**: Combines semantic vector cosine similarity (ChromaDB) with keyword full-text indexing (SQLite FTS5 BM25) across all 19,840 skills.
- **⚡ 1-Click Dynamic Install & Activate**: Activate any tool into any of the 66 specialist profiles (`orchestrator`, `security-audit`, `metatrader-quant`, etc.) without copying files or bloating workspace directories.
- **🗑️ 1-Click Eviction & Uninstall**: Evict tools from profile context cleanly when tasks complete to prevent token ceiling degradation.
- **📖 Full `SKILL.md` Inspector**: View complete markdown instructions, YAML frontmatter, input/output schemas, and script bindings in a clean modal.
- **👥 Profile & Plugin Explorer**: Audit active tools across all 66 specialist profiles, 45 production MCP servers, and 35 plugins.

### Accessing the Dashboard
- **Web UI URL**: `http://localhost:8998` (or `http://platform.predictatrade.com:8998`)
- **CLI Launcher**: `hermes-registry ui` or `hermes-registry dashboard --port 8998`
- **Systemd Service**: Managed as a resilient background daemon:
  ```bash
  sudo systemctl status hermes-registry.service
  sudo systemctl restart hermes-registry.service
  ```

---

## 📦 Release Downloads (GitHub Release `v1.0.0`)

Download pre-built production bundles directly from [**GitHub Releases v1.0.0**](https://github.com/simhaonline/hermes-installer/releases/tag/v1.0.0):

| Release Asset | Size | SHA-256 Checksum | Description |
|---|---|---|---|
| [**`hermes-content-vault-v1.0.0.tar.gz`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-content-vault-v1.0.0.tar.gz) | **152 MB** | `405779fff528dad17d311e6148d91127d6e571a319ddc4f9b093091166e3873c` | **Option A: Pure Content & Vector Vault (Recommended)**. Lightweight archive containing master SQLite FTS5 database (301 MB uncompressed), ChromaDB vector embeddings (69 MB), collection manifests, `install-hermes-local.sh`, and `hermes-registry` dynamic JIT CLI & Web UI. Zero binary bloat. |
| [**`hermes-vault.sqlite`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-vault.sqlite) | **301 MB** | `d3316c93a4f9164afff005bd83b78715bbe02ebe716015830764b0bb915489a0` | **Master SQLite Knowledge Vault**. Standalone database containing relational tables, FTS5 BM25 search tables, auto-sync triggers, and complete skill markdown text. |
| [**`hermes-agent-production.sh`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-agent-production.sh) | **181 MB** | `38c190fb7711f9f7f7940a3201c829ccc332faf5772e6490db8e919d1fc96860` | Complete host deployment script with embedded runtime binaries, engine launchers, and base configuration. |
| [**`hermes-assets.tar.gz`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-assets.tar.gz) | **134 MB** | `ce989e1e3b81d2e8b5aa640d5c9c874983d6236607162d0504048088e96157da` | Core runtime assets, configuration templates, and manifests. |
| [**`SHA256SUMS.txt`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/SHA256SUMS.txt) | Text | `540 bytes` | Cryptographic integrity checksums for all distribution files. |

---

## 🚀 Quick Start & Installation

### Option 1: 1-Line Automated Install
Deploys user accounts, Rootless Docker, 17 compiled engines, system wrappers, hybrid vector registry, and systemd service on Ubuntu LTS (22.04 / 24.04 / 26.04):

```bash
curl -fsSL https://raw.githubusercontent.com/simhaonline/hermes-installer/main/quick-install.sh | bash
```

### Option 2: Deploy Content Vault on Existing Machine (Option A - 152 MB)
Deploy the complete 19.6k+ skill registry, ChromaDB vectors, and Web UI onto any existing server in seconds:

```bash
# 1. Download and extract lightweight content archive
curl -LO https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-content-vault-v1.0.0.tar.gz
tar -xzf hermes-content-vault-v1.0.0.tar.gz

# 2. Run local installer (automatically configures vault, vectors, wrappers & systemd service)
sudo bash install-hermes-local.sh

# 3. Verify hybrid registry status
hermes-registry stats
```

---

## 🎯 Complete Master Skill Ecosystem: 19,840 Skills Across ALL 56 Domains

The ecosystem contains **19,840 curated, production-ready skills** with full YAML frontmatter, execution instructions, input/output schemas, and script bindings. Every single domain is cataloged below:

| # | Domain Classification | Skill Count | Focus & Core Capabilities | Representative Skills |
|:---:|---|:---:|---|---|
| 1 | **`foundation-skills`** | **13,748** | Complete systems engineering, Linux internals, network defense, CI/CD, cloud architecture, containerization, fullstack patterns, algorithms, API design. | `bash`, `go`, `cpp`, `csharp`, `kubernetes-ops`, `aws-well-architected`, `dockerfile`, `jwt`, `csrf`, `sqli`, `git-advanced`, `linux-hardening` |
| 2 | **`minimax-audio-voice`** | **1,292** | Multi-modal audio synthesis, MiniMax TTS/Music3, podcast production, voiceover, sound design, audio DSP, video synchronization. | `voiceover`, `music-generation`, `sound-synthesis`, `captions`, `video-production`, `podcast-studio`, `audio-video-to-text` |
| 3 | **`laravel-php-ecosystem`** | **810** | Modern PHP 8.3/8.4, Laravel 11/12 architecture, Bagisto e-commerce, Livewire, Eloquent query optimization, Pest testing, Sanctum auth. | `laravel-expert`, `bagisto-code-review`, `eloquent-chunking`, `pest-datasets`, `blade-vue-events`, `saloon-api-sdk` |
| 4 | **`quant-trading`** | **574** | Quantitative analysis, MetaTrader MQL4/MQL5 Expert Advisors, TradingView Pine Script v5, options volatility modeling, DEX arbitrage, risk parity. | `mql5-docs-lookup`, `tradingview-pine-indicators`, `options-volatility`, `pairs-trading`, `backtest-strategy`, `risk-engine` |
| 5 | **`office-excel-pdf`** | **383** | Enterprise spreadsheet automation, Excel-DNA C# UDFs, DCF valuation, WeasyPrint PDF layout, ComPDFKit OCR, DOCX parsing, table extraction. | `excel-dna-addins`, `excel-dcf-modeler`, `compdf-ocr`, `pdf-merge-split`, `table-extractor`, `docx-generator`, `sheetsmith` |
| 6 | **`community-elite`** | **327** | Strict linting, high-assurance development patterns, AST transformation, static code quality enforcement. | `anyesh-bad-python`, `code-quality-reviewer`, `python-patterns`, `refactoring-catalog` |
| 7 | **`kimi-suite`** | **309** | Ultra-long context reasoning, recursive multi-document synthesis, Kimi Code CLI tools, problem decomposition, citation verification. | `gen-docs`, `tests`, `latex`, `pull-request`, `mocking`, `dcf_skill`, `report-qa`, `benchmarks` |
| 8 | **`seo-growth-marketing`** | **262** | Generative Engine Optimization (GEO), AI search visibility (Perplexity/ChatGPT), programmatic SEO, keyword clusters, technical SEO audits. | `seo-aeo-geo`, `seo-technical-audit`, `seo-content-cluster`, `geo-platform-optimizer`, `citation-verification`, `serp-overlap` |
| 9 | **`manus-agent`** | **241** | Autonomous web execution, multi-query exploratory research, stealth browser automation, structured citation synthesis. | `workflows`, `reference`, `platforms`, `yahoo-api`, `deep-research`, `browser-pilot` |
| 10 | **`workbuddy-suite`** | **193** | Enterprise corporate productivity, calendar defragmentation, executive brief synthesis, automated document triage. | `workbuddy-agent-briefings`, `kb-lint`, `tracing`, `value`, `cowork-rfp-response`, `cowork-deal-room` |
| 11 | **`official-optional`** | **152** | Vendor-specific integrations, official cloud SDK bindings, infrastructure orchestration across hyperscalers. | `aws-modules`, `azure-common-patterns`, `gcp-cloud-functions`, `docker-compose-creator` |
| 12 | **`backend-languages`** | **135** | High-performance backend engineering across Go, Rust, Java, C#, C++, Python, TypeScript. | `golang-pro`, `rust-async-patterns`, `spring-boot-engineer`, `dotnet-backend-patterns` |
| 13 | **`ui-ux-design`** | **127** | Figma Code Connect, design token systems, Radix UI, Tailwind CSS, micro-interactions, WCAG accessibility, typography hierarchy. | `figma-code-connect`, `tailwind-best-practices`, `framer-motion`, `design-tokens-sync`, `color-palette-extractor` |
| 14 | **`mathematics-ai`** | **116** | Mathematical theorem proving, Lean/Coq formalization, LaTeX paper reading, symbolic derivation, AI4Math research workflows. | `ai4math-paper-reading`, `latex-paper-conversion`, `graph-theory-researcher`, `sympy`, `scipy-optimization` |
| 15 | **`tencent-cloud-ecosystem`** | **103** | Serverless Tencent CloudBase (TCB), TRTC real-time communications, Tencent Maps WebGL, WeChat Mini-Programs. | `cloudbase-agent`, `trtc-sdk`, `tencentmap-jsapi-gl`, `wechat-miniprogram`, `wechatpay-basic` |
| 16 | **`knowledge-graph`** | **92** | Graph RAG, Neo4j / FalkorDB Cypher queries, ontology modeling, semantic link prediction, Memstack graph stores. | `knowledge-graph-neo4j`, `lightrag`, `cypher-query-builder`, `ontology-mapper`, `mempalace` |
| 17 | **`predictatrade`** | **76** | Quant algorithmic models, live broker execution, order routing, and market risk calculators. | `pat-calibration-rebuild`, `pat-delivery-guards`, `pat-monitoring-deck` |
| 18 | **`openai-plugins`** | **55** | Converted OpenAI ChatGPT plugin manifests, GPT Actions, OpenAPI tool definitions, and procedural workflows. | `zapier-ai-actions`, `wolfram-alpha`, `speak`, `klarna-shopping`, `expedia` |
| 19 | **`omnichannel-messaging`** | **47** | Discord bots, Telegram mini-apps, WhatsApp Wassenger automation, Slack event listeners, Gmail pipelines. | `discord-bot-architect`, `telegram-mini-app-skill`, `whatsapp-cloud-api`, `slack-workflows`, `laya` |
| 20 | **`agent-teams`** | **46** | Autonomous multi-agent coordination, swarm architectures, Kanban delegation, AionUi, Takt, and OneManCompany workflows. | `aionui-agent`, `team-collaboration`, `autoagent-orchestration`, `kanban-task-coordination` |
| 21 | **`databases-timeseries`** | **45** | High-throughput time-series databases, QuestDB ingestion, TimescaleDB hypertables, ClickHouse analytics, Redis pub/sub. | `questdb-tsbs-benchmark`, `timescaledb-hyperfunctions`, `clickhouse-io`, `redis-semantic-cache` |
| 22 | **`astro-web-framework`** | **43** | Astro 4/5 development, content collections, edge middleware, islands architecture, hybrid SSR/SSG rendering. | `astro-content-collections`, `astro-ssr-rule`, `astro-edge-middleware-scope`, `astro-images-rule` |
| 23 | **`nginx-caddy-infrastructure`** | **35** | High-performance reverse proxies, Nginx load balancing, Caddy Zero-Trust TLS, rate limiting, DDoS mitigation. | `nginx-hardening`, `caddy-security`, `ssl-tls-management`, `reverse-proxy` |
| 24 | **`security-audit`** | **33** | Penetration testing, OWASP ASVS verification, smart contract auditing, IAM role least-privilege, threat modeling. | `owasp-asvs`, `smart-contract-formal-verification`, `iam-policy-reviewer`, `threat-model-creator`, `audit-reentrancy` |
| 25 | **`translation-localization`** | **33** | Multi-agent neural translation, terminology verification, RTL layouts, bilingual book translation, continuous PO/JSON sync. | `translation-localization`, `terminology-checker`, `bilingual-aligner`, `rtl-layout-validator` |
| 26 | **`web-scraping`** | **31** | Anti-bot bypass, stealth headless browsers, Scrapling DOM parsing, Scrapfly proxy pools, Apify actors. | `scrapling-crawler`, `playwright-interactive`, `stealth-browser`, `anti-bot-scraping`, `hasdata-cli` |
| 27 | **`workflow-automation`** | **31** | n8n workflow construction, Temporal distributed workflows, Airflow DAG generation, background job queues. | `n8n-workflow-patterns`, `temporal-golang-pro`, `airflow-dag-generator`, `bullmq-specialist` |
| 28 | **`safe-agent-runtime`** | **30** | NVIDIA OpenShell sandboxing, policy enforcement, container network firewalls, token consumption governors. | `openshell-policy-advisor`, `token-efficiency-optimizer`, `audit-integrity-gate`, `openshell-cli` |
| 29 | **`enterprise-data-cloud`** | **25** | Cloud data warehouses, Microsoft Fabric Lakehouse, Snowflake RBAC, BigQuery ML, Databricks Unity Catalog. | `microsoft-fabric`, `snowflake-governance-coverage`, `bigquery-view-generator`, `databricks-bundle` |
| 30 | **`react-ecosystem`** | **18** | Modern React 19 concurrent patterns, hooks, RSC, state machines, Pure React components, and performance profiling. | `react-compiler`, `react19-concurrent-patterns`, `react19-actions`, `react-ui-patterns` |
| 31 | **`chart-visualization`** | **13** | AntV G2/G6 infographics, Apache ECharts, ApexCharts, GPT-Vis dynamic SVG chart generation. | `antv-g2-chart`, `antv-g6-graph`, `antv-infographic`, `antv-x6-editor`, `apexcharts-skill`, `lime-echart` |
| 32 | **`context-optimization`** | **10** | Context window compression, TOON serialization, prompt trimming, AST surgical extraction. | `mcptoon`, `mcptoon-cli`, `mcptoon-triage`, `mcptoon-connect` |
| 33 | **`enterprise-operations`** | **10** | Autonomous browser tasks, proxy configuration, Crawlee scrapers, and enterprise search APIs. | `browser-skill`, `crawlee-scraper-skill`, `proxy-config-skill`, `serper-search-skill`, `brave-search-skill` |
| 34 | **`qwen-suite`** | **9** | Alibaba Qwen Code skills, Qwen-Agent multi-turn reasoning, tool calling, and multimodal enhancements. | `qwen-agent`, `qwen-image-enhance`, `qwen-coding-standards` |
| 35 | **`skill-forge`** | **9** | Skill development tooling, Conda-Forge recipes, Pydantic Evals, Ratler build, Typst typesetting. | `conda-forge`, `pydantic-evals`, `rattler-build`, `typst`, `sqlalchemy`, `textual` |
| 36 | **`claude-skills`** | **6** | Anthropic Claude Code plugins and skill adapters extracted from official and community sources. | `claude-code-guide`, `claude-code-sessions`, `claude-code-expert`, `claude-design` |
| 37 | **`skill-tutorials`** | **6** | Documentation frameworks, Fumadocs i18n sync, philosophical illustration, skill article publishing. | `fumadocs-i18n`, `fumadocs-article-importer`, `philosophical-illustrator`, `skill-article-publisher` |
| 38 | **`token-saving`** | **6** | Ultra-fast token trimming, progressive disclosure, prompt budget governance, and context pruning. | `trim-1`, `token-efficiency-optimizer`, `token-saver`, `token-saver-config` |
| 39 | **`autonomous-ai-agents`** | **5** | Autonomous agent frameworks, recursive self-improvement loops, plan execution monitors. | `autoagent`, `goal-loop`, `agentic-verifier` |
| 40 | **`glm-suite`** | **5** | Zhipu AI GLM multi-modal agents, image generation, paper research, and code assistants. | `glm-image-gen`, `glm-researcher`, `glm-code-reviewer` |
| 41 | **`graph-database`** | **1** | Graph data architecture, Omnigraph graph database integration, relational-to-graph mapping. | `omnigraph`, `cypher-query-builder`, `graph-schema-design` |
| 42 | **`custom`** | **352** | Custom enterprise automations, internal workflows, and domain-specific agent playbooks. | `custom-workflow`, `custom-pipeline`, `internal-tools` |
| - | **Other Domains (14 Categories)** | **38** | Micro-specialist categories across AI governance, computer vision, executive operations, and legal. | `ai-governance`, `deep-learning-nlp`, `finance-investment-ops` |
| - | **Community Skill Pool** | **64,687** | Massive indexed database of developer tools, CLI utilities, and community skill packages. | *Full pool indexed in `community_skills` with BM25 FTS5* |

---

## 🔄 Multi-Provider GitHub Scraper & Harvester (`agentskills.io` Spec)

Hermes includes a production-grade, zero-dependency Python 3.11+ scraper (`scraper.py`) and conversion module (`converter.py`) designed to discover, extract, normalize, and integrate AI skills, MCP servers, and plugin manifests across public AI providers:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               MULTI-PROVIDER REPOSITORY SCRAPER & CONVERTER (agentskills.io)           │
│                                                                                        │
│   OpenAI        Anthropic       Moonshot       Manus        Zhipu      React    Omnigraph│
│   (ChatGPT)     (Claude Code)   (Kimi CLI)     (OpenManus)  (GLM)      Vercel   Teams    │
│   ai-plugin     .claude-plugin  kimi-skills    skills/      SKILL.md   skills/  agent/   │
└───────┬─────────────┬──────────────┬──────────────┬───────────┬──────────┬─────────┬───┘
        │             │              │              │           │          │         │
        ▼             ▼              ▼              ▼           ▼          ▼         ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ARTEFACT NORMALIZATION & CONVERTER (converter.py)               │
│   • agentskills.io Frontmatter: name (<=64 chars, a-z0-9-), description (<=1024 chars) │
│   • Mandatory Actionable Sections: ## When to Use, ## Procedure, ## Pitfalls, ## Verify│
│   • Multi-Table Conversion: Skills, Agent Personas, MCP Servers, and Plugin Manifests  │
│   • Provider Metadata Preservation: metadata.hermes (category, provider, license, repo)│
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        HYBRID VAULT & VECTOR REGISTRY INGESTION                        │
│   • Disk Sync        : /srv/hermes-installer/harvested-skills/ & ~/.hermes/skill-library│
│   • SQLite FTS5 Vault: hermes-vault.sqlite (curated_skills, agent_personas, mcp_servers)│
│   • ChromaDB Vectors : vector-registry/ (skills_semantic, agents_semantic, mcp_semantic)│
│   • Instant JIT Exec : hermes-registry resolve "<intent>" -> hermes-registry activate │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Supported Provider Formats
- **OpenAI Plugins & Actions (`ai-plugin.json`)**: Converts OpenAI plugin manifests and OpenAPI endpoints into procedural, step-by-step Hermes execution instructions.
- **Anthropic Claude Code (`.claude-plugin/plugin.json`, `skills/`)**: Extracts nested skills, tool calls, and agent definitions into standalone agentskills.io format.
- **Moonshot Kimi (`kimi-skills`, `kimi-cli`)**: Normalizes long-context reasoning tools, LaTeX parsers, and financial valuation modules.
- **Manus & OpenManus (`ai-manus`, `OpenManus`)**: Extracts autonomous web navigation, stealth browser control, and research workflows.
- **Zhipu GLM (`GLM-skills`)**: Integrates multi-modal generation and visual agent skills.
- **Tencent CloudBase (`TencentCloudBase/skills`)**: Ingests serverless TCB APIs, TRTC real-time tools, and WeChat mini-program modules.
- **Alibaba Qwen (`qwen-agent`, `agent-skills`)**: Converts multi-agent reasoning, coding tools, and visual enhancers.
- **React Ecosystem (`full-stack-skills/react-skills`, `pure-react-ui-components-skills`)**: Harvests React 19 patterns, concurrent features, hooks, and UI component skills.
- **Vercel Agent Skills (`vercel-labs/agent-skills`)**: Ingests Vercel AI SDK patterns, streaming execution, and edge functions.
- **Agent Teams (`iOfficeAI/AionUi`, `nrslib/takt`, `1mancompany/OneManCompany`)**: Multi-agent team collaboration, swarm orchestration, and Kanban task coordination.
- **Omnigraph Graph DB (`ModernRelay/omnigraph`)**: Graph-based data models, schema mapping, and Cypher query execution.
- **Cross-Provider Repositories**: Scrapes `sickn33/agentic-awesome-skills`, `vivy-yi/awesome-skills`, and `mcp-manifest/mcp-manifest-spec`.

### Production Hardening & Rate-Limit Management
- **Automatic Token Discovery**: Automatically extracts GitHub Personal Access Tokens from `GITHUB_TOKEN`, `GH_TOKEN`, or local git credentials (`/root/.git-credentials`) for up to 5,000 requests/hour.
- **Recursive Git Trees API**: Fetches entire repository directory structures in a single HTTP request (`/git/trees/{branch}?recursive=1`), bypassing per-file API limits.
- **HTTP ETag Conditional Requests**: Stores response ETags in `.cache/github_scraper/` so subsequent runs on unchanged repositories consume 0 rate limit tokens.
- **Open-Source License Auditing**: Inspects repository licenses (MIT, Apache-2.0, BSD, GPL, etc.) and skips repositories without explicit open-source authorization.

### Harvester CLI Usage
```bash
# 1. Run unit test suite for converter and scraper (14 passing tests)
python3 -m unittest test_converter.py test_scraper.py -v

# 2. Harvest specific repos or topics and ingest non-destructively
python3 scraper.py --sources \
  https://github.com/full-stack-skills/react-skills \
  https://github.com/topics/pure-react-skills \
  https://github.com/vercel-labs/agent-skills \
  https://github.com/topics/agent-team \
  https://github.com/ModernRelay/omnigraph \
  --ingest

# 3. Scrape curated seeds and convert to agentskills.io format
python3 scraper.py --seeds-only --limit-artifacts 10

# 4. Resolve and activate a freshly harvested skill
hermes-registry resolve "react compiler optimization"
hermes-registry activate react-compiler --profile default
```

---

## 👥 66 Specialist Agent Profiles

Hermes provides **66 pre-configured specialist profiles** located in `~/.hermes/profiles/`. Switch execution context instantly with `hermes -p <profile>`:

```text
ORCHESTRATION & SYSTEMS             CYBERSECURITY (MULTI-TEAM)            QUANT & ALGORITHMIC TRADING
├── orchestrator                    ├── security-audit                   ├── metatrader-quant
├── coding-engineer                 ├── red-team                         ├── tradingview-quant
├── backend-architect               ├── blue-team                        ├── pat-operations
├── frontend-developer              ├── purple-team                      ├── quant-analyst
├── fullstack-guardian              ├── white-team                       ├── finance-investment-ops
├── devops-deploy                   ├── orange-team                      ├── analytics-finance
├── qa-testing                      ├── yellow-team                      └── crypto-bd-agent
├── system-architect                ├── green-team
├── cloud-infrastructure            └── ethical-hacking-pentest
└── code-reviewer

AI, ML & COMPUTER VISION            SEARCH, SEO & MARKETING              ENTERPRISE & LEGAL
├── deep-learning-researcher        ├── geo-search-specialist            ├── legal-clm-specialist
├── mlops-platform-engineer         ├── seo-growth-marketer              ├── legal-corporate
├── computer-vision-engineer        ├── agentic-search-optimizer         ├── ai-governance-officer
├── mathematics-ai                  ├── social-media-strategist          ├── executive-c-suite-advisor
├── research-science                ├── marketing-growth                 ├── hr-talent-operations
├── multi-agent-architect           ├── content-marketer                 ├── supply-chain-architect
└── ai-research-mlops               └── gtm-sales-engineer               ├── product-manager
                                                                         ├── business-operations
                                                                         └── fact-checking-analyst

ECOSYSTEM & FRAMEWORK SPECIALISTS
├── minimax-voice-agent (TTS/Audio)  ├── astro-web-architect (Astro 5)    ├── token-optimizer (Context Budget)
├── kimi-reasoning-specialist (Docs) ├── nginx-caddy-infrastructure (Ops) ├── mcp-librarian (MCP Universe)
├── manus-autonomous-agent (Web)     ├── web-scraping-specialist (DOM)    ├── skill-librarian (Skill Catalog)
├── workbuddy-enterprise (Desktop)   ├── knowledge-graph-architect (Neo4j)├── foundation-agent (Core Systems)
├── tencent-cloud-architect (Cloud)  ├── office-excel-pdf (Financials)    ├── documents-office (Document AI)
├── laravel-architect (PHP/Bagisto)  ├── database-optimizer (DBA)         ├── creative-media (Design/Media)
├── fabric-engineer (MS Fabric)      ├── data-knowledge (Lakehouse)       ├── chart-visualization (AntV/Charts)
└── devops-sre (Observability)       └── esoteric-advisor (Specialized)
```

---

## 🔌 45 Curated Production MCP Servers

All **45 production MCP servers** are pre-configured in `recommended-mcp-servers.json` with native command launchers, argument schemas, and environment isolation:

| Category | Server Name | Command | Focus & Capabilities |
|---|---|---|---|
| **Web & Research** | `brave-search` | `npx` | Real-time web index search, news, local POIs. |
| | `manus-research` | `python3` | Multi-hop autonomous crawling and structured synthesis. |
| | `scrapling-crawler` | `python3` | Adaptive anti-bot web crawling and dynamic DOM extraction. |
| | `fetch` | `uvx` | Direct HTTP/HTTPS content extraction and markdown conversion. |
| **Knowledge & Memory**| `mempalace` | `mempalace-mcp` | Local-first AI memory retrieval with AAAK dialect. |
| | `codegraph` | `codegraph` | AST knowledge graph, callers/callees impact traversal. |
| | `knowledge-graph-neo4j` | `npx` | Enterprise Neo4j graph queries and Cypher execution. |
| | `memory` | `npx` | Dynamic entity-relationship graph memory. |
| | `sqlite` | `uvx` | Direct relational SQL operations and table inspection. |
| **Developer Tools** | `git` | `uvx` | Branch inspection, diff review, commit auditing. |
| | `docker` | `uvx` | Container lifecycle, Dockerfile building, volume inspect. |
| | `filesystem` | `npx` | Scoped filesystem read/write operations. |
| | `conda-cli` | `python3` | Python virtual environment isolation and package locking. |
| | `document-specialist-mcp` | `npx` | Structured document parsing, validation, and conversion. |
| **Quant & Financial** | `metatrader5` | `python3` | MT5 broker bridge, live tick data, order execution. |
| | `questdb` | `npx` | Ultra-low latency time-series ingestion and ILP protocol. |
| | `timescaledb` | `node` | Hypertable analytics, continuous aggregates. |
| | `tradingview-signals` | `python3` | Pine Script indicator webhooks and trading alerts. |
| | `redis` | `uvx` | Semantic cache, streaming queue, and pub/sub bus. |
| | `postgres` | `npx` | Enterprise PostgreSQL database queries and migrations. |
| | `mcp-server-excel` | `uvx` | Excel workbook manipulation and C# UDF automation. |
| **Multimodal & Vision**| `roboflow-vision-mcp` | `npx` | Computer vision inference, object detection, segmentation. |
| | `huggingface-mcp` | `uvx` | HuggingFace Hub model discovery and remote inference. |
| | `pi-voice` | `python3` | Low-latency streaming voice conversation. |
| | `compdf-mcp` | `python3` | PDF OCR, page manipulation, text table extraction. |
| **Enterprise Cloud** | `microsoft-fabric` | `npx` | OneLake data lakehouse querying and PowerBI automation. |
| | `caddy-security` | `caddy` | Automatic TLS, reverse proxy, and zero-trust authentication. |
| | `ai-guardrails-mcp` | `python3` | Input/output sanitization and jailbreak defense. |
| | `openfactcheck-mcp`| `python3` | Multi-source claim decomposition and fact verification. |
| | `legal-clm-mcp` | `python3` | Contract redlining, clause risk scoring, and CLM pipelines. |
| | `supplychain-mcp` | `node` | Supply chain telemetry, ERP integration, and logistics optimization. |
| | `gtm-sales-mcp` | `uvx` | B2B pipeline automation, lead enrichment, CRM sync. |
| **Browser & Automation**| `playwright` | `npx` | Full browser automation, end-to-end UI journey testing. |
| | `puppeteer` | `npx` | Chromium headless automation, DOM screenshotting. |
| | `2captcha` | `npx` | Automated CAPTCHA / Cloudflare Turnstile bypass. |
| **Messaging & Ops** | `discord` | `npx` | Discord bot integration, channel management, webhooks. |
| | `telegram-bot` | `npx` | Telegram bot communications and mini-app bridge. |
| | `whatsapp-wassenger` | `npx` | WhatsApp omnichannel messaging and automated replies. |
| | `laya` | `python3` | Centralized notification command center (Slack/Gmail/GitHub). |
| **Workflows & Schedule**| `agent-cron` | `node` | Persistent cron job scheduling for autonomous agents. |
| | `deer-flow` | `python3` | Cyclic graph execution and agentic state-machine workflows. |

---

## 🧩 35 Active Enterprise Plugins

The platform includes **35 production plugins** registered in `~/.hermes/plugins/`:

| Plugin | Version | Focus & Capabilities |
|---|:---:|---|
| **`agent-cron`** | 1.0.0 | Autonomous agent recurring task scheduler and heartbeat monitor. |
| **`autoagent`** | 1.0.0 | Zero-code autonomous LLM agent execution framework. |
| **`cactus`** | 1.0.0 | Low-latency edge inference runtime and quantization kernels. |
| **`codegraph`** | 1.0.0 | AST knowledge graph indexing and callers/callees impact traversal. |
| **`conda-plugins`** | 1.0.0 | Dynamic Python virtual environment manager. |
| **`deer-flow`** | 1.0.0 | Cyclic state-machine agent workflow engine. |
| **`fabric-plugins`**| 1.0.0 | Microsoft Fabric OneLake Lakehouse integration. |
| **`homeassistant`** | 1.0.0 | IoT hardware automation and telemetry ingestion. |
| **`laya`** | 1.0.0 | Central notification command center (Slack, Gmail, Jira, GitHub). |
| **`manus-research`**| 1.0.0 | Multi-query exploratory autonomous research engine. |
| **`mcptoon`** | 1.0.0 | Zero-dependency MCP gateway and 99.2% token context compressor. |
| **`mempalace`** | 1.0.0 | Local holographic AI memory with AAAK dialect. |
| **`memstack`** | 1.0.0 | Hierarchical semantic memory store. |
| **`mirofish`** | 1.0.0 | Multi-agent predictive market simulation engine. |
| **`mql5-libraries`** | 1.0.0 | MetaTrader 5 trading bridge and strategy backtesting libraries. |
| **`open-company`** | 1.0.0 | Autonomous corporate organization and operations manager. |
| **`openshell`** | 1.0.0 | NVIDIA agent sandbox security and policy enforcement runtime. |
| **`pentagi`** | 1.0.0 | Autonomous penetration testing and vulnerability auditing agent. |
| **`quantmind`** | 1.0.0 | Algorithmic trading and portfolio risk management plugin. |
| **`rea`** | 1.0.0 | Binary reverse engineering, disassembly, and decompilation. |
| **`scrapling`** | 1.0.0 | Stealth browser scraping and dynamic DOM parsing plugin. |
| **`superpowers`** | 1.0.0 | Interactive debugging, reasoning boosts, and developer shortcuts. |
| **`token-saver`** | 1.0.0 | Whitespace stripper, payload compressor, and context ceiling guard. |
| **`tradingview-pinescript`** | 1.0.0 | TradingView Pine Script v5 code generator and strategy auditor. |
| **`trim-1`** | 1.0.0 | Compiled Go context trimmer for prompt-relevant lines extraction. |
| **`wookstar-plugins`**| 1.0.0 | Extended developer automation and tool integrations. |
| **`geo-optimizer`** | 1.0.0 | Generative Engine Optimization audit, JSON-LD knowledge graph generator. |
| **`gtm-engine`** | 1.0.0 | B2B outbound pipeline acceleration and lead scoring. |
| **`ai-governance`** | 1.0.0 | EU AI Act & NIST AI RMF compliance auditor and prompt-injection defense. |
| **`openfactcheck`** | 1.0.0 | Automated claim decomposition and multi-source evidence verification. |
| **`agentic-flow`** | 1.0.0 | Multi-agent swarm coordination and hierarchical delegation engine. |
| **`contract-lifecycle`** | 1.0.0 | Intelligent contract analysis, clause risk scoring, and auto-redlining. |
| **`react-skills`** | 1.0.0 | React 19 UI component development, hooks inspection, and performance auditing. |
| **`kanban`** | 1.0.0 | Multi-agent task coordination, visual board state, and handoff tracking. |
| **`timeline`** | 1.0.0 | Chronological agent activity timeline, event tracing, and execution audit. |

---

## ⚡ 17 Pre-compiled Native Engines

All **17 engines** are pre-compiled and installed in `/usr/local/bin` with automatic privilege dropping to `predictatrade` (`UID=1001`):

| # | Engine | Technology | CLI / Command | Capabilities |
|---|---|---|---|---|
| 1 | **MCPToon** | Python / Native | `mcptoon` | Zero-dependency MCP gateway & 99.2% token context compression CLI. |
| 2 | **CodeGraph** | TypeScript / WASM | `codegraph` | AST knowledge graph, callers/callees impact traversal, surgical context extraction. |
| 3 | **MemPalace** | Python / ChromaDB | `mempalace` | Local-first holographic AI memory system with AAAK dialect and zero API cost. |
| 4 | **REA** | Node.js / CLI | `rea`, `rea-agents` | Binary reverse engineering, static analysis, decompilation (ELF, Mach-O, PE). |
| 5 | **Trim-1** | Go Binary | `trim`, `trim-1` | Ultra-fast compiled context trimmer for extracting prompt-relevant lines from code. |
| 6 | **PentAGI** | Go Binary | `pentagi` | Autonomous penetration testing and security auditing agent framework. |
| 7 | **AutoAgent** | Python / CLI | `auto` | Zero-code autonomous LLM agent execution framework. |
| 8 | **MiroFish** | Python / Plugin | `plugins/mirofish` | Swarm intelligence and predictive multi-agent simulation engine. |
| 9 | **NVIDIA OpenShell** | Rust / Python | `openshell` | Sandboxed policy enforcement and private agent execution runtime. |
| 10 | **Cactus Compute** | Python / C++ | `cactus` | Low-latency edge inference runtime and quantization kernels. |
| 11 | **Laya** | Python / MCP | `laya` | Local-first AI notification command center (Slack, Gmail, GitHub, Jira). |
| 12-17| **Localization Suites** | Markdown / Code | `skill-library/` | Product localization (23 skills), multi-agent translation with terminology verification, translation file sync, book translation, and skills curriculum. |

---

## 🔍 CLI Commands & Developer Query Reference

### 1. `hermes-registry` (Hybrid Vector Search & JIT Management)
```bash
# Launch interactive Web Dashboard on port 8998
hermes-registry ui

# View combined relational (SQLite) and vector (ChromaDB) statistics
hermes-registry stats

# Natural language intent resolution (ChromaDB Cosine + SQLite FTS5 BM25)
hermes-registry resolve "audit smart contract reentrancy and token bonding curves"

# Dynamically install/activate a skill into profile context (aliases: activate / install)
hermes-registry install web3-audit --profile security-audit

# Evict the tool cleanly when the task finishes to preserve token ceilings
hermes-registry uninstall web3-audit --profile security-audit

# List all active skills for a specific profile
hermes-registry list --profile metatrader-quant
```

### 2. `hermes-vault` (Master SQLite FTS5 CLI)
```bash
# View ecosystem counts and database health
hermes-vault stats

# Search curated skills by keyword or category
hermes-vault skills quant
hermes-vault skills --category seo-growth-marketing

# Search the 64,687 community skill pool
hermes-vault community "fact-check"

# Search 480 agent personas
hermes-vault agents "computer vision"

# List recommended production MCP servers
hermes-vault mcp --recommended

# Inspect pre-compiled native engines
hermes-vault engines
```

### 3. Direct SQLite Database Queries
```bash
# Query curated skills by category
sqlite3 /home/predictatrade/.hermes/hermes-vault.sqlite \
  "SELECT category, count(*) FROM curated_skills GROUP BY category ORDER BY count(*) DESC;"

# Query recommended production MCP servers
sqlite3 /home/predictatrade/.hermes/hermes-vault.sqlite \
  "SELECT server_name, command FROM mcp_servers WHERE is_recommended=1;"

# Search agent personas by role
sqlite3 /home/predictatrade/.hermes/hermes-vault.sqlite \
  "SELECT name, division FROM agent_personas WHERE name LIKE '%quant%';"
```

---

## 🛡️ Enterprise Security & Process Isolation

1. **Non-Root Execution**:
   Hermes executes strictly as the dedicated non-root service account `predictatrade` (`UID=1001`, `GID=1001`). The account is excluded from `sudo` and privileged groups.
2. **Rootless Docker Daemon**:
   Containers execute through `unix:///run/user/1001/docker.sock` in unprivileged user namespaces. Platform host Docker (`/var/run/docker.sock`) remains strictly reserved for system infrastructure.
3. **Automatic Privilege Dropping**:
   All CLI wrappers in `/usr/local/bin` (`hermes`, `hermes-registry`, `hermes-vault`, `codegraph`, `mcptoon`, `trim`, `mempalace`, `rea`, `auto`, `pentagi`) automatically drop privileges from `root` to `predictatrade` using `runuser -u predictatrade`.
4. **Zero API Key Leakage**:
   Secrets reside strictly in `/home/predictatrade/.hermes/.env` (mode `0600`). Never hardcode API keys in repository files or commit histories.

---

## 📚 Master Documentation & Runbooks

- [**`README-HERMES.md`**](README-HERMES.md) — Comprehensive technical manual (architecture, engine benchmarks, profile configurations).
- [**`README-LOCAL-INSTALL.md`**](README-LOCAL-INSTALL.md) — Enterprise deployment runbook, air-gapped installation, and SQLite schema reference.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
