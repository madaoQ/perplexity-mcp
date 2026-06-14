# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Chat tools for Perplexity AI."""

from __future__ import annotations

from typing import Any

from dedalus_mcp import HttpMethod, tool
from dedalus_mcp.types import ToolAnnotations

from perplexity_mcp.guards import (
    validate_max_tokens,
    validate_message_content,
    validate_model,
    validate_top_p,
    validate_temperature,
)
from perplexity_mcp.request import request
from perplexity_mcp.types import JSONObject


@tool(
    description="Chat with Perplexity AI using natural language.",
    tags=["chat", "read"],
    annotations=ToolAnnotations(readOnlyHint=True),
)
async def perplexity_chat(
    model: str = "sonar",
    messages: list[dict[str, str]] | None = None,
    system_message: str | None = None,
    temperature: float = 0.2,
    top_p: float = 0.9,
    max_tokens: int = 1000,
) -> JSONObject:
    """Chat with Perplexity AI (similar to OpenAI chat completions).

    Args:
        model: Model to use (sonar, sonar-pro, sonar-reasoning, etc.).
        messages: List of message objects with role and content.
        system_message: Optional system message to prepend.
        temperature: Sampling temperature (0.0-2.0).
        top_p: Nucleus sampling parameter (0.0-1.0).
        max_tokens: Maximum response tokens (1-10000).

    Returns:
        Chat response with generated text.

    Raises:
        ValueError: If parameters are invalid.
        RuntimeError: If the API request fails.

    """
    validate_model(model)
    validate_temperature(temperature)
    validate_top_p(top_p)
    validate_max_tokens(max_tokens)

    if messages is None:
        messages = []
    else:
        for msg in messages:
            if "content" in msg:
                validate_message_content(msg["content"])

    if system_message:
        messages = [{"role": "system", "content": system_message}] + messages

    body: JSONObject = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
    }

    result = await request(HttpMethod.POST, "/chat/completions", body)
    return result


chat_tools = [perplexity_chat]