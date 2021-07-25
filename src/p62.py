#! /usr/bin/env python

from collections import Counter


def p62(perms_required):
    min_cube = 1
    third = 1 / 2

    while True:
        max_cube = min_cube * 10 - 1
        low = int(min_cube ** third)
        high = int(max_cube ** third)

        # At any point of time, if there are more than one cubic permutations of i, then
        # sorted(list(str(i ** 3))) will always return the same list
        cubes = ["".join(sorted(str(x ** 3))) for x in range(low, high + 1)]
        count = Counter(cubes)
        digits = next(
            (digits for digits, n in count.items() if n == perms_required), None
        )

        if digits:
            root = cubes.index(digits) + low
            return root ** 3
        min_cube *= 10


if __name__ == "__main__":
    print(p62(5))
