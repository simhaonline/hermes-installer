---
name: hermes-ecosystem-tools
description: >-
  Use this skill when utilizing CodeGraph, MCPToon, MemPalace, REA, Trim-1, or PentAGI tools within Hermes.
---

# Hermes Integrated Ecosystem Tools

Hermes bundles 17 advanced compiled engines and specialist CLI tools installed in `/usr/local/bin`:

## 1. CodeGraph (`/usr/local/bin/codegraph`)
AST code graph indexer and semantic search engine.
* **Index a project**: `codegraph index /srv/hermes-installer`
* **Search symbols**: `codegraph search "handleOrder"`
* **Caller/Callee Impact**: Identifies downstream dependencies before making breaking changes.

## 2. MCPToon (`/usr/local/bin/mcptoon`)
Token compression gateway achieving ~99.2% reduction in MCP/tool payload context.
* **Compress payload**: `mcptoon --input data.json`
* **Run stdio bridge**: `mcptoon serve`

## 3. Trim-1 (`/usr/local/bin/trim` / `trim-1`)
Fast compiled context trimmer that selectively extracts only prompt-relevant code lines from bulky source files.
* **Prune file lines**: `trim --query "database connection" config.yaml`

## 4. MemPalace (`/usr/local/bin/mempalace` & `mempalace-mcp`)
ChromaDB holographic semantic memory with AAAK dialect compression.
* **Query memories**: `mempalace search "installer architecture"`
* **Start stdio MCP server**: `mempalace-mcp --read-only`

## 5. REA (`/usr/local/bin/rea` & `rea-agents`)
Universal binary reverse engineering and static decompilation engine.
* **Analyze binary**: `rea analyze /usr/local/bin/trim`

## 6. PentAGI (`/usr/local/bin/pentagi`)
Autonomous penetration testing and security audit agent.
* **Help & Commands**: `pentagi --help`
