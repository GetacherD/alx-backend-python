#!/usr/bin/env python3
"""
annotation demos
"""


def safely_get_value(dct, key, default=None):
    """ annotation demo """
    if key in dct:
        return dct[key]
    return default
