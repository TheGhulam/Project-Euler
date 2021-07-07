#! /usr/bin/env python
from itertools import permutations

def ZeroToNinePandigital(n):
    nums = [str(i) for i in range(0, 10)]
    for i in str(n):
        if i in nums:
            nums.remove(i)
    if len(nums) > 0:
        return False
    return True

def property(s):
    d = [2, 3, 5, 7, 11, 13, 17]
    flag = True
    for i in range(1, 8):
        d1 = s[i]
        d2 = s[i+1]
        d3 = s[i+2]
        num = d1 + d2 + d3
        # print(int(num) / d[i-1])
        if int(num) % d[i-1] != 0:
            flag = False
    return flag



def main():
    s = 0
    for p in permutations('1234567890'): #Figured out this cool looping idea
        i = int(''.join(p))
        if ZeroToNinePandigital(i):
            if property(str(i)):
                print(i)
                s += i
    print(s)


if __name__ == "__main__":
    main()


