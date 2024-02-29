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
    min_arr = [float('inf')] * (total + 1)
    min_arr[0] = 0

    for i in range(1, len(min_arr)):
        for d in coins:
            if i >= d:
                min_arr[i] = min(min_arr[i], min_arr[i - d] + 1)
    return min_arr[total] if min_arr[total] != float('inf') else -1
