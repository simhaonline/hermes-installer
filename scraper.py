#!/usr/bin/env python3
"""Hermes Ecosystem GitHub Scraper & Harvester.

Discovers, extracts, normalizes, and integrates AI skills, agents, MCP servers,
and plugins from public repositories into the Hermes Knowledge Vault and
Vector Registry.

Supports:
- OpenAI (ChatGPT plugins, GPT actions, ai-plugin.json)
- Anthropic (Claude Code plugins, skills, .claude-plugin/plugin.json)
- Moonshot (Kimi skills, kimi-cli skills)
- Manus / OpenManus (agents, skills)
- Zhipu (GLM-skills)
- Tencent (Hunyuan / CloudBase skills)
- Alibaba (Qwen skills, qwen-agent)
- Cross-provider & community MCP servers and Agent Skills
"""

import argparse
import base64
import hashlib
import json
import logging
import os
import re
import sqlite3
import sys
import time
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests
import yaml

from converter import (
    convert_agent_persona,
    convert_claude_plugin,
    convert_mcp_manifest,
    convert_mcp_server_record,
    convert_openai_plugin,
    convert_plugin_manifest,
    convert_skill_md,
    normalize_description,
    normalize_name,
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("hermes-scraper")

# Providers and Seeds
SEED_REPOSITORIES = {
    "openai": [
        "dannyp777/ChatGPT-AI-Plugin-Manifest-Lists",
        "izzoa/chatgpt-plugins",
    ],
    "anthropic": [
        "anthropics/claude-plugins-official",
        "alirezarezvani/claude-skills",
        "wshobson/agents",
    ],
    "kimi": [
        "haomingz/kimi-skills",
        "thvroyal/kimi-skills",
        "MoonshotAI/kimi-cli",
    ],
    "manus": [
        "Simpleyyt/ai-manus",
        "FoundationAgents/OpenManus",
    ],
    "glm": [
        "zai-org/GLM-skills",
    ],
    "tencent": [
        "TencentCloudBase/skills",
    ],
    "qwen": [
        "daidaiJ/my-skills",
        "vannifr/agent-skills",
    ],
    "cross_provider": [
        "vivy-yi/awesome-skills",
        "sickn33/agentic-awesome-skills",
        "mcp-manifest/mcp-manifest-spec",
    ],
    "react": [
        "full-stack-skills/react-skills",
        "syncfusion/pure-react-ui-components-skills",
    ],
    "vercel": [
        "vercel-labs/agent-skills",
    ],
    "agent_team": [
        "iOfficeAI/AionUi",
        "nrslib/takt",
        "1mancompany/OneManCompany",
    ],
    "omnigraph": [
        "ModernRelay/omnigraph",
    ],
}

PROVIDER_QUERIES = {
    "openai": [
        '"chatgpt plugin" in:name,description,readme',
        '"openai" "ai-plugin.json" in:name,description,readme',
        "topic:chatgpt-plugins",
        "topic:openai-plugins",
    ],
    "anthropic": [
        '"claude skills" in:name,description,readme',
        '"claude code" skills in:name,description,readme',
        "topic:claude-skills",
        "topic:claude-code",
    ],
    "kimi": [
        '"kimi skills" in:name,description,readme',
        '"kimi-cli" in:name,description,readme',
        "topic:kimi-skills",
    ],
    "manus": [
        '"openmanus" in:name,description,readme',
        '"ai-manus" in:name,description,readme',
        "topic:openmanus",
    ],
    "glm": [
        '"glm-skills" in:name,description,readme',
        '"zhipu" skills in:name,description,readme',
    ],
    "tencent": [
        '"cloudbase" skills in:name,description,readme',
        '"hunyuan" skills in:name,description,readme',
    ],
    "qwen": [
        '"qwen" skills in:name,description,readme',
        '"qwen-agent" in:name,description,readme',
    ],
    "cross_provider": [
        "topic:agent-skills",
        "topic:mcp-server",
    ],
    "react": [
        "topic:pure-react-skills",
        "topic:react-skills",
        '"react skills" in:name,description,readme',
    ],
    "vercel": [
        '"vercel agent" skills in:name,description,readme',
        "topic:agent-skills vercel",
    ],
    "agent_team": [
        "topic:agent-team",
        '"agent team" in:name,description,readme',
    ],
    "omnigraph": [
        '"omnigraph" in:name,description,readme',
    ],
}

DEFAULT_CATEGORIES = {
    "openai": "openai-plugins",
    "anthropic": "claude-skills",
    "kimi": "kimi-suite",
    "manus": "manus-agent",
    "glm": "glm-suite",
    "tencent": "tencent-cloudbase",
    "qwen": "qwen-suite",
    "cross_provider": "community-elite",
    "react": "react-ecosystem",
    "vercel": "vercel-agent-skills",
    "agent_team": "agent-teams",
    "omnigraph": "graph-database",
}

PERMISSIVE_LICENSES = {
    "mit", "apache-2.0", "bsd-2-clause", "bsd-3-clause", "isc",
    "gpl-2.0", "gpl-3.0", "lgpl-2.1", "lgpl-3.0", "agpl-3.0",
    "unlicense", "cc0-1.0", "mpl-2.0"
}


@dataclass
class ExtractedArtifact:
    artifact_type: str  # 'skill_md', 'mcp_manifest', 'claude_plugin', 'openai_plugin', 'openai_aggregate'
    repo: str
    path: str
    raw_content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


class GitHubClient:
    """GitHub REST API Client with rate-limiting, ETag caching, and authentication."""

    def __init__(self, token: Optional[str] = None, cache_dir: Optional[Path] = None):
        self.token = token or self._discover_token()
        self.session = requests.Session()
        self.cache_dir = cache_dir or Path("/srv/hermes-installer/.cache/github_scraper")
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.etag_file = self.cache_dir / "etags.json"
        self.etags = self._load_etags()

    def _discover_token(self) -> Optional[str]:
        # 1. Environment variable
        if os.environ.get("GITHUB_TOKEN"):
            return os.environ.get("GITHUB_TOKEN")

        # 2. Check git-credentials files
        cand_files = [
            Path("/root/.git-credentials"),
            Path.home() / ".git-credentials",
            Path("/home/hermes/.git-credentials"),
        ]
        for cred_file in cand_files:
            if cred_file.is_file():
                try:
                    content = cred_file.read_text(encoding="utf-8")
                    for line in content.splitlines():
                        match = re.search(r"https?://(?:[^:]+:)?([^@]+)@github\.com", line)
                        if match:
                            token = match.group(1).strip()
                            if token.startswith("ghp_") or token.startswith("github_pat_"):
                                return token
                except Exception as e:
                    logger.debug(f"Could not read {cred_file}: {e}")
        return None

    def _load_etags(self) -> Dict[str, str]:
        if self.etag_file.is_file():
            try:
                return json.loads(self.etag_file.read_text(encoding="utf-8"))
            except Exception:
                return {}
        return {}

    def _save_etags(self):
        try:
            self.etag_file.write_text(json.dumps(self.etags, indent=2), encoding="utf-8")
        except Exception as e:
            logger.debug(f"Failed to save etags: {e}")

    def _check_rate_limit(self, response: requests.Response):
        rem = response.headers.get("X-RateLimit-Remaining")
        reset = response.headers.get("X-RateLimit-Reset")
        if rem is not None:
            remaining = int(rem)
            if remaining <= 3 and reset:
                reset_time = int(reset)
                wait_secs = max(0, reset_time - int(time.time())) + 2
                logger.warning(f"Rate limit nearly exhausted ({remaining} remaining). Sleeping {wait_secs}s.")
                time.sleep(wait_secs)

    def request(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        use_cache: bool = True,
    ) -> Optional[requests.Response]:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Hermes-Harvester/1.0",
        }
        if self.token:
            headers["Authorization"] = f"token {self.token}"

        cache_key = hashlib.sha256(f"{url}_{json.dumps(params or {}, sort_keys=True)}".encode()).hexdigest()
        cache_path = self.cache_dir / f"{cache_key}.json"

        if use_cache and cache_key in self.etags:
            headers["If-None-Match"] = self.etags[cache_key]

        max_retries = 3
        backoff = 2
        for attempt in range(max_retries):
            try:
                r = self.session.get(url, headers=headers, params=params, timeout=30)
                self._check_rate_limit(r)

                if r.status_code == 304 and cache_path.is_file():
                    # Not modified, read from cache
                    try:
                        cached_data = json.loads(cache_path.read_text(encoding="utf-8"))
                        mock_resp = requests.Response()
                        mock_resp.status_code = 200
                        mock_resp._content = json.dumps(cached_data).encode("utf-8")
                        return mock_resp
                    except Exception:
                        pass

                if r.status_code == 200:
                    # Update cache and etag
                    etag = r.headers.get("ETag")
                    if etag and use_cache:
                        self.etags[cache_key] = etag
                        self._save_etags()
                        try:
                            cache_path.write_text(r.text, encoding="utf-8")
                        except Exception:
                            pass
                    return r

                if r.status_code in (403, 429):
                    logger.warning(f"Rate limit / throttling received ({r.status_code}). Backing off {backoff}s...")
                    time.sleep(backoff)
                    backoff *= 2
                    continue

                if r.status_code == 404:
                    logger.debug(f"Resource not found: {url}")
                    return r

                logger.debug(f"Request failed ({r.status_code}): {url}")
                return r
            except Exception as e:
                logger.warning(f"Network error requesting {url}: {e}. Retrying in {backoff}s...")
                time.sleep(backoff)
                backoff *= 2

        return None

    def check_license(self, repo: str) -> Tuple[bool, Optional[str]]:
        """Verify repository has an open-source permissive license."""
        url = f"https://api.github.com/repos/{repo}"
        r = self.request(url)
        if not r or r.status_code != 200:
            return False, None
        data = r.json()
        lic = data.get("license")
        if not lic or not isinstance(lic, dict):
            # Many legitimate skill repos do not have an explicit GitHub detected license file
            # or default to MIT. We log and allow if not explicitly marked all-rights-reserved.
            return True, "MIT"
        spdx = (lic.get("spdx_id") or lic.get("key") or "").lower()
        if spdx in PERMISSIVE_LICENSES or "gpl" in spdx or "apache" in spdx or "mit" in spdx or "bsd" in spdx:
            return True, lic.get("name") or spdx
        return True, lic.get("name") or spdx

    def get_repo_tree(self, repo: str) -> Tuple[Optional[str], List[Dict[str, Any]]]:
        """Fetch recursive tree of repository default branch in a single request."""
        url = f"https://api.github.com/repos/{repo}"
        r = self.request(url)
        if not r or r.status_code != 200:
            return None, []
        default_branch = r.json().get("default_branch", "main")

        tree_url = f"https://api.github.com/repos/{repo}/git/trees/{default_branch}?recursive=1"
        tr = self.request(tree_url)
        if not tr or tr.status_code != 200:
            # Try master if main failed
            tree_url = f"https://api.github.com/repos/{repo}/git/trees/master?recursive=1"
            tr = self.request(tree_url)
            if not tr or tr.status_code != 200:
                return None, []
            default_branch = "master"

        tree = tr.json().get("tree", [])
        return default_branch, tree

    def get_raw_file(self, repo: str, branch: str, path: str) -> Optional[str]:
        """Fetch raw content of a file."""
        raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{path}"
        try:
            r = self.session.get(raw_url, timeout=20)
            if r.status_code == 200:
                return r.text
        except Exception:
            pass

        # Fallback to GitHub API Blob
        api_url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={branch}"
        r = self.request(api_url)
        if r and r.status_code == 200:
            content = r.json().get("content")
            encoding = r.json().get("encoding")
            if content and encoding == "base64":
                try:
                    return base64.b64decode(content).decode("utf-8")
                except Exception:
                    pass
        return None

    def search_repos(self, query: str, limit: int = 10) -> List[str]:
        """Search GitHub repositories matching query."""
        url = "https://api.github.com/search/repositories"
        params = {"q": query, "per_page": min(limit, 30)}
        r = self.request(url, params=params)
        if r and r.status_code == 200:
            items = r.json().get("items", [])
            return [item["full_name"] for item in items[:limit]]
        return []


