#!/usr/bin/python3
"""Making change module"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given amount

    Args:
        coins: list of coin denominations
        total: amount given
    """
    if total < 1:
        return 0
    min_needed = 0
    coins.sort(reverse=True)
    for denomination in coins:
        if total != 0:
            min_needed += total // denomination
            total %= denomination
    if total:
        return -1
    return min_needed
