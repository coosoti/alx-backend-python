#!/usr/bin/env python3
"""
This module contain a coroutine named wait_random that takes an int argument
 max_delay that waits for random delay between 0 and max_delay seconds and
 eventual returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    takes an int argument and wait for random delay and returns delay time
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
