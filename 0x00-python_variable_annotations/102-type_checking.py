#!/usr/bin/env python3
"""
annotation demos
"""
from typing import Tuple, List


def zoom_array(lst: Tuple,
               factor: int = 2) -> List:
    """ use of mypy """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List = [12, 72, 91]

zoom_2x: List = zoom_array(tuple(array))

zoom_3x: List = zoom_array(tuple(array), 3)
