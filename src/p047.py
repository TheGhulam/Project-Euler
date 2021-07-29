#! /usr/bin/env python


def distinctPrimeFactors(n):
    primes = set()
    while n % 2 == 0:
        primes.add(2)
        n /= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            primes.add(i)
            n /= i
    if n > 2:
        primes.add(n)
    return primes


def main(nums):
    found = False
    i = 1
    while not found:
        correct = 0
        for j in range(i, i + nums):
            if len(distinctPrimeFactors(j)) == nums:
                correct += 1
        if correct == nums:
            print(f"Found it: {i}")
            found = True
        i += 1


if __name__ == "__main__":
    main(4)
