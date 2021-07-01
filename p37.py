from p7 import sieve
import time

start = time.time()

primes = set(sieve(100))

def isPrime(n):
    if n in {2, 3, 5, 7}:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n%3 == 0 or n%5 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6
    return True


def truncs(n):
    yield n
    n_str = str(n)
    for k in range(1, len(n_str)):
        yield int(n_str[k:])
        yield int(n_str[:-k])

def check(n):
    for t in truncs(n):
        if not isPrime(t):
            return False
    return True

c = s = 0
# Ignoring single digit primes
i = 11
while c < 11:
    if check(i):
        c += 1
        s += i
        print(i)
    i += 2

print('sum', s)

print(f'Time taken: {time.time() - start:.4}')
