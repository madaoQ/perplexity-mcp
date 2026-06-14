# Perplexity MCP Server

A Type 3 DAuth MCP server for [Perplexity AI](https://perplexity.ai) API. Provides web search, chat, embeddings, and content moderation using Perplexity's search-focused AI models.

## Features

- **Search Answer** — Real-time web search with citations
- **Chat** — Conversational AI similar to chat completions
- **List Models** — View available Perplexity models
- **Moderate** — Content moderation
- **Embed** — Text embeddings

## Authentication

This server uses **Type 3 DAuth** (Dedalus Auth) — your API key is encrypted client-side and decrypted in a secure Dedalus enclave.

### Get Your Perplexity API Key

1. Go to https://www.perplexity.ai/settings/api
2. Generate a new API key (requires paid subscription)
3. Copy the key

## Installation

```bash
git clone https://github.com/dedalus-labs/perplexity-mcp.git
cd perplexity-mcp
pip install -e .
cp .env.example .env
# Edit .env and add PERPLEXITY_API_KEY
```

## Available Tools

### `perplexity_search_answer`

Search the web and get answers with citations.

```python
perplexity_search_answer(
    query="What is Model Context Protocol?",
    model="sonar",
    return_images=True,
    search_recency_days=7,
    temperature=0.2,
)
```

### `perplexity_chat`

Chat with Perplexity AI.

```python
perplexity_chat(
    model="sonar",
    messages=[{"role": "user", "content": "Hello!"}],
    temperature=0.2,
    max_tokens=500,
)
```

### `perplexity_list_models`

List available Perplexity models.

```python
perplexity_list_models()
```

### `perplexity_moderate`

Check content for harmful material.

```python
perplexity_moderate(text="This is a test message")
```

### `perplexity_embed`

Generate text embeddings.

```python
perplexity_embed(
    input="Hello world",
    model="embed",
)
```

## Cost & Rate Limits

Perplexity uses pay-per-token pricing. Check https://perplexity.ai/pricing for details.

| Model | Input | Output |
|-------|-------|--------|
| Sonar | $0.005/1M | $0.005/1M |
| Sonar Pro | $0.01/1M | $0.03/1M |
| Sonar Reasoning | $0.005/1M | $0.005/1M |

### Rate Limits

- **Free tier:** Limited requests per day
- **Pro tier:** 500 requests/day
- **Enterprise:** Custom limits

## Safety Notes

- **Requires paid API** — Perplexity API requires a paid subscription
- **Monitor costs** — Set up usage alerts at perplexity.ai/dashboard
- **Don't commit keys** — Always use environment variables

## Deploy to Dedalus

1. Push to GitHub (public repo)
2. Go to https://www.dedaluslabs.ai/dashboard
3. Add Server → Connect GitHub repo
4. Set `PERPLEXITY_API_KEY` as Required Credential
5. Deploy

## License

MIT