#!/usr/bin/env python3
"""Unit tests for scraper.py."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from scraper import ExtractedArtifact, GitHubClient, ScraperPipeline


class TestScraper(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.cache_dir = Path(self.temp_dir.name) / ".cache"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_github_client_token_discovery(self):
        with patch.dict("os.environ", {"GITHUB_TOKEN": "mock_token_123"}):
            client = GitHubClient(cache_dir=self.cache_dir)
            self.assertEqual(client.token, "mock_token_123")

    @patch("requests.Session.get")
    def test_check_license(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.headers = {"X-RateLimit-Remaining": "4999"}
        mock_resp.json.return_value = {
            "license": {"key": "mit", "name": "MIT License", "spdx_id": "MIT"}
        }
        mock_get.return_value = mock_resp

        client = GitHubClient(token="mock_token", cache_dir=self.cache_dir)
        is_open, lic_name = client.check_license("test-org/test-repo")
        self.assertTrue(is_open)
        self.assertEqual(lic_name, "MIT License")

    def test_convert_extracted_artifacts(self):
        client = GitHubClient(token="mock_token", cache_dir=self.cache_dir)
        output_dir = Path(self.temp_dir.name) / "harvested"
        pipeline = ScraperPipeline(client=client, output_dir=output_dir, dry_run=True)

        skill_artifact = ExtractedArtifact(
            artifact_type="skill_md",
            repo="org/repo",
            path="skills/calculator/SKILL.md",
            raw_content="""---
name: math-calculator
description: Performs calculation
---
# Math Calculator
Calculates math formulas.
""",
            metadata={"category": "mathematics", "provider": "test"}
        )

        mcp_artifact = ExtractedArtifact(
            artifact_type="mcp_manifest",
            repo="org/mcp-repo",
            path="mcp-manifest.json",
            raw_content=json.dumps({
                "name": "calc-service",
                "description": "Calculates numbers",
                "command": "node",
                "args": ["calc.js"]
            }),
            metadata={"category": "mcp-servers", "provider": "mcp"}
        )

        converted = pipeline.convert_artifacts([skill_artifact, mcp_artifact])
        self.assertEqual(len(converted), 2)
        self.assertEqual(converted[0]["name"], "math-calculator")
        self.assertEqual(converted[1]["name"], "calc-service-mcp")

        # Check agentskills.io sections
        for s in converted:
            self.assertIn("## When to Use", s["body"])
            self.assertIn("## Procedure", s["body"])
            self.assertIn("## Pitfalls", s["body"])
            self.assertIn("## Verification", s["body"])


if __name__ == "__main__":
    unittest.main()
