# Copyright (c) 2026 Dedalus Labs, Inc. and its contributors
# SPDX-License-Identifier: MIT

"""Server entrypoint."""

from __future__ import annotations

import asyncio

from dotenv import load_dotenv

load_dotenv()

from main import main

if __name__ == "__main__":
    asyncio.run(main())