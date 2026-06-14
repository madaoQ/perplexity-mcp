# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Direct API testing client for Perplexity MCP.

This module is used for local testing without going through the MCP server.
It bypasses DAuth and calls the Perplexity API directly using the API key.
"""

from __future__ import annotations

import asyncio
import os

import httpx
from dotenv import load_dotenv

load_dotenv()


async def test_search() -> None:
    """Test search_answer endpoint."""
    print("Testing perplexity_search_answer...")

    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        print("Error: PERPLEXITY_API_KEY not found in environment")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    body = {
        "model": "sonar",
        "query": "What is Model Context Protocol?",
        "return_images": False,
        "return_related_questions": False,
        "temperature": 0.2,
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.perplexity.ai/search",
            headers=headers,
            json=body,
            timeout=30,
        )

    if resp.status_code == 200:
        data = resp.json()
        print(f"✓ Search successful")
        print(f"  Model: {data.get('model', 'unknown')}")
    else:
        print(f"✗ Error {resp.status_code}: {resp.text[:200]}")


async def test_chat() -> None:
    """Test chat endpoint."""
    print("\nTesting perplexity_chat...")

    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        print("Error: PERPLEXITY_API_KEY not found")
        return

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    body = {
        "model": "sonar",
        "messages": [{"role": "user", "content": "Hello, how are you?"}],
        "temperature": 0.2,
        "max_tokens": 50,
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json=body,
            timeout=30,
        )

    if resp.status_code == 200:
        data = resp.json()
        print(f"✓ Chat successful")
        print(f"  Model: {data.get('model', 'unknown')}")
        choices = data.get("choices", [])
        if choices:
            msg = choices[0].get("message", {})
            print(f"  Response: {msg.get('content', 'N/A')[:100]}")
    else:
        print(f"✗ Error {resp.status_code}: {resp.text[:200]}")


async def main() -> None:
    """Run all direct API tests."""
    print("=" * 50)
    print("Perplexity Direct API Tests")
    print("=" * 50)
    print()

    await test_search()
    await test_chat()

    print()
    print("=" * 50)
    print("Tests completed!")


if __name__ == "__main__":
    asyncio.run(main())