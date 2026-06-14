"""
Perplexity MCP Client - Direct API Testing
"""

import os
import httpx
from dotenv import load_dotenv

load_dotenv()


async def test_api():
    print("Testing Perplexity API directly...\n")

    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        print("Error: PERPLEXITY_API_KEY not found")
        return

    print(f"✓ API key found: {api_key[:12]}...\n")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Test 1: chat completions
    print("1. Testing chat (chat/completions endpoint)...")
    try:
        resp = httpx.post(
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json={
                "model": "sonar",
                "messages": [{"role": "user", "content": "Hi"}],
                "max_tokens": 50,
            },
            timeout=30,
        )
        if resp.status_code == 200:
            print(f"   ✓ Success")
        else:
            print(f"   ✗ Error {resp.status_code}: {resp.text[:100]}")
    except Exception as e:
        print(f"   ✗ Exception: {e}")

    print("\n" + "=" * 50)
    print("API tests completed!")


if __name__ == "__main__":
    import asyncio
    asyncio.run(test_api())