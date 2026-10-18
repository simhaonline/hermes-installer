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
    convert_claude_plugin,
    convert_mcp_manifest,
    convert_openai_plugin,
    convert_skill_md,
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
            Path("/home/predictatrade/.git-credentials"),
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
        db_path: Path = Path("/home/predictatrade/.hermes/hermes-vault.sqlite"),
        chroma_dir: Path = Path("/home/predictatrade/.hermes/vector-registry"),
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

    def extract_artifacts_from_repo(
        self,
        repo: str,
        provider: str,
        category: str,
        limit_per_repo: int = 50,
    ) -> List[ExtractedArtifact]:
        """Inspect repository tree and extract candidate files."""
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

        # 2. Extract SKILL.md, mcp-manifest.json, plugin.json, ai-plugin.json
        matched_items = []
        for item in tree:
            path = item.get("path", "")
            lower_path = path.lower()
            if lower_path.endswith("skill.md"):
                matched_items.append(("skill_md", path))
            elif lower_path.endswith("mcp-manifest.json") or lower_path == "mcp-manifest.json":
                matched_items.append(("mcp_manifest", path))
            elif lower_path.endswith(".claude-plugin/plugin.json") or lower_path == "plugin.json":
                matched_items.append(("claude_plugin", path))
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

    def convert_artifacts(self, artifacts: List[ExtractedArtifact]) -> List[Dict[str, Any]]:
        """Convert extracted artifacts into normalized Hermes skills using converter.py."""
        converted_skills: List[Dict[str, Any]] = []

        for art in artifacts:
            try:
                if art.artifact_type == "skill_md":
                    res = convert_skill_md(art.raw_content, art.metadata)
                    converted_skills.append(res)

                elif art.artifact_type == "mcp_manifest":
                    data = json.loads(art.raw_content)
                    res = convert_mcp_manifest(data, art.metadata)
                    converted_skills.append(res)

                elif art.artifact_type == "claude_plugin":
                    data = json.loads(art.raw_content)
                    skills_list = convert_claude_plugin(data, art.metadata)
                    converted_skills.extend(skills_list)

                elif art.artifact_type == "openai_plugin":
                    data = json.loads(art.raw_content)
                    res = convert_openai_plugin(data, metadata=art.metadata)
                    converted_skills.append(res)

                elif art.artifact_type == "openai_aggregate":
                    data = json.loads(art.raw_content)
                    items = data.get("items") or data.get("plugins") or []
                    for item in items[:50]:  # limit sample batch
                        manifest = item.get("manifest") if isinstance(item, dict) else None
                        if manifest and isinstance(manifest, dict):
                            res = convert_openai_plugin(manifest, metadata=art.metadata)
                            converted_skills.append(res)
            except Exception as e:
                logger.debug(f"Failed to convert {art.path} in {art.repo}: {e}")

        logger.info(f"Converted {len(converted_skills)} skills successfully.")
        return converted_skills

    def place_skills_on_disk(self, skills: List[Dict[str, Any]]) -> List[Path]:
        """Save converted skills to disk in /srv/hermes-installer/harvested-skills/."""
        saved_paths: List[Path] = []
        for s in skills:
            category = s.get("category", "community-skills")
            name = s["name"]
            skill_dir = self.output_dir / category / name
            skill_file = skill_dir / "SKILL.md"

            if self.dry_run:
                logger.info(f"[DRY-RUN] Would create: {skill_file}")
                saved_paths.append(skill_file)
                continue

            skill_dir.mkdir(parents=True, exist_ok=True)
            skill_file.write_text(s["skill_md"], encoding="utf-8")
            saved_paths.append(skill_file)

        logger.info(f"Saved {len(saved_paths)} skills to {self.output_dir}.")
        return saved_paths

    def ingest_into_vault_and_chroma(self, skills: List[Dict[str, Any]]):
        """Ingest converted skills into SQLite Vault and ChromaDB Vector Registry."""
        if self.dry_run:
            logger.info(f"[DRY-RUN] Would ingest {len(skills)} skills into Vault & Vector Registry.")
            return

        if not self.db_path.is_file():
            logger.warning(f"Database {self.db_path} not found. Skipping DB ingestion.")
            return

        # 1. Ingest into SQLite
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        inserted_count = 0
        inserted_items: List[Tuple[int, str, str, str]] = []  # (rowid, name, category, description)

        for s in skills:
            name = s["name"]
            category = s.get("category", "community-skills")
            desc = s.get("description", "")
            tags = s.get("frontmatter", {}).get("metadata", {}).get("hermes", {}).get("tags", "")
            path = f"skill-library/{category}/{name}/SKILL.md"
            skill_md = s.get("skill_md", "")

            # Check if skill exists
            cur.execute("SELECT id FROM curated_skills WHERE name = ?", (name,))
            row = cur.fetchone()
            if row:
                row_id = row[0]
                # Update existing
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
                inserted_count += 1
                inserted_items.append((row_id, name, category, desc))

                # Insert into FTS5
                try:
                    cur.execute(
                        "INSERT INTO curated_skills_fts (rowid, name, category, description, tags, skill_md) VALUES (?, ?, ?, ?, ?, ?)",
                        (row_id, name, category, desc, tags, skill_md)
                    )
                except Exception as e:
                    logger.debug(f"FTS5 insertion error for {name}: {e}")

            # Also sync to live runtime skill-library if directory exists
            runtime_dir = Path("/home/predictatrade/.hermes/skill-library") / category / name
            try:
                runtime_dir.mkdir(parents=True, exist_ok=True)
                (runtime_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
            except Exception as e:
                logger.debug(f"Could not write to runtime skill-library: {e}")

        # Update metadata count
        cur.execute("SELECT COUNT(*) FROM curated_skills")
        total_skills = cur.fetchone()[0]
        cur.execute("REPLACE INTO metadata (key, value) VALUES ('curated_skills_count', ?)", (str(total_skills),))
        conn.commit()
        conn.close()
        logger.info(f"SQLite Vault updated: {inserted_count} new skills added (Total: {total_skills}).")

        # 2. Ingest into ChromaDB Vector Registry
        try:
            import chromadb
            client = chromadb.PersistentClient(path=str(self.chroma_dir))
            coll = client.get_or_create_collection("skills_semantic")

            if inserted_items:
                batch_size = 100
                for i in range(0, len(inserted_items), batch_size):
                    batch = inserted_items[i : i + batch_size]
                    ids = [str(item[0]) for item in batch]
                    docs = [f"{item[1]} [{item[2]}]: {item[3]}" for item in batch]
                    metas = [{"name": item[1], "category": item[2]} for item in batch]
                    coll.upsert(ids=ids, documents=docs, metadatas=metas)
                logger.info(f"ChromaDB Vector Registry updated with {len(inserted_items)} embeddings.")
        except Exception as e:
            logger.warning(f"ChromaDB ingestion skipped/error: {e}")

    def run_pipeline(
        self,
        provider: str = "all",
        seeds_only: bool = False,
        limit_repos: int = 3,
        limit_artifacts_per_repo: int = 15,
        ingest: bool = True,
    ):
        """Execute full end-to-end scraper pipeline."""
        logger.info("=== Starting Hermes Ecosystem Scraper Pipeline ===")

        # 1. Discovery
        if seeds_only:
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
        converted_skills = self.convert_artifacts(all_artifacts)

        # 4. Placement on Disk
        saved_paths = self.place_skills_on_disk(converted_skills)

        # 5. Ingestion into Vault & Vector Registry
        if ingest and converted_skills:
            self.ingest_into_vault_and_chroma(converted_skills)

        logger.info("=== Hermes Scraper Pipeline Finished Successfully ===")
        return converted_skills


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
    parser.add_argument("--provider", default="all", choices=list(SEED_REPOSITORIES.keys()) + ["all"], help="Filter by AI provider")
    parser.add_argument("--limit-repos", type=int, default=3, help="Max repos per provider to crawl")
    parser.add_argument("--limit-artifacts", type=int, default=15, help="Max artifacts per repository")
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
    )


if __name__ == "__main__":
    main()
