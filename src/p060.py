#! /usr/bin/env python


# from itertools import permutations
import math

from funcs import sieve, isPrime


# def concats_are_prime(l):
#     """
#     Takes a list and returns if all possible nubmer concatantions are prime
#     """
#     perms = []
#     for i in permutations(l, 2):
#         perms.append(int("".join(map(str, i))))
#     return all([isPrime(i) for i in perms])


def comb(a, b):
    """Find all combinations of given two numbers and check if they are prime"""
    len_a = math.floor(math.log10(a)) + 1
    len_b = math.floor(math.log10(b)) + 1
    if isPrime(int(a * (10 ** len_b) + b)) and isPrime(int(b * (10 ** len_a) + a)):
        return True
    return False


primes = list(sieve(10000))


def p60():
    for a in primes:
        for b in primes:
            if b < a:
                continue
            if comb(a, b):
                for c in primes:
                    if c < b:
                        continue
                    if comb(a, c) and comb(b, c):
                        for d in primes:
                            if d < c:
                                continue
                            if comb(a, d) and comb(b, d) and comb(c, d):
                                for e in primes:
                                    if e < d:
                                        continue
                                    if (
                                        comb(a, e)
                                        and comb(b, e)
                                        and comb(c, e)
                                        and comb(d, e)
                                    ):
                                        return a + b + c + d + e

if __name__ == "__main__":
    print(p60())

