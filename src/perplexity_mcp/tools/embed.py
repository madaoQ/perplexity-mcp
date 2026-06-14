# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Embedding tools for Perplexity AI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from perplexity_mcp.guards import validate_message_content
from perplexity_mcp.request import request
from perplexity_mcp.types import JSONObject


@tool(
    description="Generate text embeddings using Perplexity.",
    tags=["embed", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def perplexity_embed(
    input: str | list[str],
    model: str = "embed",
) -> JSONObject:
    """Generate embeddings for text.

    Args:
        input: Text or list of texts to embed.
        model: Embedding model to use.

    Returns:
        Embeddings response with vectors.

    Raises:
        ValueError: If input is empty.
        RuntimeError: If the API request fails.

    """
    if isinstance(input, str):
        validate_message_content(input)
    elif isinstance(input, list):
        if not input:
            raise ValueError("Input list cannot be empty")
        for item in input:
            validate_message_content(item)
    else:
        raise ValueError("Input must be a string or list of strings")

    body: JSONObject = {
        "input": input,
        "model": model,
    }

    result = await request(HttpMethod.POST, "/embed", body)
    return result


embed_tools = [perplexity_embed]