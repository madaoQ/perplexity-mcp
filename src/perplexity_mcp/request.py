# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Perplexity API request utilities."""

from __future__ import annotations

from typing import Any

from dedalus_mcp import HttpMethod, HttpRequest, get_context

from perplexity_mcp.types import JSONObject


def _build_url(path: str, **params: Any) -> str:
    """Build URL with query parameters, filtering None values."""
    parts = [path]
    query_parts = []
    for key, value in sorted(params.items()):
        if value is None:
            continue
        if isinstance(value, bool):
            value = "true" if value else "false"
        query_parts.append(f"{key}={value}")
    if query_parts:
        parts.append("?" + "&".join(query_parts))
    return "".join(parts)


def _str(value: Any, default: str = "") -> str:
    """Coerce to string with default."""
    if value is None:
        return default
    return str(value)


def _int(value: Any, default: int = 0) -> int:
    """Coerce to int with default."""
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def _opt_str(value: Any) -> str | None:
    """Coerce to string or None."""
    if value is None:
        return None
    return str(value)


def _bool(value: Any) -> bool:
    """Coerce to bool."""
    return bool(value)


def _nested_str(data: dict[str, Any], key: str) -> str:
    """Safely extract nested string."""
    if not isinstance(data, dict):
        return ""
    val = data.get(key)
    if val is None:
        return ""
    return str(val)


async def request(
    method: HttpMethod,
    path: str,
    payload: JSONObject | None = None,
    params: dict[str, Any] | None = None,
) -> JSONObject:
    """Dispatch HTTP request through Dedalus enclave.

    Args:
        method: HTTP method.
        path: API path.
        payload: JSON body for POST/PUT requests.
        params: Query parameters.

    Returns:
        JSON response data.

    Raises:
        RuntimeError: If the request fails.

    """
    ctx = get_context()

    url = _build_url(path, **(params or {}))
    body = payload

    req = HttpRequest(method=method, path=url, body=body)
    resp = await ctx.dispatch("perplexity", req)

    if resp.success:
        return resp.response.body if isinstance(resp.response.body, dict) else {}
    else:
        msg = resp.error.message if resp.error else "Request failed"
        raise RuntimeError(msg)