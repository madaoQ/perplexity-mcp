# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Moderation tools for Perplexity AI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from perplexity_mcp.guards import validate_message_content
from perplexity_mcp.request import request
from perplexity_mcp.types import JSONObject


@tool(
    description="Check content for potentially harmful material using Perplexity.",
    tags=["moderate", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def perplexity_moderate(text: str) -> JSONObject:
    """Moderate text for harmful content.

    Args:
        text: Text to moderate.

    Returns:
        Moderation results with flagged status.

    Raises:
        ValueError: If text is empty.
        RuntimeError: If the API request fails.

    """
    validate_message_content(text)

    body: JSONObject = {"text": text}
    result = await request(HttpMethod.POST, "/moderate", body)
    return result


moderate_tools = [perplexity_moderate]