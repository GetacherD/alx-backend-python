#!/usr/bin/env python3
"""
annotation demos
"""
from typing import Union


def sum_mixed_list(mxd_list: list[Union[int, float]]) -> float:
    """ takes float list and return their sum as float """
    sm: float = 0.0
    for i in mxd_list:
        sm += i
    return sm
