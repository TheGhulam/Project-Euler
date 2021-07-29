from math import log, ceil


# Using "Sieve of Erathosthenes"
def sieve(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False


def upper_bound_for_p_n(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


def find_n_prime(n):
    primes = list(sieve(upper_bound_for_p_n(n)))
    return primes[n-1]


if __name__ == "__main__":
    print(find_n_prime(10001))
