#!/usr/bin/env python3
"""
annotation demos
"""
from typing import Iterable
from typing import Sequence
from typing import Tuple
from typing import List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ annotation demo """
    return [(i, len(i)) for i in lst]
