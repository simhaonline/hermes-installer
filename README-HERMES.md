# Hermes Agent Production Deployment & Built-in Architecture

## Enterprise Edition: Platform Predict-A-Trade (`platform.predictatrade.com`)

This document provides complete operational, architectural, and developer documentation for the production deployment of the **Hermes Agent** platform on Ubuntu LTS (`platform.predictatrade.com`), incorporating all 16 advanced AI, engineering, reverse engineering, and multi-agent simulation engines.

---

## 1. Architectural Highlights & Security Boundaries

### A. Dedicated Service User Isolation
- **Non-Privileged Service Account**: Hermes executes strictly as the dedicated user `predictatrade` (`UID=1001`, `GID=1001`), with home directory at `/home/predictatrade`.
- **Group Isolation Boundary**: The `predictatrade` user is strictly prohibited from belonging to privileged system groups (`docker`, `sudo`, `adm`), preventing any privilege escalation from within the agent context.
- **Dedicated Project Workspace**: Primary workspace resides at `/srv/predictatrade` with `0750` permissions owned by `predictatrade:predictatrade`.
- **Subordinate IDs**: 65,536 contiguous subordinate UIDs/GIDs allocated in `/etc/subuid` and `/etc/subgid` (`predictatrade:100000:65536`) enabling rootless container namespaces.

### B. Dual Docker Daemon Architecture
- **Host Production Docker**: The host's standard Docker daemon runs unaltered on `/var/run/docker.sock` for system services and platform-level infrastructure.
- **Hermes Isolated Rootless Docker**: Hermes operates within its own dedicated **Rootless Docker** daemon (`unix:///run/user/1001/docker.sock`), managed by the systemd user service `user@1001.service` with persistent lingering enabled (`loginctl enable-linger predictatrade`).
- **Namespace & Cgroup v2 Isolation**: Enforced via systemd cgroup2fs and scoped AppArmor profile (`/etc/apparmor.d/usr.bin.rootlesskit`).
- **Pre-Loaded Official Sandbox**: The official desktop sandbox image (`nousresearch/hermes-sandbox:desktop`, 4.4 GB) is preloaded and cached directly in Rootless Docker for immediate containerized desktop tool execution without runtime pull delays.

### C. Zero-Host Contamination Multi-User Binary Wrappers
All primary Hermes binaries installed into `/usr/local/bin` seamlessly drop privileges from `root` to `predictatrade` using `runuser -u predictatrade`:
- `/usr/local/bin/hermes`
- `/usr/local/bin/hermes-skill-catalog`
- `/usr/local/bin/hermes-community-skills`
- `/usr/local/bin/hermes-mcp-universe`
- `/usr/local/bin/hermes-agent-cron`
- `/usr/local/bin/token-saver` & `/usr/local/bin/hermes-token-saver`
- `/usr/local/bin/hermes-project-context`
- `/usr/local/bin/trim` & `/usr/local/bin/trim-1`
- `/usr/local/bin/codegraph`
- `/usr/local/bin/mcptoon`
- `/usr/local/bin/mempalace` & `/usr/local/bin/mempalace-mcp`
- `/usr/local/bin/rea` & `/usr/local/bin/rea-agents`
- `/usr/local/bin/pentagi`
- `/usr/local/bin/auto`
- `/usr/local/bin/hermes-vault`
- `/usr/local/bin/hermes-registry`

### D. User Execution Model: Running as Root vs. predictatrade

#### Can I start and run projects as `root`?
**YES.** All primary command-line tools in `/usr/local/bin` (`hermes`, `hermes-vault`, `hermes-skill-catalog`, `hermes-community-skills`, `hermes-mcp-universe`, `codegraph`, `mcptoon`, `trim`, `mempalace`, `rea`, `pentagi`, `auto`, etc.) are wrapped with automatic privilege-dropping logic. When executed as `root`:
1. The wrapper automatically switches execution context to `predictatrade` via `runuser -u predictatrade`.
2. It sets `HOME="/home/predictatrade"`, `HERMES_HOME="/home/predictatrade/.hermes"`, and connects to the Rootless Docker socket (`unix:///run/user/1001/docker.sock`).
3. It preserves your working directory if accessible, or defaults to `/srv/predictatrade`.
4. **Advantage**: You get the ergonomics of typing commands directly from your root shell, while the agent and all untrusted AI code are strictly quarantined in non-root user space.

#### Can I run directly as the `predictatrade` user?
**YES.** For pure non-root interactive sessions:
```bash
su - predictatrade
cd /srv/predictatrade
hermes
```
Or run one-off commands from root:
```bash
runuser -u predictatrade -- hermes
```

#### Where should project files live?
All projects and code repositories should reside in `/srv/predictatrade/` (or subdirectories such as `/srv/predictatrade/my-project`).
- If you create project directories while logged in as `root`, ensure `predictatrade` owns them:
  ```bash
  mkdir -p /srv/predictatrade/my-algo-trader
  chown -R predictatrade:predictatrade /srv/predictatrade/my-algo-trader
  ```
- This guarantees Hermes has full read, write, execution, and git permissions without permission-denied errors.

---

## 2. Included Components & Features

### A. Skill Libraries (19,691+ Curated Skills across 52 Categories + 64,687 Community Pool)

The installation provides a comprehensive two-tiered skill architecture:

#### 1. Retained Curated Library: 19,691+ Skills across 52 Categories
Located in `/home/predictatrade/.hermes/skill-library` and `/home/predictatrade/.hermes/skills`:

