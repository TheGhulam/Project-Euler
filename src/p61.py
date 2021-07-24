#! /usr/bin/env python

from itertools import combinations

def triangle_generator(limit):
    for n in range(2, limit):
        o =  n * (n + 1) // 2
        if len(str(o)) == 4:
            yield o


def square_generator(limit):
    for n in range(2, limit):
        o = n ** 2
        if len(str(o)) == 4:
            yield o


def pentagonal_generator(limit):
    for n in range(2, limit):
        o = n * (3 * n - 1) // 2
        if len(str(o)) == 4:
            yield o


def hexagonal_generator(limit):
    for n in range(2, limit):
        o = n * (2 * n - 1)
        if len(str(o)) == 4:
            yield o


def heptagonal_generator(limit):
    for n in range(2, limit):
        o = n * (5 * n - 3) // 2
        if len(str(o)) == 4:
            yield o


def octagonal_generator(limit):
    for n in range(2, limit):
        o =  n * (3 * n - 2)
        if len(str(o)) == 4:
            yield o


def p61(limit):
    triangles = list(triangle_generator(limit))

    # for t in triangle_generator(limit):
        # for s in square_generator(limit):
            # for p in pentagonal_generator(limit):
                # for h in hexagonal_generator(limit):
                    # for hep in heptagonal_generator(limit):
                        # for o in octagonal_generator(limit):

def comb(la, lb):
    """ Takes two lists and returns cyclic numbers
    """

def cyclic(a, b):
    return str(a)[-2:] == str(b)[:2]

def p61_test_2(limit):
    for t in triangle_generator(limit):
        for s in square_generator(limit):
            for p in pentagonal_generator(limit):
                if cyclic(t, s):
                    if cyclic(s, p):
                        if cyclic (p, t):
                            return(t, s, p)
                elif cyclic(t, p):
                    if cyclic(p, s):
                        if cyclic(s, t):
                            return(t, p, s)



if __name__ == "__main__":
    # print(p61(200))
    # print(p61_test_2(200))
    print(p61(200))

