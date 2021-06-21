'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
'''
Solution based on long division:

        0.0675
       --------
   74 ) 5.00000
        4.44
          560
          518
           420
           370
            500
'''

def repeatingSequenceOfFraction(n, d):
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
        m = len(repeatingSequenceOfFraction(1, i))
        if m > s:
            s = m
            ind = i
    return ind

if __name__ == "__main__":
    print(main())
