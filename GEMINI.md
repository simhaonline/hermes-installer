# Workspace Instructions: Hermes Installer (`/srv/hermes-installer`)

## 1. Project Overview & Boundaries
This workspace houses the repository for the **Hermes Agent Production Installer & Ecosystem Suite** (`simhaonline/hermes-installer.git`).

* **Workspace Directory**: `/srv/hermes-installer`
* **Dedicated Service User**: `hermes-installer` (`UID=1002`, `GID=1002`)
* **Hermes Agent Runtime**: `/home/predictatrade/.hermes` (`predictatrade`, `UID=1001`)
* **Live Knowledge Vault**: `/home/predictatrade/.hermes/hermes-vault.sqlite` (232.75 MB)

## 2. Available Development Skills in `.agents/skills/`
* `hermes-packager`: Build offline installer bundles, regenerate SHA256SUMS, and test asset payloads.
* `hermes-vault-manager`: Search, audit, sync, and inspect the SQLite Knowledge Vault.
* `hermes-profile-builder`: Validate, update, or add specialist profiles across the 66 profile configs.
* `hermes-ecosystem-tools`: Guide to CodeGraph AST indexing, MCPToon token compression, MemPalace memory search, and REA reverse engineering.

## 3. Development Workflow & Rules
1. **Ownership**: All files must be owned by `hermes-installer:hermes-installer`.
2. **Git Discipline**:
   * Do not commit large binary archives (`*.tar.gz`, `*.sqlite`) directly to git; they are excluded via `.gitignore`.
   * Keep `SHA256SUMS.txt`, `README-HERMES.md`, and `assets/collection-manifest.json` synchronized when adding skills or profiles.
3. **Verification**:
   * Test CLI commands using `runuser -u hermes-installer -- <command>` or root with proper privilege-dropping wrappers.
   * Run `hermes-vault stats` to verify database health before and after migrations.
