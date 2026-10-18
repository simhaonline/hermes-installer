---
name: hermes-vault-manager
description: >-
  Use this skill when querying, auditing, updating, or maintaining the Hermes Knowledge Vault SQLite database (hermes-vault.sqlite).
---

# Hermes Vault Manager Skill

The Hermes Knowledge Vault (`hermes-vault.sqlite`, 229.36 MB) is the centralized repository cataloging the entire Hermes agent ecosystem.

## Database Location & Schema
* Path: `/home/predictatrade/.hermes/hermes-vault.sqlite`
* Tables:
  * `curated_skills` (19,453 entries): `name`, `category`, `description`, `tags`, `path`, `skill_md`
  * `community_skills` (64,569 entries): `name`, `repo`, `stars`, `description`, `path`, `raw_json`
  * `agent_personas` (462 entries): `persona_id`, `name`, `division`, `role`, `type`, `system_prompt`
  * `mcp_servers` (4,827 entries): `server_name`, `transport`, `command`, `args`, `env`, `is_recommended`
  * `profiles` (54 entries): `name`, `description`, `raw_config`
  * `plugins` (26 entries): `name`, `version`, `is_active`, `description`
  * `engines` (17 entries): `name`, `binary_path`, `technology`, `description`

## Common Operations

### 1. Ecosystem Statistics
```bash
hermes-vault stats
```

### 2. Querying Skills
```bash
# Curated skills
hermes-vault skills quant
hermes-vault skills "reverse engineering"

# Community skills pool
hermes-vault community "arbitrage"
```

### 3. Querying Personas
```bash
hermes-vault agents pentagi
hermes-vault agents "algorithmic trading"
```

### 4. Querying via sqlite3 directly
```bash
sqlite3 /home/predictatrade/.hermes/hermes-vault.sqlite "SELECT count(*), division FROM agent_personas GROUP BY division;"
sqlite3 /home/predictatrade/.hermes/hermes-vault.sqlite "SELECT name, command FROM mcp_servers WHERE is_recommended=1 LIMIT 10;"
```
