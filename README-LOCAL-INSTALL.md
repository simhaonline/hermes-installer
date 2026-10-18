# Hermes Agent Self-Local & Offline Installer

## 1. Overview & Answers to Backup Strategy

### Do I need to backup both `hermes-assets.tar.gz` and `hermes-agent-production.sh`?
- **Short Answer**: **No**. `hermes-agent-production.sh` previously embedded `hermes-assets.tar.gz` inside itself as base64.
- **However**: The original installer was not 100% offline for *new/separate devices* because it would attempt to:
  1. `git clone` the official Hermes Agent core repository and download `uv`.
  2. Download/compile the 16 specialized AI engines (AutoAgent, PentAGI, REA, Trim-1, CodeGraph, MemPalace, etc.).
  3. Clone community repositories from GitHub.

### The New Lightweight Content & Vector Vault Solution
To eliminate all GitHub and internet dependencies when installing or backing up on other devices, two standardized options are provided:

1. **Option A: Pure Content & Vector Vault (151 MB, Recommended)**:
   - **Archive**: `hermes-content-vault-v1.0.0.tar.gz`
   - **What it contains**:
     - `hermes-vault.sqlite` — Master database with 19,691 curated skills, 64,687 community skills, 4,837 MCPs, 480 personas, 66 profiles, 32 plugins, and FTS5 BM25 search tables (301 MB uncompressed).
     - `vector-registry/` — ChromaDB dense vector store with local ONNX embeddings across all skills, personas, profiles, and MCPs (69 MB uncompressed).
     - `hermes-registry` & `hermes-vault` — Dynamic JIT execution and query CLIs.
     - `assets/` — Complete collection manifests and JSON configurations.
   - **Advantage**: **Zero binary bloat**, fast transfer, instant semantic search, and zero-copy JIT dynamic activation without duplicating files across profiles.

2. **Option B: Standalone SQLite Knowledge Vault (301 MB)**:
   - **File**: `hermes-vault.sqlite`
   - **What it contains**: Full relational schema, B-Tree indexes, and FTS5 full-text tables.
   - **Use case**: Database-only backup or embedding in custom pipelines.

---

## 2. Deploying on Other Devices

### Step 1: Copy Archive to Target Machine
```bash
scp /srv/hermes-installer/dist/hermes-content-vault-v1.0.0.tar.gz user@your-server:~
```

### Step 2: Extract the Package
```bash
tar -xzf hermes-content-vault-v1.0.0.tar.gz
cd hermes-content-vault-v1.0.0
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
