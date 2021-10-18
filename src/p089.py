#! /usr/bin/env python


def romanToDecimal(n):
    """
    Takes in a Roman numeral and returns the decimal form of the number
    """

    values = {
            "I": 1,
            "V": 5,
            "X": 10,
            }
    s = 0
    for char in n:
        s += values[char]

    return s


print(romanToDecimal("IIIII"))
print(romanToDecimal("XVI"))
print(romanToDecimal("VVVI"))
print(romanToDecimal("VVIIIIII"))


