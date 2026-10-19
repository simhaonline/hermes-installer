# Project Memory & Architecture Record: Hermes Installer & Ecosystem

**Project**: Hermes Agent Production Deployment & Ecosystem Installer  
**Repository**: `https://github.com/simhaonline/hermes-installer.git`  
**Workspace**: `/srv/hermes-installer`  
**Dedicated Project User**: `hermes-installer` (`UID=1002`, `GID=1002`)  
**Hermes Service User**: `hermes` (Isolated System Runtime)  
**Live Knowledge Vault**: `/srv/hermes-installer/hermes-vault.sqlite` (507 MB)

---

## 1. Executive Summary & Purpose

This repository contains the standalone, enterprise-grade installer, local packaging pipeline, SQLite knowledge vault, and orchestration tooling for deploying and maintaining the **Hermes Agent** platform.

The system serves as an enterprise AI Knowledge & Capability Vault housing Prompts, Skills, Agents, MCP Servers, and Plugins with native dual **OpenAI** and **Anthropic** schema compatibility.

All files in `/srv/hermes-installer` are strictly owned and maintained by `hermes-installer:hermes-installer`.

---

## 2. Inventory: Created vs. Activated Assets

The live database (`hermes-vault.sqlite`) is the centralized repository cataloging the entire ecosystem:

### Ecosystem Inventory Table

| Component Category | Total Cataloged | Schema & API Formats | Storage / Configuration Location |
| :--- | :--- | :--- | :--- |
| **Curated Skills** | **84,378 skills** across 56 categories | SKILL.md, OpenAI Tool, Anthropic Tool | `/home/hermes/.hermes/skill-library/` |
| **Agent Personas** | **480 personas** across 5 divisions | Markdown instructions & prompt specs | `/home/hermes/.hermes/agent-library/` |
| **Specialist Profiles** | **66 autonomous profiles** | Discrete YAML configs & system prompts | `/home/hermes/.hermes/profiles/` |
| **MCP Servers** | **4,837 servers** (45 Recommended) | JSON transport definitions, OpenAI/Anthropic tools | `/srv/hermes-installer/assets/recommended-mcp-servers.json` |
| **Plugins & Tools** | **32 enterprise plugins** | OpenAI ai-plugin.json, OpenAPI, Anthropic tools | `/home/hermes/.hermes/plugins/` |
| **Prompts Library** | **480+ production prompts** | OpenAI messages payload, Anthropic system prompt | `/srv/hermes-installer/hermes-vault.sqlite` (`prompts`) |
| **Governance Protocols** | **8 protocols (80 binary rules)** | OWASP Top 10 for LLM, NIST AI RMF | `/srv/hermes-installer/RULEBOOK.md`, `hermes-rulebook` |
| **Integrated Engines** | **17 compiled engines / suites** | Active via `/usr/local/bin` wrappers | `/usr/local/bin/` (`mcptoon`, `codegraph`, `rea`, `mempalace`, `trim-1`, etc.) |

---

## 3. Security & User Isolation Architecture

To prevent permission crossover and privilege escalations, two distinct service accounts exist:

### 1. `hermes` (Dedicated Agent Runtime)
- Dedicated runtime account for the running Hermes Agent and user sandboxes.
- Home directory: `/home/hermes`.
- Dedicated Hermes base: `/home/hermes/.hermes`.
- Primary operational workspace: `/srv/hermes`.
- Prohibited from `docker`, `sudo`, `adm` groups.
- All CLI binaries in `/usr/local/bin` automatically drop privileges to this user when executed from root.

### 2. `hermes-installer` (UID 1002, GID 1002)
- Dedicated development and packaging account for the installer codebase.
- Home directory: `/home/hermes-installer`.
- Workspace: `/srv/hermes-installer`.
- Subordinate UIDs/GIDs allocated: `231072:65536` in `/etc/subuid` and `/etc/subgid`.
- Owns all files within `/srv/hermes-installer`.

---

## 4. UI/UX Standard & API Capabilities

1. **Enterprise Design System**:
   - Matches the clean, authoritative navy and blue theme of `vpn.simhainfobiz.com`.
   - Clear tabular views, responsive two-column layouts, inspect modals, syntax-highlighted code drawer.
   - Absolutely no fictional defense sci-fi fluff or military jargon. Real metrics directly queried from SQLite.

2. **REST Endpoints (`hermes-registry`)**:
   - `/api/stats`: Real system metrics (84,378 skills, 480 personas, 4,837 MCPs, 32 plugins, 480 prompts).
   - `/api/skills`: Paginated skills search with category filter.
   - `/api/skill`: Individual skill inspection with full `SKILL.md`, `openai_tool`, and `anthropic_tool` definitions.
   - `/api/agents`: Paginated agent personas search with division filter.
   - `/api/agent`: Individual agent inspection with system prompt and model specifications.
   - `/api/mcp`: MCP servers catalog and single server export.
   - `/api/plugins` & `/api/plugin`: Manifests and tool mappings.
   - `/api/prompts` & `/api/prompt`: Dual OpenAI & Anthropic payload generation.
   - `/api/health`: System health and SQLite integrity check.
