# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Typed models for Perplexity API responses."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


# Reusable config: immutable, slotted.
_FROZEN_SLOT = ConfigDict(frozen=True, slots=True)


class SearchResult(BaseModel):
    """Search result with citations."""
    model_config = _FROZEN_SLOT


    id: str | None = None
    text: str | None = None
    score: float | None = None
    cite_tokens: list[str] = Field(default_factory=list)
    image_url: str | None = None


class SearchResponse(BaseModel):
    """Search API response."""
    model_config = _FROZEN_SLOT


    results: list[SearchResult] = Field(default_factory=list)
    query: str | None = None
    total: int | None = None


class Message(BaseModel):
    """Chat message."""
    model_config = _FROZEN_SLOT


    role: str
    content: str
    name: str | None = None


class ChatResponse(BaseModel):
    """Chat API response."""
    model_config = _FROZEN_SLOT


    id: str | None = None
    model: str | None = None
    choices: list[dict[str, Any]] = Field(default_factory=list)
    usage: dict[str, Any] = Field(default_factory=dict)
    created: int | None = None


class ModelInfo(BaseModel):
    """Perplexity model info."""
    model_config = _FROZEN_SLOT


    id: str
    name: str
    description: str | None = None


class ModelList(BaseModel):
    """List of available models."""
    model_config = _FROZEN_SLOT


    models: list[ModelInfo]


class ModerationResponse(BaseModel):
    """Content moderation result."""
    model_config = _FROZEN_SLOT


    flagged: bool | None = None
    categories: dict[str, Any] = Field(default_factory=dict)


class EmbeddingResponse(BaseModel):
    """Embedding API response."""
    model_config = _FROZEN_SLOT


    model: str | None = None
    embeddings: list[list[float]] = Field(default_factory=list)
    usage: dict[str, Any] = Field(default_factory=dict)


# Type aliases for flexibility
JSONPrimitive = Literal[str, int, float, bool, None]
JSONValue = JSONPrimitive | list["JSONValue"] | dict[str, "JSONValue"]
JSONObject = dict[str, JSONValue]
JSONArray = list[JSONValue]