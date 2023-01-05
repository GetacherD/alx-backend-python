#!/usr/bin/env python3
"""
annotation demos
"""
from typing import Union
from typing import Sequence


def safe_first_element(lst: Sequence[any]) -> Union[any, None]:
    """ annotation demo """
    if lst:
        return lst[0]
    return None
