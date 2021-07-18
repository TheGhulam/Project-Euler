#! /usr/bin/env python
# https://projecteuler.net/problem=55

def is_lychrel(n):
    """
    Checks if given number is lychrel or not
    """
    for _ in range(50):
        n = n + int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True


# def is_palindrome(n):
#     return n == int(str(n)[::-1])
#
#
# def rev_and_add(n):
#     return n + int(str(n)[::-1])
#
#
# def is_lychrel_recursive(n, times=0):
#     """
#     Checks if given number is lychrel or not recursively
#     """
#     times += 1
#     if is_palindrome(rev_and_add(n)):
#         return False
#     elif times == 50:
#         return True
#     else:
#         return is_lychrel_recursive(rev_and_add(n), times=times)


def main():
    count = 0
    for i in range(1, 10001):
        if is_lychrel(i):
            count += 1
    return count


if __name__ == "__main__":
    print(main())
