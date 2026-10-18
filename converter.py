#!/usr/bin/env python3
"""Converter module for Hermes Agent Ecosystem.

Provides pure functions to convert, normalize, and validate AI artifacts
(SKILL.md, MCP manifests, Claude plugins, OpenAI plugins) into the
agentskills.io specification for Hermes Agent.

Specification:
- Frontmatter:
  - name: lowercase alphanumeric + hyphens, max 64 chars, matches directory name.
  - description: 1-1024 chars explaining what the skill does and when to use it.
  - optional: license, compatibility, metadata (metadata.hermes: category, tags, provider, etc.)
- Markdown Body:
  - ## When to Use
  - ## Procedure
  - ## Pitfalls
  - ## Verification
"""

import json
import re
from typing import Any, Dict, List, Optional
import yaml


NAME_PATTERN = re.compile(r"^[a-z0-9]([a-z0-9-]{0,62}[a-z0-9])?$")


def normalize_name(raw_name: str, fallback: str = "custom-skill") -> str:
    """Normalize a string to meet agentskills.io name specification.

    Lowercase alphanumeric and hyphens, max 64 chars, no leading/trailing hyphens.
    """
    if not raw_name or not isinstance(raw_name, str):
        raw_name = fallback

    # Replace invalid chars with hyphen
    name = re.sub(r"[^a-zA-Z0-9-]", "-", raw_name.strip()).lower()
    # Collapse multiple hyphens
    name = re.sub(r"-+", "-", name)
    # Strip leading/trailing hyphens
    name = name.strip("-")

    if not name:
        name = fallback.lower().strip("-")

    # Enforce 64 characters limit
    if len(name) > 64:
        name = name[:64].rstrip("-")

    # Final guarantee
    if not name or not NAME_PATTERN.match(name):
        # Fallback to safe name if strange edge cases occur
        name = re.sub(r"[^a-z0-9]", "", name)[:64]
        if not name:
            name = "hermes-skill"

    return name


def normalize_description(desc: Optional[str], fallback_name: str = "Hermes skill") -> str:
    """Normalize description to meet agentskills.io requirement (1-1024 characters)."""
    if not desc or not isinstance(desc, str) or not desc.strip():
        desc = f"Comprehensive capabilities, procedures, and best practices for {fallback_name}."

    # Collapse multi-line whitespace
    clean_desc = " ".join(desc.strip().split())

    if len(clean_desc) > 1024:
        clean_desc = clean_desc[:1021] + "..."

    return clean_desc


def parse_frontmatter(content: str) -> tuple[Dict[str, Any], str]:
    """Extract YAML frontmatter and markdown body from a document."""
    if not content:
        return {}, ""

    stripped = content.strip()
    if not stripped.startswith("---"):
        return {}, stripped

    parts = stripped.split("---", 2)
    if len(parts) < 3:
        return {}, stripped

    yaml_text = parts[1]
    body = parts[2].strip()

    try:
        data = yaml.safe_load(yaml_text)
        if isinstance(data, dict):
            return data, body
        return {}, body
    except Exception:
        return {}, body


def render_skill_md(frontmatter: Dict[str, Any], body: str) -> str:
    """Render YAML frontmatter and markdown body into valid SKILL.md format."""
    # Custom Dumper or safe_dump with nice formatting
    fm_str = yaml.dump(frontmatter, sort_keys=False, default_flow_style=False, allow_unicode=True).strip()
    return f"---\n{fm_str}\n---\n\n{body.strip()}\n"


