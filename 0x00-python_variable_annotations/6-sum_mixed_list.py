#!/usr/bin/env python3
"""
annotation demos
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """ takes float list and return their sum as float """
    return sum(mxd_list)
