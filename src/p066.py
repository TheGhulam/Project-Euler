#! /usr/bin/env python

from itertools import count
from math import isqrt


def minx_diophantine(d):
    for x in count(2):
        # for y in count(2):
        for y in range(1, x):
            if (((x ** 2) - 1) / y ** 2) == d:
                return x, y


def main():
    m_x = m_d = 0
    for d in range(1001):
        print(d)
        if isqrt(d) * isqrt(d) == d:
            continue
        else:
            x, _ = minx_diophantine(d)
            if x > m_x:
                m_x = x
                m_d = d
    return m_x, m_d


if __name__ == "__main__":
    print(main())
