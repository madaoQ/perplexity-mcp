# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Input validation for Perplexity API parameters."""

from __future__ import annotations

import re


# Perplexity model names: alphanumeric, hyphens
_MODEL_RE = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9_-]*$")


def validate_model(model: str) -> None:
    """Validate a Perplexity model name."""
    if not model or not _MODEL_RE.match(model):
        msg = f"Invalid model name: {model!r}"
        raise ValueError(msg)


def validate_temperature(temperature: float) -> None:
    """Validate temperature parameter."""
    if not 0.0 <= temperature <= 2.0:
        msg = f"Temperature must be between 0.0 and 2.0, got {temperature}"
        raise ValueError(msg)


def validate_top_p(top_p: float) -> None:
    """Validate top_p parameter."""
    if not 0.0 <= top_p <= 1.0:
        msg = f"top_p must be between 0.0 and 1.0, got {top_p}"
        raise ValueError(msg)


def validate_max_tokens(max_tokens: int) -> None:
    """Validate max_tokens parameter."""
    if max_tokens < 1 or max_tokens > 10000:
        msg = f"max_tokens must be between 1 and 10000, got {max_tokens}"
        raise ValueError(msg)


def validate_query(query: str) -> None:
    """Validate search query."""
    if not query or not query.strip():
        msg = "Query cannot be empty"
        raise ValueError(msg)
    if len(query) > 1000:
        msg = "Query cannot exceed 1000 characters"
        raise ValueError(msg)


def validate_message_content(content: str) -> None:
    """Validate message content."""
    if not content or not content.strip():
        msg = "Message content cannot be empty"
        raise ValueError(msg)