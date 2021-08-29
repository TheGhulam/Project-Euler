#! /usr/bin/env python

from math import factorial


def sum_of_factorial_of_digits(n):
    return sum([factorial(int(d)) for d in str(n)])


def factorial_change_counter(n):
    chain = []
    for i in range(60):
        factorial = sum_of_factorial_of_digits(n)
        if factorial in chain:
            return i + 1
        chain.append(factorial)
        n = factorial


def p74():
    required_numbers = 0
    for i in range(1000_000):
        if factorial_change_counter(i) == 60:
            required_numbers += 1
    print(required_numbers)


if __name__ == "__main__":
    p74()
