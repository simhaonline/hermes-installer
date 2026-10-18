# Hermes Agent Self-Local & Offline Installer

## 1. Overview & Answers to Backup Strategy

### Do I need to backup both `hermes-assets.tar.gz` and `hermes-agent-production.sh`?
- **Short Answer**: **No**. `hermes-agent-production.sh` previously embedded `hermes-assets.tar.gz` inside itself as base64.
- **However**: The original installer was not 100% offline for *new/separate devices* because it would attempt to:
  1. `git clone` the official Hermes Agent core repository and download `uv`.
  2. Download/compile the 16 specialized AI engines (AutoAgent, PentAGI, REA, Trim-1, CodeGraph, MemPalace, etc.).
  3. Clone community repositories from GitHub.

### The New Offline Self-Local Solution
To eliminate all GitHub and internet dependencies when installing on other devices, two standardized backup tiers are provided:

1. **Tier 1: Minimal Data & Knowledge Backup (230 MB)**:
   - **File**: `hermes-vault.sqlite`
   - **What it contains**: All 19,453 curated skills (full markdown text and YAML headers across 47 categories), 64,569 community skill packages, 4,827 MCP universe servers (including 35 recommended production servers), 462 agent persona definitions, 54 specialist profiles, 26 plugins, and 17 extended engines.
   - **Use case**: Quick backup to Google Drive, S3, or USB drive to preserve the full collected database.

2. **Tier 2: Complete Self-Contained Offline Installer (~1.7 GB)**:
   - **Directory**: `/root/hermes-self-contained-installer/`
   - **Archive**: `/root/hermes-self-contained-installer.tar.gz`
   - **What it contains**:
     - `install-hermes-local.sh` — The 100% offline installation script.
     - `hermes-vault.sqlite` — The unified SQLite knowledge vault (230 MB).
     - `hermes-vault` — Standalone CLI utility to query the vault.
     - `hermes-engines.tar.gz` — All 16 pre-compiled binary engines, Node libraries, and Python site-packages (107 MB).
     - `hermes-agent-core.tar.gz` — Pre-built Hermes Agent core engine with `node_modules` and Python launchers (333 MB).
     - `hermes-system-assets.tar.gz` — All 19,453 skills, 64,500+ community packages, MCP universe catalog, and pre-compiled runtimes (1.1 GB).
   - **Use case**: Transfer this single archive to any other Ubuntu machine (offline or air-gapped) and install in under 30 seconds with **zero GitHub downloads**.

---

## 2. Deploying on Other Devices

### Step 1: Copy Archive to Target Machine
```bash
scp /root/hermes-self-contained-installer.tar.gz root@your-new-server:/root/
```

### Step 2: Extract the Package
```bash
cd /root
tar -xzf hermes-self-contained-installer.tar.gz
cd hermes-self-contained-installer
```

### Step 3: Run the Local Installer
```bash
# Standard installation under default dedicated user 'predictatrade'
sudo bash install-hermes-local.sh

# Or install for a custom service account
sudo bash install-hermes-local.sh --user myagent
```

### Step 4: Verify Installation
```bash
sudo bash install-hermes-local.sh --validate-only
```

---

## 3. SQLite Knowledge Vault CLI (`hermes-vault`)

The installer deploys `/usr/local/bin/hermes-vault` allowing instant querying and auditing of all components:

```bash
# View ecosystem metadata & inventory totals
hermes-vault stats

# Search curated skills by query or category
hermes-vault skills math
hermes-vault skills --category mathematics-ai

# Search community skills pool (64,500+ packages)
hermes-vault community scrapfly

# List recommended production MCP servers
hermes-vault mcp --recommended

# Search all agent personas (460+ personas)
hermes-vault agents excel

# Inspect the 16 pre-compiled extended engines
hermes-vault engines
```

---

## 4. Direct SQLite Query Examples

You can also run direct SQL queries on `hermes-vault.sqlite`:

```bash
# Count skills by category
sqlite3 hermes-vault.sqlite "SELECT category, count(*) FROM curated_skills GROUP BY category ORDER BY count(*) DESC;"

# Inspect recommended MCP servers
sqlite3 hermes-vault.sqlite "SELECT server_name, command FROM mcp_servers WHERE is_recommended=1;"

# Search agent personas by role
sqlite3 hermes-vault.sqlite "SELECT persona_id, name, division FROM agent_personas WHERE name LIKE '%architect%';"
```
