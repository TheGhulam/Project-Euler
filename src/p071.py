#! /usr/bin/env python

from fractions import Fraction

def p71(d):
    reduced_proper_fractions = set()
    for b in range(d+1, 1, -1):
        for a in range(b-1, 1, -1):
            print(a, b)
            reduced_proper_fractions.add(Fraction(a, b))
    return reduced_proper_fractions





if __name__ == "__main__":
    print(p71(8))
