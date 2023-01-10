#!/usr/bin/env python3
"""
Python async demo
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ spawn function """
    res = await asyncio.gather(*[wait_random(max_delay) for i in range(n)])
    return res