| Category | Skill Count | Primary Capabilities |
|---|---|---|
| `foundation-skills` | 13,748 skills | Anthropic, OpenAI, Microsoft, Google, VoltAgent, and Hugging Face agentic skills and reasoning benchmarks |
| `minimax-audio-voice` | 1,292 skills | MiniMax voice cloning, audio synthesis, speech-to-text, MiniMax-Music3, and multimodal audio agent tooling |
| `laravel-php-ecosystem` | 810 skills | Modern Laravel fullstack engineering, Eloquent ORM, Blade, Bagisto e-commerce, LaraClaude, API skills |
| `quant-trading` | 553 skills | MQL5 Expert Advisors, MT5 bridge operations, PineScript v5 strategies, Fibonacci retracements, risk engines, order flow analyzers, volatility forecasting |
| `office-excel-pdf` | 383 skills | Excel spreadsheets, VBA macros, pivot tables, OpenPyXL/XlsxWriter automation, WeasyPrint PDF generator, ComPDFKit SDK, PDFMiner |
| `custom` | 317 skills | Predict-A-Trade proprietary signal reconciliation, payment symmetry, trade risk safety, telemetry, docker migration, runbook automation |
| `kimi-suite` | 309 skills | Moonshot Kimi K3 long-context reasoning, multi-turn reasoning chains, deep research synthesis, large-scale document analysis |
| `seo-growth-marketing` | 262 skills | Agentic SEO, SE Ranking integration, keyword research, SERP analysis, programmatic content strategy, backlink audits |
| `manus-agent` | 238 skills | Manus AI agent workflows, multi-step browser execution, automated desk research, autonomous agentic tool composition |
| `workbuddy-suite` | 193 skills | Enterprise workflow automation, PowerShell scripting, system administration, productivity copilots, office integrations |
| `backend-languages` | 135 skills | Go concurrency, Rust agentic patterns, Python asyncio, FastAPI, NestJS, Next.js fullstack engineering |
| `official-optional` | 128 skills | Bundled optional capabilities from official upstream Hermes Agent repository |
| `ui-ux-design` | 117 skills | Tailwind CSS v4, UI/UX Pro Max, Garden UI, SVG dark-mode diagrams, design tokens, responsive layouts |
| `mathematics-ai` | 116 skills | Lean 4 / Coq theorem proving, AI4Math paper reading, AI4Math auto-research, mathematics learning curricula, algebraic geometry |
| `tencent-cloud-ecosystem` | 103 skills | Tencent CloudBase serverless, Tencent RTC real-time audio/video, Tencent Maps GL JS SDK, WeChat mini-program backends |
| `community-elite` | 65 skills | Top-rated, curated multi-agent workflow tools and orchestration pipelines |
| `knowledge-graph` | 47 skills | CodeGraph callers/callees impact traversal, Neo4j graph extractors, LightRAG, Memstack holographic sync, ontology mapping |
| `astro-web-framework` | 43 skills | Astro 4+ web framework, content collections, SSG/SSR pipelines, island architecture, agentic website publishing |
| `omnichannel-messaging` | 43 skills | Telegram bot/mini-apps, Discord developer tools, WhatsApp Flows, Wassenger CRM integrations, Slack bot events |
| `nginx-caddy-infrastructure` | 35 skills | Nginx reverse proxies, high-throughput web server config, Caddy v2 security & automatic TLS, WAF rules, load balancing |
| `translation-localization` | 32 skills | Suite of 23 composable product localization skills (BrunoMiguens), multi-agent translation pipeline with terminology verification (senshinji), i18n/l10n automated file sync (irsali), book translation engine (deusyu) |
| `safe-agent-runtime` | 28 skills | NVIDIA OpenShell policy enforcement, rootless container security, memory isolation, permission boundary guards |
| `security-audit` | 26 skills | PentAGI automated security assessment, Pashov smart contract auditing, Auditmos verification, codebase security auditing, Cloudflare Zero Trust |
| `web-scraping` | 26 skills | Scrapling crawler, Scrapfly API, stealth browser crawler, HasData engine, anti-bot bypass, automated captcha solving |
| `workflow-automation` | 26 skills | Superpowers plan-then-act, multi-agent delegation, Kanban decomposition, scheduled event dispatching |
| `enterprise-data-cloud` | 25 skills | Microsoft Fabric lakehouse, Synapse Spark pipelines, PowerBI DAX, AWS S3 transfer, Azure Blob management |
| `databases-timeseries` | 23 skills | TimescaleDB hypertables, QuestDB TSBS benchmarks, PostgreSQL enterprise DBA, Redis agent cache |
| `chart-visualization` | 12 skills | ApexCharts, AntV G2Plot, Lightweight Charts, Chart.js dashboards, financial candlestick renderers |
| `productivity` | 11 skills | Document synthesis, task tracking, presentation generation, spreadsheet formula recalculation |
| `creative` | 10 skills | Prompt engineering, SVG graphics generation, branding kits, visual storytelling |
| `enterprise-operations` | 10 skills | SRE incident triage, runbook execution, SLA tracking, compliance auditing |
| `software-development` | 9 skills | Git workflows, branch protection, code review guidelines, PR automation |
| `skill-forge` | 9 skills | Dynamic agent skill generation, validation testbenches, YAML frontmatter linters |
| `skill-tutorials` | 6 skills | Claude Skills authoring guide and best practices curriculum (foreveryh) |
| `autonomous-ai-agents` | 5 skills | AutoAgent autonomous flow execution, self-improving prompt loops, recursive problem solving |
| `apple` | 4 skills | Swift scripting, macOS system commands, AppleScript automation |
| `research` | 4 skills | Academic paper synthesis, arXiv ingestion, literature review compilers |
| `context-optimization` | 4 skills | MCPToon TOON-format token compression (99.2% reduction) and Trim-1 Go context trimmer |
| `token-saving` | 4 skills | Token Saver, prompt compression, context distillation, budget enforcement |
| `media` | 3 skills | Video transcription, audio-io processing, image conversion |
| `email` | 2 skills | IMAP/SMTP mail processing, transactional email formatting |
| `devops` | 1 skills | CI/CD pipeline automation, Dockerfile optimization |
| `note-taking` | 1 skills | Markdown vault management, Obsidian sync |
| `social-media` | 1 skills | Social engagement analytics, automated posting schedulers |
| `web` | 1 skills | HTTP status inspection, curl automation |

**Total: 19,222 skills across 47 categories**

#### 2. Captured Community Skill Pool: 64,569 Unique Packages
- Located at: `/home/predictatrade/.local/share/hermes-community-skill-pool/skills`
- Manifest: `/home/predictatrade/.local/share/hermes-community-skill-pool/index.jsonl`
- Full triage breakdown: Comprehensive pool of curated and indexed skills across open-source ecosystems.
- Instant search and enablement across all 64,569 packages via `hermes-community-skills search <query>` or `hermes-vault community <query>`.

