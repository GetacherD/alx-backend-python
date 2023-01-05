#!/usr/bin/env python3
"""
annotation demos
"""
from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ annotated demo """
    return (k, float(v ** 2))
