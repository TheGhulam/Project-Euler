'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from funcs import sieve

def sum_of_primes_below(limit):
    sum = 0
    for i in sieve(limit):
        sum += i

    return sum


if __name__ == "__main__":
    print(sum_of_primes_below(2000000))
