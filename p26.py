def fractionToDecimal(n, d):
    '''
    Returns repeating sequence of a fraction.
    If sequence doesn't exist returns empty string
    '''
    res = ""
    mp = {}
    rem = n % d

    while ((rem != 0) and (rem not in mp)):
        mp[rem] = len(res)
        rem = rem * 10
        res_part = rem // d
        res += str(res_part)
        rem %= d

    if (rem == 0):
        return ""
    else:
        return res[mp[rem]:]

def main():
    s, ind = 0, 0
    for i in range(1, 1000):
        m = len(fractionToDecimal(1, i))
        if m > s:
            s = m
            ind = i
    return ind

if __name__ == "__main__":
    print(main())
