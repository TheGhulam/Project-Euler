from p7 import sieve

def isNpandigital(n):
    nums = [str(i) for i in range(1, len(str(n))+1)]
    for i in str(n):
        if i in nums:
            nums.remove(i)
    if len(nums) > 0:
        return False
    return len(str(n))

def main():
    m = n = 0
    for i in sieve(100000000):
        p = isNpandigital(i)
        if p > m:
            m = p
            n = i
        elif (p == m ) and (i > n):
            n = i
    return (m, n)


if __name__ == "__main__":
    print(main())
