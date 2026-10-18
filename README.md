# Hermes Agent Enterprise Offline Installer

[![Version](https://img.shields.io/badge/version-v0.21.5-blue.svg)](https://github.com/simhaonline/hermes-installer/releases)
[![Offline](https://img.shields.io/badge/deployment-100%25_offline-green.svg)](https://github.com/simhaonline/hermes-installer/releases)
[![Platform](https://img.shields.io/badge/platform-Ubuntu_LTS-orange.svg)](https://ubuntu.com)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](LICENSE)

A complete, self-contained, offline production installer for **Hermes Agent** with **16 advanced AI, engineering, and reverse engineering engines**, **1,688 curated skills across 33 categories**, **43,000+ indexed community skills**, **4,800+ MCP servers**, **415 agent personas**, **42 specialist profiles**, and **24 active plugins**.

---

## 🚀 Quick Start (1-Line Install)

To install on any clean Ubuntu LTS machine (22.04 / 24.04 / 26.04):

```bash
curl -fsSL https://raw.githubusercontent.com/simhaonline/hermes-installer/main/quick-install.sh | bash
```

---

## 📦 Release Downloads (Option A: Standalone Archive)

Download the complete pre-built offline bundle directly from [**GitHub Releases v1.0.0**](https://github.com/simhaonline/hermes-installer/releases/tag/v1.0.0):

| Release Asset | Size | SHA-256 Checksum | Description |
|---|---|---|---|
| [**`hermes-self-contained-installer.tar.gz`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-self-contained-installer.tar.gz) | **1.4 GB** | `467a20d77364c3987de731a0b5e6c314ee14588da3ca4a2c75d6bbc8e211a85d` | **Complete Standalone Offline Installer**: Pre-built core, 16 compiled engines, all 1,688 skills, 43k community pool, 4.8k MCPs, 415 personas, and SQLite vault. |
| [**`hermes-vault.sqlite`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-vault.sqlite) | **76 MB** | `a646b80aca91608fd1d5755fba91fe426e55536a3c4424398188e2f060820efa` | **SQLite Knowledge Vault**: Master database containing full markdown text for all skills, agents, MCPs, and plugins. |
| [**`hermes-agent-production.sh`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-agent-production.sh) | **181 MB** | `38c190fb7711f9f7f7940a3201c829ccc332faf5772e6490db8e919d1fc96860` | Production deployment script with embedded base64 payload. |
| [**`hermes-assets.tar.gz`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/hermes-assets.tar.gz) | **134 MB** | `ce989e1e3b81d2e8b5aa640d5c9c874983d6236607162d0504048088e96157da` | Core asset tarball. |
| [**`SHA256SUMS.txt`**](https://github.com/simhaonline/hermes-installer/releases/download/v1.0.0/SHA256SUMS.txt) | 634 B | — | Cryptographic integrity verification file. |

---

## ⚙️ Manual Offline Installation on Air-Gapped / New Devices

If you downloaded the 1.4 GB archive or transferred it via USB/SCP:

```bash
# 1. Extract the package
tar -xzf hermes-self-contained-installer.tar.gz
cd hermes-self-contained-installer

# 2. Run the offline installer (takes ~30 seconds)
sudo bash install-hermes-local.sh

# 3. Verify installation (0 errors, 0 warnings)
sudo bash install-hermes-local.sh --validate-only
```

*Zero external network calls, zero `git clone`, zero `uv` download, and zero `pip`/`npm` downloads.*

---

## 🛡️ Security Architecture: Root vs. `predictatrade` User

### Dedicated Service Account Isolation
- Hermes executes strictly as the dedicated non-root user `predictatrade` (`UID=1001`).
- Strictly prohibited from privileged groups (`docker`, `sudo`, `adm`), preventing host privilege escalation.
- Primary project workspace resides in `/srv/predictatrade` (`0755` permissions owned by `predictatrade:predictatrade`).

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

- **Skills Library**: 1,688 Curated Skills across 33 Categories + 43,000+ Community Skill Packages.
- **Agent Library**: 415+ Personas (Engineering, Design, Quant Trading, Security, Reverse Engineering).
- **Specialist Profiles**: 42 Pre-configured Profiles (`metatrader-quant`, `security-audit`, `coding-engineer`, `fabric-engineer`, `token-optimizer`, etc.).
- **MCP Servers**: 4,800+ Cataloged Servers + 30 Curated Production Servers (`recommended-mcp-servers.json`).
- **Plugins**: 24 Active Plugins (`superpowers`, `token-saver`, `security-guidance`, `disk-cleanup`, `mirofish`, `openshell`, etc.).

---

## 🔍 SQLite Knowledge Vault CLI (`hermes-vault`)

The installer deploys `/usr/local/bin/hermes-vault` for instant querying:

```bash
# View system metadata and ecosystem inventory
hermes-vault stats

# Search curated skills by query or category
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

## 📖 Complete Documentation

For complete architectural details, operational runbooks, and deep dive reference manuals, see:
- [**`README-HERMES.md`**](README-HERMES.md) — Comprehensive master documentation.
- [**`README-LOCAL-INSTALL.md`**](README-LOCAL-INSTALL.md) — Offline deployment manual and SQLite query reference.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
