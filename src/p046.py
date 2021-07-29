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


def main():
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


if __name__ == "__main__":
    main()
