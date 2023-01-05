#!/usr/bin/env python3
"""
annotation demos
"""
from typing import Union
from typing import Sequence
from typing import Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ annotation demo """
    if lst:
        return lst[0]
    return None
