#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file     main.py
@date     2024-03-02
@version  1.0.0
@license  GNU General Public License v3.0
@url      https://github.com/YisusChrist/python_multiprocessing_sample
@author   Alejandro Gonzalez Momblan (agelrenorenardo@gmail.com)
@desc     Sample code to test the performance of different ways to process a list of numbers
          using classic, list comprehension and multiprocessing methods
"""

import functools
import inspect
import multiprocessing
import os
from itertools import repeat
from typing import Callable

try:
    from rich import print  # pip install rich
except ImportError:
    pass

MULTIPROCESSING_THREADS = os.cpu_count()  # Use * 2 for hyper-threading in Intel CPUs
DIVIDE = True
MAX_NUMBER = 1000000
TEST_SIZE = 100


def decorator_timer(
    func: Callable[[list[int]], list[int | float]]
) -> Callable[[list[int]], list[int | float]]:
    """
    Decorator to measure the execution time of a function

    Args:
        func (Callable): Function to measure

    Returns:
        Callable: Wrapped function
    """
    from timeit import default_timer as timer

    @functools.wraps(wrapped=func)
    def wrapper(*args, **kwargs):
        t1: float = timer()
        result: list = func(*args, **kwargs)
        runtime: float = timer() - t1
        print(f"Finished {func.__name__!r} in {runtime:4f} secs")
        return result

    return wrapper


@decorator_timer
def option_1(numbers: list[int]) -> list[int | float]:
    """
    Classic way to process a list of numbers
    """
    results = []
    for number in numbers:
        tmp: int | float = process_number(number=number, divide=DIVIDE)
        results.append(tmp)

    return results


@decorator_timer
def option_2(numbers: list[int]) -> list[int | float]:
    """
    list comprehension way to process a list of numbers
    """
    results: list[int | float] = [
        process_number(number=number, divide=DIVIDE) for number in numbers
    ]
    return results


@decorator_timer
def option_3(numbers: list[int]) -> list[int | float]:
    """
    Multiprocessing way to process a list of numbers
    """
    with multiprocessing.Pool(processes=MULTIPROCESSING_THREADS) as pool:
        results: list[int | float] = pool.starmap(
            func=process_number, iterable=zip(numbers, repeat(DIVIDE))
        )

    return results


def process_number(number: int, divide: bool) -> int | float:
    """
    Very complex function to process a number with a hyuuuge loop
    """
    tmp: float = 0
    for i in range(MAX_NUMBER):
        if divide:
            tmp += number / (i + 1)
        else:
            tmp += number * (i + 1)

    return tmp


def main() -> int:
    """
    Main function
    """

    print("Testing multiprocessing with the following parameters:")
    print(f"- Test size: {TEST_SIZE}")
    print(f"- Max number: {MAX_NUMBER}")
    print(f"- CPU count: {os.cpu_count()}")
    print(f"- Multiprocessing threads: {MULTIPROCESSING_THREADS}")
    print(f"- Divide: {DIVIDE}\n")

    # Create a random list of numbers of 1000 elements
    numbers: list[int] = [i for i in range(TEST_SIZE)]
    options: list[Callable] = [
        value
        for name, value in globals().items()
        if inspect.isfunction(value) and name.startswith("option_")
    ]

    for option_func in options:
        print(f"Results: {option_func(numbers=numbers)[:10]}...\n")

    return 0


if __name__ == "__main__":
    main()
