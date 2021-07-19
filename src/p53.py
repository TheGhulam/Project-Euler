#! /usr/bin/env python
# https://projecteuler.net/problem=53

from math import factorial


def achooseb(n, r):
    return (factorial(n)) / (factorial(r) * factorial(n - r))


def main():
    count = 0
    for n in range(1, 101):
        for r in range(1, n):
            value = achooseb(n, r)
            if value > 1000_000:
                count += 1
    print(count)


if __name__ == "__main__":
    main()
