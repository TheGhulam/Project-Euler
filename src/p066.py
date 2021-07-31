#! /usr/bin/env python

import math
from itertools import count



def is_square(n):
    return math.isqrt(n) * math.isqrt(n) == n


def CF_of_sqrt(n):
    """ Compute the continued fraction representation of the
        square root of N.

        The first element in the returned array is the whole
        part of the fraction. The others are the denominators
        upto (and not including) the point where it starts
        repeating.

        Uses the algorithm explained here:
        http://www.mcs.surrey.ac.uk/Personal/R.Knott/Fibonacci/cfINTRO.html
        In the section named: "Methods of finding continued
        fractions for square roots"
    """
    if is_square(n):
        return [int(math.sqrt(n))]

    ans = []

    step1_num = 0
    step1_denom = 1

    while True:
        nextn = int((math.floor(math.sqrt(n)) + step1_num) / step1_denom)
        ans.append(int(nextn))

        step2_num = step1_denom
        step2_denom = step1_num - step1_denom * nextn

        step3_denom = (n - step2_denom ** 2) / step2_num
        step3_num = -step2_denom

        if step3_denom == 1:
            ans.append(ans[0] * 2)
            break

        step1_num, step1_denom = step3_num, step3_denom

    return ans

def contfrac_to_frac(seq):
    num, den = 1, 0
    for u in reversed(seq):
        num, den = den + num*u, num
    return num, den


def main():
    m_h, m_d = 0, 0
    for d in range(2, 1001):
        if is_square(d):
            continue
        else:
            cf = CF_of_sqrt(d)
            for i in range(1, len(cf)+1):
                h, k = contfrac_to_frac(cf[:i])
                Pell_type_approximation = (h ** 2) - (d * (k ** 2))
                if Pell_type_approximation == 1:
                    if h > m_h:
                        m_h = h
                        m_d = d
    return m_h, m_d



if __name__ == "__main__":
    print("The answer is 661 but I'm getting 991 :(")
    print(main())
