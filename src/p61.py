#! /usr/bin/env python

# Straight-forward brute-force solution in three easy steps:
# 1. Generate each polygonal number with it’s type as a tuple.
# 2. Build a dictionary (hash) of each tuple to every other tuple not of the same type that follows the criteria of the problem (ending two digits matching the beginning two digits). Here’s a sample of the relation:

# {(3, 1035): [(7, 3553), (5, 3577)]
# (3, 1081): [(6, 8128), (5, 8177)]
# (3, 1128): [(8, 2821), (7, 2839), (6, 2850), (5, 2882)]
# (3, 1176): [(6, 7626)]
# (3, 1225): [(7, 2512), (6, 2556)]

# Here’s the full set (study61.txt) of all 293 relations.
# 3. Run through the dictionary and find every six member family that follows the criteria.
# 3a. Make sure the last two digits of the last number match the first two digits of the first number.



def fn(n):
    return (
        (3, n * (n + 1) / 2),
        (4, n * n),
        (5, n * (3 * n - 1) / 2),
        (6, n * (2 * n - 1)),
        (7, n * (5 * n - 3) / 2),
        (8, n * (3 * n - 2)),
    )


def next(types, data):
    if len(types) == 6 and data[0] // 100 == data[-1] % 100:
        print(data, sum(data))
    else:
        for t, n in ds.get((types[-1], data[-1]), []):
            if t not in types:
                next(types + [t], data + [n])


p = []  # build a list of polygonal numbers with their type (type, pnum)
n = 19  # first n for octogonal number > 999

while n < 141:  # last n for triangle numbers < 10000
    for type, data in fn(n):
        if 1000 <= data <= 9999 and data % 100 > 9:
            p.append((type, data))
    n += 1

ds = {}  # build a dictionary of tuples
for t1, d1 in p:
    for t2, d2 in p:
        if t1 != t2 and d1 % 100 == d2 // 100:
            ds[t1, d1] = ds.get((t1, d1), []) + [(t2, d2)]

print("Project Euler 61 Solution Set")
for type, data in ds:
    next([type], [data])