---

## 3. The 16 Advanced Integrated Engines

| # | Repository | Component Name | Technology | Capabilities & Integration |
|---|---|---|---|---|
| 1 | `activeing123/mcptoon` | **MCPToon** | Python / CLI | Zero-dependency MCP gateway & 99.2% token context compression CLI (`/usr/local/bin/mcptoon`). Converts large MCP tool payloads into TOON notation. |
| 2 | `colbymchenry/codegraph` | **CodeGraph** | TypeScript / WASM | Pre-indexed AST knowledge graph (`/usr/local/bin/codegraph`). Computes callers/callees impact analysis and multi-language semantic code search. |
| 3 | `MemPalace/mempalace` | **MemPalace** | Python / ChromaDB | Local-first AI memory system with ChromaDB backend (`/usr/local/bin/mempalace` and `/usr/local/bin/mempalace-mcp`). AAAK Dialect compression (~30x reduction). |
| 4 | `morluto/rea` | **REA (Reverse Engineering)** | Node.js / CLI | Universal binary reverse engineering, static analysis & decompilation MCP/CLI (`/usr/local/bin/rea`, `rea-agents`). Disassembles ELF, Mach-O, and PE binaries. |
| 5 | `666ghj/MiroFish` | **MiroFish** | Python / Plugin | Universal swarm intelligence and predictive multi-agent simulation engine. Pre-installed in plugins and specialist agents. |
| 6 | `NVIDIA/OpenShell` | **NVIDIA OpenShell** | Rust / Python | Safe, private runtime for autonomous AI agents. Sandboxed policy enforcement and gRPC communication stubs installed in `openshell` Python package. |
| 7 | `HKUDS/AutoAgent` | **AutoAgent** | Python / CLI | Zero-code autonomous LLM agent execution framework (`/usr/local/bin/auto`, `autoagent` Python package). Multi-agent workflow generator and triage agent. |
| 8 | `caveman-ai/trim-1` | **Trim-1** | Go Binary | Ultra-fast compiled 1.2MB model for line-level context trimming (`/usr/local/bin/trim`, `/usr/local/bin/trim-1`). Selects relevant context lines based on prompt query. |
| 9 | `cactus-compute/cactus` | **Cactus Compute** | Python / C++ | Quantization kernels, neural graph transpiler & low-latency edge inference runtime (`cactus` Python package). Optimized for low-precision weights. |
| 10 | `vxcontrol/pentagi` | **PentAGI** | Go Binary | Autonomous penetration testing and defensive security auditing agent system (`/usr/local/bin/pentagi`). Pre-compiled Go backend with graphiti/neo4j connectors. |
| 11 | `aayushch/laya` | **Laya** | Python / MCP | Local-first AI notification command center aggregating Slack, Gmail, GitHub, and Jira (`laya` Python package & MCP definition). |
| 12 | `BrunoMiguens/translating-products-skill` | **Product Localization** | Skills Suite | Suite of 23 composable product localization skills in `/home/predictatrade/.hermes/skill-library/translation-localization/`. |
| 13 | `senshinji/claude-translation-skill` | **Multi-Agent Translation** | Skills Suite | Multi-agent translation pipeline with terminology verification and glossary enforcement. |
| 14 | `irsali/translation-skill` | **Translation File Sync** | Skills Suite | AI-powered translation file synchronizer for i18n/l10n JSON and YAML files. |
| 15 | `deusyu/translate-book` | **Book Translation** | Skills Suite | Book translation skill for PDF, DOCX, and EPUB documents using parallel subagents. |
| 16 | `foreveryh/claude-skills-tutorial` | **Skills Curriculum** | Skills Suite | Comprehensive skills curriculum and documentation authoring tutorial in `/home/predictatrade/.hermes/skill-library/skill-tutorials/`. |

---

## 4. Agent Library (480 Personas) & 66 Specialist Profiles

### 1. Agent Library (480 Personas)
Located in `/home/predictatrade/.hermes/agent-library`:
- **329 Agency Agents**: Pre-configured specialized personas across Engineering, Design, Academic Research, Copywriting, and Marketing.
- **90 Technical Specialists**: Located in `/home/predictatrade/.hermes/agent-library/specialist-agents/`, including:
  - `GEOSearchSpecialist.agent.md` — Generative Engine Optimization, Schema.org entity graphs, and AI citation visibility.
  - `SocialMediaStrategist.agent.md` — Autonomous social media marketing, viral hooks, and multi-channel scheduling.
  - `GTMSalesEngineer.agent.md` — Go-To-Market acceleration, outbound sequences, and lead scoring.
  - `CustomerSuccessSpecialist.agent.md` — Churn prevention, health scores, and customer onboarding.
  - `DeepLearningResearcher.agent.md` — Neural architectures, transformers, and distributed training.
  - `NLPPipelineEngineer.agent.md` — High-precision NLP pipelines, embeddings, and semantic search.
  - `ComputerVisionEngineer.agent.md` — YOLO object detection, Roboflow datasets, OCR, and multimodal vision.
  - `MLOpsPlatformEngineer.agent.md` — Production MLOps, MLflow registries, and vLLM/Triton serving.
  - `DataAnalyticsSpecialist.agent.md` — Automated EDA, hypothesis testing, and executive BI dashboards.
  - `DataEngineeringSpecialist.agent.md` — Modern data stack, DuckDB/ClickHouse pipelines, and dbt modeling.
  - `AgentOrchestrationSwarm.agent.md` — Multi-agent swarm coordination and hierarchical delegation.
  - `DocumentAutomationSpecialist.agent.md` — Intelligent document processing, PDF extraction, and contract redlines.
  - `FactCheckingAnalyst.agent.md` — Automated fact-checking, claim verification, and source credibility rating.
  - `FormalProblemSolver.agent.md` — First-principles formal problem solving, MECE trees, and decision matrices.
  - `AIGovernanceOfficer.agent.md` — AI ethics, EU AI Act compliance, NIST AI RMF, and safety guardrails.
  - `ExecutiveCSuiteAdvisor.agent.md` — Board governance, executive strategy memos, and corporate OKRs.
  - `HRTalentOperations.agent.md` — HR workflows, competency modeling, and employee onboarding.
  - `LegalCLMSpecialist.agent.md` — Contract lifecycle management, clause risk scoring, and RFP review.
  - `codegraph-intelligence.md` — Codebase AST knowledge graph and impact traversal.
  - `rea-reverse-engineering.md` — Binary disassembly, decompilation, and reverse engineering.
  - `mirofish-swarm.md` — Swarm intelligence and predictive multi-agent simulation.
  - `autoagent-autonomous.md` — Autonomous workflow synthesis and zero-code execution.
  - `mempalace-memory.md` — Holographic AI memory retrieval and AAAK compression.
  - `pentagi-pentest.md` — Autonomous penetration testing and security auditing.
  - `laya-command-center.md` — Notification triage and omnichannel alert routing.
  - `cactus-quant.md` — Edge quantization kernels and low-latency inference.
