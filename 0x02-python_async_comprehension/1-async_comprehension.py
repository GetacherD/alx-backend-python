#!/usr/bin/env python3
"""
async demo
"""
import asyncio
from random import random
from typing import AsyncGenerator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async generator """
    res = [i async for i in async_generator()]
    return res
