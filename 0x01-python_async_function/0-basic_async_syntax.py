#!/usr/bin/env python3
"""
Python async demo
"""
import asyncio
from random import randrange


async def wait_random(max_delay: int = 10) -> float:
    """ Get random number wait and return it """
    rn = randrange(0, max_delay)
    await asyncio.sleep(rn)
    return rn
