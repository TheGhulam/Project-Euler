#! /usr/bin/env python


from funcs import sieve, isPrime
from itertools import permutations

def concats_are_prime(l):
    """
    Takes a list and returns if all possible nubmer concatantions are prime
    """
    perms = []
    for i in permutations(l, 2):
        perms.append(int(''.join(map(str, i))))
    return all([isPrime(i) for i in perms])

def p60():
    candidates = {3}
    for prime in sieve(1000_000):
        candidates.add(prime)
        if concats_are_prime(candidates):
            pass
        else:
            candidates.remove(prime)
    return candidates


print(p60())

