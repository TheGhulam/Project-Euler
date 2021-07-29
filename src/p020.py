from functools import lru_cache

@lru_cache(100)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_digits(n):
    s = 0
    for n in str(n):
        s += int(n)
    return s

if __name__ == "__main__":
    # print(sum_of_digits(factorial(10)))
    print(sum_of_digits(factorial(100)))

