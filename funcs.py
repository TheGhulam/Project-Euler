#! /usr/bin/env python
from math import log, ceil


def isPrime(n):
    if n in {2, 3, 5, 7}:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n % 3 == 0 or n % 5 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


def sieve(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False


def nthPrime(n):
    if n < 6:
        up = 100
    else:
        up = ceil(n * (log(n) + log(log(n))))
    return list(sieve(up))[n - 1]
