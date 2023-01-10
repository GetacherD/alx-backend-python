#!/usr/bin/env python3
"""
Python async demo
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ Get random number wait and return it """
    rn = uniform(0, max_delay)
    await asyncio.sleep(rn)
    return rn
