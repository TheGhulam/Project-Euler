#! /usr/bin/env python

# Each convergent, i, of continued fraction of sqrt(D)
# n_i = a_i * n_i-1 + n_i-2
# d_i = a_i * d_i-1 + d_i-2


import math


def p64():
    L, odd_period = 13, 0

    for n in range(2, L + 1):
        r = limit = int(math.sqrt(n))
        if limit ** 2 == n:  # Skip perfect squares
            continue
        k, period = 1, 0
        while k != 1 or period == 0:  # Main loop for finding periods
            k = (n - r * r) // k
            r = (limit + r) // k * k - r
            period += 1
        if period % 2 == 1:
            odd_period += 1

    return odd_period


if __name__ == "__main__":
    print(p64())
