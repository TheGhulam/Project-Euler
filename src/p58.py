#! /usr/bin/env python

from funcs import isPrime

# Spiral 1
# 1 2 3 4 5 6 7 8 9 (9)
#     3   5   7   9 (Diff of 2)

# Spiral 2
# 10 11 12 13 14 15 ... 25 (16)
#          13   17 21   25 (Diff of 4)

# Spiral 3
# 26 ... 49 (24)
# 31 37 43 49 (Diff of 6; 2*spiral)


# 3x3 8 ((n-1)*4)
# 5x5 16
# 7x7 24


# Corner values of a square of size s have values:
# s^2 - 3s + 3, s^2 - 2s + 2, s^2 - s + 1, s^2


def corner_values(n):
    """
    returns a tuple of all 4 corners of an nxn square

    >>> corner_values(3)
    (3, 5, 7, 9)
    """
    return (n ** 2 - 3 * n + 3, n ** 2 - 2 * n + 2, n ** 2 - n + 1, n ** 2)


def main():
    ratio, side_length = 1, 1
    primes, total = 0, 0
    while ratio >= 0.1:
        side_length += 2
        for n in corner_values(side_length):
            if isPrime(n):
                primes += 1
                total += 1
            else:
                total += 1
        ratio = primes / total
    return side_length - 2


if __name__ == "__main__":
    print(main())
