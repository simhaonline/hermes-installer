# 🌌 Hermes Agent Enterprise Platform & Hybrid Vector Registry

[![Release](https://img.shields.io/badge/release-v1.0.0-blue.svg?style=for-the-badge&logo=github)](https://github.com/simhaonline/hermes-installer/releases/tag/v1.0.0)
[![Curated Skills](https://img.shields.io/badge/curated_skills-19%2C691-success.svg?style=for-the-badge&logo=codementor)](https://github.com/simhaonline/hermes-installer)
[![Community Skills](https://img.shields.io/badge/community_skills-64%2C687-purple.svg?style=for-the-badge&logo=buffer)](https://github.com/simhaonline/hermes-installer)
[![Specialist Profiles](https://img.shields.io/badge/specialist_profiles-66-orange.svg?style=for-the-badge&logo=probot)](https://github.com/simhaonline/hermes-installer)
[![Agent Personas](https://img.shields.io/badge/agent_personas-480-informational.svg?style=for-the-badge&logo=openai)](https://github.com/simhaonline/hermes-installer)
[![Production MCPs](https://img.shields.io/badge/production_mcps-45_%2F_4%2C837-yellow.svg?style=for-the-badge&logo=fastapi)](https://github.com/simhaonline/hermes-installer)
[![Active Plugins](https://img.shields.io/badge/active_plugins-32-blueviolet.svg?style=for-the-badge&logo=puzzle)](https://github.com/simhaonline/hermes-installer)
[![Precompiled Engines](https://img.shields.io/badge/native_engines-17-red.svg?style=for-the-badge&logo=gnubash)](https://github.com/simhaonline/hermes-installer)
[![Architecture](https://img.shields.io/badge/security-Rootless_Docker_%2B_UID_1001-brightgreen.svg?style=for-the-badge&logo=docker)](https://github.com/simhaonline/hermes-installer)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg?style=for-the-badge)](LICENSE)

An enterprise-grade, production-hardened AI agent platform and hybrid vector ecosystem. Features **19,691 curated skills** across **48 operational domains**, **64,687 community packages**, **480 agent personas**, **66 specialist profiles**, **45 production MCP servers** (catalog of 4,837), **32 active plugins**, and **17 pre-compiled native engines** (AST parsing, token compression, reverse engineering, penetration testing, and holographic memory).

Operates with **strict non-root process isolation** (`predictatrade`, `UID=1001`), **Rootless Docker**, and a **hybrid dense-sparse vector registry** (SQLite FTS5 + ChromaDB ONNX embeddings) for zero-copy, just-in-time (JIT) skill execution.

---

## 🏛️ Platform Architecture

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        HERMES ENTERPRISE CLI INTERFACE                                  │
│   hermes              hermes-registry          hermes-vault       codegraph / mcptoon  │
│   (Interactive Agent) (Dense + Sparse Search)  (FTS5 Database)    (AST / Token Trimmer)│
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        HYBRID VECTOR KNOWLEDGE VAULT                                   │
│  ┌────────────────────────────────────────────────┐  ┌───────────────────────────────┐ │
│  │   Master SQLite FTS5 Database (301 MB)        │  │  ChromaDB Dense Vectors (69MB)│ │
│  │   • 19,691 Curated Skills (Full Markdown Text) │  │  • all-MiniLM-L6-v2 Embeddings│ │
│  │   • 64,687 Community Skill Pool               │  │  • Cosine Similarity Search   │ │
│  │   • 480 Personas & 66 Specialist Profiles      │  │  • Instant Intent Resolution  │ │
│  │   • BM25 Porter Stemmer Full-Text Indexes     │  │  • Zero External API Costs     │ │
│  └────────────────────────────────────────────────┘  └───────────────────────────────┘ │
└───────────────────────────────────────────┬────────────────────────────────────────────┘
                                            │
                                            ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        17 PRE-COMPILED NATIVE ENGINES                                  │
│   CodeGraph (AST)   •  MCPToon (99.2% Token Compression)  •  MemPalace (AAAK Memory)   │
│   REA (Reverse Eng) •  Trim-1 (Line Trimmer)             •  PentAGI (Auto Pentest)    │
│   AutoAgent (Swarm) •  Cactus (Edge Kernels)             •  MiroFish (Simulation)     │
│   NVIDIA OpenShell  •  Laya (Notification Command Ctr)   •  6x Localization Suites    │
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

## 📦 Release Downloads (GitHub Release `v1.0.0`)

Download pre-built production bundles directly from [**GitHub Releases v1.0.0**](https://github.com/simhaonline/hermes-installer/releases/tag/v1.0.0):

| Release Asset | Size | SHA-256 Checksum | Description |
|---|---|---|---|
| [**`hermes-content-vault-v1.0.0.tar.gz`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-content-vault-v1.0.0.tar.gz) | **152 MB** | `c8ec51542c3245acbaab979de9815b930a74f09f869a6a256b956d43caf43b40` | **Option A: Pure Content & Vector Vault (Recommended)**. Lightweight archive containing master SQLite FTS5 database (301 MB uncompressed), ChromaDB vector embeddings (69 MB), collection manifests, `install-hermes-local.sh`, and `hermes-registry` dynamic JIT CLI & Web UI. Zero binary bloat. |
| [**`hermes-vault.sqlite`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-vault.sqlite) | **301 MB** | `d3316c93a4f9164afff005bd83b78715bbe02ebe716015830764b0bb915489a0` | **Master SQLite Knowledge Vault**. Standalone database containing relational tables, FTS5 BM25 search tables, auto-sync triggers, and complete skill text. |
| [**`hermes-agent-production.sh`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-agent-production.sh) | **181 MB** | `38c190fb7711f9f7f7940a3201c829ccc332faf5772e6490db8e919d1fc96860` | Complete host deployment script with embedded runtime binaries, engine launchers, and base configuration. |
| [**`hermes-assets.tar.gz`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-assets.tar.gz) | **134 MB** | `ce989e1e3b81d2e8b5aa640d5c9c874983d6236607162d0504048088e96157da` | Core runtime assets, configuration templates, and manifests. |
| [**`SHA256SUMS.txt`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/SHA256SUMS.txt) | Text | `525 bytes` | Cryptographic integrity checksums for all distribution files. |

---

## 🚀 Quick Start & Installation

### Option 1: Deploy Content Vault on Existing Hermes Machine (Option A)
Unpack the complete 19.6k+ skill registry, vector index, and CLI tools onto any server running Hermes in seconds:

```bash
# 1. Download and extract lightweight content archive
curl -LO https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-content-vault-v1.0.0.tar.gz
tar -xzf hermes-content-vault-v1.0.0.tar.gz

# 2. Inspect hybrid registry stats (relational + ChromaDB vectors)
./hermes-registry stats

# 3. Resolve skills using natural language intent
./hermes-registry resolve "audit smart contract reentrancy and token bonding curves"

# 4. Activate skills on-demand without duplicating files
./hermes-registry activate audit-reentrancy --profile default
```

### Option 2: 1-Line Full Host Automated Install
Deploys user accounts, Rootless Docker, 17 compiled engines, system wrappers, and configuration on Ubuntu LTS (22.04 / 24.04 / 26.04):

```bash
curl -fsSL https://raw.githubusercontent.com/simhaonline/hermes-installer/main/quick-install.sh | bash
```

---

## 🎯 Curated Skill Ecosystem: 19,691 Skills Across 48 Domains

All **19,691 curated skills** contain full natural language instructions, execution guardrails, script bindings, and input/output contracts.

| Category / Domain | Skill Count | Focus & Core Capabilities | Representative Skills |
|---|:---:|---|---|
| **`foundation-skills`** | **13,748** | Complete system engineering, cloud architectures, Linux internals, network defense, CI/CD pipelines, containerization, fullstack patterns, algorithms, API design. | `bash`, `go`, `cpp`, `csharp`, `kubernetes-ops`, `aws-well-architected`, `dockerfile`, `jwt`, `csrf`, `sqli`, `git-advanced`, `linux-hardening` |
| **`minimax-audio-voice`** | **1,292** | Multi-modal audio synthesis, MiniMax TTS/Music3, podcast production, voiceover, sound design, audio DSP, video synchronization. | `voiceover`, `music-generation`, `sound-synthesis`, `captions`, `video-production`, `podcast-studio`, `audio-video-to-text` |
| **`laravel-php-ecosystem`** | **810** | Modern PHP 8.3/8.4, Laravel 11/12 architecture, Bagisto e-commerce, Livewire, Eloquent query optimization, Pest testing, Sanctum auth. | `laravel-expert`, `bagisto-code-review`, `eloquent-chunking`, `pest-datasets`, `blade-vue-events`, `saloon-api-sdk` |
| **`quant-trading`** | **574** | Quantitative analysis, MetaTrader MQL4/MQL5 Expert Advisors, TradingView Pine Script v5, options volatility modeling, DEX arbitrage, risk parity. | `mql5-docs-lookup`, `tradingview-pine-indicators`, `options-volatility`, `pairs-trading`, `backtest-strategy`, `risk-engine` |
| **`office-excel-pdf`** | **383** | Enterprise spreadsheet automation, Excel-DNA C# UDFs, DCF valuation, WeasyPrint PDF layout, ComPDFKit OCR, DOCX parsing, table extraction. | `excel-dna-addins`, `excel-dcf-modeler`, `compdf-ocr`, `pdf-merge-split`, `table-extractor`, `docx-generator`, `sheetsmith` |
| **`community-elite`** | **321** | Strict linting, high-assurance development patterns, AST transformation, static code quality enforcement. | `anyesh-bad-python`, `code-quality-reviewer`, `python-patterns`, `refactoring-catalog` |
| **`submitted`** | **318** | Peer-reviewed community submissions across specialized scientific and production workflows. | `specialized-testing`, `domain-modeling`, `system-assessment` |
| **`kimi-suite`** | **309** | Ultra-long context reasoning, recursive multi-document synthesis, Kimi Code CLI tools, problem decomposition, citation verification. | `gen-docs`, `tests`, `latex`, `pull-request`, `mocking`, `dcf_skill`, `report-qa`, `benchmarks` |
| **`seo-growth-marketing`** | **262** | Generative Engine Optimization (GEO), AI search visibility (Perplexity/ChatGPT), programmatic SEO, keyword clusters, technical SEO audits. | `seo-aeo-geo`, `seo-technical-audit`, `seo-content-cluster`, `geo-platform-optimizer`, `citation-verification`, `serp-overlap` |
| **`manus-agent`** | **238** | Autonomous web execution, multi-query exploratory research, stealth browser automation, structured citation synthesis. | `workflows`, `reference`, `platforms`, `yahoo-api`, `deep-research`, `browser-pilot` |
| **`workbuddy-suite`** | **193** | Enterprise corporate productivity, calendar defragmentation, executive brief synthesis, automated document triage. | `workbuddy-agent-briefings`, `kb-lint`, `tracing`, `value`, `cowork-rfp-response`, `cowork-deal-room` |
| **`official-optional`** | **152** | Vendor-specific integrations, official SDK bindings, cloud provider orchestration. | `aws-modules`, `azure-common-patterns`, `gcp-cloud-functions` |
| **`backend-languages`** | **135** | High-performance backend engineering across Go, Rust, Java, C#, C++, Python, TypeScript. | `golang-pro`, `rust-async-patterns`, `spring-boot-engineer`, `dotnet-backend-patterns` |
| **`ui-ux-design`** | **127** | Figma Code Connect, design token systems, Radix UI, Tailwind CSS, micro-interactions, WCAG accessibility, typography hierarchy. | `figma-code-connect`, `tailwind-best-practices`, `framer-motion`, `design-tokens-sync`, `color-palette-extractor` |
| **`mathematics-ai`** | **116** | Mathematical theorem proving, Lean/Coq formalization, LaTeX paper reading, symbolic derivation, AI4Math research workflows. | `ai4math-paper-reading`, `latex-paper-conversion`, `graph-theory-researcher`, `sympy`, `scipy-optimization` |
| **`tencent-cloud-ecosystem`** | **103** | Serverless Tencent CloudBase (TCB), TRTC real-time communications, Tencent Maps WebGL, WeChat Mini-Programs. | `cloudbase-agent`, `trtc-sdk`, `tencentmap-jsapi-gl`, `wechat-miniprogram`, `wechatpay-basic` |
| **`knowledge-graph`** | **92** | Graph RAG, Neo4j / FalkorDB Cypher queries, ontology modeling, semantic link prediction, Memstack graph stores. | `knowledge-graph-neo4j`, `lightrag`, `cypher-query-builder`, `ontology-mapper` |
| **`predictatrade`** | **76** | Proprietary quantitative infrastructure, MT5 Wine operations, real-time signal reconciliation, broker cost accounting. | `pat-operations`, `pat-monitoring-deck`, `pat-signal-delivery-audit`, `pat-ev-math-accuracy` |
| **`omnichannel-messaging`** | **47** | Discord bots, Telegram mini-apps, WhatsApp Wassenger automation, Slack event listeners, Gmail pipelines. | `discord-bot-architect`, `telegram-mini-app`, `whatsapp-cloud-api`, `slack-workflows` |
| **`databases-timeseries`** | **45** | High-throughput time-series databases, QuestDB ingestion, TimescaleDB hypertables, ClickHouse analytics, Redis pub/sub. | `questdb-tsbs-benchmark`, `timescaledb-hyperfunctions`, `clickhouse-io`, `redis-semantic-cache` |
| **`astro-web-framework`** | **43** | Astro 4/5 development, content collections, edge middleware, islands architecture, hybrid SSR/SSG rendering. | `astro-content-collections`, `astro-ssr-rule`, `astro-edge-middleware-scope`, `astro-images-rule` |
| **`nginx-caddy-infrastructure`** | **35** | High-performance reverse proxies, Nginx load balancing, Caddy Zero-Trust TLS, rate limiting, DDoS mitigation. | `nginx-hardening`, `caddy-security`, `ssl-tls-management`, `reverse-proxy` |
| **`security-audit`** | **33** | Penetration testing, OWASP ASVS verification, smart contract auditing, IAM role least-privilege, threat modeling. | `owasp-asvs`, `smart-contract-formal-verification`, `iam-policy-reviewer`, `threat-model-creator` |
| **`translation-localization`** | **33** | Multi-agent neural translation, terminology verification, RTL layouts, bilingual book translation, continuous PO/JSON sync. | `translation-localization`, `terminology-checker`, `bilingual-aligner`, `rtl-layout-validator` |
| **`web-scraping`** | **31** | Anti-bot bypass, stealth headless browsers, Scrapling DOM parsing, Scrapfly proxy pools, Apify actors. | `scrapling-crawler`, `playwright-interactive`, `stealth-browser`, `anti-bot-scraping` |
| **`workflow-automation`** | **31** | n8n workflow construction, Temporal distributed workflows, Airflow DAG generation, background job queues. | `n8n-workflow-patterns`, `temporal-golang-pro`, `airflow-dag-generator`, `bullmq-specialist` |
| **`safe-agent-runtime`** | **30** | NVIDIA OpenShell sandboxing, policy enforcement, container network firewalls, token consumption governors. | `openshell-policy-advisor`, `token-efficiency-optimizer`, `audit-integrity-gate` |
| **`enterprise-data-cloud`** | **25** | Cloud data warehouses, Microsoft Fabric Lakehouse, Snowflake RBAC, BigQuery ML, Databricks Unity Catalog. | `microsoft-fabric`, `snowflake-governance-coverage`, `bigquery-view-generator`, `databricks-bundle` |
| **Specialized Niches (20 Domains)** | **88** | AI Governance, Computer Vision (Roboflow), Deep Learning (vLLM/Triton), CLM Legal, GTM Sales, Document Automation. | `ai-governance-grc`, `roboflow-vision-mcp`, `deep-learning-nlp`, `contract-redliner`, `gtm-positioning` |
| **Community Skill Pool** | **64,687** | Indexed repository of open-source agent skills, developer utilities, and tools searchable via FTS5 BM25. | *Full pool indexed in `community_skills` table* |

---

## 👥 66 Specialist Agent Profiles

Hermes provides **66 pre-configured specialist profiles** in `~/.hermes/profiles/`. Switch execution context instantly with `hermes -p <profile>`:

```text
ORCHESTRATION & SYSTEMS             CYBERSECURITY (TEAM EXERCISES)        QUANT & ALGORITHMIC TRADING
├── orchestrator                    ├── security-audit                   ├── metatrader-quant
├── coding-engineer                 ├── red-team                         ├── tradingview-quant
├── backend-architect               ├── blue-team                        ├── pat-operations
├── frontend-developer              ├── purple-team                      ├── quant-analyst
├── fullstack-guardian              ├── white-team                       ├── finance-investment-ops
├── devops-deploy                   ├── orange-team                      └── crypto-bd-agent
├── qa-testing                      ├── yellow-team
└── system-architect                └── green-team

AI, ML & COMPUTER VISION            SEARCH, SEO & MARKETING              ENTERPRISE & LEGAL
├── deep-learning-researcher        ├── geo-search-specialist            ├── legal-clm-specialist
├── mlops-platform-engineer         ├── seo-growth-marketer              ├── legal-corporate
├── computer-vision-engineer        ├── social-media-strategist          ├── ai-governance-officer
├── mathematics-ai                  ├── marketing-growth                 ├── executive-c-suite-advisor
├── research-science                ├── content-marketer                 ├── hr-talent-operations
└── multi-agent-architect           └── gtm-sales-engineer               ├── supply-chain-architect
                                                                         └── product-manager

ECOSYSTEM SPECIALISTS (FRAMEWORKS & CLOUDS)
├── minimax-voice-agent (TTS/Audio)  ├── astro-web-architect (Astro 5)    ├── token-optimizer (Context Budget)
├── kimi-reasoning-specialist (Docs) ├── nginx-caddy-infrastructure (Ops) ├── mcp-librarian (MCP Universe)
├── manus-autonomous-agent (Web)     ├── web-scraping-specialist (DOM)    ├── skill-librarian (Skill Catalog)
├── workbuddy-enterprise (Desktop)   ├── knowledge-graph-architect (Neo4j)└── foundation-agent (Core Systems)
├── tencent-cloud-architect (Cloud)  ├── office-excel-pdf (Financials)
└── laravel-architect (PHP/Bagisto)
```

---

## 🔌 45 Curated Production MCP Servers

Pre-configured in `recommended-mcp-servers.json` with native tool bindings, security isolation, and environment variable substitution:

```text
WEB & RESEARCH                      MEMORY & KNOWLEDGE GRAPH             DEVELOPER TOOLS
├── brave-search (Web Search)       ├── mempalace (AAAK Memory)          ├── git (Version Control)
├── manus-research (Deep Crawl)     ├── codegraph (AST Indexing)         ├── docker (Container Engine)
├── scrapling-crawler (Anti-Bot)    ├── knowledge-graph-neo4j (Cypher)   ├── filesystem (Scoped IO)
└── fetch (HTTP Content Reader)     ├── memory (Entity-Relationship)     ├── conda-cli (Env Isolation)
                                    └── sqlite (Relational DB)           └── document-specialist-mcp

QUANT & FINANCIAL DATA              MULTIMODAL & COMPUTER VISION         ENTERPRISE PLATFORMS
├── metatrader5 (MT5 Broker Bridge) ├── roboflow-vision-mcp (Inference)  ├── microsoft-fabric (OneLake)
├── questdb (Ultra-Low-Latency TS)  ├── huggingface-mcp (Hub Models)     ├── caddy-security (TLS & Auth)
├── timescaledb (Hypertables)       ├── pi-voice (Real-Time Audio)       ├── ai-guardrails-mcp (Safety)
├── tradingview-signals (Alerts)    └── compdf-mcp (OCR & Layout)        ├── openfactcheck-mcp (Evidence)
├── redis (Semantic Cache & PubSub)                                      ├── legal-clm-mcp (Redlining)
├── postgres (Enterprise SQL)                                            ├── gtm-sales-mcp (Pipelines)
└── mcp-server-excel (Formulas/UDF)                                      └── supplychain-mcp (Logistics)

BROWSER AUTOMATION & CAPTCHA        MESSAGING & NOTIFICATIONS            WORKFLOWS & SCHEDULING
├── playwright (Headless Browser)   ├── discord (Guild & Channels)       ├── agent-cron (Autonomous Jobs)
├── puppeteer (Chromium Engine)     ├── telegram-bot (Mini-Apps)         └── deer-flow (Graph Execution)
└── 2captcha (Turnstile Solver)     ├── whatsapp-wassenger (Omnichannel)
                                    └── laya (Notification Hub)
```

---

## ⚡ 17 Native Pre-compiled Engines

Pre-installed in `/usr/local/bin` with automatic privilege dropping to `predictatrade` (`UID=1001`):

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
| 12-17| **Skill Suites** | Markdown / Code | `skill-library/` | Product localization (23 skills), multi-agent translation with terminology verification, translation file sync, book translation, and skills curriculum. |

---

## 🔍 Hybrid Vector Registry & Interactive Dashboard (`hermes-registry`)

Hermes provides `/usr/local/bin/hermes-registry` offering both an **Interactive Web Dashboard / UI** and an **autonomous CLI engine** for hybrid search (dense ChromaDB vector embeddings + sparse SQLite FTS5 BM25), package management, and dynamic JIT tool execution:

### 1. Interactive Web Dashboard & UI

Launch the embedded zero-dependency Web Dashboard:

```bash
# Launch on default port 8888 (accessible locally or over network)
hermes-registry ui

# Or specify custom host and port
hermes-registry dashboard --host 0.0.0.0 --port 8888
```

The Web Dashboard (`http://localhost:8888` or `http://platform.predictatrade.com:8888`) provides:
- **🔎 Hybrid Search Engine**: Instant search combining semantic vector cosine similarity with full-text keyword indexing across all 19,691 skills.
- **📂 Category Explorer**: Filter across 48 domain classifications (Financial Quant, Security Audit, GEO, MLOps, Office/PDF, etc.).
- **📖 Skill Inspector**: Full modal viewer for `SKILL.md` instructions, frontmatter, parameters, and code examples.
- **⚡ 1-Click Install & Activate**: Dynamically activate any skill into any of the 66 specialist profiles (`orchestrator`, `security-audit`, `metatrader-quant`, etc.) without copying files.
- **🗑️ 1-Click Uninstall & Deactivate**: Remove tools from profile context instantly to preserve prompt token ceilings.
- **👥 Profile Manager**: Visual inspection of active tools across all 66 profiles.
- **🔌 MCP & Plugins Hub**: Directory of 45 curated production MCP servers and 32 plugins.

### 2. Autonomous CLI Usage

```bash
# 1. View combined relational (SQLite) and vector (ChromaDB) statistics
hermes-registry stats

# 2. Natural language intent resolution (Hybrid Dense ChromaDB + Sparse SQLite FTS5)
hermes-registry resolve "audit solana smart contract reentrancy and token bonding curves"

# 3. Dynamically install/activate a skill into profile context (aliases: activate / install)
hermes-registry install web3-audit --profile security-audit

# 4. Evict the tool cleanly when the task finishes to keep prompt context clean (aliases: deactivate / uninstall)
hermes-registry uninstall web3-audit --profile security-audit
```

---

## 🗄️ SQLite Knowledge Vault CLI (`hermes-vault`)

The master SQLite vault at `/home/predictatrade/.hermes/hermes-vault.sqlite` (301 MB) can be queried instantly via `/usr/local/bin/hermes-vault`:

```bash
# View ecosystem counts and system metadata
hermes-vault stats

# Search curated skills by keyword or category
hermes-vault skills geo
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

---

## 🛡️ Enterprise Security & Isolation Rules

1. **Non-Root Execution**:
   Hermes executes under the dedicated service user `predictatrade` (`UID=1001`, `GID=1001`). The account is excluded from `sudo` and privileged groups.
2. **Rootless Docker Daemon**:
   Containers run via `unix:///run/user/1001/docker.sock` in unprivileged user namespaces. Host Docker (`/var/run/docker.sock`) remains untouched.
3. **Automatic Privilege Dropping**:
   All CLI wrappers in `/usr/local/bin` automatically drop privileges from `root` to `predictatrade` using `runuser -u predictatrade`. Root users enjoy full ergonomics without host contamination.
4. **Zero API Key Leakage**:
   Secrets reside strictly in `~/.hermes/.env` (mode `0600`). Never hardcode secrets in YAML configs or git repositories.

---

## 📚 Master Documentation & Guides

- [**`README-HERMES.md`**](README-HERMES.md) — Comprehensive technical manual (architecture, engine benchmarks, profile configurations).
- [**`README-LOCAL-INSTALL.md`**](README-LOCAL-INSTALL.md) — Offline deployment runbook, air-gapped installation, and SQLite schema.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