- **13 Quantitative Trading Specialists**: Quant researchers, MQL5 EA developers, PineScript strategy engineers.
- **Fabric, Personal AI Employee & PM Personas**: Project managers, sprint planners, enterprise data architects.

### 2. 66 Dedicated Specialist Profiles
Configured with independent memory stores and selective skill routing in `/home/predictatrade/.hermes/profiles/`:
`orchestrator`, `coding-engineer`, `qa-testing`, `devops-sre`, `cloud-infrastructure`, `security-audit`, `ethical-hacking-pentest`, `red-team`, `blue-team`, `purple-team`, `white-team`, `yellow-team`, `green-team`, `orange-team`, `ai-llm-engineer`, `ai-research-mlops`, `data-knowledge`, `research-science`, `metatrader-quant`, `analytics-finance`, `business-operations`, `documents-office`, `legal-corporate`, `creative-media`, `marketing-growth`, `communications-sales`, `mcp-librarian`, `skill-librarian`, `esoteric-advisor`, `multi-agent-architect`, `backend-architect`, `database-optimizer`, `code-reviewer`, `agentic-search-optimizer`, `token-optimizer`, `tradingview-quant`, `fabric-engineer`, `web-scraping-specialist`, `knowledge-graph-architect`, `product-manager`, `chart-visualization`, `pat-operations`, `mathematics-ai`, `office-excel-pdf`, `nginx-caddy-infrastructure`, `astro-web-architect`, `minimax-voice-agent`, `kimi-reasoning-specialist`, `manus-autonomous-agent`, `workbuddy-enterprise`, `tencent-cloud-architect`, `laravel-architect`, `seo-growth-marketer`, `foundation-agent`, `geo-search-specialist`, `social-media-strategist`, `gtm-sales-engineer`, `mlops-platform-engineer`, `computer-vision-engineer`, `fact-checking-analyst`, `ai-governance-officer`, `executive-c-suite-advisor`, `hr-talent-operations`, `legal-clm-specialist`, `supply-chain-architect`, and `deep-learning-researcher`.

- **Multi-Agent Kanban Decomposition**: Pre-initialized on default profile via SQLite database at `/home/predictatrade/.hermes/kanban.db`.
- **Subagent Parallelism**: Concurrency cap of 3 child agents, spawn depth limit of 2, 250 max turns.

---

## 5. MCP (Model Context Protocol) Suite (45 Curated Servers)

Stored in `/home/predictatrade/.hermes/mcp-library/recommended-mcp-servers.json`:

| Server Name | Transport | Purpose & Capabilities |
|---|---|---|
| `filesystem` | stdio | Workspace file read/write, directory scanning, and bounded file access |
| `memory` | stdio | Graph-based associative semantic memory across sessions |
| `git` | stdio | Full git repository management: diffs, status, commit log, branch inspection |
| `metatrader5` | stdio / IPC | MetaTrader 5 trade execution, account telemetry, order placement, tick ingest |
| `timescaledb` | stdio | High-throughput time-series financial hypertable storage and querying |
| `questdb` | stdio | Nanosecond-precision tick recording and TSBS quantitative benchmarks |
| `redis` | stdio | In-memory key-value state cache and pub/sub message broker |
| `postgres` | stdio | Relational database operations, transactions, and trade accounting |
| `sqlite` | stdio | Local profile state, Kanban task board, and persistent operational metrics |
| `puppeteer` | stdio | Headless Chromium browser automation, screenshot capture, DOM scraping |
| `playwright` | stdio | Cross-browser automated interaction, form testing, and end-to-end flows |
| `fetch` | stdio | HTTP/HTTPS static content retrieval and HTML-to-markdown conversion |
| `brave-search` | stdio | Privacy-first live web search and real-time market intelligence |
| `docker` | stdio | Rootless container lifecycle, image inspection, and sandbox execution |
| `whatsapp-wassenger` | stdio | WhatsApp CRM messaging, customer support alerts, and order notices |
| `telegram-bot` | stdio | Real-time trading signal alerts, Telegram mini-app webhook bridge |
| `discord` | stdio | Discord channel notifications, trading room bot interactions |
| `tradingview-signals` | stdio | Webhook ingest for PineScript alerts and strategy execution triggers |
| `conda-cli` | stdio | Conda environment management and binary package isolation |
| `microsoft-fabric` | stdio | Microsoft Fabric lakehouse integration, Synapse Spark jobs, PowerBI models |
| `scrapling-crawler` | stdio | Stealth adaptive anti-detection web scraper and HTML parser |
| `knowledge-graph-neo4j` | stdio | Cypher query execution, entity graph relationships, ontology queries |
| `agent-cron` | stdio | Scheduled background cron tasks, recurring watchdogs, intervals |
| `deer-flow` | stdio | Recursive research web search and deep-crawl knowledge synthesis |
| `2captcha` | stdio | Automated CAPTCHA solving for continuous scraping workflows |
| `codegraph` | stdio | Pre-indexed AST knowledge graph, caller/callee traversal, semantic search |
| `mcptoon` | stdio | Zero-dependency MCP gateway compressing tool payloads to TOON (99.2% token savings) |
| `mempalace` | stdio / HTTP | ChromaDB holographic memory retrieval with AAAK dialect compression |
| `rea` | stdio | Binary reverse engineering, disassembly, and static security analysis |
| `laya` | stdio | Unified notification command center for Slack, Gmail, GitHub, Jira |
| `mcp-server-excel` | stdio | Enterprise spreadsheet processing, data extraction, formula auditing, and workbook synthesis |
| `compdf-mcp` | stdio | High-performance PDF parsing, annotation extraction, document conversion, and table reconstruction |
| `caddy-security` | stdio | Infrastructure security gateway, automated TLS, authentication, and reverse proxy management |
| `pi-voice` | stdio | Real-time speech-to-text, text-to-speech, and audio streaming interface |
| `manus-research` | stdio | Multi-agent autonomous research and deep web knowledge extraction workflow bridge |
| `geo-search-mcp` | stdio | Generative Engine Optimization (GEO) and AI search visibility audit MCP server |
| `social-media-mcp` | stdio | Social media automation and multi-platform publishing MCP server |
| `openfactcheck-mcp` | stdio | Automated fact-checking, claim verification, and evidence retrieval MCP server |
| `roboflow-vision-mcp` | stdio | Roboflow computer vision dataset, inference, and object detection MCP server |
| `huggingface-mcp` | stdio | Hugging Face Hub model discovery, dataset querying, and spaces MCP server |
| `legal-clm-mcp` | stdio | Contract Lifecycle Management (CLM) clause analysis and redlining MCP server |
| `supplychain-mcp` | stdio | Supply chain network resilience, freight tracking, and logistics optimization MCP server |
| `gtm-sales-mcp` | stdio | Go-To-Market pipeline acceleration, lead scoring, and customer retention MCP server |
| `ai-guardrails-mcp` | stdio | Runtime prompt-injection defense, output hallucination filter, and safety guardrails MCP server |
| `document-specialist-mcp` | stdio | Intelligent document processing, PDF form extraction, and layout analysis MCP server |

