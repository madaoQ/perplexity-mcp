# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Model listing tools for Perplexity AI."""

from __future__ import annotations

from dedalus_mcp import tool
from dedalus_mcp.types import ToolAnnotations

from perplexity_mcp.types import ModelInfo, ModelList


@tool(
    description="List available Perplexity models.",
    tags=["models", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def perplexity_list_models() -> ModelList:
    """List available Perplexity models.

    Returns:
        List of available models with their IDs and descriptions.

    """
    # Perplexity doesn't have a public list models endpoint
    # Return known models based on documentation
    return ModelList(
        models=[
            ModelInfo(
                id="sonar",
                name="Sonar",
                description="Fast, efficient model for search and chat",
            ),
            ModelInfo(
                id="sonar-pro",
                name="Sonar Pro",
                description="Higher quality for complex queries",
            ),
            ModelInfo(
                id="sonar-reasoning",
                name="Sonar Reasoning",
                description="Optimized for reasoning tasks",
            ),
            ModelInfo(
                id="sonar-reasoning-pro",
                name="Sonar Reasoning Pro",
                description="Advanced reasoning with larger context",
            ),
        ]
    )


model_tools = [perplexity_list_models]