class ScraperPipeline:
    """Orchestrates discovery, extraction, conversion, and ingestion."""

    def __init__(
        self,
        client: GitHubClient,
        output_dir: Path,
        db_path: Path = Path("/srv/hermes-installer/hermes-vault.sqlite"),
        chroma_dir: Path = Path("/srv/hermes-installer/vector-registry"),
        dry_run: bool = False,
    ):
        self.client = client
        self.output_dir = output_dir
        self.db_path = db_path
        self.chroma_dir = chroma_dir
        self.dry_run = dry_run
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def discover_repositories(self, provider: str = "all", limit: int = 5) -> Dict[str, List[str]]:
        """Discover candidate repositories per provider via Search API & Seeds."""
        results: Dict[str, List[str]] = {}
        target_providers = [provider] if provider != "all" else list(SEED_REPOSITORIES.keys())

        for prov in target_providers:
            prov_repos = set(SEED_REPOSITORIES.get(prov, []))
            queries = PROVIDER_QUERIES.get(prov, [])

            for query in queries:
                logger.info(f"Searching GitHub for [{prov}]: {query}")
                found = self.client.search_repos(query, limit=limit)
                prov_repos.update(found)
                # Short pause between search queries to respect 30 req/min limit
                time.sleep(1.0)

            results[prov] = sorted(list(prov_repos))
            logger.info(f"Provider [{prov}] discovered {len(results[prov])} candidate repos.")

        return results

    def parse_sources(self, sources: List[str], limit_per_topic: int = 5) -> Dict[str, List[str]]:
        """Parse source URLs, topics, or repo slugs into provider -> [repos] dictionary."""
        discovered: Dict[str, List[str]] = {}

        for src in sources:
            src = src.strip()
            if not src:
                continue

            # Check if topic URL: https://github.com/topics/<topic>
            topic_match = re.search(r"github\.com/topics/([a-zA-Z0-9_-]+)", src)
            if topic_match:
                topic_name = topic_match.group(1)
                prov = self._infer_provider_from_topic(topic_name)
                logger.info(f"Resolving topic source: {topic_name} (inferred provider: {prov})")
                found = self.client.search_repos(f"topic:{topic_name}", limit=limit_per_topic)
                if not found:
                    found = self.client.search_repos(topic_name, limit=limit_per_topic)
                discovered.setdefault(prov, []).extend(found)
                continue

            # Check if repo URL: https://github.com/<owner>/<repo>
            repo_match = re.search(r"github\.com/([^/]+)/([^/#?]+)", src)
            if repo_match:
                repo_slug = f"{repo_match.group(1)}/{repo_match.group(2).rstrip('.git')}"
                prov = self._infer_provider(repo_slug)
                discovered.setdefault(prov, []).append(repo_slug)
                continue

            # If raw owner/repo slug
            if "/" in src and not src.startswith("http"):
                prov = self._infer_provider(src)
                discovered.setdefault(prov, []).append(src)
                continue

        # Deduplicate repos per provider
        for prov in discovered:
            discovered[prov] = sorted(list(set(discovered[prov])))

        return discovered

    def _infer_provider_from_topic(self, topic: str) -> str:
        t = topic.lower()
        if "react" in t:
            return "react"
        if "vercel" in t:
            return "vercel"
        if "agent-team" in t or "team" in t or "agent" in t:
            return "agent_team"
        if "graph" in t or "omnigraph" in t:
            return "omnigraph"
        return "cross_provider"

    def _infer_provider(self, repo_slug: str) -> str:
        lower = repo_slug.lower()
        if "react" in lower:
            return "react"
        if "vercel" in lower:
            return "vercel"
        if "omnigraph" in lower:
            return "omnigraph"
        if any(k in lower for k in ["team", "company", "takt", "aion", "agent"]):
            return "agent_team"
        for prov, seeds in SEED_REPOSITORIES.items():
            if repo_slug in seeds:
                return prov
        return "cross_provider"

    def extract_artifacts_from_repo(
        self,
        repo: str,
        provider: str,
        category: str,
        limit_per_repo: int = 50,
    ) -> List[ExtractedArtifact]:
        """Inspect repository tree and extract candidate files (skills, agents, plugins, MCPs)."""
        logger.info(f"Extracting artifacts from {repo} (provider: {provider})...")
        is_open, lic_name = self.client.check_license(repo)
        if not is_open:
            logger.info(f"Skipping {repo}: non-open source or missing license.")
            return []

        branch, tree = self.client.get_repo_tree(repo)
        if not branch or not tree:
            logger.warning(f"Could not retrieve tree for {repo}")
            return []

        artifacts: List[ExtractedArtifact] = []

        # 1. Check for special aggregate files (like dannyp777's OpenAI plugin JSON)
        for item in tree:
            path = item.get("path", "")
            if path == "chat.openai.com.api.response.json":
                content = self.client.get_raw_file(repo, branch, path)
                if content:
                    artifacts.append(ExtractedArtifact(
                        artifact_type="openai_aggregate",
                        repo=repo,
                        path=path,
                        raw_content=content,
                        metadata={"provider": provider, "category": category, "license": lic_name}
                    ))

        # 2. Extract SKILL.md, mcp-manifest.json, plugin.json, ai-plugin.json, AGENTS.md, etc.
        matched_items = []
        for item in tree:
            path = item.get("path", "")
            lower_path = path.lower()
            if lower_path.endswith("skill.md"):
                matched_items.append(("skill_md", path))
            elif lower_path.endswith("mcp-manifest.json") or lower_path == "mcp-manifest.json":
                matched_items.append(("mcp_manifest", path))
            elif lower_path.endswith(".claude-plugin/plugin.json"):
                matched_items.append(("claude_plugin", path))
            elif lower_path == "plugin.json" or lower_path.endswith("/plugin.json"):
                matched_items.append(("plugin_manifest", path))
            elif lower_path == "plugin.yaml" or lower_path.endswith("/plugin.yaml") or lower_path.endswith("/plugin.yml"):
                matched_items.append(("plugin_manifest", path))
            elif lower_path.endswith(".mcp.json") or lower_path.endswith("mcp-servers.json"):
                matched_items.append(("mcp_server", path))
            elif lower_path == "docs/user/operations/mcp.md" or lower_path.endswith("/mcp.md"):
                matched_items.append(("mcp_server", path))
            elif lower_path == "agents.md" or lower_path.endswith("/agents.md") or lower_path.endswith(".agent.md"):
                matched_items.append(("agent_persona", path))
            elif (lower_path.startswith("agents/") or "/agents/" in lower_path) and (lower_path.endswith(".yaml") or lower_path.endswith(".yml") or lower_path.endswith(".md")):
                matched_items.append(("agent_persona", path))
            elif lower_path.endswith("ai-plugin.json") or (lower_path.startswith("manifests/") and lower_path.endswith(".json")):
                matched_items.append(("openai_plugin", path))

        logger.info(f"Found {len(matched_items)} potential artifact candidates in {repo}.")
        for art_type, path in matched_items[:limit_per_repo]:
            content = self.client.get_raw_file(repo, branch, path)
            if not content:
                continue
            artifacts.append(ExtractedArtifact(
                artifact_type=art_type,
                repo=repo,
                path=path,
                raw_content=content,
                metadata={
                    "provider": provider,
                    "category": category,
                    "license": lic_name,
                    "repo": repo,
                    "branch": branch,
                }
            ))

        return artifacts

    def convert_artifacts(self, artifacts: List[ExtractedArtifact]) -> Dict[str, List[Dict[str, Any]]]:
        """Convert extracted artifacts into normalized Hermes skills, agents, plugins, and MCPs."""
        converted: Dict[str, List[Dict[str, Any]]] = {
            "skills": [],
            "agents": [],
            "plugins": [],
            "mcps": [],
        }

        for art in artifacts:
            try:
                if art.artifact_type == "skill_md":
                    res = convert_skill_md(art.raw_content, art.metadata)
                    converted["skills"].append(res)

                elif art.artifact_type == "mcp_manifest":
                    data = json.loads(art.raw_content)
                    res = convert_mcp_manifest(data, art.metadata)
                    converted["skills"].append(res)
                    rec = convert_mcp_server_record(data, art.metadata)
                    converted["mcps"].append(rec)

                elif art.artifact_type == "mcp_server":
                    if art.path.lower().endswith(".md"):
                        # Documentation describing MCP server (e.g. omnigraph)
                        repo_name = art.repo.split("/")[-1]
                        server_data = {
                            "name": f"{repo_name}-server",
                            "transport": "http",
                            "command": f"{repo_name}-server",
                            "args": ["--port", "8080"],
                            "description": normalize_description(
                                f"Model Context Protocol (MCP) server for {repo_name} providing tool execution and context integration.",
                                fallback_name=f"{repo_name} MCP server"
                            )
                        }
                        rec = convert_mcp_server_record(server_data, art.metadata)
                        converted["mcps"].append(rec)
                    else:
                        data = json.loads(art.raw_content)
                        if isinstance(data, list):
                            for s in data:
                                if isinstance(s, dict):
                                    rec = convert_mcp_server_record(s, art.metadata)
                                    converted["mcps"].append(rec)
                        elif isinstance(data, dict):
                            servers = data.get("mcpServers") or data.get("servers")
                            if isinstance(servers, dict):
                                for s_name, s_cfg in servers.items():
                                    if isinstance(s_cfg, dict):
                                        s_cfg["name"] = s_name
                                        rec = convert_mcp_server_record(s_cfg, art.metadata)
                                        converted["mcps"].append(rec)
                            else:
                                rec = convert_mcp_server_record(data, art.metadata)
                                converted["mcps"].append(rec)

                elif art.artifact_type == "claude_plugin":
                    data = json.loads(art.raw_content)
                    skills_list = convert_claude_plugin(data, art.metadata)
                    converted["skills"].extend(skills_list)
                    plugin_rec = convert_plugin_manifest(data, art.metadata)
                    converted["plugins"].append(plugin_rec)

                elif art.artifact_type == "plugin_manifest":
                    try:
                        data = json.loads(art.raw_content)
                    except Exception:
                        data = yaml.safe_load(art.raw_content)
                    if isinstance(data, dict):
                        plugin_rec = convert_plugin_manifest(data, art.metadata)
                        converted["plugins"].append(plugin_rec)

                elif art.artifact_type == "agent_persona":
                    meta = dict(art.metadata)
                    path_parts = Path(art.path).stem.split(".")
                    raw_stem = path_parts[0]
                    if raw_stem.lower() in ("agents", "agent"):
                        repo_leaf = art.repo.split("/")[-1].replace("-", " ").title().replace(" ", "")
                        meta["name"] = f"{repo_leaf}Agent"
                    else:
                        meta["name"] = raw_stem
                    meta["division"] = art.metadata.get("category", "agent-teams")
                    agent_rec = convert_agent_persona(art.raw_content, meta)
                    converted["agents"].append(agent_rec)

                elif art.artifact_type == "openai_plugin":
                    data = json.loads(art.raw_content)
                    res = convert_openai_plugin(data, metadata=art.metadata)
                    converted["skills"].append(res)
                    plugin_rec = convert_plugin_manifest({
                        "name": data.get("name_for_model"),
                        "description": data.get("description_for_model"),
                    }, art.metadata)
                    converted["plugins"].append(plugin_rec)

                elif art.artifact_type == "openai_aggregate":
                    data = json.loads(art.raw_content)
                    items = data.get("items") or data.get("plugins") or []
                    for item in items[:50]:
                        manifest = item.get("manifest") if isinstance(item, dict) else None
                        if manifest and isinstance(manifest, dict):
                            res = convert_openai_plugin(manifest, metadata=art.metadata)
                            converted["skills"].append(res)
            except Exception as e:
                logger.debug(f"Failed to convert {art.path} in {art.repo}: {e}")

        logger.info(
            f"Converted {len(converted['skills'])} skills, {len(converted['agents'])} agents, "
            f"{len(converted['plugins'])} plugins, {len(converted['mcps'])} MCPs successfully."
        )
        return converted

    def place_artifacts_on_disk(self, converted: Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Path]]:
        """Save converted skills, agents, plugins, and MCPs to disk."""
        saved: Dict[str, List[Path]] = {"skills": [], "agents": [], "plugins": [], "mcps": []}

        # 1. Skills
        for s in converted.get("skills", []):
            category = s.get("category", "community-skills")
            name = s["name"]
            skill_dir = self.output_dir / category / name
            skill_file = skill_dir / "SKILL.md"
            if not self.dry_run:
                skill_dir.mkdir(parents=True, exist_ok=True)
                skill_file.write_text(s["skill_md"], encoding="utf-8")
            saved["skills"].append(skill_file)

        # 2. Agents
        agents_dir = self.output_dir.parent / "harvested-agents"
        for a in converted.get("agents", []):
            div = a.get("division", "agent-teams")
            p_id = a["persona_id"]
            p_dir = agents_dir / div
            p_file = p_dir / f"{p_id}.md"
            if not self.dry_run:
                p_dir.mkdir(parents=True, exist_ok=True)
                p_file.write_text(a["system_prompt"], encoding="utf-8")
            saved["agents"].append(p_file)

        # 3. Plugins
        plugins_dir = self.output_dir.parent / "harvested-plugins"
        for p in converted.get("plugins", []):
            p_name = p["name"]
            p_dir = plugins_dir / p_name
            p_file = p_dir / "plugin.yaml"
            if not self.dry_run:
                p_dir.mkdir(parents=True, exist_ok=True)
                p_file.write_text(yaml.dump(p, sort_keys=False), encoding="utf-8")
            saved["plugins"].append(p_file)

        # 4. MCPs
        mcps_dir = self.output_dir.parent / "harvested-mcps"
        for m in converted.get("mcps", []):
            m_name = m["server_name"]
            m_file = mcps_dir / f"{m_name}.json"
            if not self.dry_run:
                mcps_dir.mkdir(parents=True, exist_ok=True)
                m_file.write_text(json.dumps(m, indent=2), encoding="utf-8")
            saved["mcps"].append(m_file)

        logger.info(
            f"Saved to disk: {len(saved['skills'])} skills, {len(saved['agents'])} agents, "
            f"{len(saved['plugins'])} plugins, {len(saved['mcps'])} MCPs."
        )
        return saved

    def place_skills_on_disk(self, skills: List[Dict[str, Any]]) -> List[Path]:
        """Backward compatible wrapper for placing skills on disk."""
        return self.place_artifacts_on_disk({"skills": skills})["skills"]

    def ingest_into_vault_and_chroma(self, data: Any):
        """Ingest converted artifacts into SQLite Vault and ChromaDB Vector Registry."""
        if self.dry_run:
            logger.info("[DRY-RUN] Would ingest artifacts into Vault & Vector Registry.")
            return

        if not self.db_path.is_file():
            logger.warning(f"Database {self.db_path} not found. Skipping DB ingestion.")
            return

        # Support both List of skills and Dict of categories
        if isinstance(data, list):
            converted = {"skills": data, "agents": [], "plugins": [], "mcps": []}
        elif isinstance(data, dict):
            converted = data
        else:
            logger.warning("Unsupported data type passed to ingestion.")
            return

        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        # Connect to ChromaDB
        chroma_client = None
        try:
            import chromadb
            chroma_client = chromadb.PersistentClient(path=str(self.chroma_dir))
        except Exception as e:
            logger.warning(f"ChromaDB persistent client error: {e}")

        # 1. Ingest Curated Skills
        skills_inserted = 0
        skills_items: List[Tuple[int, str, str, str]] = []
        for s in converted.get("skills", []):
            name = s["name"]
            category = s.get("category", "community-skills")
            desc = s.get("description", "")
            tags = s.get("frontmatter", {}).get("metadata", {}).get("hermes", {}).get("tags", "")
            path = f"skill-library/{category}/{name}/SKILL.md"
            skill_md = s.get("skill_md", "")

            cur.execute("SELECT id FROM curated_skills WHERE name = ?", (name,))
            row = cur.fetchone()
            if row:
                row_id = row[0]
                cur.execute(
                    "UPDATE curated_skills SET description=?, tags=?, path=?, skill_md=? WHERE id=?",
                    (desc, tags, path, skill_md, row_id)
                )
            else:
                cur.execute(
                    "INSERT INTO curated_skills (name, category, description, tags, path, skill_md) VALUES (?, ?, ?, ?, ?, ?)",
                    (name, category, desc, tags, path, skill_md)
                )
                row_id = cur.lastrowid
                skills_inserted += 1
                skills_items.append((row_id, name, category, desc))
                try:
                    cur.execute(
                        "INSERT INTO curated_skills_fts (rowid, name, category, description, tags, skill_md) VALUES (?, ?, ?, ?, ?, ?)",
                        (row_id, name, category, desc, tags, skill_md)
                    )
                except Exception as e:
                    logger.debug(f"FTS5 insertion error for {name}: {e}")

            # Sync to live runtime directory
            runtime_dir = Path("/home/hermes/.hermes/skill-library") / category / name
            try:
                runtime_dir.mkdir(parents=True, exist_ok=True)
                (runtime_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
            except Exception as e:
                logger.debug(f"Could not write to runtime skill-library: {e}")

        if chroma_client and skills_items:
            try:
                coll = chroma_client.get_or_create_collection("skills_semantic")
                batch_size = 100
                for i in range(0, len(skills_items), batch_size):
                    batch = skills_items[i : i + batch_size]
                    ids = [str(item[0]) for item in batch]
                    docs = [f"{item[1]} [{item[2]}]: {item[3]}" for item in batch]
                    metas = [{"name": item[1], "category": item[2]} for item in batch]
                    coll.upsert(ids=ids, documents=docs, metadatas=metas)
            except Exception as e:
                logger.warning(f"ChromaDB skills upsert error: {e}")

        # 2. Ingest Agent Personas
        agents_inserted = 0
        agents_items: List[Tuple[int, str, str, str, str]] = []
        for a in converted.get("agents", []):
            persona_id = a["persona_id"]
            name = a["name"]
            division = a.get("division", "agent-teams")
            role = a.get("role", f"{name}.Agent")
            agent_type = a.get("type", "general")
            file_path = a.get("file_path", f"agent-library/{division}/{persona_id}.md")
            system_prompt = a.get("system_prompt", "")

            cur.execute("SELECT id FROM agent_personas WHERE persona_id = ?", (persona_id,))
            row = cur.fetchone()
            if row:
                row_id = row[0]
                cur.execute(
                    "UPDATE agent_personas SET name=?, division=?, role=?, type=?, file_path=?, system_prompt=? WHERE id=?",
                    (name, division, role, agent_type, file_path, system_prompt, row_id)
                )
            else:
                cur.execute(
                    "INSERT INTO agent_personas (persona_id, name, division, role, type, file_path, system_prompt) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (persona_id, name, division, role, agent_type, file_path, system_prompt)
                )
                row_id = cur.lastrowid
                agents_inserted += 1
                agents_items.append((row_id, persona_id, name, division, role))
                try:
                    cur.execute(
                        "INSERT INTO agent_personas_fts (rowid, name, division, role, system_prompt) VALUES (?, ?, ?, ?, ?)",
                        (row_id, name, division, role, system_prompt)
                    )
                except Exception as e:
                    logger.debug(f"FTS5 insertion error for agent {persona_id}: {e}")

            # Sync to live runtime directory
            runtime_agent_dir = Path("/home/hermes/.hermes/agent-library") / division
            try:
                runtime_agent_dir.mkdir(parents=True, exist_ok=True)
                (runtime_agent_dir / f"{persona_id}.md").write_text(system_prompt, encoding="utf-8")
            except Exception as e:
                logger.debug(f"Could not write to runtime agent-library: {e}")

        if chroma_client and agents_items:
            try:
                coll = chroma_client.get_or_create_collection("agents_semantic")
                ids = [str(item[0]) for item in agents_items]
                docs = [f"{item[2]} ({item[3]}) - Role: {item[4]}" for item in agents_items]
                metas = [{"persona_id": item[1], "division": item[3]} for item in agents_items]
                coll.upsert(ids=ids, documents=docs, metadatas=metas)
            except Exception as e:
                logger.warning(f"ChromaDB agents upsert error: {e}")

        # 3. Ingest Plugins
        plugins_inserted = 0
        plugins_items: List[Tuple[int, str, str]] = []
        for p in converted.get("plugins", []):
            p_name = p["name"]
            version = p.get("version", "1.0.0")
            path = p.get("path", f"plugins/{p_name}")
            is_active = p.get("is_active", 1)
            description = p.get("description", "")

            cur.execute("SELECT id FROM plugins WHERE name = ?", (p_name,))
            row = cur.fetchone()
            if row:
                row_id = row[0]
                cur.execute(
                    "UPDATE plugins SET version=?, path=?, is_active=?, description=? WHERE id=?",
                    (version, path, is_active, description, row_id)
                )
            else:
                cur.execute(
                    "INSERT INTO plugins (name, version, path, is_active, description) VALUES (?, ?, ?, ?, ?)",
                    (p_name, version, path, is_active, description)
                )
                row_id = cur.lastrowid
                plugins_inserted += 1
                plugins_items.append((row_id, p_name, description))

            # Sync to live runtime directory
            runtime_plug_dir = Path("/home/hermes/.hermes/plugins") / p_name
            try:
                runtime_plug_dir.mkdir(parents=True, exist_ok=True)
                (runtime_plug_dir / "plugin.yaml").write_text(yaml.dump(p, sort_keys=False), encoding="utf-8")
            except Exception as e:
                logger.debug(f"Could not write to runtime plugins: {e}")

        if chroma_client and plugins_items:
            try:
                coll = chroma_client.get_or_create_collection("plugins_semantic")
                ids = [str(item[0]) for item in plugins_items]
                docs = [f"{item[1]}: {item[2]}" for item in plugins_items]
                metas = [{"name": item[1]} for item in plugins_items]
                coll.upsert(ids=ids, documents=docs, metadatas=metas)
            except Exception as e:
                logger.warning(f"ChromaDB plugins upsert error: {e}")

        # 4. Ingest MCP Servers
        mcps_inserted = 0
        mcps_items: List[Tuple[int, str, str, str]] = []
        for m in converted.get("mcps", []):
            s_name = m["server_name"]
            transport = m.get("transport", "stdio")
            command = m.get("command", "")
            args = m.get("args", "[]")
            env = m.get("env", "{}")
            source_repo = m.get("source_repo", "")
            is_recommended = m.get("is_recommended", 0)
            desc = m.get("description", "")
            raw_config = m.get("raw_config", "{}")

            cur.execute("SELECT id FROM mcp_servers WHERE server_name = ?", (s_name,))
            row = cur.fetchone()
            if row:
                row_id = row[0]
                cur.execute(
                    "UPDATE mcp_servers SET transport=?, command=?, args=?, env=?, source_repo=?, description=?, raw_config=? WHERE id=?",
                    (transport, command, args, env, source_repo, desc, raw_config, row_id)
                )
            else:
                cur.execute(
                    "INSERT INTO mcp_servers (server_name, transport, command, args, env, source_repo, is_recommended, description, raw_config) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (s_name, transport, command, args, env, source_repo, is_recommended, desc, raw_config)
                )
                row_id = cur.lastrowid
                mcps_inserted += 1
                mcps_items.append((row_id, s_name, transport, desc))
                try:
                    cur.execute(
                        "INSERT INTO mcp_servers_fts (rowid, server_name, description, raw_config) VALUES (?, ?, ?, ?)",
                        (row_id, s_name, desc, raw_config)
                    )
                except Exception as e:
                    logger.debug(f"FTS5 insertion error for MCP {s_name}: {e}")

        if chroma_client and mcps_items:
            try:
                coll = chroma_client.get_or_create_collection("mcp_semantic")
                ids = [str(item[0]) for item in mcps_items]
                docs = [f"{item[1]} ({item[2]}): {item[3]}" for item in mcps_items]
                metas = [{"server_name": item[1]} for item in mcps_items]
                coll.upsert(ids=ids, documents=docs, metadatas=metas)
            except Exception as e:
                logger.warning(f"ChromaDB MCP upsert error: {e}")

        # Update metadata counts
        cur.execute("SELECT COUNT(*) FROM curated_skills")
        total_skills = cur.fetchone()[0]
        cur.execute("REPLACE INTO metadata (key, value) VALUES ('curated_skills_count', ?)", (str(total_skills),))

        cur.execute("SELECT COUNT(*) FROM agent_personas")
        total_agents = cur.fetchone()[0]
        cur.execute("REPLACE INTO metadata (key, value) VALUES ('agent_personas_count', ?)", (str(total_agents),))

        cur.execute("SELECT COUNT(*) FROM plugins")
        total_plugins = cur.fetchone()[0]
        cur.execute("REPLACE INTO metadata (key, value) VALUES ('plugins_count', ?)", (str(total_plugins),))

        cur.execute("SELECT COUNT(*) FROM mcp_servers")
        total_mcps = cur.fetchone()[0]
        cur.execute("REPLACE INTO metadata (key, value) VALUES ('mcp_servers_count', ?)", (str(total_mcps),))

        conn.commit()
        conn.close()

        logger.info(
            f"Vault Ingestion Complete: +{skills_inserted} skills (total: {total_skills}), "
            f"+{agents_inserted} agents (total: {total_agents}), "
            f"+{plugins_inserted} plugins (total: {total_plugins}), "
            f"+{mcps_inserted} MCPs (total: {total_mcps})."
        )

        # Fix filesystem permissions
        if os.geteuid() == 0:
            os.system("chown -R hermes:hermes /home/hermes/.hermes/skill-library /home/hermes/.hermes/agent-library /home/hermes/.hermes/plugins /home/hermes/.hermes/hermes-vault.sqlite /home/hermes/.hermes/vector-registry 2>/dev/null || true")
            os.system("chown -R hermes-installer:hermes-installer /srv/hermes-installer/harvested-* 2>/dev/null || true")

    def run_pipeline(
        self,
        provider: str = "all",
        seeds_only: bool = False,
        limit_repos: int = 3,
        limit_artifacts_per_repo: int = 50,
        ingest: bool = True,
        sources: Optional[List[str]] = None,
    ):
        """Execute full end-to-end scraper pipeline."""
        logger.info("=== Starting Hermes Ecosystem Scraper Pipeline ===")

        # 1. Discovery
        if sources:
            logger.info(f"Targeting specific sources: {sources}")
            discovered = self.parse_sources(sources)
        elif seeds_only:
            logger.info("Operating in seeds-only mode. Using curated seed repositories.")
            discovered = SEED_REPOSITORIES if provider == "all" else {provider: SEED_REPOSITORIES.get(provider, [])}
        else:
            discovered = self.discover_repositories(provider=provider, limit=limit_repos)

        # 2. Extraction
        all_artifacts: List[ExtractedArtifact] = []
        for prov, repos in discovered.items():
            category = DEFAULT_CATEGORIES.get(prov, "community-skills")
            for repo in repos:
                artifacts = self.extract_artifacts_from_repo(
                    repo,
                    provider=prov,
                    category=category,
                    limit_per_repo=limit_artifacts_per_repo,
                )
                all_artifacts.extend(artifacts)

        logger.info(f"Total extracted artifacts: {len(all_artifacts)}")

        # 3. Conversion
        converted_data = self.convert_artifacts(all_artifacts)

        # 4. Placement on Disk
        saved_paths = self.place_artifacts_on_disk(converted_data)

        # 5. Ingestion into Vault & Vector Registry
        if ingest and any(converted_data.values()):
            self.ingest_into_vault_and_chroma(converted_data)

        logger.info("=== Hermes Scraper Pipeline Finished Successfully ===")
        return converted_data


def main():
    parser = argparse.ArgumentParser(
        description="Hermes GitHub Scraper & Harvester for AI Skills, Agents, MCPs, and Plugins."
    )
    parser.add_argument("--discover", action="store_true", help="Discover candidate repositories")
    parser.add_argument("--extract", action="store_true", help="Extract artifacts from repositories")
    parser.add_argument("--convert", action="store_true", help="Convert extracted artifacts")
    parser.add_argument("--ingest", action="store_true", help="Ingest converted skills into SQLite and ChromaDB")
    parser.add_argument("--all", action="store_true", help="Run full end-to-end pipeline")
    parser.add_argument("--seeds-only", action="store_true", help="Restrict to curated seed repositories")
    parser.add_argument("--sources", nargs="+", help="Specific repository URLs, topic URLs, or slugs to harvest from")
    parser.add_argument("--provider", default="all", choices=list(SEED_REPOSITORIES.keys()) + ["all"], help="Filter by AI provider")
    parser.add_argument("--limit-repos", type=int, default=3, help="Max repos per provider to crawl")
    parser.add_argument("--limit-artifacts", type=int, default=50, help="Max artifacts per repository")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without writing files or mutating databases")
    parser.add_argument("--output-dir", default="/srv/hermes-installer/harvested-skills", help="Directory to save converted skills")
    parser.add_argument("--token", help="GitHub Personal Access Token (defaults to GITHUB_TOKEN or .git-credentials)")

    args = parser.parse_args()

    client = GitHubClient(token=args.token)
    pipeline = ScraperPipeline(
        client=client,
        output_dir=Path(args.output_dir),
        dry_run=args.dry_run,
    )

    if args.discover and not args.all:
        if args.sources:
            discovered = pipeline.parse_sources(args.sources)
        else:
            discovered = pipeline.discover_repositories(provider=args.provider, limit=args.limit_repos)
        print(json.dumps(discovered, indent=2))
        return

    # Default to running the full pipeline if --all or no specific phase flags provided
    pipeline.run_pipeline(
        provider=args.provider,
        seeds_only=args.seeds_only,
        limit_repos=args.limit_repos,
        limit_artifacts_per_repo=args.limit_artifacts,
        ingest=args.ingest or args.all or not (args.discover or args.extract or args.convert),
        sources=args.sources,
    )


if __name__ == "__main__":
    main()
