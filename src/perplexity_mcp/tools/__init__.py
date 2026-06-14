# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Tool registry for perplexity-mcp.

Modules:
  search  -- perplexity_search_answer
  chat    -- perplexity_chat
  models  -- perplexity_list_models
  moderate -- perplexity_moderate
  embed   -- perplexity_embed
"""

from __future__ import annotations

from perplexity_mcp.tools.chat import chat_tools
from perplexity_mcp.tools.embed import embed_tools
from perplexity_mcp.tools.models import model_tools
from perplexity_mcp.tools.moderate import moderate_tools
from perplexity_mcp.tools.search import search_tools

perplexity_tools = [
    *search_tools,
    *chat_tools,
    *model_tools,
    *moderate_tools,
    *embed_tools,
]