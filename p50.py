#! /usr/bin/env python
from funcs import sieve


def main(limit):
    primes = list(sieve(limit))

    length = 0  # Length of the consecutive prime sum
    largest = 0  # Value of the consecutive primes sum
    maxj = len(primes)

    for i in range(len(primes)):
        for j in range(i+length, maxj):
            s = sum(primes[i:j])
            if s < limit:
                if s in primes:
                    length = j - i
                    largest = s
            else:
                maxj = j + 1
                break

    print(largest)


if __name__ == "__main__":
    main(1000000)
