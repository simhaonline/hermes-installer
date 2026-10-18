#!/usr/bin/env python3
"""Unit tests for converter.py."""

import unittest
from converter import (
    convert_skill_md,
    convert_mcp_manifest,
    convert_claude_plugin,
    convert_openai_plugin,
    normalize_name,
    normalize_description,
    ensure_markdown_sections,
    parse_frontmatter,
    NAME_PATTERN,
)


class TestConverter(unittest.TestCase):

    def test_normalize_name(self):
        self.assertEqual(normalize_name("My Super Skill!"), "my-super-skill")
        self.assertEqual(normalize_name("---ugly___name---"), "ugly-name")
        self.assertEqual(normalize_name("a" * 100), "a" * 64)
        self.assertTrue(NAME_PATTERN.match(normalize_name("valid-skill-123")))
        self.assertTrue(NAME_PATTERN.match(normalize_name("UPPERCASE_NAME")))
        self.assertEqual(normalize_name(""), "custom-skill")

    def test_normalize_description(self):
        desc = "  Short   description \n with newlines. "
        normalized = normalize_description(desc)
        self.assertEqual(normalized, "Short description with newlines.")
        self.assertTrue(len(normalized) <= 1024)

        long_desc = "x" * 2000
        truncated = normalize_description(long_desc)
        self.assertEqual(len(truncated), 1024)
        self.assertTrue(truncated.endswith("..."))

    def test_parse_frontmatter(self):
        content = """---
name: test-skill
description: A test skill
---

# Title
Some content
"""
        fm, body = parse_frontmatter(content)
        self.assertEqual(fm.get("name"), "test-skill")
        self.assertEqual(fm.get("description"), "A test skill")
        self.assertIn("# Title", body)

    def test_convert_skill_md_agentskills_spec(self):
        raw = """---
name: sample-skill
description: Sample skill for testing
---

# Sample Skill

Some documentation.
"""
        result = convert_skill_md(raw, {"category": "test-cat", "provider": "test-prov"})
        self.assertEqual(result["name"], "sample-skill")
        self.assertEqual(result["category"], "test-cat")
        self.assertEqual(result["frontmatter"]["metadata"]["hermes"]["provider"], "test-prov")

        # Check required sections
        body = result["body"]
        self.assertIn("## When to Use", body)
        self.assertIn("## Procedure", body)
        self.assertIn("## Pitfalls", body)
        self.assertIn("## Verification", body)

        # Re-parse generated SKILL.md
        fm, re_body = parse_frontmatter(result["skill_md"])
        self.assertEqual(fm["name"], "sample-skill")
        self.assertIn("## When to Use", re_body)

    def test_convert_mcp_manifest(self):
        manifest = {
            "name": "sqlite-query",
            "description": "Execute queries against SQLite databases",
            "command": "python3",
            "args": ["-m", "mcp_sqlite", "--db", "/data/test.db"],
            "transport": "stdio",
            "env": {"DEBUG": "1"}
        }
        result = convert_mcp_manifest(manifest, {"category": "database-mcp", "author": "TestAuthor"})
        self.assertEqual(result["name"], "sqlite-query-mcp")
        self.assertIn("Use the sqlite-query MCP server", result["description"])
        self.assertIn("## When to Use", result["body"])
        self.assertIn("## Procedure", result["body"])
        self.assertIn("## Pitfalls", result["body"])
        self.assertIn("## Verification", result["body"])
        self.assertIn("mcp_sqlite", result["skill_md"])
        self.assertEqual(result["frontmatter"]["metadata"]["hermes"]["author"], "TestAuthor")

    def test_convert_claude_plugin_with_skills_array(self):
        plugin = {
            "name": "dev-assistant",
            "version": "2.1.0",
            "description": "Development tools for Claude",
            "author": "Anthropic",
            "skills": [
                {"name": "git-helper", "description": "Helper for git commands"},
                {"name": "code-lint", "description": "Lints python and typescript"}
            ]
        }
        results = convert_claude_plugin(plugin, {"category": "developer-tools"})
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["name"], "git-helper")
        self.assertEqual(results[1]["name"], "code-lint")
        for r in results:
            self.assertIn("## When to Use", r["body"])
            self.assertIn("## Procedure", r["body"])
            self.assertIn("## Pitfalls", r["body"])
            self.assertIn("## Verification", r["body"])

    def test_convert_claude_plugin_standalone(self):
        plugin = {
            "name": "single-plugin",
            "version": "1.0.0",
            "description": "Standalone plugin with no skills array",
            "author": "Community"
        }
        results = convert_claude_plugin(plugin)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "single-plugin")
        self.assertIn("## When to Use", results[0]["body"])

    def test_convert_openai_plugin(self):
        ai_plugin = {
            "name_for_model": "weatherBot",
            "name_for_human": "Weather Bot",
            "description_for_model": "Get live weather forecasts and alerts.",
            "description_for_human": "Accurate global weather forecasts.",
            "auth": {"type": "service_http"},
            "api": {"url": "https://api.weatherbot.com/openapi.json"}
        }
        openapi = {
            "paths": {
                "/forecast": {
                    "get": {
                        "operationId": "getForecast",
                        "summary": "Retrieve 7-day weather forecast"
                    }
                }
            }
        }
        result = convert_openai_plugin(ai_plugin, openapi_spec=openapi)
        self.assertEqual(result["name"], "weatherbot-plugin")
        self.assertIn("weather", result["description"].lower())
        self.assertIn("getForecast", result["body"])
        self.assertIn("## When to Use", result["body"])
        self.assertIn("## Procedure", result["body"])
        self.assertIn("## Pitfalls", result["body"])
        self.assertIn("## Verification", result["body"])

    def test_convert_agent_persona(self):
        from converter import convert_agent_persona
        content = """---
name: ReactFullStackSpecialist
role: ReactFullStackSpecialist.Agent
description: Specialist in React, Next.js, and Full-Stack architecture
---
# React Specialist
Executes full-stack React workflows.
"""
        res = convert_agent_persona(content, {"division": "react-ecosystem"})
        self.assertEqual(res["name"], "ReactFullStackSpecialist")
        self.assertEqual(res["persona_id"], "ReactFullStackSpecialist.agent")
        self.assertEqual(res["division"], "react-ecosystem")
        self.assertIn("ReactFullStackSpecialist", res["system_prompt"])

    def test_convert_plugin_manifest(self):
        from converter import convert_plugin_manifest
        manifest = {
            "name": "react-skills",
            "version": "1.0.0",
            "description": "React ecosystem tools and skills"
        }
        res = convert_plugin_manifest(manifest)
        self.assertEqual(res["name"], "react-skills")
        self.assertEqual(res["version"], "1.0.0")
    def test_convert_mcp_server_record(self):
        from converter import convert_mcp_server_record
        data = {
            "name": "hello-echo-mcp",
            "description": "Demo MCP server",
            "transport": {
                "type": "stdio",
                "command": "echo",
                "args": ["hello-mcp"]
            }
        }
        res = convert_mcp_server_record(data, {"repo": "iOfficeAI/AionUi", "is_recommended": 1})
        self.assertEqual(res["server_name"], "hello-echo-mcp")
        self.assertEqual(res["transport"], "stdio")
        self.assertEqual(res["command"], "echo")
        self.assertEqual(res["args"], '["hello-mcp"]')
        self.assertEqual(res["source_repo"], "iOfficeAI/AionUi")
        self.assertEqual(res["is_recommended"], 1)


if __name__ == "__main__":
    unittest.main()

