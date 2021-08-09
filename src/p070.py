#! /usr/bin/env python


from math import gcd

def a_perm_b_int(a, b):
    return sorted(str(a)) == sorted(str(b))


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



def p70():
    m_ratio = m_n = 0
    for i in range(1, 10 ** 7):
        print(i)
        p = phi(i)
        if a_perm_b_int(p, i):
            ratio = i/p
            if ratio > m_ratio:
                m_ratio = ratio
                m_n = i
    return m_n



if __name__ == "__main__":
    print(p70())
