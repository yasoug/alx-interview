#!/usr/bin/python3
"""Prime Game module"""


def isPrime(n):
    """Looks for prime numbers"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def countPrime(nums):
    """Counts the prime numbers in the list"""
    count = 0
    for num in nums:
        if isPrime(num):
            count += 1
    return count


def isWinner(x, nums):
    """Determines who the winner is"""
    Ben = 0
    Maria = 0
    if x <= 0 or not nums:
        return None
    for num in range(x):
        num_arr = [n for n in range(1, nums[num] + 1)]
        if countPrime(num_arr) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return "Ben"
    if Ben == Maria:
        return None
    return "Maria"
