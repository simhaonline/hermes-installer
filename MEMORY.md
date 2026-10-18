# Project Memory & Architecture Record: Hermes Installer & Ecosystem

**Project**: Hermes Agent Production Deployment & Ecosystem Installer  
**Repository**: `https://github.com/simhaonline/hermes-installer.git`  
**Workspace**: `/srv/hermes-installer`  
**Host Platform**: `platform.predictatrade.com` (Ubuntu LTS Linux)  
**Creation / Migration Date**: 2026-10-18  
**Dedicated Project User**: `hermes-installer` (`UID=1002`, `GID=1002`)  
**Hermes Service User**: `predictatrade` (`UID=1001`, `GID=1001`)  

---

## 1. Executive Summary & Purpose

This repository contains the standalone, enterprise-grade installer, local packaging pipeline, SQLite knowledge vault, and orchestration tooling for deploying and maintaining the **Hermes Agent** platform on `platform.predictatrade.com`.

All previous build artifacts, scratch files, and intermediate archives that resided in `/root` (`/root/hermes-installer` and `/root/hermes-installer-git`) have been completely cleaned up (reclaiming ~2.1 GB disk space). Development is now centralized in `/srv/hermes-installer` under the dedicated non-privileged user `hermes-installer`.

---

## 2. Inventory: Created vs. Activated Assets

A central milestone of this deployment was indexing and staging the complete Hermes AI Agent ecosystem into the SQLite Knowledge Vault (`hermes-vault.sqlite`, 232.75 MB).

### Ecosystem Inventory Table

| Component Category | Total Cataloged / Created | Activated in Hermes Runtime | Storage / Configuration Location |
| :--- | :--- | :--- | :--- |
| **Curated Skills** | **19,691 skills** across 52 categories | **412 active skills** in discovery path | `/home/predictatrade/.hermes/skills/` (live)<br>`/home/predictatrade/.hermes/skill-library/` (catalog) |
| **Community Skills** | **64,687 packages** in vault pool | Available on-demand via catalog CLI | `/home/predictatrade/.local/share/hermes-community-skill-pool/` |
| **Agent Personas** | **480 personas** across 5 divisions | 480 prompt definitions available | `/home/predictatrade/.hermes/agent-library/` |
| **Specialist Profiles** | **66 autonomous profiles** | **66 profiles active** (`hermes -p`) | `/home/predictatrade/.hermes/profiles/` |
| **MCP Servers** | **4,837 servers** in universe catalog | **45 recommended** / 0 persistent daemon | `/home/predictatrade/.hermes/mcp-library/recommended-mcp-servers.json` |
| **Plugins** | **32 enterprise plugins** | **65 enabled** (10 custom + 55 bundled) | `/home/predictatrade/.hermes/plugins/`<br>`/home/predictatrade/.hermes/config.yaml` |
| **Integrated Engines** | **17 compiled engines / suites** | Active via `/usr/local/bin` wrappers | `/usr/local/bin/` (`mcptoon`, `codegraph`, `rea`, `mempalace`, `trim-1`, etc.) |

---

## 3. Detailed Component Breakdown

### A. Skills System
1. **Curated Library (19,453 skills)**:
   - Primary categories: `foundation-skills` (13,748), `minimax-audio-voice` (1,292), `laravel-php-ecosystem` (810), `quant-trading` (553), `office-excel-pdf` (383), `custom` (317), `kimi-suite` (309), `seo-growth-marketing` (262), `manus-agent` (238), `workbuddy-suite` (193), `backend-languages` (135), `official-optional` (128), `ui-ux-design` (117), `mathematics-ai` (116), `tencent-cloud-ecosystem` (103), `community-elite` (65), `knowledge-graph` (47), etc.
2. **Community Pool (64,569 packages)**:
   - Indexed in SQLite vault table `community_skills`.
   - Searchable via CLI: `hermes-community-skills search <query>`.
3. **Activated Skills (377 skills)**:
   - Reside in `/home/predictatrade/.hermes/skills/`.
   - Includes 317 proprietary Predict-A-Trade automation skills, plus core productivity, software engineering, security, and research tools.

### B. Agent Personas & Specialist Profiles
1. **Agent Personas (462 in database / 491+ files)**:
   - **Agency Agents** (328): Fullstack Engineering, UI/UX Design, Academic Research, Copywriting, Marketing.
   - **Specialist Agents** (84): AST CodeGraph, REA Reverse Engineering, MiroFish Swarm, PentAGI Pentest, MemPalace Holographic Memory, AutoAgent, Laya Command Center, Cactus Quant.
   - **Personal AI Employee** (41): Enterprise operations, calendar triage, sprint planning.
   - **Fabric & Quantitative Specialists** (9): OneLake architects, MQL5 EA developers, PineScript strategy engineers.
2. **Specialist Profiles (54 profiles)**:
   - Configured in `/home/predictatrade/.hermes/profiles/` with isolated memory stores, session databases, SOUL prompts, and custom skill routing.
   - Key profiles: `orchestrator`, `coding-engineer`, `security-audit`, `qa-testing`, `devops-sre`, `metatrader-quant`, `fabric-engineer`, `web-scraping-specialist`, `token-optimizer`, `product-manager`.
   - Kanban task board initialized in `/home/predictatrade/.hermes/kanban.db` under `orchestrator`.

