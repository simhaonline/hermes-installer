#!/usr/bin/env python3
"""Unit tests for Hermes Hybrid Vector Registry API and Dashboard server."""

import json
import sqlite3
import unittest
import urllib.parse
from http.server import HTTPServer
from io import BytesIO
from pathlib import Path
from unittest.mock import MagicMock, patch

# Import the handler from hermes-registry
import sys
sys.path.insert(0, "/srv/hermes-installer")
# Dynamically import hermes-registry since it has a hyphen in filename and no .py extension
import importlib.util
from importlib.machinery import SourceFileLoader
loader = SourceFileLoader("hermes_registry", "/srv/hermes-installer/hermes-registry")
spec = importlib.util.spec_from_loader("hermes_registry", loader)
hermes_registry = importlib.util.module_from_spec(spec)
loader.exec_module(hermes_registry)


class MockHTTPHandler(hermes_registry.RegistryHTTPHandler):
    """Subclass RegistryHTTPHandler to capture responses in memory without a live socket."""

    def __init__(self, path, method="GET", body=b""):
        self.path = path
        self.command = method
        self.headers = {"Content-Length": str(len(body))}
        self.rfile = BytesIO(body)
        self.wfile = BytesIO()
        self.response_status = None
        self.response_headers = {}

    def send_response(self, code, message=None):
        self.response_status = code

    def send_header(self, keyword, value):
        self.response_headers[keyword.lower()] = value

    def end_headers(self):
        pass

    def log_message(self, format, *args):
        pass  # suppress logging during tests


class TestRegistryAPI(unittest.TestCase):
    """Test suite verifying all REST API endpoints and dashboard delivery."""

    def test_get_dashboard_html(self):
        handler = MockHTTPHandler("/")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        self.assertIn("text/html", handler.response_headers.get("content-type", ""))
        body = handler.wfile.getvalue().decode("utf-8")
        self.assertIn("Hermes Agent Enterprise", body)
        self.assertIn("design-tokens", body.lower())

    def test_api_stats(self):
        handler = MockHTTPHandler("/api/stats")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        data = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertEqual(data.get("status"), "online")
        counts = data.get("counts", {})
        self.assertGreaterEqual(counts.get("curated_skills", 0), 19000)
        self.assertGreaterEqual(counts.get("agent_personas", 0), 500)
        self.assertGreaterEqual(counts.get("profiles", 0), 60)
        self.assertGreaterEqual(counts.get("mcp_servers", 0), 4000)
        self.assertIn("chromadb", data)

    def test_api_categories(self):
        handler = MockHTTPHandler("/api/categories")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        data = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 50)
        self.assertIn("category", data[0])
        self.assertIn("count", data[0])

    def test_api_profiles(self):
        handler = MockHTTPHandler("/api/profiles")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        data = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertIn("profiles", data)
        self.assertIn("active_map", data)
        self.assertGreaterEqual(len(data["profiles"]), 60)

    def test_api_mcp_and_plugins(self):
        handler = MockHTTPHandler("/api/mcp-and-plugins")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        data = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertIn("mcps", data)
        self.assertIn("plugins", data)
        self.assertGreaterEqual(len(data["mcps"]), 40)
        self.assertGreaterEqual(len(data["plugins"]), 30)

    def test_api_agents_list(self):
        handler = MockHTTPHandler("/api/agents?limit=5")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        data = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertIn("results", data)
        self.assertIn("total", data)
        self.assertGreaterEqual(data["total"], 550)
        self.assertEqual(len(data["results"]), 5)
        agent = data["results"][0]
        self.assertIn("name", agent)
        self.assertIn("division", agent)
        self.assertIn("role", agent)

    def test_api_agents_filter(self):
        handler = MockHTTPHandler("/api/agents?division=agency-agents&limit=10")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        data = json.loads(handler.wfile.getvalue().decode("utf-8"))
        for agent in data["results"]:
            self.assertEqual(agent["division"], "agency-agents")

    def test_api_agent_detail(self):
        # Fetch one valid agent first
        h_list = MockHTTPHandler("/api/agents?limit=1")
        h_list.do_GET()
        d_list = json.loads(h_list.wfile.getvalue().decode("utf-8"))
        agent_name = d_list["results"][0]["name"]

        handler = MockHTTPHandler(f"/api/agent?name={urllib.parse.quote(agent_name)}")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        data = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertEqual(data["name"], agent_name)
        self.assertIn("system_prompt", data)
        self.assertTrue(len(data["system_prompt"]) > 0)

    def test_api_agent_not_found(self):
        handler = MockHTTPHandler("/api/agent?name=NonExistentPersona12345")
        handler.do_GET()
        self.assertEqual(handler.response_status, 404)

    def test_api_mcp_search(self):
        handler = MockHTTPHandler("/api/mcp-search?q=postgres&limit=5")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        data = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertIn("results", data)
        self.assertIn("total", data)
        self.assertGreater(data["total"], 0)
        self.assertLessEqual(len(data["results"]), 5)

    def test_api_diagnostics(self):
        handler = MockHTTPHandler("/api/diagnostics")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        data = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertEqual(data.get("status"), "healthy")
        self.assertEqual(data.get("sqlite_integrity"), "ok")
        self.assertGreater(data.get("sqlite_size_mb", 0), 200)
        self.assertIn("server_time_utc", data)
        self.assertIn("python_version", data)

    def test_api_search_skills(self):
        handler = MockHTTPHandler("/api/search?q=react&limit=5")
        handler.do_GET()
        self.assertEqual(handler.response_status, 200)
        data = json.loads(handler.wfile.getvalue().decode("utf-8"))
        self.assertIn("results", data)
        self.assertGreater(len(data["results"]), 0)


if __name__ == "__main__":
    unittest.main()
