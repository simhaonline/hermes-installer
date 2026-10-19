# Project Memory & Architecture Record: Hermes Installer & Ecosystem

**Project**: Hermes Agent Production Deployment & Ecosystem Installer  
**Repository**: `https://github.com/simhaonline/hermes-installer.git`  
**Workspace**: `/srv/hermes-installer`  
**Dedicated Project User**: `hermes-installer` (`UID=1002`, `GID=1002`)  
**Hermes Service User**: `hermes` (Isolated System Runtime)  
**Live Knowledge Vault**: `/srv/hermes-installer/hermes-vault.sqlite` (507.47 MB)  
**Live Web Dashboard**: `http://46.62.188.249:8998/`

---

## 1. Executive Summary & Core Mission

This repository houses the standalone, enterprise-grade installer, packaging pipeline, SQLite knowledge vault, and orchestration tooling for deploying and maintaining the **Hermes Agent** platform.

The system serves as an enterprise AI Knowledge & Capability Vault housing Prompts, Skills, Agents, MCP Servers, and Plugins with native dual **OpenAI** and **Anthropic** schema compatibility.

All files in `/srv/hermes-installer` are strictly owned and maintained by `hermes-installer:hermes-installer`. Large binary archives (`*.tar.gz`, `*.sqlite`) are git-ignored; lightweight releases are staged via `package-content-vault.sh`.

---

## 2. Inventory: Created vs. Activated Assets

The live database (`hermes-vault.sqlite`, 507.47 MB) is the centralized repository cataloging the entire ecosystem:

### Ecosystem Inventory Table

| Component Category | Total Cataloged | Schema & API Formats | Storage / Configuration Location |
| :--- | :--- | :--- | :--- |
| **Curated Skills** | **84,378 skills** across 56 categories | SKILL.md, OpenAI Tool, Anthropic Tool | SQLite FTS5 / `/home/hermes/.hermes/skill-library/` |
| **Agent Personas** | **480 personas** across 5 divisions | Markdown instructions & prompt specs | SQLite / `/home/hermes/.hermes/agent-library/` |
| **Specialist Profiles** | **66 autonomous profiles** | Discrete YAML configs & system prompts | `/home/hermes/.hermes/profiles/` |
| **MCP Servers** | **4,837 servers** (45 Recommended) | JSON transport definitions, OpenAI/Anthropic tools | `/srv/hermes-installer/assets/recommended-mcp-servers.json` |
| **Plugins & Tools** | **32 enterprise plugins** | OpenAI ai-plugin.json, OpenAPI, Anthropic tools | SQLite / `/home/hermes/.hermes/plugins/` |
| **Prompts Library** | **480 production prompts** | OpenAI messages payload, Anthropic system prompt | `/srv/hermes-installer/hermes-vault.sqlite` (`prompts`) |
| **Governance Protocols** | **8 protocols (80 binary rules)** | OWASP Top 10 for LLM, NIST AI RMF | `/srv/hermes-installer/RULEBOOK.md`, `hermes-rulebook` |
| **Integrated Engines** | **17 compiled engines / suites** | Active via `/usr/local/bin` wrappers | `/usr/local/bin/` (`mcptoon`, `codegraph`, `rea`, `mempalace`, `trim-1`, etc.) |

---

## 3. Security & Multi-User Isolation Architecture

To prevent permission crossover, data staleness, and privilege escalations, distinct service and system accounts exist:

### 1. `hermes` (Dedicated Agent Runtime User)
- Dedicated runtime account for the running Hermes Agent daemon and execution sandboxes.
- Home directory: `/home/hermes`.
- Dedicated Hermes base: `/home/hermes/.hermes`.
- Primary operational workspace: `/srv/hermes`.
- Prohibited from `docker`, `sudo`, `adm` groups.
- All CLI binaries in `/usr/local/bin` automatically drop privileges to this user when executed from root.