---

## 6. Active Plugins & Extensions (32 Plugins)

Located in `/home/predictatrade/.hermes/plugins/`:
- **`agentic-flow`**: Multi-agent swarm coordination, cyclic state machine workflows, and hierarchical delegation.
- **`geo-optimizer`**: Generative Engine Optimization audit, JSON-LD knowledge graph generator, and AI answer engine tracker.
- **`openfactcheck`**: Automated claim decomposition, multi-source evidence retrieval, and fact verification engine.
- **`ai-governance`**: EU AI Act and NIST AI RMF compliance checker, runtime prompt-injection guardrails, and risk auditor.
- **`contract-lifecycle`**: Intelligent contract analysis, clause risk scoring, auto-redlining, and procurement evaluation.
- **`gtm-engine`**: B2B outbound pipeline acceleration, lead scoring, customer retention telemetry, and churn prediction.
- **`mcptoon`**: Zero-dependency MCP gateway & 99.2% token context compression CLI.
- **`codegraph`**: AST knowledge graph and impact analysis engine.
- **`mempalace`**: Local AI memory system with ChromaDB backend and AAAK dialect.
- **`rea`**: Universal binary reverse engineering, static analysis & decompilation.
- **`trim-1`**: Line-level context trimming engine.
- **`mirofish`**: Swarm intelligence and predictive multi-agent simulation.
- **`openshell`**: NVIDIA safe private agent runtime and sandbox isolation.
- **`autoagent`**: Autonomous LLM agent execution framework.
- **`cactus`**: Quantization kernels and neural graph transpiler.
- **`laya`**: Local AI notification aggregator.
- **`pentagi`**: Autonomous penetration testing backend.
- **`superpowers`**: Step-by-step workflow planner, verification safeguards, tool chaining.
- **`homeassistant`**: IoT smart-home integration with entity querying and service calls.
- **`token-saver`**: Interceptor reducing token consumption across extended sessions.
- **`disk-cleanup`**: Automated workspace garbage collection and artifact grooming.
- **`security-guidance`**: Real-time shell command vetting and safety boundary enforcement.
- **`memstack`**: Long-term holographic semantic memory across sessions.
- **`quantmind`**: High-frequency quant and risk modeling toolkit.
- **`agent-cron`**: Scheduled cron watchdog and interval manager.
- **`scrapling`**: Stealth anti-detection web scraper.
- **`deer-flow`**: Deep recursive research crawler.
- **`tradingview-pinescript`**: TradingView strategy and indicator integration.
- **`mql5-libraries`**: MQL5 trading bridges and EA components.
- **`fabric-plugins`**: Microsoft Fabric lakehouse and Synapse Spark extensions.
- **`manus-research`**: Autonomous web research, evidence verification, and multi-source synthesis plugin.
- **`wookstar-plugins`**: Advanced Claude plugin suite for enterprise workflows and multi-agent coordination.

---

## 7. Command-Line Reference

| Command | Functionality | Example |
|---|---|---|
| `hermes` | Interactive agent CLI session (auto-drops privileges to `predictatrade`) | `hermes` or `hermes -p default chat` |
| `hermes-skill-catalog` | Search, inspect, list categories, enable or disable skills | `hermes-skill-catalog search quant` |
| `hermes-community-skills` | Search and activate community skills from the 25,000+ pool | `hermes-community-skills search scrapfly` |
| `hermes-mcp-universe` | Search, inspect, and register MCP servers | `hermes-mcp-universe search redis` |
| `hermes-agent-cron` | Manage scheduled jobs, cron watchdogs, and intervals | `hermes-agent-cron list` |
| `token-saver` | Token consumption analytics, savings statistics, and compression | `token-saver stats` |
| `trim` / `trim-1` | Fast line-level context trimming for large files | `trim --query "database connection" config.yaml` |
| `codegraph` | Codebase AST graph generation and impact traversal | `codegraph index .` or `codegraph search "handleOrder"` |
| `mcptoon` | Run zero-dependency token compression gateway | `mcptoon --input data.json` |
| `mempalace` | Local AI memory search, ingest, and audit | `mempalace search "trade strategy"` |
| `mempalace-mcp` | Start MemPalace MCP server on stdio or HTTP | `mempalace-mcp --palace ~/.hermes/memories` |
| `rea` | Reverse engineering and binary analysis CLI | `rea analyze /usr/local/bin/trim` |
| `auto` | AutoAgent dynamic autonomous agent runner | `auto agent --help` |
| `pentagi` | Autonomous penetration testing and audit suite | `pentagi --help` |
| `hermes-vault` | SQLite Knowledge Vault CLI (stats, skills, MCP, agents, engines) | `hermes-vault stats` |

