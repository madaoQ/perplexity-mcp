# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for Perplexity API responses."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


class SearchResult(BaseModel, frozen=True, slots=True):
    """Search result with citations."""

    id: str | None = None
    text: str | None = None
    score: float | None = None
    cite_tokens: list[str] = Field(default_factory=list)
    image_url: str | None = None


class SearchResponse(BaseModel, frozen=True, slots=True):
    """Search API response."""

    results: list[SearchResult] = Field(default_factory=list)
    query: str | None = None
    total: int | None = None


class Message(BaseModel, frozen=True, slots=True):
    """Chat message."""

    role: str
    content: str
    name: str | None = None


class ChatResponse(BaseModel, frozen=True, slots=True):
    """Chat API response."""

    id: str | None = None
    model: str | None = None
    choices: list[dict[str, Any]] = Field(default_factory=list)
    usage: dict[str, Any] = Field(default_factory=dict)
    created: int | None = None


class ModelInfo(BaseModel, frozen=True, slots=True):
    """Perplexity model info."""

    id: str
    name: str
    description: str | None = None


class ModelList(BaseModel, frozen=True, slots=True):
    """List of available models."""

    models: list[ModelInfo]


class ModerationResponse(BaseModel, frozen=True, slots=True):
    """Content moderation result."""

    flagged: bool | None = None
    categories: dict[str, Any] = Field(default_factory=dict)


class EmbeddingResponse(BaseModel, frozen=True, slots=True):
    """Embedding API response."""

    model: str | None = None
    embeddings: list[list[float]] = Field(default_factory=list)
    usage: dict[str, Any] = Field(default_factory=dict)


# Type aliases for flexibility
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]
JSONArray = list[JSONValue]