### C. MCP (Model Context Protocol) Suite
1. **Universe Catalog (4,827 servers)**:
   - Searchable via `hermes-mcp-universe search <query>`.
2. **Recommended Production Suite (35 servers)**:
   - Pre-configured in `/home/predictatrade/.hermes/mcp-library/recommended-mcp-servers.json`.
   - Core tools (`codegraph`, `mcptoon`, `mempalace-mcp`, `rea`, `trim-1`) run directly as standalone CLI utilities without idle daemon overhead.

### D. Active Plugins (26 Installed, 59 Enabled in Session)
- **26 Installed Plugins** in `/home/predictatrade/.hermes/plugins/`:
  `agent-cron`, `autoagent`, `cactus`, `codegraph`, `conda-plugins`, `deer-flow`, `fabric-plugins`, `homeassistant`, `laya`, `manus-research`, `mcptoon`, `mempalace`, `memstack`, `mirofish`, `mql5-libraries`, `open-company`, `openshell`, `pentagi`, `quantmind`, `rea`, `scrapling`, `superpowers`, `token-saver`, `tradingview-pinescript`, `trim-1`, `wookstar-plugins`.
- **4 Custom Plugins Enabled in `config.yaml`**: `disk-cleanup`, `homeassistant`, `security-guidance`, `superpowers`.
- **55 Bundled Hermes Platform/Search Plugins**: Web search engines (`tavily`, `searxng`, `brave`, `exa`, `ddgs`), headless browser engines (`browser-use`, `firecrawl`), and chat gateways (`telegram`, `discord`, `whatsapp`, `slack`, `teams`).

---

## 4. Security & User Isolation Architecture

To prevent permission crossover and privilege escalations, two distinct service accounts exist:

### 1. `predictatrade` (UID 1001, GID 1001)
- Dedicated runtime account for the running Hermes Agent.
- Home directory: `/home/predictatrade`.
- Isolated Rootless Docker daemon: `unix:///run/user/1001/docker.sock`.
- Primary operational workspace: `/srv/predictatrade`.
- All CLI binaries in `/usr/local/bin` automatically drop privileges to this user when executed from root.

### 2. `hermes-installer` (UID 1002, GID 1002)
- Dedicated development and packaging account for the installer codebase.
- Home directory: `/home/hermes-installer`.
- Workspace: `/srv/hermes-installer`.
- Subordinate UIDs/GIDs allocated: `231072:65536` in `/etc/subuid` and `/etc/subgid`.
- Owns all files within `/srv/hermes-installer`.
- Configured with Git credentials and `safe.directory`.

---

## 5. Repository Structure (`/srv/hermes-installer`)

```
/srv/hermes-installer/
├── .git/                      # Git repository (origin: simhaonline/hermes-installer.git)
├── .gitignore                 # Ignores *.tar.gz, *.sqlite, bundle/, __pycache__/
├── assets/                    # Installer configuration and metadata assets
│   ├── PROJECT_HANDOFF.md     # Architectural handoff document
│   ├── TOKEN_POLICY.md        # Token compression & budget enforcement policy
│   ├── collection-manifest.json # Curated skills category manifest
│   ├── configure.py           # Ecosystem configuration and profile generator
│   ├── official-install.sh    # Base upstream installation script
│   ├── profiles.json          # 54 specialist profiles definition
│   ├── recommended-mcp-servers.json # 35 recommended MCP servers
│   └── submitted-installer.txt# Historical installer reference
├── hermes-vault               # CLI helper for inspecting SQLite vault
├── install-hermes-local.sh    # Offline/local ecosystem installation script
├── quick-install.sh           # Minimal bootstrap script
├── README-HERMES.md           # Comprehensive enterprise documentation (582 lines)
├── README-LOCAL-INSTALL.md    # Local offline installation instructions
├── README.md                  # Project overview and quickstart guide
├── SHA256SUMS.txt             # Checksums for offline asset bundles
├── MEMORY.md                  # This session memory and state record
└── MEMORRY.md -> MEMORY.md    # Convenience symlink
```

---

## 6. Git Synchronization State

- **Remote**: `https://github.com/simhaonline/hermes-installer.git`
- **Branch**: `main`
- **Current Synced Commit**: `b303931` (*"feat: complete enterprise ecosystem with 19,453 skills, 54 profiles, 35 MCPs, 26 plugins, and 230MB SQLite vault"*)
- **Tag**: `v1.0.0`
- **Working Tree**: Clean

---

## 7. Developer Instructions for New Session

When starting the next conversation under `/srv/hermes-installer`:
1. Work directly within `/srv/hermes-installer`.
2. Git commits and pushes will use the credentials already stored for `simhaonline`.
3. To inspect the live Hermes installation at any time, run:
   ```bash
   hermes-vault stats
   hermes-skill-catalog categories
   hermes plugins list --plain
   ```
4. All files in this repository should maintain ownership `hermes-installer:hermes-installer`.
