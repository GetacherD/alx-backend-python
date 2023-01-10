#!/usr/bin/env python3
"""
async demo
"""
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ async generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
