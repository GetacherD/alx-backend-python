#!/usr/bin/env python3
"""
annotation demos
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a function that takes float and retur float """
    return lambda x: x * multiplier
