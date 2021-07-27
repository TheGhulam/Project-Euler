#! /usr/bin/env python


import math
import re

# sqrt(5) ~= 2.23; int(2.23) = 2; 2 + <fraction>

def is_perfect_square(n):
    closest_root = math.sqrt(n)
    return n == closest_root * closest_root


def recurring_pattern(n):
    p = re.compile(r'(.+?)\1+')
    match = re.findall(p, str(n))
    if len(match) > 0:
        period = str(n).count(match[0])
        return match, period
    return match


def p64(n, dp):

    if is_perfect_square(n):
        return 0
    else:
        a0_float = math.sqrt(n)
        a0 = int(a0_float)
        a_rest = []
        for _ in range(dp):
            a_next_float = (a0_float - a0) ** -1
            a_next = int(a_next_float)
            a_rest.append(a_next)
            a0_float = a_next_float
            a0 = a_next
        return n, a0, a_rest

def main():
    for i in range(2, 14):
        if p64(i, 10) == 0:
            continue
        else:
            n, a0, a_rest = p64(i, 10)
            pattern = int(''.join(map(str, a_rest)))
            print(n, a0, a_rest)
            print(pattern)
            print('rp', recurring_pattern(pattern))



if __name__ == "__main__":
    main()
