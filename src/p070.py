#! /usr/bin/env python


from funcs import sieve
from math import sqrt

"""
We can reduce our search significantly by selecting prime pairs (p_1, p_2)
and calculate n as n = p_1 * p_2. This allows the totient to be calculated as
phi(n) = (p_1 - 1)(p_2 - 1) for n. Now just find the minimum ratio for those
n and phi(n) that are permutations.

The range of primes was selected by taking the square root of the upper bound,
10,000,000 which is about 3162 and taking ~30% for a range of primes from
2000 to 4000 (247 primes).
"""

L = 10 ** 7
primes = list(sieve(int(1.2 * sqrt(L))))
del primes[: int(0.6 * len(primes))]


def p70(limit):
    min_q, min_n, i = 2, 0, 0
    for p1 in primes:
        i += 1
        for p2 in primes[i:]:
            if (p1 + p2) % 9 != 1:
                continue
            n = p1 * p2
            if n > limit:
                return min_n
            phi = (p1 - 1) * (p2 - 1)
            q = n / float(phi)
            if sorted(str(phi)) == sorted(str(n)) and min_q > q:
                min_q, min_n = q, n
    return "Not found"


if __name__ == "__main__":
    print(p70(L))
