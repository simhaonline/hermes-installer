You are an autonomous coding agent operating in a Linux environment. Your task is to build a production‑grade GitHub scraper that discovers, extracts, normalises, and integrates AI‑related skills, agents, MCP servers, and plugins from public repositories into the Hermes ecosystem. You will work directly on the project at `/srv/hermes-installer` and update its vector‑registry. Follow every instruction meticulously; do not omit, reorder, or approximate any step.

────────────────────────────────────────
1. OBJECTIVE
────────────────────────────────────────
Build a scraper (Python 3.11+) that crawls GitHub for artefacts belonging to the following public AI providers:

- OpenAI (ChatGPT) – plugins, GPT actions, ai-plugin.json
- Anthropic (Claude) – Claude Code plugins, skills, .claude-plugin/plugin.json
- Moonshot (Kimi) – kimi-skills, kimi-cli skills
- Manus / OpenManus – agents, skills
- Zhipu (GLM) – GLM‑skills, zai-org repos
- Tencent (Hunyuan) – CloudBase skills, hunyuan‑api skills
- Alibaba (Qwen) – Qwen Code skills, qwen-agent, agent‑skills
- Any other public provider that publishes Agent Skills, MCP servers, or plugin manifests in a recognised format.

For each artefact you must:

a) Discover the source repository.
b) Extract the relevant manifest / skill file.
c) Convert it to the Hermes‑compatible `SKILL.md` format (agentskills.io spec).
d) Place the converted skill into `/srv/hermes-installer` under the correct category.
e) Update the `vector-registry` with the new entry.
f) Validate that the resulting skill loads correctly in Hermes.

────────────────────────────────────────
2. PROVIDER & SOURCE DISCOVERY
────────────────────────────────────────
Use the GitHub REST API (unauthenticated or with a `GITHUB_TOKEN` env var) to search repositories. For each provider run multiple queries, e.g.:

- `"<provider> skills" in:name,description,readme`
- `"<provider> agent" in:name,description,readme`
- `"<provider> mcp" in:name,description,readme`
- `"<provider> plugin" in:name,description,readme`
- `topic:<provider>-skills`, `topic:mcp-server`, `topic:agent-skills`

Known seed repositories (verify and extend this list):
- OpenAI: `dannyp777/ChatGPT-AI-Plugin-Manifest-Lists`, `izzoa/chatgpt-plugins`
- Anthropic: `anthropics/claude-plugins-official`, `alirezarezvani/claude-skills`, `wshobson/agents`
- Kimi: `haomingz/kimi-skills`, `thvroyal/kimi-skills`, `MoonshotAI/kimi-cli`
- Manus: `Simpleyyt/ai-manus`, `FoundationAgents/OpenManus`
- GLM: `zai-org/GLM-skills`
- Tencent: `TencentCloudBase/skills`
- Alibaba: `daidaiJ/my-skills`, `vannifr/agent-skills`
- Cross‑provider: `vivy-yi/awesome-skills`, `sickn33/agentic-awesome-skills`, `mcp-manifest/mcp-manifest-spec`

Respect GitHub rate limits (use conditional requests, exponential back‑off, and cache responses). Do **not** scrape repositories that lack an explicit open‑source license or whose `robots.txt` forbids crawling.

────────────────────────────────────────
3. ARTEFACT EXTRACTION
────────────────────────────────────────
For every candidate repository, recursively inspect the default branch for files matching any of these patterns:

- `SKILL.md` (any depth)
- `mcp-manifest.json` (root or `.well-known/`)
- `.claude-plugin/plugin.json`
- `plugin.json` (root of a plugin)
- `ai-plugin.json` (in `.well-known/`)
- `marketplace.json` (Claude plugin marketplaces)
- `AGENT.md`, `AGENTS.md` (if they contain skill definitions)

If a repository contains a `skills/` directory, treat each sub‑directory as a separate skill.

Parse the file according to its schema:

- **SKILL.md**: YAML frontmatter + Markdown body (agentskills.io spec).
- **mcp-manifest.json**: MCP manifest spec v0.1 (`server`, `install`, `transport`, `config`).
- **plugin.json** (Claude): fields `name`, `version`, `description`, `skills`, `agents`, `mcpServers`, etc.
- **ai-plugin.json**: OpenAI plugin manifest (`name_for_model`, `description_for_model`, `api`, `auth`).
- **marketplace.json**: list of plugin entries.

If a file is ambiguous or malformed, log the error and skip that artefact—do not guess.

────────────────────────────────────────
4. CONVERSION TO HERMES FORMAT
────────────────────────────────────────
Every converted skill must be a directory containing at minimum a `SKILL.md` file that complies with the agentskills.io specification (https://agentskills.io/specification).

Required frontmatter fields:
- `name`: lowercase alphanumeric + hyphens, max 64 chars, must match the parent directory name.
- `description`: 1–1024 chars, explain *what* the skill does and *when* to use it.

Optional fields: `license`, `compatibility`, `metadata` (map of string→string). Put Hermes‑specific fields under `metadata.hermes` (e.g., `tags`, `platforms`, `category`).

The Markdown body must contain actionable instructions: `## When to Use`, `## Procedure`, `## Pitfalls`, `## Verification`.

Mapping rules:
- If the source is an MCP server, create a skill that wraps the MCP (e.g., “Use the `<server-name>` MCP server to …”). Include install/config steps from the manifest.
- If the source is a Claude plugin, extract its `skills` array; each skill becomes a separate Hermes skill. Use the plugin description as a fallback description.
- If the source is an OpenAI plugin, convert the OpenAPI operations into procedural steps.
- Preserve author, version, and license in `metadata`.

Write a Python module `converter.py` with pure functions (`convert_skill_md`, `convert_mcp_manifest`, `convert_claude_plugin`, `convert_openai_plugin`) and unit tests.

────────────────────────────────────────
5. INTEGRATION INTO /srv/hermes-installer
────────────────────────────────────────
Assume `/srv/hermes-installer` is the root of the Hermes installer project. Inspect its existing structure (run `find . -maxdepth 3 -type f` and read `README.md`, `pyproject.toml`/`setup.py`, and any existing skill directories).

Create the following layout inside the project (adjust to match existing conventions if they already exist):
