#! /usr/bin/env python

import itertools


def is_cube(n):
    return round(n ** (1 / 3)) ** 3 == n



def main():
    found = False
    n = 100
    while not found:
        n += 1
        cube = n ** 3
        perms = [
            int("".join(map(str, a)))
            for a in itertools.permutations(str(cube))
        ]
        perms = [perm for perm in perms if len(str(perm)) == len(str(cube))]
        filtered_perms = set(filter(is_cube, perms))
        if len(filtered_perms) == 5:
            found = True
            print(filtered_perms)


if __name__ == "__main__":
    main()