### 2. `hermes-installer` (UID 1002, GID 1002)
- Dedicated development, packaging, and CI user for the installer codebase.
- Home directory: `/home/hermes-installer`.
- Workspace: `/srv/hermes-installer`.
- Subordinate UIDs/GIDs allocated: `231072:65536` in `/etc/subuid` and `/etc/subgid`.
- Owns all files within `/srv/hermes-installer`.

### 3. Multi-User System Isolation & Synchronization
- Every system user (`UID >= 1000` or `root`, e.g. `predictatrade`, `sysadmin`, `hermes-installer`, `hermes`) maintains an isolated `~/.hermes/` directory.
- `hermes-vault` automatically detects user context via `Runtime User : <current_user> (Isolated Environment)`.
- When updating via `sudo hermes-installer --update --all-users` or nightly cron, the synchronizer iterates over all `/home/*/.hermes` directories and refreshes `hermes-vault.sqlite` while strictly maintaining user ownership (`chown -R <uid>:<gid>`).
- `/etc/skel/.hermes` is maintained as a template so any newly created Linux account automatically inherits the latest vault.

---

## 4. Lifecycle & Continuous Synchronization (`hermes-installer`)

The `hermes-installer` CLI (`/usr/local/bin/hermes-installer` and `/srv/hermes-installer/hermes-installer`) orchestrates all deployment, update, and synchronization tasks:

```bash
# 1. Incremental asset synchronization (ingests newly harvested content and syncs current user ~/.hermes)
hermes-installer --update

# 2. Server-wide multi-user environment synchronization (updates all /home/*/.hermes and /etc/skel)
sudo hermes-installer --update --all-users

# 3. Automated scheduled cron installation (runs nightly at 03:00 UTC with --all-users)
sudo hermes-installer --install-cron "0 3 * * *"

# 4. Remove automated update cron schedule
sudo hermes-installer --remove-cron

# 5. Live ecosystem inventory and database telemetry
hermes-installer --stats

# 6. Cryptographic integrity and testbench execution (29 unit tests + SQLite PRAGMA audit)
hermes-installer --validate
```

---

## 5. UI/UX Standards & REST API Endpoints

1. **Enterprise Design System**:
   - Strictly aligned with the corporate theme of `vpn.simhainfobiz.com`.
   - Clean, professional sidebar without badge counters, pills, or distracting numbers.
   - Clean headers: `Overview`, `Prompts Library`, `Skills Catalog`, `Agent Personas`, `MCP Universe`, `Plugins & Tools`, `AI Governance`, `System Diagnostics`, `API Explorer`.
   - Zero fictional sci-fi jargon or military fluff. All data queried directly from SQLite FTS5.

2. **REST Endpoints (`hermes-registry`)**:
   - `/api/stats`: Real system metrics (84,378 skills, 480 personas, 4,837 MCPs, 32 plugins, 480 prompts).
   - `/api/skills` & `/api/search`: Paginated skills search with category filter (supports both `results` and `skills` response keys).
   - `/api/skill`: Individual skill inspection with full `SKILL.md`, `openai_tool`, and `anthropic_tool` definitions.
   - `/api/agents`: Paginated agent personas search with division filter.
   - `/api/agent`: Individual agent inspection with system prompt and model specifications.
   - `/api/mcp`: MCP servers catalog and single server export.
   - `/api/plugins` & `/api/plugin`: Manifests and tool mappings.
   - `/api/prompts` & `/api/prompt`: Dual OpenAI & Anthropic payload generation.
   - `/api/health`: System health and SQLite integrity check.

---

## 6. Release Packaging Pipeline (`package-content-vault.sh`)

- Generates lightweight `dist/hermes-content-vault-v1.0.0.tar.gz` (211 MB).
- Includes master SQLite database (`hermes-vault.sqlite`, 507.47 MB uncompressed), ChromaDB vector registry, CLI executables (`hermes-installer`, `hermes-registry`, `hermes-vault`, `hermes-rulebook`), web dashboard, and manifests.
- Automatically calculates and updates `SHA256SUMS.txt`.
