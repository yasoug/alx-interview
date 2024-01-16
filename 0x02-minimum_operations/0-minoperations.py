#!/usr/bin/python3
"""Script for the function minOperations"""


def minOperations(n):
    """
    Returns the fewest number of operations needed
    to result in exactly `n` `H` characters in a file
    """
    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(n // i) + i
