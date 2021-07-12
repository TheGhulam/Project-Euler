#! /usr/bin/env python
from funcs import sieve, isPrime
from itertools import permutations


def main():
    for a in sieve(10000):
        b = a + 3330
        c = b + 3330
        perms = set(permutations(str(a)))
        if (
            isPrime(a)
            and isPrime(b)
            and isPrime(c)
            and (tuple(str(b)) in perms)
            and (tuple(str(c)) in perms)
        ):
            print(a, b, c)

if __name__ == "__main__":
    main()
