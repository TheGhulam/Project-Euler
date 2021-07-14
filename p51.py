#! /usr/bin/env python
# https://projecteuler.net/problem=51
import re
from time import time
from funcs import isPrime

start = time()


def sortedDigitsList(n):
    """
    convert a number to a sorted digits list
    """
    return [int(d) for d in sorted(list(str(n)))]


def getXDigitSmallestPrime(numOfDigits, numOfPrimes):
    """
    get smallest prime with such property
    """
    for n in range(10 ** (numOfDigits - 1), 10 ** numOfDigits):
        primes = []
        if isPrime(n):
            primes.append(n)
            digits_list = sortedDigitsList(n)
            same_digit = digits_list[0]
            for i in range(same_digit + 1, 10):
                rex = re.compile(str(same_digit))
                ns = rex.sub(str(i), str(n))  # Substitute same_digit with i
                if isPrime(int(ns)):
                    primes.append(int(ns))
        if len(primes) == numOfPrimes:
            return primes[0]
        else:
            primes.clear()
    return 0


def main():
    assert 13 == getXDigitSmallestPrime(2, 6)
    assert 56003 == getXDigitSmallestPrime(5, 7)

    print(getXDigitSmallestPrime(6, 8))  # T&E
    print(f"Time taken: {time()-start}")


if __name__ == "__main__":
    main()
