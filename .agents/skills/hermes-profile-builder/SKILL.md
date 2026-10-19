---
name: hermes-profile-builder
description: >-
  Use this skill when defining, validating, or updating the 54 autonomous agent profiles and Multi-Agent Kanban decomposition for Hermes.
---

# Hermes Profile Builder Skill

Hermes supports running discrete autonomous agent profiles with independent memory stores, targeted skill sets, and specialized system prompts.

## Profile Architecture
Profiles reside in `/home/hermes/.hermes/profiles/<profile_name>/`:
* `profile.yaml`: Metadata description and role definition.
* `config.yaml`: Profile-scoped configuration (LLM model, memory limits, toolsets, enabled/disabled skills).
* `SOUL.md`: Primary system personality instructions.
* `memories/`: Independent SQLite / ChromaDB associative memory store.
* `sessions/`: Conversation session storage.

## Profile Definitions Reference
* Manifest: `assets/profiles.json` (54 defined profiles)
* Generator script: `assets/configure.py profiles`

## Validation Steps
1. Verify profile configuration syntax:
   ```bash
   python3 -c "import yaml; yaml.safe_load(open('assets/profiles.json'))"
   ```
2. Test launching a profile:
   ```bash
   hermes -p orchestrator --version
   ```
3. Test Multi-Agent Kanban status:
   ```bash
   hermes -p orchestrator kanban list
   ```
