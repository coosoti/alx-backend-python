#!/usr/bin/env python3
"""
This module contains a regular function, task_wait_random, that takes an
integer max_delay and returns a asyncio.Task
"""

import asyncio
import time


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """
    takes max_delay as an argument and return asyncio Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
