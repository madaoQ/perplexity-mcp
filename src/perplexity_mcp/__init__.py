# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Perplexity AI MCP server for Dedalus.

Provides search, chat, embeddings, and content moderation using Perplexity AI.
Credentials provided by clients at runtime via DAuth token exchange.
"""

from __future__ import annotations

from perplexity_mcp.config import create_perplexity_connection
from perplexity_mcp.tools import perplexity_tools

__all__ = ["create_perplexity_connection", "perplexity_tools"]