def ensure_markdown_sections(
    body: str,
    skill_name: str,
    description: str,
    when_to_use: Optional[str] = None,
    procedure: Optional[str] = None,
    pitfalls: Optional[str] = None,
    verification: Optional[str] = None,
) -> str:
    """Ensure the markdown body contains all four required sections."""
    lines = body.strip().splitlines() if body else []
    body_text = body.strip() if body else ""

    # Detect existing headings (case-insensitive)
    has_when = bool(re.search(r"^##\s+When\s+to\s+Use", body_text, re.IGNORECASE | re.MULTILINE))
    has_procedure = bool(re.search(r"^##\s+Procedure", body_text, re.IGNORECASE | re.MULTILINE))
    has_pitfalls = bool(re.search(r"^##\s+Pitfalls", body_text, re.IGNORECASE | re.MULTILINE))
    has_verification = bool(re.search(r"^##\s+Verification", body_text, re.IGNORECASE | re.MULTILINE))

    title_header = f"# {skill_name.replace('-', ' ').title()}\n\n{description}\n"
    if not body_text.startswith("# "):
        body_text = title_header + "\n" + body_text

    additions = []

    if not has_when:
        content = when_to_use or f"- When interacting with {skill_name} capabilities or automation.\n- When required by workflows calling for {description}."
        additions.append(f"## When to Use\n\n{content}")

    if not has_procedure:
        content = procedure or f"1. Verify prerequisites and runtime environment.\n2. Execute relevant operations or CLI actions for {skill_name}.\n3. Review generated logs or outputs."
        additions.append(f"## Procedure\n\n{content}")

    if not has_pitfalls:
        content = pitfalls or f"- Avoid executing unverified configurations or missing required credentials.\n- Ensure schema boundaries and timeouts are respected."
        additions.append(f"## Pitfalls\n\n{content}")

    if not has_verification:
        content = verification or f"- Inspect exit status and command outputs.\n- Run verification check to confirm {skill_name} functions as expected."
        additions.append(f"## Verification\n\n{content}")

    if additions:
        body_text = body_text.strip() + "\n\n" + "\n\n".join(additions)

    return body_text.strip() + "\n"