---

## 8. Practical Usage Guide: Skills, Agents, MCPs, and Plugins

### A. How to Use SKILLS (1,688 Curated + 43,000 Community Pool)

#### 1. Discovering & Inspecting Skills
```bash
# List all 33 categories and skill counts
hermes-skill-catalog categories

# Search curated skills by keyword or category
hermes-skill-catalog search "fibonacci"
hermes-skill-catalog search "mql5" --category quant-trading
hermes-skill-catalog search "reverse engineering" --category security-audit

# Inspect detailed instructions, inputs, and code requirements for any skill
hermes-skill-catalog info fibonacci-retracement
hermes-skill-catalog info mql5-ea-scaffold

# Search community pool (43,000+ packages)
hermes-community-skills search scrapfly
hermes-community-skills search crypto-arbitrage
```

#### 2. Enabling Skills for Profiles
Skills can be toggled per profile:
```bash
# Enable a skill in the default profile
hermes-skill-catalog enable fibonacci-retracement --profile default

# Enable in a specialist profile
hermes-skill-catalog enable mql5-ea-scaffold --profile metatrader-quant
```

#### 3. How Skills are Invoked in an Active Hermes Session
When chatting with Hermes (`hermes` or `hermes -p <profile>`), Hermes automatically has access to all enabled skills in `~/.hermes/skills/`:
- **Natural Language Triggering**: Simply ask Hermes to perform the task, and it will autonomously discover and invoke the relevant skill.
  > *"Analyze the tick log in tick_data.csv and calculate the 0.382 and 0.618 Fibonacci retracement levels for BTC/USD."*
  > *"Generate an MQL5 Expert Advisor template for MetaTrader 5 implementing a dual-EMA crossover with trailing stop."*
- **Explicit Skill Directives**: You can instruct Hermes to follow a specific skill definition:
  > *"Execute using the `solidity-security-audit` skill on contracts/Vault.sol and report vulnerabilities."*
  > *"Use the `mcptoon-compress` skill to summarize large JSON response before saving to disk."*

---

### B. How to Use AGENTS (415+ Personas & 42 Specialist Profiles)

#### 1. Running with 42 Pre-Configured Specialist Profiles
Hermes supports switching entire agent profiles with independent memory stores, targeted skill sets, and specialized system prompts using `-p <profile>`:
```bash
# Quantitative algorithmic trading & MetaTrader 5 development
hermes -p metatrader-quant

# Code security auditing, penetration testing & smart contract verification
hermes -p security-audit

# Fullstack software engineering, refactoring & architectural design
hermes -p coding-engineer

# Enterprise data platforms, Microsoft Fabric, OneLake & Synapse Spark
hermes -p fabric-engineer

# Stealth web crawling, Scrapling, and anti-bot bypassing
hermes -p web-scraping-specialist

# Context distillation, Trim-1 context pruning & TOON token compression
hermes -p token-optimizer

# Agile Kanban decomposition & technical product management
hermes -p product-manager
```

#### 2. Invoking Specialist Personas (from Agent Library)
Over 415 structured persona markdown documents reside in `/home/predictatrade/.hermes/agent-library/`:
- **Specialist Personas**: Located in `specialist-agents/` (e.g., `codegraph-intelligence.md`, `pentagi-pentest.md`, `rea-reverse-engineering.md`, `mirofish-swarm.md`, `autoagent-autonomous.md`, `mempalace-memory.md`, `translation-localization.md`, `cactus-quant.md`, `laya-command-center.md`).
- **Agency Personas**: 329 personas in `agency-agents/` across Engineering, Design, Academic Research, and Marketing.

**Usage Methods**:
```bash
# Method A: Launch Hermes with a specialist persona prompt
hermes --prompt "$(cat /home/predictatrade/.hermes/agent-library/specialist-agents/codegraph-intelligence.md)"

# Method B: Search personas via hermes-vault CLI
hermes-vault agents pentagi
hermes-vault agents reverse-engineering

# Method C: Query persona prompts directly via SQLite
sqlite3 /root/hermes-vault.sqlite "SELECT system_prompt FROM agent_personas WHERE name='pentagi-pentest';"
```

#### 3. Multi-Agent Kanban Task Decomposition
Hermes includes a built-in SQLite Kanban board (`/home/predictatrade/.hermes/kanban.db`):
```bash
# Add tasks assigned to specific specialist agents
hermes -p default kanban task add "Audit Vault.sol for reentrancy" --agent security-audit
hermes -p default kanban task add "Build MQL5 bridge to Redis" --agent metatrader-quant

# List active Kanban board status
hermes -p default kanban list
```

---

### C. How to Use MCP (Model Context Protocol) Servers

#### 1. Recommended Production Servers (30 Pre-Configured Servers)
The 30 curated production MCP servers are stored in `/home/predictatrade/.hermes/mcp-library/recommended-mcp-servers.json`:
- `filesystem`, `memory`, `git`, `docker`, `sqlite`, `postgres`, `redis`, `timescaledb`, `questdb`
- `codegraph`, `mcptoon`, `mempalace`, `rea`, `laya`
- `puppeteer`, `playwright`, `fetch`, `brave-search`, `scrapling-crawler`, `deer-flow`, `2captcha`
- `metatrader5`, `tradingview-signals`, `microsoft-fabric`, `telegram-bot`, `discord`, `whatsapp-wassenger`

