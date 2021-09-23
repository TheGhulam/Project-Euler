#! /usr/bin/env python

with open('../data/p079_keylog.txt', 'r') as f:
    logins = []
    for line in f:
        logins.append(line.strip())
    logins = list(set(logins))

def digits_sorter(digit, logins):
    digits = set()
    for l in logins:
        if digit in l:
            for d in l:
                if d == digit:
                    break
                else:
                    digits.add(digit)
    return digits

def main():
    digit_1 = set()
    digit_2 = set()
    digit_3 = set()
    for login in logins:
        digit_1.add(login[0])
        digit_2.add(login[1])
        digit_3.add(login[2])

    print(digit_1)
    print(digit_2)
    print(digit_3)

    print(digit_1 | digit_2 | digit_3)

    print(digits)


if __name__ == "__main__":
    main()
