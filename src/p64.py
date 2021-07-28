#! /usr/bin/env python


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
