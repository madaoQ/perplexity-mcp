"""
Perplexity API Client

Handles authentication and API calls to Perplexity AI.
Based on actual Perplexity API: https://docs.perplexity.ai
"""

from typing import Any

from dedalus_mcp import HttpMethod, HttpRequest, get_context, tool
from dedalus_mcp.auth import Connection, SecretKeys

# Perplexity API base URL
PERPLEXITY_API_BASE = "https://api.perplexity.ai"


def create_perplexity_connection() -> Connection:
    """
    Create a DAuth connection to Perplexity API.
    Uses Bearer token authentication.
    """
    return Connection(
        name="perplexity",
        secrets=SecretKeys(token="PERPLEXITY_API_KEY"),
        base_url=PERPLEXITY_API_BASE,
        auth_header_format="Bearer {api_key}",
    )


@tool(name="search_answer", description="Search the web and get answers with citations using Perplexity AI")
async def search_answer(
    query: str,
    model: str = "sonar",
    return_images: bool = False,
    return_related_questions: bool = False,
    search_recency_days: int | None = None,
    temperature: float = 0.2,
) -> dict[str, Any]:
    """
    Search for an answer using Perplexity AI with real-time web search.

    Args:
        query: The search query
        model: Model to use (sonar, sonar-pro, sonar-reasoning, etc.)
        return_images: Whether to include images in response
        return_related_questions: Whether to include related questions
        search_recency_days: Limit results to recent days
        temperature: Sampling temperature

    Returns:
        Search results with citations
    """
    ctx = get_context()

    body: dict[str, Any] = {
        "model": model,
        "query": query,
        "return_images": return_images,
        "return_related_questions": return_related_questions,
        "temperature": temperature,
    }

    if search_recency_days:
        body["search_recency_days"] = search_recency_days

    req = HttpRequest(
        method=HttpMethod.POST,
        path="/search",
        body=body,
    )

    resp = await ctx.dispatch("perplexity", req)

    if resp.success:
        return {"success": True, "data": resp.response.body}
    else:
        return {"success": False, "error": resp.error.message}


@tool(name="chat", description="Chat with Perplexity AI using natural language")
async def chat(
    model: str = "sonar",
    messages: list[dict[str, str]] | None = None,
    system_message: str | None = None,
    temperature: float = 0.2,
    top_p: float = 0.9,
    max_tokens: int = 1000,
) -> dict[str, Any]:
    """
    Chat with Perplexity AI (similar to OpenAI chat completions).

    Args:
        model: Model to use (sonar, sonar-pro, sonar-reasoning, etc.)
        messages: List of message objects with role and content
        system_message: Optional system message
        temperature: Sampling temperature
        top_p: Nucleus sampling parameter
        max_tokens: Maximum response tokens

    Returns:
        Chat response
    """
    ctx = get_context()

    # Build messages array
    if messages is None:
        messages = []

    if system_message:
        messages = [{"role": "system", "content": system_message}] + messages

    req = HttpRequest(
        method=HttpMethod.POST,
        path="/chat/completions",
        body={
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "top_p": top_p,
            "max_tokens": max_tokens,
        },
    )

    resp = await ctx.dispatch("perplexity", req)

    if resp.success:
        return {"success": True, "data": resp.response.body}
    else:
        return {"success": False, "error": resp.error.message}


@tool(name="list_models", description="List available Perplexity models")
async def list_models() -> dict[str, Any]:
    """
    List available Perplexity models.

    Returns:
        List of available models with their IDs
    """
    # Perplexity doesn't have a public list models endpoint
    # Return known models based on documentation
    return {
        "success": True,
        "data": {
            "models": [
                {"id": "sonar", "name": "Sonar", "description": "Fast, efficient for search"},
                {"id": "sonar-pro", "name": "Sonar Pro", "description": "Higher quality for complex queries"},
                {"id": "sonar-reasoning", "name": "Sonar Reasoning", "description": "Optimized for reasoning tasks"},
                {"id": "sonar-reasoning-pro", "name": "Sonar Reasoning Pro", "description": "Advanced reasoning"},
            ]
        }
    }


@tool(name="moderate", description="Check content for potentially harmful material using Perplexity")
async def moderate(
    text: str,
) -> dict[str, Any]:
    """
    Moderate text for harmful content.

    Args:
        text: Text to moderate

    Returns:
        Moderation results
    """
    ctx = get_context()

    req = HttpRequest(
        method=HttpMethod.POST,
        path="/moderate",
        body={"text": text},
    )

    resp = await ctx.dispatch("perplexity", req)

    if resp.success:
        return {"success": True, "data": resp.response.body}
    else:
        return {"success": False, "error": resp.error.message}


@tool(name="embed", description="Generate text embeddings using Perplexity")
async def embed(
    input: str | list[str],
    model: str = "embed",
) -> dict[str, Any]:
    """
    Generate embeddings for text.

    Args:
        input: Text or list of texts to embed
        model: Embedding model

    Returns:
        Embeddings response
    """
    ctx = get_context()

    req = HttpRequest(
        method=HttpMethod.POST,
        path="/embed",
        body={
            "input": input,
            "model": model,
        },
    )

    resp = await ctx.dispatch("perplexity", req)

    if resp.success:
        return {"success": True, "data": resp.response.body}
    else:
        return {"success": False, "error": resp.error.message}


# Export all tools
perplexity_tools = [
    search_answer,
    chat,
    list_models,
    moderate,
    embed,
]