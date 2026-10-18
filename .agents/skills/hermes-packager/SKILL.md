---
name: hermes-packager
description: >-
  Use this skill when packaging, building, or updating the Hermes Agent offline installer bundle,
  recalculating SHA256 checksums, or staging asset tarballs in /srv/hermes-installer.
---

# Hermes Installer Packager Skill

This skill guides the preparation, packaging, and validation of the Hermes Agent offline installer assets.

## Core Asset Components

1. **`hermes-vault.sqlite`**: The complete ecosystem metadata database (~230 MB).
2. **`hermes-assets.tar.gz`**: Packaged collection of curated skills, specialist agent personas, MCP definitions, and profile templates.
3. **`hermes-engines.tar.gz`**: Pre-compiled binaries and runtime packages (`mcptoon`, `codegraph`, `rea`, `mempalace`, `trim-1`, `pentagi`, `autoagent`, `cactus`, `openshell`).
4. **`hermes-agent-core.tar.gz`**: Pinned core Hermes agent runtime and uv cache.

## Packaging Workflow

### 1. Build Asset Bundle
When updating assets or skills:
```bash
# Verify current git state
git status

# Inspect existing assets in assets/
ls -la assets/

# Recompute SHA256 checksums for any generated archives
sha256sum install-hermes-local.sh quick-install.sh README-HERMES.md > SHA256SUMS.txt
```

### 2. Validate Archive Health
Ensure archives are valid and not truncated:
```bash
tar -tzf <archive-name>.tar.gz >/dev/null && echo "Archive valid"
```

### 3. Verify Offline Script Compatibility
Verify that `install-hermes-local.sh` passes bash syntax check:
```bash
bash -n install-hermes-local.sh
bash -n quick-install.sh
```
