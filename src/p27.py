import time
import math

start = time.time()

def isPrime(n):
    if n in {2, 3, 5, 7}:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n % 3 == 0 or n % 5 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
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
