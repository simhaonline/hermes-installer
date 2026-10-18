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

1. **Tier 1: Minimal Data & Knowledge Backup (75 MB)**:
   - **File**: `hermes-vault.sqlite`
   - **What it contains**: All 1,688 curated skills (full markdown text and YAML headers), 43,370 community skill packages, 4,859 MCP universe servers (including 30 recommended production servers), 415 agent persona definitions, 42 specialist profiles, 24 plugins, and 17 extended engines.
   - **Use case**: Quick backup to Google Drive, S3, or USB drive to preserve the full collected database.

2. **Tier 2: Complete Self-Contained Offline Installer (1.5 GB)**:
   - **Directory**: `/root/hermes-self-contained-installer/`
   - **Archive**: `/root/hermes-self-contained-installer.tar.gz`
   - **What it contains**:
     - `install-hermes-local.sh` — The 100% offline installation script.
     - `hermes-vault.sqlite` — The unified SQLite knowledge vault (75 MB).
     - `hermes-engines.tar.gz` — All 16 pre-compiled binary engines, Node libraries, and Python site-packages (107 MB).
     - `hermes-agent-core.tar.gz` — Pre-built Hermes Agent core engine with `node_modules` and Python launchers (333 MB).
     - `hermes-system-assets.tar.gz` — All 1,688 skills, 43,000+ community packages, MCP universe catalog, and tool runtimes (976 MB).
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
hermes-vault skills quant
hermes-vault skills --category quant-trading

# Search community skills pool (43,000+ packages)
hermes-vault community scrapfly

# List recommended production MCP servers
hermes-vault mcp --recommended

# Search all agent personas (415+ personas)
hermes-vault agents financial

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

# Query full system prompt of a specialist agent
sqlite3 hermes-vault.sqlite "SELECT system_prompt FROM agent_personas WHERE name='codegraph-intelligence';"
```
