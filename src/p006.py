import sys


def sum_of_square(n):
    return ((n)*(n+1)*(2*n+1))/6

def square_of_sum(n):
    return ((n*(n+1))/2)**2

if __name__ == '__main__':
    num = int(sys.argv[1])
    print(square_of_sum(num)-sum_of_square(num))
