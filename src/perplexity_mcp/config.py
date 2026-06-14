# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Perplexity API configuration."""

from dedalus_mcp.auth import Connection, SecretKeys

# Perplexity API base URL
PERPLEXITY_API_BASE = "https://api.perplexity.ai"


def create_perplexity_connection() -> Connection:
    """Create a DAuth connection to Perplexity API.

    Uses Bearer token authentication.
    The API key is encrypted client-side and decrypted in the Dedalus enclave.

    Returns:
        Configured Connection for Perplexity API.

    """
    return Connection(
        name="perplexity",
        secrets=SecretKeys(token="PERPLEXITY_API_KEY"),
        base_url=PERPLEXITY_API_BASE,
        auth_header_format="Bearer {api_key}",
    )