def convert_skill_md(content: str, metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Pure function to convert and normalize an existing SKILL.md.

    Args:
        content: Raw markdown text with or without frontmatter.
        metadata: Optional metadata dictionary (author, provider, category, repo, tags).

    Returns:
        Dict with keys: name, description, frontmatter, body, skill_md, category
    """
    metadata = metadata or {}
    raw_fm, body = parse_frontmatter(content)

    raw_name = raw_fm.get("name")
    if not raw_name or str(raw_name).lower().strip() in ("skill", "skills", "custom-skill", "my-skill"):
        path_str = metadata.get("path", "")
        if path_str:
            parts = [p for p in path_str.split("/") if p and not p.lower().endswith(".md")]
            if parts and parts[-1].lower() not in ("skill", "skills"):
                raw_name = parts[-1]
        if not raw_name or str(raw_name).lower().strip() in ("skill", "skills"):
            title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip()
                if title.lower() not in ("skill", "skills", "readme"):
                    raw_name = title
    if not raw_name:
        raw_name = metadata.get("name") or "hermes-skill"
    name = normalize_name(raw_name)

    raw_desc = raw_fm.get("description") or metadata.get("description")
    description = normalize_description(raw_desc, fallback_name=name)

    category = (
        metadata.get("category")
        or (raw_fm.get("metadata", {}).get("hermes", {}).get("category") if isinstance(raw_fm.get("metadata"), dict) else None)
        or "community-skills"
    )

    # Build standardized frontmatter
    frontmatter: Dict[str, Any] = {
        "name": name,
        "description": description,
    }

    if "license" in raw_fm:
        frontmatter["license"] = str(raw_fm["license"])
    elif "license" in metadata:
        frontmatter["license"] = str(metadata["license"])

    if "compatibility" in raw_fm:
        frontmatter["compatibility"] = str(raw_fm["compatibility"])

    # Metadata map (string -> string or nested dict for hermes)
    fm_metadata = raw_fm.get("metadata") if isinstance(raw_fm.get("metadata"), dict) else {}
    hermes_meta = fm_metadata.get("hermes") if isinstance(fm_metadata.get("hermes"), dict) else {}

    hermes_meta["category"] = category
    if "provider" in metadata:
        hermes_meta["provider"] = str(metadata["provider"])
    if "repo" in metadata:
        hermes_meta["repo"] = str(metadata["repo"])
    if "author" in metadata:
        hermes_meta["author"] = str(metadata["author"])
    if "tags" in metadata:
        hermes_meta["tags"] = str(metadata["tags"])

    fm_metadata["hermes"] = hermes_meta
    frontmatter["metadata"] = fm_metadata

    # Normalize body sections
    normalized_body = ensure_markdown_sections(body, name, description)
    skill_md = render_skill_md(frontmatter, normalized_body)

    return {
        "name": name,
        "description": description,
        "frontmatter": frontmatter,
        "body": normalized_body,
        "skill_md": skill_md,
        "category": category,
    }


def convert_mcp_manifest(manifest_json: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Pure function to convert an MCP manifest (v0.1) into a Hermes SKILL.md.

    Args:
        manifest_json: Parsed JSON dict of mcp-manifest.json or MCP server config.
        metadata: Optional metadata dictionary (author, provider, category, repo, tags).

    Returns:
        Dict with keys: name, description, frontmatter, body, skill_md, category
    """
    metadata = metadata or {}

    # Extract server info
    server = manifest_json.get("server") if isinstance(manifest_json.get("server"), dict) else manifest_json
    raw_name = server.get("name") or manifest_json.get("name") or metadata.get("name") or "mcp-server"
    name = normalize_name(f"{raw_name}-mcp" if not raw_name.endswith("-mcp") else raw_name)

    raw_desc = (
        server.get("description")
        or manifest_json.get("description")
        or metadata.get("description")
        or f"Use the {raw_name} Model Context Protocol (MCP) server for external tool execution."
    )
    description = normalize_description(
        f"Use the {raw_name} MCP server: {raw_desc}",
        fallback_name=f"{raw_name} MCP server"
    )

    command = server.get("command") or manifest_json.get("command") or "node"
    args = server.get("args") or manifest_json.get("args") or []
    if isinstance(args, list):
        args_str = " ".join(str(a) for a in args)
    else:
        args_str = str(args)

    transport = server.get("transport") or manifest_json.get("transport") or "stdio"
    env_vars = server.get("env") or manifest_json.get("env") or {}

    category = metadata.get("category") or "mcp-servers"
    provider = metadata.get("provider") or "mcp"

    frontmatter: Dict[str, Any] = {
        "name": name,
        "description": description,
        "metadata": {
            "hermes": {
                "category": category,
                "provider": provider,
                "transport": str(transport),
                "command": str(command),
                "tags": "mcp, protocol, tools, integration",
            }
        }
    }

    if "license" in manifest_json:
        frontmatter["license"] = str(manifest_json["license"])
    elif "license" in metadata:
        frontmatter["license"] = str(metadata["license"])

    if "author" in metadata:
        frontmatter["metadata"]["hermes"]["author"] = str(metadata["author"])
    if "version" in manifest_json:
        frontmatter["metadata"]["hermes"]["version"] = str(manifest_json["version"])

    # Construct procedures
    env_lines = ""
    if isinstance(env_vars, dict) and env_vars:
        env_lines = "\n### Required Environment Variables:\n" + "\n".join(f"- `{k}`: {v}" for k, v in env_vars.items())

    procedure = f"""### 1. Configuration
Configure the MCP server in your Hermes or client configuration:
```json
{{
  "mcpServers": {{
    "{raw_name}": {{
      "command": "{command}",
      "args": {json.dumps(args if isinstance(args, list) else [args])},
      "transport": "{transport}"
    }}
  }}
}}
```{env_lines}

### 2. Execution
Start and register the server:
```bash
{command} {args_str}
```

### 3. Usage
Interact with tools and prompts exposed by the {raw_name} server via native Hermes tool calls.
"""

    pitfalls = f"""- Ensure the `{command}` runtime is installed and accessible in the system PATH.
- Missing environment variables will cause the server subprocess to terminate unexpectedly.
- Check transport mode ({transport}); network/firewall policies may restrict external sockets.
"""

    verification = f"""- Validate server startup by executing `hermes mcp list` or testing the connection.
- Verify server response with:
```bash
echo '{{"jsonrpc": "2.0", "method": "ping", "id": 1}}' | {command} {args_str}
```
"""

    body = f"# {raw_name.title()} MCP Server Integration\n\n{description}\n\n"
    normalized_body = ensure_markdown_sections(
        body,
        name,
        description,
        when_to_use=f"Use this skill whenever you need to interact with external tools, APIs, or database connections exposed by `{raw_name}`.",
        procedure=procedure.strip(),
        pitfalls=pitfalls.strip(),
        verification=verification.strip(),
    )

    skill_md = render_skill_md(frontmatter, normalized_body)

    return {
        "name": name,
        "description": description,
        "frontmatter": frontmatter,
        "body": normalized_body,
        "skill_md": skill_md,
        "category": category,
    }


def convert_claude_plugin(plugin_json: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """Pure function to convert a Claude plugin manifest into Hermes SKILL.md entries.

    If plugin contains a 'skills' list, each skill becomes an individual skill.
    Otherwise, converts the plugin itself into a Hermes skill.

    Args:
        plugin_json: Parsed JSON dict from .claude-plugin/plugin.json or marketplace entry.
        metadata: Optional metadata dictionary (author, provider, category, repo).

    Returns:
        List of converted skill dictionaries.
    """
    metadata = metadata or {}
    results: List[Dict[str, Any]] = []

    plugin_name = plugin_json.get("name") or metadata.get("name") or "claude-plugin"
    plugin_desc = plugin_json.get("description") or metadata.get("description") or f"Claude plugin: {plugin_name}"
    author = plugin_json.get("author") or metadata.get("author") or "Anthropic Ecosystem"
    version = plugin_json.get("version") or metadata.get("version") or "1.0.0"
    license_val = plugin_json.get("license") or metadata.get("license") or "MIT"
    category = metadata.get("category") or "claude-skills"

    skills = plugin_json.get("skills")
    if isinstance(skills, list) and skills:
        for idx, item in enumerate(skills):
            if isinstance(item, dict):
                s_name = item.get("name") or f"{plugin_name}-skill-{idx+1}"
                s_desc = item.get("description") or plugin_desc
                s_prompt = item.get("prompt") or item.get("instructions") or ""
            elif isinstance(item, str):
                s_name = item
                s_desc = f"{item} skill provided by {plugin_name} plugin."
                s_prompt = ""
            else:
                continue

            name = normalize_name(s_name)
            description = normalize_description(s_desc, fallback_name=name)

            frontmatter = {
                "name": name,
                "description": description,
                "license": str(license_val),
                "metadata": {
                    "hermes": {
                        "category": category,
                        "provider": "anthropic",
                        "plugin": str(plugin_name),
                        "author": str(author),
                        "version": str(version),
                        "tags": f"claude, plugin, {plugin_name}",
                    }
                }
            }

            body = f"# {name.replace('-', ' ').title()}\n\n{description}\n\n"
            if s_prompt:
                body += f"## Core Instructions\n\n{s_prompt}\n\n"

            normalized_body = ensure_markdown_sections(
                body,
                name,
                description,
                when_to_use=f"Use this skill when performing tasks requiring {name} within the {plugin_name} capability suite.",
                procedure=f"1. Initialize the {plugin_name} context.\n2. Execute the workflow defined for {name}.\n3. Verify output matches requirements.",
                pitfalls=f"- Ensure compatible model context and necessary permissions are granted.\n- Review dependencies specific to {plugin_name}.",
                verification=f"- Test execution against sample inputs to confirm correct response behavior.",
            )

            skill_md = render_skill_md(frontmatter, normalized_body)
            results.append({
                "name": name,
                "description": description,
                "frontmatter": frontmatter,
                "body": normalized_body,
                "skill_md": skill_md,
                "category": category,
            })
    else:
        # Single skill for the plugin itself
        name = normalize_name(plugin_name)
        description = normalize_description(plugin_desc, fallback_name=name)

        frontmatter = {
            "name": name,
            "description": description,
            "license": str(license_val),
            "metadata": {
                "hermes": {
                    "category": category,
                    "provider": "anthropic",
                    "author": str(author),
                    "version": str(version),
                    "tags": f"claude, plugin, {plugin_name}",
                }
            }
        }

        body = f"# {name.replace('-', ' ').title()}\n\n{description}\n\n"
        normalized_body = ensure_markdown_sections(
            body,
            name,
            description,
            when_to_use=f"Use this skill when interacting with the {plugin_name} plugin capabilities.",
            procedure=f"1. Enable the {plugin_name} integration.\n2. Invoke requested plugin commands or actions.\n3. Validate output artifacts.",
            pitfalls=f"- Check for required configuration parameters in .claude-plugin/plugin.json.\n- Maintain session state where applicable.",
            verification=f"- Execute basic health check or verification command for {plugin_name}.",
        )

        skill_md = render_skill_md(frontmatter, normalized_body)
        results.append({
            "name": name,
            "description": description,
            "frontmatter": frontmatter,
            "body": normalized_body,
            "skill_md": skill_md,
            "category": category,
        })

    return results


def convert_openai_plugin(
    ai_plugin_json: Dict[str, Any],
    openapi_spec: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Pure function to convert an OpenAI ChatGPT plugin manifest + OpenAPI spec into a Hermes skill.

    Args:
        ai_plugin_json: Parsed JSON dict from ai-plugin.json.
        openapi_spec: Optional parsed dict of the OpenAPI schema.
        metadata: Optional metadata dictionary (author, provider, category, repo).

    Returns:
        Dict with keys: name, description, frontmatter, body, skill_md, category
    """
    metadata = metadata or {}
    openapi_spec = openapi_spec or {}

    raw_name = (
        ai_plugin_json.get("name_for_model")
        or ai_plugin_json.get("name_for_human")
        or metadata.get("name")
        or "openai-plugin"
    )
    name = normalize_name(f"{raw_name}-plugin" if not raw_name.endswith("-plugin") else raw_name)

    raw_desc = (
        ai_plugin_json.get("description_for_model")
        or ai_plugin_json.get("description_for_human")
        or metadata.get("description")
        or f"OpenAI plugin for {raw_name} integration."
    )
    description = normalize_description(raw_desc, fallback_name=raw_name)

    category = metadata.get("category") or "openai-plugins"
    auth_info = ai_plugin_json.get("auth") if isinstance(ai_plugin_json.get("auth"), dict) else {}
    auth_type = auth_info.get("type", "none")

    frontmatter: Dict[str, Any] = {
        "name": name,
        "description": description,
        "metadata": {
            "hermes": {
                "category": category,
                "provider": "openai",
                "auth_type": str(auth_type),
                "tags": f"openai, chatgpt-plugin, {raw_name}",
            }
        }
    }

    if "contact_email" in ai_plugin_json:
        frontmatter["metadata"]["hermes"]["contact"] = str(ai_plugin_json["contact_email"])
    if "legal_info_url" in ai_plugin_json:
        frontmatter["metadata"]["hermes"]["legal"] = str(ai_plugin_json["legal_info_url"])

    # Extract OpenAPI endpoints into procedural steps
    api_steps = []
    paths = openapi_spec.get("paths", {}) if isinstance(openapi_spec.get("paths"), dict) else {}
    for path, methods in paths.items():
        if isinstance(methods, dict):
            for method, op in methods.items():
                if method.lower() in ("get", "post", "put", "delete", "patch") and isinstance(op, dict):
                    op_id = op.get("operationId") or f"{method.upper()} {path}"
                    summary = op.get("summary") or op.get("description") or f"Call {method.upper()} on {path}"
                    api_steps.append(f"- **{op_id}**: `{method.upper()} {path}` — {summary.strip()}")

    procedure_content = "### API Operations:\n"
    if api_steps:
        procedure_content += "\n".join(api_steps[:20])  # limit to top 20 endpoints for readability
    else:
        procedure_content += f"1. Configure authentication credentials (type: `{auth_type}`).\n"
        procedure_content += f"2. Direct requests to the plugin API service.\n"
        procedure_content += "3. Process and format responses into conversational outputs."

    pitfalls = f"""- Authentication type `{auth_type}` must be properly supplied in request headers.
- Rate limits and quotas apply to third-party API backends.
- Schema validation: ensure request payload matches OpenAPI specification.
"""

    verification = f"""- Test API connectivity and status with a probe request:
```bash
curl -I -s "{ai_plugin_json.get('api', {}).get('url', 'https://api.example.com')}"
```
- Verify expected 200 OK or appropriate authentication challenge.
"""

    body = f"# {raw_name.title()} Plugin\n\n{description}\n\n"
    normalized_body = ensure_markdown_sections(
        body,
        name,
        description,
        when_to_use=f"Use this skill when requiring actions, queries, or workflows supported by {raw_name}.",
        procedure=procedure_content.strip(),
        pitfalls=pitfalls.strip(),
        verification=verification.strip(),
    )

    skill_md = render_skill_md(frontmatter, normalized_body)

    return {
        "name": name,
        "description": description,
        "frontmatter": frontmatter,
        "body": normalized_body,
        "skill_md": skill_md,
        "category": category,
    }
