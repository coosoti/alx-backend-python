#!/usr/bin/env python3
"""
This module contains a type-annotated function sum_mixed_list which takes a
 list mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """takes a mixed list of ints and floats and returns sum in float type"""
    return sum(mxd_list)
