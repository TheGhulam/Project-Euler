import math
import sys


def is_amicable(n):
    divisors_a = [i for i in no_of_divisiors_less_than(n)]
    s_a = sum(divisors_a)
    divisors_b = [i for i in no_of_divisiors_less_than(s_a)]
    s_b = sum(divisors_b)
    if s_b == n and n != s_a:
        return True


def no_of_divisiors_less_than(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors[1:]):
        yield divisor

def main(n):
    amicables = []
    for i in range(n):
        if is_amicable(i):
            amicables.append(i)
    # print(amicables)
    return sum(amicables)

if __name__ == "__main__":
    # print(is_amicable(int(sys.argv[1])))
    print(main(10000+1))
