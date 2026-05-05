"""Configuration for integration tests that require API keys."""

import os

import pytest

# Importing agency_swarm triggers .env loading via python-dotenv
import agency_swarm  # noqa: F401

# Verify API key is loaded; skip integration tests gracefully if missing.
# CI on fork repos (without configured secrets) will see these as skipped,
# not failed. Upstream repos with secrets configured run the full suite.
if not os.getenv("OPENAI_API_KEY"):
    pytest.skip("OPENAI_API_KEY not found in environment — skipping integration tests")
