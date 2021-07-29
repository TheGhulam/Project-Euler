#! /usr/bin/env python
# https://projecteuler.net/problem=45

def triangle(n):
    return (n*(n+1))//2

def pentagonal(n):
    return n*(3*n-1)//2

def hexagonal(n):
    return n*(2*n-1)

triangles = set()
pentagonals = set()
hexagonals = set()

for i in range(1,100000):
    triangles.add(triangle(i))
    pentagonals.add(pentagonal(i))
    hexagonals.add(hexagonal(i))


print(triangles & pentagonals & hexagonals)
