#!/usr/bin/env python3
"""
Python async demo
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ spawn function """
    t1 = time.time()
    asyncio.run(wait_n(n, max_delay))
    t2 = time.time()
    return (t2 - t1) / n
