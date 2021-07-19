from math import factorial

gridPoints = 20

def ncr(n, r):
    '''
    returns binomial coefficient of n,r
    '''
    return factorial(n)/(factorial(r)*factorial(n-r))

# Number of lattice points from (0, 0) to (a,b) is given by binomial coefficient
# C(a+b,a)

print('Number of lattice points is: ' + str(ncr(gridPoints+gridPoints, gridPoints)))


# SO solution using memoization

def memoize(f):
    f.cache = {}
    def _f(*args, **kwargs):
        if args not in f.cache:
            f.cache[args] = f(*args, **kwargs)
        return f.cache[args]
    return _f

@memoize
def search(node):
    x, y = node
    if x <= 0 or y <= 0:
        return 1
    return search((x-1, y)) + search((x,y-1))


if __name__ == "__main__":
    print(search((20,20)))
