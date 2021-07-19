# https://projecteuler.net/problem=16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

number = 2**1000

def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

if __name__ == "__main__":
    print(sum_of_digits(number))
