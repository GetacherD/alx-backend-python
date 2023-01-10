#!/usr/bin/env python3
"""
Python async demo
"""
import asyncio
from random import randrange


async def wait_random(max_delay: int = 10) -> float:
    """ Get random number wait and return it """
    ret = -1
    if max_delay <= 0:
        ret = 0
        max_delay = 1
    rn = randrange(0, max_delay)
    await asyncio.sleep(rn)
    if ret == 0:
        return ret
    return rn
