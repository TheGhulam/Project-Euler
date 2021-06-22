import time
import math

start = time.time()

def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    for i in range(3, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

primes = []

for i in range(1000):
    if isPrime(i):
        primes.append(i)

longest, largestA, largestB = 0, 0, 0

for a in range(-1000, 1000):
    for b in primes:
        n = 0
        term = n ** 2 + a * n + b

        while isPrime(term):
            term = n ** 2 + a * n + b
            n += 1

        if n > longest:
            longest, largestA, largestB = n, a, b

print(largestA * largestB)

print("Elapsed time: ", time.time() - start, "sec")
