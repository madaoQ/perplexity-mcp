# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Search tools for Perplexity AI."""

from __future__ import annotations

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from perplexity_mcp.guards import validate_model, validate_query, validate_temperature
from perplexity_mcp.request import _bool, _int, _opt_str, request
from perplexity_mcp.types import JSONObject


@tool(
    description="Search the web and get answers with citations using Perplexity AI.",
    tags=["search", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def perplexity_search_answer(
    query: str,
    model: str = "sonar",
    return_images: bool = False,
    return_related_questions: bool = False,
    search_recency_days: int | None = None,
    temperature: float = 0.2,
) -> JSONObject:
    """Search for an answer using Perplexity AI with real-time web search.

    Args:
        query: The search query.
        model: Model to use (sonar, sonar-pro, sonar-reasoning, etc.).
        return_images: Whether to include images in response.
        return_related_questions: Whether to include related questions.
        search_recency_days: Limit results to recent days.
        temperature: Sampling temperature (0.0-2.0).

    Returns:
        Search results with citations.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_query(query)
    validate_model(model)
    validate_temperature(temperature)

    body: JSONObject = {
        "model": model,
        "query": query,
        "return_images": return_images,
        "return_related_questions": return_related_questions,
        "temperature": temperature,
    }

    if search_recency_days is not None:
        _int(search_recency_days)  # validate
        body["search_recency_days"] = search_recency_days

    result = await request(HttpMethod.POST, "/search", body)
    return result


search_tools = [perplexity_search_answer]