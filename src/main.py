"""
Perplexity MCP Server - Main Entry Point

A Type 3 DAuth MCP server for Perplexity AI API.
"""

import os
from dotenv import load_dotenv

from dedalus_mcp import MCPServer
from dedalus_mcp.server import TransportSecuritySettings

from .perplexity import create_perplexity_connection, perplexity_tools

load_dotenv()


def create_server() -> MCPServer:
    """Create and configure the Perplexity MCP server."""
    perplexity_conn = create_perplexity_connection()

    server = MCPServer(
        name="perplexity-mcp",
        connections=[perplexity_conn],
        http_security=TransportSecuritySettings(
            enable_dns_rebinding_protection=False
        ),
        streamable_http_stateless=True,
        authorization_server=os.getenv("DEDALUS_AS_URL", "https://as.dedaluslabs.ai"),
    )

    server.collect(*perplexity_tools)

    return server


async def main() -> None:
    """Start the server."""
    server = create_server()
    await server.serve(port=8080)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())