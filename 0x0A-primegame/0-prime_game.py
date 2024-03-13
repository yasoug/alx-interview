#!/usr/bin/python3
"""Prime Game module"""


def isPrime(n):
    """Looks for prime numbers"""
    if n <= 1:
        return []

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        for i in range(p * p, n + 1, p):
            primes[i] = False
        p += 1
    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """Determines who the winner is"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primes = isPrime(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return 'Ben'
    elif Ben < Maria:
        return 'Maria'
    return None
