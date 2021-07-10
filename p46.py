#! /usr/bin/env python
# https://projecteuler.net/problem=46
## Notes
# c = p + 2 * n^2
# n = ((c-p)/2)^0.5
# For n to be positive integer there are 2 conditions:
# 1. c > p
# 2. n((c-p)/2) should be an integer


import math


def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    for i in range(3, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


c = 3
primes = [2]

while True:
    if isPrime(c):
        primes.append(c)
    else:
        for i in primes:
            if math.sqrt(((c - i) / 2)) == int(math.sqrt(((c - i) / 2))):
                break
        else:
            print(c)
            break
    c += 2
