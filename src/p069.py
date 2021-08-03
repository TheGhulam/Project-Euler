#! /usr/bin/env python


from math import gcd


def phi(n):
    """Euler's totient function AKA phi

    >>> phi(5)
    4
    """
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


def p69(limit):
    # Solution is too slow for given range
    m_value, m_n = 0, 0
    for n in range(2, limit + 1):
        print(n)
        score = n / phi(n)
        if score > m_value:
            m_value = score
            m_n = n
    return m_n


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]


def p69_updated(limit):
    """
    Hack method which solves the problem without using phi function.
    It works by multiplying distinct, consecutive primes starting from 2 until
    we reach, but do not exceed, the limit. This reduces to simply finding the
    closest primorial to our limit and never having to calculate any totients.

    This answers the problem, but finds only the first n to exceed our limit.
    There may, in fact, be many n that have the same ratio.
    """
    m_n = 1
    for p in primes:
        if m_n * p > limit:
            return m_n
        m_n *= p
    return "Buy me some more prime numbers!"


if __name__ == "__main__":
    # print(p69(1_000_000))
    print(p69_updated(1_000_000))
