#!/usr/bin/env python3
"""
This module contains a code with correct duck-typed annotations
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of a sequence or None if the sequence is empty"""
    if lst:
        return lst[0]
    else:
        return None
