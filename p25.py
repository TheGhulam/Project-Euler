from functools import lru_cache

@lru_cache(100)
def fibonacci(i):
    if i == 1 or i == 0:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)

i = 0
while len(str(fibonacci(i))) != 1000:
    i += 1
print(i+1) # As need index starting from 1