#### 2. Configuring MCP Servers in Hermes
MCP servers are defined in `/home/predictatrade/.hermes/config.yaml` (or profile `config.yaml`).
Example configuration:
```yaml
mcp_servers:
  codegraph:
    command: codegraph
    args: ["serve"]
  mcptoon:
    command: mcptoon
    args: ["serve"]
  mempalace:
    command: mempalace-mcp
    args: []
  filesystem:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/srv/predictatrade"]
  sqlite:
    command: uvx
    args: ["mcp-server-sqlite", "--db-path", "/home/predictatrade/.hermes/hermes-vault.sqlite"]
```

#### 3. Using MCP Servers Directly from CLI
Each MCP engine can also be used directly as a standalone CLI tool in scripts or the terminal:
```bash
# CodeGraph: Generate AST knowledge graph and impact search
codegraph index /srv/predictatrade/my-project
codegraph search "handleOrderExecution"

# MCPToon: Compress JSON/MCP payloads by 99.2%
mcptoon --input tool_response.json

# MemPalace: Holographic AI memory retrieval
mempalace search "arbitrage strategy rules"

# REA: Binary reverse engineering & disassembly
rea analyze /usr/local/bin/trim

# Trim-1: Rapid line-level context pruning
trim --query "database connection pooling" config.yaml
```

---

### D. How to Use PLUGINS (24 Active Plugins)

#### 1. Managing Plugins
```bash
# List all installed plugins and their status
hermes -p default plugins list

# Enable specific plugins
hermes -p default plugins enable superpowers
hermes -p default plugins enable token-saver
hermes -p default plugins enable security-guidance
hermes -p default plugins enable disk-cleanup
hermes -p default plugins enable mirofish
hermes -p default plugins enable openshell
```

#### 2. Key Plugins & Their Roles During Execution
- **`superpowers`**: Enforces a strict plan-then-act workflow. Hermes decomposes complex goals into subtasks with intermediate verification steps and test verification before marking work complete.
- **`token-saver`**: Intercepts input context and tool outputs, stripping redundant whitespace and compressing logs. Check metrics via `token-saver stats`.
- **`security-guidance`**: Intercepts and validates bash commands before execution, blocking destructive root modifications, unsafe `rm -rf` patterns, and sandbox escapes.
- **`disk-cleanup`**: Periodically grooms temporary build artifacts, scrapers' browser caches, and stale Docker containers.
- **`mirofish`**: Multi-agent predictive simulation engine. Allows Hermes to simulate complex multi-agent market scenarios or user interactions before acting.
- **`openshell`**: NVIDIA's agent isolation runtime enforcing fine-grained sandbox security boundaries.

---

## 9. Self-Local Offline Installer & SQLite Knowledge Vault

### A. Backup Strategy Clarification: Do I need both files?
- **Original Files**: `hermes-agent-production.sh` previously bundled `hermes-assets.tar.gz` as an embedded base64 payload. However, running that script on a brand new, separate device would still attempt to fetch from GitHub (cloning Hermes core, downloading `uv`, downloading pip wheels, and querying community Git repos).
- **The Self-Local Solution**: To eliminate all external internet and GitHub dependencies when deploying on other devices, two clean backup options are provided:

1. **Option 1: Complete Offline Standalone Installer (`hermes-self-contained-installer.tar.gz`, 1.4 GB)**:
   - **File**: `/root/hermes-self-contained-installer.tar.gz` (SHA-256: `39d3ae500da3ab94c1af6c63e4c93cf067952dd59dd4108d1adf95fe4387d5f3`)
   - **Contents**:
     - `install-hermes-local.sh`: 100% offline shell installer with zero GitHub/pip/npm calls.
     - `hermes-vault.sqlite`: Unified SQLite database (75 MB).
     - `hermes-engines.tar.gz`: Pre-compiled binaries and site-packages for all 16 engines (107 MB).
     - `hermes-agent-core.tar.gz`: Pre-built Hermes Agent core engine (`4ed093c`) with all node_modules (333 MB).
     - `hermes-system-assets.tar.gz`: 1,688 skills, 43,000+ community skills, MCP universe, and tools runtime (976 MB).
   - **Deployment to another device**:
     ```bash
     scp /root/hermes-self-contained-installer.tar.gz root@new-server:/root/
     cd /root && tar -xzf hermes-self-contained-installer.tar.gz
     cd hermes-self-contained-installer && sudo bash install-hermes-local.sh
     ```
     Installs and verifies in under **30 seconds** without touching GitHub or the internet.

2. **Option 2: Single-File SQLite Knowledge Vault (`hermes-vault.sqlite`, 75 MB)**:
   - **File**: `/root/hermes-vault.sqlite` (and `/home/predictatrade/.hermes/hermes-vault.sqlite`)
   - **Contents**:
     - `curated_skills`: All 1,688 skills with complete markdown text and YAML headers.
     - `community_skills`: 43,370 indexed community packages with triage classifications and star counts.
     - `mcp_servers`: 4,859 cataloged MCP servers + 30 curated production servers.
     - `agent_personas`: 415 agent persona definitions with full markdown prompts.
     - `profiles`: 42 specialist profile configurations.
     - `plugins`: 24 active plugins.
     - `engines`: 17 extended AI/reverse-engineering/quant engines.
   - **Use case**: Lightweight, portable backup to cloud storage or USB stick for preserving all ecosystem metadata and knowledge.

### B. SQLite Vault CLI (`hermes-vault`)

The system provides `/usr/local/bin/hermes-vault` for querying the SQLite database:
```bash
# View ecosystem metadata & total inventory counts
hermes-vault stats

# Search curated skills (by query or category)
hermes-vault skills quant
hermes-vault skills --category quant-trading

# Search community skills pool (43,000+ packages)
hermes-vault community scrapfly

# List recommended production MCP servers
hermes-vault mcp --recommended

# Search agent personas (415+ personas)
hermes-vault agents financial

# Inspect the 16 pre-compiled extended engines
hermes-vault engines
```

---

## 10. Maintenance & Operations

### Fast Validation Check
To verify complete system health without modifying files:
```bash
bash /root/hermes-agent-production.sh --validate-only
# Or using the local installer:
bash /root/hermes-self-contained-installer/install-hermes-local.sh --validate-only
```

