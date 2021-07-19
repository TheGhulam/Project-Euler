#! /usr/bin/env python
# https://projecteuler.net/problem=57


def main():
    """
    # https://math.stackexchange.com/questions/730349/convergents-of-square-root-of-2
    # if p/q is first convergent then the next convergent can be written as (p+2q)/(p+q)
    """
    p, q, counter = 1, 1, 0
    for _ in range(1000):
        numerator = p + 2 * q
        denominator = p + q
        if len(str(numerator)) > len(str(denominator)):
            counter += 1
        p = numerator
        q = denominator
    return counter

if __name__ == "__main__":
    print(main())
