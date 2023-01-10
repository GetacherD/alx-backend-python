#!/usr/bin/env python3
"""
asyncio demo
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ spawn function """
    tasks = map(lambda k: wait_random(max_delay), range(n))
    res = await asyncio.gather(*list(tasks))
    return sorted(res)
