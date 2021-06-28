from functools import lru_cache


@lru_cache(100)
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

def curious(n):
    s = sum([factorial(int(i)) for i in str(n)])
    if s == n:
        return True

print(f'Curious 145 = {curious(145)}')

if __name__ == "__main__":
    s = 0
    for n in range(3, 1000000):
        if curious(n):
            s += n
    print(s)
