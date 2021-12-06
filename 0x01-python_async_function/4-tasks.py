#!/usr/bin/env python3
"""
this module contains a new function task_wait_n spawns tasks n times with a
given delay between each function call
"""

import asyncio
from asyncio.tasks import Task
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
