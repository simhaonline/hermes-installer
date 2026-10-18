# Hermes Agent Enterprise Offline Installer

[![Version](https://img.shields.io/badge/version-v0.21.5-blue.svg)](https://github.com/simhaonline/hermes-installer/releases)
[![Offline](https://img.shields.io/badge/deployment-100%25_offline-green.svg)](https://github.com/simhaonline/hermes-installer/releases)
[![Skills](https://img.shields.io/badge/curated_skills-19%2C691-brightgreen.svg)](https://github.com/simhaonline/hermes-installer)
[![Community Pool](https://img.shields.io/badge/community_pool-64%2C687-purple.svg)](https://github.com/simhaonline/hermes-installer)
[![Profiles](https://img.shields.io/badge/specialist_profiles-66-orange.svg)](https://github.com/simhaonline/hermes-installer)
[![MCP Servers](https://img.shields.io/badge/mcp_servers-4%2C837-yellow.svg)](https://github.com/simhaonline/hermes-installer)
[![Plugins](https://img.shields.io/badge/plugins-32-blueviolet.svg)](https://github.com/simhaonline/hermes-installer)
[![Platform](https://img.shields.io/badge/platform-Ubuntu_LTS-blue.svg)](https://ubuntu.com)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)

A complete, self-contained, offline production installer for **Hermes Agent** with **17 advanced AI, engineering, and reverse engineering engines**, **19,691 curated skills across 52 categories**, **64,687 indexed community skills**, **4,837 MCP servers (45 curated production servers)**, **480 agent personas**, **66 specialist profiles**, and **32 active plugins**.

---

## 🚀 Quick Start (1-Line Install)

To install on any clean Ubuntu LTS machine (22.04 / 24.04 / 26.04):

```bash
curl -fsSL https://raw.githubusercontent.com/simhaonline/hermes-installer/main/quick-install.sh | bash
```

---

## 📦 Release Downloads (Option A: Pure Content Vault)

Download the pre-built content vault archive directly from [**GitHub Releases v1.0.0**](https://github.com/simhaonline/hermes-installer/releases/tag/v1.0.0):

| Release Asset | Size | SHA-256 Checksum | Description |
|---|---|---|---|
| [**`hermes-content-vault-v1.0.0.tar.gz`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-content-vault-v1.0.0.tar.gz) | **151 MB** | `31c1e1aad8e36055a422bbcb76d3109fa6603dd72ad23276448cc0b055ff2b6a` | **Option A Pure Content & Vector Vault**: Standalone lightweight release containing SQLite FTS5 database, ChromaDB dense vector embeddings, manifests, and dynamic execution tools (Zero binary bloat). |
| [**`hermes-vault.sqlite`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-vault.sqlite) | **301 MB** | `d3316c93a4f9164afff005bd83b78715bbe02ebe716015830764b0bb915489a0` | **SQLite Knowledge Vault**: Master database with FTS5 BM25 search tables, auto-sync triggers, and relational schemas. |
| [**`hermes-agent-production.sh`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-agent-production.sh) | **181 MB** | `38c190fb7711f9f7f7940a3201c829ccc332faf5772e6490db8e919d1fc96860` | Production deployment script with embedded base64 payload. |
| [**`hermes-assets.tar.gz`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-assets.tar.gz) | **134 MB** | `ce989e1e3b81d2e8b5aa640d5c9c874983d6236607162d0504048088e96157da` | Core asset tarball. |
| [**`SHA256SUMS.txt`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/SHA256SUMS.txt) | Text | See SHA256SUMS.txt | Cryptographic integrity verification file. |

---

## ⚙️ Deploying Content Vault on Any Hermes Machine

To unpack the complete 19.6k+ skill registry and vector index onto any server running Hermes:

```bash
# 1. Extract the lightweight content archive
tar -xzf hermes-content-vault-v1.0.0.tar.gz

# 2. Inspect hybrid registry stats (relational + ChromaDB vectors)
./hermes-registry stats

# 3. Dynamically resolve skills from natural language intent
./hermes-registry resolve "audit smart contract reentrancy"

# 4. Activate skills on-demand without duplicating files
./hermes-registry activate audit-reentrancy --profile default
```

*100% portable, zero binary bloat, and zero external embedding API costs.*

---

## 🛡️ Security Architecture: Root vs. `predictatrade` User

### Dedicated Service Account Isolation
- Hermes executes strictly as the dedicated non-root user `predictatrade` (`UID=1001`).
- Strictly prohibited from privileged groups (`docker`, `sudo`, `adm`), preventing host privilege escalation.
- Primary project workspace resides in `/srv/predictatrade` (`0750` permissions owned by `predictatrade:predictatrade`).

### Dual Docker Daemon Architecture
- **Host Standard Docker**: Remains unaltered on `/var/run/docker.sock` for system services.
- **Hermes Rootless Docker**: Operates on `unix:///run/user/1001/docker.sock` without sudo, isolated via user namespaces and AppArmor.
- Containers can be run, built, and composed directly by `predictatrade` without `sudo`.

### Automatic Privilege Dropping
All CLI tools in `/usr/local/bin` (`hermes`, `hermes-vault`, `hermes-skill-catalog`, `codegraph`, `mcptoon`, `trim`, `mempalace`, `rea`, `auto`, `pentagi`) automatically drop privileges to `predictatrade` when run from root. You can execute commands as `root` from any terminal, and they run safely in user space.

---

## 🧰 The 16 Integrated Advanced Engines

| # | Engine | Technology | CLI / Binary | Capabilities |
|---|---|---|---|---|
| 1 | **MCPToon** | Python / CLI | `mcptoon` | Zero-dependency MCP gateway & 99.2% token context compression CLI. |
| 2 | **CodeGraph** | TypeScript / WASM | `codegraph` | Pre-indexed AST knowledge graph, callers/callees impact traversal. |
| 3 | **MemPalace** | Python / ChromaDB | `mempalace`, `mempalace-mcp` | Local-first AI memory system with ChromaDB backend and AAAK dialect. |
| 4 | **REA** | Node.js / CLI | `rea`, `rea-agents` | Universal binary reverse engineering, static analysis & decompilation. |
| 5 | **MiroFish** | Python / Plugin | `plugins/mirofish` | Universal swarm intelligence and predictive multi-agent simulation engine. |
| 6 | **NVIDIA OpenShell** | Rust / Python | `openshell` | Sandboxed policy enforcement and private agent execution runtime. |
| 7 | **AutoAgent** | Python / CLI | `auto` | Zero-code autonomous LLM agent execution framework. |
| 8 | **Trim-1** | Go Binary | `trim`, `trim-1` | Ultra-fast compiled model for line-level context trimming. |
| 9 | **Cactus Compute** | Python / C++ | `cactus` | Low-latency edge inference runtime and quantization kernels. |
| 10 | **PentAGI** | Go Binary | `pentagi` | Autonomous penetration testing and security auditing agent system. |
| 11 | **Laya** | Python / MCP | `laya` | Local-first AI notification command center (Slack, Gmail, GitHub, Jira). |
| 12-16 | **Skill Suites** | Markdown / Code | `skill-library` | Product localization (23 skills), multi-agent translation with terminology verification, translation file sync, book translation, and skills curriculum. |

---

## 📊 Ecosystem Inventory

- **Skills Library**: **19,691 Curated Skills across 52 Categories** + **64,687 Community Skill Packages** (including GEO/SEO optimization, social media automation, deep learning/NLP recipes, computer vision with Roboflow, MLOps, fact-checking, AI governance, CLM contracts, and GTM sales).
- **Agent Library**: **480 Personas** (Specialist, Agency, Quant Trading, Security, System Engineering, Legal, and Governance).
- **Specialist Profiles**: **66 Pre-configured Profiles** (including `geo-search-specialist`, `social-media-strategist`, `gtm-sales-engineer`, `mlops-platform-engineer`, `computer-vision-engineer`, `fact-checking-analyst`, `ai-governance-officer`, `executive-c-suite-advisor`, `hr-talent-operations`, `legal-clm-specialist`, `supply-chain-architect`, `deep-learning-researcher`, `mathematics-ai`, `office-excel-pdf`, `nginx-caddy-infrastructure`, `astro-web-architect`, `minimax-voice-agent`, `kimi-reasoning-specialist`, `manus-autonomous-agent`, `workbuddy-enterprise`, `tencent-cloud-architect`, `laravel-architect`, `seo-growth-marketer`, `foundation-agent`).
- **MCP Servers**: **4,837 Cataloged Servers** + **45 Curated Production Servers** (`recommended-mcp-servers.json` including `geo-search-mcp`, `social-media-mcp`, `openfactcheck-mcp`, `roboflow-vision-mcp`, `huggingface-mcp`, `legal-clm-mcp`, `supplychain-mcp`, `gtm-sales-mcp`, `ai-guardrails-mcp`, `document-specialist-mcp`).
- **Plugins**: **32 Active Plugins** (including `agentic-flow`, `geo-optimizer`, `openfactcheck`, `ai-governance`, `contract-lifecycle`, `gtm-engine`, `superpowers`, `token-saver`, `security-guidance`, `disk-cleanup`, `manus-research`, `wookstar-plugins`, `mirofish`, `openshell`).
- **Knowledge Vault**: **233 MB SQLite Database** (`hermes-vault.sqlite`) storing full definitions, metadata, and markdown text.
- **Built-in Python Libraries**: `openpyxl`, `xlsxwriter`, `pdfminer.six` pre-installed for immediate Excel/PDF processing.

---

## 🔍 SQLite Knowledge Vault CLI (`hermes-vault`)

The installer deploys `/usr/local/bin/hermes-vault` for instant querying:

```bash
# View system metadata and ecosystem inventory
hermes-vault stats

# Search curated skills by query or category
hermes-vault skills geo
hermes-vault skills --category geo-search-optimization

# Search community skills pool (64,680+ packages)
hermes-vault community "fact-check"

# List recommended production MCP servers (45 servers)
hermes-vault mcp --recommended

# Search agent personas (480 personas)
hermes-vault agents "computer vision"

# Inspect the 17 pre-compiled extended engines
hermes-vault engines
```

---

## ⚡ Hybrid Vector Registry & Dynamic JIT Execution CLI (`hermes-registry`)

Hermes provides dynamic on-demand tool resolution and execution via `/usr/local/bin/hermes-registry`, eliminating profile disk duplication:

```bash
# View combined relational (SQLite) and vector (ChromaDB) statistics
hermes-registry stats

# Natural language intent resolution (Hybrid Dense ChromaDB + Sparse SQLite FTS5)
hermes-registry resolve "audit solana smart contract reentrancy and token bonding curves"

# Dynamically link a resolved tool into the active profile
hermes-registry activate audit-reentrancy --profile default

# Cleanly evict the tool from profile context when task finishes
hermes-registry deactivate audit-reentrancy --profile default
```

---

## 📖 Complete Documentation

For complete architectural details, operational runbooks, and deep dive reference manuals, see:
- [**`README-HERMES.md`**](README-HERMES.md) — Comprehensive master documentation.
- [**`README-LOCAL-INSTALL.md`**](README-LOCAL-INSTALL.md) — Offline deployment manual and SQLite query reference.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
