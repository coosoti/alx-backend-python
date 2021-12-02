#!/usr/bin/env python3
"""
This module contains a type-annotated function make_multiplier that takes a
 float multiplier as argument and returns a function that multiplies a float
 by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by a number"""

    def multiplier_function(number: float) -> float:
        """multiplies a number(float) by a multiplier"""
        return multiplier * number

    return multiplier_function
