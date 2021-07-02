def pandigital(n, p):
    s = ''
    for i in range(1, p+1):
        s += str(n * i)
    return s

def ispandigital(n):
    for d in range(1, 10):
        if str(d) not in str(n):
            return False
    return True

def main():
    m = 0
    for i in range(10000):
        # Upper bound 3 found through trial and error
        for j in range(1, 3):
            p = pandigital(i, j)
            if ispandigital(p) and (len(p) == 9):
                if int(p) > int(m):
                    m = p
    return m


if __name__ == "__main__":
    print(main())

