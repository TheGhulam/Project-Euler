#! /usr/bin/env python

# Very difficult. Need to review
import math

pentagonals = []
combinations = []

for i in range(1, 5000):
    pentagonals.append((i * (3 * i - 1)) / 2)

for j in pentagonals:
    for k in pentagonals:
        combinations.append(j + k)
        combinations.append(abs(j - k))

# n(3n-1)/2 = x
# x = (1+sqrt(24x+1))/6


def isPentagonal(n):
    s = math.sqrt(24 * n + 1)
    s = (s + 1) / 6
    return s == int(s)


found = False
i = 0
while not found:
    n1 = combinations[i]
    n2 = combinations[i + 1]
    if isPentagonal(n1) and isPentagonal(n2):
        print(n2)
        break
    i += 2
