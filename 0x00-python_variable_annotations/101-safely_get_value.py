#!/usr/bin/env python3
"""
This module has parameters and return values, type annotations are added to
 the function
"""
from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """return value from a dict or return default value"""
    if key in dct:
        return dct[key]
    else:
        return default
