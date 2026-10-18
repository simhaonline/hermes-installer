# Hermes Agent Enterprise Edition: Global Rulebook & Governance Protocols
**Platform**: platform.predictatrade.com (Ubuntu Linux LTS)  
**Standard**: Swiss Institutional Bullion Standard (simharefinery.com & Predict-A-Trade)  
**Version**: 1.0.0 Enterprise Production  
**Last Updated**: 2026-10-18  

---

## Table of Contents
1. [Protocol 1: Platform Security Boundaries & User Isolation](#protocol-1-platform-security-boundaries--user-isolation)
2. [Protocol 2: AI CLI Operational Standards & Ecosystem Workflows](#protocol-2-ai-cli-operational-standards--ecosystem-workflows)
3. [Protocol 3: Specialist Agent Personas & Swarm Architecture](#protocol-3-specialist-agent-personas--swarm-architecture)
4. [Protocol 4: Specialist Runtime Profiles & JIT Context Injection](#protocol-4-specialist-runtime-profiles--jit-context-injection)
5. [Protocol 5: Model Context Protocol (MCP) Universe & Tool Sandboxing](#protocol-5-model-context-protocol-mcp-universe--tool-sandboxing)
6. [Protocol 6: Pre-Compiled High-Performance Ecosystem Engines](#protocol-6-pre-compiled-high-performance-ecosystem-engines)
7. [Protocol 7: UI/UX Swiss Institutional Bullion Design Standard](#protocol-7-uiux-swiss-institutional-bullion-design-standard)
8. [Protocol 8: Development, Packaging & Repository Discipline](#protocol-8-development-packaging--repository-discipline)

---

## Protocol 1: Platform Security Boundaries & User Isolation

> [!SECURITY]
> Strict privilege separation is mandatory across all execution layers. Root account execution of agent workloads or untrusted code is categorically prohibited.

### 1.1 Dedicated Service Accounts
* **`predictatrade` (`UID=1001`, `GID=1001`)**:
  * Dedicated runtime service account for the active Hermes Agent.
  * Runtime Home: `/home/predictatrade` (contains `.hermes/`, `hermes-vault.sqlite`, `profiles/`, `agent-library/`, `skills/`, `skill-library/`, `chromadb/`).
  * Rootless Docker Daemon: `unix:///run/user/1001/docker.sock`.
  * All autonomous agent execution loops, tool calls, and model inference runners must run strictly under this account.
* **`hermes-installer` (`UID=1002`, `GID=1002`)**:
  * Dedicated developer account for maintaining, packaging, and building the installer repository.
  * Workspace Directory: `/srv/hermes-installer`.
  * All files in `/srv/hermes-installer` must always remain owned by `hermes-installer:hermes-installer`.
* **Platform Infrastructure (Rootful Docker)**:
  * Standard host Docker daemon on `/var/run/docker.sock` is reserved exclusively for platform infrastructure (PostgreSQL, QuestDB, reverse proxies).

### 1.2 Automated Privilege Dropping
* All system-wide CLI binaries located in `/usr/local/bin` (`hermes`, `hermes-vault`, `hermes-registry`, `hermes-rulebook`, `hermes-skill-catalog`, `hermes-community-skills`, `hermes-mcp-universe`, `codegraph`, `mcptoon`, `trim`, `mempalace`, `rea`, `pentagi`, `auto`) must automatically drop privileges to user `predictatrade` (`UID=1001`) when invoked by `root` unless explicitly instructed otherwise.

### 1.3 Zero Root Contamination Policy
* Never store tarballs, sqlite databases, or temporary build artifacts in `/root`.
* Scratch files and intermediate data must be placed in designated project directories or `/home/predictatrade/.hermes/cache/`.

---

## Protocol 2: AI CLI Operational Standards & Ecosystem Workflows

> [!IMPORTANT]
> Always verify CLI exit codes and validate tool availability before initiating long-running workflows.

### 2.1 Primary Agent CLI (`hermes`)
The central execution interface for the Hermes Agent suite:
```bash
# 1. Interactive Terminal UI
hermes

# 2. Execute with Specialist Profile Context
hermes -p <profile_name>

# 3. Headless / Batch Task Execution
hermes run --query "<task_description>" -p <profile_name>

# 4. Automated Autonomous Execution (Continuous loop with auto-approval)
hermes agent -q "<prompt>" --auto-approve
```

### 2.2 Knowledge Vault Engine (`hermes-vault`)
Sub-millisecond SQLite FTS5 queries against `/home/predictatrade/.hermes/hermes-vault.sqlite` (304.03 MB database):
```bash
# Display full system ledger telemetry and component inventory
hermes-vault stats

# Search 19,840 curated production skills
hermes-vault skills "<search_term>" [--category <cat>] [--limit 30]

# Search 64,687 community pool skills
hermes-vault community "<search_term>" [--limit 25]

# Search 554 specialist agent personas
hermes-vault agents "<search_term>" [--limit 30]

# Search 66 runtime configuration profiles
hermes-vault profiles "<search_term>"

# Search 4,842 MCP servers & curated tools
hermes-vault mcp "<search_term>" [--recommended]

# List native high-performance engines
hermes-vault engines

# Display or search this Rulebook
hermes-vault rulebook [protocol_number]
```

### 2.3 Hybrid Vector Registry Service (`hermes-registry`)
Systemd Service: `hermes-registry.service` running on `http://0.0.0.0:8998`:
```bash
# Hybrid FTS5 + ChromaDB semantic skill search
hermes-registry search "<natural_language_intent>" --limit 20

# Dynamically activate/symlink a skill into the active profile
hermes-registry activate <skill_name> [--profile <target_profile>]

# Evict a skill from active profile
hermes-registry deactivate <skill_name> [--profile <target_profile>]

# Check systemd daemon status
systemctl status hermes-registry.service

# View interactive terminal Rulebook
hermes-rulebook [--search <query>] [--protocol <1-8>]
```

---

## Protocol 3: Specialist Agent Personas & Swarm Architecture

> [!NOTE]
> The platform deploys **554 Specialist Agent Personas** categorized across **8 Core Enterprise Divisions**. Multi-agent workflows must follow strict Kanban handoff protocols.

### 3.1 Division Distribution & Personas
| Division | Persona Count | Primary Focus & Domain Specialties |
| :--- | :---: | :--- |
| **Software Engineering & Optimization** | 300 | AST refactor, compiler optimization, Rust/Go/C++ native systems, microservices, API scaffolding, memory leak profiling |
| **Security Auditing & Penetration Testing** | 72 | Smart contract audit, reverse engineering, red-team adversary, cloud IAM audit, binary forensics, threat modeling |
| **Product Strategy & Executive Leadership** | 68 | GTM orchestration, SaaS financial modeling, PRD creation, enterprise pricing, board communication, executive memos |
| **Quantitative Finance & Algorithmic Trading** | 57 | MetaTrader quant, portfolio risk manager, order book microstructure, options volatility surface, multi-asset backtester |
| **Data Engineering & MLOps** | 19 | Vector embeddings architect, Ray/Spark data pipelines, model registry governor, drift forensics, feature store |
| **Full-Stack & Cloud Architecture** | 17 | Distributed systems architect, database scaling engineer, Kubernetes cluster orchestrator, gRPC specialist |
| **Autonomous Research & Synthesis** | 13 | Scientific paper reader, mathematical proof validator, patent intelligence researcher, literature graph builder |
| **DevOps & SRE Reliability** | 8 | Zero-downtime deployer, Prometheus/Grafana observability engineer, chaos test runner, incident commander |

### 3.2 Swarm Orchestration & Kanban Execution Protocols
Multi-agent collaboration is tracked in `/home/predictatrade/.hermes/kanban.db` following a 4-stage pipeline:
1. **Decomposition**: Orchestrator Persona analyzes requirement and generates isolated, atomic work packets.
2. **Delegation**: Work packets are routed to specialist personas loaded with tailored profile contexts.
3. **Verification Gate**: Deliverables must pass automated verification (test suites, lint, PRAGMA checks) before status change.
4. **Evidence Ledger**: Completed tickets record exact code diffs, logs, and benchmark proofs into the immutable ledger.

---

## Protocol 4: Specialist Runtime Profiles & JIT Context Injection

> [!IMPORTANT]
> Profiles dynamically alter agent capabilities, tools, and prompts without code recompilation.

### 4.1 Profile Architecture
All 66 profiles are located in `/home/predictatrade/.hermes/profiles/<profile_name>/`. Each profile contains:
* `config.json`: Model configuration, temperature, max context tokens, and system prompt override.
* `.agents/skills/`: Symlinked active tools drawn from `/home/predictatrade/.hermes/skill-library/`.

### 4.2 Just-In-Time (JIT) Context Injection
Switching profiles instantly modifies the toolset exposed to the LLM agent:
```bash
# Switch active profile via CLI
hermes -p quantitative-finance-specialist

# Switch active profile via Registry REST API
curl -X POST http://localhost:8998/api/profiles/active -H "Content-Type: application/json" -d '{"profile": "agentic-search-optimizer"}'
```

### 4.3 Active Target Profile Rule
* All runtime modifications, tool audits, and benchmark evaluations must verify compatibility against the active target profile (currently `agentic-search-optimizer`).

---

## Protocol 5: Model Context Protocol (MCP) Universe & Tool Sandboxing

> [!SECURITY]
> All 4,842 MCP servers indexed in SQLite must adhere to strict sandboxing, authentication, and execution lifetimes.

### 5.1 Universe Scale & Curated Suite
* **Indexed Universe**: 4,842 community and enterprise MCP servers.
* **Production Curated Suite**: 45 hardened MCP servers configured for instant runtime use:
  * Database & Storage: `postgres`, `questdb`, `filesystem`, `memory`, `chromadb`
  * Web & Automation: `brave-search`, `puppeteer`, `playwright`, `browserbase`
  * Reverse Engineering: `rea`, `cutter`, `frida`, `gdb`
  * Knowledge & AST: `codegraph`, `mempalace`, `mcptoon`
  * Enterprise Plugins: 35 verified plugins in `/home/predictatrade/.hermes/plugins/`

### 5.2 MCP Sandboxing & Execution Rules
1. **User Isolation**: MCP servers must run as user `predictatrade` or in rootless Docker containers.
2. **Process Teardown**: Stdio transport subprocesses must be terminated cleanly upon session completion.
3. **Network & Proxy**: External network calls must use authenticated proxies with exponential backoff and rate-limit handling.
4. **Token Hygiene**: Never pass raw credentials in command arguments or environment logs.

---

## Protocol 6: Pre-Compiled High-Performance Ecosystem Engines

> [!TIP]
> Always leverage native pre-compiled binaries over generic interpreted scripts for high-volume tasks.

| Engine Binary | Location | Primary Purpose & Performance Advantage |
| :--- | :--- | :--- |
| **`mcptoon`** | `/usr/local/bin/mcptoon` | Zero-dependency tool payload compressor. Converts verbose JSON schemas to TOON format, saving up to 99.2% tokens before context insertion. |
| **`codegraph`** | `/usr/local/bin/codegraph` | AST knowledge graph parser and caller/callee impact traversal (`codegraph index <dir>`, `codegraph search <sym>`). |
| **`trim` / `trim-1`** | `/usr/local/bin/trim` | Ultra-fast compiled context trimmer to extract prompt-relevant lines from large code files. |
| **`mempalace`** | `/usr/local/bin/mempalace` | Holographic AI memory retrieval using AAAK dialect (`mempalace search <query>`). |
| **`rea`** | `/usr/local/bin/rea` | Native binary disassembly, decompilation, and reverse engineering (ELF, Mach-O, PE). |
| **`pentagi`** | `/usr/local/bin/pentagi` | Autonomous penetration testing backend with automated vulnerability verification. |
| **`auto`** | `/usr/local/bin/auto` | Autonomous self-healing execution loop with real-time error recovery. |
| **`ChromaDB`** | Local Vector Store | 5 Semantic collections: `skills_semantic`, `agents_semantic`, `profiles_semantic`, `mcp_semantic`, `plugins_semantic`. |

---

## Protocol 7: UI/UX Swiss Institutional Bullion Design Standard

> [!NOTE]
> All dashboards, web surfaces, and visual artifacts must strictly follow the Swiss Institutional Bullion Standard (simharefinery.com & Predict-A-Trade).

### 7.1 Palette Hierarchy
* **Sovereign Navy**:
  * Deepest Navy: `#071324` (Header, sidebar background, terminal panels)
  * Primary Navy: `#0C1E36` (Card headers, modal headers, elevated layers)
  * Surface Navy: `#142844` (Card borders, table headers, hover accents)
* **Bullion Gold**: `#D4AF37` (Luxury accent, primary borders, active navigation badges, focus rings)
* **Institutional Emerald**: `#15803D` (Live operational status, PRAGMA OK, active profile pills)
* **Daylight Mode Canvas**:
  * Paper Background: `#FBFBFC` (Warm luxury paper background)
  * Pure White Elevated: `#FFFFFF` (Surface cards, table rows)
  * Hairline Borders: `#E5E9F0` (Structural dividers)

### 7.2 Typography Rules
* **Display / Serifs**: `'Cormorant Garamond', Garamond, Georgia, serif` (Hero titles, modal section titles)
* **Interface / Sans**: `'Plus Jakarta Sans', -apple-system, sans-serif` (Body text, buttons, table data)
* **Technical / Monospace**: `'IBM Plex Mono', 'SF Mono', monospace` (Code snippets, hashes, ports, paths)

### 7.3 Zero-Slop Standard
* **Balanced Grids**: Never leave orphaned cards in KPI grids. Always enforce balanced responsive grid columns.
* **No Muddy Tints**: Never use raw yellow/olive tones (`#FBBA03` or `rgba(136,189,49)`).
* **High Contrast**: Ensure WCAG AAA contrast across all text elements in both dark and daylight themes.

---

## Protocol 8: Development, Packaging & Repository Discipline

> [!IMPORTANT]
> All work in `/srv/hermes-installer` must maintain rigorous git hygiene and verified checksums.

### 8.1 Workspace Ownership & Permissions
* Every file created or edited within `/srv/hermes-installer` must be owned by `hermes-installer:hermes-installer`.
* Execution commands must be executed using:
  ```bash
  runuser -u hermes-installer -- <command>
  ```

### 8.2 Git Discipline & Asset Protection
* **No Direct Commits of Large Binaries**: `.sqlite` databases, `.tar.gz` archives, and ISOs are strictly excluded via `.gitignore`.
* **Sync Manifests**: When adding skills, profiles, or MCP servers, regenerate and verify:
  * `README.md` and `README-HERMES.md`
  * `SHA256SUMS.txt`
  * `assets/collection-manifest.json`

### 8.3 Verification Obligation
* Before declaring any ticket or task complete:
  1. Verify CLI output: `hermes-vault stats` must execute with exit code 0.
  2. Verify HTTP endpoints: `curl -s http://localhost:8998/api/stats` must return HTTP 200.
  3. Validate UI views: Confirm zero JavaScript runtime errors across all view routes.

---
*Hermes Agent Enterprise Edition • Predict-A-Trade Platform • End of Governance Rulebook*