### Full Re-installation / Update
To re-run the production installation with all assets, security checks, and rootless docker verification:
```bash
bash /root/hermes-agent-production.sh --skip-sync
```

### Advanced Options
```bash
# Force re-download / re-sync of community repositories (takes ~1h)
bash /root/hermes-agent-production.sh --force-sync

# Force clean reinstall of Hermes core engine and tools
bash /root/hermes-agent-production.sh --force-reinstall

# Skip refreshing public catalogs (instant setup using cached collections)
bash /root/hermes-agent-production.sh --skip-sync
```

### Inspect Rootless Docker Status
```bash
runuser -u predictatrade -- env XDG_RUNTIME_DIR=/run/user/1001 systemctl --user status docker
```

---

## 11. Hybrid Vector Registry & Dynamic Execution Architecture (`hermes-registry`)

To prevent agent context degradation and disk bloat (eliminating 12+ GB of redundant copies across 66 specialist profiles), Hermes features a **Hybrid Vector Registry & Dynamic Just-In-Time (JIT) Execution Engine**:

```
                                USER NATURAL LANGUAGE INTENT
                                              │
                      ┌───────────────────────┴───────────────────────┐
                      ▼                                               ▼
         [SQLite FTS5 Full-Text Engine]                  [ChromaDB Dense Vector Store]
         • Exact keywords, tools, tags                   • Semantic conceptual similarity
         • Sub-10ms BM25 ranking                         • Local ONNX all-MiniLM-L6-v2 embeddings
         • 19,691 Curated Skills                         • 19,691 Skills + 480 Personas + 66 Profiles
                      │                                               │
                      └───────────────────────┬───────────────────────┘
                                              ▼
                                 [Reciprocal Rank Fusion]
                                              ▼
                         [Top Ranked Tools & Persona Match]
                                              │
                          ┌───────────────────┴───────────────────┐
                          ▼                                       ▼
             [JIT Dynamic Activation]                 [Zero-Bloat Context Eviction]
        `hermes-registry activate <skill>`       `hermes-registry deactivate <skill>`
         Symlinks tool into active context         Evicts symlink when goal finishes
```

### Key CLI Capabilities:
- **Registry Statistics**:
  ```bash
  hermes-registry stats
  ```
  Reports counts and storage footprint across SQLite (relational + FTS5 BM25) and ChromaDB (vector embeddings).

- **Natural Language Intent Resolution**:
  ```bash
  hermes-registry resolve "audit solana smart contract reentrancy and token bonding curves"
  ```
  Instantly performs dual-stage ranking:
  1. Dense semantic matching via ChromaDB (`skills_semantic`, `profiles_semantic`, `mcp_semantic`, `plugins_semantic`).
  2. Sparse keyword matching via SQLite FTS5 (`curated_skills_fts`).
  3. Outputs recommended specialist profile, enterprise plugins, MCP engines, and ranked skills.

- **Dynamic JIT Activation & Eviction**:
  ```bash
  # Dynamically link a skill into the active profile
  hermes-registry activate audit-reentrancy --profile default

  # Evict skill when task finishes to keep agent context clean
  hermes-registry deactivate audit-reentrancy --profile default
  ```

- **Option A: Pure Content Vault Release (`hermes-content-vault-v1.1.0.tar.gz`)**:
  - Contains SQLite FTS5 database (`hermes-vault.sqlite`), ChromaDB pre-computed vector embeddings (`vector-registry`), manifests, and CLI utilities (151 MB compressed).
  - Packaged via `bash /srv/hermes-installer/package-content-vault.sh`.
  - Zero binary bloat: 100% portable across machines without large runtimes or C/Rust binaries.

---

## 12. Verification Checklist & Health Status

| Component | Status | Verification Details |
|---|---|---|
| Dedicated Service User | **PASSED** | `predictatrade` (UID: 1001), strict isolation from `docker`, `sudo`, `adm` |
| Rootless Docker | **PASSED** | Cgroup v2 active, socket `unix:///run/user/1001/docker.sock`, `hello-world` OK |
| Desktop Sandbox Image | **PASSED** | `nousresearch/hermes-sandbox:desktop` (4.4 GB) cached and verified |
| Hermes Agent Engine | **PASSED** | `v0.21.5+5853.g4ed093c`, audio-io extension compiled, config check passed |
| Curated Skill Library | **PASSED** | 19,691 skills across 52 categories (`hermes-skill-catalog` active) |
| Community Skill Pool | **PASSED** | 64,687 packages cataloged with security triage |
| Agent Library & Profiles | **PASSED** | 480 agent personas + 66 specialist profiles with Kanban initialized |
| MCP Universe Catalog | **PASSED** | 4,837 servers indexed + 45 recommended production configurations |
| 17 Extended AI Engines | **PASSED** | All binaries, libraries, and Python modules verified under user `predictatrade` |
| Active Plugins | **PASSED** | 32 active enterprise plugins including `agentic-flow`, `geo-optimizer`, `openfactcheck`, `ai-governance`, `contract-lifecycle`, `gtm-engine`, `mcptoon`, `codegraph`, `mempalace`, `rea`, `openshell` |
| SQLite Knowledge Vault | **PASSED** | `hermes-vault.sqlite` (301 MB with FTS5 BM25 index & triggers) |
| ChromaDB Vector Registry | **PASSED** | `/home/predictatrade/.hermes/vector-registry` (69 MB, all 19,691 skills + 480 personas + 66 profiles + 45 MCPs + 32 plugins) |
| Dynamic JIT Registry CLI | **PASSED** | `/usr/local/bin/hermes-registry` (hybrid resolve, activate, deactivate, stats) |
| Option A Content Vault | **PASSED** | `hermes-content-vault-v1.1.0.tar.gz` (151 MB) in `dist/` verified with SHA-256 |
| Self-Local Full Installer | **PASSED** | `hermes-self-contained-installer.tar.gz` (1.4 GB) 100% offline verified |
| Helper CLI Binaries | **PASSED** | All multi-user binaries in `/usr/local/bin` dropping root privileges safely |
