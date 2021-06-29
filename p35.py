from collections import deque

def sieve(limit):
    nums = [True] * (limit+1)
    nums[0] = nums[1] = False

    for i, is_prime in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i*i, limit+1, i):
                nums[n] = False

def rotations(n):
    l = deque(list(str(n)))
    r = []

    for _ in range(len(l)):
        r.append(int("".join(list(l))))
        l.rotate()
    return r

def main(n):
    cp = []
    s = list(sieve(n))
    for i in s:
        r = rotations(i)
        flags = [False] * len(r)
        for k, j in enumerate(r):
            if j in s:
                flags[k] = True
        if all(flags):
            print(i)
            cp.append(i)
    return len(cp)


print(main(1000000))
