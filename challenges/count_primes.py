"""
Input: n = 10
Output: 4

"""

"""
    if n == 0 or n == 1:
        return "not prime"
    if n == 2:
        return "prime"
    # devide by 2 tp check for even numbers
    if n % 2 == 0:
        return "not prime"
    for odd in range(3, math.ceil(math.sqrt(n)) + 1, 2):
        if n % odd == 0:
            return "not prime"
    return "prime"
"""
import math


def is_prime(x):
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for odd in range(3, math.ceil(math.sqrt(x)) + 1, 2):
        if x % odd == 0:
            return False
    return True


def count_prime(n):
    if n < 0 or n > (5 * 10**6):
        return -1
    count = 0
    for x in range(n+1):
        if is_prime(x):
            count += 1
    return count


print(count_prime(10))